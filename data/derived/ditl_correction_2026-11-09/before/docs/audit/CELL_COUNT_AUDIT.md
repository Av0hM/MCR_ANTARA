# Scientific grid, cell counting and coverage audit

Audit date: 2026-11-02. Audit only; simulation code, input configurations, scientific results and MCR source were not changed.

**Source notation:** `R:` means this MCR repository; `S:` means `/home/sammo/Desktop/Projects/ANTARA_CODES-main/`; `P:` means the `PDR Sims/` member tree in `/home/sammo/Downloads/PDR Sims-20261021T072428Z-1-001.zip`; `D:` means the `MCR DATA/` member tree in `/home/sammo/Downloads/MCR DATA-20261021T072514Z-1-001.zip`; `G:` means `PROJECT_ANTARA/saa_sim/` inside `P:AbhishekSims/PROJECT_ANTARA.zip`. Archive members were read from disposable copies under `/tmp/antara-audit/`. Line numbers refer to the inspected working files/archive members, not an assumed common version. See [repository map](REPOSITORY_MAP.md) for scope and source identities.

**Evidence terms:** Confirmed = demonstrated by inspected code, file comparison or arithmetic. Suspected = plausible consequence needing a discriminating test. Unestablished = the producing inputs/revision or required validation were not recovered. A passing regression is not physical validation.


## Coordinate systems and domain construction

The report specifies geographic latitude/longitude cells, but its endpoints and totals are inconsistent. `R:sections/01_mission_context.tex:163` says “270°W to 10°E” and “130°×60°”. In the supplied code `P:grid_common.py:15–24`, longitude is continuous **−270° to +10°**, a **280°** span, latitude −50° to +10°. At .5° this allocates **560×120=67,200** cells, not 31,200. Longitude wraps to [−180,180) for IRENE and maps back with modulo arithmetic (`grid_common.py:44–65`). A literal 270°W is equivalent to 90°E; changing it to 270°E would produce another span, not automatically the claimed 130°. The intended endpoints must be explicitly decided, not guessed.

The common SAA polygon has vertices (lon,lat): (−90,−5), (−80,−20), (−60,−35), (−40,−35), (−20,−25), (−10,−15), (−20,−5), (−50,0), (−70,0), closed back to start. Cells with **positive-area overlap** are retained (`grid_common.py:78–87`). Shapely operations occur in angular degree space, not equal-area projection. Touch-only cells are excluded; the entire retained cell gets eligible dwell even if the spacecraft lies outside the polygon part of that boundary cell. This differs from point-in-polygon Science gating.

Independent evaluation of the overlap mask, with no orbit propagation, reproduced:

| Resolution | Full 280°×60° allocation | Polygon-overlap cells | MCR nominal 130°×60° total |
|---|---:|---:|---:|
| 5° | 672 | 92 | 312 |
| 1° | 16,800 | 2,020 | 7,800 |
| .5° | 67,200 | 7,940 | 31,200 |

The extra longitudes are mostly outside this polygon, so the 280° allocation error does **not by itself prove** the 7940 retained polygon cells are wrong. The confirmed error is inconsistent definitions/denominators. No grid should be repaired by silently swapping a longitude sign.

## Four different counters

| Counter | Implementation | Meaning and limits |
|---|---|---|
| PDR `pass_count` | P:count_cell_passes.py:313–327 | Increments on transition into a retained cell; contiguous samples count once. Re-entry counts again, even within one orbit. No unique SAA/orbit ID retained. |
| PDR `time_seconds` | same, line 324 | Adds fixed STEP_SECONDS for each eligible sample. Geometric dwell, no payload enable/pointing/dead time/storage/downlink gate. |
| Integrated `_cell_pass_counts` | S:Science:1030–1035,1115–1119 | **Generation-step counter**, despite name. 10° geographic bins prefixed by flux region; neither PDR .5° grid nor required 5°/1°/.5° tier maps. |
| RAAN `SAA_count` / `GS_count` | S:MCR:869–873 | Number of positive 300-second samples between ascending-equator crossings; classification counts records pooled over both runs. Not detector passes or elevation-based contacts. |

Summing cell visits is not a count of independent SAA passages. A single pass can cross many cells. Coarsening a grid requires unique passage-ID unions, not summing child-cell pass counts. **Suspected:** tier aggregation may violate this; generating code/IDs are absent, so no claim of a confirmed overcount in tier tables is made.

## Propagation, sampling and restart

PDR source defaults: 3 days, 1 s sampling, 2026-01-01 UTC, 600 km, 3 kg, RAAN 15°, e=.001, SSO inclination derived from a first-order J2 formula; DP853/equinoctial, 10×10 gravity, NRLMSISE00/DTM2000 fallback, .01 m² isotropic drag/SRP. It is not identical to Science's 97.6°/2000 epoch or the latest MCR campaign's 2026/3-kg large-area model. The comment promising essentially zero LTAN drift from the J2 formula is not a demonstrated long-term result (`count_cell_passes.py:132–146`).

The loop uses `[0,n_steps)` and fixed point-sample dwell. Grid boundaries can be missed or overallocated by one sampling interval; a corner crossing can be arbitrarily short despite the printed cell-width heuristic. Required tests: synthetic straight tracks with analytically known intersections; ±longitude wrapping; exact lower/upper boundaries; corner/boundary-only overlaps; convergence at .25/.5/1/2 s; no annual propagation needed.

**Confirmed restart bug:** `count_cell_passes.py:299–308` accepts a checkpoint solely when `n_steps` agrees. Different epoch, RAAN, spacecraft, timestep/duration pairs, polygon, or grid definitions can have identical n_steps. Stored old counts/dwell can then be combined with a different orbit. Save/compare resolved config, source/model/data identity and array shape; reject incompatible restart; compare uninterrupted and split short tracks. No supplied output is asserted to have suffered such a restart without evidence.

The 18-Month `cell_pass_counts.csv` has 7940 rows and sum of per-cell visits **214,039**. `tier_slice_EMSC_546d_SELFCHECK.csv` has the same pass-count sum; this does not prove 214,039 independent SAA passes or completion of 546 days. The source supplied still says 3 days and no archived trajectory manifest establishes the long run's settings or slicing implementation.

## Recomputed disposition table

| Output under P:Simulation Outputs/18-Month Simulation/ | Evaluated | Primary | Supplementary | Blank disposition |
|---|---:|---:|---:|---:|
| tier_disposition_MMSC_4mo_min.csv | 92 | 92 | 0 | 0 |
| tier_disposition_MMSC_6mo_nominal.csv | 92 | 92 | 0 | 0 |
| tier_disposition_MSC_12mo_min.csv | 2020 | 1915 | 105 | 0 |
| tier_disposition_MSC_14mo_nominal.csv | 2020 | 1931 | 89 | 0 |
| per_cell_disposition_emsc.csv | 7940 | 4213 | 3719 | 8 |

These reproduce `R:appendices/L_new_evidence.tex:11–15`. The `(1)` EMSC CSV is byte-identical, not a second independent experiment. The two MMSC files are separate duration cases and are not presumed identical because counts agree. Primary fractions on their modeled domains are 100%, 94.80%, 95.59%, and 53.06% respectively; they are not interchangeable with MCR eligible-region fractions.

As a diagnostic only, 92/312=29.49%, 1915/7800=24.55%, 1931/7800=24.76%, 4213/31200=13.50%. **Do not report these as final mission failure rates either:** MSC explicitly excludes undetectable cells, EMSC uses an AP9 >1%-of-peak eligible set, and the longitude/denominator itself is unresolved.

## Tier validity against actual requirements

| Tier | Requirement from active MCR | What recovered products establish / do not establish |
|---|---|---|
| MMSC | ≥70% bounding-grid coverage, ≥3 independent SAA passes/cell, ≥2 channels, ≤50% flux uncertainty, ≥90% core coverage (sections/01:178–190) | 92 polygon cells labeled Primary; no proof of global denominator, core mask, independent visits, two calibrated channels or received data |
| MSC | ≥90% detectable-flux eligible cells, ≥5 independent passes/cell, ≤25% in two lowest channels, registered maps and monthly comparisons (01:255–265) | 1915/1931 Primary labels. CSV exports `best_sigma_F_F_pct`, total counts and zero-channel count; these are insufficient to prove the two-lowest-channel condition. Generator absent. |
| EMSC | ≥95% of AP9 >1%-peak cells, ≥5 passes, ≤10% one channel/≤15% remaining, ≥3 channels (01:327–337) | CSV has best/worst finite errors, zero-channel count, coverage/pass/error booleans and disposition. Source for these booleans and defined peak/spectrum/eligibility missing; missing/zero channels must not be discarded as “finite only.” Primary rows found have no zero-channel flags, but that alone is not calibration proof. |

Poisson planning approximations 1/√N give 4 counts for 50%, 16 for 25%, ≥45 for 15%, 100 for 10%. They are per cell **per effective energy channel**, not per pass or all bins pooled; systematic calibration/background uncertainties can dominate. The response matrix determines independent channels, not an arbitrary 64-bin output format.

## Rate-map ingestion defects and gaps

P:step2_process_irene_outputs.py:72–79 checks row width only for first five records. Lines 117–125 overwrite a cell on duplicate input, increment `matched` for each row and calculate missing=n_flagged−matched. Duplicate rows can hide an actually missing cell. No checks enforce finite/nonnegative flux, integral/omnidirectional semantics, expected epoch/altitude, or mean versus percentile identity. Test duplicate/missing pairs, late malformed rows, wrong units/energy direction, NaN and negative flux. Monotonic integral-flux violations are clipped to zero at line 147 instead of being reported with diagnostic provenance.

The nominal generator writes `radiation_outputs.txt`; processor expects `radiation_outputs_mean_flux.txt`; percentile config writes `outputs_rate.txt` while provided file is `outputs_rate_pctile_flux_99.txt`. Manual renames/edits are part of the unrecovered provenance. Mean raw file absent; do not substitute the percentile file.

## Acceptance pipeline to implement after review

Define common longitude/geodetic/grid/eligible-region contract → retain immutable passage IDs and interval intersections → compute science-enabled exposure rather than geometric dwell alone → fold validated directional mixed-field response and background → reconstruct effective per-channel products → propagate statistical and systematic uncertainty → apply independent-pass and received-telemetry requirements → generate all tier tables, coverage denominators and figures from the same checked dataset. Validate synthetic cases before short orbital convergence runs and only then consider long campaigns.
