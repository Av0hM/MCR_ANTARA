# Numerical claim-to-source traceability and supersession

The detailed historical artifact graph remains in `DATA_PROVENANCE.md`. The following controls newly accepted or corrected MCR claims; labels apply only to the stated scope.

| Claim / location | Actual source or calculation | Status and limits |
|---|---|---|
| 2029-01-01, 3U/3 kg, 600 km, 97.6°, e~.001, 25 Wh, ~five years | Latest authoritative user instruction; `config/mission/antara_2029.json` | CONFIRMED DESIGN INPUT; not an output timestamp or lifetime validation |
| Five 14×6×6 mm XYZ main blocks, front 2×6×6 mm, 11 SiPMs | User instruction; current immutable payload config | CONFIRMED DESIGN INPUT; no recovered controlled CAD |
| 70/72 mm, 2592 mm³=2.592 cm³ | Exact dimension sums/products; GeometryTests | VALIDATED RESULT for arithmetic only |
| Teflon .11 mm/±Z face; coated 6.22 mm | Confirmed per-face decision; 6+2×.11 | Material dimension, excludes packaging |
| 250 µm=.25 mm entrance Al | User input and exact /1000 conversion | Not modeled by supplied count-rate script |
| 20 ns shaping, 200/250/300 ns coincidence references, post-shaping 20 ns | Latest user instruction and coincidence-window clarification | Planning inputs; no dead-time or processor-latency inference |
| 64 bins, 5–100 MeV | User provisional format and committed science requirement; config log64 edges | Reporting choice, not calibrated energy resolution |
| Mean p358.920/e67779.655 Hz; p99 p975.659/e503419.743 Hz | Four raw IRENE flux outputs → independent validator → derived `validation_summary.json` | Reproduced MODEL PREDICTIONS; G=1 cm² sr, isotropy, unit efficiency, p>5.5/e>.35 MeV |
| Same-cell summed maxima 68055.635/504245.064 Hz | Same aligned per-cell spectra and independent conversion | Not sum of independent maxima, not joint percentile or electronics upper bound |
| Source epoch2026-01-01, altitude600km | Raw header and all records MJD61041 | Verified source identity; approved preliminary 2029 planning reference |
| 92/2020/7940 polygon cells | Supplied PDR polygon; independent clipping and Shapely agreement | VALIDATED RESULT for positive-area mask; scientific denominator open |
| MMSC/MSC/EMSC disposition counts | Original tier CSVs enumerated in `DATA_PROVENANCE.md` and Appendix L | File contents reproduced; generating tier logic/response not recovered, no success acceptance |
| 62.7% | Historical DITL pass statistics, `ISSUES.md:A10`, original source detection-conditional sample denominator | Relabeled; not duration-weighted SAA science duty |
| Minimum slew .442496° | Historical 18-row `ANTARA_Science_slew_events.csv`, independent original audit | Replaces unexplained5.4° filter/minimum claim |
| RAAN 54.4–74.7% column | `raan_master_trade_matrix(1).csv`; inspected MCR source averages run minima | Mean run-minimum, not worst-case sample; no numeric output altered |
| >8000 historical SAA-only annual records | Two-run grouping in recovered old classification table, prior audit exact counts | Valid pooled tally; not one spacecraft's one-year revolution count |
| New RAAN685798 classification rows | Latest `orbit_classification(1).csv`, seven RAAN/two-run grouping in original audit | Raw bookkeeping, not detector-on SAA passages |
| 8–10-year modeled cutoff | Supplied drag CSV, including censored334.93km endpoint; Appendix M | No reentry or five-year operational qualification inferred |
| 1536.3g BOM entries | Supplied workbook, Appendix L original transcription | Partial candidate subtotal, not completed spacecraft mass |

## Superseded statements

| Superseded statement | Current disposition |
|---|---|
| Single-block Rev.2.1 or historical five-layer response is current | New six-scintillator geometry; neither old response transfers |
| Silicon entrance retained / mandatory rear veto | Silicon removed; rear optional/unselected |
| Block orientation/SiPM count/per-face coating unresolved | Longitudinal X, ±Y main SiPMs,11 total; ±Z .11mm per face confirmed |
| 20ns coincidence and guessed20ns dead time | 20ns shaping, 200ns nominal coincidence; dead time unknown |
| MCU feasibility follows directly from250ns | Whole architecture/timestamps/queues/throughput must qualify |
| Approximately400Hz is maximum event rate | Historical conditional estimate; per-cell maps control planning; actual trigger ceiling unknown |
| AP9/AE9 tables are 2029-generated or shielded | Verified2026 grid, no shield transport in conversion |
| 312/7800/31200 rectangular cells define approved SAA | 92/2020/7940 geometric polygon overlap; eligibility still open |
| 13000–108000 historical summed rates are counts proving precision | Claim withdrawn; missing time integration invalidates interpretation |
| RAAN min_soc column is worst observed SOC | Mean of run minima; patch adds separate worst minimum |
| >8000 pooled SAA-only records are physically impossible | Two-run pooling explains tally; classifier semantics still approximate |
| Completed or annual-named simulation proves mission success | Complete horizon, response, exposure, uncertainty and delivery evidence required |
| CMG selection / placeholder-only closure tables | Current RW+MTQ; concrete evidence/verification gates replace blanks |

Historical source files, raw outputs and immutable configuration snapshots remain preserved. Current narrative warnings prevent their reuse as approved performance.
