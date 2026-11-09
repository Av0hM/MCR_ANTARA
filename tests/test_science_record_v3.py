import binascii
import unittest
from scripts import science_record_v3 as v

class RecordTests(unittest.TestCase):
    def record(self):
        return dict(entry_us=1,exit_us=2,lat_e7=150000000,lon_e7=740000000,alt_mm=600000000,
                    histogram=[0]*64,sequence=42,status=v.status_marker('DETECTION',{k:3 for k in v.HEALTH}))
    def test_size_roundtrip_zero_counts(self):
        r=self.record();b=v.encode(r);self.assertEqual(len(b),292);self.assertEqual(v.decode(b),r)
    def test_crc_reference(self):self.assertEqual(binascii.crc_hqx(b'123456789',65535),0x29b1)
    def test_corrupt_crc(self):
        b=bytearray(v.encode(self.record()));b[40]^=1
        with self.assertRaises(ValueError):v.decode(b)
    def test_order(self):
        r=self.record();r['exit_us']=1
        with self.assertRaises(ValueError):v.encode(r)
    def test_float_expected_counts_rejected(self):
        r=self.record();r['histogram'][0]=.5
        with self.assertRaises(ValueError):v.encode(r)
    def test_status_codes(self):
        for mode in v.MODES:
            for code in range(4):
                health={k:code for k in v.HEALTH}
                self.assertEqual(v.decode_status(v.status_marker(mode,health)),dict(mode=mode,health=health))
    def test_reserved_mode(self):
        with self.assertRaises(ValueError):v.decode_status(7)
    def test_uint16_overflow(self):
        h=[0]*64;h[0]=65535;self.assertTrue(v.fits_uint16(h));h[0]+=1;self.assertFalse(v.fits_uint16(h))
    def test_uint32_overflow(self):
        r=self.record();r['histogram'][0]=2**32
        with self.assertRaises(ValueError):v.encode(r)
    def test_position_range(self):
        r=self.record();r['lon_e7']=1800000000
        with self.assertRaises(ValueError):v.encode(r)
    def test_one_two_three_boundaries(self):
        for b,n in [([],1),([1],2),([1,2],3)]:
            intervals=v.readings(0,3,b);self.assertEqual(len(intervals),n)
            self.assertEqual(sum(y-x for x,y in intervals),3)
            self.assertEqual(v.assign_events([0,1,2],[0,0,0],intervals)[0][0],intervals[0][1])
    def test_count_conservation(self):
        spans=v.readings(0,9,[3,6]);h=v.assign_events([0,3,5,6,8],[0,1,1,2,63],spans)
        self.assertEqual(sum(map(sum,h)),5);self.assertEqual([sum(x) for x in h],[1,2,2])
    def test_short_zero_count_valid(self):
        spans=v.readings(100,101,[]);self.assertEqual(spans,[(100,101)])
        self.assertEqual(v.assign_events([],[],spans),[[0]*64])
    def test_no_exposure(self):self.assertEqual(v.readings(1,1,[]),[])
    def test_unknown_timing(self):
        with self.assertRaises(ValueError):v.readings(1,4,None)
    def test_cell_boundaries_and_wrapping(self):
        self.assertNotEqual(v.cell_key(0,.99,1),v.cell_key(0,1,1))
        self.assertEqual(v.cell_key(0,180,1),v.cell_key(0,-180,1))
    def test_gap_no_event_duplication(self):
        with self.assertRaises(ValueError):v.assign_events([3],[0],[(0,2),(4,6)])
    def test_aggregated_poisson(self):
        self.assertAlmostEqual(v.poisson_fraction(25+25+50),.1)
        self.assertIsNone(v.poisson_fraction(0))
        self.assertGreater(v.poisson_fraction(25),v.poisson_fraction(100))
    def test_aos_los_relay_intersection(self):
        self.assertEqual(v.intersect([(0,10)],[(2,4),(6,11)]),[(2,4),(6,10)])
    def test_no_mask_penalty(self):self.assertEqual(v.capacity(514),1233600)
    def test_units(self):
        self.assertEqual(v.capacity(244016),585638400);self.assertEqual(256*1024//292,897)
        self.assertNotEqual(128*2**20,128*10**6)
    def test_queue_conservation(self):
        r=v.backlog([(1,292),(2,292),(6,292)],[(3,4)])
        self.assertEqual(r['generated_bytes'],r['transferred_bytes']+r['remaining_bytes'])
        self.assertEqual(r['remaining_bytes'],292)
    def test_relay_only(self):
        r=v.backlog([(0,50000)],v.intersect([(0,20)],[(10,11)]))
        self.assertEqual(r['transferred_bytes'],2400)
    def test_no_contact(self):self.assertEqual(v.backlog([(0,292)],[])['remaining_bytes'],292)
    def test_missed_contact(self):
        r=v.backlog([(0,292),(10,292)],[(11,12)])
        self.assertEqual(r['peak_required_bytes'],584)
    def test_storage_overflow(self):
        r=v.backlog([(0,584)],[],storage_bytes=292)
        self.assertEqual(r['dropped_bytes'],292);self.assertEqual(r['remaining_bytes'],292)
    def test_generation_during_contact(self):
        r=v.backlog([(0,100),(5,100),(10,100)],[(0,10)])
        self.assertEqual(r['transferred_bytes'],200);self.assertEqual(r['remaining_bytes'],100)
    def test_duplicate_windows(self):
        with self.assertRaises(ValueError):v.backlog([],[(0,3),(2,5)])
    def test_unknown_health_not_nominal(self):self.assertEqual(self.record()['status']>>4,4095)
    def test_record_conservation_decode(self):
        r=self.record();r['histogram']=list(range(64));self.assertEqual(sum(v.decode(v.encode(r))['histogram']),2016)


class EvidenceBudgetTests(unittest.TestCase):
    def test_historical_epoch_not_relabelled(self):
        import json
        from pathlib import Path
        p=Path(__file__).resolve().parents[1]/'data/derived/telemetry_v3_2026-11-09/gs_summary.json'
        r=json.loads(p.read_text())
        self.assertEqual(r['epochs'],['2000-03-01T00:00:00+00:00'])
        self.assertLess(r['relay_overlap_s'],r['duration_s'])
        self.assertEqual(r['relay_capacity_bytes'],v.capacity(r['relay_overlap_s']))
    def test_record_config_schema_agrees(self):
        import json
        from pathlib import Path
        p=Path(__file__).resolve().parents[1]/'config/science/science_record_v3.json'
        c=json.loads(p.read_text());self.assertEqual(c['record_bytes'],v.SIZE)
        self.assertEqual(c['mode_codes'],v.MODES)
        self.assertEqual(c['reading_policy']['minimum_duration'],'NONE imposed')
        self.assertIsNone(c['arbitrary_derating']);self.assertEqual(c['science_allocation'],1)
    def test_ordered_windows_reject_invalid_duration(self):
        with self.assertRaises(ValueError):v.intersect([(1,0)],[])
    def test_no_empty_record_on_shutdown(self):
        self.assertEqual(v.readings(3,3,[]),[])
        self.assertEqual(v.readings(3,4,[]),[(3,4)])
    def test_daily_interval_split(self):
        # One visibility contact spanning UTC midnight, no masking or lost endpoint.
        full=[(86399,86402)]
        left=v.intersect(full,[(0,86400)]);right=v.intersect(full,[(86400,172800)])
        self.assertEqual(sum(v.capacity(b-a) for a,b in left+right),7200)

class FragmentBudgetTests(unittest.TestCase):
    def test_source_segments_preserve_exposure_and_cell_visit_policy(self):
        import csv
        from pathlib import Path
        d=Path(__file__).resolve().parents[1]/'data/derived/telemetry_v3_2026-11-09'
        for tier in ['MMSC','MSC','EMSC']:
            seg=list(csv.DictReader((d/f'{tier}_acquisition_segments.csv').open()))
            self.assertEqual(sum(float(r['end_s'])-float(r['start_s']) for r in seg),342)
            self.assertTrue(all(float(a['end_s'])<=float(b['start_s']) for a,b in zip(seg,seg[1:])))
            visits={r['visit_id'] for r in seg}
            releases=list(csv.DictReader((d/f'{tier}_3_releases.csv').open()))
            self.assertEqual(len(releases),3*len(visits))
    def test_no_hardware_minimum_from_encoding_quantum(self):
        # One microsecond is merely an encodable fixture; hardware qualification is separate.
        self.assertEqual(v.readings(0,1,[]),[(0,1)])
        self.assertEqual(v.readings(0,2,[1]),[(0,1),(1,2)])

if __name__=='__main__':unittest.main()
