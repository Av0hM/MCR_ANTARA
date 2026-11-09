"""Preliminary v3 codec and deterministic accounting fixtures; not flight software."""
import binascii
import math
import struct
from bisect import bisect_right

MODES = {'COLD_AND_DARK': 0, 'DETUMBLE': 1, 'SUN_POINTING': 2,
         'DETECTION': 3, 'RELAY': 4, 'SLEWING': 5, 'SAFE': 6, 'UNKNOWN': 15}
HEALTH = ('obc', 'eps', 'adcs', 'comms', 'payload', 'other_thermal')
BODY = struct.Struct('<QQiii64IIH')
SIZE = BODY.size + 2


def integer(x, lo, hi):
    if type(x) is not int or not lo <= x <= hi:
        raise ValueError('Integer out of range')
    return x


def status_marker(mode, health):
    if mode not in MODES or set(health) != set(HEALTH):
        raise ValueError('Explicit mode and six health codes required')
    return MODES[mode] | sum(integer(health[k], 0, 3) << (4+2*i) for i,k in enumerate(HEALTH))


def decode_status(word):
    integer(word, 0, 65535)
    mode = word & 15
    if mode not in MODES.values():
        raise ValueError('Reserved mode code')
    return dict(mode=next(k for k,v in MODES.items() if v == mode),
                health={k:(word >> (4+2*i)) & 3 for i,k in enumerate(HEALTH)})


def validate_record(r):
    for k in ('entry_us','exit_us'): integer(r[k],0,2**64-1)
    if r['exit_us'] <= r['entry_us']: raise ValueError('Positive half-open exposure required')
    integer(r['lat_e7'],-900000000,900000000)
    integer(r['lon_e7'],-1800000000,1799999999)
    integer(r['alt_mm'],-2**31,2**31-1)
    integer(r['sequence'],0,2**32-1)
    decode_status(r['status'])
    if len(r['histogram']) != 64: raise ValueError('64 bins required')
    for n in r['histogram']: integer(n,0,2**32-1)


def encode(r):
    validate_record(r)
    body = BODY.pack(r['entry_us'],r['exit_us'],r['lat_e7'],r['lon_e7'],r['alt_mm'],
                     *r['histogram'],r['sequence'],r['status'])
    return body + struct.pack('<H', binascii.crc_hqx(body, 0xffff))


def decode(data):
    if len(data) != SIZE: raise ValueError('Wrong record size')
    if binascii.crc_hqx(data[:-2],0xffff) != struct.unpack('<H',data[-2:])[0]:
        raise ValueError('CRC mismatch')
    v=BODY.unpack(data[:-2])
    r=dict(entry_us=v[0],exit_us=v[1],lat_e7=v[2],lon_e7=v[3],alt_mm=v[4],
           histogram=list(v[5:69]),sequence=v[69],status=v[70])
    validate_record(r)
    return r


def fits_uint16(histogram):
    if len(histogram)!=64: raise ValueError('64 bins required')
    for x in histogram: integer(x,0,2**32-1)
    return max(histogram) <= 65535


def cell_key(lat,lon,resolution):
    if not all(math.isfinite(x) for x in (lat,lon,resolution)) or not -90 <= lat < 90 or resolution<=0:
        raise ValueError('Invalid coordinate/grid')
    return (math.floor((lat+90)/resolution),math.floor((((lon+180)%360)-180+180)/resolution))


def readings(start_us,end_us,available_boundaries_us,preferred=3):
    """Partition using supplied realizable boundaries; no minimum duration/count.

    Boundaries come from acquisition hardware or an explicitly ideal fixture.
    All valid exposure is retained, including zero-count and short intervals.
    Caller closes a segment at each cell/mode/shutdown boundary. This is offline
    partitioning; flight implementation requires accumulation banks/timestamps.
    """
    integer(start_us,0,2**64-1);integer(end_us,start_us,2**64-1)
    integer(preferred,1,3)
    if end_us==start_us: return []
    if available_boundaries_us is None: raise ValueError('Acquisition boundaries unknown')
    for t in available_boundaries_us: integer(t,start_us,end_us)
    if list(available_boundaries_us)!=sorted(set(available_boundaries_us)):
        raise ValueError('Boundaries must be unique and sorted')
    inside=[t for t in available_boundaries_us if start_us<t<end_us]
    n=min(preferred,1+len(inside))
    chosen=[]
    for i in range(1,n):
        remaining=[t for t in inside if t not in chosen]
        target=start_us+(end_us-start_us)*i/n
        chosen.append(min(remaining,key=lambda t:abs(t-target)))
    edges=[start_us]+sorted(chosen)+[end_us]
    return list(zip(edges,edges[1:]))


def poisson_fraction(total_counts):
    integer(total_counts,0,2**63-1)
    return None if total_counts==0 else 1/math.sqrt(total_counts)


def assign_events(event_times_us,event_bins,intervals):
    """Events at a boundary belong only to the next half-open interval."""
    if len(event_times_us)!=len(event_bins): raise ValueError('Mismatched events')
    validate_windows(intervals)
    out=[[0]*64 for _ in intervals];starts=[a for a,b in intervals]
    for t,k in zip(event_times_us,event_bins):
        integer(t,0,2**64-1);integer(k,0,63)
        i=bisect_right(starts,t)-1
        if i<0 or t>=intervals[i][1]: raise ValueError('Event outside exposure')
        out[i][k]+=1
    return out


def validate_windows(windows):
    end=-math.inf
    for a,b in windows:
        if not math.isfinite(a+b) or a<0 or b<=a or a<end:
            raise ValueError('Invalid, overlapping or unsorted windows')
        end=b
    return windows


def intersect(a,b):
    validate_windows(a);validate_windows(b)
    out=[];i=j=0
    while i<len(a) and j<len(b):
        lo=max(a[i][0],b[j][0]);hi=min(a[i][1],b[j][1])
        if hi>lo: out.append((lo,hi))
        if a[i][1] <= b[j][1]: i+=1
        else: j+=1
    return out


def capacity(seconds,bitrate=19200):
    if not math.isfinite(seconds) or seconds<0 or not math.isfinite(bitrate) or bitrate<=0:
        raise ValueError('Invalid link inputs')
    return math.floor(bitrate*seconds/8)


def backlog(generation,eligible_windows,storage_bytes=None,bitrate=19200):
    """FIFO byte stream, initially empty, pausable across contacts, no framing.

    generation=(time_s,bytes); availability occurs at interval completion.
    Eligible windows MUST already include visibility AND Relay gates.
    No mask or efficiency is applied here. Fractional bytes are held internally
    until the end of a service segment; inputs in this study are integer seconds.
    """
    validate_windows(eligible_windows)
    if storage_bytes is not None: integer(storage_bytes,0,2**63-1)
    capacity(0,bitrate)
    last=-1
    for t,n in generation:
        if not math.isfinite(t) or t<last or t<0: raise ValueError('Generation order')
        integer(n,0,2**63-1);last=t
    q=peak=sent=lost=0;idx=0;rows=[]
    def add_until(t,service_start=None):
        nonlocal idx,q,peak,sent,lost
        cursor=service_start
        while idx<len(generation) and generation[idx][0]<=t:
            when,n=generation[idx]
            if cursor is not None:
                take=min(q,capacity(when-cursor,bitrate));q-=take;sent+=take;cursor=when
            q+=n;peak=max(peak,q)
            if storage_bytes is not None and q>storage_bytes:
                lost+=q-storage_bytes;q=storage_bytes
            idx+=1
        return cursor
    for a,b in eligible_windows:
        add_until(a);before=q;oldsent=sent
        cursor=add_until(b,a)
        take=min(q,capacity(b-cursor,bitrate));q-=take;sent+=take
        rows.append(dict(start_s=a,end_s=b,capacity_bytes=capacity(b-a,bitrate),
                         queue_before_bytes=before,transferred_bytes=sent-oldsent,
                         queue_after_bytes=q,unused_capacity_bytes=capacity(b-a,bitrate)-(sent-oldsent)))
    add_until(math.inf)
    total=sum(n for t,n in generation)
    assert total==q+sent+lost
    return dict(generated_bytes=total,transferred_bytes=sent,remaining_bytes=q,
                peak_required_bytes=peak,dropped_bytes=lost,contacts=rows)
