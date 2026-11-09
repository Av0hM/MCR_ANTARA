# Remaining decisions and PDR work

## Decisions that block physical validation

1. **Material and optics:** select scintillator material; choose isolated/partial/common coupling only after light collection, cross-talk, localization and calibration comparison. Specify inter-block surfaces/gaps, front reflector/SiPM face and grease coupling area/thickness.
2. **Controlled CAD/ICD:** provide current six-scintillator assembly, tolerances, housing, entrance shield and channel interfaces. The approved dimensions/axes/per-face coating and eleven SiPM count need no further clarification.
3. **Acquisition architecture:** define post-shaping 20 ns meaning; choose trigger topology, coincidence definition, sensor/ASIC/ADC mapping and candidate components. Measure timestamp precision, ADC/processing latency, shared/per-channel dead time, burst loss and throughput. The 200/250/300 ns values concern coincidence windows; they do not decide MCU feasibility.
4. **Rear detector:** optional and unselected. Decide only from transport/classification evidence; silicon entrance is already removed.
5. **Response/reconstruction:** qualify geometry-matched acceptance, 5–100 MeV response, front observable, mixed-species rejection and response-matrix versus trained-model approach. Electron-rich rate proxies cannot be removed from capacity studies without evidence.
6. **Science contract:** approve independent-observation, flux-eligible/core-cell and uncertainty/temporal definitions without weakening committed tier thresholds.
7. **Data engineering:** select histogram encoding, cadence, diagnostics, buffering and downlink handling; 64 bins is the provisional format, not resolution or packet-size closure.

## Implementation and evidence constraints

- Authoritative simulator sibling is read-only in this session. The tested accounting patch is delivered but unapplied. Source issues remain partially resolved until it is reviewed/applied with its source hashes and surrounding tests.
- Current mission/configuration is explicit but no automatic legacy-response adapter is installed. Required interfaces deliberately reject unqualified responses.
- Team-approved RAAN and 2026 radiation maps are usable preliminary 2029 references. A reproducible 2029 runtime/environment/ephemeris manifest remains necessary for a physically epoch-matched claim; no full run is authorized or performed.
- Tier-disposition generation code/manifests and complete annual output remain missing. Historical count-derived success claims are withdrawn.

Prioritized sequence: apply/retest accounting patch in the authoritative workspace; integrate tested visit/checkpoint/telemetry contracts there with migration policy; resolve optics/CAD and acquisition interfaces; validate response and mixed-field timing; approve science eligibility/independence; run bounded coupled cases and timestep/restart checks; only then request authorization for long campaigns and update feasibility percentages from traceable products.


## Safe simulator integration follow-up

Production integration was rechecked and stopped at the access gate. Both source hashes still match the delivered patch prerequisites at base `51933bb902288de095f362546c73b006fe702882`; read-only `git apply --check` succeeds. The authoritative source and `.git` remain outside this session's writable roots. No branch/worktree was created, patch applied, unrelated change moved, or regression suite rerun. This is an environment-access prerequisite, not a new hardware/scientific approval request.

See [integration preflight](SIMULATOR_PATCH_INTEGRATION.md) for patch checksum, dirty-source details and safe isolation procedure, and [regression disposition](SIMULATOR_REGRESSION_RESULTS.md) for historical versus deferred tests. Resume in a session with write access to the authoritative repository and its Git metadata; preserve the reviewed dirty prerequisites separately from the accounting patch. Visit/checkpoint production integration remains a separate outstanding task even after this patch applies. Next response work is bounded geometry/path-length verification, followed by material-specific transport once CAD/material decisions close.

## Geometric-factor follow-up (2026-11-06)

1. **Evidence retrieval, not a hardware decision:** obtain the executed dwell source/config/checkpoint/completion manifest, elapsed duration, sampled RAAN and any pooling/scaling. The table matches an `18-Month Simulation` archive member, but nearby source defaults to three days. No mission-duration multiplier is authorized by this evidence.
2. Obtain raw 65-threshold IRENE output, mean/percentile semantics, model/database version, ephemeris/epoch/altitude and generating conversion. Current candidate source requests only two thresholds and G=0.314; supplied rates prove G=1. Do not relabel these as 2029-generated.
3. **Hardware/physics decisions:** select material, mechanical gaps/optical isolation, front interfaces and trigger/containment topology. Determine whether front+any-block, stopping-depth-dependent or all-through coincidence is intended. A collimator remains hypothetical. Do not adopt EJ-200 or full-stack coincidence from the study.
4. Compare source CSDA to aluminium PSTAR around 5–7 MeV, then transport through actual 250 µm entrance Al. The optional approximation gives 5.95 MeV, distinct from study5.4/planning5.5; no validated threshold selected. Preserve committed5–100 MeV requirement and evaluate low-energy accessibility.
5. Approve fixed science eligibility/core/mission-peak definitions, independent observations and joint calibrated-channel/temporal acceptance contract. Per-bin 1%-peak sets differ and cannot substitute for mission-tier denominators.
6. Next bounded experiment: analytical two-plane versus gap-free ray fixture agreement (initial on/off-axis and quadrature tests now pass), followed by geometry/material/trigger-specific angular transport with deposition and side-exit scoring. Qualify effective G, electron backgrounds, shared livetime and reconstruction using physical evidence before coupling to verified orbit exposure. No annual campaign needed for this stage.

Software accounting reproduction is complete for this supplied study. Detector performance, absolute science yield, electronics ceiling and MMSC/MSC/EMSC success remain unqualified. Existing external simulator integration and grid-visit/checkpoint tasks remain separate and open.

## Simulation evidence gates — 2026-11-09

**MCR evidence blockers:** obtain actual full24h LEOP and No-LEOP telemetry/events plus executed manifests; supplied files cover only1h. Reconcile annual telemetry/event export identities and overlapping-window discrepancies before annual performance claims. Resolve2s mode/event labels, MB/MiB serialization/link conventions, and boundary-flush byte metadata. Identify thermal case/epoch/initial-state timestamp convention and applicable selected-component limits; summary hot/cold columns are one history's extrema. Recover historical detumble source, seeds, input distribution and censor/failure records; all supplied trials use nonzero initial accelerations rejected by current source.

**PDR work:** geometry-matched FPDU transport/response, optical/material and trigger interfaces, mixed-field throughput/dead time, actuator/magnetic-field/timestep validation, independent-channel/visit requirements, component-correlated thermal model and TVAC, structural/environmental verification, RF packet receipt and losses. Keep reaction wheels+magnetorquers and the approved six-scintillator baseline; no hardware decision was made here.

The revised MCR is suitable for a conditional concept discussion with these evidence gates recorded, not unconditional feasibility closure, a completed annual demonstration or science-tier acceptance. No expensive rerun is authorized by this evidence ingestion.

**Subsequent scope decision:** the user excluded the short24h-named outputs and selected only `leop_1yr` for operational MCR evidence. Obtaining the full-day pair is no longer a prerequisite for this requested annual-only review. Matched annual source/configuration, complete telemetry and consistent event accounting remain blockers to annual performance claims. Thermal/detumble gates remain unchanged.


## Telemetry v3 / memory / communications closure — 2026-11-09

Confirmed for MCR:292-byte reference,64uint32bins,entry/exit tags,combined16-bit status,full19.2kbps/2400bytes/s with100%science allocation during eligible Relay; no arbitrary derating. No arbitrary minimum acquisition duration or individual-record precision threshold. Preserve valid zero-count records. These supersede conflicting earlier tentative record/rate policy notes.

MCR evidence limits: obtain actual grid-study elapsed horizon/scaling/RAAN; reconcile annual event/telemetry identities; identify runtime station/elevation mask; obtain current acquisition windows and true cell crossings. Until then, cross-study data balance and sustained storage sufficiency are conditional. Do not relabel historical contact dates as2029.

PDR: qualify timer resolution/readout latency and continuous counter handoff to realize3/2/1 nonoverlapping readings; retain all exposure across shutdown fragments. Define calibration/livetime/background metadata cadence and storage. Verify uint32 overflow and evaluate uint16/compression on real integer detector records; no ratio assumed. Select actual OBC memory after RTOS/reconstruction/DMA budgets, flash reserves/endurance/radiation and power-loss tests; define retention/acknowledgement policy.128MiB is a candidate rolling queue;16GB is an archival trade, not a requirement.

PDR communications: AX100-supported bitrate/configuration, modulation/coding, RF budget/EIRP/gains/losses/sensitivity/EbN0/margin, framing/FEC/overhead, retransmission/loss, modem compatibility, measured net application throughput and housekeeping/command allocations. No invented link margin or arbitrary MCR discount.


## Section 3 requirement closure — 2026-11-09

Use `SUBSYSTEM_REQUIREMENT_TRACEABILITY.md` as the per-ID allocation/verification register and `MCR_FEASIBILITY_GAPS.md` for concept blockers. Thirty-two of51rows flag missing concept-level evidence/allocations; this is not a count of hardware failures. Required owner reconciliation: MSC all-operational channels versus Section1 summary≥4; eligible flux/core and statistical independence; effective response/trigger envelope; battery reserve/DoD and bus limits; pointing/acquisition/control authority; selected-component thermal limits and coupled cases; complete mass/provider mechanical loads; sustained production/outage/FSW memory; station/mask/source completeness. These cannot all be deferred as PDR hardware testing. No threshold or mission ID has been weakened.

PDR verification remains explicit for RF/protocol/net throughput, calibration/response, actuator/HIL, media power-loss integrity, received-product reconstruction, thermal correlation and structural/deployment qualification after concept allocations are justified. GSO-003 is NOT MET by the supplied annual evidence group; obtain consistent completed records before an annual data-return claim. No new long-duration simulation is authorized by this requirements update.
