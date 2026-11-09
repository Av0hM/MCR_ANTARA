# Corrected DITL authority — 2026-11-09

This current correction supersedes all earlier Science/DITL-dependent statistics and evidence statuses below. Earlier entries are retained as historical audit history, not active numerical claims. Independent physics/design/RAAN/thermal/detumble findings are unaffected. Current sources: `CORRECTED_DITL_RUN_VALIDATION.md`, `DITL_CORRECTION_IMPACT_MATRIX.md`, `STORAGE_BACKLOG_VALIDATION.md`, and `evidence/science-ditl/run_registry.json`.

All three corrected timestamp spans are complete (86400/86400/31536000 s), epoch2000-03-01. Annual acquisition247258 s; minimum recorded battery15.097556 Wh; full ideal Relay428836800 bytes; preferred EMSC v3 slot volume46637364 bytes; nominal peak75336 bytes; seven-day outage peak1010028 bytes. Runtime config and transition/slew semantics remain unresolved. No2029 calibration or qualified science success follows.

Current requirement status totals: {'CONDITIONAL': 17, 'OPEN': 28, 'SUPPORTED': 3, 'NOT EVALUATED': 3}. ANT-OBC-FR-002 is CONDITIONAL (outage spill needed); ANT-GSO-FR-003 is CONDITIONAL (coverage corrected, logger/source closure open), replacing its earlier NOT MET truncation rationale. Full updated register: `SUBSYSTEM_REQUIREMENT_TRACEABILITY.md`.

---

## Prior audit history (DITL-dependent entries superseded)

# Data and result provenance

Audit date: 2026-11-02. Audit only; simulation code, input configurations, scientific results and MCR source were not changed.

**Source notation:** `R:` means this MCR repository; `S:` means `/home/sammo/Desktop/Projects/ANTARA_CODES-main/`; `P:` means the `PDR Sims/` member tree in `/home/sammo/Downloads/PDR Sims-20261021T072428Z-1-001.zip`; `D:` means the `MCR DATA/` member tree in `/home/sammo/Downloads/MCR DATA-20261021T072514Z-1-001.zip`; `G:` means `PROJECT_ANTARA/saa_sim/` inside `P:AbhishekSims/PROJECT_ANTARA.zip`. Archive members were read from disposable copies under `/tmp/antara-audit/`. Line numbers refer to the inspected working files/archive members, not an assumed common version. See [repository map](REPOSITORY_MAP.md) for scope and source identities.

**Evidence terms:** Confirmed = demonstrated by inspected code, file comparison or arithmetic. Suspected = plausible consequence needing a discriminating test. Unestablished = the producing inputs/revision or required validation were not recovered. A passing regression is not physical validation.


## Provenance levels

A byte-identical source copy establishes artifact identity. A code writer with the same filename establishes a candidate producer. Neither establishes the exact executed configuration, RNG realization, model database or successful validation. The strongest recovered chains and remaining gaps are below; all four CSVs and all nine figures in R are covered individually.

## Checked-in CSVs

All four `R:evidence/raan_2026-10-22/` files are byte-identical to `S:results/mcr/` counterparts. Their candidate writer is `S:src/simulations/power/ANTARA_MCR.py:351–488,875–1045`. Its current configuration is 2026, 3 kg, 97.6°, 3650-day cap, 300 s samples, two runs per RAAN. These files have no run manifest proving those settings were used; source has uncommitted edits and no archived seed. The October-21 `D` files with the same basenames are **different** one-year artifacts.

| CSV | Independent audit check | Provenance/interpretation |
|---|---|---|
| `raan_master_trade_matrix.csv` | 7 rows; every class total matches raw classification grouping | avg power 9.022353–11.174851 W; `min_soc` .5443067–.7466236 is averaged run minima, not global minimum; `lifetime_years` is mean termination time |
| `orbit_classification.csv` | 685,798 rows; no duplicate `(RAAN,run,orbit_number)` keys; 14 groups; all totals match | candidate writer groups ascending-equator crossings; SAA_count/GS_count are **positive 300-second samples**, not independent pass/contact counts; constant `orbit_period_min=97.0` is written, not measured |
| `drag_lifetime_analysis.csv` | 14 records, 2 per RAAN; range 8.226253–9.993165 years; 13 near 300 km, one 334.932479 km | final 30° case is censored above cutoff; latest code includes a finite horizon; no physical reentry output |
| `mission_statistics.csv` | all five means equal RAAN 180° master row; lifetime endpoints match its two drag rows | produced after RAAN loop, so it summarizes only final RAAN. CI=2.576×population SD/√2; not independently validated 99% inference |

SHA-256 identifiers:

```text
orbit_classification.csv 547fc2d146c32460da38048cad703667e3fd3c5562f15dc2a3e92df189a90820
drag_lifetime_analysis.csv 4adc8bedc92213cb3a7a5fbe9ef85578afd4e614203120bb74e1fc8904bda925
mission_statistics.csv a8ef9dc90fe393c54b064d9682f8d18b0d7b16c63c960df69a7e0701ab60a8be
raan_master_trade_matrix.csv 8989ea52b7a84833fc63c245720b557db13cd08eb5433490e5676e4dc19dd6e0
```

## Every checked-in figure

| R:media file | Recovered source identity | Producer/configuration status |
|---|---|---|
| `mmsc_4mo.png` | exact bytes of P:Simulation Outputs/18-Month Simulation/tier_slice_MMSC_4mo_min.png | **dwell/visit slice image**, not the distinct `tier_disposition_MMSC_4mo_min.png`; slice/disposition generators absent |
| `msc_12mo.png` | exact bytes of P:Simulation Outputs/18-Month Simulation/tier_slice_MSC_12mo_min.png | same distinction; not the disposition image; producing epoch/config/slicing method unestablished |
| `emsc.png` | exact bytes of both P:…/per_cell_disposition_emsc.png and `(1).png` | paired disposition CSV recovered; classifier source absent |
| `spectrum.png` | exact bytes of P:…/saa_proton_spectrum.png | 64-row paired CSV exists; generating spectrum/response algorithm absent; no live measurement claim justified |
| `saa_3day.png` | exact bytes of P:Simulation Outputs/3day_cell_pass_counts_heatmap.png | candidate P:count_cell_passes.py heatmap writer; current 3-day/2026 config; run identity unestablished; not included in active TeX |
| `ditl_overview.png` | no exact match in inspected P/D archive PNGs or S figures | raw historical DITL CSV matches numerical narrative, but exact image producing revision/plot command unestablished |
| `saa_magnetic_anomaly.png` | R:sections/01_mission_context.tex:40 says original-draft image, year 2000 | generator, magnetic model/coefficient set and license/source attribution unestablished |
| `orbit_type_timeline.png` | no exact match recovered | candidate CONOPS plotting workflow not established; unreferenced by active TeX |
| `representative_ground_tracks.png` | no exact match recovered | source/config unestablished; unreferenced by active TeX |

TikZ schematics in appendices A/B are authored report illustrations, not quantitative simulated outputs. `main.pdf` is a pre-existing 61-page build artifact. Poppler metadata reports xdvipdfmx (20260113), creation 2026-10-22 12:35:37 IST. Extracted text confirms the grid contradiction, disposition table and latest RAAN table are present; PDF physical page 55 (printed page 48) was rendered and visually inspected, confirming Figure 6 is a pass-count map. This was a targeted content check, not a full layout certification or proof of exact TeX/build-tool provenance. It was not overwritten/rebuilt.

## Major report numbers traced to data

| Claim and report location | Actual source/calculation | Audit disposition |
|---|---|---|
| 87.5% Sun, 7.3% Detection, 1.0% Relay; 18 slews (sections/04:5) | D:Day-In-Life and Subsystem performance/ANTARA_Science_telemetry.csv: 43,201 rows, 37,781 Sun / 3,134 Detection / 450 Relay; slew CSV has 18 rows | Rounded historical row fractions reproduce; 0–86400 s at 2 s. No interval/end-state columns, so do not apply new terminal-row semantics retroactively. |
| 15.15 Wh, 60.6% (sections/04:7) | min battery 15.1535251545 Wh /25×100=60.6141%; final 24.0626395381 Wh | Arithmetic supported for old run; not usable-capacity/hardware validation |
| 6 SAA, 5 proton records, 62.7% (sections/04:7; I:63–77) | SAA CSV 6 rows, 2696 s dwell; proton CSV 5 rows; unweighted mean science_fraction=.6269801931 | Ratio uses generating samples / Detection samples, not total SAA dwell; 491 science-enabled telemetry samples nominally 982 s, only ~36.42% of 2696 s. Boundary semantics prevent treating this as a precise corrected livetime. |
| 2460 s startup detumble (L:29) | D:…/ANTARA_Science_detumble_events.csv:2, start 120, end 2580 | One historical initial condition, not MC reliability |
| 368+414 s contacts, 11.73 Mbit (sections/04:10; L:29) | D:…/ANTARA_Science_gs_contacts.csv:2–3; 782×15000 bits | Gross geometric capacity arithmetic supported. Actual contact-file downlink is 0 and .002558663130942058 MiB; not 1.5 MB delivered. |
| 18.8 min slew total, .02 s mean/.31 s max timing error, .4° P95 (I:54–61) | D slew CSV sum=18.766667 min, mean signed actual−estimated=.0224237 s, max absolute=.3078108 s; D telemetry outside SLEWING gives .4° nearest-rank P95 for both error columns | Historical descriptive values reproduce, not independent controller accuracy. **Reported 5.4° minimum slew angle does not:** raw minimum .442496°, maximum 175.808369°. |
| 6.05 W mean generation (I:136) | arithmetic row mean D telemetry =6.04987206896 W | Historical constant-sampling descriptive mean; not current EPS result |
| .060 MB science (I:155) | D telemetry science_data_mb sums .0599365234375; old writer divides bytes by 1024² | Unit is MiB; 62,848 bytes. Different packet model from current 272-byte histogram flush. |
| 13,000–108,000 lowest-channel counts (I:197) | D proton CSV `total_counts_per_channel`; D:ANTARA_Science_Sim.py:1819–1841 sums count rates | **Confirmed historical counting bug**: missing dt; upstream diagnostic differential-rate units also lack energy width. Cannot use for Poisson tier acceptance. |
| Annual 11.22 W, .987 mean SOC, .834 min SOC, 787 cycles (I:209–216) | D:Detailed-ConOps and Mission Design/mission_statistics.csv, RAAN 180° only | Standalone 8 W constant-load annual power study, mislabeled integrated simulation; not one-year Science evidence |
| Latest 9.02–11.17 W; 54.4–74.7% (sections/04:13) | R master matrix; transcription in M:9–15 | Supports study aggregate only. Min SOC is average of minima. |
| 8.2–10 years and 335 km endpoint (sections/04:15, sections/05:15) | R drag CSV; M:25–33 | Supported as termination times, not reentry/lifetime guarantee |
| 92/2020/7940 domains; 92/1915/1931/4213 Primary Map (L:11–15) | P tier-disposition CSVs | Exact counts independently reproduced; geometry reproduces polygon-overlap domains; tier generator and per-channel validity unestablished |
| 312/7800/31200 target cells (sections/01:164,241,314) | 130°×60° divided by 5°²/1°²/.5°² | Arithmetic correct for a 130° box, but reported longitude endpoints do not specify such a box |
| G=.314, half-angle 18.4° (B:42) | π×1 cm²×sin²(arctan(10/30))=.314159 cm² sr | Idealized approximation; finite aperture/sensor geometry not calibrated |
| 256 bytes / minute ~34 bit/s (B:92; H:170–174) | 64×4=256; 256×8/60=34.1333 bit/s | Counter-only arithmetic. Continuous daily total 368,640 bytes before headers; no flight availability/overhead proof. |
| 1536.3 g entered BOM subtotal (L:31,55–72) | Sum listed numeric mass rows =1536.3 g | Transcription arithmetic agrees; original BOM workbook not verified in this audit, missing payload/deployment/multiplicity still prevents closure |
| 28.8 Wh vendor, 22.5 Wh historical, .17 W OBC, CMG/RW selection | R:L:75, H:48, sections/03 | Report/source-document claims, not simulator results. Manufacturer primary documents not independently qualified here. |

## External outputs and incomplete chains

- `S:results/science/<tag>_ANTARA_Science_{telemetry,saa_passes,gs_contacts,mode_transitions,slew_events,detumble_events,rejected_transitions,proton_passes}.csv` are written by Science logger/export routines; associated JSONL archives, summaries and checkpoints are part of a run. Tag names alone prove neither preset duration nor version. Numerous repair-tag outputs are historical and were not pooled.
- `S:results/science/leop_1yr_ANTARA_Science_telemetry.csv` endpoint inspection: last `time_sec=4320000`, `state_time_sec=4320020`, `interval_duration_sec=20`. This is about 50 days, not a 365-day completed run, and is not a terminal observation. No assertion is made that no other annual run exists.
- `S:results/mcr/{power_analysis,battery_analysis,conops_analysis}.csv` are candidate detailed campaign outputs from MCR:875–912; not embedded in R. No full-row validation of these large external files was performed. They must supply per-run extrema/energy balance before accepting master aggregates.
- `S:results/thermal/ANTARA_Thermal_{telemetry,worst_case_summary}.csv` and thermal PNGs map to ThermalSimulator export/plot methods at 1092–1269; current file names do not archive resolved hot/cold config. No thermal qualification result is asserted in R.
- CONOPS, average-power, battery-trade and detumble summaries/figures map to their named entrypoints in the repository map. Exact historical figure revisions/seeds remain unestablished unless explicitly hash-matched above.
- `D:GNSS/GNSS_performance.txt` is a separate reported summary; Java source helpers exist, but source TLE catalog, execution log/configuration and repeatable numerical chain were not recovered for report acceptance.
- P's mean rate CSV has the expected rate conversion but raw `radiation_outputs_mean_flux.txt` is missing. The percentile raw output exists and identifies AP9 integral omni ≥5 MeV. It is not a replacement for the missing mean result.
- P's `saa_proton_spectrum.csv` uses 64 energy bins with `region_count_rate_hz` and `expected_counts_mission`; the code that derived spectral allocation and exposure is absent. A curve named “spectrum” is not a detector response or energy reconstruction validation.
- Nested G contains 8 per-thread ROOT files and two transport PNGs, GDML, macros and C++ source. The deposition plot scripts identify candidate input branches. Execution macro, seeds, event count logs, physics-data versions and correspondence of binary build to sources are not archived as a manifest. ROOT contents were not replayed or treated as calibrated response.

## Acceptance record required

For each accepted result retain an immutable source/config/data manifest, exact processing command, output hashes, completion record, and interpretation of numerator/denominator/units. Preserve archived results as historical evidence; corrected outputs should have new run IDs. The next table enumerates the PDR CSV/PNG files individually and marks candidate writers rather than inventing missing code.

| P: archive member | Candidate producer / missing provenance |
|---|---|
| `AbhishekSims/Results/proton_range_verification.png` | AbhishekSims/plot_range.py; summed energy deposition, not calibrated reconstructed energy. |
| `AbhishekSims/Results/proton_range_vs_thickness.png` | AbhishekSims/plot_wrt_thickness.py; deepest-hit layer-boundary proxy. |
| `AbhishekSims/Results/saa_pileup_vs_shaping_time.png` | AbhishekSims/pile_up_prob.py; assumed 100 kHz, exact figure run unestablished. |
| `Simulation Outputs/18-Month Simulation/Copy of mean_cell_proton_rate_heatmap.png` | step2_process_irene_outputs.py candidate writer; mean raw input missing; percentile raw input available separately. |
| `Simulation Outputs/18-Month Simulation/Copy of mean_cell_proton_rates.csv` | step2_process_irene_outputs.py candidate writer; mean raw input missing; percentile raw input available separately. |
| `Simulation Outputs/18-Month Simulation/cell_pass_counts.csv` | count_cell_passes.py candidate writer; 18-month runtime settings not retained. |
| `Simulation Outputs/18-Month Simulation/cell_pass_counts_heatmap.png` | count_cell_passes.py candidate writer; 18-month runtime settings not retained. |
| `Simulation Outputs/18-Month Simulation/per_cell_disposition_emsc(1).csv` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/per_cell_disposition_emsc(1).png` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/per_cell_disposition_emsc.csv` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/per_cell_disposition_emsc.png` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/saa_proton_spectrum.csv` | Spectrum generator absent; paired CSV/PNG only. |
| `Simulation Outputs/18-Month Simulation/saa_proton_spectrum.png` | Spectrum generator absent; paired CSV/PNG only. |
| `Simulation Outputs/18-Month Simulation/tier_disposition_MMSC_4mo_min.csv` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_disposition_MMSC_4mo_min.png` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_disposition_MMSC_6mo_nominal.csv` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_disposition_MMSC_6mo_nominal.png` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_disposition_MSC_12mo_min.csv` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_disposition_MSC_12mo_min.png` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_disposition_MSC_14mo_nominal.csv` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_disposition_MSC_14mo_nominal.png` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_slice_EMSC_546d_SELFCHECK.csv` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_slice_EMSC_546d_SELFCHECK.png` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_slice_MMSC_4mo_min.csv` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_slice_MMSC_4mo_min.png` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_slice_MMSC_6mo_nominal.csv` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_slice_MMSC_6mo_nominal.png` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_slice_MSC_12mo_min.csv` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_slice_MSC_12mo_min.png` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_slice_MSC_14mo_nominal.csv` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/18-Month Simulation/tier_slice_MSC_14mo_nominal.png` | Tier/slice/classification generator absent; separate data/plot artifact, not regenerated. |
| `Simulation Outputs/3day_cell_pass_counts.csv` | count_cell_passes.py candidate writer; 18-month runtime settings not retained. |
| `Simulation Outputs/3day_cell_pass_counts_heatmap.png` | count_cell_passes.py candidate writer; 18-month runtime settings not retained. |
| `Simulation Outputs/3day_cell_time_spent_heatmap.png` | count_cell_passes.py candidate writer; 18-month runtime settings not retained. |
| `Simulation Outputs/cell_proton_rate_heatmap_worstcase.png` | step2_process_irene_outputs.py candidate writer; mean raw input missing; percentile raw input available separately. |
| `Simulation Outputs/cell_proton_rates_worstcase.csv` | step2_process_irene_outputs.py candidate writer; mean raw input missing; percentile raw input available separately. |
| `Simulation Outputs/mean_cell_proton_rate_heatmap.png` | step2_process_irene_outputs.py candidate writer; mean raw input missing; percentile raw input available separately. |
| `Simulation Outputs/mean_cell_proton_rates.csv` | step2_process_irene_outputs.py candidate writer; mean raw input missing; percentile raw input available separately. |
