"""Render the Section 3 requirements from one versioned register; no model changes."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/'config/requirements/section3_feasibility_v1.json'
GROUPS=[('eps',['EPS'],'Electrical Power System (EPS)'),('com',['COM'],'Communications System (COMMS)'),('pld',['PLD'],'Scientific Payload'),('adcs',['ADCS'],'Attitude Determination and Control System (ADCS)'),('obc',['OBC'],'On-Board Computer (OBC)'),('int',['INT'],'Spacecraft Coordinate System'),('thermal_structural',['THM','STR'],'Thermal and Structural Configuration'),('gso',['GSO'],'Ground Segment and Mission Operations'),('sys',['SYS'],'Outstanding MCR Evidence')]
STATUS={'SUPPORTED':'S','CONDITIONAL':'C','OPEN':'O','NOT MET':'NM','NOT EVALUATED':'NE'}
ASSESS={
'eps':'The fixed/deployable array and battery architecture provide a defined basis for energy analysis, not a closed energy margin. The 25 Wh planning value is not a permissible depth-of-discharge limit. Startup reserve, bus peaks and worst-RAAN/EOL depletion require allocations at concept level; component aging and transient qualification follow at PDR.',
'com':'Histogram-based return and scheduled Relay are consistent with the current architecture. Full-rate capacity arithmetic is model-supported; sustained generation, matched contact identity and the outage envelope remain prerequisites to concept-level data balance. Physical link margin, protocol behavior and net throughput require PDR verification.',
'pld':'The longitudinal scintillators and distributed SiPM readout define an inspectable payload concept; the record codec has bounded software evidence. Neither the stopping response nor effective geometric acceptance is calibrated. Material/optical interfaces, mixed-species trigger demand and qualified channels are concept-level feasibility gaps, not details that can be waived until qualification. The tier rows flow down Section 1 without replacing its criteria: MMSC uses at least two channels; MSC retains all operational channels and the comparison table\'s at-least-four statement pending reconciliation; EMSC retains its primary-map ≤15% rule, minimum three channels and two 9–10 month sub-period maps. The counting examples N≈4 and N≥16 do not replace full uncertainty or create a new confidence level.',
'adcs':'Reaction wheels plus magnetorquers address controlled pointing and momentum unloading without reviving the CMG selection. The single startup event and incompatible Monte Carlo summary do not establish a detumble reliability. Initial-condition, pointing, torque and timing allocations must be justified at concept level; representative closed-loop and hardware-in-loop validation then belongs to PDR.',
'obc':'The reference format makes the assembly and queue workloads concrete. A 256 KiB dedicated queue contains the small bounded fixture; this is not a total OBC RAM requirement. The 128 MiB candidate store fails the separate 187498164-byte no-downlink grid-retention sensitivity, but that unmatched sensitivity is not an approved retention mission case. Sustained workload, outage policy and total system memory must be allocated before unconditional feasibility; media and reset tests follow at PDR.',
'int':'The common frame aligns payload, antenna and array interfaces and is supported as a documented convention only. Alignment tolerance, time/position accuracy and electrical/command ICD ownership remain open derived allocations. These interfaces must be defined before integrated margins can be combined; calibration and installation surveys verify them later.',
 'thermal_structural':'The lumped thermal model and 3U packaging are useful concept representations. They do not establish component thermal compliance or launch structural integrity. Missing selected-component limits, coupled hot/cold cases, complete mass and provider load/interface limits prevent an unconditional concept-feasibility finding. SDM/deployables remain here under the existing combined heading. Correlated thermal-vacuum, modal, vibration and deployment qualification are PDR verification tasks after those allocations exist.',
'gso':'BITS Goa and the current mode sequence provide the planned operational path from exposure to received science. Historical contacts support opportunity calculations, not 2029 availability. The supplied annual evidence fails the complete, time-aligned verification obligation. Observation eligibility, qualified independent passes and sustained station/outage assumptions must be closed at concept level; end-to-end exercises then verify the ground chain.',
'sys':'The design-maturity statement above is conditional: missing essential allocations cannot all be deferred as detailed PDR work. Requirements marked S support only their stated reference/model scope; NM identifies the supplied annual evidence failure. The centralized register separates concept blockers from later qualification and records exact parents, interfaces and closure methods.'}

def tex(s):
    s=s.replace('\\','\\textbackslash{}')
    for a,b in [('&',r'\&'),('%',r'\%'),('_',r'\_'),('#',r'\#'),('$',r'\$')]:s=s.replace(a,b)
    return s

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
            for fraction in [13,42,13,23,9]:
                out+=r'>{\RaggedRight\arraybackslash}p{\dimexpr(\linewidth-8\tabcolsep)*'+str(fraction)+r'/100\relax}'+'\n'
            out+='@{}}\n'+r'\toprule ID & Requirement / acceptance condition & Mission driver & Evidence / verification & Status\\\midrule'+'\n'
            for r in chunk:
                prefix,num=r['id'].rsplit('-FR-',1)
                ident=r'\mbox{'+prefix+r'-}\newline\mbox{FR-'+num+'}'
                evidence=tex(r['evidence'])+r' \emph{Verify:} '+tex(r['verification_method'])+'.'
                out+=r'\phantomsection\label{req:'+r['id']+'}'+ident+' & '+tex(r['requirement'])+' & '+tex(r['mission_driver'])+' & '+evidence+' & '+STATUS[r['status']]+r'\\'+'\n\\addlinespace[3pt]\n'
            out+='\\bottomrule\n\\end{tabular}\n\\end{table}\n'
        out+=r'\textit{Status: S supported within stated scope; C conditional; O open; NM not met; NE not evaluated.}'+'\n'
        out+=r'\paragraph{Feasibility assessment.} '+tex(ASSESS[slug])+'\n'
        (ROOT/f'sections/requirements/{slug}.tex').write_text(out)
    # Structured central traceability, kept outside main narrative to avoid duplication.
    md='# Subsystem requirement traceability register\n\nSource of truth: `config/requirements/section3_feasibility_v1.json`. Generated tables use the exact requirement text. S is not flight qualification. Existing Section 1 MM-M/MS-M/EM-M IDs remain authoritative; child rows are allocations, not new success tiers.\n'
    for r in req:
        md+='\n## '+r['id']+' — '+r['status']+'\n\n'+r['requirement']+'\n\n'
        for key,label in [('parent_requirements','Parent requirement'),('tier_relevance','Tier relevance'),('mission_driver','Mission driver'),('interface_or_budget','Interface / budget'),('evidence','Existing evidence'),('evidence_scope','Evidence scope'),('verification_method','Verification method'),('open_decision','Open decision'),('concept_closure','MCR closure'),('pdr_verification','PDR verification')]:md+='- **'+label+':** '+r[key]+'\n'
        md+='- **Sources:** '+', '.join('`'+p+'`' for p in r['evidence_paths'])+'\n'
        md+='- **Concept-level blocker:** '+('Yes' if r['concept_blocker'] else 'No; retain scope/interface obligation')+'\n'
    (ROOT/'docs/audit/SUBSYSTEM_REQUIREMENT_TRACEABILITY.md').write_text(md)

if __name__=='__main__':render()
