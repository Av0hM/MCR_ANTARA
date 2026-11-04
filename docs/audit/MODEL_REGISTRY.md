> **Current-baseline supersession (2026-11-04):** Use [FPDU_APPROVED_BASELINE.md](FPDU_APPROVED_BASELINE.md), [2029_AUDIT_RECONCILIATION.md](2029_AUDIT_RECONCILIATION.md) and [REMAINING_OPEN_DECISIONS.md](REMAINING_OPEN_DECISIONS.md). The record below is retained as historical audit evidence. Silicon is removed, rear detection optional, main blocks longitudinal along X, eleven SiPMs on ±Y/main plus front, Teflon 0.11 mm per ±Z face. Coincidence references are 200/250/300 ns, shaping 20 ns, qualified dead time unknown. Optical isolation remains open. Earlier 20 ns coincidence/dead-time guesses and unresolved coating-thickness interpretation are superseded.

# Model and configuration registry

> **2026-11-04 payload follow-up:** The audit below is the unchanged 2026-11-02 finding snapshot, with original source line references. The current narrative specification is [Appendix A.2](../../appendices/B_payload_detail_visual.tex), updated with five main blocks plus a front scintillator, EJ-550 coupling and candidate MCU/FPGA processing. Current coincidence input is 20 ns; a separately suggested 20 ns dead time is tentative. See [compatibility review](PAYLOAD_SIMULATION_COMPATIBILITY.md), [open decisions](PAYLOAD_OPEN_DECISIONS.md) and [change log](PAYLOAD_UPDATE_CHANGELOG.md). Documentation updates do not close the historical physics/model findings.

Audit date: 2026-11-02. Audit only; simulation code, input configurations, scientific results and MCR source were not changed.

**Source notation:** `R:` means this MCR repository; `S:` means `/home/sammo/Desktop/Projects/ANTARA_CODES-main/`; `P:` means the `PDR Sims/` member tree in `/home/sammo/Downloads/PDR Sims-20261021T072428Z-1-001.zip`; `D:` means the `MCR DATA/` member tree in `/home/sammo/Downloads/MCR DATA-20261021T072514Z-1-001.zip`; `G:` means `PROJECT_ANTARA/saa_sim/` inside `P:AbhishekSims/PROJECT_ANTARA.zip`. Archive members were read from disposable copies under `/tmp/antara-audit/`. Line numbers refer to the inspected working files/archive members, not an assumed common version. See [repository map](REPOSITORY_MAP.md) for scope and source identities.

**Evidence terms:** Confirmed = demonstrated by inspected code, file comparison or arithmetic. Suspected = plausible consequence needing a discriminating test. Unestablished = the producing inputs/revision or required validation were not recovered. A passing regression is not physical validation.


## Configuration identities

| Model | Epoch/duration | Physical and numerical parameters | Location/status |
|---|---|---|---|
| Approved MCR design | 2029-01-01; ~5-year operations objective | 600 km, 97.6°, e=0.001; maximum 3 kg; launch-dependent RAAN; Rev 2.1 one-block payload | R:sections/02_mission_overview.tex:10,30; design requirement, not completed run |
| Current Science working tree | 2000-03-01; 24 h default, 8760 h preset | 3 kg, 600 km, 97.6°, e=.001, RAAN **30°**; Cd=2.2, Cr=1.8, area .01 m² | S:helper/antara_models.py under src/simulations, lines 78–99; RAAN locally modified |
| Archived DITL | 2000-03-01, 24 h; 2 s sampling | same listed orbit except RAAN 15°; embedded config, 5 environment channels | D:ANTARA_Science_Sim.py:134–155; raw event timestamps confirm epoch; exact run manifest absent |
| Latest MCR campaign candidate | 2026-01-01; 3650 days cap | 3 kg, 97.6°, 600 km, e=.001; RAAN 0:30:180°, 2 draws each; 300 s samples; 300 km cutoff | S:src/simulations/power/ANTARA_MCR.py:96–136,537; output copies match but exact producing revision/seed unestablished |
| Archived MCR campaign | 2026-01-01; 365 days | 4 kg, 97.4°, same RAAN set, 2 draws; 300 s | D:ANTARA_MCR.py:90–130; different outputs from latest campaign |
| Dedicated drag variants | 2000-01-01 12 UTC; up to 30 years | 4 kg, 98°, e=.0001; 500–600 km; area .076799 m²; multiplier 1 or 1.5; Cd=2.2; RK4 60 s, daily observations, 450 km cutoff | S:src/simulations/orbit/ANTARA_drag_{study,finalconfig}.py:44–121; no reentry calculation |
| Grid encounter propagation | 2026-01-01; **3 days in supplied source** | 600 km, 3 kg, e=.001, RAAN 15°; inclination from first-order J2 SSO formula; 1 s samples; area .01 m² | P:count_cell_passes.py:103–172; 546-day output config not archived |
| IRENE mean grid | fixed 2026-01-01, GDZ 600 km | AP9, mean, integral thresholds 5 and 100 MeV; one centroid/overlap cell | P:step1_generate_irene_inputs.py:44–55; corresponding raw mean output missing |
| IRENE percentile grid | MJD 61041 (2026-01-01), GDZ 600 km | AP9 integral omnidirectional ≥5 MeV, percentile 99 config | P:IRENE/irene_config_rate.txt:1–9; output header reports software 1.58.001; not mean/differential flux |
| Thermal | 2000-03-01 nominal; 24 h, 2 s/10 substeps | 600 km, 97.6°, RAAN 15°, 3 kg; seven thermal nodes; internal 1.8 kg × 800 J/kg/K; T0=293.15 K | S:src/simulations/thermal/ThermalSimulator.py:280–400; synthetic heat schedule, not DITL coupling |
| CONOPS | 2023-01-01 12 UTC, 30 days, 60 s | Eckstein–Hechler orbit, rectangular SAA/Goa classifiers | S:src/simulations/conops/ANTARA_conops.py:25–55 |
| Pointing | 2026-01-01 12 UTC, one day | Keplerian, nadir +Z antenna, 10° station mask, 30 m station altitude | S:src/simulations/pointing/ANTARA_pointing_budget.py; local changes preserved; distinct from Science |
| Solar-only final study | 2026-03-20 equinox, 24 h, 30 s | 97.4°; .021 m² fixed + 2 × .018065 m²; efficiency .30 × .72675 | S:src/simulations/power/ANTARA_FINAL_POWERGEN.py:41–61,114 |
| Annual average study | 365 days, 300 s, 3 draws | RAAN 75°, 4 kg, 97.4°; 25 Wh, 8 W load | S:src/simulations/power/ANTARA_avg.py:90–153 |
| Battery analytic trade | no propagated epoch | 10/15/20/25/30 Wh; 97 min period, 8 W; precomputed eclipse fractions; 10 s SOC illustration | S:src/simulations/power/TradeCase.py:20–144; cycle life assumed |

## Physical models and units

| Model | Implemented assumptions and units | Validation boundary |
|---|---|---|
| Science propagation | EME2000 inertial, WGS84 ellipsoid/ITRF Earth-fixed; equinoctial numerical integration, DP853; 10×10 normalized gravity; NRLMSISE00 preferred, DTM2000 fallback; isotropic drag/SRP | S:Science:2458–2555. Atmosphere/weather provenance and fallback activation must be recorded per run. Position m, velocity m/s, elapsed s, UTC dates. |
| MCR propagation | DP853, 5×5 gravity, Sun/Moon third bodies, DTM2000, .076799 m² isotropic drag/SRP area | S:MCR:566–649. Its area is 7.679 times Science's .01 m²; no common lifetime implication. Cutoff altitude is radial norm minus equatorial radius, not geodetic altitude (lines 701–705). |
| Magnetic field | Science shared ADCS default `dipole`; IGRF helper via ppigrf, ENU nT → NED T → inertial rotation at query date; optional dipole fallback | S:models:171,251 and Science:485–603. A successful import or mocked frame test is not field calibration. |
| Attitude | scalar-first body-to-inertial quaternion; +X RAM/payload, +Y relay/nadir, +Z fixed panel; finite slew and wheel-capacity events | S:models:69–75,101–109; approximate slew torque proxy, not fully coupled flight controller. 0.4° is configured performance, not a measured acceptance result. |
| Integrated EPS | 25 Wh capacity, 18 Wh initial; .085 m², efficiency .193515, 1361 W/m², charge and temperature factors .88 each; 22 W parameter | S:models:111–133,197; local Science EPS consumes its own functions. OBC .8 W, EPS 1.2 W, payload 10 W (+2 W coincidence parameter), TX 12 W, ADCS .8/4.5 W. |
| MCR EPS | 25 Wh initial/capacity, 8 W constant load; fixed .030 + two .030 m² panels; .28 cell × .513 system efficiency; fixed body −Z, wings use randomized tracking-loss cosine | S:MCR:115–132,260–339. Wings do not consume actual common body incidence. Degradation 1−.05×mission_fraction, not a fixed EOL-only evaluation. |
| MCR battery aging | throughput integrates pre-clamp net energy; cycles=throughput/(2×25 Wh); capacity=25×(1−.00005×cycles) | S:MCR:813–841. Counts curtailed charging as throughput; impact on reported thousands of cycles/capacity needs recalculation. |
| Ground contact | Science topocentric elevation, Goa 15°N/74°E/70 m, mask 15°; optional Svalbard off by default; 19.2 kbit/s parameter | S:models:140–152; MCR instead uses lat 0–20°, lon 60–80° box (MCR:213–219). No common RF margin. |
| Environment | five differential baseline points 5/10/20/50/100 MeV with 35000/18000/6000/900/110 particles cm⁻² s⁻¹ sr⁻¹ MeV⁻¹ | S:models:242–250; no live AP9. Polygon-depth factor .5–2, empirical pitch exponent .5, east–west ±.15, optional storm ×1.5. No response-calibrated absolute environment. |
| Current payload | 64 log bins 5–100 MeV; expected counts, G=π sin²(arctan(1/3))=0.314159 cm² sr, 1 cm² ideal sensor, five-layer assignment | S:Science:900–998,1139–1157; old architecture, no Rev 2.1 reconstruction. 250 ns per-bin dead time vs environment diagnostic 1 μs; .5 Hz dark rate added to each bin. |
| PDR rate fold | rate=integral omni flux × .314/(4π), Hz; 5–100 band is difference of threshold rates | P:step2:133–149. Isotropy and ideal efficiency assumed; ≥5 MeV includes >100 MeV. |
| Geant4 transport | FTFP_BERT; imported multi-layer GDML; GPS proton-only macros; event energy deposited per named layer (MeV) | G:saa_sim.cc:32–34; RunAction/EventAction/SteppingAction. No optical photon/SiPM/ADC response or mixed-field classifier demonstrated. |
| Pile-up | P=1−exp(−R×2.5×shaping_time), assumed R=100000 Hz | P:AbhishekSims/pile_up_prob.py:9–29. This is not derived from the grid rate file (max mean ≥5 rate 116.39 Hz, 99th-percentile 320.60 Hz under its different assumptions). |
| Thermal balance | six face nodes + bus; solar/albedo/Earth IR/radiation/conduction; RK4; 2.7 K space; σ=5.670374419e−8 W m⁻² K⁻⁴; .05 W/K face coupling | S:Thermal:316–380; heat-load and optical assumptions independent of flight hardware. No structural FEA/qualification evidence recovered. |

In this table `models`, `Science`, `MCR`, and `Thermal` abbreviate the corresponding fully named `S:src/simulations/` files in the repository map.

## Required run manifest

Record source commit **and dirty diff/hash**, complete resolved config, preset/CLI overrides, RNG algorithm/seed and each MC draw, geometry/response version, backend/fallback names, Orekit/IGRF/space-weather/model-database hashes and supported date ranges, units/coordinate convention, time horizon/actual termination reason, timestep controls, completion marker, output hashes and processing script. Current defaults cannot retroactively supply missing metadata. `min_soc` in the latest trade is the **mean of run minima** (MCR:994), not the worst sample across both runs.

## Working-source fingerprints

| Source | SHA-256 |
|---|---|
| `S:src/simulations/helper/antara_models.py` | `3c10b328a48b7a9705e61d17d4e445a67266567ed7a5dd25fc20b13c9a209ed5` |
| `S:src/simulations/ditl/ANTARA_Science_Sim.py` | `92baa85028d79c9ebb347e5a8a5c17325c814b7ef42ad3dbefbefc3076724413` |
| `S:src/simulations/power/ANTARA_MCR.py` | `cdb98ac45806865244a275ba5c0cd40434394af26cd2ca85f9596f31f8a63fd0` |
| `D:ANTARA_Science_Sim.py` | `ab79a250fa342cddad9f720a5eb800855ceca6990b6e4664b5063181e3dfc088` |
| `D:ANTARA_MCR.py` | `b6efac228fccbfc210f3833ce2c43557a4a1cd1438053a06f23d6411e7a4fb9c` |
| `P:count_cell_passes.py` | `9b10a909211753165aba494efbde7f7daa72ec4f17c6046382e99b7dd0dbca22` |
| `P:grid_common.py` | `9eec601e2f12174340333110257e4b842fe02b35d6b057c1f2a30df7afc8ae9d` |

## Current payload input revision — 2026-11-04

`config/payload/fpdu_2026-11-04.json` and its exact schema record CONFIRMED DESIGN INPUT: five 6×6×14 mm main blocks, one 6×6×2 mm front piece, two Teflon-coated sides per main block with stated 0.11 mm thickness, and EJ-550 grease. Geometry axes/assembly, coating interpretation, material and channel map remain unknown. Material volume is 2592 mm³ = 2.592 cm³, not packaged volume. Silicon and rear detector retained.

PRELIMINARY ESTIMATE: 400 Hz peak proton count rate, protons only, 250 µm (0.25 mm) aluminium, assumed geometric factor 1 cm² sr and assumed 100% efficiency. User-supplied; generator, spectrum, integration bounds and epoch unknown. No electronics limit inferred.

CANDIDATE ARCHITECTURE: SiPM→ASIC→ADC→MCU/FPGA→classification/binning. Shaping 20 ns and a stated ASIC-to-ADC 20 ns interval do not define total latency. User follow-up confirms current coincidence width 20 ns; suggested dead time 20 ns remains REQUIRES VALIDATION and distinct from the null qualified-dead-time field. MCU budget preference comfortably >250 ns requires measured margin. No response adapter or power/packet model is supplied. Calibration/optical response/event classification remain REQUIRES VALIDATION.
