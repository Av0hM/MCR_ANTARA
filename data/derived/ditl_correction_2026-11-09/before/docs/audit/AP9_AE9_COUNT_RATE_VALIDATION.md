> **Approved-baseline follow-up:** The original ingestion audit below is preserved. The unified implementation now accepts this 2026 source as a preliminary 2029 planning reference, verifies its exact polygon cell domain, and incorporates qualified statements in the MCR. See [count-rate reconciliation](FPDU_COUNT_RATE_RECONCILIATION.md) and [implementation record](IMPLEMENTATION_CHANGELOG.md). No raw rate or flux output was changed.

# AP9/AE9 count-rate validation — 2026-11-04

## Reproduction result

**PASS for arithmetic reproduction, not for detector qualification.** Independently parsed all four raw IRENE text outputs, checked metadata and spectra, compared all four converted flux CSVs exactly, and reproduced both rate tables. Each rate table contains 7,940 rows × six rate/proxy columns = **47,640 numerical values**, all matching the supplied six-significant-digit exports. Keys match without rounding. Separately executing the original count-rate script yielded byte-identical archived CSVs. Original files were never overwritten.

Products:

- [Independent mean reproduction](../../data/derived/payload_count_rate_2026_audit/reproduced_count_rate_per_cell_mean.csv)
- [Independent percentile-99 reproduction](../../data/derived/payload_count_rate_2026_audit/reproduced_count_rate_per_cell_peak99.csv)
- [Machine-readable statistics, inventory and checks](../../data/derived/payload_count_rate_2026_audit/validation_summary.json)
- [Independent validator](../../scripts/validate_count_rate_evidence.py) and [regression tests](../../tests/test_count_rate_evidence.py)

The independent implementation uses Python's standard library and raw text values, not imports of the supplied numerical functions. It preserves the arithmetic for valid in-range data but rejects unsafe inputs rather than reproducing the source script's silent boundary clamping.

## Calculation and units

Let F(>E) be integral omnidirectional flux in particles cm⁻² s⁻¹. For bracketing energies E₀ and E₁, the script sets

`t = ln(Ethreshold/E₀) / ln(E₁/E₀)`

and interpolates `F = exp[(1−t) ln F₀ + t ln F₁]` when both fluxes are positive. With either endpoint zero it uses `(1−t)F₀ + tF₁`: linear in flux, **still logarithmic in energy**, not linear in energy. This is a numerical spectral-shape approximation, not a transport model. Proton 5.5 MeV is bracketed by 3.75 and 5.6 MeV; electron 0.35 MeV by 0.25 and 0.4 MeV.

For isotropic directional intensity J, `Fomni = ∫J dΩ = 4π J`. With a defined geometric factor G in cm² sr, the ideal incident rate is `R = J G = Fomni G/(4π)`, in s⁻¹. Thus the `*_rate_per_sr` columns numerically represent **ideal isotropic rates for G=1 cm² sr and unit efficiency**. The column name is misleading: once G is applied, the rate is Hz, not Hz/sr. Without G, F/(4π) is directional intensity. Never apply both an angle-integrated G and a second solid-angle integral.

The `proton_rate`, `electron_rate` and `total_rate` columns are numerically the integral fluxes multiplied by a nominal 1 cm². They are **flux×area proxies**, not directional telescope rates. In particular, a one-sided ideal planar area A viewing an isotropic hemisphere has G=πA, yielding FA/4, not FA. The source's console label “G=1 cm²” confuses area with geometric factor. Preserve original column names for reproduction, but use explicit interpretation in any report.

There is no shield-thickness parameter, transmission function, material model, response matrix, optical calculation, rejection efficiency or dead-time correction in `count_rate_per_cell.py`. A sharp energy threshold, even if motivated elsewhere by a range estimate, is not a validated **250 µm aluminium** model. The two nine-line IRENE configs also contain no shielding specification. No evidence establishes upstream shield transport in these flux outputs.

## Numerical results

All values below are **2026-01-01, 600 km, sampled-grid ideal isotropic rates**, G=1 cm² sr, unit efficiency, **unshielded in this calculation**, protons >5.5 MeV and electrons >0.35 MeV. They are neither accepted-background nor electronics-trigger predictions. Values are independently calculated before CSV rounding.

| Input statistic / species | Grid maximum (Hz) | Maximum cell (latitude, longitude) | Unweighted grid mean (Hz) | cos(latitude)-weighted mean (Hz) |
|---|---:|---|---:|---:|
| Mean model, proton | 358.920119 | −30.75°, −49.25° | 130.780963 | 126.214519 |
| Mean model, electron | 67,779.655072 | −34.75°, −39.25° | 11,370.840831 | 10,747.874858 |
| Mean model, sum | 68,055.634723 | −34.75°, −39.25° | 11,501.621794 | 10,874.089377 |
| Percentile 99, proton | 975.658699 | −30.75°, −48.25° | 367.752907 | 355.080101 |
| Percentile 99, electron | 503,419.742516 | −34.75°, −39.25° | 88,218.501639 | 83,696.085970 |
| Sum of species percentile-99 proxies | 504,245.063602 | −34.75°, −39.25° | 88,586.254546 | 84,051.166071 |

The sum's maximum is evaluated at one common cell; it is not the sum of separate species maxima. The sum of two marginal 99th-percentile estimates is **not a demonstrated 99th percentile of their combined process**. Nor is a maximum across this grid a continuous-space or full-mission bound. The electron/summed maximum lies on the southern boundary of the sampled domain, so broader coverage is especially important. Spatial means, including cosine-weighted means, are not orbit dwell-time-weighted rates.

IRENE's mean and percentile modes describe static statistical flux maps; percentile values apply at a location and energy, not a mission-wide maximum guarantee. A temporal worst-case assessment requires an appropriate scenario analysis. See the [IRENE 1.58.001 User’s Guide, pp. 17–18](https://www.vdl.afrl.af.mil/programs/ae9ap9/files/package/IRENE_Users_Guide.pdf). No such new environment simulation was run here.

## Science energy interval

The archived calculation uses **F(>5.5 MeV)**, not `F(>5)−F(>100)`. It excludes 5–5.5 MeV protons while retaining the integral tail above 100 MeV. The largest exported proton threshold is 20 MeV; that does **not** truncate each integral flux at 20 MeV, but it prevents extracting F(>100) from these outputs. The source function silently returns F(>20) for a requested 100 MeV threshold, which would give an incorrect band subtraction. The new checker rejects out-of-grid requests.

As a labeled threshold-sensitivity calculation only, interpolating F(>5) yields ideal isotropic maxima **370.865743 Hz** (mean) and **1020.395368 Hz** (percentile 99), with the same respective proton-maximum cells. These are still integral-above-threshold values, not 5–100 MeV rates. Do not combine an AP-8 PDF's >100 MeV peak with an AP9 grid's >5 MeV value. For a proper science interval, request a matching >100 MeV threshold or a sufficiently resolved spectrum and fold the detector response. Differences of marginal percentile spectra also require care: percentile-of-band flux is not generally the difference of two marginal percentiles.

## Geographic alignment and completeness

All four raw tables, four converted flux CSVs and two rate CSVs share the same full `(MJD, altitude, latitude, longitude)` key set **and order**. There are zero duplicates and zero missing cells relative to one another. All values are finite and nonnegative; all integral spectra are nonincreasing with threshold.

The domain has 70 distinct latitudes (−34.75 to −0.25°) and 160 distinct longitudes (−89.75 to −10.25°), each axis spaced 0.5°. The 7,940 occupied centers are not the full 11,200-cell bounding rectangle. **The remaining 3,260 rectangle combinations cannot be declared missing errors or intentionally excluded cells without the original mask/ephemeris.** Absolute completeness of the intended SAA domain remains unestablished. Equal files cannot prove that the same omitted cells are present nowhere.

The validator rejects duplicate keys, empty tables, nonfinite coordinates and unequal key sets; its alignment helper joins by complete key and can handle reordered rows. An explicitly supplied expected-key set detects a shared omission. The evidence audit additionally enforces the observed 7,940-cell revision and reports the cell-key SHA-256. Future regenerated runs need an independently controlled domain/ephemeris manifest, not this count alone.

## Confirmed source weaknesses and limits

| Finding | Source | Consequence / protection |
|---|---|---|
| Out-of-range thresholds silently clamped | `count_rate_per_cell.py:40–43` | No valid >100 MeV retrieval from this grid; independent implementation raises an error. |
| Duplicate cells accepted when both files duplicate the same rows | `count_rate_per_cell.py:68–70` | Equal row arrays do not prove uniqueness; explicit duplicate-key rejection added in independent checker. |
| Shared missing cells not detected | Same lines | Require expected domain; observed agreement alone cannot establish absolute completeness. |
| No explicit units, finite/nonnegative, monotonicity or unique-energy checks | `energy_columns:25–33`, `flux_above:36–53` | Invalid/signed/NaN input can propagate or be misinterpreted; audit checks raw metadata and spectra. |
| Approximate equality can snap nearby energy to a column | `count_rate_per_cell.py:45` | Independent checker uses exact endpoint identity and tests nearby thresholds. No effect demonstrated on supplied default thresholds. |
| Mean-generating config and ephemeris/database absent | Configs line 2,7,9 | CSV arithmetic reproducible; upstream IRENE run not independently regenerated. |
| ODS summary uses endpoints rather than range | `Sheet1!N7942` | Cached 199.929387 is not the column maximum 5144.51739; data rows themselves match. |

No defect above was “fixed” in the raw source scripts. Their preservation supports reproducible historical evidence.

## Tests and repeatable commands

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_count_rate_evidence.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_count_rate_evidence.py' -v
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

**19 new count-rate tests passed.** Full local discovery: **28 passed, 3 optional legacy payload tests skipped** (31 discovered, approximately 2.1 seconds). Coverage includes power-law interpolation, exact and near thresholds, zero/fallback/extreme flux, invalid energies and flux, integral monotonicity, 4π and unit conversions, duplicate/missing/extra cells, reorder alignment, epoch/altitude mismatch, raw units and complete evidence reproduction. Skipped tests require the separate Orekit legacy environment and are unrelated to this ingestion. No annual orbit run, Monte Carlo transport, hardware validation or environment regeneration was performed.
