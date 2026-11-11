"""Validate the editorial revision without treating prose changes as physics changes."""
import collections, hashlib, json, re, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'data/derived/feasibility_editorial_2026-11-09'
BUILD=ROOT/'tmp/pdfs/feasibility'
def normalized(s):
    s=re.sub(r'PROJECT ANTARA[^\n]*\n','',s)
    s=re.sub(r'(Requirements|Narrative) Edition\s+\d+\s*/\s*\d+','',s)
    s=re.sub(r'Table\s+\d+','Table N',s)
    return re.sub(r'\s+','',s)
def body(text,start,end):
    # Headings in the contents carry page numbers, whereas body headings do not.
    a=re.search(r'^'+re.escape(start)+r'\s*$',text,re.M).end()
    b=re.search(r'^'+re.escape(end)+r'\s*$',text[a:],re.M).start()+a
    return text[a:b]
def main():
    checks={};texts={};logs={}
    for ed in ['requirements','narrative']:
        pdf=BUILD/ed/f'main_{ed}.pdf'
        texts[ed]=subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True)
        log=pdf.with_suffix('.log').read_text()
        logs[ed]=re.findall(r'^.*(?:Overfull \\[hv]box|undefined references|undefined citations|multiply defined|Missing character|LaTeX Error).*$',log,re.M)
        checks[ed+'_clean_build']=not logs[ed]
    for n,start,end in [(4,'4 Integrated Mission Feasibility','5 Feasibility, Risk and Engineering Budgets'),(5,'5 Feasibility, Risk and Engineering Budgets','A Detailed Technical Supporting Analysis')]:
        checks[f'section_{n}_identical']=normalized(body(texts['requirements'],start,end))==normalized(body(texts['narrative'],start,end))
    checks['no_requirement_matrices_in_narrative']='Mission Feasibility Requirements:' not in texts['narrative']
    checks['no_subsystem_ids_in_narrative']=not re.search(r'ANT-\w+-\s*FR-',texts['narrative'])
    rows=json.loads((ROOT/'config/requirements/section3_feasibility_v1.json').read_text())['requirements']
    before=json.loads((BASE/'before/config/requirements/section3_feasibility_v1.json').read_text())['requirements']
    checks['all_51_requirements_and_ids_unchanged']=rows==before and len(rows)==51
    pattern=r'\\begin\{longtable\}.*?\\end\{longtable\}'
    checks['all_10_science_tables_verbatim']=re.findall(pattern,(BASE/'before/sections/01_mission_context.tex').read_text(),re.S)==re.findall(pattern,(ROOT/'sections/01_mission_context.tex').read_text(),re.S)
    manifest=json.loads((BASE/'protected_manifest.json').read_text())
    changed=[p for p,h in manifest.items() if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h]
    checks['all_config_evidence_and_media_unchanged']=not changed
    table=lambda s: s[s.index('Recorded timestamp span'):s.index('\\bottomrule',s.index('Recorded timestamp span'))]
    old=table((BASE/'before/sections/corrected_ditl/operations.tex').read_text())
    new=table((ROOT/'sections/corrected_ditl/operations.tex').read_text())
    new='\n'.join(x for x in new.split('\n') if not x.startswith(('Cold and Dark','Detumble')))
    checks['existing_ditl_result_rows_verbatim']=old==new
    for n in ['leop_24h','no_leop_24h','leop_1yr']:
        d=json.loads((ROOT/f'data/derived/ditl_correction_2026-11-09/{n}_summary.json').read_text())
        checks[n+'_mode_accounting_complete']=sum(d['mode_seconds'].values())==d['duration_s']
    from scripts.render_section3_requirements import tex
    from scripts.feasibility_editorial import evidence
    from scripts.render_mcr_editions import narrative_requirement
    for ed in ['requirements','narrative']:
        s='\n'.join(p.read_text() for p in (ROOT/f'sections/{ed}').glob('*.tex'))
        checks[ed+'_all_obligations_and_results']=all(tex(r['requirement'] if ed=='requirements' else narrative_requirement(r['requirement'])) in s and tex(evidence(r)) in s for r in rows)
    result={'checks':checks,'protected_file_count':len(manifest),'changed_protected_files':changed,'build_issues':logs}
    (BASE/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    if not all(checks.values()):raise SystemExit(1)
if __name__=='__main__':main()
