> **Current-baseline supersession (2026-11-04):** Use [FPDU_APPROVED_BASELINE.md](FPDU_APPROVED_BASELINE.md), [2029_AUDIT_RECONCILIATION.md](2029_AUDIT_RECONCILIATION.md) and [REMAINING_OPEN_DECISIONS.md](REMAINING_OPEN_DECISIONS.md). The record below is retained as historical audit evidence. Silicon is removed, rear detection optional, main blocks longitudinal along X, eleven SiPMs on ±Y/main plus front, Teflon 0.11 mm per ±Z face. Coincidence references are 200/250/300 ns, shaping 20 ns, qualified dead time unknown. Optical isolation remains open. Earlier 20 ns coincidence/dead-time guesses and unresolved coating-thickness interpretation are superseded.

# FPDU open decisions — 2026-11-04

Current narrative specification: [Appendix A.2](../../appendices/B_payload_detail_visual.tex). Machine inputs: [FPDU-2026-11-04](../../config/payload/fpdu_2026-11-04.json). This is an update to Rev. 2.1, not an invented formal Rev. 2.2 approval. Labels distinguish supplied design decisions from demonstrated performance.

The user follow-up states “20ns rn is the coincidence time right now, also the deadtime i guess”. Accordingly, **20 ns coincidence width is CONFIRMED DESIGN INPUT** as the current setting. **20 ns dead time is tentative and REQUIRES VALIDATION**. The qualified dead-time field stays null. The follow-up does not establish what the separately stated ASIC-to-ADC interval means, or authorize adding intervals together.

| ID / priority | Open decision and consequence | Required closure evidence / owner |
|---|---|---|
| P-01 / P0 | Arrangement and axes of five 6×6×14 mm blocks and one 6×6×2 mm front piece. Five blocks do not specify five stages. | Payload mechanical lead: controlled assembly CAD/ICD, coordinates, clearances, dimensions and revision; show front piece relative to active Si and rear detector. |
| P-02 / P0 | Relationship to Rev. 2.1's single block. One optical assembly may be possible but is unconfirmed. | Payload systems/optics leads: document assembly interpretation, optical isolation, surfaces and channel mapping. |
| P-03 / P0 | Teflon coats two sides per main block; 0.11 mm per face versus total and faces unknown. | Mechanical/optics drawing identifying faces, thickness convention, tolerances; do not infer packaged bounds. |
| P-04 / P0 | Scintillator material, surface finish, front-piece reflector treatment, SiPM count/location and EJ-550 geometry. | Materials and optics bill of materials plus optical bench measurements; grease thickness/transmission not supplied. |
| P-05 / P0 | Active Si thickness/area and rear detector geometry/readout; new front piece trigger role. | Updated detector ICD and transport sweep; retain both sensors and rear penetration information. |
| P-06 / P0 | Conditional rate provenance and its relation to trigger load. | Recover generating source/configuration, input spectrum, angular/energy integration, epoch, location/percentile and shielding geometry. |
| P-07 / P0 | What each 20 ns parameter measures. Current coincidence width, ASIC shaping, stated ASIC-to-ADC interval and tentative dead time are distinct. | Electronics timing diagram with edges, jitter/skew, acquisition/conversion/pipeline definitions; measure resolving time and busy behavior. |
| P-08 / P0 | MCU/FPGA selection and the available processing budget. A 20 ns coincidence width does not decide digital latency. | Candidate architecture, timestamp/trigger strategy, worst-case execution and measured timing margin. MCU preference requires budget comfortably >250 ns; FPGA if MCU constraints cannot be met. |
| P-09 / P0 | Shared vs per-channel dead time, all-particle load, sustained/burst capacity, buffers/event loss. | Injection campaign, busy/overflow/live-time counters, agreed loss limit; measure service interval separately from latency. |
| P-10 / P1 | ADC/ASIC/SiPM/processor models, ADC bits/rate and saturation behavior. | Selected datasheets and bench characterization; no performance values assigned now. |
| P-11 / P0 | 5–100 MeV response, purity/efficiency, angular acceptance and energy migration. | Geometry-matched transport, optical/electronics model, mixed-species response/confusion matrices and proton calibration scans. |
| P-12 / P1 | Histogram edges, overflow/underflow, physical energy resolution, packets/cadence and diagnostic data. | Firmware interface, count conservation tests and packet accounting. A 64-bin format does not establish 64 independent energy channels. |
| P-13 / P1 | Payload power and engineering margins. | Selected components, measured mode loads and thermal dependencies; preserve current spacecraft budgets as study assumptions pending separate review. |

P-06 concerns the **PRELIMINARY ESTIMATE of 400 Hz peak proton count rate under protons-only incidence, 250 µm (0.25 mm) aluminium shielding, assumed geometric factor 1 cm² sr and assumed 100% detection efficiency**. This is user-supplied, not a verified electronics limit or all-particle trigger rate. The estimate's energy integration bounds are unspecified; the separate mission measurement requirement remains 5–100 MeV.

## Recommended engineering sequence

1. Close P-01–05 with a controlled mechanical/optical/channel ICD. Create a new configuration revision for resolved values; do not mutate this input snapshot or rename old response files as compatible.
2. Recover P-06 provenance and separate incident spectra, accepted proton counts and all-particle triggers. Preserve all source/configuration hashes and integration units.
3. Close timing definitions P-07; prototype candidate processing paths and test P-08–10 with configurable margin and burst fixtures. Keep coincidence width and dead time independent even if measured values happen to agree.
4. Build the geometry-to-transport and optics/electronics response interfaces. Validate energy deposition, light output, noise, digitization, topology and stopping/penetrating reconstruction. Archive calibration and uncertainty; reject legacy L1–L5 mappings.
5. Close histogram/packet/power interfaces P-12–13. Run bounded science-yield integration against a qualified response before considering any mission-duration campaign.
6. Review evidence and update MCR performance claims only after the relevant verification gates pass. No full-year simulation is needed for this update.
