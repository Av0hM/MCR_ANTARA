# Repository and workflow map

Audit date: 2026-11-02. Audit only; simulation code, input configurations, scientific results and MCR source were not changed.

**Source notation:** `R:` means this MCR repository; `S:` means `/home/sammo/Desktop/Projects/ANTARA_CODES-main/`; `P:` means the `PDR Sims/` member tree in `/home/sammo/Downloads/PDR Sims-20261021T072428Z-1-001.zip`; `D:` means the `MCR DATA/` member tree in `/home/sammo/Downloads/MCR DATA-20261021T072514Z-1-001.zip`; `G:` means `PROJECT_ANTARA/saa_sim/` inside `P:AbhishekSims/PROJECT_ANTARA.zip`. Archive members were read from disposable copies under `/tmp/antara-audit/`. Line numbers refer to the inspected working files/archive members, not an assumed common version. See [repository map](REPOSITORY_MAP.md) for scope and source identities.

**Evidence terms:** Confirmed = demonstrated by inspected code, file comparison or arithmetic. Suspected = plausible consequence needing a discriminating test. Unestablished = the producing inputs/revision or required validation were not recovered. A passing regression is not physical validation.


## Actual checkout and review scope

`R` is a report repository, not the mission simulation repository. Its starting commit is `33858662513fe9da4a2be3c7affb46054b0545b8`; it was clean at inspection. There is no `src/`, `tests/`, dependency manifest, simulation entrypoint, `source_archive/`, or committed raw DITL/grid dataset here. README's assertion that original TeX files are in `source_archive/` is false for this checkout (`README.md:5`). The protected `.agents/`, `.aws/`, `.codex/` directories are environment surfaces, not scientific source. Git internals and credentials were not treated as mission inputs.

```text
MCR_ANTARA/
  main.tex                  report entrypoint
  preamble.tex, .latexmkrc   typography, XeLaTeX toolchain
  main.pdf                  pre-existing compiled artifact
  sections/                 five active sections + five unreferenced additions
  appendices/               13 included source/support files A through M
  evidence/raan_2026-10-22/ four CSVs
  media/                    nine PNGs (six referenced by active TeX)
  README*.md, *_NOTES*.md, NEW_RAAN_EVIDENCE_README.md
  docs/audit/               this audit, added now
```

All report source files, inclusion relationships, four embedded CSVs, and nine image identities were inventoried. The simulation audit additionally follows the explicitly named source modules into `S`, and the report's supplied study archives into `P` and `D`. This is not a claim to have verified every unrelated sibling project, every historical binary/checkpoint, every plot pixel, or every row of the multi-gigabyte external telemetry collections. Large external results were inventoried and selectively streamed/endpoint-inspected; no pickle was loaded. The 61-page PDF was text-extracted and the science-grid evidence page visually inspected; it was not rebuilt or certified exhaustively to match current TeX. The conclusions about report claims refer to active LaTeX.

`S` HEAD is `51933bb902288de095f362546c73b006fe702882`, **with pre-existing modifications** to `src/simulations/helper/antara_models.py`, `pointing/ANTARA_pointing_budget.py`, and `power/ANTARA_MCR.py`. Untracked build/figure/package/scratch directories also pre-existed. Those edits were preserved. In particular, current shared RAAN is 30° rather than committed 15°, and the MCR script is 3650 days/3 kg/97.6° rather than committed 365 days/4 kg/97.4°. A commit ID alone does not identify these runs.

Archive SHA-256:

- PDR Sims ZIP: `1f13d956dcc7b820e903c67e479d9561c94911419371c7403eb2a00212934b0e`
- MCR DATA ZIP: `64baec249e52fba2656a52a87216cbf5806fc4f6b9aeffde3bae54e92ef7bc59`

## Report build graph

`main.tex` inputs `preamble`, sections 01–05, then A–M. A–F are combined under one technical-support appendix. G–J are historical source-detail sections with a supersession warning; K–M are additional integrated/study evidence. Filename letters therefore are not necessarily rendered appendix letters. None of `sections/*_additions.tex` is included. Their duplicate labels and placeholders do not create active-document duplicate-label defects unless later included.

XeLaTeX twice is the documented build. Dependencies include Noto Serif/Sans/Mono, Latin Modern Math, fontspec, unicode-math, TikZ, tabularx/longtable, graphicx and hyperref (`preamble.tex`, `.latexmkrc`). There is no automated CSV-to-LaTeX table generator: numeric evidence tables are transcribed. Three unreferenced images are `saa_3day.png`, `orbit_type_timeline.png`, `representative_ground_tracks.png`.

## External source module map

Paths below are relative to `S:src/simulations/` unless marked otherwise. Separate implementations are deliberately listed separately.

| Module/entrypoint | Inputs and dependencies | Workflow/output |
|---|---|---|
| `ditl/ANTARA_Science_Sim.py` | shared MissionConfig/ADCS; local EPS/FSM, orbit, SAA/GS, IGRF, environment, PayloadModel, communications | CLI scenario → orbit/guidance/FSM → gated payload/EPS/link → telemetry + event archives → summaries/figures/checkpoints |
| `ditl/scenarios.py` | shared defaults; LEOP inclusion flag | `leop_24h`, `no_leop_24h`, `leop_1yr` (8760 h) |
| `ditl/compare_scenarios.py` | existing scenario CSVs | streamed duration-weighted comparison; completeness requirements; not a propagator |
| `ditl/plot_fsm_diagram.py` | FSM rules, Graphviz | SVG/PNG/diagram documentation |
| `helper/antara_models.py` | NumPy, slew/wheel numerics | config, shared FSM/EPS/ADCS; Science deliberately has local FSM/EPS implementations |
| `helper/fsm_spec.py` | transition specification | drift guard; not proof that every local FSM matches |
| `helper/slew_profile.py`, `wheel_dynamics.py` | angular rate/acceleration, torque and momentum | event-resolved slews/wheel limits; approximate actuator model |
| `helper/telemetry_metrics.py` | full telemetry, intervals and end-state times | streaming exact summaries; display decimation is separate |
| `helper/pass_statistics.py`, `event_archive.py` | science samples/events | bounded statistics and append-only JSONL archive |
| `helper/serialization.py` | trusted versioned state | checkpoint compatibility; does not validate physics provenance |
| `helper/paths.py` | Orekit data locations | results/figures directories; no automatic Science download |
| `power/ANTARA_MCR.py` | module constants, randomized 7-RAAN campaign | seven CSV families, cutoff lifetime, simple constant-load EPS; runs on import |
| `power/ANTARA_avg.py` | independent 365-day/RAAN-75° config, 3 draws | battery/power study; runs on import |
| `power/ANTARA_FINAL_POWERGEN.py` | independent one-day equinox config | solar generation trade, different panel areas/efficiencies |
| `power/TradeCase.py` | hardcoded eclipse fractions, 97-min period, battery capacities | analytic DoD, SOC illustrations, assumed cycle-life summary |
| `orbit/ANTARA_drag_study.py`, `ANTARA_drag_finalconfig.py` | separate area/tumbling assumptions | 500–600 km sweep to 450 km, daily sampling, up to 30 years; runs on import |
| `conops/ANTARA_conops.py` | 2023 epoch, 30 days, Eckstein–Hechler, rectangular regions | encounter log, not topocentric RF visibility; runs on import |
| `pointing/ANTARA_pointing_budget.py` | 2026 one-day Keplerian orbit, +Z antenna | geometric boresight study, not Science +Y tracking |
| `thermal/ThermalSimulator.py` | independent ThermalMissionConfig | seven-node RK4 heat balance; CSVs/plots and hot/cold cases |
| `detumble/leop_detumble_mc.py` | shared ADCS, seeded samples/synthetic B | bounded or MC detumble trials; parallel worker entrypoint |
| `detumble/analyze_detumble_mc.py` | trusted MC pickle | plots/CSV summaries and fitted success contours |
| `legacy/ANTARA_Master.py` | independent legacy definitions | superseded; do not use to qualify current Science |
| `S:scripts/verify_physics_dependencies.py` | installed backends | dependency/backend probe, not detector validation |
| `S:scripts/generate_validation_report.py` | standalone subsystem checks | validation JSON/log/report, independent of MCR table transcription |
| `D:ANTARA_Science_Sim.py` | flat `paths` import, embedded MissionConfig | historical 5-channel DITL version, different payload/time accounting |
| `D:ANTARA_MCR.py` | flat `paths` import, 365-day/4-kg config | original annual RAAN tables; not latest cutoff campaign |
| `P:grid_common.py` | NumPy/Shapely | common 0.5° grid and polygon-overlap mask |
| `P:count_cell_passes.py` | Orekit data, grid_common | 3-day default geometric visits/dwell; CSV/XLSX/NPY/plots, NPZ restart |
| `P:step1_generate_irene_inputs.py` | static grid centroids | AP9 mean integral-flux config + ephemeris; external Windows IRENE invocation |
| `P:step2_process_irene_outputs.py` | external IRENE text, G=0.314 | isotropic rate fold and heatmap; cannot infer detector efficiency |
| `P:AbhishekSims/PROJECT_ANTARA.zip` | nested Geant4/CMake/GDML project | proton transport → per-thread ROOT deposition arrays |
| `P:AbhishekSims/plot_range.py`, `plot_wrt_thickness.py`, `pile_up_prob.py` | ROOT arrays or assumed rate | deposition/depth-proxy/pile-up figures |
| `P:AbhishekSims/step-to-gdml.py` | CAD conversion | geometry preparation; archived GDML must be separately identified |
| `D:GNSS/*.java` | Orekit/TLE, visibility, antenna/link and DOP helpers | separate GNSS visibility/link/DOP study; no trace to principal MCR science claims established |

No tier-disposition, duration-slice or 64-bin spectrum generating script was found in the inspected PDR archive. Do not attribute those files to `count_cell_passes.py` merely because they share a directory.

## Dependencies and tests

`S:requirements.txt` lists NumPy, pandas, SciPy, Matplotlib, Cartopy, Shapely, Skyfield, Graphviz, pytest, ppigrf 2.1.0 and SpacePy 0.7.0. Orekit/JVM are Conda dependencies. Orekit data, EOP/gravity/ephemeris/space-weather versions are separate scientific inputs; requirements do not pin these. PDR additionally needs openpyxl for its own XLSX exports, IRENE 1.58.001 as reported by the archived output, and Geant4/GDML/CMake plus uproot for transport plots. Presence of SpacePy is not live AP9 support.

Existing tests cover attitude, slew/wheel events, FSM transitions, finite-input guards, checkpoint/restart archives, telemetry weighting, scenario reporting, multiprocessing and subsystem reference checks. No recovered test suite qualifies Rev 2.1 detector response, grid tier construction or IRENE parser identity/units. Test execution and exact scope are in [ISSUES](ISSUES.md).

## Safe reproduction order

Inspect/configure without importing study modules → freeze source/config/data hashes → run pure accounting/geometry tests → short orbital/science tests in isolated output directories → review response/coverage → longer scenarios only after approval of the audit findings. No annual propagation, transport campaign, long-term drag run, download, or report rebuild was launched in this audit.

## Complete tracked file inventory at audit start

```text
.latexmkrc
NEW_RAAN_EVIDENCE_README.md
README.md
README_REVISED.md
REVISED_EVIDENCE_NOTES.md
REVISION_NOTES_2029.md
appendices/A_operational_logic_visual.tex
appendices/B_payload_detail_visual.tex
appendices/C_simulation_provenance.tex
appendices/D_thermal_structural_details.tex
appendices/E_budgets_and_bom_details.tex
appendices/F_orbit_rf_support.tex
appendices/G_source_detail.tex
appendices/H_source_detail.tex
appendices/I_source_detail.tex
appendices/J_source_detail.tex
appendices/K_integrated_ditl_detail.tex
appendices/L_new_evidence.tex
appendices/M_updated_raan_drag_study.tex
evidence/raan_2026-10-22/drag_lifetime_analysis.csv
evidence/raan_2026-10-22/mission_statistics.csv
evidence/raan_2026-10-22/orbit_classification.csv
evidence/raan_2026-10-22/raan_master_trade_matrix.csv
main.pdf
main.tex
media/ditl_overview.png
media/emsc.png
media/mmsc_4mo.png
media/msc_12mo.png
media/orbit_type_timeline.png
media/representative_ground_tracks.png
media/saa_3day.png
media/saa_magnetic_anomaly.png
media/spectrum.png
preamble.tex
sections/01_mission_context.tex
sections/01_mission_context_additions.tex
sections/02_mission_overview.tex
sections/02_mission_overview_additions.tex
sections/03_spacecraft_architecture.tex
sections/03_spacecraft_architecture_additions.tex
sections/04_simulations.tex
sections/04_simulations_additions.tex
sections/05_feasibility_and_budgets.tex
sections/05_feasibility_and_budgets_additions.tex
```
