# Geometric-factor numerical validation

## Reproduced results

Independent implementation: `scripts/validate_geometric_factor.py`. Supplied implementation rerun separately into `/tmp/antara-gfactor-audit/original/`. No original outputs overwritten. All 4 coarse and 63 fine rows reproduce; largest absolute differences across all numeric fields are 1.99e-13 and 8.18e-14 respectively. Original-script rerun also matches supplied tables (≤8.18e-14).

R_unit = [F_omni(>E_low) − F_omni(>E_high)]/(4π), with units s⁻¹/(cm² sr). Multiplying by G [cm² sr], dimensionless efficiency and exposure [s] gives expected counts. The omnidirectional interpretation is the study assumption supported by its candidate pipeline; absent raw IRENE headers prevent independent verification of that upstream semantic. No additional energy width or solid angle is multiplied into these **integral differences**. Subtracting the >100 MeV tail is necessary; the ≥5 MeV headline includes that tail and is not the 5–100 MeV science rate.

N_required = 1/σ²; G_required = N_required/(R_unit ε T). The 10/15/25/50% targets correspond to expected counts 100/44.444…/16/4. These are Poisson counting proxies, not confidence guarantees for a random realized count or total reconstructed flux errors. Fractional expected-count targets are not rounded to integer observations.

| Incident band MeV | Selected cells | G95 10% | G95 15% | G95 25% | G95 50% | At G=0.3: 10% coverage |
|---|---:|---:|---:|---:|---:|---:|
| 5.4–10 | 7596 | 0.364535 | 0.162016 | 0.058326 | 0.014581 | 93.549% |
| 10–20 | 7177 | 0.413303 | 0.183690 | 0.066129 | 0.016532 | 92.253% |
| 20–40 | 7052 | 0.500042 | 0.222241 | 0.080007 | 0.020002 | 89.663% |
| 40–100 | 7144 | 0.360776 | 0.160345 | 0.057724 | 0.014431 | 93.253% |

All G values are cm² sr, ε=1, using the supplied unscaled per-cell dwell. Full precision, medians, peak rates and coverage at every target remain in the reproduced CSVs. At G=0.3 all four broad bands meet the 25% expected-count target in 100% of their respective selected sets; this is not coverage of every polygon cell or mission success.

## Input checks

- 7,940 unique cell keys: exact set equality, reordered by geographic bounds before joining; zero missing or duplicate cells. Bounds must be valid half-degree cells and canonical geographic coordinates. No silent inner-join loss or rounded-key aliasing.
- All 65 integral spectra finite, nonnegative and monotonically nonincreasing. Every supplied adjacent-band column matches integral subtraction. All flux-to-rate conversions agree within 5.69e-14 Hz absolute.
- NPY flags exactly match polygon membership, and rates match CSV values. Headline maximum 370.6584703683 Hz is >5 MeV, not the earlier >5.5 MeV proton maximum.
- Input grid has **65 points and 64 intervals**. At 5.4 MeV, 5–5.23961 is removed and 5.23961–5.49069 is truncated, leaving 63 rows. These are not 64 calibrated channels. The separate provisional telemetry schema has 65 edges for 64 bins over 5–100 MeV.
- Log-log threshold interpolation applies to positive endpoints; if an endpoint is zero, flux is interpolated linearly against log energy. Adjacent differences telescope exactly; splitting additionally at 10,20,40 MeV conserves rates/counts. Unsupported extrapolation is rejected.
- Each bin selects R ≥ 1% of **its own** peak; the 95th percentile is NumPy-style linear interpolation at rank 0.95(n−1). It is not a statistical confidence level and does not mean 95% joint multichannel coverage. Empirical coverage can differ from exactly 95% by order-statistic rounding/ties.

## Edge cases and confirmed script weaknesses

The source merge validates one-to-one duplicate keys but silently drops unmatched keys. Its rounded minimum-coordinate key ignores upper bounds and aliases malformed cells. It does not reject negative/nonmonotonic/nonfinite spectra or zero exposure. All-zero spectra select all cells under R≥0 and lead to invalid divisions. Below-grid queries clamp to the first threshold, above-grid queries return zero, permitting unsupported extrapolation. These do not affect the supplied valid positive dataset, but are confirmed unsafe behaviors for reuse. The independent audit rejects malformed inputs, preserves zero-exposure selected cells with infinite required G and zero count coverage, and explicitly marks an empty positive-rate population. The supplied code remains unchanged.

## Sensitivity and cutoff

Holding inputs fixed, G scales as 1/(εTσ²). Halving effective efficiency doubles required G; doubling **verified** exposure halves it. This algebra does not authorize mission-duration scaling. Fine-bin 10% G95 ranges from 3.928400 to 10.330093 cm² sr versus 0.360776–0.500042 for broad bands. At 25%, all requirements are 0.16 times the 10% values (fine: 0.628544–1.652815). Wider bands collect more incident counts; their differently selected populations prevent interpreting these ratios as universal per-cell gains.

Changing only the cutoff to 5.5 MeV yields first-band G95(10%)=0.380453683 and G95(25%)=0.060872589; 7,588 selected cells. This is a 4.3668% increase in G95, including the small eligibility change. Other broad bands are unchanged. The 5.4 MeV baseline is preserved; neither cutoff satisfies proof of the full committed 5–100 MeV calibrated response.

## Commands and test evidence

Use `/home/sammo/miniconda3/envs/orekit_env/bin/python` (P below), with `PYTHONDONTWRITEBYTECODE=1`:

```sh
P=/home/sammo/miniconda3/envs/orekit_env/bin/python
$P scripts/validate_geometric_factor.py --out data/derived/geometric_factor_2026-11-05_audit
$P evidence/geometric_factor_2026-11-05/required_geometric_factor.py --rates evidence/geometric_factor_2026-11-05/cell_proton_rates.csv --passes evidence/geometric_factor_2026-11-05/cell_pass_counts.csv --out /tmp/antara-gfactor-audit/original
$P -m pytest -q -p no:cacheprovider tests
MPLCONFIGDIR=/tmp/antara-gfactor-audit/mpl $P scripts/plot_geometric_factor_audit.py
```

Final suite: **107 passed, 3 skipped, 16 subtests passed**. Includes 36 new tests: interpolation/thresholds, malformed spectra/grid/cells/headers, zero and extreme rates, zero exposure, denominator/percentile, bin conservation, efficiency/exposure scaling, quadrature convergence, source quadrature equivalence, units and on/off-axis ray fixtures. Three optional legacy simulator tests lack their external source opt-in; they do not qualify production integration. Initial targeted run had one incorrect test expectation (10 s was insufficient for 100 counts); the fixture exposure was corrected to 100 s, with no algorithm change. Logs are retained in the derived audit directory. No transport or long-duration run performed.
