"""Figures from registry-selected corrected audit outputs, not simulation runs."""
from validate_corrected_ditl import ROOT,OUT,SCENARIOS,selected,dump
import json,numpy as np,pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=ROOT/'evidence/science-ditl/figures';D.mkdir(exist_ok=True)
S={s:json.loads((OUT/(s+'_summary.json')).read_text()) for s in SCENARIOS}
from validate_corrected_ditl import selected
for scenario,summary in S.items():
 if summary['run_id']!=selected(scenario,verify=False)['run_id']:raise ValueError('Summary identity differs from authoritative registry')
F={s:pd.read_csv(OUT/(s+'_plot.csv')) for s in SCENARIOS}
manifest=[]
def save(fig,name,runs):
 fig.tight_layout(rect=(0,.06,1,.94));fig.suptitle('Corrected exports: 2000-03-01 epoch; model predictions',fontsize=11)
 fig.text(.01,.01,'Source: new-science-ditl CSVs; '+', '.join(S[s]['run_id'] for s in runs),fontsize=6)
 p=D/('corrected_20261109_'+name+'.png');fig.savefig(p,dpi=180);plt.close(fig);manifest.append(dict(path=str(p.relative_to(ROOT)),runs=[S[s]['run_id'] for s in runs],source='Registry-selected CSVs; scalar plots may be display-sampled; summaries use full data.'))
pair=SCENARIOS[:2];modes=sorted(set().union(*(S[s]['mode_seconds'] for s in SCENARIOS)));colors=plt.get_cmap('tab10')
fig,ax=plt.subplots(2,1,figsize=(9,5),sharex=True)
for a,s in zip(ax,pair):
 f=F[s]
 for j,m in enumerate(modes):
  mask=f['mode']==m;a.scatter(f.time_sec[mask]/3600,np.full(mask.sum(),j),s=4,color=colors(j),label=m)
 a.set(yticks=range(len(modes)),yticklabels=modes,title=s+' (24 h)',ylabel='Recorded mode')
ax[-1].set_xlabel('Elapsed hours; display sampling only');save(fig,'day_modes',pair)
fig,ax=plt.subplots(1,2,figsize=(9,3.8));x=np.arange(len(modes))
for i,s in enumerate(pair):
 ax[0].bar(x+(i-.5)*.36,[S[s]['mode_seconds'].get(m,0)/3600 for m in modes],.36,label=s)
 f=F[s];ax[1].plot(f.time_sec/3600,f.battery_wh*4,label=s)
ax[0].set(xticks=x,xticklabels=modes,ylabel='Left-held duration (h)');ax[0].tick_params(axis='x',rotation=60);ax[0].legend(fontsize=7)
ax[1].set(xlabel='Elapsed hours (24 h)',ylabel='Battery / 25 Wh (%)');ax[1].legend(fontsize=7);save(fig,'day_occupancy_battery',pair)
fig,ax=plt.subplots(1,3,figsize=(10,3.6))
for i,s in enumerate(pair):
 r=S[s];ax[0].bar(np.arange(3)+(i-.5)*.35,[r['saa_s'],r['detection_in_saa_s'],r['acquisition_gate_s']],.35,label=s)
 ax[1].bar(np.arange(2)+(i-.5)*.35,[r['contact_s'],r['contacts']['relay_overlap_s']],.35)
 ax[2].bar(i,r['transferred_source_mb'])
ax[0].set(xticks=range(3),xticklabels=['SAA','Detection\nin SAA','Gate'],ylabel='Exposure (s; 24 h)');ax[0].legend(fontsize=6)
ax[1].set(xticks=range(2),xticklabels=['Visibility','Relay overlap'],ylabel='Contact time (s; 24 h)')
ax[2].set(xticks=range(2),xticklabels=['LEOP','No LEOP'],ylabel='Native transfer (source MB; 24 h)');save(fig,'day_exposure_contacts',pair)
fig,ax=plt.subplots(figsize=(7,2.8));x=np.arange(3)
for i,s in enumerate(pair):ax.bar(x+(i-.5)*.35,[S[s]['event_mode_seconds'].get(m,0) for m in ['COLD_AND_DARK','DETUMBLE','SLEWING']],.35,label=s)
ax.set(xticks=x,xticklabels=['Cold and Dark','Detumble','All Slewing'],ylabel='Transition-log duration (s; 24 h)');ax.legend(fontsize=8);save(fig,'startup',pair)
s='leop_1yr';r=S[s];day=pd.read_csv(OUT/(s+'_daily.csv'))
fig,ax=plt.subplots(3,1,figsize=(9,7),sharex=True)
ax[0].plot(day.day,day.acquisition_s,label='Acquisition gate');ax[0].plot(day.day,day.saa_s,label='Geographic SAA',alpha=.7);ax[0].set_ylabel('Daily exposure (s)');ax[0].legend(fontsize=8)
ax[1].fill_between(day.day,day.battery_min_wh*4,day.battery_max_wh*4,alpha=.5);ax[1].set_ylabel('Battery / 25 Wh (%)')
ax[2].plot(day.day,day.contact_s,label='Visibility');ax[2].plot(day.day,day.relay_s,label='Relay overlap');ax[2].set(ylabel='Daily contact (s)',xlabel='Elapsed day (365-day recorded span)');ax[2].legend(fontsize=8);save(fig,'annual_exposure_battery_contacts',[s])
fig,ax=plt.subplots(1,2,figsize=(9,3.5));ax[0].bar(modes,[r['mode_seconds'].get(m,0)/86400 for m in modes]);ax[0].tick_params(axis='x',rotation=60);ax[0].set_ylabel('Left-held mode duration (days)')
ax[1].plot(day.day,np.cumsum(day.acquisition_s)/3600,label='Acquisition gate');ax[1].plot(day.day,np.cumsum(day.saa_s)/3600,label='Geographic SAA');ax[1].set(xlabel='Elapsed day (365-day span)',ylabel='Cumulative exposure (h)');ax[1].legend(fontsize=8);save(fig,'annual_modes_cumulative',[s])
fig,ax=plt.subplots(2,1,figsize=(9,5),sharex=True);ax[0].plot(day.day,day.generated_source_mb,label='Generated');ax[0].plot(day.day,day.delivered_source_mb,label='Transferred');ax[0].set_ylabel('Native source MB/day');ax[0].legend(fontsize=8)
ax[1].plot(day.day,day.storage_max_source_mb);ax[1].ticklabel_format(axis='y',useOffset=False);ax[1].set(xlabel='Elapsed day (365-day span)',ylabel='Peak native store (source MB)');save(fig,'annual_native_data',[s])
fig,ax=plt.subplots(figsize=(9,3.7))
for tier in ['MMSC','MSC','EMSC']:
 q=pd.read_csv(OUT/(s+'_'+tier+'_3_queue.csv'));ax.step(q.end_s/86400,q.queue_after_bytes/1024,where='post',label=tier+' after contact')
ax.set(xlabel='Elapsed day (365-day span)',ylabel='Ideal v3 remaining queue (KiB)',title='Contact-end backlog only; within-contact peaks reported separately');ax.legend();save(fig,'annual_v3_queue',[s])
dump(OUT/'figure_manifest.json',manifest)
