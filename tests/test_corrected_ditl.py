"""Bounded software accounting checks, not detector/hardware qualification."""
import json,unittest,tempfile
from pathlib import Path
import numpy as np
from scripts.validate_corrected_ditl import selected,windows,daily,sha,OUT,ROOT
from scripts.science_record_v3 import capacity,backlog,intersect,readings,assign_events,poisson_fraction
class CorrectedTests(unittest.TestCase):
 def test_unique_selection(self):
  for s in ['leop_24h','no_leop_24h','leop_1yr']:self.assertTrue(selected(s,verify=False)['run_id'].startswith('corrected_'))
 def test_ambiguous_rejected(self):
  r={'scenario':'x','authoritative_for_report':True,'status':'VALIDATED'}
  with self.assertRaises(ValueError):selected('x',{'runs':[r,r]},False)
 def test_superseded_rejected(self):
  with self.assertRaises(ValueError):selected('x',{'runs':[{'scenario':'x','authoritative_for_report':True,'status':'SUPERSEDED EVIDENCE'}]},False)
 def test_hash_mismatch(self):
  with self.assertRaises(ValueError):selected('x',{'runs':[{'scenario':'x','authoritative_for_report':True,'status':'VALIDATED','files':[{'path':'README.md','sha256':'bad'}]}]},True)
 def test_sha(self):
  import hashlib
  self.assertEqual(sha(ROOT/'README.md'),hashlib.sha256((ROOT/'README.md').read_bytes()).hexdigest())
 def test_nonuniform_intervals(self):
  self.assertEqual(windows(np.array([0,2,22]),np.array([2,20,0]),np.array([True,True,True])),[(0,22)])
 def test_daily_split(self):self.assertEqual(list(daily([(86399,86402)],2)),[1,2])
 def test_visibility_relay_only(self):
  service=intersect([(0,10)],[(5,15)]);self.assertEqual(service,[(5,10)]);self.assertEqual(capacity(5),12000)
 def test_no_derating(self):self.assertEqual(capacity(514),1233600)
 def test_queue_and_outage(self):
  a=backlog([(1,292),(2,292)],[(5,6)]);b=backlog([(1,292),(2,292)],[])
  self.assertEqual(a['transferred_bytes'],584);self.assertEqual(b['remaining_bytes'],584)
 def test_overflow(self):self.assertEqual(backlog([(1,584)],[],storage_bytes=292)['dropped_bytes'],292)
 def test_short_zero_and_conservation(self):
  intervals=readings(0,3,[1,2],3);self.assertEqual(sum(b-a for a,b in intervals),3)
  self.assertEqual(sum(map(sum,assign_events([],[],intervals))),0)
  self.assertEqual(sum(map(sum,assign_events([0,1,2],[0,1,2],intervals))),3)
  self.assertIsNone(poisson_fraction(0));self.assertEqual(poisson_fraction(100),.1)
 def test_corrected_horizons_and_units(self):
  for sc,h in [('leop_24h',86400),('no_leop_24h',86400),('leop_1yr',31536000)]:
   s=json.loads((OUT/(sc+'_summary.json')).read_text());self.assertEqual(s['duration_s'],h);self.assertAlmostEqual(sum(s['mode_seconds'].values()),h)
   self.assertTrue(s['epoch'].startswith('2000-03-01'));self.assertAlmostEqual(s['minimum_soc_pct_at_planning25Wh'],s['battery_min_wh']*4)
   self.assertLess(s['storage_balance_max_residual_source_mb'],1e-10)
 def test_tier_exposure_queue_conservation(self):
  for sc in ['leop_24h','no_leop_24h','leop_1yr']:
   s=json.loads((OUT/(sc+'_summary.json')).read_text())
   for t in s['tiers']:self.assertEqual(t['bytes'],292*t['records']);self.assertAlmostEqual(t['exposure_s'],s['acquisition_gate_s'])
   for q in s['queues']:self.assertEqual(q['generated_bytes'],q['transferred_bytes']+q['remaining_bytes']+q['dropped_bytes'])
 def test_legacy_analysis_refuses(self):
  from scripts.validate_simulation_evidence import science
  with self.assertRaisesRegex(RuntimeError,'Superseded'):science('leop_1yr')

 def test_bad_timestamps(self):
  from scripts.validate_corrected_ditl import elapsed_weights
  for t in [[0,2,2],[0,2,1],[1,2],[0,float('nan')]]:
   with self.assertRaises(ValueError):elapsed_weights(t)
 def test_truncated_horizon(self):
  from scripts.validate_corrected_ditl import named_horizon_status
  self.assertEqual(named_horizon_status(4320020,31536000),'INCOMPLETE')
  self.assertEqual(named_horizon_status(31536000,31536000),'COMPLETE TIMESTAMP SPAN')
 def test_active_report_no_superseded_figure_or_raw_paths(self):
  for folder in ['sections','appendices']:
   for p in (ROOT/folder).rglob('*.tex'):
    text=p.read_text()
    for forbidden in ['partial_annual_mode_exposure.png','partial_annual_storage.png','telemetry_v3_2026-11-09/bounded_queue.png','evidence/science_ditl/raw/']:
     self.assertNotIn(forbidden,text,str(p))
 def test_ditl_requirements_cite_current_summary(self):
  r=json.loads((ROOT/'config/requirements/section3_feasibility_v1.json').read_text())['requirements']
  for ident in ['ANT-OBC-FR-002','ANT-GSO-FR-003','ANT-COM-FR-001','ANT-EPS-FR-002']:
   row=next(x for x in r if x['id']==ident)
   self.assertIn('data/derived/ditl_correction_2026-11-09/leop_1yr_summary.json',row['evidence_paths'])
