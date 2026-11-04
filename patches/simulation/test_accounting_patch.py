"""Run with ANTARA_SOURCE_ROOT pointing to original or patched source checkout.
AST extraction avoids executing the expensive MCR study at import time.
"""
import ast
import os
from pathlib import Path
from types import SimpleNamespace
import unittest
import numpy as np
import math

ROOT=Path(os.environ['ANTARA_SOURCE_ROOT'])
SCIENCE=ROOT/'src/simulations/ditl/ANTARA_Science_Sim.py'
POWER=ROOT/'src/simulations/power/ANTARA_MCR.py'

class Repairs(unittest.TestCase):
    def test_environment_is_spectral_density(self):
        tree=ast.parse(SCIENCE.read_text())
        method=next(n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='compute_flux')
        method.returns=None
        for arg in method.args.args: arg.annotation=None
        namespace={'np':np,'math':math}
        exec(compile(ast.fix_missing_locations(ast.Module(body=[method],type_ignores=[])),str(SCIENCE),'exec'),namespace)
        fake=SimpleNamespace(saa_depth_factor=lambda *a:1,magnetic_pitch_angle_deg=lambda *a:0,ew_asymmetry_factor=lambda *a:1,get_ap9_flux=lambda *a:np.array([2.,3.]),config=SimpleNamespace(detector_efficiency=[1.,.5],detector_dead_time_sec=.1,detector_dark_count_rate_hz=5,storm_time_flux_multiplier=2),PITCH_EXPONENT=1,geometric_factor_cm2sr=2,n_channels=2)
        result=namespace['compute_flux'](fake,0,0,600,None,None,None)
        self.assertNotIn('count_rate',result)
        np.testing.assert_array_equal(result['spectral_rate_density_hz_per_mev'],[4,3])
    def test_curtailed_energy_not_throughput(self):
        source=POWER.read_text(); start=source.index('            battery_energy += delta_energy') if '            battery_energy += delta_energy' in source else source.index('            accepted_delta_energy =')
        end=source.index('            soc = (',start)
        import textwrap
        ns=dict(battery_energy=25.,battery_capacity_remaining=25.,BATTERY_CAPACITY=25.,delta_energy=10.,throughput_wh=0.)
        exec(textwrap.dedent(source[start:end]),ns)
        self.assertEqual(ns['throughput_wh'],0)
        self.assertEqual(ns['battery_energy'],25)
    def test_summary_preserves_all_raan_groups_and_extreme(self):
        source=POWER.read_text()
        self.assertIn('"mean_run_min_soc"',source)
        self.assertIn('"worst_min_soc"',source)
        self.assertIn('np.min(raan_min_soc)',source)
        tree=ast.parse(source)
        loops=[n for n in tree.body if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='RAAN']
        self.assertEqual(len(loops),1)
        self.assertTrue(any(isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=='stats_rows' and n.func.attr=='append' for n in ast.walk(loops[0])))
    def test_effective_bin_metadata(self):
        source=SCIENCE.read_text()
        self.assertIn('"effective_bin_intervals_mev"',source)
        self.assertIn('effective_bin_intervals[1:3] = [None, None]',source)

if __name__=='__main__': unittest.main()
