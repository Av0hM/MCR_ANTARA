import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from validate_corrected_ditl import *
for sc in SCENARIOS:
 p=OUT/(sc+'_summary.json')
 if not p.exists():continue
 s=json.loads(p.read_text());r=selected(sc,verify=False);paths={x['kind']:ROOT/x['path'] for x in r['files']};tr=read(paths['mode_transitions']);f=pd.read_csv(paths['telemetry'],usecols=['time_sec','mode','battery_wh'])
 mode=f['mode'].iloc[0];last=0.;occ=defaultdict(float);er=[];chain=0
 for x in tr.itertuples():
  chain+=int(mode!=x.from_mode);occ[mode]+=x.time_sec-last
  if mode=='RELAY' and x.time_sec>last:er.append((last,x.time_sec))
  last=x.time_sec;mode=x.to_mode
 occ[mode]+=s['duration_s']-last
 if mode=='RELAY':er.append((last,s['duration_s']))
 changed=f['mode']!=f['mode'].shift();actual=f.loc[changed].iloc[1:]
 same=list(actual['mode'])==list(tr.to_mode)
 s['event_mode_seconds']=dict(occ);s['transition_chain_errors']=chain;s['transition_mode_sequence_match']=same
 s['transition_offset_range_s']=[float((actual.time_sec.to_numpy()-tr.time_sec.to_numpy()).min()),float((actual.time_sec.to_numpy()-tr.time_sec.to_numpy()).max())] if same else None
 c=read(paths['gs_contacts']);ew=intersect(list(zip(c.aos_time_sec,c.los_time_sec)),er)
 s['event_mode_relay_contact_overlap_s']=sum(b-a for a,b in ew);s['event_mode_relay_capacity_bytes']=sum(capacity(b-a) for a,b in ew)
 s['sample_vs_event_mode_scope']='Both interval conventions reported; row mode changes can lag transition timestamps. Do not silently substitute event mode into row-level acquisition.'
 delta=np.diff(f.battery_wh.to_numpy())
 s['recorded_battery_increase_wh']=float(delta[delta>0].sum());s['recorded_battery_decrease_wh']=float(-delta[delta<0].sum())
 s['battery_change_scope']='Adjacent recorded states only; charge throughput and curtailment UNKNOWN'
 dump(p,s)

a=pd.read_csv(ROOT/'evidence/new-science-ditl/leop_24h_ANTARA_Science_telemetry.csv',usecols=['time_sec','lat_deg','lon_deg','alt_km'])
b=pd.read_csv(ROOT/'evidence/new-science-ditl/no_leop_24h_ANTARA_Science_telemetry.csv',usecols=a.columns)
c=a.merge(b,on='time_sec',suffixes=('_leop','_no_leop'))
dump(OUT/'scenario_comparability.json',dict(classification='SENSITIVITY ONLY: runtime manifests unavailable',common_timestamp_rows=len(c),max_coordinate_absolute_differences={k:float(abs(c[k+'_leop']-c[k+'_no_leop']).max()) for k in ['lat_deg','lon_deg','alt_km']},unknown_parameters=['RAAN','inclination','mass','payload response revision','integrator','mask','battery capacity','control parameters'],cadence_day_s=[2,20],cadence_annual_s=[2,50,60]))
