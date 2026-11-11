"""Render the Section 3 requirements from one versioned register; no model changes."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/'config/requirements/section3_feasibility_v1.json'
GROUPS=[('eps',['EPS'],'Electrical Power System (EPS)'),('com',['COM'],'Communications System (COMMS)'),('pld',['PLD'],'Scientific Payload'),('adcs',['ADCS'],'Attitude Determination and Control System (ADCS)'),('obc',['OBC'],'On-Board Computer (OBC)'),('int',['INT'],'Spacecraft Coordinate System'),('thermal_structural',['THM','STR'],'Thermal and Structural Configuration'),('gso',['GSO'],'Ground Segment and Mission Operations'),('sys',['SYS'],'System Integration')]
STATUS={'SUPPORTED':'S','CONDITIONAL':'C','OPEN':'O','NOT MET':'NM','NOT EVALUATED':'NE'}
try:
    from .feasibility_editorial import ASSESS, assessment, evidence
except ImportError:
    from feasibility_editorial import ASSESS, assessment, evidence

def tex(s):
    s=s.replace('\\','\\textbackslash{}')
    for a,b in [('&',r'\&'),('%',r'\%'),('_',r'\_'),('#',r'\#'),('$',r'\$')]:s=s.replace(a,b)
    return s

def write_if_changed(path, text):
    """Avoid needless rebuilds and partial generated files in parallel builds."""
    if path.exists() and path.read_text() == text:
        return
    import os, tempfile
    with tempfile.NamedTemporaryFile(mode='w', dir=path.parent, delete=False) as f:
        f.write(text)
        temporary = f.name
    os.replace(temporary, path)


def render():
    req=json.loads(REG.read_text())['requirements']
    for slug,subs,title in GROUPS:
        rows=[r for r in req if r['subsystem'] in subs]
        out='% Generated from config/requirements/section3_feasibility_v1.json.\n'
        for chunk_index in range(0,len(rows),3):
            chunk=rows[chunk_index:chunk_index+3]
            out+=r"\begin{table}[H]\centering\small\setlength{\tabcolsep}{3pt}"+'\n'
            if chunk_index:out+=r'\ContinuedFloat\captionsetup{list=no}'+'\n'
            continuation=' (continued)' if chunk_index else ''
            out+='\\caption{Mission Feasibility Requirements: '+tex(title)+continuation+'}'
            if not chunk_index:out+='\\label{tab:fr-'+slug+'}'
            out+='\n'+r"\begin{tabular}{@{}"+'\n'
            for fraction in [44,32,24]:
                out+=r'>{\RaggedRight\arraybackslash}p{\dimexpr(\linewidth-4\tabcolsep)*'+str(fraction)+r'/100\relax}'+'\n'
            out+='@{}}\n'+r'\toprule Requirement & Simulation / Analysis Result & Feasibility Assessment\\\midrule'+'\n'
            for r in chunk:
                prefix,num=r['id'].rsplit('-FR-',1)
                ident=r'\mbox{'+prefix+r'-}\newline\mbox{FR-'+num+'}'
                result=tex(evidence(r))
                out+=r'\phantomsection\label{req:'+r['id']+'}'+ident+r'\par '+tex(r['requirement'])+' & '+result+' & '+tex(assessment(r)).replace('CONDITIONALLY SUPPORTED', r'CONDITIONALLY\newline SUPPORTED').replace('SUPPORTED BY SIMULATION', r'SUPPORTED BY\newline SIMULATION')+r'\\'+'\n\\addlinespace[3pt]\n'
            out+='\\bottomrule\n\\end{tabular}\n\\end{table}\n'
        out+=r'\paragraph{Feasibility assessment.} '+tex(ASSESS[slug])+'\n'
        write_if_changed(ROOT/f'sections/requirements/{slug}.tex', out)
    # Structured central traceability, kept outside main narrative to avoid duplication.
    md='# Subsystem requirement traceability register\n\nSource of truth: `config/requirements/section3_feasibility_v1.json`. Generated tables use the exact requirement text. S is not flight qualification. Existing Section 1 MM-M/MS-M/EM-M IDs remain authoritative; child rows are allocations, not new success tiers.\n'
    for r in req:
        md+='\n## '+r['id']+' — '+r['status']+'\n\n'+r['requirement']+'\n\n'
        for key,label in [('parent_requirements','Parent requirement'),('tier_relevance','Tier relevance'),('mission_driver','Mission driver'),('interface_or_budget','Interface / budget'),('evidence','Existing evidence'),('evidence_scope','Evidence scope'),('verification_method','Verification method'),('open_decision','Open decision'),('concept_closure','MCR closure'),('pdr_verification','PDR verification')]:md+='- **'+label+':** '+r[key]+'\n'
        md+='- **Sources:** '+', '.join('`'+p+'`' for p in r['evidence_paths'])+'\n'
        md+='- **Concept-level blocker:** '+('Yes' if r['concept_blocker'] else 'No; retain scope/interface obligation')+'\n'
    write_if_changed(ROOT/'docs/audit/SUBSYSTEM_REQUIREMENT_TRACEABILITY.md', md)

if __name__=='__main__':render()
