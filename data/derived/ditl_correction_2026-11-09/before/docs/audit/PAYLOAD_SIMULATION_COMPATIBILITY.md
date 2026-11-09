# Current compatibility disposition — approved-v2

| Existing model/product | Remains usable | Cannot qualify |
|---|---|---|
| AP9/AE9 2026 mean/99 maps and reproduced rates | Preliminary 2029 environment planning, exact cell alignment and idealized rate conversion | Shielding, current G, accepted events, 5–100 MeV differential response, maximum trigger rate |
| Rev. 2.1 single main block + silicon | Historical design provenance | Current six-scintillator mechanics/readout or response |
| Legacy five-layer DITL/Geant4 | Historical reproduction, isolated accounting regression | Eleven-SiPM geometry, optical isolation, calibrated response/classifier or electronics |
| Grid passage/dwell simulations | Geometric opportunities with stated polygon/time assumptions | Independent measurements, qualified channels, precision, downlinked valid science |
| RAAN/EPS/drag products | Team-accepted preliminary planning references with original metadata and accounting caveats | Independently proven 2029 generation, current payload power/data rate or full success |
| Current configuration / accounting interfaces | Explicit inputs, units, histogram/timing/coverage contracts and software tests | Detector physical calibration or hardware selection |

Required interface: geometry/material/optical revision → species/angle/deposition/optical response → sensor/ASIC/ADC/trigger observable records → calibrated classification/reconstruction → 64-bin record with exposure/loss/background metadata → mission-tier evaluator. No valid implementation of this complete chain was found. Current `require_qualified_response()` refuses all unqualified response IDs. No archived output was changed in place. Source corrections are supplied as a tested but unapplied patch; local reference functions do not silently replace production simulators.

The following earlier compatibility review is preserved as historical evidence and is superseded wherever it conflicts with the current baseline.

---

# FPDU simulation compatibility review — 2026-11-04

This review precedes physical model changes. Only declarative metadata, payload documentation and bounded tests were added. No numerical result was changed in place. **CONFIRMED DESIGN INPUT** does not imply a calibrated response; revised energy response, optical response, calibrated efficiency, timing margin and event classification **REQUIRE VALIDATION** (status: **REQUIRES VALIDATION**).

Source shorthand follows the [repository map](REPOSITORY_MAP.md): `S` is the sibling `ANTARA_CODES-main` working tree; `P` is the supplied PDR Sims archive; `D` is the supplied MCR DATA archive; `G` is the nested `PROJECT_ANTARA/saa_sim` GEANT4 source. These are distinct source versions. Archive source members were inspected in `/tmp/antara-payload-update`, without launching archive scripts. Audit snapshots retain their original line references.

## Baseline comparison and disposition

| Source/model | Actual behavior / evidence | Compatibility with new configuration |
|---|---|---|
| Rev. 2.1 source DOCX, 18 September 2026, §§3,8,9,14 | One main scintillator; two-side minimum/four-side optional SiPM readout; active Si and rear tag; FPGA processing | Single-block wording and fixed FPGA preference are superseded. Silicon/rear concepts retained. Whether five blocks form one optical assembly is unresolved. No demonstrated response to transfer. |
| `S:src/simulations/ditl/ANTARA_Science_Sim.py:900–998` | Si + L1–L5 thicknesses 2/4/12/22/30 mm; layer/bin-index efficiencies and event-type map; 64 log bins | **Incompatible response.** New five main blocks are not old five layers. No adapter added. |
| `S:Science:604–610,1139–1157` | Ideal G ≈0.314159 cm² sr; differential spectrum × G × efficiency × ΔE × dt; per-bin nonparalyzable dead time; additive dark counts | Valid only as legacy expected-count arithmetic under stated assumptions. Not event reconstruction, calibrated efficiency or new payload yield. |
| `S:Science:837–843` | Diagnostic differential flux × G × efficiency lacks energy widths yet is treated as rate/dead-time input | Confirmed dimensional defect remains documented; not repaired by replacing it with the supplied estimate. |
| `S:src/simulations/helper/antara_models.py:242–257` | Five baseline spectral points; diagnostic dead time 1 µs; payload dead time 250 ns; coincidence field 20 ns | Distinct historical settings. New shaping 20 ns does not come from the old coincidence field. User now confirms current coincidence width 20 ns, tentatively suggests dead time 20 ns. No source parameter changed. |
| `S:Science:1030–1186` | Cell histograms, first-three-bin periphery merge, four-byte counters +16-byte header, event/cadence flush; event type from first bin | Arithmetic regressions remain useful. No new detector classifier or packet model; channel topology and telemetry not closed. |
| `D:ANTARA_Science_Sim.py:1700–1841` | Historical five-channel rates; different packet/count semantics; per-pass sums lack dt | Superseded evidence, not current 64-bin output or new-geometry validation. |
| `P:step2_process_irene_outputs.py:43–44,133–149` | Integral omnidirectional AP9 flux ÷4π ×0.314; ≥5 and ≥100 MeV thresholds differenced for band | Ideal isotropic incident-rate estimate, not reconstructed accepted counts/electronics triggers. Different geometric factor, no demonstrated new shielding/response. |
| `G:src/SteppingAction.cc:30–64`, `EventAction.cc:58–65` | Routes deposited energy into Si, L1–L5 and rear columns by old volume names | Superseded geometry/deposition evidence. No EJ-550/Teflon optical model, SiPM electrical response, ASIC/ADC or new classifier established. |
| `G:saa_sim.cc:32–34`; proton GPS macros | FTFP_BERT transport, proton-only source cases | Neither a mixed-field response nor electronics validation. Existing ROOT/plots remain historical. |
| `P:AbhishekSims/plot_range.py`, `plot_wrt_thickness.py:57–82` | Deposited energy and deepest-hit boundary proxy | Not calibrated incident-energy reconstruction or primary stopping endpoints. Do not reuse curves for new blocks. |
| `P:AbhishekSims/pile_up_prob.py:9–29` | Assumed 100 kHz, resolving window=2.5×shaping, Poisson overlap | Study-specific analytic illustration, not measured throughput/dead time or revised peak proof. |
| Grid visits/coverage (`P:grid_common.py`, `count_cell_passes.py`) | Geometric visits/dwell independent of new optical inputs | Preserved as geometry/exposure studies with prior audit limitations. Science-success claims still require correct coverage denominator plus qualified response/count uncertainties. |
| Existing EPS, packet/downlink and mission results | Legacy power/operations/response assumptions | Outputs remain unchanged, but do not close revised payload power, data volume or science yield. No unrelated model changed. |

The **PRELIMINARY ESTIMATE is 400 Hz peak proton count rate under protons-only incidence, 250 µm (0.25 mm) aluminium shielding, assumed geometric factor 1 cm² sr and assumed 100% detection efficiency**. Its generating simulation, spectrum and calculation remain unidentified. No reviewed file establishes its provenance. It must not replace differential spectra, count histograms or all-particle trigger demand. The 1 cm² sr assumption is not the old 1 cm² sensor area or old 0.314 cm² sr ideal acceptance.

## Missing executable interface

`config/payload/fpdu_2026-11-04.json` is a versioned input record, not consumed by existing simulators. Its exact JSON Schema prevents silent promotion of unknowns. `scripts/validate_payload_config.py` validates the immutable contract, computes material volumes and rejects every response binding while `qualified_response_id` is null. This guard protects future consumers only; the legacy simulator remains runnable under its old assumptions.

Before a physical adapter is justified, supply: controlled geometry/material/channel map → species/energy/angle deposits and secondary identities → optical photons/light response with quenching → SiPM gain/noise/saturation → ASIC shaping and ADC acquisition/digitization → timestamp/trigger/busy/buffer behavior → calibrated topology/reconstruction → histogram/packet interface. Every response product needs configuration/geometry hash, source spectrum, seed/statistics, units, calibration and validation record. A common filename or five-element count is not compatibility evidence.

## Bounded tests and remaining verification

Executed checks are logged in [changelog](PAYLOAD_UPDATE_CHANGELOG.md). Configuration tests verify supplied geometry, volumes, units, conditional rate labels, separate timing fields and rejection of legacy/unqualified response bindings. Optional legacy tests check expected-count conservation through bin merge, exposure scaling and zero-dead-time arithmetic with dark rate disabled. They do **not** classify measured events or prove zero hardware loss.

The following tests are specified for implementation once the named interface exists; no invented hardware simulation was added:

| Test | Bounded fixture / pass criterion | Missing input |
|---|---|---|
| Event-to-energy histogram conservation | Feed lower edge, internal edges, upper edge, underflow, overflow, NaN and saturation; each finite classified event enters exactly one documented category; accepted+rejected+invalid counters equal input events; specify last-edge policy | Calibrated classifier, bin edges, overflow policy. Legacy expected-count merge is not this function. |
| Zero hardware dead time | Synthetic timestamps, including simultaneous hits; with configured zero busy time, accepted+explicitly rejected events equals arrivals, no artificial busy losses | Trigger/event processor; timestamp tie policy and shared/per-channel semantics |
| ADC/event throughput | Sweep explicit assumed nominal and peak **all-particle** trigger rates; separately use the conditional proton estimate above only as a labeled load fixture. Vary ADC initiation/service interval independently from conversion latency; compare utilization λ×service interval, queue depth, overflow and processed counts against a hand-scheduled deterministic stream | Nominal rate absent, peak total triggers absent, service interval and buffers absent; conditional proton rate is not an all-particle limit |
| Burst/overflow | Empty, single, simultaneous burst of B and B+1 events, then drain; assert arrived=processed+rejected+overflow+queued at every step; test service start/end ties | Buffer capacity B and busy/trigger policy |
| MCU preference with configurable margin | Let budget T and required reserve m be explicit test inputs. Require T>250 ns and measured worst-case latency plus allocated timing uncertainty ≤T(1−m), with an agreed additional interpretation of “comfortably”. Synthetic examples only: T=500 ns, m=.2, latency+jitter=300 ns passes this necessary inequality; 450 ns fails; T=250 ns fails preference regardless of latency | Real processing budget, margin and WCET/jitter; arithmetic alone cannot select MCU |
| FPGA timing candidate | Apply the same latency/uncertainty/reserve inequality with FPGA evidence; T=100 ns, m=.2, 70 ns passes arithmetic, 90 ns fails. No MCU 250 ns preference threshold is imposed on FPGA | Candidate FPGA path and measured/implemented timing; throughput checked separately |
| Coincidence/dead-time independence | Sweep coincidence width around the current 20 ns input while holding busy time fixed, then sweep busy time independently; tagged timing acceptance and busy losses must respond to the appropriate parameter | Edge convention, jitter and trigger implementation; tentative dead time 20 ns requires measurement |
| Response compatibility | Reject old L1–L5 and unqualified Rev. 2.1 matrices even if file dimensions match; require exact controlled geometry/material/channel/response IDs and calibration evidence | No qualified revised matrix available; current configuration guard therefore rejects all bindings |

These are proposed verification procedures, not reported successful hardware/Monte Carlo tests. No annual simulation, Monte Carlo transport, firmware qualification or physics calibration was performed.

## Source control evidence

The three supplied `ANTARA_FPDU_Payload_Redesign_Verified*.docx` files were compared by SHA-256 and are byte-identical (`32d425c80b4851a54b93375efab3fc65a3a91f402223aa409e6dc90e954b3487`); no identity was inferred from naming. Their “Verified” title describes a design/analysis baseline, not new detector qualification. The supplied ICDs/CAD archive contains COTS structure, ADCS, panel, navigation and radio interfaces; no current custom FPDU five-block assembly drawing was located. Legacy payload GDML is a different source and does not resolve this gap.
