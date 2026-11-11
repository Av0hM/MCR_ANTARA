"""Traceability/document invariants, not tests of spacecraft physical compliance."""
import hashlib,json,re,unittest
from pathlib import Path
from scripts.render_section3_requirements import GROUPS,tex
ROOT=Path(__file__).resolve().parents[1]
class RequirementsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=json.loads((ROOT/'config/requirements/section3_feasibility_v1.json').read_text())['requirements']
        cls.before=(ROOT/'data/derived/section3_requirements_2026-11-09/section3_before.tex').read_text()
        cls.after=(ROOT/'sections/03_spacecraft_architecture.tex').read_text()
    def test_unique_stable_ids(self):
        ids=[r['id'] for r in self.rows]
        self.assertEqual(len(ids),len(set(ids)));self.assertEqual(len(ids),51)
        self.assertTrue(all(re.fullmatch(r'ANT-[A-Z]+-FR-\d{3}',i) for i in ids))
    def test_exact_heading_structure(self):
        f=lambda s:re.findall(r'\\subsection\{([^}]+)\}',s)
        self.assertEqual(f(self.before)[:-1],f(self.after)[:-1]);self.assertEqual(f(self.after)[-1], "System Integration");self.assertEqual(len(f(self.after)),9)
    def test_feasibility_tables_use_result_columns(self):
        for slug,_,_ in GROUPS:
            text=(ROOT/f'sections/requirements/{slug}.tex').read_text()
            self.assertIn('Simulation / Analysis Result',text)
            self.assertIn('Feasibility Assessment',text)
            self.assertNotIn('Verify:',text)
    def test_all_tables_included_once(self):
        for slug,subs,title in GROUPS:
            self.assertEqual(self.after.count('\\subsystempresentation{'+slug+'}'),1)
            text=(ROOT/f'sections/requirements/{slug}.tex').read_text()
            self.assertIn('Mission Feasibility Requirements',text)
            self.assertIn('Feasibility assessment.',text)
    def test_exact_text_and_unique_labels(self):
        alltext='\n'.join((ROOT/f'sections/requirements/{slug}.tex').read_text() for slug,_,_ in GROUPS)
        for r in self.rows:
            self.assertEqual(alltext.count('\\label{req:'+r['id']+'}'),1)
            self.assertIn(tex(r['requirement']),alltext)
    def test_complete_traceability(self):
        fields=['parent_requirements','tier_relevance','mission_driver','evidence','evidence_paths','status','verification_method','evidence_scope','open_decision','concept_closure','pdr_verification','interface_or_budget','numerical_basis']
        for r in self.rows:
            for k in fields:self.assertTrue(r[k],(r['id'],k))
            self.assertIn(' shall ',r['requirement'])
            for p in r['evidence_paths']:self.assertTrue((ROOT/p).is_file(),p)
    def test_status_vocabulary_and_scope(self):
        allowed={'SUPPORTED','CONDITIONAL','OPEN','NOT MET','NOT EVALUATED'}
        for r in self.rows:
            self.assertIn(r['status'],allowed)
            if r['status']=='SUPPORTED':
                self.assertNotEqual(r['evidence_scope'],'Flight condition not yet qualified')
                self.assertIn('only',r['evidence_scope'])
            if r['status']=='NOT MET':self.assertIn('artifact',r['evidence_scope'])
    def test_mission_criteria_and_old_configs_preserved(self):
        hashes=json.loads((ROOT/'data/derived/section3_requirements_2026-11-09/baseline_hashes.json').read_text())
        for p,h in hashes.items():
            if p in ['main.tex','main.pdf'] or p.startswith('config/'):
                data=(ROOT/p).read_bytes()
                if p == 'main.tex':
                    data=data.replace(b'\\input{edition}\n',b'').replace(b'{\\sffamily\\color{AntaraGrey}\\MCREditionName\\par}\n',b'')
                self.assertEqual(hashlib.sha256(data).hexdigest(),h,p)
    def test_no_arbitrary_science_or_link_threshold(self):
        r={r['id']:r for r in self.rows}
        self.assertIn('no arbitrary minimum duration or count',r['ANT-PLD-FR-011']['requirement'])
        self.assertIn('no arbitrary derating',r['ANT-COM-FR-001']['requirement'])
        self.assertIn('19200',r['ANT-COM-FR-001']['requirement'])
        self.assertIn('dead time',r['ANT-PLD-FR-006']['requirement'])
    def test_channel_ambiguity_explicit(self):
        r=next(r for r in self.rows if r['id']=='ANT-PLD-FR-003')
        self.assertIn('≥4',r['evidence']);self.assertEqual(r['status'],'OPEN')
    def test_no_duplicate_requirement_text(self):
        t=[r['requirement'] for r in self.rows];self.assertEqual(len(t),len(set(t)))
    def test_supported_not_whole_subsystem(self):
        self.assertEqual({r['id'] for r in self.rows if r['status']=='SUPPORTED'}, {'ANT-COM-FR-001','ANT-PLD-FR-010','ANT-INT-FR-001'})
        self.assertEqual(next(r['status'] for r in self.rows if r['id']=='ANT-OBC-FR-002'),'CONDITIONAL')
        self.assertTrue(any(r['concept_blocker'] for r in self.rows))

if __name__=='__main__':unittest.main()
