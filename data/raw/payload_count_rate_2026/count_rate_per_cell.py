#!/usr/bin/env python3
"""
Per-cell detector count rate from SPENVIS-style integral flux maps.

Assumes the flux_<E>MeV columns are INTEGRAL fluxes (>E) in cm^-2 s^-1
(omnidirectional). The flux above an arbitrary threshold is obtained by
log-E / log-flux interpolation between the two bracketing columns (linear in
flux for a cell where either bracket value is zero).

Count rate (unit efficiency, unit geometric factor):
    rate_omni  = flux(>E_th) * 1 cm^2            [counts/s]
    rate_per_sr = rate_omni / (4*pi)             [counts/s, G = 1 cm^2 sr, isotropic]

Usage:
    python count_rate_per_cell.py PROTON.csv ELECTRON.csv -o out.csv
    python count_rate_per_cell.py p.csv e.csv --p-thresh 5.5 --e-thresh 0.35
"""
import argparse
import re

import numpy as np
import pandas as pd


def energy_columns(df):
    """Return (energies [MeV], column names) sorted by energy."""
    pairs = []
    for c in df.columns:
        m = re.fullmatch(r"flux_([0-9.]+)MeV", c)
        if m:
            pairs.append((float(m.group(1)), c))
    pairs.sort()
    return np.array([p[0] for p in pairs]), [p[1] for p in pairs]


def flux_above(df, e_th):
    """Integral flux above e_th (MeV) for every row of df."""
    E, cols = energy_columns(df)
    F = df[cols].to_numpy(float)
    if e_th <= E[0]:
        return F[:, 0].copy()          # below grid: use lowest bin (lower bound)
    if e_th >= E[-1]:
        return F[:, -1].copy()
    j = np.searchsorted(E, e_th)       # E[j-1] <= e_th <= E[j]
    if np.isclose(E[j], e_th):
        return F[:, j].copy()
    E0, E1 = E[j - 1], E[j]
    F0, F1 = F[:, j - 1], F[:, j]
    t = np.log(e_th / E0) / np.log(E1 / E0)
    out = F0 * (1 - t) + F1 * t        # linear fallback (handles zeros)
    both = (F0 > 0) & (F1 > 0)
    out[both] = np.exp(np.log(F0[both]) * (1 - t) + np.log(F1[both]) * t)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("protons", help="proton flux CSV")
    ap.add_argument("electrons", help="electron flux CSV")
    ap.add_argument("-o", "--output", default="count_rate_per_cell.csv")
    ap.add_argument("--p-thresh", type=float, default=5.5, help="proton threshold, MeV")
    ap.add_argument("--e-thresh", type=float, default=0.35, help="electron threshold, MeV")
    args = ap.parse_args()

    p = pd.read_csv(args.protons)
    e = pd.read_csv(args.electrons)
    key = ["datetime_mjd", "alt_km", "lat_deg", "lon_deg"]
    if len(p) != len(e) or not (p[key].values == e[key].values).all():
        raise SystemExit("Proton and electron files do not share the same cells/order.")

    out = p[key].copy()
    out["proton_rate"] = flux_above(p, args.p_thresh)
    out["electron_rate"] = flux_above(e, args.e_thresh)
    out["total_rate"] = out["proton_rate"] + out["electron_rate"]
    for c in ("proton", "electron", "total"):
        out[f"{c}_rate_per_sr"] = out[f"{c}_rate"] / (4 * np.pi)

    out.to_csv(args.output, index=False, float_format="%.6g")

    w = np.cos(np.deg2rad(out["lat_deg"]))
    print(f"Wrote {len(out)} cells -> {args.output}")
    print(f"Thresholds: protons > {args.p_thresh} MeV, electrons > {args.e_thresh} MeV\n")
    for c in ("proton_rate", "electron_rate", "total_rate"):
        print(f"{c:14s} mean={out[c].mean():.4g}  cos(lat)-wtd mean={np.average(out[c], weights=w):.4g}"
              f"  max={out[c].max():.4g}")
    i = out["total_rate"].idxmax()
    print(f"\nPeak total rate cell: lat={out.lat_deg[i]}, lon={out.lon_deg[i]}, "
          f"{out.total_rate[i]:.4g} counts/s (omni, G=1 cm^2)")


if __name__ == "__main__":
    main()
