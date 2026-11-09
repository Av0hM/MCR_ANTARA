# Subsystem requirement traceability register

Source of truth: `config/requirements/section3_feasibility_v1.json`. Generated tables use the exact requirement text. S is not flight qualification. Existing Section 1 MM-M/MS-M/EM-M IDs remain authoritative; child rows are allocations, not new success tiers.

## ANT-EPS-FR-001 — CONDITIONAL

The EPS shall sustain the scheduled mission loads with the 25 Wh planning battery across representative launch-dependent RAAN and eclipse cases, without an accumulating energy deficit.

- **Parent requirement:** 2029 baseline; tier observation windows
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Energy / life
- **Interface / budget:** Energy / life
- **Existing evidence:** Corrected annual solar/load integrals are 50288.809/30866.103 Wh; runtime and EOL identity unresolved.
- **Evidence scope:** Corrected recorded-model accounting only; runtime configuration and hardware compliance unresolved
- **Verification method:** Analysis + test
- **Open decision:** Close a common mass/load/array/epoch baseline and minimum-energy trajectory for each required scenario.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Close a common mass/load/array/epoch baseline and minimum-energy trajectory for each required scenario.
- **PDR verification:** Close a common mass/load/array/epoch baseline and minimum-energy trajectory for each required scenario.
- **Sources:** `data/derived/ditl_correction_2026-11-09/leop_1yr_summary.json`, `docs/audit/CORRECTED_DITL_RUN_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-EPS-FR-002 — OPEN

The EPS shall keep battery energy within selected-cell operating and depth-of-discharge limits during startup, science, Relay and Safe Mode. Numerical SOC/DoD limits remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** Survival; continuous operations
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Battery safety
- **Interface / budget:** Battery safety
- **Existing evidence:** Corrected annual minimum 15.097556 Wh; actual capacity and supplier limits unknown.
- **Evidence scope:** Corrected recorded-model accounting only; runtime configuration and hardware compliance unresolved
- **Verification method:** Analysis + test
- **Open decision:** Allocate temperature-dependent cell limits, reserve and recovery thresholds; verify worst depletion, not mean SOC.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Allocate temperature-dependent cell limits, reserve and recovery thresholds; verify worst depletion, not mean SOC.
- **PDR verification:** Allocate temperature-dependent cell limits, reserve and recovery thresholds; verify worst depletion, not mean SOC.
- **Sources:** `data/derived/ditl_correction_2026-11-09/leop_1yr_summary.json`, `docs/audit/CORRECTED_DITL_RUN_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-EPS-FR-003 — OPEN

The EPS shall supply simultaneous and transient load demand within bus voltage, current and ripple allocations, including payload acquisition, radio transmit and actuator peaks. These limits remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** Payload / COMMS / ADCS availability
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Power interfaces
- **Interface / budget:** Power interfaces
- **Existing evidence:** Mode loads exist; qualified peaks and bus limits absent.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Freeze selected loads/inrush and rails; test transients, resets and brownout protection.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Freeze selected loads/inrush and rails; test transients, resets and brownout protection.
- **PDR verification:** Freeze selected loads/inrush and rails; test transients, resets and brownout protection.
- **Sources:** `appendices/E_budgets_and_bom_details.tex`
- **Concept-level blocker:** Yes

## ANT-EPS-FR-004 — CONDITIONAL

The EPS shall generate the allocated Sun-Pointing energy using the fixed +Z panel and two deployed panels, with illumination, pointing and conversion losses explicitly accounted for.

- **Parent requirement:** Approved panel concept; mission energy
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Array / ADCS
- **Interface / budget:** Array / ADCS
- **Existing evidence:** Configuration defined; generating and deployed-area identities differ.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Verify panel quantities, deployment state, angular response and coupled generation against the energy allocation.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Verify panel quantities, deployment state, angular response and coupled generation against the energy allocation.
- **Sources:** `docs/audit/INTEGRATED_SUBSYSTEM_CONSISTENCY.md`, `sections/05_feasibility_and_budgets.tex`, `appendices/M_updated_raan_drag_study.tex`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-EPS-FR-005 — OPEN

The EPS shall reserve energy for detumble, safe-state survival and recovery until the next usable generation opportunity; maximum recovery duration and energy reserve remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** LEOP; autonomous recovery
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Startup / safety
- **Interface / budget:** Startup / safety
- **Existing evidence:** One 2460 s detumble event; left-held load integral 1.528000 Wh; reserve not allocated.
- **Evidence scope:** Corrected recorded-model accounting only; runtime configuration and hardware compliance unresolved
- **Verification method:** Analysis + test
- **Open decision:** Bound initial state, eclipse, failed acquisition and recovery duration; demonstrate reserve and protective transitions.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Bound initial state, eclipse, failed acquisition and recovery duration; demonstrate reserve and protective transitions.
- **PDR verification:** Bound initial state, eclipse, failed acquisition and recovery duration; demonstrate reserve and protective transitions.
- **Sources:** `data/derived/ditl_correction_2026-11-09/leop_1yr_summary.json`, `docs/audit/CORRECTED_DITL_RUN_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-EPS-FR-006 — CONDITIONAL

The EPS shall maintain the mission energy allocation through the approximately five-year operations objective using traceable EOL degradation and cycling assumptions.

- **Parent requirement:** 2029 baseline operations objective
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** EOL / lifetime
- **Interface / budget:** EOL / lifetime
- **Existing evidence:** EOL study inputs exist; average generation is not an EOL margin.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Close degradation, thermal/cycle capacity and worst-case duty assumptions; correlate array/battery aging evidence.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Close degradation, thermal/cycle capacity and worst-case duty assumptions; correlate array/battery aging evidence.
- **PDR verification:** Close degradation, thermal/cycle capacity and worst-case duty assumptions; correlate array/battery aging evidence.
- **Sources:** `docs/audit/INTEGRATED_SUBSYSTEM_CONSISTENCY.md`, `sections/05_feasibility_and_budgets.tex`, `appendices/M_updated_raan_drag_study.tex`
- **Concept-level blocker:** Yes

## ANT-COM-FR-001 — SUPPORTED

The communications planning budget shall use 19200 bit/s (2400 bytes/s), 100% science allocation and no arbitrary derating during eligible visibility-intersect-Relay windows.

- **Parent requirement:** Approved communications planning baseline
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** MCR link budget
- **Interface / budget:** MCR link budget
- **Existing evidence:** Corrected annual Relay opportunity 428836800 bytes; full-rate arithmetic reproduced.
- **Evidence scope:** Corrected recorded-model accounting only; runtime configuration and hardware compliance unresolved
- **Verification method:** Analysis
- **Open decision:** Verify device configuration and net throughput at PDR; do not relabel ideal capacity as measured delivery.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Verify device configuration and net throughput at PDR; do not relabel ideal capacity as measured delivery.
- **Sources:** `data/derived/ditl_correction_2026-11-09/leop_1yr_summary.json`, `docs/audit/CORRECTED_DITL_RUN_VALIDATION.md`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-COM-FR-002 — CONDITIONAL

The communications schedule shall return the generated science workload within the accepted retention/outage envelope, with bounded backlog and no unaccounted science loss. The sustained workload/envelope remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** Science delivery; all tiers
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Data balance
- **Interface / budget:** Data balance
- **Existing evidence:** Corrected annual EMSC slot sensitivity:46637364 bytes; nominal peak75336 bytes; response/timing open.
- **Evidence scope:** Corrected recorded-model accounting only; runtime configuration and hardware compliance unresolved
- **Verification method:** Analysis + test
- **Open decision:** Obtain matched acquisition/contact traces; include command/housekeeping and verified application throughput before closure.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Obtain matched acquisition/contact traces; include command/housekeeping and verified application throughput before closure.
- **PDR verification:** Obtain matched acquisition/contact traces; include command/housekeeping and verified application throughput before closure.
- **Sources:** `data/derived/ditl_correction_2026-11-09/leop_1yr_summary.json`, `docs/audit/CORRECTED_DITL_RUN_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-COM-FR-003 — OPEN

The communications interface shall support BITS Goa with a traceable station, frequency/modem and elevation-mask configuration; capacity shall use the producing mask exactly once.

- **Parent requirement:** Approved primary station; relay operations
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Ground interface
- **Interface / budget:** Ground interface
- **Existing evidence:** Historical station label GS1_India; actual mask/RAAN unverified.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Recover runtime station/mask and demonstrate end-to-end modem/radio compatibility; no unsupported 10/15-degree conversion.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Recover runtime station/mask and demonstrate end-to-end modem/radio compatibility; no unsupported 10/15-degree conversion.
- **PDR verification:** Recover runtime station/mask and demonstrate end-to-end modem/radio compatibility; no unsupported 10/15-degree conversion.
- **Sources:** `docs/audit/GS_19K2_LINK_CLOSURE.md`, `docs/audit/GS_PASS_CAPACITY_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-COM-FR-004 — OPEN

The communications protocol shall detect corrupted or missing records and resume interrupted transfers with identifiable sequence, acknowledgement and duplicate handling.

- **Parent requirement:** Usable received science products
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Transfer integrity
- **Interface / budget:** Transfer integrity
- **Existing evidence:** v3 CRC/sequence tested; packet reception and retry protocol absent.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Test contact interruptions, loss, duplicate packets, resumption and retained unacknowledged records.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Test contact interruptions, loss, duplicate packets, resumption and retained unacknowledged records.
- **Sources:** `docs/audit/GS_19K2_LINK_CLOSURE.md`, `docs/audit/GS_PASS_CAPACITY_VALIDATION.md`, `docs/audit/SCIENCE_RECORD_V3.md`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-COM-FR-005 — NOT EVALUATED

The communications design shall close RF link and net science-throughput budgets for the selected hardware and operational geometry before claiming physical data-return compliance.

- **Parent requirement:** Radio-to-ground interface
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** PDR RF closure
- **Interface / budget:** PDR RF closure
- **Existing evidence:** No qualified link margin or application throughput.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + hardware test
- **Open decision:** Verify bitrate, coding, EIRP/gain, pointing/polarization/path losses, sensitivity/EbN0, overhead, retransmissions and net throughput.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Verify bitrate, coding, EIRP/gain, pointing/polarization/path losses, sensitivity/EbN0, overhead, retransmissions and net throughput.
- **Sources:** `docs/audit/GS_19K2_LINK_CLOSURE.md`, `docs/audit/GS_PASS_CAPACITY_VALIDATION.md`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-PLD-FR-001 — OPEN

The payload shall provide calibrated differential trapped-proton flux over 5–100 MeV, with energy-dependent response, background discrimination and uncertainty adequate for the approved tier products.

- **Parent requirement:** Primary flight objective; MM-M-03; MS-M-03; EM-M-05
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Proton science
- **Interface / budget:** Proton science
- **Existing evidence:** No calibrated six-scintillator response; 5.4/5.5 MeV study cutoffs do not close 5 MeV.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Validate geometry/material/transport, classified proton response and reconstructed energy against independent calibration data.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Validate geometry/material/transport, classified proton response and reconstructed energy against independent calibration data.
- **PDR verification:** Validate geometry/material/transport, classified proton response and reconstructed energy against independent calibration data.
- **Sources:** `docs/audit/FPDU_RESPONSE_VALIDATION_PLAN.md`, `appendices/B_payload_detail_visual.tex`
- **Concept-level blocker:** Yes

## ANT-PLD-FR-002 — OPEN

The payload science chain shall enable a 5°×5° MMSC map: at least 70% polygon coverage, 90% core coverage, 3 independent passes/cell, at least 2 channels and fractional flux uncertainty ≤50% per populated cell/channel.

- **Parent requirement:** MM-M-01 through MM-M-05
- **Tier relevance:** MMSC
- **Mission driver:** MMSC
- **Interface / budget:** MMSC
- **Existing evidence:** 92 geometric cells; eligible/core and independent-pass definitions unresolved.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Accept core/eligibility/independence and calibrated uncertainty contract; evaluate delivered cell/channel aggregates, not individual records.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Accept core/eligibility/independence and calibrated uncertainty contract; evaluate delivered cell/channel aggregates, not individual records.
- **PDR verification:** Accept core/eligibility/independence and calibrated uncertainty contract; evaluate delivered cell/channel aggregates, not individual records.
- **Sources:** `sections/01_mission_context.tex`, `docs/audit/SAA_POLYGON_AND_COVERAGE_CONTRACT.md`
- **Concept-level blocker:** Yes

## ANT-PLD-FR-003 — OPEN

The payload science chain shall enable the MSC 1°×1° atlas: at least 90% detectable-cell coverage, 5 independent passes/cell, uncertainty ≤25% in the two lowest operational channels, all operational channels, and monthly maps with >3σ changes flagged.

- **Parent requirement:** MS-M-01 through MS-M-05; tier comparison table
- **Tier relevance:** MSC
- **Mission driver:** MSC
- **Interface / budget:** MSC
- **Existing evidence:** Detailed criteria say all operational channels; summary specifies ≥4. Both retained pending reconciliation.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Resolve channel-count wording without weakening either source; validate common grids, temporal maps and full uncertainty.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Resolve channel-count wording without weakening either source; validate common grids, temporal maps and full uncertainty.
- **PDR verification:** Resolve channel-count wording without weakening either source; validate common grids, temporal maps and full uncertainty.
- **Sources:** `sections/01_mission_context.tex`, `docs/audit/SAA_POLYGON_AND_COVERAGE_CONTRACT.md`
- **Concept-level blocker:** Yes

## ANT-PLD-FR-004 — OPEN

The payload science chain shall enable 0.5°×0.5° EMSC products: ≥95% of cells above AP9 1%-of-mission-peak eligibility, 5 independent passes/cell, ≥3 channels, ≤10% uncertainty in one channel and ≤15% in every other operational channel.

- **Parent requirement:** EM-M-01 through EM-M-06
- **Tier relevance:** EMSC
- **Mission driver:** EMSC
- **Interface / budget:** EMSC
- **Existing evidence:** Primary-map ≤15% rule and two 9–10 month submaps remain binding; required-G percentiles are not compliance.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Evaluate full-window and sub-period products with a fixed eligible set and calibrated channel covariance; retain primary-map rule.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Evaluate full-window and sub-period products with a fixed eligible set and calibrated channel covariance; retain primary-map rule.
- **PDR verification:** Evaluate full-window and sub-period products with a fixed eligible set and calibrated channel covariance; retain primary-map rule.
- **Sources:** `sections/01_mission_context.tex`, `docs/audit/GEOMETRIC_FACTOR_SCIENCE_ELIGIBILITY.md`
- **Concept-level blocker:** Yes

## ANT-PLD-FR-005 — CONDITIONAL

The payload mechanical/readout interface shall conform to five longitudinal 6×6×14 mm blocks, a 6×6×2 mm front element and eleven SiPMs, with no silicon entrance stage.

- **Parent requirement:** Current geometry/interface baseline
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Approved FPDU
- **Interface / budget:** Approved FPDU
- **Existing evidence:** Geometry arithmetic/configuration checked; package/material/optics unselected.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Inspection + test
- **Open decision:** Inspect CAD/ICD and assembled geometry; resolve material, isolation, clearances and optional rear detector.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Inspect CAD/ICD and assembled geometry; resolve material, isolation, clearances and optional rear detector.
- **Sources:** `config/payload/fpdu_2026-11-04-approved-v2.json`, `docs/audit/FPDU_GEOMETRY_VALIDATION.md`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-PLD-FR-006 — CONDITIONAL

The payload timing interface shall distinguish 20 ns ASIC shaping from the 200 ns coincidence target and ≥250 ns allowance (about 300 ns preferred); it shall not assign these values as detector dead time.

- **Parent requirement:** Approved electronics planning inputs
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Timing / readout
- **Interface / budget:** Timing / readout
- **Existing evidence:** Separate config fields; qualified latency/dead time remain unknown.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Measure shaping, coincidence resolution/jitter, additional20 ns delay, ADC/service latency and livetime independently.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Measure shaping, coincidence resolution/jitter, additional20 ns delay, ADC/service latency and livetime independently.
- **Sources:** `docs/audit/FPDU_ELECTRONICS_TIMING_TRADE.md`, `config/payload/fpdu_2026-11-04-approved-v2.json`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-PLD-FR-007 — OPEN

The payload readout shall handle the declared mixed-species peak/burst trigger envelope without unflagged saturation, pileup, loss or counter overflow. Rate, loss and dead-time allocations remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** Science quality; electronics capacity
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** All-particle throughput
- **Interface / budget:** All-particle throughput
- **Existing evidence:** Proton-only400 Hz is not a bound; electron incident proxies can dominate.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Derive transport/threshold/acceptance-trigger envelope; test shared-trigger dead time, burst buffers and overflow at selected hardware limits.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Derive transport/threshold/acceptance-trigger envelope; test shared-trigger dead time, burst buffers and overflow at selected hardware limits.
- **PDR verification:** Derive transport/threshold/acceptance-trigger envelope; test shared-trigger dead time, burst buffers and overflow at selected hardware limits.
- **Sources:** `docs/audit/FPDU_COUNT_RATE_RECONCILIATION.md`, `docs/audit/FPDU_ELECTRONICS_TIMING_TRADE.md`
- **Concept-level blocker:** Yes

## ANT-PLD-FR-008 — OPEN

The payload response allocation shall provide energy-dependent effective geometric factor and livetime sufficient for tier exposure/precision, including background and reconstruction uncertainty. Required acceptance values remain conditional on verified exposure.

- **Parent requirement:** MM-M-04; MS-M-02; EM-M-03
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Acceptance / counts
- **Interface / budget:** Acceptance / counts
- **Existing evidence:** Broad-band G95≈0.36–0.50 cm² sr at10% is ideal counting arithmetic, not achieved G.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Close exposure provenance, transport-and-trigger acceptance, reconstruction/background covariance and response calibration; do not tune G to force success.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Close exposure provenance, transport-and-trigger acceptance, reconstruction/background covariance and response calibration; do not tune G to force success.
- **PDR verification:** Close exposure provenance, transport-and-trigger acceptance, reconstruction/background covariance and response calibration; do not tune G to force success.
- **Sources:** `docs/audit/GEOMETRIC_FACTOR_PHYSICAL_INTERPRETATION.md`, `docs/audit/GEOMETRIC_FACTOR_NUMERICAL_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-PLD-FR-009 — CONDITIONAL

The payload science accounting shall conserve counts across acquisition time and effective energy-bin boundaries, retain valid zero-count exposure, and carry livetime, background and calibration identity into accumulated cell/channel uncertainty.

- **Parent requirement:** MM-M-03/04; MS-M-02/03; EM-M-03/05
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Scientific integrity
- **Interface / budget:** Scientific integrity
- **Existing evidence:** Reference conservation tests pass; legacy expected counts are not reconstructed events.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Validate bin merging/unfolding, exposure and loss metadata end-to-end; apply precision to aggregates, not each record.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Validate bin merging/unfolding, exposure and loss metadata end-to-end; apply precision to aggregates, not each record.
- **Sources:** `scripts/fpdu_contracts.py`, `docs/audit/SCIENCE_DITL_EVIDENCE_VALIDATION.md`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-PLD-FR-010 — SUPPORTED

The payload reference science format shall define entry/exit timestamps, latitude/longitude/altitude, 64 provisional uint32 bins, sequence, 16-bit mode/health marker and CRC in 292 bytes excluding radio framing.

- **Parent requirement:** Approved science record contract
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Telemetry v3
- **Interface / budget:** Telemetry v3
- **Existing evidence:** Codec/schema and CRC/count tests support the logical interface.
- **Evidence scope:** Supported reference format/codec only
- **Verification method:** Inspection + software test
- **Open decision:** Qualify acquisition-to-record integration and linked metadata; logical format support does not verify detector or RF performance.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Qualify acquisition-to-record integration and linked metadata; logical format support does not verify detector or RF performance.
- **Sources:** `config/science/science_record_v3.json`, `tests/test_science_record_v3.py`, `docs/audit/SCIENCE_RECORD_V3.md`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-PLD-FR-011 — CONDITIONAL

The payload scheduler shall prefer 3 readings per eligible visit, seek 2 when feasible and retain 1 when necessary, with nonoverlapping valid intervals, correct cell assignment and conserved counts/exposure; no arbitrary minimum duration or count is imposed.

- **Parent requirement:** Approved acquisition clarification; tier independence
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Reading policy
- **Interface / budget:** Reading policy
- **Existing evidence:** Reference partitions tested; exact crossings and hardware boundaries unknown.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Verify timer/readout continuity and counter handoff at cell/mode/shutdown boundaries; preserve zero-count records and do not count subdivisions as independent passes.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Verify timer/readout continuity and counter handoff at cell/mode/shutdown boundaries; preserve zero-count records and do not count subdivisions as independent passes.
- **Sources:** `docs/audit/SCIENCE_RECORD_V3.md`, `docs/audit/TIER_RECORD_GENERATION.md`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-ADCS-FR-001 — OPEN

The ADCS shall detumble and acquire a safe Sun-Pointing state from the accepted deployment attitude/rate envelope within the EPS startup allocation; envelope, deadline and reliability target remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** LEOP; EPS reserve
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Startup acquisition
- **Interface / budget:** Startup acquisition
- **Existing evidence:** One 2460 s event; historical 16133/50000 successes are source-incompatible.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Approve initial-condition/timeout envelope; reproduce censored trials with verified field, dynamics and controller; demonstrate coupled startup energy.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Approve initial-condition/timeout envelope; reproduce censored trials with verified field, dynamics and controller; demonstrate coupled startup energy.
- **PDR verification:** Approve initial-condition/timeout envelope; reproduce censored trials with verified field, dynamics and controller; demonstrate coupled startup energy.
- **Sources:** `docs/audit/DETUMBLE_EVIDENCE_VALIDATION.md`, `docs/audit/SCIENCE_DITL_EVIDENCE_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-ADCS-FR-002 — OPEN

The ADCS shall maintain payload +X science and +Y Relay boresights within allocated acceptance/link pointing-error envelopes during valid acquisition/transfer. Numeric error and jitter allocations remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** Effective G; RF gain; valid exposure
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Science / Relay pointing
- **Interface / budget:** Science / Relay pointing
- **Existing evidence:** No geometry-matched acceptance or selected-antenna error allocation.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Derive knowledge/control/jitter tolerances from acceptance and antenna patterns; measure closed-loop errors during operation.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Derive knowledge/control/jitter tolerances from acceptance and antenna patterns; measure closed-loop errors during operation.
- **PDR verification:** Derive knowledge/control/jitter tolerances from acceptance and antenna patterns; measure closed-loop errors during operation.
- **Sources:** `docs/audit/DETUMBLE_EVIDENCE_VALIDATION.md`, `docs/audit/SCIENCE_DITL_EVIDENCE_VALIDATION.md`, `appendices/F_orbit_rf_support.tex`
- **Concept-level blocker:** Yes

## ANT-ADCS-FR-003 — OPEN

The ADCS shall hold Sun Pointing and perform recovery/Safe Mode attitudes within the EPS generation and thermal allocations. Numeric attitude limits remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** EPS generation; thermal survival
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Survival pointing
- **Interface / budget:** Survival pointing
- **Existing evidence:** Mode concept defined; common pointing-energy/thermal limits not closed.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Close loss-of-Sun/eclipsed recovery and sensor failure cases with traceable power/thermal limits.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Close loss-of-Sun/eclipsed recovery and sensor failure cases with traceable power/thermal limits.
- **Sources:** `docs/audit/DETUMBLE_EVIDENCE_VALIDATION.md`, `docs/audit/SCIENCE_DITL_EVIDENCE_VALIDATION.md`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-ADCS-FR-004 — OPEN

The ADCS shall complete and settle science/Relay slews before their qualified windows and keep transition overhead within the mission exposure/data-return allocation. Deadline and settling limits remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** Tier exposure; Relay opportunities
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Slew timing
- **Interface / budget:** Slew timing
- **Existing evidence:** Complete day/year timestamp spans; telemetry/transition/slew duration definitions disagree.
- **Evidence scope:** Corrected recorded-model accounting only; runtime configuration and hardware compliance unresolved
- **Verification method:** Analysis + test
- **Open decision:** Reconcile interval/event identity; validate moving targets, slew/settle timing and mode guards under worst initial states.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Reconcile interval/event identity; validate moving targets, slew/settle timing and mode guards under worst initial states.
- **PDR verification:** Reconcile interval/event identity; validate moving targets, slew/settle timing and mode guards under worst initial states.
- **Sources:** `data/derived/ditl_correction_2026-11-09/leop_1yr_summary.json`, `docs/audit/CORRECTED_DITL_RUN_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-ADCS-FR-005 — OPEN

The ADCS shall keep wheel momentum and torque within selected actuator limits and unload using magnetorquers against the declared disturbance envelope. Numerical authority/margin allocations remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** Reaction-wheel + magnetorquer concept
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Actuator authority
- **Interface / budget:** Actuator authority
- **Existing evidence:** Hardware/field coupling unqualified; zero archived wheel momentum is not proof.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Select actuators and inertia; validate disturbance rejection, saturation, orbital-field authority and power across representative orientations.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Select actuators and inertia; validate disturbance rejection, saturation, orbital-field authority and power across representative orientations.
- **PDR verification:** Select actuators and inertia; validate disturbance rejection, saturation, orbital-field authority and power across representative orientations.
- **Sources:** `docs/audit/DETUMBLE_EVIDENCE_VALIDATION.md`, `docs/audit/SCIENCE_DITL_EVIDENCE_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-ADCS-FR-006 — CONDITIONAL

The ADCS shall report acquisition, saturation and pointing faults to the mode controller and enforce safe guards before declaring science/Relay readiness.

- **Parent requirement:** A.1 safety and transition logic
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Mode reliability
- **Interface / budget:** Mode reliability
- **Existing evidence:** FSM exists; historical boundary/SAFE timing discrepancies remain.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Simulation + hardware-in-loop
- **Open decision:** Fault-inject stale sensors, failed slews and saturation; verify guards, recovery and time-consistent readiness without chatter.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Fault-inject stale sensors, failed slews and saturation; verify guards, recovery and time-consistent readiness without chatter.
- **Sources:** `docs/audit/DETUMBLE_EVIDENCE_VALIDATION.md`, `docs/audit/SCIENCE_DITL_EVIDENCE_VALIDATION.md`, `appendices/A_operational_logic_visual.tex`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-OBC-FR-001 — CONDITIONAL

The OBC shall allocate record assembly separately from the science queue: 292 bytes per packed reference record and explicitly budgeted acquisition banks, stack and DMA; a two-bank histogram fixture adds 512 bytes.

- **Parent requirement:** Telemetry v3 interface
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Assembly RAM
- **Interface / budget:** Assembly RAM
- **Existing evidence:** 804-byte illustrative payload working set; not total RAM or selected architecture.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Verify memory map, concurrency, acquisition latency and high-water marks for actual firmware.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Verify memory map, concurrency, acquisition latency and high-water marks for actual firmware.
- **Sources:** `docs/audit/OBC_RAM_FLASH_SIZING.md`, `docs/audit/STORAGE_BACKLOG_VALIDATION.md`, `docs/audit/SCIENCE_RECORD_V3.md`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-OBC-FR-002 — CONDITIONAL

The OBC science queue shall retain the corrected nominal workload without loss and provide nonvolatile spill for the accepted outage envelope; science RAM, persistent retention and total system memory shall be allocated separately.

- **Parent requirement:** Bounded v3 workload; all-tier storage
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Queue RAM
- **Interface / budget:** Queue RAM
- **Existing evidence:** Corrected annual nominal EMSC peak75336 bytes; seven-day outage1010028 bytes exceeds256KiB RAM.
- **Evidence scope:** Corrected recorded-model accounting only; runtime configuration and hardware compliance unresolved
- **Verification method:** Analysis + software test
- **Open decision:** Accepted outage envelope, spill policy, reserves and actual production
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Establish sustained peak/burst envelope and queue metadata overhead; candidate RAM is not a minimum hardware capacity.
- **Sources:** `data/derived/ditl_correction_2026-11-09/leop_1yr_summary.json`, `docs/audit/CORRECTED_DITL_RUN_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-OBC-FR-003 — CONDITIONAL

The OBC persistent science store shall retain all unacknowledged records through the accepted contact-outage/retention envelope, including metadata/reserves; that envelope remains an OPEN DERIVED REQUIREMENT.

- **Parent requirement:** Science delivery; outage recovery
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Persistent storage
- **Interface / budget:** Persistent storage
- **Existing evidence:** Corrected annual seven-day EMSC outage peak1010028 bytes;128MiB exceeds it before reserves.
- **Evidence scope:** Corrected recorded-model accounting only; runtime configuration and hardware compliance unresolved
- **Verification method:** Analysis + test
- **Open decision:** Set retention/outage workload and reserves; validate media endurance, recovery and full-buffer policy without silent data loss.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Set retention/outage workload and reserves; validate media endurance, recovery and full-buffer policy without silent data loss.
- **PDR verification:** Set retention/outage workload and reserves; validate media endurance, recovery and full-buffer policy without silent data loss.
- **Sources:** `data/derived/ditl_correction_2026-11-09/leop_1yr_summary.json`, `docs/audit/CORRECTED_DITL_RUN_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-OBC-FR-004 — OPEN

The OBC shall provision total FSW/system memory and execution capacity separately from record assembly, queue and persistent storage, covering control, reconstruction, commands and fault handling. Limits remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** Concurrent subsystem operation
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** System RAM / compute
- **Interface / budget:** System RAM / compute
- **Existing evidence:** No integrated worst-case memory/execution budget.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Measure stack/heap/DMA/RTOS high-water marks and worst-case service times under combined acquisition and fault load.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Measure stack/heap/DMA/RTOS high-water marks and worst-case service times under combined acquisition and fault load.
- **PDR verification:** Measure stack/heap/DMA/RTOS high-water marks and worst-case service times under combined acquisition and fault load.
- **Sources:** `docs/audit/OBC_RAM_FLASH_SIZING.md`, `docs/audit/STORAGE_BACKLOG_VALIDATION.md`, `docs/audit/SCIENCE_RECORD_V3.md`
- **Concept-level blocker:** Yes

## ANT-OBC-FR-005 — NOT EVALUATED

The OBC shall maintain record integrity and sequence continuity across interrupted writes, reset and Relay interruption, recovering only complete records and retaining unacknowledged data.

- **Parent requirement:** Usable science; ANT-COM-FR-004 interface
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Data persistence
- **Interface / budget:** Data persistence
- **Existing evidence:** Reference CRC passes; atomic media writes and acknowledgements not implemented.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Power-cut and reset tests; recover journal/CRC tails, reboot/sequence epochs, retransmission and duplicate handling.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Power-cut and reset tests; recover journal/CRC tails, reboot/sequence epochs, retransmission and duplicate handling.
- **Sources:** `docs/audit/OBC_RAM_FLASH_SIZING.md`, `docs/audit/STORAGE_BACKLOG_VALIDATION.md`, `docs/audit/SCIENCE_RECORD_V3.md`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-OBC-FR-006 — CONDITIONAL

The OBC shall execute approved state-machine guards, validate commands, report faults and enter a defined safe state without uncommanded detector/Relay operation.

- **Parent requirement:** A.1 FSM; system safety
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Control / fault management
- **Interface / budget:** Control / fault management
- **Existing evidence:** Mode logic documented; flight integration and command integrity unqualified.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Verify command authorization/integrity, watchdogs, fault priorities and startup/recovery transitions by fault injection.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Verify command authorization/integrity, watchdogs, fault priorities and startup/recovery transitions by fault injection.
- **Sources:** `appendices/A_operational_logic_visual.tex`, `docs/audit/SCIENCE_DITL_EVIDENCE_VALIDATION.md`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-OBC-FR-007 — OPEN

The OBC shall preserve payload timestamps, cell/configuration identity and linked livetime/background/quality metadata through storage and ground reconstruction, without treating unknown health as nominal.

- **Parent requirement:** Record validity; calibrated maps
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Metadata / time
- **Interface / budget:** Metadata / time
- **Existing evidence:** v3 has linked-session metadata; size/cadence and clock performance open.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Budget metadata and clock/position correlation; validate missing/stale identity, epoch wrapping and ground reconstruction.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Budget metadata and clock/position correlation; validate missing/stale identity, epoch wrapping and ground reconstruction.
- **PDR verification:** Budget metadata and clock/position correlation; validate missing/stale identity, epoch wrapping and ground reconstruction.
- **Sources:** `docs/audit/OBC_RAM_FLASH_SIZING.md`, `docs/audit/STORAGE_BACKLOG_VALIDATION.md`, `docs/audit/SCIENCE_RECORD_V3.md`
- **Concept-level blocker:** Yes

## ANT-INT-FR-001 — SUPPORTED

The subsystem interface definitions shall preserve +X payload entrance with inward −X particle travel, ±Y main SiPMs, ±Z reflector faces, +Y relay boresight and +Z fixed-array orientation.

- **Parent requirement:** Approved mechanical/pointing interfaces
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Body-frame ICD
- **Interface / budget:** Body-frame ICD
- **Existing evidence:** Current config/diagrams agree; installation must be inspected.
- **Evidence scope:** Supported documented frame convention only
- **Verification method:** Inspection + software test
- **Open decision:** Survey integrated axes and coordinate transforms; do not infer alignment accuracy from convention.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Survey integrated axes and coordinate transforms; do not infer alignment accuracy from convention.
- **Sources:** `config/payload/fpdu_2026-11-04-approved-v2.json`, `docs/audit/FPDU_GEOMETRY_VALIDATION.md`, `sections/03_spacecraft_architecture.tex`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-INT-FR-002 — OPEN

The navigation/time interface shall bound clock and position errors so each science interval is unambiguously assigned to its cell/exposure window. Numerical errors and synchronization allocations remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** All tier grids; v3 UTC contract
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Spatial / temporal tags
- **Interface / budget:** Spatial / temporal tags
- **Existing evidence:** Integer scaling and POSIX convention defined; actual accuracy unknown.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Allocate timing/navigation errors including crossing interpolation and leap-second handling; verify end-to-end time correlation.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Allocate timing/navigation errors including crossing interpolation and leap-second handling; verify end-to-end time correlation.
- **PDR verification:** Allocate timing/navigation errors including crossing interpolation and leap-second handling; verify end-to-end time correlation.
- **Sources:** `docs/audit/SCIENCE_RECORD_V3.md`, `docs/audit/SAA_POLYGON_AND_COVERAGE_CONTRACT.md`
- **Concept-level blocker:** Yes

## ANT-INT-FR-003 — OPEN

The integration ICD shall allocate power, harness/connector, data, thermal and safe-state interfaces with explicit ownership and compatible command/status semantics.

- **Parent requirement:** System integration; failure containment
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Subsystem interoperability
- **Interface / budget:** Subsystem interoperability
- **Existing evidence:** No closed common hardware/ICD baseline.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Inspect pinouts, routing, grounding, resets and environmental compatibility; demonstrate interoperable safe states.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Inspect pinouts, routing, grounding, resets and environmental compatibility; demonstrate interoperable safe states.
- **PDR verification:** Inspect pinouts, routing, grounding, resets and environmental compatibility; demonstrate interoperable safe states.
- **Sources:** `docs/audit/REMAINING_OPEN_DECISIONS.md`, `docs/audit/INTEGRATED_SUBSYSTEM_CONSISTENCY.md`
- **Concept-level blocker:** Yes

## ANT-THM-FR-001 — OPEN

The thermal subsystem shall keep each selected component within traceable operating and survival temperature limits for nominal and Safe Mode cases; numerical limits/node mapping remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** Science availability; bus safety
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Component survival
- **Interface / budget:** Component survival
- **Existing evidence:** One history: internal −14.061 to21.159°C; no component compliance limits.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Obtain selected-part limits and map nodes/components before claiming even preliminary thermal compliance; correlate refined model.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Obtain selected-part limits and map nodes/components before claiming even preliminary thermal compliance; correlate refined model.
- **PDR verification:** Obtain selected-part limits and map nodes/components before claiming even preliminary thermal compliance; correlate refined model.
- **Sources:** `docs/audit/THERMAL_EVIDENCE_VALIDATION.md`, `appendices/D_thermal_structural_details.tex`
- **Concept-level blocker:** Yes

## ANT-THM-FR-002 — CONDITIONAL

The thermal assessment shall bound hot, cold and eclipse temperatures using mission-compatible attitude and mode-dependent internal heat loads, including startup, science, Relay and safe recovery.

- **Parent requirement:** EPS / ADCS / payload operating scenarios
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Thermal cases
- **Interface / budget:** Thermal cases
- **Existing evidence:** Supplied extrema are one history; 1.9–4.9 W schedule is independent of DITL.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Establish coupled case envelopes/initial conditions and numerical convergence; execute bounded model checks then thermal-vacuum correlation.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Establish coupled case envelopes/initial conditions and numerical convergence; execute bounded model checks then thermal-vacuum correlation.
- **PDR verification:** Establish coupled case envelopes/initial conditions and numerical convergence; execute bounded model checks then thermal-vacuum correlation.
- **Sources:** `docs/audit/THERMAL_EVIDENCE_VALIDATION.md`, `appendices/D_thermal_structural_details.tex`
- **Concept-level blocker:** Yes

## ANT-THM-FR-003 — OPEN

The thermal interfaces shall allocate battery charge/discharge temperature constraints and payload temperature-dependent calibration/stability limits. Both numerical allocations remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** EPS safety; calibrated proton flux
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Battery / calibration
- **Interface / budget:** Battery / calibration
- **Existing evidence:** No selected-part limits or payload thermal response characterization.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Measure/obtain battery and detector limits; assign heater/control and calibration compensation before closing feasibility.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Measure/obtain battery and detector limits; assign heater/control and calibration compensation before closing feasibility.
- **PDR verification:** Measure/obtain battery and detector limits; assign heater/control and calibration compensation before closing feasibility.
- **Sources:** `docs/audit/THERMAL_EVIDENCE_VALIDATION.md`, `appendices/D_thermal_structural_details.tex`
- **Concept-level blocker:** Yes

## ANT-THM-FR-004 — OPEN

The thermal-mechanical design shall keep gradients and resulting distortions/stresses within allocated alignment and material limits; numerical limits remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** Payload/antenna alignment; structure
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Thermal gradients
- **Interface / budget:** Thermal gradients
- **Existing evidence:** 31.704°C face spread is a node difference, not structural stress.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Couple thermal fields to material/assembly stress and alignment models; correlate interface temperatures.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Couple thermal fields to material/assembly stress and alignment models; correlate interface temperatures.
- **Sources:** `docs/audit/THERMAL_EVIDENCE_VALIDATION.md`, `appendices/D_thermal_structural_details.tex`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-STR-FR-001 — OPEN

The structure/integration budget shall fit the selected 3 U deployer envelope and keep the complete design mass, including all allocations and contingency, at or below 3.0 kg.

- **Parent requirement:** Approved 3 U and3 kg baseline
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Envelope / mass
- **Interface / budget:** Envelope / mass
- **Existing evidence:** 1536.3 g is incomplete BOM; provider ICD, payload and deployment allocations open.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Close full mass/inertia/CAD budget and contingency, then measure assembly against selected deployer interface; generic dimensions are not acceptance limits.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Close full mass/inertia/CAD budget and contingency, then measure assembly against selected deployer interface; generic dimensions are not acceptance limits.
- **PDR verification:** Close full mass/inertia/CAD budget and contingency, then measure assembly against selected deployer interface; generic dimensions are not acceptance limits.
- **Sources:** `appendices/D_thermal_structural_details.tex`, `sections/05_feasibility_and_budgets.tex`, `config/mission/antara_2029.json`
- **Concept-level blocker:** Yes

## ANT-STR-FR-002 — OPEN

The structure shall withstand applicable launch loads and meet provider modal, vibration and shock requirements without loss of function or interface integrity. Numerical load/frequency limits remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** Commissioning; mechanical ICD
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Launch survival
- **Interface / budget:** Launch survival
- **Existing evidence:** No provider load envelope, FEA/modal or qualification evidence.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Obtain provider requirements at concept closure; complete FEA, modal correlation and approved vibration/shock qualification plan.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Obtain provider requirements at concept closure; complete FEA, modal correlation and approved vibration/shock qualification plan.
- **PDR verification:** Obtain provider requirements at concept closure; complete FEA, modal correlation and approved vibration/shock qualification plan.
- **Sources:** `appendices/D_thermal_structural_details.tex`, `sections/05_feasibility_and_budgets.tex`, `config/mission/antara_2029.json`
- **Concept-level blocker:** Yes

## ANT-STR-FR-003 — OPEN

The solar deployment/retention mechanism shall retain both panels safely through launch and release/verify deployment without collision, harness damage or loss of the required generation geometry.

- **Parent requirement:** Approved one-fixed/two-deployable array
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** SDM / deployables
- **Interface / budget:** SDM / deployables
- **Existing evidence:** Architecture stated; mechanism, clearances and retention life unverified.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Allocate release power, loads, clearance, harness/connector routing, safe inhibit and retention duration; inspect CAD and test representative deployment.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Allocate release power, loads, clearance, harness/connector routing, safe inhibit and retention duration; inspect CAD and test representative deployment.
- **PDR verification:** Allocate release power, loads, clearance, harness/connector routing, safe inhibit and retention duration; inspect CAD and test representative deployment.
- **Sources:** `appendices/D_thermal_structural_details.tex`, `sections/05_feasibility_and_budgets.tex`, `config/mission/antara_2029.json`
- **Concept-level blocker:** Yes

## ANT-STR-FR-004 — CONDITIONAL

The mechanical integration shall preserve FPDU optical/readout interfaces and body-frame clearances through assembly, thermal cycling and operational life.

- **Parent requirement:** FPDU geometry; integration safety
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Payload packaging
- **Interface / budget:** Payload packaging
- **Existing evidence:** Active material dimensions exclude coating, gaps, sensors and housing.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Close packaged CAD, tolerance/harness stack and materials compatibility; verify fit and environmental stability without changing active geometry.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Close packaged CAD, tolerance/harness stack and materials compatibility; verify fit and environmental stability without changing active geometry.
- **Sources:** `appendices/D_thermal_structural_details.tex`, `sections/05_feasibility_and_budgets.tex`, `config/mission/antara_2029.json`, `config/payload/fpdu_2026-11-04-approved-v2.json`, `docs/audit/FPDU_GEOMETRY_VALIDATION.md`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-GSO-FR-001 — OPEN

The ground/operations chain shall plan and verify the approved observation windows: MMSC4–6 months and≥150 operational received passes; MSC12–14 months and≥900 operational passes; EMSC18–20 months and≥2400 operational passes.

- **Parent requirement:** Section1 tier duration tables; MM/MS/EM science requirements
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Tier duration / passes
- **Interface / budget:** Tier duration / passes
- **Existing evidence:** Corrected annual timestamp span complete; legacy response and source configuration not qualified.
- **Evidence scope:** Corrected recorded-model accounting only; runtime configuration and hardware compliance unresolved
- **Verification method:** Analysis + test
- **Open decision:** Demonstrate qualified exposure and delivery within tier windows; retain orbital/SAA targets as planning context, not independent observations.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Demonstrate qualified exposure and delivery within tier windows; retain orbital/SAA targets as planning context, not independent observations.
- **PDR verification:** Demonstrate qualified exposure and delivery within tier windows; retain orbital/SAA targets as planning context, not independent observations.
- **Sources:** `data/derived/ditl_correction_2026-11-09/leop_1yr_summary.json`, `docs/audit/CORRECTED_DITL_RUN_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-GSO-FR-002 — NOT EVALUATED

Ground science processing shall reconstruct versioned cell/channel products from received records and linked exposure/calibration metadata, retaining zero counts, excluded-data reasons and independent-passage identifiers.

- **Parent requirement:** MM-M-03/05; MS-M-03/05; EM-M-05/06
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Map reconstruction
- **Interface / budget:** Map reconstruction
- **Existing evidence:** No received current-FPDU archive; reference codec is only a starting interface.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Round-trip representative calibrated records, missed/duplicate packets, per-channel errors and temporal maps against an independent evaluator.
- **MCR closure:** Retain the stated interface obligation and evidence scope at MCR; detailed implementation verification may proceed at PDR.
- **PDR verification:** Round-trip representative calibrated records, missed/duplicate packets, per-channel errors and temporal maps against an independent evaluator.
- **Sources:** `docs/audit/GS_PASS_CAPACITY_VALIDATION.md`, `docs/audit/TIER_RECORD_GENERATION.md`, `docs/audit/SCIENCE_DITL_EVIDENCE_VALIDATION.md`, `docs/audit/SCIENCE_RECORD_V3.md`
- **Concept-level blocker:** No; retain scope/interface obligation

## ANT-GSO-FR-003 — CONDITIONAL

Operations verification shall use complete, time-aligned telemetry, contact and transfer records for every claimed mission-window data-return result.

- **Parent requirement:** MCR data-return feasibility
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** Evidence integrity
- **Interface / budget:** Evidence integrity
- **Existing evidence:** Corrected telemetry spans365days; contact/native data totals reconcile; mode/slew semantics unresolved.
- **Evidence scope:** Corrected recorded-model accounting only; runtime configuration and hardware compliance unresolved
- **Verification method:** Inspection + analysis
- **Open decision:** Producing source revision, runtime manifest and transition/slew logger semantics
- **MCR closure:** Reconcile logger/control meanings and bind completed timestamp span to runtime configuration.
- **PDR verification:** Reconcile source identities and completion/terminal records before claiming annual closure. This status applies to supplied evidence, not proven spacecraft inability.
- **Sources:** `data/derived/ditl_correction_2026-11-09/leop_1yr_summary.json`, `docs/audit/CORRECTED_DITL_RUN_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-GSO-FR-004 — OPEN

Ground operations shall establish primary-station availability and a missed-contact recovery schedule that maintains the accepted science retention envelope, including command/fault response. Availability and outage limits remain OPEN DERIVED REQUIREMENTS.

- **Parent requirement:** BITS Goa; ANT-COM-FR-002; ANT-OBC-FR-003
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** GS availability
- **Interface / budget:** GS availability
- **Existing evidence:** Corrected longest intercontact gap48458s; actual station outage commitment unknown.
- **Evidence scope:** Corrected recorded-model accounting only; runtime configuration and hardware compliance unresolved
- **Verification method:** Analysis + test
- **Open decision:** Set staffing/modem availability, contact exceptions, recovery/acknowledgement procedures and outage acceptance; test end-to-end exercises.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Set staffing/modem availability, contact exceptions, recovery/acknowledgement procedures and outage acceptance; test end-to-end exercises.
- **PDR verification:** Set staffing/modem availability, contact exceptions, recovery/acknowledgement procedures and outage acceptance; test end-to-end exercises.
- **Sources:** `data/derived/ditl_correction_2026-11-09/leop_1yr_summary.json`, `docs/audit/CORRECTED_DITL_RUN_VALIDATION.md`
- **Concept-level blocker:** Yes

## ANT-SYS-FR-001 — CONDITIONAL

The system feasibility assessment shall identify a common mass, epoch, orbit/RAAN, duty-cycle, response and resource baseline for each combined margin and disclose incompatible evidence rather than pool it.

- **Parent requirement:** 2029 baseline; all subsystem budgets
- **Tier relevance:** MMSC / MSC / EMSC
- **Mission driver:** MCR integration
- **Interface / budget:** MCR integration
- **Existing evidence:** Existing studies differ in epoch/mass/response and completion.
- **Evidence scope:** Flight condition not yet qualified
- **Verification method:** Analysis + test
- **Open decision:** Close concept-level allocations and source identities before claiming integrated margins; qualify hardware/physical models at PDR.
- **MCR closure:** Establish the stated allocation/evidence before an unconditional concept-feasibility conclusion. Close concept-level allocations and source identities before claiming integrated margins; qualify hardware/physical models at PDR.
- **PDR verification:** Close concept-level allocations and source identities before claiming integrated margins; qualify hardware/physical models at PDR.
- **Sources:** `docs/audit/INTEGRATED_SUBSYSTEM_CONSISTENCY.md`, `config/mission/antara_2029.json`
- **Concept-level blocker:** Yes
