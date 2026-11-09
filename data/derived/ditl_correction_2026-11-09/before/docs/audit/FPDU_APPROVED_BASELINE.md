# Approved FPDU and mission baseline

Current revision: `FPDU-2026-11-04-approved-v2`, selected by `config/payload/current.json`. Authority: latest unified user instruction, including clarification that 200/250/300 ns refer to coincidence windows. This is a versioned design-input contract, not a formal hardware Rev. 2.2 release or validated detector.

Evidence labels: **CONFIRMED DESIGN INPUT** (approved input), **PRELIMINARY ESTIMATE** (conditional assumption), **MODEL PREDICTION** (calculation), **VALIDATED RESULT** (only the tested scope), **OPEN DECISION** (unresolved). “Requires validation” is a condition, not evidence of successful validation.

| Item | Current authoritative input | Qualification |
|---|---|---|
| Mission | 3U, maximum 3 kg, 2029-01-01 UTC, ~600 km, 97.6°, e~0.001 | Configuration `config/mission/antara_2029.json`; no completed campaign implied |
| RAAN / EPS / ADCS | Launch-dependent; representative 0:30:180°; 25 Wh; reaction wheels + magnetorquers | Existing physics untouched |
| Science | Trapped-proton differential flux, 5–100 MeV; MMSC/MSC/EMSC thresholds retained | Independent observations, eligible/core cells and calibrated channels still need closure |
| Main blocks | Five, XYZ = 14 × 6 × 6 mm in longitudinal X series | 70 mm material length |
| Front | One, XYZ = 2 × 6 × 6 mm | Total 72 mm active material, excluding packaging |
| Direction | +X outward RAM boresight; particles enter +X face and travel −X | Matches existing body frame |
| Readout | Two SiPMs per main block, ±Y; one front SiPM | 11 sensors; ADC/channel mapping unknown |
| Reflector | Teflon on ±Z main faces, 0.11 mm **per face** | Coated Z 6.22 mm; no default X/Y coating |
| Coupling | EJ-550 grease | Thickness, area and material performance unknown |
| Silicon / rear | Silicon entrance removed; rear optional and unselected | Legacy topology not current |
| Shield | Entrance Al 250 µm = 0.25 mm | Transport unvalidated; not all-around housing |
| Optics/material | One material intended for all six, selection open; isolation open | No assumed cross-talk, light yield or separator |
| Timing | Shaping 20 ns; coincidence 200 ns; allowance ≥250 ns, preferred ~300 ns; post-shaping 20 ns | Post-shaping meaning open; dead time, ADC latency, processing latency and max trigger rate null |
| Data | 64 provisional bins; versioned 5–100 MeV reporting edges | Not 64 calibrated channels; no final bytes/cadence/encoding |

The earlier `fpdu_2026-11-04.json` and schema are immutable superseded snapshots. They retain now-rejected silicon/20 ns coincidence assumptions solely for historical reproduction. The validator CLI defaults to the current pointer; its retained historical API and an explicit old file validate only that superseded snapshot. Current code must use `scripts/fpdu_contracts.py:current_configuration()` and must not translate old response curves onto this design.

Operational objective ~five years, modeled decay to 300 km and physical reentry are three distinct endpoints. The new mission file is an explicit adapter contract; existing simulator defaults were not silently replaced. A runtime manifest must record applied overrides, actual environment backends, ephemeris/date coverage and output completion before claiming a qualified 2029 simulation.
