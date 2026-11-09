"""Plot independently reproduced requirements; never a detector-response curve."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def main():
    d=ROOT/'data/derived/geometric_factor_2026-11-05_audit'
    fine=pd.read_csv(d/'required_G_fine_bins.csv');coarse=pd.read_csv(d/'required_G_coarse_channels.csv')
    fig,ax=plt.subplots(figsize=(7.1,3.5),layout='constrained')
    colors=['#136879','#b35b19']
    for target,color in zip([10,25],colors):
        ax.stairs(fine[f'G95_{target}pct'],list(fine.E_lo)+[fine.E_hi.iloc[-1]],color=color,label=f'{target}% Poisson uncertainty: fine intervals')
        for i,row in coarse.iterrows():
            ax.plot([row.E_lo,row.E_hi],[row[f'G95_{target}pct']]*2,color=color,ls='--',lw=2,label=f'{target}%: broad bands' if i==0 else None)
    ax.set(xscale='log',yscale='log',xlabel='Incident-spectrum energy interval (MeV)',ylabel=r'Required $G_{95}$ (cm$^2$ sr)',xlim=(5.4,100))
    ax.grid(alpha=.2,which='both');ax.legend(fontsize=8,ncol=2,loc='lower left',bbox_to_anchor=(0,1.02),frameon=False)
    fig.savefig(ROOT/'media/geometric_factor_requirements.png',dpi=220)
    plt.close(fig)
if __name__=='__main__':main()
