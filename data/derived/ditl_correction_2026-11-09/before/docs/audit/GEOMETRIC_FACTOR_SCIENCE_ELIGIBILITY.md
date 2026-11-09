# Geometric-factor study and science eligibility

## Populations and statistics

The model first restricts to the 7,940 positive-overlap polygon cells, then selects a **different population for each energy band** using band rate ≥1% of that band's peak. All supplied cells have positive dwell. Zero exposure must remain an infinite requirement, not be silently removed. Selected populations are:

| Incident band MeV | Selected cells | G95 10% | G95 15% | G95 25% | G95 50% | At G=0.3: 10% coverage |
|---|---:|---:|---:|---:|---:|---:|
| 5.4–10 | 7596 | 0.364535 | 0.162016 | 0.058326 | 0.014581 | 93.549% |
| 10–20 | 7177 | 0.413303 | 0.183690 | 0.066129 | 0.016532 | 92.253% |
| 20–40 | 7052 | 0.500042 | 0.222241 | 0.080007 | 0.020002 | 89.663% |
| 40–100 | 7144 | 0.360776 | 0.160345 | 0.057724 | 0.014431 | 93.253% |

At G=0.3 the 15% selected-cell coverages are 99.039%,98.760%,97.604%,99.580%; the 25% and 50% coverages are 100% in each separately selected band. All use supplied dwell and ε=1. No number is a coverage fraction of 7,940 cells unless its denominator is explicitly changed and recomputed. A per-bin 95th percentile does not imply 95% in the intersection of all required channels; a worst-case union bound alone can be much lower.

## Comparison with committed requirements

| Requirement | What this study addresses | What remains unverified |
|---|---|---|
| MMSC 70% region / 90% core, required channels/precision | Broad-band expected counts can be calculated | Region/core eligibility, proper coarse-grid aggregation, calibrated channels, independent passes, temporal/delivery conditions |
| MSC 90% detectable cells, 25% in two lowest channels, ≥5 independent passes and monthly maps | Per-band Poisson proxy | Joint channel coverage, detectable-cell definition, monthly exposure, independence and full uncertainty |
| EMSC EM-M-02 ≥95% of cells above 1% mission peak flux | Numerically resembles the study's 95%/1% choices | Mission peak versus per-bin peak, strict > versus ≥, AP9 identity, fixed eligible population |
| EMSC EM-M-01/03 0.5° map, ≤10% one channel and ≤15% other operational channels | Per-band target counts | Joint per-cell logic, operational channel response, total flux uncertainty |
| EMSC EM-M-04/05/06 ≥5 independent passes, ≥3 operational channels, full/sub-epoch maps | Table includes 15–40 cell-entry counts | Independent observation definition, timestamps, ≥3 calibrated channels, two 9–10 month submaps and verified full observation window |

The actual requirement text in `sections/01_mission_context.tex` remains controlling; this table is a comparison, not a replacement. No scientific requirement or eligible-region definition was changed.

## Acceptance contract proposed for subsequent validation

Freeze a scientifically justified eligible-cell mask and energy-channel definition before tier evaluation. Retain chronological pass IDs, cell entry/exit, science-enabled dwell and livetime; repeated samples in a continuous visit are not independent observations. Preserve missing channels as failures/unknowns, not excluded favorable populations. Evaluate per-cell joint channel precision over required epochs, then coverage over the approved denominator. Coarsen counts and exposures with explicit area/flux weighting rather than simply summing fine-cell pass counters. Require stored/downlinked record evidence. Duration extrapolation requires verified orbit sampling and exposure scaling; not performed here.

The 64 onboard bins are a reporting choice, not 64 independent calibrated measurements. The study's 63 surviving intervals follow a 5.4 MeV cutoff on a 65-point spectrum. Broad-band aggregation reduces required counts per reporting channel by collecting more protons into a wider energy interval, but may sacrifice required spectral information. No bin merging or science-resolution relaxation is recommended without energy-response and requirement review.

For background-subtracted signal S=Non−αNoff, independent Poisson counting gives variance Non+α²Noff before uncertainty in α. Background-model, efficiency, exposure/livetime, acceptance, energy migration and calibration covariance must be added or propagated jointly. Low/zero signal needs appropriate likelihood/confidence treatment; four expected counts and 50% Gaussian-style error are not a coverage guarantee. Large incident electron proxies make background and trigger livetime important, but no rejection factor or dead time is invented.

**Disposition:** reproduced conditional count-yield metrics may be reported. No MMSC, MSC or EMSC pass percentage, actual effective G, or maximum electronics trigger rate can now be defensibly certified.
