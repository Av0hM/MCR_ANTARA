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
