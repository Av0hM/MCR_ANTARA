> **Current-baseline supersession (2026-11-04):** Use [FPDU_APPROVED_BASELINE.md](FPDU_APPROVED_BASELINE.md), [2029_AUDIT_RECONCILIATION.md](2029_AUDIT_RECONCILIATION.md) and [REMAINING_OPEN_DECISIONS.md](REMAINING_OPEN_DECISIONS.md). The record below is retained as historical audit evidence. Silicon is removed, rear detection optional, main blocks longitudinal along X, eleven SiPMs on ±Y/main plus front, Teflon 0.11 mm per ±Z face. Coincidence references are 200/250/300 ns, shaping 20 ns, qualified dead time unknown. Optical isolation remains open. Earlier 20 ns coincidence/dead-time guesses and unresolved coating-thickness interpretation are superseded.

# Payload response and counting audit

> **2026-11-04 payload follow-up:** The audit below is the unchanged 2026-11-02 finding snapshot, with original source line references. The current narrative specification is [Appendix A.2](../../appendices/B_payload_detail_visual.tex), updated with five main blocks plus a front scintillator, EJ-550 coupling and candidate MCU/FPGA processing. Current coincidence input is 20 ns; a separately suggested 20 ns dead time is tentative. See [compatibility review](PAYLOAD_SIMULATION_COMPATIBILITY.md), [open decisions](PAYLOAD_OPEN_DECISIONS.md) and [change log](PAYLOAD_UPDATE_CHANGELOG.md). Documentation updates do not close the historical physics/model findings.

Audit date: 2026-11-02. Audit only; simulation code, input configurations, scientific results and MCR source were not changed.

**Source notation:** `R:` means this MCR repository; `S:` means `/home/sammo/Desktop/Projects/ANTARA_CODES-main/`; `P:` means the `PDR Sims/` member tree in `/home/sammo/Downloads/PDR Sims-20261021T072428Z-1-001.zip`; `D:` means the `MCR DATA/` member tree in `/home/sammo/Downloads/MCR DATA-20261021T072514Z-1-001.zip`; `G:` means `PROJECT_ANTARA/saa_sim/` inside `P:AbhishekSims/PROJECT_ANTARA.zip`. Archive members were read from disposable copies under `/tmp/antara-audit/`. Line numbers refer to the inspected working files/archive members, not an assumed common version. See [repository map](REPOSITORY_MAP.md) for scope and source identities.

**Evidence terms:** Confirmed = demonstrated by inspected code, file comparison or arithmetic. Suspected = plausible consequence needing a discriminating test. Unestablished = the producing inputs/revision or required validation were not recovered. A passing regression is not physical validation.


## Three different payload models must remain separate

1. **Historical DITL** (`D:ANTARA_Science_Sim.py:1700–1841`): five differential environment channels, rate arrays, a rate-scaled data-volume formula and per-pass summaries. This is the source-compatible schema for the 2000-epoch DITL CSV, not today's 64-bin packet model.
2. **Current Science** (`S:src/simulations/ditl/ANTARA_Science_Sim.py:872–1275`): idealized five-layer telescope, 64 expected-count bins, event-driven histogram packet flushes. Layers 2/4/12/22/30 mm plus silicon/rear-veto definitions remain in code.
3. **MCR Rev 2.1** (`R:appendices/B_payload_detail_visual.tex:1–98`): one scintillator block, silicon coincidence, side SiPM observables and rear penetration tag; stopping/penetrating response functions and mixed-species response matrix are proposed. Those functions are not implemented/validated by either model above. G transport also uses the old multi-layer geometry.

This is a **confirmed model/baseline mismatch**, not a claim that a future one-block instrument cannot work. Retain historical studies under explicit legacy labels; they cannot demonstrate the revised payload's acceptance, energy resolution or purity.

## Current counting path

`MissionConfig.energy_channels_mev` and baseline flux → SAA depth/pitch/east–west/storm factors → linear interpolation to 64 geometric energy-bin centers → `raw_rate_i = differential_flux_i × G × efficiency_i × ΔE_i` → per-bin nonparalyzable dead-time factor → additive dark rate → `expected_counts_i = rate_i × dt` → optional first-three-bin sum → cumulative cell histogram and pending packet accumulator.

- Flux units are particles cm⁻² s⁻¹ sr⁻¹ MeV⁻¹; multiplying by cm² sr, MeV, seconds is necessary to obtain counts. Current payload includes width and dt (`Science:1139–1143`). It generates fractional expected counts, not Poisson draws or event reconstruction.
- G=0.314159 cm² sr is internally consistent with a 1 cm² ideal planar sensor and 18.435° sharp cone. A finite 10 mm-radius aperture 30 mm away from a square 10×10 mm sensor does not by itself prove a uniform sharp cone or energy-independent acceptance.
- Efficiencies (.92×.85 through .90×.99, etc.) are hardcoded layer factors (`Science:938–948`), not calibrated response matrices. Silicon entrance losses, light transport, temperature/noise, Birks quenching, SiPM saturation, ADC resolution, electron/heavy-ion leakage and angular migration are not quantified by this calculation.
- No inversion/unfolding or reconstruction from measured deposited energy is executed. Energy bin/layer/event-type assignment is by bin index (`Science:962–998`), not by observed signals. The `validate_contiguous_pattern` helper is not proof of a functioning event classifier.

## Confirmed defects and their scope

| Finding | Source | Consequence / verification |
|---|---|---|
| Historical per-pass totals sum rates without dt | D:ANTARA_Science_Sim.py:1819,1841; records retain rates at 1784 | At 2 s cadence, summing Hz misses ×2 even before fixing differential-channel width. Verify constant physical exposure at 1/2/4 s yields invariant counts; withdraw old 13k–108k count-derived success claims. |
| Environment diagnostic rate lacks energy width but is treated as counts/s and given dead-time suppression | S:Science:813,837–843; analogous D environment path | Differential rate has units s⁻¹ MeV⁻¹; adding .5 Hz and multiplying by seconds of dead time is not dimensionally valid. Current PayloadModel has a separate width-aware path, so do not automatically apply this finding to its counts. Test integrated flat-spectrum known-band counts. |
| `_cell_pass_counts` counts generation calls | S:Science:1115–1119 | One visit becomes many “passes” and changes with dt. Currently private state, not proof that MCR tier CSVs used it. Verify 100 steps in one visit count as one unique pass. |
| Rear-veto mask is unreachable with current bin map | S:Science:929,962–978,1135–1137 | map returns only L1–L5, so rear_veto mask is always false; Type6/rear-veto-specific efficiency branch also unreachable (1042–1045). Boundary tests should exercise stopping and penetrating topology, rather than assume the branch executes. |
| Returned event_type always first bin's type | S:Science:1181–1186 | `event_types[0]` is Type1 for every sample; per-pass event labels are not topology distributions. Test a high-energy-only input, expected Type6/tagged classification after redesign. |
| Historical science-data “background-only header” behavior contradicts formula | D:Science:1757–1775 | total_count_rate includes ≥background; dividing by nominal background makes count_scale≥1, capped to 1. Zero proton signal still emits full science payload rather than just 16-byte header. Verify zero-signal fixture; current flush model supersedes this. |
| Range plot is deepest active layer's far boundary, labeled “Proton Stopping Endpoint” | P:AbhishekSims/plot_wrt_thickness.py:57–82 | Not a tracked stopping point; penetrating events and secondary deposits can set deepest layer. Verify primary-track endpoint/escape flag against the proxy and relabel historical plot after review. |

## Suspected model errors and missing physical validation

**Global versus per-bin dead time (high priority).** Current Science applies `1/(1+r_i τ)` independently to energy bins (`1139–1142`), while the architecture describes a coincidence telescope/front-end. If bins share acquisition dead time, the live fraction should depend on total trigger rate including rejected/background events. Splitting an unchanged spectrum into more bins then increases modeled accepted total. Hardware topology has not been frozen, so this is a suspected physical-model error, not an experimentally confirmed detector defect. Test bin-refinement invariance with τ=0 and a shared-trigger finite-τ benchmark; measure τ before selecting the model. Arithmetic mean livetime across bins (`1083–1086`) is not automatically detector exposure.

**Two dead-time settings.** `detector_dead_time_sec=1e-6` and `detector_dead_time_ns=250` differ by four (`S:models:245,257`). They feed different paths. This is a confirmed inconsistency of model assumptions, not evidence of a fourfold error in every exported result.

**Background and precision.** Dark rate .5 Hz is added separately to all 64 bins; outside signal this can improve apparent `1/sqrt(N)` precision. Flux error after background subtraction depends on background uncertainty, not total accepted counts alone. `1/sqrt(max(N,1))` reports 100% at zero counts rather than undefined flux precision (`1157,1209`); no exposure/calibration/systematic uncertainty is propagated. Test zero-signal/high-background and calibration-error floors, plus correct low-count confidence intervals.

**Merged bins.** Periphery bins 1–3 are summed into bin 1 and two counters zeroed (`1146–1152`), but returned edges/centers still describe the original 64-bin grid (`1214–1215`). Counts are conserved, but the effective merged response/width is not communicated by altered edges. A downstream flux estimator may divide by the old first-bin width. Test round-trip serialized counts plus response metadata and confirm invariance of integrated flux. This is an interface hazard, not proof an absent downstream reconstructor made that mistake.

**IRENE grid rates.** P's .314/(4π) fold assumes isotropic omnidirectional flux and ideal detection. It supplies total ≥5 MeV and optionally 5–100 MeV band rates, not 64 independent calibrated energy channels. Mean and percentile inputs have different thresholds/statistical semantics. No direct equality to Science's directional baseline should be imposed.

## Transport evidence

G uses FTFP_BERT and GDML with silicon, aluminium and polystyrene volumes. ROOT contains deposition branches `E_primary`, `E_Si`, `E_L1`–`E_L5`, `E_Veto`; eight thread files are archived, but were not replayed in this audit. `range_verification.mac:8–16` scans 5–150 MeV (comment says 5–100); `saa_core_physics.mac` uses an assumed spectrum, 10 mm circular plane and 18.4° angular bound, not a recorded orbit-specific response campaign. No electronics/optical response or mixed-field purity measurement follows from energy-deposition plots.

`G:src/SteppingAction.cc:33` adds all deposited energy to the legacy total, and `RunAction.cc:90–96` divides by the chosen scoring volume's mass. GDML's `PayloadLV` is the world container (`geometry/payload-3.gdml:9907`), not an individual sensitive silicon/scintillator volume. This output cannot be interpreted as detector-specific absorbed dose. Confirm total mass selection and whether daughter mass is included before quantifying its bias; test two materials/volumes with separately scored deposits.

P's pile-up plot assumes 100 kHz (`pile_up_prob.py:9`), while its ideal mean and 99th-percentile ≥5 MeV maps peak at 116.39 and 320.60 Hz. These are distinct assumptions, not evidence to select any one as the flight peak. A mixed-species L0-rate fold and bench throughput tests must resolve them.

## Verification sequence

Freeze Rev 2.1 mechanical/material geometry → independently calculate geometric acceptance → monoenergetic/angular/species transport with truth-tagged stopping/escaping tracks → optical/electronics/noise/dead-time model → response and confusion matrices → injected-spectrum reconstruction closure → background/calibration-aware per-channel count/exposure products → coupled short Science yield and packet tests. Existing regression passes only establish software behavior within the old model.
