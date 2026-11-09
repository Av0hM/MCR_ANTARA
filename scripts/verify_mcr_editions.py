"""Compare compiled editions and preserve a machine-readable evidence report."""
import argparse, collections, hashlib, json, re, subprocess, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def extract(pdf):
    return subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True)

def normalize(s, tables=False):
    s=re.sub(r'PROJECT ANTARA[^\n]*\n','',s)
    s=re.sub(r'Source transcription \| Technical review pending[^\n]*','',s)
    if tables:s=re.sub(r'Table\s+\d+','Table NUMBER',s)
    return re.sub(r'\s+','',s)

def start(pages,title):
    pattern=re.compile(r'^'+re.escape(title)+r'[ \t]*$',re.M)
    matches=[i for i,p in enumerate(pages) if pattern.search(p)]
    assert len(matches)==1,(title,matches)
    return matches[0]

def image_hashes(pdf):
    with tempfile.TemporaryDirectory(prefix='antara-edition-images-') as d:
        subprocess.run(['pdfimages','-all',str(pdf),str(Path(d)/'img')],check=True,capture_output=True)
        return collections.Counter(hashlib.sha256(p.read_bytes()).hexdigest() for p in Path(d).iterdir())

def main():
    ap=argparse.ArgumentParser()
    for k in ['requirements','narrative','default','baseline']:ap.add_argument('--'+k,required=True,type=Path)
    ap.add_argument('--output',type=Path,default=ROOT/'data/derived/dual_editions_2026-11-09/comparison.json')
    a=ap.parse_args();pdfs={k:getattr(a,k).resolve() for k in ['requirements','narrative','default','baseline']}
    texts={k:extract(v) for k,v in pdfs.items()};pages={k:v.split('\f') for k,v in texts.items()}
    section={}
    for k in ['requirements','narrative']:
        section[k]={n:start(pages[k],t) for n,t in [(1,'1 Mission Context, Objectives, and Success Criteria'),(3,'3 Spacecraft Architecture and Ground Segment'),(4,'4 Integrated Mission Feasibility')]}
    checks={}
    checks['requirements_matches_previous_pdf_except_edition_label']=normalize(texts['requirements']).replace('RequirementsEdition','')==normalize(texts['baseline'])
    checks['default_matches_requirements']=normalize(texts['default'])==normalize(texts['requirements'])
    slices={}
    for k in ['requirements','narrative']:
        p=pages[k];ix=section[k]
        slices[k]={'sections_1_2':'\f'.join(p[ix[1]:ix[3]]),'section_3':'\f'.join(p[ix[3]:ix[4]]),'sections_4_through_appendices':'\f'.join(p[ix[4]:])}
    for name in ['sections_1_2','sections_4_through_appendices']:
        checks[name+'_compiled_text_equal']=normalize(slices['requirements'][name],True)==normalize(slices['narrative'][name],True)
    checks['requirements_captions_present']='Mission Feasibility Requirements:' in texts['requirements']
    checks['narrative_has_no_requirement_captions']='Mission Feasibility Requirements:' not in texts['narrative']
    checks['narrative_has_no_formal_requirement_ids']=not re.search(r'ANT-\w+-\s*FR-',texts['narrative'])
    # Every numeric lexeme in all 51 obligation/evidence fields must occur in
    # both compiled Section 3 versions; source tests separately preserve full semantics.
    rows=json.loads((ROOT/'config/requirements/section3_feasibility_v1.json').read_text())['requirements']
    needed=set(re.findall(r'\d+(?:\.\d+)?',' '.join(r['requirement']+' '+r['evidence'] for r in rows)))
    missing={}
    for k in ['requirements','narrative']:
        s=normalize(slices[k]['section_3']).replace(',','')
        missing[k]=sorted(x for x in needed if x not in s)
        checks[k+'_all_register_numeric_lexemes_in_compiled_section3']=not missing[k]
    images={k:image_hashes(pdfs[k]) for k in ['requirements','narrative']}
    checks['embedded_raster_assets_identical']=images['requirements']==images['narrative']
    # Figure/equation/TikZ source identity is checked by source-hash regression.
    logs={}
    for k in ['requirements','narrative','default']:
        log=pdfs[k].with_suffix('.log')
        s=log.read_text(errors='replace')
        errors=re.findall(r'^.*(?:Overfull \\[hv]box|undefined references|undefined citations|multiply defined|LaTeX Error).*$' ,s,re.M)
        logs[k]=errors;checks[k+'_no_overflow_or_reference_errors']=not errors
    report={'checks':checks,'page_counts':{k:len([p for p in v if p.strip()]) for k,v in pages.items()},'section_start_pdf_pages':{k:{str(n):i+1 for n,i in v.items()} for k,v in section.items()},'required_numeric_lexemes':sorted(needed),'missing_numeric_lexemes':missing,'embedded_raster_objects':{k:sum(v.values()) for k,v in images.items()},'pdfs':{k:{'path':str(v),'sha256':hashlib.sha256(v.read_bytes()).hexdigest()} for k,v in pdfs.items()},'log_errors':logs,'normalization':'Remove running header/footer and whitespace; shared body comparisons additionally ignore table caption/reference numbers. No scientific values are normalized.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'checks':checks,'pages':report['page_counts'],'missing':missing},indent=2))
    if not all(checks.values()):raise SystemExit('Edition comparison failed')
if __name__=='__main__':main()
