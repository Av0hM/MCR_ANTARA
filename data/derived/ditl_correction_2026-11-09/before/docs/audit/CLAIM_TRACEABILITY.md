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

## Geometric-factor evidence integration (2026-11-06)

| Claim | Actual source / independent check | Qualification |
|---|---|---|
| 7,940 matching 0.5° overlap cells | New `cell_proton_rates.csv`, `cell_pass_counts.csv`; strict key sets and polygon intersection in `scripts/validate_geometric_factor.py` | Geometric domain, not mission science denominator |
| 98–294 s cell dwell, pooled 1,453,556 s | Supplied dwell CSV; byte-identical archived `18-Month Simulation` member | Actual duration, scaling, RAAN and runtime epoch unverified |
| Integral rate is flux/(4π), G=1 | All 65 flux/rate column pairs; max absolute difference 5.69e-14 | Isotropic unit-G proxy, no qualified detector acceptance |
| Four coarse G95(10%) values 0.364535/0.413303/0.500042/0.360776 | Independently reproduced `data/derived/geometric_factor_2026-11-05_audit/required_G_coarse_channels.csv` | ε=1, cutoff5.4, supplied dwell, per-band1%-peak eligibility |
| Fine G95(10%) 3.9284–10.3301 | Reproduced `required_G_fine_bins.csv` | 65 input thresholds,64 original intervals,63 after cutoff; not calibrated channels |
| Two 6 mm square planes 72 mm apart: G=0.002488494 | Independent overlap quadrature, `ideal_square_geometry.csv`; convergence and ray tests | Ideal all-through straight tracks; not actual effective G |
| 5.5 MeV cutoff first-band G95=0.380453683 | `cutoff_5p5_coarse.csv` | 4.3668% sensitivity; altered bin selection included, not validated shielding |
| Optional source Al cutoff≈5.952391 MeV | Supplied `energy_from_range(0.025*2.699,'Al')` | Simplified unvalidated CSDA, not adopted flight threshold |
| Updated MCR equation/table/figure | Appendix A.2.5, `tab:required-g`, `fig:required-g-binning`; five GEOMETRIC_FACTOR audit reports | Conditional arithmetic only; no tier pass percentage |

Superseded interpretations: 63 intervals equal 64 calibrated channels; directory label proves an 18-month runtime; 95th percentile proves EMSC; G=0.3 is achieved by the payload; optional EJ-200 is selected; a 5.4 MeV hard cutoff validates 250 µm Al transmission. These interpretations are explicitly rejected, without altering original evidence or committed requirements. The verified 2026 date of the older AP9/AE9 archive does not establish the epoch of this new 65-threshold table.

## Integrated evidence ingestion — 2026-11-09

| Claim | Source and verification | Boundary |
|---|---|---|
| Both24h-named exports span3600s with terminal snapshots | `evidence/science_ditl/raw/{leop_24h,no_leop_24h}_ANTARA_Science_telemetry.csv`; strict endpoint/interval checks | Complete1h outputs, not24h |
| LEOP2460s detumble; recorded minimum15.209249672Wh | Telemetry duration weights and detumble event; `evidence/science-ditl/validation/leop_24h_summary.json` | One event; mode boundaries disagree2s with event log |
| No-LEOP minimum18.003630966Wh, final19.570485039Wh | Corresponding telemetry/summary | First state is post-step;25Wh SOC reference declared |
| No SAA/acquisition/contact/data during either hour | Boolean gates, incremental data and blank event exports | No daily science-duty or capacity inference |
| Annual telemetry covers4,320,020s, no terminal |1,861,462 telemetry rows, streamed interval sum | Incomplete; event exports inconsistent even after horizon filtering |
| Annual events origin2000-03-01 UTC | Absolute event timestamp minus elapsed time | Does not establish unknown one-hour/thermal epochs or compatible annual telemetry |
| Internal thermal−14.060918…21.159372°C | All43,201 thermal rows; K/C and summary time/extrema verification | Single-history model prediction, no hardware limits |
| Summary hot/cold columns are same-history extrema | `evidence/thermal/validation/node_statistics.csv` matches all seven source rows | ±10°C arithmetic allowances are not compliance margins |
| Detumble16,133/50,000 reported success; median951.5s among successful rows | `evidence/detumble/raw/detumble_mc_summary.csv`; strict norms/censoring checks | Historical inputs incompatible with current source; independence/timeout unknown |
|136 passed,3 skipped,16 subtests | `evidence/science-ditl/validation/tests.log` | Accounting tests, not physical qualification or production simulator integration |

Earlier 24-hour six-pass/two-contact/62.7% examples remain historical and distinct. No missing23hours, annual endpoint, thermal bounding case, convergence history or qualified FPDU measurement was synthesized. New MCR claims are in Sections3.4/3.7/4/5 and AppendicesA.1/A.3/A.4/A.5/F; the geometric-factor results and approved mission requirements are preserved.

**Final adoption decision:** one-hour arithmetic above is preserved for audit only; the user directed its exclusion from the MCR comparison. The final report adopts only annual-labelled telemetry/event evidence for operations, with their incompatibility explicit, alongside independent thermal and historical detumble evidence. The annual mode/exposure figure derives from `leop_1yr_summary.json`; no full-year completion is asserted.


## Science Record v3 and ideal 19.2 kbps budget — 2026-11-09

| Current claim | Exact source / calculation | Boundary |
|---|---|---|
| 292-byte reference record; uint16 alternative164 | `config/science/science_record_v3.json`; struct size/CRC tests | Excludes radio framing and linked metadata; not flight qualification |
| No minimum duration; retain zero counts; prefer3/2/1 | User's acquisition-time clarification; `SCIENCE_RECORD_V3.md` | Timing boundaries remain hardware-dependent; precision/tier success separate |
| 214039 visits,1453556s;62499388/124998776/187498164bytes | Original `cell_pass_counts.csv`; `grid_sensitivity.json` | Horizon unknown; geometric sensitivity, no daily/annual scaling |
| 820contacts244016s; minimum514s/day;gap48458s | Original annual GS CSV, exact AOS/LOS and daily integration; `historical_contacts.csv` | 2000-03-01 epoch; runtime mask/RAAN unknown |
| Visibility585638400bytes; Relay428836800bytes | 19200/8 ×244016s and178682s respectively; `gs_summary.json` | Full-rate modeled opportunity; no arbitrary derating; not delivered data |
| 57/174/231 preferred record slots | `tier_generation.csv`; sampled partial telemetry gate342s | Ideal timing partition; current FPDU counts not generated |
| 256KiB holds897 records;128MiB459649 | Integer division by292; `memory.json` | Science-only allocation before metadata, not total hardware memory |
| Maximum bounded EMSC queue67452bytes | `EMSC_3_releases.csv`, `EMSC_3_queue.csv`, `bounded_backlog.json` | Startup-concentrated legacy gate; not sustained mission storage closure |

Superseded active claims: 15–18kbps planning baseline; unencoded/unknown logical record byte size; arbitrary throughput derating; assumed300–400kB/day as current production. Historical originals remain intact and marked. Existing independent payload/orbit/thermal evidence is unchanged. Full protocol/link loss and net science throughput qualification is explicitly deferred to PDR.


## Section 3 feasibility flowdown — 2026-11-09

The centralized `config/requirements/section3_feasibility_v1.json` and `SUBSYSTEM_REQUIREMENT_TRACEABILITY.md` now trace51child obligations to unchanged Section1 mission IDs, approved interfaces and bounded evidence. All9existing Section3 headings retain their original prose and gain a requirements table/assessment. Status totals:4SUPPORTED(scope-limited),15CONDITIONAL,28OPEN,1NOT MET(evidence completeness),3NOT EVALUATED. No supported status implies whole-subsystem or hardware qualification.

The numerical parent criteria remain byte-for-byte unchanged. The MSC comparison table's≥4channels versus detailed all-operational wording is an explicit OPEN issue, not silently resolved. Concept blockers and PDR verification are separated in `MCR_FEASIBILITY_GAPS.md`. Generator and regression checks protect exact texts, IDs, sources and unchanged prior mission/configuration evidence.
