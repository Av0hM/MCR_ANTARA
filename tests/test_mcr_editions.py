"""Bounded presentation and baseline checks; not spacecraft validation."""
import hashlib
import json
import re
import unittest
from pathlib import Path
from scripts.render_mcr_editions import narrative_requirement, render_narrative
from scripts.render_section3_requirements import GROUPS, tex

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/'data/derived/dual_editions_2026-11-09'
class EditionsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline=json.loads((AUDIT/'baseline_manifest.json').read_text())
        cls.rows=json.loads((ROOT/'config/requirements/section3_feasibility_v1.json').read_text())['requirements']
    def test_full_matrices_unchanged(self):
        for p,h in self.baseline['source_hashes'].items():
            if p.startswith('sections/requirements/'):
                self.assertEqual(hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),h,p)
    def test_all_shared_technical_sources_unchanged(self):
        changed={'main.tex','.latexmkrc','README.md','sections/03_spacecraft_architecture.tex','scripts/render_section3_requirements.py'}
        for p,h in self.baseline['source_hashes'].items():
            if p not in changed:self.assertEqual(hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),h,p)
    def test_all_constraints_and_evidence_preserved(self):
        for slug,subs,_ in GROUPS:
            text=(ROOT/f'sections/narrative/{slug}.tex').read_text()
            for r in self.rows:
                if r['subsystem'] in subs:
                    self.assertIn(tex(narrative_requirement(r['requirement'])),text,r['id'])
                    self.assertIn(tex(r['evidence']),text,r['id'])
    def test_no_matrices_or_status_legends_in_narrative(self):
        for p in (ROOT/'sections/narrative').glob('*.tex'):
            s=p.read_text()
            for forbidden in [r'\begin{table}',r'\begin{longtable}','Mission Feasibility Requirements',r'\label{req:',r'\textit{Status:']:
                self.assertNotIn(forbidden,s)
    def test_same_shared_entrypoint(self):
        for n in ['main_requirements.tex','main_narrative.tex']:
            self.assertIn(r'\input{main}',(ROOT/n).read_text())
        self.assertIn(r'\requirementseditiontrue',(ROOT/'edition.tex').read_text())
        self.assertIn(r'\def\ANTARANarrative{1}',(ROOT/'main_narrative.tex').read_text())
    def test_generator_idempotence(self):
        before={p:p.read_bytes() for p in (ROOT/'sections/narrative').glob('*.tex')}
        render_narrative()
        self.assertTrue(all(p.read_bytes()==b for p,b in before.items()))
    def test_inventory_covers_every_baseline_table(self):
        rows=json.loads((AUDIT/'table_inventory.json').read_text())
        for p in (AUDIT/'baseline/sections').rglob('*.tex'):
            count=len(re.findall(r'\\begin\{(?:table|longtable)\}',p.read_text()))
            source=str(p.relative_to(AUDIT/'baseline'))
            self.assertEqual(count,sum(r['source']==source for r in rows),source)
    def test_raw_assets_and_old_pdf_preserved(self):
        for p,h in {**self.baseline['asset_hashes'],**self.baseline['existing_pdf_hashes']}.items():
            self.assertEqual(hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),h,p)
