"""Figures use reproduced derived tables, not rerun mission simulations."""
from pathlib import Path
import json,csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(__file__).resolve().parents[1]/'data/derived/telemetry_v3_2026-11-09'
fig,ax=plt.subplots(figsize=(8,3.7))
rows=list(csv.DictReader((D/'historical_daily_capacity.csv').open()))
ax.plot([int(r['day']) for r in rows],[int(r['visibility_bytes'])/1e6 for r in rows],label='Visibility ceiling',lw=.8,color='#819ba7')
ax.plot([int(r['day']) for r in rows],[int(r['relay_bytes'])/1e6 for r in rows],label='Visibility ∩ Relay',lw=.9,color='#007f83')
ax.set(xlabel='Day since 2000-03-01 (365-day accounting window)',ylabel='Ideal capacity (decimal MB/day)',title='Historical event logs: 19.2 kbps, no throughput derating')
ax.legend(ncol=2,fontsize=8);ax.grid(alpha=.2);fig.tight_layout();fig.savefig(D/'historical_capacity.png',dpi=180);plt.close(fig)
fig,ax=plt.subplots(figsize=(8,3.3))
for tier in ['MMSC','MSC','EMSC']:
    release=list(csv.DictReader((D/f'{tier}_3_releases.csv').open()))
    service=list(csv.DictReader((D/f'{tier}_3_queue.csv').open()))
    # Plot exact change events; fluid drain endpoints approximated by full-window endpoints.
    # Release peaks and queue-at-contact-end are exact, use labels making interpolation explicit.
    events=[(float(r['time_s']),int(r['bytes'])) for r in release]
    events += [(float(r['end_s']),-int(r['transferred_bytes'])) for r in service if int(r['transferred_bytes'])]
    events.sort();x=[0];y=[0];total=0
    for t,n in events:total+=n;x.append(t/3600);y.append(total/1024)
    ax.step(x,y,where='post',label=tier)
ax.set(xlabel='Elapsed time (h; startup portion of incomplete 50-day telemetry)',ylabel='Queue (KiB)',title='Ideal v3 partition sensitivity; drainage credited at contact end')
ax.legend();ax.grid(alpha=.2);fig.tight_layout();fig.savefig(D/'bounded_queue.png',dpi=180);plt.close(fig)
