"""Bounded queue/serialization diagnostics on corrected summaries and ledgers."""
from validate_corrected_ditl import *
for sc in SCENARIOS:
 p=OUT/(sc+'_summary.json');s=json.loads(p.read_text())
 for q in s['queues']:
  case=q['case'];gen=[tuple(x) for x in pd.read_csv(OUT/(case+'_releases.csv')).itertuples(index=False,name=None)];gen=[(float(t),int(n)) for t,n in gen]
  ledger=pd.read_csv(OUT/(case+'_queue.csv'));w=list(zip(ledger.start_s,ledger.end_s))
  q['ram_overflow_bytes']=backlog(gen,w,storage_bytes=262144)['dropped_bytes'];q['flash_overflow_bytes']=backlog(gen,w,storage_bytes=134217728)['dropped_bytes']
  gaps=[(0,w[0][0])]+[(w[i][1],w[i+1][0]) for i in range(len(w)-1)]+[(w[-1][1],s['duration_s'])]
  a,b=max(gaps,key=lambda x:x[1]-x[0]);q['longest_no_service_interval_s']=[a,b];q['generated_during_longest_gap_bytes']=sum(n for t,n in gen if a<t<=b)
  if case.endswith('_3'):
   lo=0.001;hi=19200.
   for _ in range(24):
    mid=(lo+hi)/2
    if backlog(gen,w,bitrate=mid)['remaining_bytes']==0:hi=mid
    else:lo=mid
   q['minimum_bitrate_final_balance_bps']=hi;q['rate_ratio_19200_to_final_balance']=19200/hi
 p.write_text(json.dumps(s,indent=2)+'\n')
 print(sc,'queue completion done',flush=True)
