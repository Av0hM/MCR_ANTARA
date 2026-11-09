"""Bounded accounting/geometry tests; no detector qualification implied."""
import importlib.util
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from scripts.validate_geometric_factor import (align,band,cell_keys,interpolate,percentile,
    spectrum,table,square_g,midpoint_square_g,ray_lengths,read_csv,COARSE)

E=np.array([5.,10.,100.])
R=np.array([[100.,50.,5.],[20.,10.,1.]])

def cells():
    return pd.DataFrame(dict(lon_min_deg=[-60.,-59.5],lon_max_deg=[-59.5,-59.],lat_min_deg=[-20.,-20.],lat_max_deg=[-19.5,-19.5]))

def test_power_law_interpolation():
    np.testing.assert_allclose(interpolate(E,R,20),[25,5])

def test_zero_interpolation():
    np.testing.assert_allclose(interpolate([5,20],np.array([[10.,0.]]),10),[5])

@pytest.mark.parametrize('q',[0,4.9,100.1,float('nan')])
def test_extrapolation_rejected(q):
    with pytest.raises(ValueError): interpolate(E,R,q)

@pytest.mark.parametrize('r',[[[1,2,0]],[[1,-1,0]],[[1,np.inf,0]],[[1,np.nan,0]]])
def test_invalid_spectrum(r):
    with pytest.raises(ValueError): spectrum(E,r)

@pytest.mark.parametrize('e',[[5,5,100],[5,100,10],[-5,10,100]])
def test_invalid_energy_grid(e):
    with pytest.raises(ValueError): spectrum(e,R)

def test_missing_cell():
    with pytest.raises(ValueError,match='Missing'): align(cells(),cells().iloc[:1])

def test_duplicate_cell():
    with pytest.raises(ValueError,match='Duplicate'): cell_keys(pd.concat([cells(),cells().iloc[:1]]))

def test_order_independent():
    np.testing.assert_array_equal(align(cells(),cells().iloc[::-1]),cells())

@pytest.mark.parametrize('col,value',[('lon_min_deg',-59.99),('lon_max_deg',-59),('lat_max_deg',91)])
def test_bad_bounds(col,value):
    c=cells(); c.loc[0,col]=value
    with pytest.raises(ValueError): cell_keys(c)

def test_duplicate_headers(tmp_path):
    p=tmp_path/'bad.csv';p.write_text('a,a\n1,2\n')
    with pytest.raises(ValueError):read_csv(p)

def test_band_conservation():
    np.testing.assert_allclose(band(E,R,5,20,5.4)+band(E,R,20,100,5.4),band(E,R,5.4,100,5.4))

def test_cutoff():
    np.testing.assert_array_equal(band(E,R,5,5.3,5.4),[0,0])
    assert np.all(band(E,R,5,10,5.5)<band(E,R,5,10,5.4))

def test_percentile_linear():
    assert percentile([10,20,30,40],95)==38.5
    assert np.isinf(percentile([1,np.inf],95))
    assert percentile([1,np.inf],0)==1

def test_zero_exposure_retained():
    row=table(E,R,[0,100],[(5,10)]).iloc[0]
    assert row.n_cells==2 and np.isinf(row.G95_10pct)
    assert row['cov_at_G0.3_10pct']==.5

def test_zero_rate_empty_population():
    row=table(E,np.zeros_like(R),[1,1],[(5,10)]).iloc[0]
    assert row.n_cells==0 and np.isinf(row.G95_10pct)
    assert row['cov_at_G0.3_10pct']==0

def test_efficiency_exposure_scaling():
    a=table(E,R,[10,20],[(5,10)]).iloc[0]
    b=table(E,R,[10,20],[(5,10)],efficiency=.5).iloc[0]
    c=table(E,R,[20,40],[(5,10)]).iloc[0]
    assert b.G95_10pct==pytest.approx(2*a.G95_10pct)
    assert c.G95_10pct==pytest.approx(a.G95_10pct/2)
    assert a.G95_25pct==pytest.approx(.16*a.G95_10pct)

def test_extreme_finite_flux():
    row=table(E,R*1e100,[1,1],[(5,10)]).iloc[0]
    assert np.isfinite(row.G95_10pct) and row.G95_10pct>0

def test_bin_specific_denominator():
    r=np.array([[100.,99.,0.],[100.,0.,0.]])
    t=table(E,r,[1,1],[(5,10),(10,100)],cutoff=5)
    assert list(t.n_cells)==[2,1]

@pytest.mark.parametrize('s',[.02,.2,7.2])
def test_quadrature_convergence(s):
    assert square_g(.6,s,80)==pytest.approx(square_g(.6,s,160),rel=1e-9)
    assert midpoint_square_g(.6,s,480)==pytest.approx(square_g(.6,s),rel=1e-4)

def test_original_quadrature_equivalence():
    p=Path(__file__).resolve().parents[1]/'evidence/geometric_factor_2026-11-05/required_geometric_factor.py'
    spec=importlib.util.spec_from_file_location('supplied',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    assert m.g_squares(.6,.2,n=12)==pytest.approx(midpoint_square_g(.6,.2,12),rel=1e-13)

def test_units_and_aperture_limit():
    assert square_g(.6,0)==pytest.approx(np.pi*.36)
    assert square_g(6,72)==pytest.approx(100*square_g(.6,7.2))
    assert 250*1e-3==.25

def test_ray_on_axis():
    np.testing.assert_allclose(ray_lengths([0,0,0],[1,0,0]),[.2,1.4,1.4,1.4,1.4,1.4])

def test_ray_off_axis_exits_side():
    x=ray_lengths([0,0,0],[1,1,0])
    assert x.sum()==pytest.approx(.3*np.sqrt(2)) and x[-1]==0

def test_ray_miss():
    assert ray_lengths([0,1,0],[1,0,0]).sum()==0
