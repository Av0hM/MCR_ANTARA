"""Read-only, bounded evidence accounting. Does not run spacecraft simulations."""
from pathlib import Path
import csv, json, hashlib, ast, re
from collections import defaultdict
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
SCI=ROOT/'evidence/science_ditl/raw'
OUT=ROOT/'evidence/science-ditl/validation'
MODES=['COLD_AND_DARK','DETUMBLE','SUN_POINTING','DETECTION','RELAY','SLEWING','SAFE']

def read_csv(path,**kw):
    with open(path,newline='') as f:
        row=next(csv.reader(f),[])
    if not row:return pd.DataFrame()
    if len(row)!=len(set(row)):raise ValueError('Duplicate headers')
    return pd.read_csv(path,**kw)

def boolean(x):
    s=pd.Series(x)
    if not s.isin([True,False,'True','False',0,1,'0','1']).all():raise ValueError('Malformed Boolean')
    return s.isin([True,'True',1,'1']).to_numpy()

def intervals(frame):
    t=frame.time_sec.to_numpy(float);w=frame.interval_duration_sec.to_numpy(float)
    if not np.isfinite([t,w]).all() or (w<0).any() or (np.diff(t)<=0).any():raise ValueError('Invalid time series')
    if not np.allclose(t[1:],t[:-1]+w[:-1],atol=1e-7,rtol=0):raise ValueError('Gap/overlap')
    if not np.allclose(frame.state_time_sec,t+w,atol=1e-7,rtol=0):raise ValueError('Invalid state endpoints')
    term=boolean(frame.terminal_snapshot)
    if (term & (w!=0)).any() or ((w==0)&~term).any():raise ValueError('Invalid terminal interval')
    return w

def completion(start,end,terminal,expected):
    if start!=0:return 'INCOMPLETE: missing beginning'
    if not terminal:return 'INCOMPLETE: no terminal snapshot'
    if not np.isclose(end,expected,atol=1e-7,rtol=0):return 'COMPLETE RECORDED WINDOW; NOT EXPECTED HORIZON'
    return 'COMPLETE EXPECTED HORIZON'

def weighted(values,weights):
    v,w=np.asarray(values,float),np.asarray(weights,float)
    if not np.isfinite(v).all() or not np.isfinite(w).all() or (w<0).any():raise ValueError('Invalid weighted measurement')
    return float(np.dot(v,w/w.sum())) if w.sum()>0 else None

def soc(wh,capacity):
    if capacity<=0 or not np.isfinite(capacity):raise ValueError('Invalid capacity')
    return np.asarray(wh)*100/capacity

def vector(s):
    if not isinstance(s,str) or not s.startswith('[') or not s.endswith(']'):raise ValueError('Invalid vector syntax')
    body=s[1:-1].strip()
    tokens=[x for x in re.split(r'[\s,]+',body) if x]
    a=np.asarray([float(x) for x in tokens],float)
    if a.ndim!=1 or not np.isfinite(a).all() or (a<0).any():raise ValueError('Invalid histogram')
    return a

def temperature_c(kelvin, celsius):
    k,c=np.asarray(kelvin,float),np.asarray(celsius,float)
    if not np.isfinite([k,c]).all() or not np.allclose(k-273.15,c,rtol=0,atol=1e-10):
        raise ValueError('Temperature unit mismatch')
    return c

def censored_completion(success, times):
    ok=boolean(success);t=np.asarray(times,float)
    if len(t)!=len(ok) or not np.isfinite(t[ok]).all() or (t[ok]<0).any():raise ValueError('Invalid completion')
    return {'n':len(t),'successes':int(ok.sum()),'nonconverged':int((~ok).sum()),
            'successful_median_s':float(np.median(t[ok])) if ok.any() else None}

def compare_configuration(left,right,fields):
    if any(left.get(k) in (None,'UNKNOWN') or right.get(k) in (None,'UNKNOWN') for k in fields):return 'INSUFFICIENT EVIDENCE'
    return 'DIRECTLY COMPARABLE' if all(left[k]==right[k] for k in fields) else 'INCOMPATIBLE CONFIGURATION'


def science(run):
    raise RuntimeError("Superseded DITL sources: use validate_corrected_ditl.py and run_registry.json; historical results are read-only.")
    path=SCI/f'{run}_ANTARA_Science_telemetry.csv'
    columns=['time_sec','state_time_sec','interval_duration_sec','terminal_snapshot','mode','battery_wh','solar_w','load_w','in_saa','gs_visible','science_generation_enabled','relay_link_active','storage_mb','science_data_mb','downlinked_mb','cumulative_science_generated_mb','cumulative_downlinked_mb','sun_submode','payload_pointing_error_deg','sun_pointing_error_deg','relay_pointing_error_deg','science_counts_per_bin','science_total_count_rate','science_histogram_bytes','lat_deg','lon_deg','alt_km','payload_power_state']
    result=dict(run=run,rows=0,mode_seconds=defaultdict(float),mode_energy_wh=defaultdict(float),submode_seconds=defaultdict(float),elapsed_s=0.,saa_s=0.,detection_in_saa_s=0.,acquisition_gate_s=0.,acquisition_in_saa_s=0.,contact_s=0.,link_s=0.,generated_model_mb=0.,transferred_model_mb=0.,generated_wh=0.,consumed_wh=0.,battery_min_wh=float('inf'),storage_max_model_mb=0.,packet_bytes=0.,accepted_expected_counts=0.,histogram_records=0,rate_count_max_error=0.,rate_count_sum_max_error=0.,storage_balance_max_error=0.,cumulative_generation_max_error=0.,cumulative_downlink_max_error=0.,serialization_rows_outside_acquisition_gate=0,telemetry_transitions=[])
    previous=None;lastmode=None;points=[];pointing={x:[0.,0.,0.] for x in ['DETECTION','SUN_POINTING','RELAY']};bincount=np.zeros(64)
    for frame in pd.read_csv(path,usecols=columns,chunksize=25000):
        w=intervals(frame);t=frame.time_sec.to_numpy();
        if previous is not None and abs(t[0]-previous['state_time_sec'])>1e-7:raise ValueError('Cross-chunk gap')
        if not frame['mode'].isin(MODES).all():raise ValueError('Unknown mode')
        if result['rows']==0:
            result['start_s']=float(t[0]);result['first_recorded_battery_wh']=float(frame.battery_wh.iloc[0]);result['initial_storage_inferred_model_mb']=float(frame.storage_mb.iloc[0]-frame.science_data_mb.iloc[0]+frame.downlinked_mb.iloc[0])
        saa=boolean(frame.in_saa);gate=boolean(frame.science_generation_enabled);gs=boolean(frame.gs_visible);link=boolean(frame.relay_link_active)
        result['rows']+=len(frame);result['elapsed_s']+=float(w.sum())
        for key,mask in [('saa_s',saa),('detection_in_saa_s',saa&(frame['mode']=='DETECTION')),('acquisition_gate_s',gate),('acquisition_in_saa_s',saa&gate),('contact_s',gs),('link_s',link)]:result[key]+=float(w[mask].sum())
        for mode in MODES:
            mask=(frame['mode']==mode).to_numpy();result['mode_seconds'][mode]+=float(w[mask].sum());result['mode_energy_wh'][mode]+=float(np.dot(frame.load_w.to_numpy()[mask],w[mask])/3600)
        for sub in frame.sun_submode.unique():result['submode_seconds'][str(sub)]+=float(w[(frame.sun_submode==sub).to_numpy()].sum())
        for mode,col in [('DETECTION','payload_pointing_error_deg'),('SUN_POINTING','sun_pointing_error_deg'),('RELAY','relay_pointing_error_deg')]:
            mask=(frame['mode']==mode).to_numpy()&(w>0);v=frame[col].to_numpy(float)[mask]
            if not np.isfinite(v).all():raise ValueError('Invalid pointing')
            pointing[mode][0]+=float(np.dot(v,w[mask]));pointing[mode][1]+=float(w[mask].sum());pointing[mode][2]=max(pointing[mode][2],float(v.max()) if len(v) else 0.)
        gen=frame.science_data_mb.to_numpy(float);down=frame.downlinked_mb.to_numpy(float)
        cumg=result['generated_model_mb']+np.cumsum(gen);cumd=result['transferred_model_mb']+np.cumsum(down)
        for key,v in [('cumulative_generation_max_error',cumg-frame.cumulative_science_generated_mb),('cumulative_downlink_max_error',cumd-frame.cumulative_downlinked_mb),('storage_balance_max_error',result['initial_storage_inferred_model_mb']+cumg-cumd-frame.storage_mb)]:result[key]=max(result[key],float(np.max(abs(v))))
        result['generated_model_mb']+=float(gen.sum());result['transferred_model_mb']+=float(down.sum());result['packet_bytes']+=float(frame.science_histogram_bytes.sum())
        result['generated_wh']+=float(np.dot(frame.solar_w,w)/3600);result['consumed_wh']+=float(np.dot(frame.load_w,w)/3600)
        result['battery_min_wh']=min(result['battery_min_wh'],float(frame.battery_wh.min()));result['storage_max_model_mb']=max(result['storage_max_model_mb'],float(frame.storage_mb.max()))
        result['serialization_rows_outside_acquisition_gate']+=int(((gen>0)&~gate&~boolean(frame.terminal_snapshot)).sum()) # Flush outside acquisition can be legitimate.
        for stamp,mode in zip(t,frame['mode']):
            if lastmode is not None and mode!=lastmode:result['telemetry_transitions'].append([float(stamp),str(mode)])
            lastmode=mode
        for i in np.flatnonzero(gate):
            a=vector(frame.science_counts_per_bin.iloc[i]);r=vector(frame.science_total_count_rate.iloc[i])
            if len(a)!=64 or len(r)!=64:raise ValueError('Missing channels')
            bincount+=a;result['histogram_records']+=1
            result['rate_count_max_error']=max(result['rate_count_max_error'],float(np.max(abs(a-r*w[i]))))
            result['rate_count_sum_max_error']=max(result['rate_count_sum_max_error'],float(abs(a.sum()-r.sum()*w[i])))
        sampled=frame.iloc[::max(1,len(frame)//250)].drop(columns=['science_counts_per_bin','science_total_count_rate'])
        points.append(sampled);previous=frame.iloc[-1].to_dict()
    result['accepted_expected_counts']=float(bincount.sum());result['end_s']=float(previous['state_time_sec']);result['terminal_snapshot']=bool(previous['terminal_snapshot']);result['final_battery_wh']=float(previous['battery_wh']);result['final_storage_model_mb']=float(previous['storage_mb'])
    result['completeness']=completion(result['start_s'],result['end_s'],result['terminal_snapshot'],31536000 if run=='leop_1yr' else 86400)
    result['pointing']={m:dict(mean_deg=v[0]/v[1] if v[1] else None,max_deg=v[2] if v[1] else None,denominator_s=v[1]) for m,v in pointing.items()}
    result['minimum_soc_pct_at_25Wh']=float(soc(result['battery_min_wh'],25))
    result['events']={};result['epoch_from_events']='UNKNOWN';passcounts=np.zeros(64)
    for kind in ['gs_contacts','saa_passes','proton_passes','mode_transitions','slew_events','detumble_events','rejected_transitions']:
        ev=read_csv(SCI/f'{run}_ANTARA_Science_{kind}.csv');row={'rows':len(ev),'columns':list(ev.columns)}
        for col in ['duration_sec','dwell_sec','downlinked_mb','data_collected_mb']:
            if col in ev:row[col+'_sum']=float(ev[col].sum())
        if 'aos_time' in ev and len(ev):
            origin=pd.to_datetime(ev.aos_time.iloc[0])-pd.to_timedelta(ev.aos_time_sec.iloc[0],unit='s');result['epoch_from_events']=origin.isoformat()
        if kind=='proton_passes' and len(ev):
            for s in ev.total_counts_per_bin:passcounts+=vector(s)
            row['expected_counts_sum']=float(passcounts.sum());row['histogram_total_max_abs_difference']=float(np.max(abs(passcounts-bincount)))
        if kind=='mode_transitions':
            actual=[[float(r.time_sec),r.to_mode] for r in ev.itertuples()] if len(ev) else []
            row['exact_match_to_telemetry']=actual==result['telemetry_transitions']
        result['events'][kind]=row
    OUT.mkdir(parents=True,exist_ok=True)
    pd.concat(points).to_csv(OUT/f'{run}_plot_samples.csv',index=False)
    np.savetxt(OUT/f'{run}_expected_counts_by_bin.csv',bincount,delimiter=',',header='legacy_expected_counts',comments='')
    # Transition list is retained separately so summary remains readable.
    (OUT/f'{run}_transitions.json').write_text(json.dumps(result.pop('telemetry_transitions'),indent=2))
    (OUT/f'{run}_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(run,json.dumps({k:v for k,v in result.items() if k not in ['events','pointing','submode_seconds']},default=dict),flush=True)
    return result

def thermal():
    root=ROOT/'evidence/thermal';d=read_csv(root/'raw/ANTARA_Thermal_telemetry.csv');t=d.time_sec.to_numpy(float)
    if not np.isfinite(t).all() or (np.diff(t)<=0).any():raise ValueError('Thermal timestamps')
    rows=[];summary=read_csv(root/'raw/ANTARA_Thermal_worst_case_summary.csv').set_index('node')
    for node in ['+X','-X','+Y','-Y','+Z','-Z','internal']:
        c=d[node+'_temp_c'].to_numpy();k=d[node+'_temp_k'].to_numpy()
        temperature_c(k,c)
        rows.append(dict(node=node,min_c=float(c.min()),max_c=float(c.max()),time_weighted_mean_c=float(np.trapezoid(c,t)/(t[-1]-t[0])),min_time_s=float(t[np.argmin(c)]),max_time_s=float(t[np.argmax(c)])))
        np.testing.assert_allclose([c.min(),c.max(),c.min()-10,c.max()+10],[summary.loc[node,'cold_case_temp_c'],summary.loc[node,'hot_case_temp_c'],summary.loc[node,'cold_case_temp_with_margin_c'],summary.loc[node,'hot_case_temp_with_margin_c']],rtol=0,atol=1e-10)
        np.testing.assert_allclose([t[np.argmin(c)]/3600,t[np.argmax(c)]/3600],[summary.loc[node,'cold_case_time_hr'],summary.loc[node,'hot_case_time_hr']],rtol=0,atol=1e-10)
    out=root/'validation';out.mkdir(exist_ok=True);pd.DataFrame(rows).to_csv(out/'node_statistics.csv',index=False)
    x=dict(rows=len(d),start_s=float(t[0]),last_label_s=float(t[-1]),sampling_s=sorted(set(np.diff(t))),summary_matches_single_history=True,independent_hot_cold_runs_present=False,internal_heat_min_w=float(d.internal_dissipation_w.min()),internal_heat_max_w=float(d.internal_dissipation_w.max()),max_face_gradient_c=float(d[[x+'_temp_c' for x in ['+X','-X','+Y','-Y','+Z','-Z']]].max(axis=1).sub(d[[x+'_temp_c' for x in ['+X','-X','+Y','-Y','+Z','-Z']]].min(axis=1)).max()))
    (out/'summary.json').write_text(json.dumps(x,indent=2));print('thermal',x,rows,flush=True)
    return d,rows

def detumble():
    root=ROOT/'evidence/detumble';d=read_csv(root/'raw/detumble_mc_summary.csv')
    success=boolean(d.success);times=d.time_to_complete_sec.to_numpy(float)
    if not np.isfinite(times[success]).all() or (times[success]<0).any():raise ValueError('Invalid successful completion')
    r=np.linalg.norm(d[['rate0_x','rate0_y','rate0_z']],axis=1);a=np.linalg.norm(d[['accel0_x','accel0_y','accel0_z']],axis=1)
    np.testing.assert_allclose(r,d.rate0_mag,rtol=1e-12);np.testing.assert_allclose(a,d.accel0_mag,rtol=1e-12)
    result=dict(samples=len(d),reported_success=int(success.sum()),nonconverged=int((~success).sum()),reported_fraction=float(success.mean()),success_only_median_s=float(np.median(times[success])),success_only_p95_s=float(np.percentile(times[success],95)),success_only_max_s=float(np.max(times[success])),unsuccessful_infinite_times=int(np.isinf(times[~success]).sum()),hit_rate_cap=int(boolean(d.hit_rate_cap).sum()),all_peak_wheel_momentum_zero=bool((d.peak_wheel_momentum_nms==0).all()),nonzero_acceleration_rows=int((a>0).sum()),timeout_s='UNKNOWN',seed='UNKNOWN',independence='UNVERIFIED',initial_rate_range_deg_s=[float(r.min()),float(r.max())],initial_acceleration_range_deg_s2=[float(a.min()),float(a.max())])
    out=root/'validation';out.mkdir(exist_ok=True);(out/'summary.json').write_text(json.dumps(result,indent=2));print('detumble',result,flush=True)
    return d,result

def write_comparisons():
    raise RuntimeError("Superseded DITL sources: use validate_corrected_ditl.py and run_registry.json; historical results are read-only.")
    a=json.loads((OUT/'leop_24h_summary.json').read_text());b=json.loads((OUT/'no_leop_24h_summary.json').read_text())
    keys=['elapsed_s','saa_s','acquisition_gate_s','contact_s','generated_model_mb','transferred_model_mb','storage_max_model_mb','first_recorded_battery_wh','battery_min_wh','final_battery_wh','generated_wh','consumed_wh']
    rows=[]
    for key in keys:
        x,y=a[key],b[key];rows.append(dict(metric=key,LEOP=x,No_LEOP=y,difference_NoLEOP_minus_LEOP=y-x,percent_change_vs_LEOP=100*(y-x)/x if x else None))
    for mode in MODES:
        x,y=a['mode_seconds'][mode],b['mode_seconds'][mode];rows.append(dict(metric=mode+'_seconds',LEOP=x,No_LEOP=y,difference_NoLEOP_minus_LEOP=y-x,percent_change_vs_LEOP=100*(y-x)/x if x else None))
    pd.DataFrame(rows).to_csv(OUT/'one_hour_comparison.csv',index=False)
    horizon=json.loads((OUT/'leop_1yr_summary.json').read_text())['end_s'];result={}
    for kind,start,end in [('gs_contacts','aos_time_sec','los_time_sec'),('saa_passes','entry_time_sec','exit_time_sec'),('proton_passes','entry_time_sec','exit_time_sec'),('slew_events','start_time_sec','end_time_sec'),('mode_transitions','time_sec','time_sec')]:
        d=read_csv(SCI/f'leop_1yr_ANTARA_Science_{kind}.csv');sub=d[d[end]<=horizon]
        x=dict(all_rows=len(d),last_event_s=float(d[end].max()),rows_ending_within_telemetry_horizon=len(sub))
        for c in ['duration_sec','dwell_sec','downlinked_mb','data_collected_mb']:
            if c in sub:x[c+'_overlap_sum']=float(sub[c].sum())
        if kind=='proton_passes':x['overlap_expected_counts']=float(sum(vector(s).sum() for s in sub.total_counts_per_bin))
        result[kind]=x
    (OUT/'annual_event_overlap.json').write_text(json.dumps(result,indent=2)+'\n')


def main():
    for run in ['leop_24h','no_leop_24h','leop_1yr']:science(run)
    thermal();detumble();write_comparisons()
if __name__=='__main__':main()
