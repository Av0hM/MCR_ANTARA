"""Optional tests of OLD expected-count arithmetic, never new-geometry response.

Set ANTARA_LEGACY_SRC to a disposable copy of ANTARA_CODES-main/src and run
using its Orekit Python environment. Without it these tests explicitly skip.
No event reconstruction implementation exists to test for the new design.
"""
import os
import sys
import unittest
from types import SimpleNamespace

SOURCE = os.environ.get('ANTARA_LEGACY_SRC')
if SOURCE:
    sys.path.insert(0, SOURCE)
    import numpy as np
    import orekit
    orekit.initVM()
    from simulations.ditl import ANTARA_Science_Sim as science


@unittest.skipUnless(SOURCE, 'Set ANTARA_LEGACY_SRC to isolated legacy source copy')
class LegacyAccountingTests(unittest.TestCase):
    def sample(self, merge, seconds):
        c = science.MissionConfig(enable_periphery_bin_merge=merge,
                                 detector_dead_time_ns=0., detector_dark_count_rate_hz=0.)
        env = SimpleNamespace(PITCH_EXPONENT=2., compute_flux=lambda *a, **kw: {
            'saa_depth': .01, 'pitch_angle_deg': 0., 'ew_factor': 1.,
            'measured_flux': np.ones(5), 'ap9_flux': np.ones(5)})
        p = science.PayloadModel(c, env)
        _, result = p.generate_data(seconds, -25., -50., 600., np.ones(3), np.ones(3), np.ones(3))
        return p, result

    def test_zero_deadtime_preserves_expected_counts(self):
        p, result = self.sample(False, 2.)
        expected = p.geometric_factor_cm2sr * p.bin_efficiency_lookup * p.bin_widths_mev * 2.
        np.testing.assert_allclose(result['counts_per_bin'], expected, rtol=1e-13)
        self.assertAlmostEqual(sum(result['counts_per_bin']), sum(expected))

    def test_merge_conserves_histogram_and_pending_counts(self):
        plain, a = self.sample(False, 2.)
        merged, b = self.sample(True, 2.)
        self.assertAlmostEqual(sum(a['counts_per_bin']), sum(b['counts_per_bin']))
        self.assertAlmostEqual(b['counts_per_bin'][0], sum(a['counts_per_bin'][:3]))
        np.testing.assert_array_equal(b['counts_per_bin'][1:3], [0., 0.])
        cell = b['cell_id']
        np.testing.assert_allclose(merged._cell_histograms[cell], b['counts_per_bin'])
        np.testing.assert_allclose(merged._pending_bin_counts[cell], b['counts_per_bin'])

    def test_exposure_scaling(self):
        _, a = self.sample(False, 1.)
        _, b = self.sample(False, 4.)
        np.testing.assert_allclose(b['counts_per_bin'], np.array(a['counts_per_bin']) * 4.)
