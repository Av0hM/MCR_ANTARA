> **Scope update (user direction, 2026-11-09):** Exclude the short24h-named outputs from MCR operational evidence. Use only the `leop_1yr` group for operations, retaining its incomplete-telemetry and incompatible-event limitations. Thermal and detumble remain separate studies. One-hour calculations below are retained as an audit trail, not adopted comparison results.

# LEOP versus No-LEOP validation: supplied one-hour windows

**24-hour comparison blocked by absent full-day outputs.** Both filenames contain24h but both end with a valid zero-duration terminal snapshot at3600s. All1801 timestamps are unique, monotonically increasing with2s intervals before terminal. No missing interval was filled. An optional request for full-day paths was sent; independent analysis proceeded.

## Comparability

Recorded latitude/longitude/altitude arrays match exactly across these two traces. Initial battery is not logged before the first integration interval; first recorded state is at2s. Candidate default18Wh is consistent with the energy balance but not an independently supplied initial-state manifest. Capacity25Wh is used only for explicitly labelled planning-normalized SOC. Both panel_deployed flags remainFalse; that flag alone cannot establish actual surface geometry or deployment mechanism state. Full attitude, angular-rate, orbit/RAAN, epochs, EPS layout, ground station, seed and solver configurations are missing. Therefore: **INSUFFICIENT EVIDENCE for a controlled LEOP-only causal comparison**, despite a directly comparable observed time/position window. Do not turn startup into an avoidable burden or infer annual availability.

## Independent interval accounting

Each row owns [time_sec,state_time_sec), weighted by interval_duration_sec. Terminal contributes no elapsed time or energy, but any final packet must remain in data totals. The table reports No-LEOP minus LEOP; percentages use LEOP as denominator only when nonzero.

| Metric | LEOP | No-LEOP | Difference | Relative change |
|---|---|---|---|---|
| Elapsed (s) | 3600.000000 | 3600.000000 | +0.000000 | +0.000% |
| SAA geographic dwell (s) | 0.000000 | 0.000000 | +0.000000 | N/A |
| Science acquisition gate (s) | 0.000000 | 0.000000 | +0.000000 | N/A |
| Contact visibility (s) | 0.000000 | 0.000000 | +0.000000 | N/A |
| Generated source MB | 0.000000 | 0.000000 | +0.000000 | N/A |
| Transferred source MB | 0.000000 | 0.000000 | +0.000000 | N/A |
| Maximum storage source MB | 10.000000 | 10.000000 | +0.000000 | +0.000% |
| First recorded battery (Wh) | 17.998889 | 18.003631 | +0.004742 | +0.026% |
| Minimum recorded battery (Wh) | 15.209250 | 18.003631 | +2.794381 | +18.373% |
| Final battery (Wh) | 15.209250 | 19.570485 | +4.361235 | +28.675% |
| Integrated recorded solar (Wh) | 0.000000 | 4.961517 | +4.961517 | N/A |
| Integrated load (Wh) | 2.790750 | 3.391032 | +0.600282 | +21.510% |
| COLD_AND_DARK (s) | 122 | 0 | -122 | -100.000% |
| DETUMBLE (s) | 2460 | 0 | -2460 | -100.000% |
| SUN_POINTING (s) | 952 | 3600 | +2648 | +278.151% |
| DETECTION (s) | 0 | 0 | +0 | N/A |
| RELAY (s) | 0 | 0 | +0 | N/A |
| SLEWING (s) | 64 | 0 | -64 | -100.000% |
| SAFE (s) | 2 | 0 | -2 | -100.000% |

Minimum recorded SOC using25Wh is60.8370% versus72.0145%; the latter is the post-first-step minimum, not proof that initial SOC exceeded72%. Both end with10 source-labelled MB storage and no new data. Load integration and recorded battery changes are consistent with18Wh initial energy within floating-point residuals in these two windows. LEOP solar is identically0; No-LEOP integrates4.961517Wh recorded solar and3.391032Wh load. Source solar_w may already include conversion/charge factors; do not apply those again or claim available array margin. The final battery difference4.361235Wh is a descriptive comparison with unclosed configuration identity.

Mode occupancy fractions use3600s: Cold/Dark3.3889%, Detumble68.3333%, Sun Pointing26.4444%, Slewing1.7778%, Safe0.0556% in LEOP; No-LEOP is100% Sun Pointing. Science/Relay time is0. LEOP Sun Pointing is labelledECLIPSE for952s; passive/eclipse submodes are not additional disjoint primary modes. No-LEOP submodes remain in its JSON summary.

## Event consistency

LEOP event log lists Cold/Dark ending120s, detumble120–2580s (2460s), and a66s slew2586–2652s. Telemetry labels Cold/Dark for122s, Detumble122–2582s, a64s slew2588–2652s, then Safe2652–2654s. Event log records Safe entry and exit both2652s. This is a confirmed2s mode-label/event boundary discrepancy, not silently corrected. The SAFE reason is persistent pointing-budget violation; it is not evidence of battery brownout. No-LEOP transition/slew/detumble files are blank and telemetry has no such events. Exact event/telemetry match is false for LEOP and true for No-LEOP.

## Exposure and communications

Elapsed3600s; geographic SAA dwell0; Detection0; acquisition-enabled0; visibility0; relay link0; generated/transferred0 for both. Thus SAA science-duty fractions are **undefined (0/0)**, not0% or62.7%. Accepted detector exposure, valid reconstructed measurements and delivered current-FPDU records are unqualified. Zero counts in these runs say nothing about FPDU sensitivity. Blank event files alone are weak evidence, but telemetry independently confirms no encounters/contacts here. Gross capacity over this observed zero-contact window is0 under any finite rate; no daily capacity can be inferred.

Figures: `one_hour_operations.png`, `one_hour_power_pointing.png`, `one_hour_occupancy_energy.png` under `evidence/science-ditl/figures/`. They use the verified60-minute duration, common axes and explicit model labels. No decorative zero-exposure/contact chart is added.
