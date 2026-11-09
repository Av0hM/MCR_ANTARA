"""Fast count-rate evidence regressions; no IRENE, transport or orbit run."""
import copy
from datetime import datetime, timedelta
import math
from pathlib import Path
import tempfile
import unittest

from scripts.validate_count_rate_evidence import (
    RAW, KEYS, align_rows, audit, index_rows, interpolate_integral,
    isotropic_rate, read_irene, validate_spectrum,
)


def row(lon):
    return dict(zip(KEYS, [61041., 600., -20.25, lon]))


class CountRateTests(unittest.TestCase):
    def test_power_law_interpolation(self):
        self.assertAlmostEqual(interpolate_integral([1., 10.], [100., 1.], math.sqrt(10)), 10.)

    def test_exact_thresholds(self):
        for e, expected in [(1., 100.), (2., 20.), (10., 1.)]:
            self.assertEqual(interpolate_integral([1., 2., 10.], [100., 20., 1.], e), expected)

    def test_near_threshold_not_snapped(self):
        self.assertGreater(interpolate_integral([1., 2., 10.], [100., 20., 1.], 2.-1e-6), 20.)

    def test_outside_threshold_rejected(self):
        for e in [0., -1., .9, 10.1, 100., math.nan, math.inf]:
            with self.subTest(e=e), self.assertRaises(ValueError):
                interpolate_integral([1., 10.], [100., 1.], e)

    def test_zero_flux(self):
        self.assertEqual(interpolate_integral([1., 10.], [0., 0.], 5.), 0.)
        self.assertEqual(isotropic_rate(0.), 0.)

    def test_one_zero_log_energy_linear_flux_fallback(self):
        self.assertAlmostEqual(interpolate_integral([1., 100.], [100., 0.], 10.), 50.)

    def test_extreme_finite_flux(self):
        value = interpolate_integral([1., 100.], [1e300, 1e-300], 10.)
        self.assertAlmostEqual(value, 1., places=10)
        self.assertTrue(math.isfinite(isotropic_rate(1e308)))
        self.assertGreater(interpolate_integral([1., 100.], [1e-300, 1e-302], 10.), 0.)

    def test_invalid_flux_rejected(self):
        for f in [-1., math.nan, math.inf]:
            with self.subTest(f=f), self.assertRaises(ValueError):
                interpolate_integral([1., 10.], [f, 0.], 5.)

    def test_invalid_energy_grids(self):
        for energies, flux in [([], []), ([1., 1.], [2., 1.]), ([2., 1.], [2., 1.]),
                               ([0., 1.], [2., 1.]), ([1., math.inf], [2., 1.]), ([1., 2.], [1.])]:
            with self.subTest(energies=energies), self.assertRaises(ValueError):
                validate_spectrum(energies, flux)

    def test_integral_monotonicity(self):
        with self.assertRaisesRegex(ValueError, 'increases'):
            validate_spectrum([1., 2.], [1., 2.])

    def test_units_and_four_pi_conversion(self):
        self.assertAlmostEqual(isotropic_rate(4*math.pi), 1.)
        self.assertAlmostEqual(isotropic_rate(4*math.pi, geometric_factor=2.), 2.)
        for unit in ['#/cm^2/s/MeV', '#/cm^2/s/sr']:
            with self.assertRaises(ValueError):
                isotropic_rate(1., flux_unit=unit)
        with self.assertRaises(ValueError):
            isotropic_rate(1., factor_unit='cm^2')

    def test_invalid_geometric_factor_and_overflow(self):
        for g in [-1., math.nan, math.inf]:
            with self.assertRaises(ValueError):
                isotropic_rate(1., geometric_factor=g)
        with self.assertRaises(ValueError):
            isotropic_rate(1e308, geometric_factor=1e308)

    def test_duplicate_coordinates_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            index_rows([row(-50.), row(-50.)])

    def test_missing_cells_rejected_even_if_both_inputs_missing(self):
        expected = index_rows([row(-50.), row(-49.5)])
        for p, e in [([row(-50.)], [row(-50.)]), ([row(-50.),row(-49.5)], [row(-50.)])]:
            with self.assertRaisesRegex(ValueError, 'Missing'):
                align_rows(p, e, expected)

    def test_extra_cell_rejected(self):
        with self.assertRaisesRegex(ValueError, 'extra'):
            align_rows([row(-50.), row(-49.5)], [row(-50.)], index_rows([row(-50.)]))

    def test_reordering_joins_by_full_key(self):
        p = [row(-50.), row(-49.5)]
        e = list(reversed(copy.deepcopy(p)))
        self.assertEqual([(a['lon_deg'],b['lon_deg']) for a,b in align_rows(p,e,index_rows(p))],
                         [(-50.,-50.),(-49.5,-49.5)])

    def test_epoch_altitude_and_coordinate_mismatch(self):
        for key,value in [('datetime_mjd',62137.),('alt_km',601.),('lat_deg',math.nan)]:
            e = row(-50.);e[key]=value
            with self.assertRaises(ValueError):
                align_rows([row(-50.)],[e],index_rows([row(-50.)]))
        self.assertEqual(datetime(1858,11,17)+timedelta(days=61041), datetime(2026,1,1))

    def test_raw_metadata_units_rejected(self):
        source = next(RAW.rglob('radiation_outputs_protons_final_mean_flux.txt'))
        text = '\n'.join(source.read_text().splitlines()[:15])
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.txt';p.write_text(text.replace('flux(#/cm^2/s)', 'flux(#/cm^2/s/MeV)'))
            with self.assertRaisesRegex(ValueError,'metadata/units'):
                read_irene(p,'AP9')

    def test_complete_archived_evidence_reproduction(self):
        with tempfile.TemporaryDirectory() as d:
            report=audit(RAW,Path(d))
        self.assertEqual(report['grid']['rows'],7940)
        self.assertTrue(report['raw_files_unchanged'])
        for case in ('mean','peak99'):
            self.assertTrue(report['cases'][case]['all_47640_rate_values_match_six_significant_digits'])
        self.assertEqual(report['ods']['data_rows'],7940)
        self.assertEqual(report['ods']['formulas'],1)


if __name__ == '__main__':
    unittest.main()
