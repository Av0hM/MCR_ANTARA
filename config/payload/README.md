# Current FPDU baseline

`current.json` points to **FPDU-2026-11-04-approved-v2**, the unified user-approved input revision. Its exact schema freezes confirmed inputs and explicitly unknowns. [Appendix A.2](../../appendices/B_payload_detail_visual.tex) is the narrative specification; [baseline register](../../docs/audit/FPDU_APPROVED_BASELINE.md) provides traceability.

The earlier `fpdu_2026-11-04.json` and schema are preserved **superseded snapshots**. Their silicon/rear-detector, unresolved arrangement/coating and 20 ns coincidence/tentative dead-time descriptions do not control the current design. `scripts/validate_payload_config.py` defaults to the current pointer; an explicit historical file validates only as a labeled superseded snapshot. Current validation uses `scripts/fpdu_contracts.py` and its tests.

Current geometry: five 14×6×6 mm (X,Y,Z) main blocks in series, 2×6×6 mm front piece, inward travel −X from the +X-facing entrance, 11 SiPMs, main SiPM faces ±Y, Teflon 0.11 mm per ±Z face, coated Z 6.22 mm. EJ-550 coupling is confirmed; optical isolation, material and readout mapping are open. Silicon is removed; rear scintillator is optional/unselected.

ASIC shaping 20 ns; coincidence window planning references 200/250/300 ns; separately stated post-shaping delay 20 ns has unqualified meaning. ADC latency, digital latency, detector dead time and maximum trigger rate remain null. Null never means zero. No qualified detector response or old five-layer transfer is supplied.

The approved mission input is `config/mission/antara_2029.json`. The AP9/AE9 raw source epoch remains 2026-01-01 despite use as a 2029 planning reference. The rate script does not model the newly specified 250 µm front aluminium. No final encoding, packet size, data cadence or physical response is inferred from the 64-bin logical telemetry schema.
