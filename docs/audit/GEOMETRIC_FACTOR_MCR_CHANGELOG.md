# Geometric-factor evidence and MCR integration changelog

Date: 2026-11-06. Starting MCR repository commit: `23170a89a9b47265bb2bb8dcd97a10ffe7eb9bfd`. Starting report: 62-page approved-FPDU PDF. No applicable `AGENTS.md` was found in this workspace or ancestor directories. Existing untracked simulator-accounting audit reports and supplied evidence were preserved; no branch/commit or external simulator modification was made.

## Stage disposition

1. **Inventory/provenance:** all 9 files inventoried and hashed (8 scientific artifacts, 1 excluded bytecode cache). Dwell table exactly matches archived `18-Month Simulation` member; actual duration/RAAN/runtime configuration unavailable. Candidate source defaults cannot establish actual inputs. New 65-threshold radiation provenance remains incomplete.
2. **Independent arithmetic:** all 4 coarse and 63 fine rows reproduced within floating-point tolerance. Strict cell, spectrum, units, NPY and polygon checks pass. Original script rerun independently in `/tmp`; original outputs untouched.
3. **Required-G interpretation:** documented unit-G incident rates, per-bin eligibility, Poisson-only targets, efficiency/exposure scaling and fine/coarse trade. No claim of achieved G or calibrated channels.
4. **Physical comparison:** converged two-square integrals, source midpoint comparison and synthetic six-box ray tests. All-through 72 mm G≈0.002488494 is conditional; no material/collimator/trigger topology selected. Actual transport/effective G unknown.
5. **Requirements:** MMSC/MSC/EMSC thresholds unchanged. Compared per-bin 1%/95% statistic to mission-peak eligibility and joint-channel requirements. No mission-success metric certified.
6. **Shielding:** retained source cutoff5.4; reproduced 5.5 sensitivity and optional unvalidated CSDA≈5.95. No shield transmission or energy-response curve fabricated.
7. **MCR:** integrated one detailed analysis with table/figure and short cross-references; distinguished historical spectrum title assumptions. Preserved Appendix A.1–A.6 grouping.
8. **Tests/build:** 107 tests passed, 3 optional legacy tests skipped, 16 subtests passed. XeLaTeX/latexmk exit0; final report66 pages. No annual or multi-year run.
9. **Traceability/open decisions:** source hashes, detailed limitations, exact output inventory and remaining PDR gates recorded. All original hashes rechecked unchanged.

## Exact modified files

| File | Change / reason |
|---|---|
| `appendices/B_payload_detail_visual.tex` | Added A.2.5 required-G analysis, equation3, table18, figure7, ideal geometry and cutoff limitations; closure subsection shifts to A.2.6 |
| `sections/04_simulations.tex` | Section4.5 summarizes conditional design requirement and links detailed analysis |
| `appendices/C_simulation_provenance.tex` | Table23 records distinct new study with unknown epoch/percentile/duration |
| `appendices/L_new_evidence.tex` | AppendixG.2 distinguishes new bundle; figure12 caption flags historical546-day/G0.314 assumptions as unverified runtime labels |
| `docs/audit/CLAIM_TRACEABILITY.md` | Added numerical source mapping and rejected/superseded interpretations |
| `docs/audit/REMAINING_OPEN_DECISIONS.md` | Added missing manifests, geometry/trigger/shielding/eligibility gates and bounded next experiment |

## Exact new deliverable files

- `docs/audit/GEOMETRIC_FACTOR_SOURCE_PROVENANCE.md`
- `docs/audit/GEOMETRIC_FACTOR_NUMERICAL_VALIDATION.md`
- `docs/audit/GEOMETRIC_FACTOR_PHYSICAL_INTERPRETATION.md`
- `docs/audit/GEOMETRIC_FACTOR_SCIENCE_ELIGIBILITY.md`
- `docs/audit/GEOMETRIC_FACTOR_MCR_CHANGELOG.md`
- `scripts/validate_geometric_factor.py`
- `scripts/plot_geometric_factor_audit.py`
- `tests/test_geometric_factor.py`
- `media/geometric_factor_requirements.png`
- `output/pdf/ANTARA_MCR_GEOMETRIC_FACTOR_2026-11-06.pdf`

New files under `data/derived/geometric_factor_2026-11-05_audit/`:

- `required_G_coarse_channels.csv`
- `required_G_fine_bins.csv`
- `cutoff_5p5_coarse.csv`
- `ideal_square_geometry.csv`
- `source_inventory.json`
- `upstream_archive_inventory.json`
- `validation_summary.json`
- `environment_and_diagnostics.json`
- `tests-all.log`
- `original-run.log`
- `latexmk-build.log`
- `xelatex-final.log`
- `build_summary.json`

The original evidence folder and the two pre-existing `SIMULATOR_ACCOUNTING_*.md` reports appear untracked in Git but were not created/modified by this integration. Historical PDFs, payload configurations, raw datasets and external simulator remain unchanged. No mission threshold, RAAN/EPS/ADCS/thermal/lifetime/CONOPS model changed.

## Verification and PDF review

Commands for arithmetic, source-script rerun, tests and plot are in `GEOMETRIC_FACTOR_NUMERICAL_VALIDATION.md`; interpreter/package versions are in `environment_and_diagnostics.json`. Test log records 107 passed,3 skipped,16 subtests. Three skips are optional external legacy source tests; no production integration is implied. New tests cover36 cases, including strict input checks, count conservation, percentile behavior, zero-exposure retention, quadrature convergence and on/off-axis ray paths.

Build command (isolated build files, same requested XeLaTeX options):

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=/tmp/antara-gfactor-audit/latex main.tex
```

Successful 66-page output copied to the new PDF path; old62-page report retained. Final log: 0 overfull boxes, no undefined references, no multiply-defined labels. Existing-style Latin Modern math bold substitutions and120 underfull-box diagnostics remain; these are not reported as a warning-free build. Inspected rendered PDF pages21,31–33,37,62 (printed pages13,23–25,29,54), including new table/plot, evidence table and revised historical caption. Plot legend was moved outside the axes to avoid obscuring data. No clipped new text/table/figure or broken cross-reference found. Appendix group structure remains A.1–A.6. `build_summary.json` records PDF SHA-256 and build checks.

## Next verification gates

Retrieve complete environment and exposure manifests first; do not scale dwell from a directory label. Then close material/gaps/optical and trigger topology choices needed for a bounded geometry-matched proton/electron transport matrix. Compare aluminium ranges with PSTAR before interpreting the low-energy threshold; qualify effective G, livetime and reconstruction with transport/bench evidence. Finally evaluate a fixed scientific eligibility/independence contract using verified science exposure and delivery records. Current results establish reproducible conditional counting requirements only.
