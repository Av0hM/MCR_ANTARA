"""Registry-selected corrected evidence audit; never runs a simulation.
Legacy telemetry has no interval endpoint columns. Left-held states on [t_i,t_i+1)
are a declared numerical interpretation, not a recovered integrator manifest.
"""
from pathlib import Path
import csv,hashlib,json,math
from collections import Counter,defaultdict
from datetime import datetime,timedelta
import numpy as np
import pandas as pd
try:
 from .science_record_v3 import backlog,cell_key,capacity,intersect
except ImportError:
 from science_record_v3 import backlog,cell_key,capacity,intersect
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data/derived/ditl_correction_2026-11-09'
REG=ROOT/'evidence/science-ditl/run_registry.json'
SCENARIOS=['leop_24h','no_leop_24h','leop_1yr']
KINDS=['telemetry','mode_transitions','saa_passes','proton_passes','gs_contacts','slew_events','detumble_events','rejected_transitions']
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
def dump(p,obj):
 Path(p).parent.mkdir(parents=True,exist_ok=True);Path(p).write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')
def read(p):
 return pd.read_csv(p) if Path(p).stat().st_size>1 else pd.DataFrame()
def selected(scenario,registry=None,verify=True):
 reg=registry or json.loads(REG.read_text());runs=[r for r in reg['runs'] if r['scenario']==scenario and r['authoritative_for_report']]
 if len(runs)!=1 or runs[0]['status']=='SUPERSEDED EVIDENCE':raise ValueError('Ambiguous or superseded run selection')
 r=runs[0]
 if verify:
  for f in r['files']:
   if sha(ROOT/f['path'])!=f['sha256']:raise ValueError('Source checksum mismatch')
 return r

def inventory():
 files=[];runs=[]
 for scenario in SCENARIOS:
  ff=[]
  for kind in KINDS:
   p=ROOT/'evidence/new-science-ditl'/f'{scenario}_ANTARA_Science_{kind}.csv'
   with p.open(newline='') as f:
    reader=csv.reader(f);headers=next(reader,[]);first=last=None;n=0
    for row in reader:
     if not row:continue
     if len(row)!=len(headers):raise ValueError(f'Malformed CSV {p}:{n+2}')
     if first is None:first=row
     last=row;n+=1
   stamps=[i for i,c in enumerate(headers) if c.endswith('time_sec') or c in ['aos_time','los_time','entry_time','exit_time']]
   item=dict(path=str(p.relative_to(ROOT)),sha256=sha(p),bytes=p.stat().st_size,rows=n,columns=headers,first_timestamps={headers[i]:first[i] for i in stamps} if first else {},last_timestamps={headers[i]:last[i] for i in stamps} if last else {},kind=kind)
   ff.append(item);files.append(item)
  runid='corrected_'+scenario+'_'+ff[0]['sha256'][:10]
  runs.append(dict(run_id=runid,scenario=scenario,source_directory='evidence/new-science-ditl',files=ff,epoch='UNKNOWN pending cross-file check',duration_s=float(ff[0]['last_timestamps']['time_sec']),configuration_identity='UNKNOWN: no runtime manifest supplied',status='CORRECTED AUTHORITATIVE CANDIDATE',authoritative_for_report=True,supersedes=['superseded_'+scenario],limitations='Authority is scoped to verified recorded quantities, not recovered physical configuration.'))
  old=[]
  for p in sorted((ROOT/'evidence/science_ditl/raw').glob(scenario+'_*.csv')):old.append(dict(path=str(p.relative_to(ROOT)),sha256=sha(p)))
  runs.append(dict(run_id='superseded_'+scenario,scenario=scenario,files=old,status='SUPERSEDED EVIDENCE',authoritative_for_report=False))
 dump(REG,dict(schema_version=1,runs=runs))
 dump(OUT/'inventory.json',files)
 # Dependencies are captured before report edits; preserve exact affected line text.
 deps=[]
 needles=['science_ditl','science-ditl','telemetry_v3_2026-11-09','50 days','50days','4320020','4\\,320\\,020','67452','67\\,452','428836800','428\\,836\\,800','incomplete annual','incomplete trace']
 for folder in ['sections','appendices','docs/audit','scripts','config/requirements']:
  for p in (ROOT/folder).rglob('*'):
   if p.suffix not in ['.tex','.md','.py','.json']:continue
   for i,line in enumerate(p.read_text().splitlines(),1):
    if any(n in line for n in needles):deps.append(dict(path=str(p.relative_to(ROOT)),line=i,text=line))
 dump(OUT/'initial_dependency_inventory.json',deps)
 lines=['# Corrected DITL evidence inventory','', 'Candidate folder: `evidence/new-science-ditl/`. Original files remain untouched. Exact headers, timestamp extrema, byte sizes and SHA-256 hashes: `data/derived/ditl_correction_2026-11-09/inventory.json`. No producing code or runtime manifest was supplied. Full identity is not inferred from current design.','', '| Scenario/file | Rows | Bytes | SHA-256 |','|---|---:|---:|---|']
 for f in files:lines.append(f"| `{Path(f['path']).name}` | {f['rows']} | {f['bytes']} | `{f['sha256']}` |")
 lines+=['','Registry: `evidence/science-ditl/run_registry.json`. All three telemetry files span zero to their named horizons; source/state semantics and cross-file consistency still require validation. Empty one-byte event files have no schema and establish no positive event evidence. Initial downstream references are captured before edits in `initial_dependency_inventory.json`.']
 (ROOT/'docs/audit/CORRECTED_DITL_EVIDENCE_INVENTORY.md').write_text('\n'.join(lines)+'\n')
 print('Inventory complete',len(files),flush=True)

def elapsed_weights(t):
 t=np.asarray(t,float)
 if len(t)<2 or not np.isfinite(t).all() or t[0]!=0 or (np.diff(t)<=0).any():raise ValueError('Invalid, duplicate or nonmonotonic timestamps')
 return np.r_[np.diff(t),0.]

def named_horizon_status(end,expected):
 return 'COMPLETE TIMESTAMP SPAN' if end==expected else 'INCOMPLETE'

def windows(t,w,mask):
 out=[]
 for a,dt in zip(t[mask],w[mask]):
  if dt<=0:continue
  b=a+dt
  if out and out[-1][1]==a:out[-1]=(out[-1][0],b)
  else:out.append((float(a),float(b)))
 return out

def daily(wins,days):
 out=np.zeros(days)
 for a,b in wins:
  for d in range(int(a//86400),min(days,int(math.ceil(b/86400)))):out[d]+=max(0,min(b,(d+1)*86400)-max(a,d*86400))
 return out

def epoch_of(events):
 vals=set()
 for frame,pairs in events:
  for absolute,relative in pairs:
   if absolute in frame:
    for a,b in zip(frame[absolute],frame[relative]):vals.add((datetime.fromisoformat(a.replace('Z','+00:00'))-timedelta(seconds=float(b))).isoformat())
 if len(vals)!=1:raise ValueError('Conflicting or missing absolute epochs')
 return next(iter(vals))

def audit(scenario):
 r=selected(scenario);paths={f['kind']:ROOT/f['path'] for f in r['files']};events={k:read(p) for k,p in paths.items() if k!='telemetry'}
 cols=['time_sec','mode','lat_deg','lon_deg','alt_km','battery_wh','solar_w','load_w','in_saa','in_eclipse','gs_visible','science_generation_enabled','relay_link_active','storage_mb','science_data_mb','downlinked_mb','cumulative_science_generated_mb','cumulative_downlinked_mb','science_histogram_bytes','payload_pointing_error_deg','sun_pointing_error_deg','relay_pointing_error_deg','science_counts_per_bin','science_total_count_rate','science_livetime_fraction','payload_power_state','science_event_type']
 # Scalar arrays fit in memory; vector parsing is streamed independently below.
 scalars=[c for c in cols if c not in ['science_counts_per_bin','science_total_count_rate']]
 f=pd.read_csv(paths['telemetry'],usecols=scalars,low_memory=False);t=f.time_sec.to_numpy(float)
 if not np.isfinite(t).all() or t[0]!=0 or (np.diff(t)<=0).any():raise ValueError('Nonmonotonic, duplicate or missing start')
 w=elapsed_weights(t);end=float(t[-1]);expected=31536000 if scenario=='leop_1yr' else 86400
 for c in ['in_saa','in_eclipse','gs_visible','science_generation_enabled','relay_link_active']:
  if f[c].dtype!=bool:raise ValueError('Invalid Boolean')
 numeric=f.select_dtypes(include='number')
 if not np.isfinite(numeric.to_numpy()).all():raise ValueError('Missing/nonfinite scalar')
 saa=f.in_saa.to_numpy();gate=f.science_generation_enabled.to_numpy();gs=f.gs_visible.to_numpy();relay=(f['mode']=='RELAY').to_numpy();link=f.relay_link_active.to_numpy();days=math.ceil(end/86400)
 modes={m:float(w[(f['mode']==m).to_numpy()].sum()) for m in f['mode'].unique()}
 result=dict(run_id=r['run_id'],scenario=scenario,rows=len(f),epoch=epoch_of([(events['gs_contacts'],[('aos_time','aos_time_sec'),('los_time','los_time_sec')]),(events['saa_passes'],[('entry_time','entry_time_sec'),('exit_time','exit_time_sec')])]),duration_s=end,requested_duration_s='UNKNOWN; filename/preset intent only',expected_named_horizon_s=expected,completeness=named_horizon_status(end,expected),terminal_semantics='Endpoint row present; no terminal_snapshot or interval_duration fields. Left-held integration excludes last row duration; producing code revision UNKNOWN.',mode_seconds=modes,cadence_counts={str(k):int(v) for k,v in zip(*np.unique(np.diff(t),return_counts=True))},missing_samples='UNKNOWN expected adaptive schedule; no duplicate/nonmonotonic timestamps',configuration={k:'UNKNOWN' for k in ['source_revision','runtime_config','raan_deg','inclination_deg','eccentricity','mass_kg','battery_capacity_wh','solar_panel_geometry','payload_revision','adcs','ground_station_coordinates','elevation_mask_deg','integrator','integration_timestep']})
 assert abs(sum(modes.values())-end)<1e-6
 result.update(altitude_km_range=[float(f.alt_km.min()),float(f.alt_km.max())],first_recorded_battery_wh=float(f.battery_wh.iloc[0]),battery_min_wh=float(f.battery_wh.min()),battery_max_wh=float(f.battery_wh.max()),final_battery_wh=float(f.battery_wh.iloc[-1]),minimum_soc_pct_at_planning25Wh=float(f.battery_wh.min()*4),battery_underflow_rows=int((f.battery_wh<0).sum()),generated_wh=float(np.dot(f.solar_w,w)/3600),consumed_wh=float(np.dot(f.load_w,w)/3600),saa_s=float(w[saa].sum()),acquisition_gate_s=float(w[gate].sum()),acquisition_in_saa_s=float(w[gate&saa].sum()),detection_in_saa_s=float(w[saa&(f['mode']=='DETECTION').to_numpy()].sum()),contact_s=float(w[gs].sum()),relay_visibility_s=float(w[gs&relay].sum()),link_active_s=float(w[link].sum()),eclipse_s=float(w[f.in_eclipse.to_numpy()].sum()),gate_outside_detection_or_saa_rows=int((gate&(~saa|~(f['mode']=='DETECTION').to_numpy())).sum()),link_outside_relay_visibility_rows=int((link&~(gs&relay)).sum()),generated_source_mb=float(f.science_data_mb.sum()),transferred_source_mb=float(f.downlinked_mb.sum()),storage_max_source_mb=float(f.storage_mb.max()),final_storage_source_mb=float(f.storage_mb.iloc[-1]),histogram_bytes=float(f.science_histogram_bytes.sum()))
 initial_store=float(f.storage_mb.iloc[0]-f.science_data_mb.iloc[0]+f.downlinked_mb.iloc[0]);result['initial_storage_source_mb']=initial_store
 result['storage_balance_max_residual_source_mb']=float(abs(initial_store+f.science_data_mb.cumsum()-f.downlinked_mb.cumsum()-f.storage_mb).max())
 result['generation_cumulative_max_residual_source_mb']=float(abs(f.science_data_mb.cumsum()-f.cumulative_science_generated_mb).max());result['transfer_cumulative_max_residual_source_mb']=float(abs(f.downlinked_mb.cumsum()-f.cumulative_downlinked_mb).max())
 result['mode_energy_wh']={m:float(np.dot(f.load_w.to_numpy()[(f['mode']==m).to_numpy()],w[(f['mode']==m).to_numpy()])/3600) for m in modes}
 result['pointing']={}
 for m,c in [('DETECTION','payload_pointing_error_deg'),('SUN_POINTING','sun_pointing_error_deg'),('RELAY','relay_pointing_error_deg')]:
  mask=(f['mode']==m).to_numpy()&(w>0);result['pointing'][m]={'weighted_mean_deg':float(np.dot(f[c].to_numpy()[mask],w[mask])/w[mask].sum()) if mask.any() else None,'max_deg':float(f.loc[mask,c].max()) if mask.any() else None}
 sw=windows(t,w,saa);vw=windows(t,w,gs);rw=windows(t,w,gs&relay);gw=windows(t,w,gate)
 result['sampled_saa_encounters']=len(sw);result['safe_entries']=int(((f['mode']=='SAFE')&(f['mode'].shift()!='SAFE')).sum());result['max_relay_gap_s']=max([rw[0][0],end-rw[-1][1]]+[rw[i+1][0]-rw[i][1] for i in range(len(rw)-1)]) if rw else end
 trans=events['mode_transitions'];actual=list(zip(t[1:][f['mode'].to_numpy()[1:]!=f['mode'].to_numpy()[:-1]],f['mode'].to_numpy()[1:][f['mode'].to_numpy()[1:]!=f['mode'].to_numpy()[:-1]]));reported=list(zip(trans.time_sec,trans.to_mode));result['transition_exact_match']=actual==reported;result['telemetry_transition_count']=len(actual);result['event_transition_count']=len(reported)
 result['event_checks']={}
 for kind,a,b,duration in [('gs_contacts','aos_time_sec','los_time_sec','duration_sec'),('saa_passes','entry_time_sec','exit_time_sec','dwell_sec'),('proton_passes','entry_time_sec','exit_time_sec','dwell_sec'),('slew_events','start_time_sec','end_time_sec','duration_sec'),('detumble_events','start_time_sec','end_time_sec','duration_sec')]:
  e=events[kind]
  if e.empty:result['event_checks'][kind]={'rows':0,'schema':'ABSENT'};continue
  residual=float(abs(e[b]-e[a]-e[duration]).max());duplicates=int(e.duplicated([a,b]).sum());bad=int(((e[a]<0)|(e[b]>end)|(e[b]<e[a])).sum())
  result['event_checks'][kind]=dict(rows=len(e),sum_duration_s=float(e[duration].sum()),duration_max_residual_s=residual,duplicate_intervals=duplicates,outside_horizon_rows=bad)
  if residual>1e-6 or duplicates or bad:result['event_checks'][kind]['status']='INCONSISTENT'
 contacts=events['gs_contacts'];cw=list(zip(contacts.aos_time_sec,contacts.los_time_sec));eligible=intersect(cw,rw)
 result['contacts']=dict(count=len(cw),duration_s=float(contacts.duration_sec.sum()),min_duration_s=float(contacts.duration_sec.min()),max_duration_s=float(contacts.duration_sec.max()),mean_duration_s=float(contacts.duration_sec.mean()),max_gap_s=max([cw[i+1][0]-cw[i][1] for i in range(len(cw)-1)],default=0),daily_min_s=float(daily(cw,days).min()),daily_mean_s=float(daily(cw,days).mean()),visibility_capacity_bytes=sum(capacity(b-a) for a,b in cw),relay_overlap_s=sum(b-a for a,b in eligible),relay_capacity_bytes=sum(capacity(b-a) for a,b in eligible),recorded_transfer_source_mb=float(contacts.downlinked_mb.sum()),max_elevation_deg=float(contacts.max_el_deg.max()),mask='UNKNOWN; already applied by producer; no second adjustment')
 # Every GS contact retains its own current-source capacity ledger.
 pd.DataFrame([dict(aos_s=a,los_s=b,visibility_capacity_bytes=capacity(b-a),relay_overlap_s=sum(y-x for x,y in intersect([(a,b)],rw)),relay_capacity_bytes=sum(capacity(y-x) for x,y in intersect([(a,b)],rw))) for a,b in cw]).to_csv(OUT/(scenario+'_contacts.csv'),index=False)
 result['contact_telemetry_duration_difference_s']=result['contact_s']-result['contacts']['duration_s'];result['contact_delivery_difference_source_mb']=result['transferred_source_mb']-result['contacts']['recorded_transfer_source_mb']
 result['payload_compatibility']='LEGACY five-channel columns plus 64-vector outputs; no matched current-six-scintillator response/calibration evidence.'
 # Count vectors are not silently converted to qualified events; compare source arrays both ways.
 totals=np.zeros(64);ratetotals=np.zeros(64);maxerr=0.;offset=0;active_rows=0
 for ch in pd.read_csv(paths['telemetry'],usecols=['science_counts_per_bin','science_total_count_rate','science_generation_enabled'],chunksize=25000):
  for j in np.flatnonzero(ch.science_generation_enabled.to_numpy()):
   aa=np.fromstring(ch.science_counts_per_bin.iloc[j].strip('[]').replace(',',' '),sep=' ');bb=np.fromstring(ch.science_total_count_rate.iloc[j].strip('[]').replace(',',' '),sep=' ')
   if len(aa)!=64 or len(bb)!=64 or not np.isfinite(aa).all() or (aa<0).any():raise ValueError('Invalid vector')
   totals+=aa;ratetotals+=bb*w[offset+j];maxerr=max(maxerr,float(abs(aa-bb*w[offset+j]).max()));active_rows+=1
  offset+=len(ch)
 result['array_sum_on_gate']=float(totals.sum());result['rate_times_forward_interval_sum_on_gate']=float(ratetotals.sum());result['array_vs_rate_dt_max_residual']=maxerr;result['acquisition_rows']=active_rows
 pp=events['proton_passes'];result['proton_pass_array_sum']=float(sum(np.fromstring(s.strip('[]').replace(',',' '),sep=' ').sum() for s in pp.total_counts_per_bin))
 # Sample-owned geographic keys, not exact crossing-time reconstruction.
 tiers=[];queues=[];sens=[]
 for tier,res in [('MMSC',5.),('MSC',1.),('EMSC',.5)]:
  groups=defaultdict(list);visit=0;prev=None;cur=None;cells=set();geovisits=0
  for i in range(len(t)-1):
   key=cell_key(f.lat_deg.iloc[i],f.lon_deg.iloc[i],res) if saa[i] else None
   if key!=prev and key is not None:visit+=1;geovisits+=1;cells.add(key)
   prev=key
   if gate[i] and key is not None:
    if cur is not None and cur['visit']==visit and cur['b']==t[i]:cur['b']=t[i+1]
    else:
     cur={'visit':visit,'a':float(t[i]),'b':float(t[i+1]),'cell':key};groups[visit].append(cur)
   else:cur=None
  for n in [1,2,3]:
   gen=[]
   for segs in groups.values():
    allocation=[1]*len(segs)
    while sum(allocation)<n:
     j=max(range(len(segs)),key=lambda j:(segs[j]['b']-segs[j]['a'])/allocation[j]);allocation[j]+=1
    for seg,nn in zip(segs,allocation):
     for j in range(1,nn+1):gen.append((seg['a']+(seg['b']-seg['a'])*j/nn,292))
   gen.sort();q=backlog(gen,eligible);ledger=q.pop('contacts');case=f'{scenario}_{tier}_{n}'
   pd.DataFrame(ledger).to_csv(OUT/(case+'_queue.csv'),index=False)
   pd.DataFrame(gen,columns=['time_s','bytes']).to_csv(OUT/(case+'_releases.csv'),index=False)
   daycounts=Counter(min(days-1,int(a//86400)) for a,b in gen);peak=Counter(math.floor(a) for a,b in gen)
   tiers.append(dict(tier=tier,readings=n,geometric_visits=geovisits,geometric_cells=len(cells),science_enabled_visits=len(groups),acquisition_segments=sum(map(len,groups.values())),records=len(gen),bytes=292*len(gen),exposure_s=sum(s['b']-s['a'] for ss in groups.values() for s in ss),mean_daily_bytes=292*len(gen)/days,max_daily_bytes=292*max(daycounts.values(),default=0),peak_one_second_records=max(peak.values(),default=0)))
   queues.append(dict(case=case,**q,balance_lower_bound_bps=q['generated_bytes']*8/result['contacts']['relay_overlap_s'] if result['contacts']['relay_overlap_s'] else None))
   if n==3:
    # Deterministic outage at every calendar day; bounded postprocessing, not propagation.
    for outage_days in [1,3,7]:
     worst=0
     for day in range(days):
      lo=day*86400;hi=min(end,(day+outage_days)*86400);service=[]
      for a,b in eligible:
       if b<=lo or a>=hi:service.append((a,b))
       else:
        if a<lo:service.append((a,lo))
        if b>hi:service.append((hi,b))
      worst=max(worst,backlog(gen,service)['peak_required_bytes'])
     sens.append(dict(case=case,outage_days=outage_days,worst_peak_bytes=worst))
    worst=0
    for a,b in cw:
     service=[(x,y) for x,y in eligible if y<=a or x>=b];worst=max(worst,backlog(gen,service)['peak_required_bytes'])
    sens.append(dict(case=case,outage_days='one complete contact',worst_peak_bytes=worst))
 result['tiers']=tiers;result['queues']=queues;result['outages']=sens
 result['v3_scope']='Ideal sample-owned partition workload. Hardware timing, true boundary crossings and accepted counts UNKNOWN. No minimum reading duration; valid zero-count slots retained. Fragmentation may require >preferred records to preserve disjoint exposure.'
 # Daily values split intervals at midnight rather than row counting.
 dailyrows=[]
 for d in range(days):
  ww=np.maximum(0,np.minimum(t+w,(d+1)*86400)-np.maximum(t,d*86400));mask=(t>=d*86400)&(t<(d+1)*86400)
  dailyrows.append(dict(day=d,acquisition_s=float(ww[gate].sum()),saa_s=float(ww[saa].sum()),science_mode_s=float(ww[(f['mode']=='DETECTION').to_numpy()].sum()),contact_s=float(daily(cw,days)[d]),relay_s=float(daily(eligible,days)[d]),battery_min_wh=float(f.loc[mask,'battery_wh'].min()),battery_max_wh=float(f.loc[mask,'battery_wh'].max()),generated_source_mb=float(f.loc[mask,'science_data_mb'].sum()),delivered_source_mb=float(f.loc[mask,'downlinked_mb'].sum()),storage_max_source_mb=float(f.loc[mask,'storage_mb'].max())))
 pd.DataFrame(dailyrows).to_csv(OUT/(scenario+'_daily.csv'),index=False)
 # Deterministic plot samples only; all summaries above use full-resolution data.
 f.iloc[::max(1,len(f)//6000)].to_csv(OUT/(scenario+'_plot.csv'),index=False)
 dump(OUT/(scenario+'_summary.json'),result)
 reg=json.loads(REG.read_text());rr=next(x for x in reg['runs'] if x['run_id']==r['run_id']);rr.update(epoch=result['epoch'],duration_s=end,status='VALIDATED TIMESTAMP SPAN; MODEL/INTERVAL SEMANTICS CONDITIONAL',derived_summary=str((OUT/(scenario+'_summary.json')).relative_to(ROOT)));dump(REG,reg)
 print(scenario,{k:result[k] for k in ['duration_s','epoch','mode_seconds','saa_s','acquisition_gate_s','battery_min_wh','generated_source_mb','transferred_source_mb','array_vs_rate_dt_max_residual']},flush=True)

if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--inventory',action='store_true');p.add_argument('--run',choices=SCENARIOS);a=p.parse_args()
 if a.inventory:inventory()
 if a.run:audit(a.run)
