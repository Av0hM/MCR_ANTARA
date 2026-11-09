> **Approved-baseline follow-up:** The original ingestion audit below is preserved. The unified implementation now accepts this 2026 source as a preliminary 2029 planning reference, verifies its exact polygon cell domain, and incorporates qualified statements in the MCR. See [count-rate reconciliation](FPDU_COUNT_RATE_RECONCILIATION.md) and [implementation record](IMPLEMENTATION_CHANGELOG.md). No raw rate or flux output was changed.

# Count-rate MCR recommendations — 2026-11-04

**Recommendation: report reproducible environmental rate estimates as provisional study evidence, not qualified payload performance.** Do not change the MCR LaTeX until these findings are reviewed. No LaTeX was edited in this ingestion.

## Proposed reporting language

> Supplied IRENE 1.58.001 AP9/AE9 integral omnidirectional flux maps contain 7,940 geographic cells at 600 km and MJD 61041 (2026-01-01). Under an isotropic conversion with assumed geometric factor 1 cm² sr and unit efficiency, the largest ideal proton incident-rate estimates above 5.5 MeV are 358.920 Hz for the mean map and 975.659 Hz for the percentile-99 map. The calculation contains no aluminium shielding transport or calibrated detector response, and neither value is a 5–100 MeV accepted count rate or an electronics trigger-rate bound.

The corresponding electron >0.35 MeV ideal isotropic incident-rate maxima are **67,779.7 Hz** (mean) and **503,420 Hz** (percentile-99), under the same G=1 cm² sr, unit-efficiency and no-shield-transport assumptions. These indicate that electrons need explicit analysis, not that these numbers are accepted electron background. Silicon/scintillator deposition, thresholds, optical/electronic response, coincidence, saturation and classification determine actual background acceptance. Rejected events can still consume front-end capacity. No rejection factor, efficiency or dead time is inferred.

The summed percentile-column maximum **504,245 Hz** is a sum of species proxies at a common cell under the same idealizations, not a verified joint 99th-percentile event-rate prediction. The unsuffixed CSV maxima—proton 12,260.5 and electron 6,326,160—are flux×1 cm² proxies, not the rates for G=1 cm² sr. Avoid quoting those as directional telescope counts.

## Comparison with the prior conditional estimate

The earlier **PRELIMINARY ESTIMATE of 400 Hz peak proton count rate** assumed **protons only, 250 µm (0.25 mm) aluminium shielding, geometric factor 1 cm² sr and 100% detection efficiency**. It remains user-supplied with generating simulation, spectrum and calculation unidentified. The new **975.659 Hz** percentile-99 ideal isotropic proton maximum is about **2.439 times** that conditional estimate, a numerical difference of **575.659 Hz**. This is not a measured discrepancy between equivalent models: the new calculation has no shield transport, explicitly uses >5.5 MeV, and supplies a fixed-date percentile map, while the earlier estimate's integration limits/statistical case are unknown.

The mean-map ideal maximum of 358.920 Hz is closer numerically, but proximity does not prove it generated the earlier **400 Hz estimate under protons-only incidence, 250 µm (0.25 mm) aluminium, G=1 cm² sr and 100% efficiency**. Nor does changing G to the historical 0.314 cm² sr resolve provenance: that hypothetical rescaling would make the new percentile-99 maximum about 306.357 Hz, under still-unshielded isotropic assumptions. Do not tune G, efficiency or shielding until a number matches. Recover the original source or keep the two estimates separately labeled.

## Evidence disposition

| Evidence/value | Suitable provisional use | Not supported / needed next |
|---|---|---|
| Mean and percentile-99 flux/rate CSVs | Reproducible **2026** fixed-grid environmental arithmetic, with explicit units, thresholds and idealizations | Not 2029-calibrated, not measured response, not full-mission rate envelope |
| Proton maxima above | Provisional >5.5 MeV, isotropic, G=1 cm² sr, unit-efficiency incident-rate sizing scenarios | No aluminium response or 5–100 MeV acceptance |
| Electron maxima above | Explicit test-load scenarios and motivation to quantify electron response | Not detector-accepted background or proof of rejection capability |
| Sum of species percentile columns | Transparent arithmetic sensitivity scenario | No demonstrated joint percentile or all-particle trigger upper bound |
| ODS data region | Numeric copy of mean proton table | Do not use N7942 as whole-column maximum |
| AP-8/AE-8 peak PDFs | Separately identified historical model evidence | Do not mix with AP9/AE9 spectrum, threshold subtraction or percentile validation |
| 2028 AP-8/UP-MAX anisotropy data/plot | Evidence that directional assumptions require investigation | No validated AP9 correction, new-geometry acceptance or 2029 orbit alignment |

## Payload and 2029 compatibility

The latest payload specification is the dated **FPDU-2026-11-04 update to the Rev. 2.1 design narrative**, with five 6×6×14 mm main blocks plus a 6×6×2 mm front scintillator, unresolved assembly/channel geometry, retained silicon entrance and rear tag. Rev. 2.1's earlier single-block description and the old five-layer DITL response are not interchangeable with these blocks.

Environment flux tables are potentially reusable as **2026 source inputs** to a future geometry-qualified transport calculation. They contain no detector model to transfer or qualify. The supplied rate script can serve as a preserved idealized reference, but should not be wired into the current payload/grid/DITL simulator as a physical response. The independent audit checker adds validation without overwriting those simulators or the immutable payload input revision.

A corrected mission analysis must explicitly generate/record the **approved 2029 ephemeris or grid dates**, orbit, altitude, geographic mask, model/executable/database versions and complete mean/percentile/scenario settings. Changing a date label in the existing CSV does not regenerate the environment. The AP9/AE9 maps are statistical models, not measurements calibrated in a particular calendar year; even a proper 2029 run should be called “modeled for the 2029 configuration,” not “2029-calibrated.”

Request exact 5 and 100 MeV proton thresholds (or a sufficiently resolved differential spectrum) and enough energy/angle coverage for transport and trigger load outside the science band. Retain explicit statistical semantics for band-integrated and combined-species quantities. Obtain the original cell ephemeris/mask so omissions can be tested against an independent expected domain, not merely matching tables. All mission-specific rates, accepted-background estimates, science yield and timing capacity closure require that updated analysis plus a validated response.

## Can this establish an electronics upper bound?

**No credible upper bound on actual electronics trigger rate is established.** The files lack geometry-dependent acceptance, shielding/secondary production, all relevant species and energy ranges, trigger topology, channel multiplicity, noise/dark triggers, thresholds, coincidence behavior, buffering and measured busy time. A static percentile map is not a hard maximum; species marginal percentiles do not define their joint temporal distribution. The sampled region is incomplete as a mission envelope, with its highest electron rate on a domain boundary. A geometrical G and unit efficiency for two incident species do not bound every electrical trigger.

The present **20 ns coincidence-window input** and **tentative 20 ns dead-time suggestion** remain separate. This evidence does not validate either, establish a 40 ns total latency, prove a 50 MHz capacity, or select MCU versus FPGA. Capacity requires a timing budget and realistic sustained/burst event tests; no new values were fabricated.

## Pending decisions blocking further validation

Cross-reference the existing [payload open-decisions register](PAYLOAD_OPEN_DECISIONS.md):

1. **P-01–05: controlled CAD/ICD, material and optical/readout map.** Resolve block arrangement, front-piece position relative to Si, two coated faces and 0.11 mm interpretation, silicon/rear dimensions, SiPM channels and EJ-550 interfaces. These determine acceptance and response.
2. **P-06: environment/rate provenance.** Supply the original conditional-estimate calculation, original `grid_ephemeris.txt`/mask, executable/database hashes, full run configs/logs and approved 2029 environment prescription. Select whether the required statistic is a local percentile or a mission-duration confidence target.
3. **P-07–10: electronics definitions.** Resolve ASIC-to-ADC interval, channel/trigger architecture, ADC service interval versus latency, thresholds, busy/dead-time topology, jitter, buffering and loss criterion. Agree worst-case processing budget and engineering margin before MCU/FPGA selection.
4. **P-11: detector calibration and classification.** Define geometry-matched transport/optical/electronic validation, electron/proton response and energy migration. No arbitrary efficiency or rejection factor may close this gap.
5. **P-12–13: packets and measured power.** Needed after response/timing closure to connect counts to telemetry, storage and power; these files supply neither.

Recommended sequence: recover source manifests and freeze geometry/interfaces; generate a bounded approved-epoch environment/threshold test case; verify units/domain/spectrum; run response validation and mixed-field trigger studies; test timing/buffering with measured components; only then integrate revised yield/telemetry and revise MCR performance claims. The current ingestion is complete without launching an expensive mission-duration run.
