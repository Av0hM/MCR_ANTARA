# MCR feasibility gaps and PDR boundary

The revised Section 3 supports a conditional concept discussion, not unconditional mission feasibility or flight qualification. The requirements below state what must be established now; PDR performs implementation verification after allocations exist. Statuses are evidence dispositions, not readiness scores.

## Essential concept-level blockers

| Domain | Missing condition needed at concept level | Linked IDs | PDR verification after allocation |
|---|---|---|---|
| Science response and success | Geometry-matched5–100MeV response, energy-dependent acceptance/efficiency, qualified channels/background; eligible/core/independent-pass contracts; MSC channel wording | ANT-PLD-FR-001–004,007–009 | Transport/bench calibration, reconstruction cross-validation, shared-trigger livetime/overflow and end-to-end map evaluation |
| EPS sustainability | Common mission/RAAN/load/array baseline; battery/DoD reserve, peaks, recovery and EOL bounds | ANT-EPS-FR-001–006 | Electrical/transient/aging correlation and protective-state tests |
| ADCS acquisition/pointing | Accepted deployment envelope, pointing/jitter/settling allocations and wheel/MTQ authority relative to disturbance/inertia | ANT-ADCS-FR-001–005 | Source-matched censored Monte Carlo, coupled dynamics/power, actuator/HIL tests |
| Data production and memory | Verified sustained acquisition, outage/retention envelope, total FSW RAM/compute, linked metadata/time budgets | ANT-COM-FR-002–004; ANT-OBC-FR-003/004/007; ANT-INT-FR-002 | Full workload queue service, atomic media/power-cut/reset/retry tests |
| Ground availability/evidence | Actual runtime station/mask/RAAN; matched complete telemetry/events; received science and outage procedures | ANT-GSO-FR-001–004; ANT-COM-FR-003 | End-to-end station exercises, packet reconstruction and contact recovery |
| Thermal | Selected component operating/survival and battery/calibration limits; node mapping; common coupled hot/cold/eclipse scenarios | ANT-THM-FR-001–004 | Refined thermal/stress model correlation, heater/control and thermal-vacuum testing |
| Mechanical/SDM | Complete≤3kg mass/inertia/contingency; selected3U deployer ICD and applicable launch load envelope; packaged FPDU/deployable clearance/release concept | ANT-STR-FR-001–004; ANT-INT-FR-003 | FEA/modal/vibration/shock, CAD inspection and representative deployment/environment tests |
| Combined margins | A common run baseline and consistent source identities; do not pool incompatible epochs/masses/responses | ANT-SYS-FR-001 | Controlled integrated validation and traceable hardware interfaces |

Exact per-row concept-blocker flags are in the JSON register; the table groups interfaces that must also be tracked even where detailed testing can wait. Source-based values are not loosened to close any gap.

## Supported within limited scope

- ANT-COM-FR-001: full19.2kbps arithmetic on eligible Relay windows, not physical RF throughput.
- ANT-PLD-FR-010:292-byte reference format/codec, not current detector acquisition.
- ANT-OBC-FR-002:67452-byte bounded fixture queue, not sustained science or total OBC RAM sizing.
- ANT-INT-FR-001:documented coordinate convention, not alignment tolerance or as-built installation.

## Explicit not-met evidence and adverse scenarios

ANT-GSO-FR-003 is NOT MET by the supplied annual artifact group: telemetry stops at50days+20s without a terminal snapshot and the longer event exports disagree over the shared interval. This is a failed completeness/alignment acceptance condition; it is not proof that the spacecraft cannot operate for a year.

The128MiB storage candidate cannot retain the separate187498164-byte grid three-reading sensitivity without delivery. This adverse scenario is retained under conditional ANT-OBC-FR-003; it is not promoted to a binding all-mission no-downlink retention requirement. The historical detumble summary's32.266% reported convergence is not accepted as flight reliability or tested against an invented target. Missing supplier thermal limits cannot be declared either met or violated from the lumped temperatures.

## What can legitimately wait for PDR

Detailed RF link closure, frame/protocol losses and measured net throughput (ANT-COM-FR-005), atomic storage/power interruption implementation (ANT-OBC-FR-005), and end-to-end received-product testing (ANT-GSO-FR-002) are NOT EVALUATED. Their obligations are defined now. Component selection, tolerance measurement, qualification and environmental correlation can follow at PDR only after the concept-level feasible operating envelope/resource allocations have been established. No blanket deferral removes essential response, energy, pointing, thermal, mass or data-balance requirements.
