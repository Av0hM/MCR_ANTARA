"""Read-only evidence analysis; no orbit propagation or invented detector counts."""
from pathlib import Path
import csv, json, hashlib, math
from datetime import datetime, timedelta, timezone
import numpy as np
import pandas as pd
from science_record_v3 import capacity, intersect, backlog, cell_key, readings
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data/derived/telemetry_v3_2026-11-09'
RAW=ROOT/'evidence/science_ditl/raw'

def dump(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')
def csvout(name,rows):
    if rows:
        with (OUT/name).open('w') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def hashfile(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
    return h.hexdigest()
def append_window(w,a,b):
    if w and w[-1][1]==a:w[-1]=(w[-1][0],b)
    else:w.append((a,b))
def daily(windows,days):
    out=np.zeros(days)
    for a,b in windows:
        for d in range(int(a//86400),min(days,int((b-1e-9)//86400)+1)):
            out[d]+=max(0,min(b,(d+1)*86400)-max(a,d*86400))
    return out

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    paths=[RAW/f'leop_1yr_ANTARA_Science_{n}.csv' for n in ['gs_contacts','mode_transitions','telemetry']]
    paths += [ROOT/'evidence/geometric_factor_2026-11-05'/n for n in ['cell_pass_counts.csv','cell_proton_rates.csv']]
    paths += [RAW/f'{run}_ANTARA_Science_gs_contacts.csv' for run in ['leop_24h','no_leop_24h']]
    paths += [ROOT/'config/science/science_record_v3.json',ROOT/'config/science/science_record_v3.schema.json',ROOT/'scripts/science_record_v3.py',ROOT/'scripts/complete_telemetry_budget.py',ROOT/'scripts/plot_telemetry_budget.py',Path(__file__)]
    dump('source_inventory.json',[dict(path=str(p.relative_to(ROOT)),sha256=hashfile(p),bytes=p.stat().st_size) for p in paths])
    grid=pd.read_csv(paths[3]);keys=['lon_min_deg','lat_min_deg']
    assert not grid.duplicated(keys).any() and len(grid)==7940
    rates=pd.read_csv(paths[4],usecols=keys)
    assert set(map(tuple,grid[keys].values))==set(map(tuple,rates[keys].values))
    visits=int(grid.pass_count.sum());dwell=float(grid.time_seconds.sum())
    dump('grid_sensitivity.json',dict(cells=len(grid),visits=visits,geometric_dwell_s=dwell,horizon='UNKNOWN',
        bytes_per_reading=292,volume=[dict(readings=n,records=n*visits,bytes=n*visits*292) for n in [1,2,3]],
        coarsening='Visit counts cannot be summed to obtain unique 1 or 5 degree visits without trajectory chronology.'))
    c=pd.read_csv(paths[0]);assert not c.duplicated(['aos_time_sec','los_time_sec','station']).any()
    windows=list(zip(c.aos_time_sec,c.los_time_sec))
    assert all(abs((b-a)-d)<1e-9 for (a,b),d in zip(windows,c.duration_sec))
    assert all(windows[i][1]<=windows[i+1][0] for i in range(len(windows)-1))
    epochs=set()
    for row in c.itertuples():
        a=datetime.fromisoformat(row.aos_time.replace('Z','+00:00'));b=datetime.fromisoformat(row.los_time.replace('Z','+00:00'))
        assert (b-a).total_seconds()==row.duration_sec
        epochs.add((a-timedelta(seconds=row.aos_time_sec)).isoformat())
        epochs.add((b-timedelta(seconds=row.los_time_sec)).isoformat())
    trans=pd.read_csv(paths[1]);relay=[];mode='COLD_AND_DARK';last=0;chain_errors=0
    for row in trans.itertuples():
        assert row.time_sec>=last
        chain_errors+=int(row.from_mode!=mode)
        if mode=='RELAY' and row.time_sec>last: append_window(relay,last,row.time_sec)
        mode=row.to_mode;last=row.time_sec
    # Tail beyond last transition is unknown; contacts after it excluded from certified overlap.
    eligible=intersect(windows,relay)
    cd=daily(windows,365);ed=daily(eligible,365)
    rows=[]
    for i,((a,b),row) in enumerate(zip(windows,c.itertuples())):
        ew=intersect([(a,b)],relay);sec=sum(y-x for x,y in ew)
        rows.append(dict(index=i,aos_utc=row.aos_time,los_utc=row.los_time,aos_s=a,los_s=b,
          visibility_s=b-a,relay_overlap_s=sec,visibility_capacity_bytes=capacity(b-a),
          relay_capacity_bytes=sum(capacity(y-x) for x,y in ew),recorded_transfer_source_mb=row.downlinked_mb,
          queue_before_bytes='UNKNOWN: no matched v3 generation',v3_transferred_bytes='UNKNOWN',
          backlog_after_bytes='UNKNOWN',unused_v3_capacity_bytes='UNKNOWN',mask='UNKNOWN runtime; candidate Science default 15 degrees'))
    csvout('historical_contacts.csv',rows)
    csvout('historical_daily_capacity.csv',[dict(day=d,visibility_s=float(cd[d]),relay_s=float(ed[d]),
        visibility_bytes=capacity(cd[d]),relay_bytes=capacity(ed[d])) for d in range(365)])
    gs=dict(contacts=len(c),epochs=sorted(epochs),station_labels=sorted(set(c.station)),
        horizon='365-day accounting window inferred from elapsed event extent, not completion proof',
        duration_s=float(cd.sum()),mean_daily_s=float(cd.mean()),minimum_daily_s=float(cd.min()),
        max_daily_s=float(cd.max()),max_intercontact_gap_s=max(windows[i+1][0]-windows[i][1] for i in range(len(windows)-1)),
        first_contact_s=windows[0][0],last_contact_end_s=windows[-1][1],
        visibility_capacity_bytes=int(sum(r['visibility_capacity_bytes'] for r in rows)),
        mean_daily_visibility_capacity_bytes=float(cd.mean()*2400),minimum_daily_visibility_capacity_bytes=capacity(cd.min()),
        relay_overlap_s=sum(b-a for a,b in eligible),relay_capacity_bytes=sum(capacity(b-a) for a,b in eligible),
        minimum_daily_relay_s=float(ed.min()),mean_daily_relay_s=float(ed.mean()),
        recorded_transfer_source_mb=float(c.downlinked_mb.sum()),transition_chain_errors=chain_errors,
        runtime_mask='UNKNOWN; current source default 15 degrees; no second mask correction',
        short_contact_logs={run:'EMPTY (one newline); not full-day evidence' for run in ['leop_24h','no_leop_24h']})
    dump('gs_summary.json',gs)
    # Stream all partial-annual rows, retaining only interval/cell accounting and gate segments.
    cols=['time_sec','state_time_sec','interval_duration_sec','mode','in_saa','gs_visible','science_generation_enabled','relay_link_active','lat_deg','lon_deg']
    tiers={name:dict(resolution=res,geometric_visits=0,geometric_cells=set(),science_visit_ids=set(),prev=None,segments=[],current=None) for name,res in [('MMSC',5.),('MSC',1.),('EMSC',.5)]}
    vis=[];telrelay=[];active=[];end=0;rows_count=0;gate_s=0
    for ch in pd.read_csv(paths[2],usecols=cols,chunksize=50000):
        # pandas recognizes True/False; refuse arbitrary string truthiness.
        for col in ['in_saa','gs_visible','science_generation_enabled','relay_link_active']:
            assert ch[col].dtype==bool
        for row in ch.itertuples(index=False):
            a=row.time_sec;b=row.state_time_sec;dt=row.interval_duration_sec
            assert a==end and b-a==dt and dt>0
            end=b;rows_count+=1
            if row.gs_visible: append_window(vis,a,b)
            if row.gs_visible and row.mode=='RELAY':append_window(telrelay,a,b)
            if row.relay_link_active:append_window(active,a,b)
            gate=bool(row.science_generation_enabled)
            if gate: assert row.in_saa and row.mode=='DETECTION';gate_s+=dt
            for tier,t in tiers.items():
                key=cell_key(row.lat_deg,row.lon_deg,t['resolution']) if row.in_saa else None
                if key is not None:
                    t['geometric_cells'].add(key);t['geometric_visits']+=int(key!=t['prev'])
                t['prev']=key
                cur=t['current']
                if gate:
                    t['science_visit_ids'].add(t['geometric_visits'])
                    if cur and cur['end_s']==a and cur['cell']==key: cur['end_s']=b
                    else:
                        if cur:t['segments'].append(cur)
                        t['current']=dict(start_s=a,end_s=b,cell=key,visit_id=t['geometric_visits'])
                elif cur:t['segments'].append(cur);t['current']=None
    outtiers=[];budgets=[];sens=[]
    for tier,t in tiers.items():
        if t['current']:t['segments'].append(t['current'])
        # Acquisition segments can split one geometric visit on a mode/gate change.
        csvout(f'{tier}_acquisition_segments.csv',t['segments'])
        groups={}
        for seg in t['segments']:groups.setdefault(seg['visit_id'],[]).append(seg)
        for n in [1,2,3]:
            gen=[]
            for segments in groups.values():
                allocations=[1]*len(segments)
                # Every interrupted acquisition requires a distinct exposure interval.
                # Do not discard exposure or falsely bridge a shutdown to meet a count target.
                target=max(n,len(segments))
                while sum(allocations)<target:
                    j=max(range(len(segments)),key=lambda i:(segments[i]['end_s']-segments[i]['start_s'])/allocations[i])
                    allocations[j]+=1
                for seg,partitions in zip(segments,allocations):
                    a=round(seg['start_s']*1e6);b=round(seg['end_s']*1e6)
                    bounds=sorted(set(a+(b-a)*i//partitions for i in range(1,partitions)))
                    for x,y in readings(a,b,bounds,partitions):gen.append((y/1e6,292))
            gen.sort()
            daybytes={}
            for time,size in gen:daybytes[int(time//86400)]=daybytes.get(int(time//86400),0)+size
            q=backlog(gen,telrelay);label=f'{tier}_{n}'
            csvout(label+'_releases.csv',[dict(time_s=a,bytes=b) for a,b in gen])
            csvout(label+'_queue.csv',q.pop('contacts'))
            outtiers.append(dict(tier=tier,resolution_deg=t['resolution'],geometric_visits=t['geometric_visits'],
                geometric_cells=len(t['geometric_cells']),science_enabled_visits=len(t['science_visit_ids']),acquisition_segments=len(t['segments']),preferred_readings_per_visit=n,
                exposure_s=gate_s,records=len(gen),bytes=q['generated_bytes'],mean_bytes_per_elapsed_day=q['generated_bytes']/(end/86400),
                max_calendar_day_bytes=max(daybytes.values(),default=0),max_one_second_records=max([sum(1 for x,_ in gen if int(x)==int(v)) for v,_ in gen],default=0),peak_records_per_release_timestamp=max([sum(1 for x,_ in gen if x==v) for v,_ in gen],default=0),
                status='legacy-gate/sample-cell ideal partition; interrupted exposure imposes fragmentation floor; not verified science records'))
            budgets.append(dict(case=label,aggregate_balance_lower_bound_bps=q['generated_bytes']*8/sum(b-a for a,b in telrelay),**q))
            worstmiss=0
            for i in range(len(telrelay)):
                miss=backlog(gen,telrelay[:i]+telrelay[i+1:]);worstmiss=max(worstmiss,miss['peak_required_bytes'])
            sens.append(dict(case=label,outage='one missed eligible relay window',peak_required_bytes=worstmiss))
            worst_contact=0
            for lo,hi in vis:
                retained=[(a,b) for a,b in telrelay if b<=lo or a>=hi]
                worst_contact=max(worst_contact,backlog(gen,retained)['peak_required_bytes'])
            sens.append(dict(case=label,outage='one missed complete visibility contact (all Relay fragments)',peak_required_bytes=worst_contact))
            for days in [1,3,7]:
                worst=0
                for d in range(math.ceil(end/86400)):
                    outage=[(d*86400,(d+days)*86400)]
                    rem=[]
                    for a,b in telrelay:
                        lo,hi=outage[0]
                        if b<=lo or a>=hi:rem.append((a,b))
                        else:
                            if a<lo:rem.append((a,lo))
                            if b>hi:rem.append((hi,b))
                    worst=max(worst,backlog(gen,rem)['peak_required_bytes'])
                sens.append(dict(case=label,outage=f'{days} calendar day(s), worst start day',peak_required_bytes=worst))
    csvout('tier_generation.csv',outtiers);dump('bounded_backlog.json',budgets);csvout('outage_sensitivity.csv',sens)
    dump('telemetry_window_summary.json',dict(rows=rows_count,horizon_s=end,epoch='UNKNOWN for telemetry; not inherited from conflicting events',
        gate_s=gate_s,visibility_s=sum(b-a for a,b in vis),relay_visibility_s=sum(b-a for a,b in telrelay),
        relay_capacity_bytes=sum(capacity(b-a) for a,b in telrelay),recorded_link_active_s=sum(b-a for a,b in active),
        timing_policy='Equal ideal subdivisions; hardware boundaries unverified. No minimum exposure or count threshold.',
        geometric_boundary='Sample-owned cells; exact crossing times unavailable; exposure conserved across intervals.',
        sustainable_rate_bps='NOT established by incomplete mixed-source artifacts'))
    dump('memory.json',dict(record_bytes=292,uint16_record_bytes=164,ram_bytes=262144,ram_record_slots=262144//292,
        ram_remainder_bytes=262144%292,flash_bytes=134217728,flash_record_slots=134217728//292,
        archival_usable_bytes=16000000000,archival_record_slots=16000000000//292,
        assembly_buffer_bytes=292,ping_pong_histograms_bytes=512,combined_fixture_working_bytes=804,
        caveat='804 bytes excludes stack/DMA/queue pointers/RTOS/ECC/filesystem/metadata and other subsystems; not total OBC RAM.'))
    print(json.dumps(dict(gs=gs,telemetry_tiers=outtiers,memory=json.loads((OUT/'memory.json').read_text())),indent=2))

if __name__=='__main__':main()
