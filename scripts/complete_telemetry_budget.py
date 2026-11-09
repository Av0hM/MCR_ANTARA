"""Small derived sensitivity tables from the read-only telemetry extraction."""
raise RuntimeError("Superseded DITL outputs are read-only; use corrected run registry and analysis.")
import json,csv,math
from pathlib import Path
from science_record_v3 import backlog
D=Path(__file__).resolve().parents[1]/'data/derived/telemetry_v3_2026-11-09'
def read(n):return list(csv.DictReader((D/n).open()))
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
q=json.loads((D/'bounded_backlog.json').read_text())
for r in q:
    name=r['case'];gen=[(float(x['time_s']),int(x['bytes'])) for x in read(name+'_releases.csv')]
    w=[(float(x['start_s']),float(x['end_s'])) for x in read(name+'_queue.csv')]
    lo=1e-9;hi=19200.
    for _ in range(45):
        mid=(lo+hi)/2
        if backlog(gen,w,bitrate=mid)['remaining_bytes']==0:hi=mid
        else:lo=mid
    r['minimum_byte_balance_bitrate_bps']=hi;r['ideal_rate_ratio']=19200/hi
    r['largest_relay_gap_s']=max([w[i+1][0]-w[i][1] for i in range(len(w)-1)],default=0)
    r['zero_overflow_at_ram_allocation']=backlog(gen,w,storage_bytes=262144)['dropped_bytes']==0
    # A missed whole visibility contact can include several relay fragments.
    # Supplied partial telemetry fragments are treated as eligible windows here.
    gaps=[(w[i][1],w[i+1][0]) for i in range(len(w)-1)]
    worst=max(gaps,key=lambda p:p[1]-p[0]) if gaps else (0,0)
    r['generation_in_longest_relay_gap_bytes']=sum(n for t,n in gen if worst[0]<t<=worst[1])
dump('bounded_backlog.json',q)
g=json.loads((D/'grid_sensitivity.json').read_text())
for r in g['volume']:
    r['MiB']=r['bytes']/2**20;r['uint16_bytes_unapproved']=r['records']*164
    r['ideal_required_relay_seconds']=r['bytes']/2400
    r['exceeds_128MiB_without_delivery']=r['bytes']>128*2**20
    r['capacity_shortfall_bytes_without_delivery']=max(0,r['bytes']-128*2**20)
dump('grid_sensitivity.json',g)
print('Derived minimum bitrates and storage sensitivities complete')
