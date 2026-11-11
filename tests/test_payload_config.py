"""Historical snapshot checks; current inputs are tested in test_fpdu_contracts.py."""
import copy
import json
import unittest
from scripts.validate_payload_config import CONFIG, ROOT, validate, material_volumes_mm3, require_qualified_response


class PayloadInputTests(unittest.TestCase):
    def setUp(self):
        self.c = json.loads(CONFIG.read_text())

    def test_historical_snapshot_contract(self):
        validate(self.c)

    def test_material_volumes_and_cm_conversion(self):
        v = material_volumes_mm3(self.c)
        self.assertEqual(v, dict(main_each=504, main_total=2520, front_total=72, total=2592))
        self.assertEqual(v['total'] / 1000, 2.592)
        self.assertIsNone(self.c['geometry']['packaged_dimensions_mm'])

    def test_shielding_conversion(self):
        s = self.c['conditional_peak_proton_rate']['shielding']
        self.assertEqual(s['thickness_um'] / 1000, s['thickness_mm'])
        self.assertEqual(s['material'], 'aluminium')

    def test_conditional_rate_contract(self):
        r = self.c['conditional_peak_proton_rate']
        self.assertEqual((r['value'], r['unit'], r['status']), (400, 'Hz', 'PRELIMINARY ESTIMATE'))
        self.assertEqual(r['incident_particles'], 'protons only')
        self.assertEqual(r['geometric_factor'], {'value': 1, 'unit': 'cm^2 sr'})
        self.assertEqual(r['assumed_detection_efficiency'], 1.)
        self.assertFalse(r['verified_electronics_limit'])
        self.assertFalse(r['all_particle_trigger_rate'])
        for field in ('generating_simulation', 'input_spectrum', 'calculation', 'epoch'):
            self.assertIsNone(r[field])

    def test_reject_area_only_or_unconditional_rate(self):
        for field, value in [('status', 'CONFIRMED DESIGN INPUT'), ('geometric_factor', {'value': 1, 'unit': 'cm^2'}), ('verified_electronics_limit', True)]:
            c = copy.deepcopy(self.c)
            c['conditional_peak_proton_rate'][field] = value
            with self.assertRaises(ValueError):
                validate(c)

    def test_coincidence_is_not_qualified_deadtime(self):
        e = self.c['electronics']
        self.assertEqual(e['coincidence_window_ns'], 20)
        self.assertEqual(e['tentative_readout_dead_time_ns'], 20)
        self.assertIsNone(e['readout_dead_time_ns'])
        self.assertEqual(e['dead_time_status'], 'REQUIRES VALIDATION')
        self.assertEqual(e['processor_selection']['mcu_budget_reference_ns'], 250)
        self.assertFalse(e['serial_latency_sum_authorized'])
        c = copy.deepcopy(self.c)
        c['electronics']['readout_dead_time_ns'] = 20
        with self.assertRaises(ValueError):
            validate(c)

    def test_no_invented_optics_or_channel_topology(self):
        self.assertEqual(self.c['optical_coupling']['material'], 'EJ-550 optical coupling grease')
        for k in ('assembly_arrangement', 'axis_orientation', 'optical_segmentation', 'readout_channel_count'):
            self.assertIsNone(self.c['geometry'][k])
        self.assertTrue(self.c['geometry']['active_silicon_entrance_retained'])
        self.assertTrue(self.c['geometry']['rear_penetration_detector_retained'])
        self.assertFalse(self.c['geometry']['rear_is_unconditional_veto'])

    def test_reject_legacy_and_unqualified_rev21_response(self):
        for response in ('legacy_L1_L5', 'Rev_2.1_single_block', 'FPDU-2026-11-04', None):
            with self.assertRaisesRegex(ValueError, 'REQUIRES VALIDATION'):
                require_qualified_response(self.c, response)

    def test_report_estimate_keeps_assumptions_together(self):
        for path in ('appendices/B_payload_detail_visual.tex',):
            paragraphs = (ROOT / path).read_text().split('\n\n')
            rate_paragraphs = [p for p in paragraphs if '400~Hz' in p]
            self.assertEqual(len(rate_paragraphs), 1)
            for token in ('PRELIMINARY ESTIMATE', 'protons only', '250~', '0.25~mm', 'aluminium', '1~cm', 'sr', '100\\%', 'efficiency'):
                self.assertIn(token, rate_paragraphs[0])


if __name__ == '__main__':
    unittest.main()
