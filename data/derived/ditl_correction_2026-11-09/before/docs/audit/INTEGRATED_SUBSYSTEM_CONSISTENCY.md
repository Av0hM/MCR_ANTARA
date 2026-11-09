> **Scope update (user direction, 2026-11-09):** Exclude the short24h-named outputs from MCR operational evidence. Use only the `leop_1yr` group for operations, retaining its incomplete-telemetry and incompatible-event limitations. Thermal and detumble remain separate studies. One-hour calculations below are retained as an audit trail, not adopted comparison results.

# Integrated subsystem consistency

Approved baseline remains2029-01-01,~600km97.6°SSO,e≈.001,max3kg,25Wh planning,one fixed+Z/two deployables,reaction wheels+magnetorquers,current six-scintillator FPDU and~five-year operations. No scientific threshold or hardware selection changed.

| Comparison | Classification | Evidence / restriction |
|---|---|---|
| Two one-hour telemetry time and orbital-position arrays | DIRECTLY COMPARABLE | Identical0–3600s samples and lat/lon/alt arrays |
| LEOP as sole causal change | INSUFFICIENT EVIDENCE | No executed configs/attitudes/solver/seed; different startup/control trajectories |
| SOC presentation using25Wh planning capacity | COMPARABLE AFTER EXPLICIT NORMALIZATION | Wh extrema are recorded;25Wh capacity is declared reference, not proven run metadata |
| Annual event exports versus annual telemetry | INCOMPATIBLE CONFIGURATION / export association | Different horizons and substantial overlap discrepancies; exact cause unknown |
| Annual event epoch versus2029 | INCOMPATIBLE CONFIGURATION | Absolute event dates imply2000-03-01 |
| One-hour and thermal epochs versus2029 | INSUFFICIENT EVIDENCE | No absolute dates/configs; source2000 defaults do not establish run epoch |
| Orbit/mass/RAAN across DITL and thermal | INSUFFICIENT EVIDENCE | Candidate600km97.6°e.0013kg; Science currentRAAN30°,Thermal15°; actual runtime overrides unknown |
| Solar geometry and EPS | INSUFFICIENT EVIDENCE | Candidate Science lumped area.085m²/.193515 efficiency; thermal surface cells; no common deployed-panel/attitude config |
| DITL electrical loads versus thermal internal heat | SENSITIVITY STUDY ONLY | Thermal1.9–4.9W independent synthetic schedule, not same state-driven dissipated heat |
| Supplied detumble summary versus current source | INCOMPATIBLE CONFIGURATION | All trial accelerations nonzero; current implementation rejects them |
| Detumble torque/field/initial-attitude match to DITL | INSUFFICIENT EVIDENCE | Generating source, field, gains, initial attitude, seeds absent |
| Legacy payload versus approved FPDU | INCOMPATIBLE CONFIGURATION | Five-layer/efficiency/dead-time assumptions and no calibrated six-scintillator response |
| Ground station/link/data volumes | INSUFFICIENT EVIDENCE | Candidate Goa15° mask/19.2kbit/s; event/telemetry mismatch and MB/MiB convention |
| State-machine boundary semantics | INSUFFICIENT EVIDENCE | One-hour event/row labels differ2s; SAFE dwell differs from same-time event transitions |
| Complete24h/annual operations | INSUFFICIENT EVIDENCE | Complete1h outputs; incomplete50day telemetry; event span alone not completion |

No common unconditional power, thermal, ADCS or mission-success margin is calculated. Operational model facts remain useful for a conditional concept discussion; they do not qualify the current FPDU or prove annual steady-state operation.

MCR evidence blockers: obtain full-day pair and run manifests; reconcile annual exports and timestamps; identify thermal case and component limits; identify detumble generator/censoring and source mismatch. PDR tasks: close optics/materials/trigger, geometry-matched detector response and mixed-field throughput, actuator/field/timing qualification, thermal coupling/TVAC and structural tests, link/packet integrity, fixed eligibility/independent-pass contract. Long campaigns require separate authorization only after bounded checks and provenance closure.
