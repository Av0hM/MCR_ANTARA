import copy
import unittest
from scripts import fpdu_contracts as f

class RecordTests(unittest.TestCase):
    def setUp(self):
        c=f.current_configuration()
        self.r=dict(schema_version='FPDU-science-record-v1',timestamp_utc='2029-01-01T00:00:00Z',latitude_deg=-20,longitude_deg=-40,altitude_km=600,histogram_kind='observed_counts',histogram=[0]*64,bin_edges_id=c['science']['bin_edges_id'],bin_edges_mev=c['science']['bin_edges_mev'],metadata=dict(instrument_configuration=c['configuration_id'],calibration_version=None,response_model_version=None,quality_flags=['unqualified_response'],interval_duration_sec=1,livetime_sec=None))
    def test_valid_unqualified_logical_record(self): f.validate_science_record(self.r)
    def test_missing_channel(self):
        self.r['histogram'].pop()
        with self.assertRaises(ValueError): f.validate_science_record(self.r)
    def test_expected_vs_observed(self):
        self.r['histogram'][0]=.5
        with self.assertRaises(ValueError): f.validate_science_record(self.r)
        self.r['histogram_kind']='expected_counts';f.validate_science_record(self.r)
    def test_livetime_duration(self):
        self.r['metadata']['livetime_sec']=2
        with self.assertRaises(ValueError): f.validate_science_record(self.r)
    def test_bad_identity(self):
        self.r['bin_edges_id']='unversioned'
        with self.assertRaises(ValueError): f.validate_science_record(self.r)
    def test_coordinate_and_timestamp(self):
        for key,value in [('longitude_deg',180),('latitude_deg',91),('timestamp_utc','2029-01-01')]:
            r=copy.deepcopy(self.r);r[key]=value
            with self.assertRaises(ValueError): f.validate_science_record(r)
    def test_no_nonfinite_or_negative(self):
        for value in (float('nan'),-1):
            self.r['histogram'][0]=value
            with self.assertRaises(ValueError): f.validate_science_record(self.r)
    def test_public_validator_defaults_current(self):
        import subprocess,sys
        result=subprocess.run([sys.executable,str(f.ROOT/'scripts/validate_payload_config.py')],capture_output=True,text=True,check=True)
        self.assertIn('FPDU-2026-11-04-approved-v2 current input contract PASS',result.stdout)
    def test_report_current_timing_and_faces(self):
        s=(f.ROOT/'appendices/B_payload_detail_visual.tex').read_text()
        for token in ('0.11~mm per','6.22','eleven','200 ns','250$ ns','300$ ns','Qualified detector dead time & Unknown','EJ-550','358.920','975.659','optical isolation','Silicon removed'):
            self.assertIn(token,s)
        self.assertNotIn('Coincidence window width & 20 ns',s)

if __name__=='__main__': unittest.main()
