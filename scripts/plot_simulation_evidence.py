"""Figures derived from supplied evidence only; no simulation or extrapolation."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
COL=['#007c83','#b65c24']

def save(fig,area,name):
    fig.savefig(ROOT/f'evidence/{area}/figures/{name}.png',dpi=180,bbox_inches='tight');plt.close(fig)

def main():
    raise RuntimeError("Old DITL plot inputs are superseded; use corrected figures. Independent thermal/detumble artifacts remain historical references.")
    labels=['LEOP: recorded 1 h','No-LEOP: recorded 1 h'];runs=['leop_24h','no_leop_24h']
    data=[pd.read_csv(ROOT/f'evidence/science_ditl/raw/{r}_ANTARA_Science_telemetry.csv') for r in runs]
    sums=[json.loads((ROOT/f'evidence/science-ditl/validation/{r}_summary.json').read_text()) for r in runs]
    modes=['COLD_AND_DARK','DETUMBLE','SUN_POINTING','SLEWING','SAFE'];colors=['#444444','#9d6c4f','#c49a00','#8563ac','#d54b4b']
    fig,axes=plt.subplots(2,2,figsize=(9,5),layout='constrained',sharex=True)
    for j,(d,label) in enumerate(zip(data,labels)):
        t=d.time_sec.to_numpy()/60
        axes[0,j].step(t,[modes.index(m) for m in d['mode']],where='post',color=COL[j]);axes[0,j].set(title=label,yticks=range(5),yticklabels=['Cold/dark','Detumble','Sun pointing','Slewing','Safe'],ylim=(-.4,4.4))
        axes[1,j].plot(t,d.battery_wh/25*100,color=COL[j]);axes[1,j].set(xlabel='Elapsed time (min)',ylabel='Recorded SOC (% of 25 Wh)',ylim=(58,90),xlim=(0,60));axes[1,j].grid(alpha=.2)
    fig.suptitle('Complete one-hour exports; filenames say 24h. No SAA/contact/acquisition in this window.',fontsize=10)
    save(fig,'science-ditl','one_hour_operations')
    fig,ax=plt.subplots(2,2,figsize=(9,5),layout='constrained',sharex=True)
    for j,(d,label) in enumerate(zip(data,labels)):
        ax[0,j].plot(d.time_sec/60,d.solar_w,label='Recorded solar');ax[0,j].plot(d.time_sec/60,d.load_w,label='Load');ax[0,j].set(title=label,ylabel='Power (W)',ylim=(0,14));ax[0,j].legend(fontsize=8)
        ax[1,j].plot(d.time_sec/60,d.sun_pointing_error_deg,label='Sun error');ax[1,j].plot(d.time_sec/60,d.payload_pointing_error_deg,label='Payload error');ax[1,j].set(xlabel='Elapsed time (min)',ylabel='Diagnostic angle (deg)',ylim=(0,180));ax[1,j].legend(fontsize=8)
    fig.suptitle('Recorded model diagnostics; no flight pointing or EPS margin implied',fontsize=10)
    save(fig,'science-ditl','one_hour_power_pointing')
    fig,ax=plt.subplots(1,2,figsize=(9,3.8),layout='constrained')
    x=np.arange(len(modes))
    for j,s in enumerate(sums):
        ax[0].barh(x+(j-.5)*.35,[s['mode_seconds'][m]/60 for m in modes],height=.35,color=COL[j],label=labels[j])
        ax[1].barh(x+(j-.5)*.35,[s['mode_energy_wh'][m] for m in modes],height=.35,color=COL[j])
    for a in ax:a.set(yticks=x,yticklabels=['Cold/dark','Detumble','Sun pointing','Slewing','Safe']);a.grid(axis='x',alpha=.2)
    ax[0].set_xlabel('Mode duration (min)');ax[1].set_xlabel('Integrated recorded load (Wh)');ax[0].legend(fontsize=7)
    fig.suptitle('One-hour startup/occupancy comparison; telemetry labels, not corrected event times',fontsize=10)
    save(fig,'science-ditl','one_hour_occupancy_energy')
    annual=json.loads((ROOT/'evidence/science-ditl/validation/leop_1yr_summary.json').read_text())
    fig,ax=plt.subplots(1,2,figsize=(9,3.8),layout='constrained')
    names=['SUN_POINTING','SLEWING','DETECTION','RELAY','DETUMBLE']
    values=[annual['mode_seconds'][n]/3600 for n in names]
    ax[0].barh(names,values,color=COL[0]);ax[0].set_xlabel('Recorded mode duration (h)')
    for i,v in enumerate(values):ax[0].text(v+8,i,f'{v:.2f}',va='center',fontsize=8)
    ax[0].set_xlim(0,max(values)*1.22)
    ax[1].barh(['SAA geography','Detection in SAA','Acquisition gate'],[annual['saa_s'],annual['detection_in_saa_s'],annual['acquisition_gate_s']],color=[COL[0],COL[0],COL[1]])
    ax[1].set(xscale='log',xlabel='Recorded exposure (s, logarithmic axis)',xlim=(100,1000000))
    for i,v in enumerate([annual['saa_s'],annual['detection_in_saa_s'],annual['acquisition_gate_s']]):ax[1].text(v*1.1,i,f'{v:g}',va='center',fontsize=8)
    fig.suptitle('leop_1yr telemetry only: incomplete at 50 days + 20 s; event exports inconsistent',fontsize=10)
    save(fig,'science-ditl','partial_annual_mode_exposure')
    a=pd.read_csv(ROOT/'evidence/science-ditl/validation/leop_1yr_plot_samples.csv')
    fig,ax=plt.subplots(2,1,figsize=(8,4.6),layout='constrained',sharex=True)
    ax[0].plot(a.time_sec/86400,a.storage_mb-10,color=COL[0]);ax[0].set(ylabel='Storage above initial 10\n(source MB units)')
    ax[1].plot(a.time_sec/86400,a.cumulative_science_generated_mb,label='Serialized science');ax[1].plot(a.time_sec/86400,a.cumulative_downlinked_mb,ls='--',label='Transferred');ax[1].set(xlabel='Elapsed time (days)',ylabel='Cumulative source MB');ax[1].legend(fontsize=8)
    fig.suptitle('Incomplete annual-labelled telemetry: 50 days + 20 s; inconsistent with event exports',fontsize=10)
    save(fig,'science-ditl','partial_annual_storage')
    th=pd.read_csv(ROOT/'evidence/thermal/raw/ANTARA_Thermal_telemetry.csv');stats=pd.read_csv(ROOT/'evidence/thermal/validation/node_statistics.csv')
    fig,ax=plt.subplots(2,1,figsize=(8,5),layout='constrained',sharex=True)
    for n in stats.node:ax[0].plot(th.time_hr,th[n+'_temp_c'],label=n,lw=1)
    ax[0].set(ylabel='Node temperature (°C)');ax[0].legend(ncol=4,fontsize=8)
    ax[1].plot(th.time_hr,th.internal_dissipation_w,color=COL[0]);ax[1].set(xlabel='Recorded time label (h)',ylabel='Internal heat (W)')
    fig.suptitle('Single supplied 24 h thermal history; independent synthetic heat schedule',fontsize=10)
    save(fig,'thermal','validated_history')
    fig,ax=plt.subplots(figsize=(7,3.4),layout='constrained')
    for i,r in stats.iterrows():ax.plot([r.min_c,r.max_c],[i,i],lw=4,color=COL[0]);ax.scatter([r.min_c,r.max_c],[i,i],color=COL[0]);ax.scatter(r.time_weighted_mean_c,i,color=COL[1],zorder=4)
    ax.set(yticks=range(7),yticklabels=stats.node,xlabel='Temperature (°C)',title='Single-history extrema and time-weighted means (24 h labels)');ax.grid(axis='x',alpha=.2)
    fig.text(.5,-.04,'Not independent HOT/COLD cases; no component limits or compliance margin supplied',ha='center',fontsize=8)
    save(fig,'thermal','validated_envelope')
    dt=pd.read_csv(ROOT/'evidence/detumble/raw/detumble_mc_summary.csv');ok=dt.success==1;v=np.sort(dt.loc[ok,'time_to_complete_sec'])
    fig,ax=plt.subplots(1,2,figsize=(9,3.8),layout='constrained')
    ax[0].step(v,np.arange(1,len(v)+1)/len(dt)*100,where='post',color=COL[0]);ax[0].set(xlabel='Reported completion time (s)',ylabel='Fraction of all 50,000 rows (%)',ylim=(0,100));ax[0].text(.04,.8,'33,867 nonconverged\nCensor times unavailable',transform=ax[0].transAxes,fontsize=9)
    bins=np.arange(0,65,5);x=[];y=[];ns=[]
    for lo,hi in zip(bins[:-1],bins[1:]):
        mask=(dt.rate0_mag>=lo)&(dt.rate0_mag<hi);x.append((lo+hi)/2);y.append(100*dt.loc[mask,'success'].mean());ns.append(int(mask.sum()))
    ax[1].bar(x,y,width=4,color=COL[0]);ax[1].set(xlabel='Initial spin magnitude (deg/s)',ylabel='Reported successful rows (%)',ylim=(0,100))
    fig.suptitle('Historical synthetic summary: 16,133/50,000 reported successes; duration varies by trial',fontsize=10)
    save(fig,'detumble','validated_summary')
    pd.DataFrame(dict(rate_bin_center_deg_s=x,sample_count=ns,reported_success_pct=y)).to_csv(ROOT/'evidence/detumble/validation/spin_groups.csv',index=False)
if __name__=='__main__':main()
