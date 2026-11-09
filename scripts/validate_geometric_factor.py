"""Independent, bounded audit of supplied idealized unit-G proton tables.
No transport, response, orbit extrapolation or mission-success decision.
"""
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
import numpy as np
import pandas as pd
from numpy.polynomial.legendre import leggauss

ROOT = Path(__file__).resolve().parents[1]
BOUNDS = ['lon_min_deg', 'lon_max_deg', 'lat_min_deg', 'lat_max_deg']
SIGMAS = (.10, .15, .25, .50)
COARSE = [(5.4, 10), (10, 20), (20, 40), (40, 100)]


def read_csv(path):
    with open(path, newline='') as f:
        header = next(csv.reader(f))
    if len(header) != len(set(header)):
        raise ValueError('Duplicate column headers')
    return pd.read_csv(path)


def cell_keys(frame):
    v = frame[BOUNDS].to_numpy(float)
    if not np.isfinite(v).all() or not np.equal(v * 2, np.round(v * 2)).all():
        raise ValueError('Nonfinite or off-grid coordinates')
    if not ((v[:, 1]-v[:, 0] == .5) & (v[:, 3]-v[:, 2] == .5)).all():
        raise ValueError('Invalid cell bounds')
    if not ((v[:, 0] >= -180) & (v[:, 1] <= 180) & (v[:, 2] >= -90) & (v[:, 3] <= 90)).all():
        raise ValueError('Coordinates outside canonical geographic bounds')
    keys = [tuple(x) for x in v]
    if len(set(keys)) != len(keys):
        raise ValueError('Duplicate geographic cells')
    return keys


def align(rates, passes):
    rk, pk = cell_keys(rates), cell_keys(passes)
    if set(rk) != set(pk):
        raise ValueError('Missing or extra geographic cells')
    index = {k: i for i, k in enumerate(pk)}
    return passes.iloc[[index[k] for k in rk]].reset_index(drop=True)


def spectrum(energies, rates):
    e, r = np.asarray(energies, float), np.asarray(rates, float)
    if e.ndim != 1 or len(e) < 2 or not np.isfinite(e).all() or (e <= 0).any() or (np.diff(e) <= 0).any():
        raise ValueError('Invalid energy grid')
    if r.ndim != 2 or r.shape[1] != len(e) or not np.isfinite(r).all() or (r < 0).any() or (np.diff(r, axis=1) > 0).any():
        raise ValueError('Nonfinite, negative or nonmonotonic integral spectrum')
    return e, r


def interpolate(e, r, energy):
    e, r = spectrum(e, r)
    if not np.isfinite(energy) or not e[0] <= energy <= e[-1]:
        raise ValueError('Threshold outside supported energy grid')
    j = int(np.searchsorted(e, energy))
    if e[j] == energy:
        return r[:, j].copy()
    w = np.log(energy/e[j-1])/np.log(e[j]/e[j-1])
    a, b = r[:, j-1], r[:, j]
    result = a*(1-w)+b*w
    positive = (a > 0) & (b > 0)
    result[positive] = np.exp(np.log(a[positive])*(1-w)+np.log(b[positive])*w)
    return result


def band(e, r, low, high, cutoff):
    if high <= low or not np.isfinite([low, high, cutoff]).all():
        raise ValueError('Invalid band')
    low = max(low, cutoff)
    if low >= high:
        return np.zeros(len(r))
    return interpolate(e, r, low)-interpolate(e, r, high)


def percentile(values, p):
    """Linear order-statistic quantile, retaining infinite zero-exposure requirements."""
    x = np.sort(np.asarray(values, float))
    if not len(x) or np.isnan(x).any() or not 0 <= p <= 100:
        raise ValueError('Invalid percentile population')
    h = (len(x)-1)*p/100
    i, j = int(np.floor(h)), int(np.ceil(h))
    if i == j or x[i] == x[j]:
        return float(x[i])
    if np.isinf(x[j]):
        return float('inf')
    return float(x[i]+(h-i)*(x[j]-x[i]))


def table(e, r, exposure, edges, cutoff=5.4, efficiency=1., peak_fraction=.01):
    spectrum(e, r)
    t = np.asarray(exposure, float)
    if t.shape != (len(r),) or not np.isfinite(t).all() or (t < 0).any():
        raise ValueError('Invalid exposure')
    if not np.isfinite(efficiency) or not 0 < efficiency <= 1 or not 0 <= peak_fraction <= 1:
        raise ValueError('Invalid efficiency or threshold')
    rows = []
    for lo, hi in edges:
        if hi <= cutoff:
            continue
        rate = band(e, r, lo, hi, cutoff)
        select = (rate > 0) & (rate >= peak_fraction*rate.max())
        rr = rate[select]
        row = dict(E_lo=max(lo, cutoff), E_hi=hi, n_cells=int(select.sum()),
                   peak_rate_Hz_perG=float(rate.max()), median_rate_Hz_perG=float(np.median(rr)) if len(rr) else np.nan)
        for s in SIGMAS:
            exposure_rate = rr * efficiency * t[select]
            need = np.full(len(rr), np.inf)
            np.divide(1/s**2, exposure_rate, out=need, where=exposure_rate > 0)
            tag = f'{round(s*100)}pct'
            row[f'G95_{tag}'] = percentile(need, 95) if len(rr) else np.inf
            row[f'Gmedian_{tag}'] = percentile(need, 50) if len(rr) else np.inf
            row[f'cov_at_G0.3_{tag}'] = float(np.mean(.3*exposure_rate >= 1/s**2)) if len(rr) else 0.
        rows.append(row)
    return pd.DataFrame(rows)


def square_g(side_cm, separation_cm, n=160):
    """Two aligned square planes; independent 2D overlap integral, cm² sr."""
    if side_cm <= 0 or separation_cm < 0 or n < 2:
        raise ValueError('Invalid ideal geometry')
    if separation_cm == 0:
        return float(np.pi*side_cm**2)
    x, w = leggauss(n)
    u = (x+1)*side_cm/2
    weights = w*side_cm/2
    s2 = separation_cm**2
    f = (side_cm-u[:,None])*(side_cm-u[None,:])*s2/(s2+u[:,None]**2+u[None,:]**2)**2
    return float(4*np.sum(f*weights[:,None]*weights[None,:]))


def midpoint_square_g(side, separation, n):
    # Algebraic reduction of the source n^4 quadrature; no transport assumption.
    k = np.arange(-n+1, n)
    d = k*side/n
    multiplicity = n-np.abs(k)
    return float(np.sum(multiplicity[:,None]*multiplicity[None,:]*separation**2 /
                        (separation**2+d[:,None]**2+d[None,:]**2)**2)*(side/n)**4)


def ray_lengths(origin, direction):
    """Gap-free six-box numerical fixture. u=-X inward, v=Y,w=Z; cm."""
    o, d = np.asarray(origin, float), np.asarray(direction, float)
    if o.shape != (3,) or d.shape != (3,) or not np.isfinite([o,d]).all() or np.linalg.norm(d) == 0:
        raise ValueError('Invalid ray')
    d = d/np.linalg.norm(d)
    depths = [0, .2, 1.6, 3., 4.4, 5.8, 7.2]
    lengths = []
    for a,b in zip(depths[:-1], depths[1:]):
        enter, leave = 0., np.inf
        for axis, low, high in [(0,a,b),(1,-.3,.3),(2,-.3,.3)]:
            if d[axis] == 0:
                if not low <= o[axis] <= high:
                    leave = -1
            else:
                t1,t2 = sorted(((low-o[axis])/d[axis], (high-o[axis])/d[axis]))
                enter,leave = max(enter,t1),min(leave,t2)
        lengths.append(max(0., leave-enter))
    return np.array(lengths)


def audit(source, out):
    from shapely.geometry import Polygon, box
    out.mkdir(parents=True, exist_ok=True)
    inventory = [dict(path=str(p.relative_to(source)), size=p.stat().st_size,
                      sha256=hashlib.sha256(p.read_bytes()).hexdigest(), scientific_evidence=p.suffix != '.pyc')
                 for p in sorted(source.rglob('*')) if p.is_file()]
    r, p = read_csv(source/'cell_proton_rates.csv'), read_csv(source/'cell_pass_counts.csv')
    p = align(r, p)
    for frame in (r,p):
        if not (frame.in_saa == 1).all():
            raise ValueError('Unexpected SAA flags')
    if not np.isfinite(p.pass_count).all() or (p.pass_count < 0).any() or (p.pass_count % 1 != 0).any():
        raise ValueError('Malformed pass counts')
    polygon = Polygon(json.loads((ROOT/'config/science/saa_polygon_v1.json').read_text())['vertices'])
    expected = {(float(x),float(x+.5),float(y),float(y+.5)) for x in np.arange(-90,-10,.5)
                for y in np.arange(-35,0,.5) if polygon.intersection(box(x,y,x+.5,y+.5)).area > 1e-12}
    if set(cell_keys(r)) != expected:
        raise ValueError('Polygon overlap membership differs')
    columns = sorted([(float(m[1]), c) for c in r.columns if (m := re.fullmatch(r'count_rate_ge_([\d.]+)MeV_hz', c))])
    e = np.array([v for v,c in columns]); rates = r[[c for v,c in columns]].to_numpy()
    spectrum(e,rates)
    unit_error = 0.
    for j,(energy,col) in enumerate(columns):
        fluxcol = col.replace('count_rate_ge_', 'flux_ge_').replace('MeV_hz','MeV_cm2s')
        expected_rate = r[fluxcol].to_numpy()/(4*np.pi)
        np.testing.assert_allclose(rates[:,j], expected_rate, rtol=2e-12, atol=1e-12)
        unit_error = max(unit_error, float(np.max(abs(rates[:,j]-expected_rate))))
    for c in r.columns:
        m = re.fullmatch(r'count_rate_([\d.]+)_([\d.]+)MeV_hz',c)
        if m:
            np.testing.assert_allclose(r[c], band(e,rates,float(m[1]),float(m[2]),5), rtol=2e-10,atol=1e-12)
    np.testing.assert_allclose(r.count_rate_hz,rates[:,0])
    grid,flags = np.load(source/'cell_proton_count_rate_hz.npy'),np.load(source/'cell_saa_flag.npy')
    assert grid.shape == flags.shape == (120,560)
    iy = ((r.lat_min_deg+50)*2).astype(int); ix = ((r.lon_min_deg+270)*2).astype(int)
    expected_flags = np.zeros_like(flags); expected_flags[iy,ix] = 1
    np.testing.assert_array_equal(flags,expected_flags)
    np.testing.assert_allclose(grid[iy,ix],r.count_rate_hz)
    result = dict(cells=len(r), energy_thresholds=len(e), dwell_sum_s=float(p.time_seconds.sum()),
                  dwell_min_s=float(p.time_seconds.min()),dwell_max_s=float(p.time_seconds.max()),
                  pass_min=int(p.pass_count.min()),pass_max=int(p.pass_count.max()),unit_max_abs_error=unit_error,
                  headline_peak_hz=float(r.count_rate_hz.max()), comparisons={})
    for name,edges in [('coarse_channels',COARSE),('fine_bins',list(zip(e[:-1],e[1:])) )]:
        computed = table(e,rates,p.time_seconds,edges)
        original = read_csv(source/f'required_G_{name}.csv')
        np.testing.assert_allclose(computed.to_numpy(),original[computed.columns].to_numpy(), rtol=2e-11,atol=2e-12)
        computed.to_csv(out/f'required_G_{name}.csv', index=False)
        result['comparisons'][name] = dict(rows=len(computed),max_abs_error=float(np.max(abs(computed.to_numpy()-original[computed.columns].to_numpy()))))
        if name == 'fine_bins':
            result['fine_G95_10pct_range'] = [float(computed.G95_10pct.min()),float(computed.G95_10pct.max())]
    table(e,rates,p.time_seconds,COARSE,cutoff=5.5).to_csv(out/'cutoff_5p5_coarse.csv',index=False)
    # Split at arbitrary coarse boundaries: telescope identity demonstrates conservation.
    split = sorted(set([5.4,10.,20.,40.,100.]+[float(v) for v in e if v>5.4]))
    summed = sum(band(e,rates,a,b,5.4) for a,b in zip(split[:-1],split[1:]))
    np.testing.assert_allclose(summed, band(e,rates,5.4,100,5.4),rtol=2e-12,atol=2e-12)
    geometry=[]
    for separation in [0,.02,.2,.48,1.6,3,4.4,5.8,7.2]:
        g = square_g(.6,separation)
        geometry.append(dict(separation_cm=separation,G_cm2_sr=g,G_n80=square_g(.6,separation,80),
                             midpoint_n30=midpoint_square_g(.6,separation,30) if separation else None))
    pd.DataFrame(geometry).to_csv(out/'ideal_square_geometry.csv',index=False)
    (out/'source_inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
    (out/'validation_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,default=ROOT/'evidence/geometric_factor_2026-11-05')
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    if args.out.resolve() == args.source.resolve() or args.source.resolve() in args.out.resolve().parents:
        parser.error('Output must be separate from original evidence')
    audit(args.source,args.out)
