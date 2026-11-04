"""Bounded software checks; none qualifies the physical FPDU."""
import copy
import csv
import json
import math
import unittest
from scripts import fpdu_contracts as f

class GeometryTests(unittest.TestCase):
    def setUp(self): self.c=f.current_configuration()
    def test_geometry(self):
        g=self.c['geometry']; m=g['main']; front=g['front']
        self.assertEqual(m['dimensions_xyz_mm'],[14,6,6]); self.assertEqual(m['quantity'],5)
        self.assertEqual(front['dimensions_xyz_mm'],[2,6,6])
        self.assertEqual(math.prod(m['dimensions_xyz_mm']),504)
        self.assertEqual(5*14, m['active_length_x_mm']); self.assertEqual(g['total_active_length_mm'],72)
        self.assertEqual((5*504+72)/1000,2.592); self.assertEqual(g['total_material_volume_mm3'],2592)
    def test_faces_and_coating(self):
        m=self.c['geometry']['main']; self.assertEqual(m['sipm_faces'],['+Y','-Y'])
        r=m['reflector']; self.assertEqual(r['faces'],['+Z','-Z']); self.assertEqual(r['thickness_per_face_mm'],.11)
        self.assertEqual(6+2*.11,r['coated_z_mm'])
    def test_sensors_and_unknown_optics(self):
        g=self.c['geometry']; self.assertEqual(5*g['main']['sipms_per_block']+g['front']['sipm_count'],11)
        self.assertFalse(g['silicon_entrance_detector']); self.assertEqual(g['rear_detector'],'optional_unselected')
        self.assertIsNone(g['optical_isolation']); self.assertIsNone(g['scintillator_material'])
        self.assertIsNone(g['front']['reflector_faces']); self.assertIsNone(self.c['electronics']['adc_channel_count'])
    def test_shield_and_environment(self):
        s=self.c['entrance_shielding']; self.assertEqual(s['thickness_um']/1000,s['thickness_mm'])
        e=self.c['environment']; self.assertEqual(e['geometric_factor_cm2_sr'],1)
        self.assertEqual(e['source_epoch_utc'],'2026-01-01T00:00:00Z'); self.assertFalse(e['shielding_in_rate_script'])
    def test_timing(self):
        e=self.c['electronics']
        for key,value in [('asic_shaping_time_ns',20),('coincidence_target_ns',200),('timing_allowance_min_ns',250),('preferred_timing_allowance_ns',300),('post_shaping_delay_ns',20)]: self.assertEqual(e[key],value)
        for key in ('qualified_detector_dead_time_ns','adc_conversion_latency_ns','digital_processing_latency_ns','processor_selected','max_trigger_rate_hz'): self.assertIsNone(e[key])
    def test_no_legacy_response(self):
        for response in ('legacy_L1_L5','Rev_2.1_single_block',self.c['configuration_id'],None):
            with self.assertRaises(ValueError): f.require_qualified_response(response)
    def test_schema_and_edges(self):
        c=self.c; self.assertEqual(len(c['science']['bin_edges_mev']),65)
        schema=json.loads((f.ROOT/'config/science/fpdu_histogram_v1.schema.json').read_text())
        self.assertEqual(schema['properties']['bin_edges_mev']['const'],c['science']['bin_edges_mev'])

class AccountingTests(unittest.TestCase):
    def test_flat_spectrum_dimensions(self): self.assertEqual(f.differential_counts([5,10,20],[2,2],3,.5,4),[60,120])
    def test_time_and_bin_invariance(self):
        a=sum(f.differential_counts([5,100],[2],1,1,10)); b=sum(f.differential_counts([5,10,20,100],[2,2,2],1,1,5))*2
        self.assertEqual(a,b)
    def test_missing_and_invalid_channels(self):
        for flux in ([1],[-1,1],[float('nan'),1]):
            with self.assertRaises(ValueError): f.differential_counts([5,10,20],flux,1,1,10)
    def test_histogram_conservation(self):
        h=f.histogram_reconstructed([4,5,10,100,101,float('nan')],[5,10,100])
        self.assertEqual(h,dict(histogram=[1,2],underflow=1,overflow=1,invalid=1))
    def test_effective_merged_width(self):
        m=f.merge_histogram([1,2,3],[5,10,20,40],[0,2,3]); self.assertEqual(m,dict(counts=[3,3],edges_mev=[5,20,40],widths_mev=[15,20]))
    def test_zero_deadtime(self): self.assertEqual(f.shared_nonparalyzable_rates([10,20],100,0),([10,20],1))
    def test_unknown_deadtime_rejected(self):
        with self.assertRaises(ValueError): f.shared_nonparalyzable_rates([10],100,None)
    def test_shared_deadtime_bin_invariance(self):
        a,l=f.shared_nonparalyzable_rates([100],1000,1000); b,_=f.shared_nonparalyzable_rates([50,50],1000,1000)
        self.assertEqual(sum(a),sum(b)); self.assertLess(l,1)
    def test_background_and_zero(self):
        self.assertIsNone(f.net_precision(0,0,0,0)); self.assertIsNone(f.net_precision(10,20,20,0)); self.assertGreater(f.net_precision(101,100,100,0),1)
    def test_battery_curtailment(self): self.assertEqual(f.battery_exchange(25,25,10),dict(stored_wh=25,throughput_wh=0,curtailed_wh=10,unserved_wh=0))
    def test_battery_depletion(self): self.assertEqual(f.battery_exchange(2,25,-5)['throughput_wh'],2)
    def test_soc_run_identity(self):
        s=f.run_soc_summary({(0,'a'):[.8,.7],(0,'b'):[.6,.5],(30,'a'):[.9,.8]})
        self.assertEqual(s[0]['worst_min_soc'],.5); self.assertEqual(s[0]['mean_run_min_soc'],.6); self.assertEqual(s[30]['worst_min_soc'],.8)

class CoverageTests(unittest.TestCase):
    def test_continuous_visit(self):
        v=f.VisitAccounting()
        for t in range(100): v.add(t,1,'a',True)
        self.assertEqual(v.cells['a']['visits'],1); self.assertEqual(len(v.cells['a']['passages']),1); self.assertEqual(v.cells['a']['science_sec'],100)
    def test_leave_reenter_same_pass(self):
        v=f.VisitAccounting()
        for t,c in enumerate(['a','b','a',None,'a']): v.add(t,1,c)
        self.assertEqual(v.cells['a']['visits'],3); self.assertEqual(len(v.cells['a']['passages']),2)
    def test_missing_interval(self):
        v=f.VisitAccounting(); v.add(0,1,'a')
        with self.assertRaises(ValueError): v.add(2,1,'a')
    def test_timestep_convergence(self):
        results=[]
        for dt in (1,.5,.25):
            v=f.VisitAccounting()
            for i in range(int(4/dt)): v.add(i*dt,dt,'a' if i*dt<2 else 'b',True)
            results.append(v.cells)
        self.assertEqual(results[0],results[1]); self.assertEqual(results[0],results[2])
    def test_wrapping_and_coarsening(self):
        self.assertEqual(f.cell_index(0,180,1),f.cell_index(0,-180,1))
        self.assertEqual(f.cell_index(-20.1,-40.1,5),f.cell_index(-20.9,-40.9,5))
    def test_polygon_counts_and_exact_raw_domain(self):
        p=json.loads((f.ROOT/'config/science/saa_polygon_v1.json').read_text())['vertices']
        for resolution,n in [(5,92),(1,2020),(.5,7940)]: self.assertEqual(len(f.polygon_cells(p,resolution)),n)
        expected=f.polygon_cells(p,.5)
        for name in ('mean','peak99'):
            with (f.ROOT/f'data/raw/payload_count_rate_2026/count_rate_per_cell_{name}.csv').open() as stream:
                keys=[(float(r['lat_deg']),float(r['lon_deg'])) for r in csv.DictReader(stream)]
            self.assertEqual(len(keys),len(set(keys))); self.assertEqual(set(keys),expected)
    def test_touching_boundary_excluded(self): self.assertEqual(f.clipped_area([(0,0),(1,0),(1,1),(0,1),(0,0)],1,2,0,1),0)
    def test_checkpoint_change_and_shapes(self):
        c=dict(epoch='2029',grid=[1],step_sec=1,response_id=None,input_hashes=['abc'],state_shapes=[2,3])
        h=f.checkpoint_identity(c); f.validate_checkpoint(h,c,[2,3])
        for key,value in [('epoch','2026'),('grid',[2]),('step_sec',2),('input_hashes',['def'])]:
            altered=dict(c,**{key:value})
            with self.assertRaises(ValueError): f.validate_checkpoint(h,altered,[2,3])
        with self.assertRaises(ValueError): f.validate_checkpoint(h,c,[3,2])
    def test_complete_and_incomplete(self):
        self.assertEqual(f.validate_complete_intervals([(0,1),(1,1),(2,0)],2),2)
        for rows in ([(0,1),(1,1)],[(0,1),(2,0)],[(0,1),(1.5,.5),(2,0)]):
            with self.assertRaises(ValueError): f.validate_complete_intervals(rows,2)

class TimingTests(unittest.TestCase):
    def test_unknown_capacity(self):
        r=f.timing_trade(504245.064); self.assertIsNone(r['queue_stable_mean']); self.assertIsNone(r['deadline_margin_ns'])
    def test_configurable_capacity_and_margin(self):
        r=f.timing_trade(500000,1000,1000,2000,50,100); self.assertEqual(r['processor_utilization'],.5); self.assertEqual(r['deadline_margin_ns'],850)
        self.assertFalse(f.timing_trade(500000,3000)['queue_stable_mean'])
    def test_zero_flux(self): self.assertEqual(f.queue_trace([],100,2)['accepted'],0)
    def test_burst_overflow(self): self.assertEqual(f.queue_trace([0,0,0,100],100,2),dict(accepted=3,lost=1,peak_occupancy=2,max_residence_ns=200))
    def test_no_artificial_zero_service_loss(self): self.assertEqual(f.queue_trace([0,0,0],0,1)['lost'],0)
    def test_unsorted_and_extreme(self):
        with self.assertRaises(ValueError): f.queue_trace([1,0],1,1)
        with self.assertRaises(ValueError): f.timing_trade(float('inf'),1)

if __name__=='__main__': unittest.main()
