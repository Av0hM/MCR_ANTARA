# DITL CORRECTION IMPACT MATRIX — corrected evidence 2026-11-09

Corrected source registry: `evidence/science-ditl/run_registry.json`. Recompute with `scripts/validate_corrected_ditl.py`; source hashes/headers are in `inventory.json`, numerical summaries and ledgers in `data/derived/ditl_correction_2026-11-09/`. Prior DITL conclusions are superseded, not silently retained.

| Scenario/metric | Superseded | Corrected | Change |
|---|---:|---:|---:|
| leop_24h/duration_s | 3,600 | 86,400 | 82,800 |
| leop_24h/saa_s | 0 | 2,696 | 2,696 |
| leop_24h/acquisition_gate_s | 0 | 758 | 758 |
| leop_24h/battery_min_wh | 15.209 | 15.128 | -0.081 |
| leop_24h/generated_wh | 0 | 145.575 | 145.575 |
| leop_24h/consumed_wh | 2.791 | 85.167 | 82.376 |
| leop_24h/generated_source_mb | 0 | 0.009 | 0.009 |
| leop_24h/transferred_source_mb | 0 | 0.009 | 0.009 |
| leop_24h/storage_max_source_mb | 10 | 10.005 | 0.005 |
| leop_24h/contact_s | 0 | 766 | 766 |
| leop_24h/mode_seconds:DETUMBLE | 2,460 | 2,460 | 0 |
| leop_24h/mode_seconds:RELAY | 0 | 894 | 894 |
| leop_24h/mode_seconds:COLD_AND_DARK | 122 | 122 | 0 |
| leop_24h/mode_seconds:SLEWING | 64 | 980 | 916 |
| leop_24h/mode_seconds:DETECTION | 0 | 2,676 | 2,676 |
| leop_24h/mode_seconds:SAFE | 2 | 0 | -2 |
| leop_24h/mode_seconds:SUN_POINTING | 952 | 79,268 | 78,316 |
| no_leop_24h/duration_s | 3,600 | 86,400 | 82,800 |
| no_leop_24h/saa_s | 0 | 2,696 | 2,696 |
| no_leop_24h/acquisition_gate_s | 0 | 758 | 758 |
| no_leop_24h/battery_min_wh | 18.004 | 18.004 | 0 |
| no_leop_24h/generated_wh | 4.962 | 150.403 | 145.441 |
| no_leop_24h/consumed_wh | 3.391 | 85.719 | 82.328 |
| no_leop_24h/generated_source_mb | 0 | 0.009 | 0.009 |
| no_leop_24h/transferred_source_mb | 0 | 0.009 | 0.009 |
| no_leop_24h/storage_max_source_mb | 10 | 10.005 | 0.005 |
| no_leop_24h/contact_s | 0 | 766 | 766 |
| no_leop_24h/mode_seconds:DETUMBLE | 0 | 0 | 0 |
| no_leop_24h/mode_seconds:RELAY | 0 | 894 | 894 |
| no_leop_24h/mode_seconds:COLD_AND_DARK | 0 | 0 | 0 |
| no_leop_24h/mode_seconds:SLEWING | 0 | 980 | 980 |
| no_leop_24h/mode_seconds:DETECTION | 0 | 2,674 | 2,674 |
| no_leop_24h/mode_seconds:SAFE | 0 | 0 | 0 |
| no_leop_24h/mode_seconds:SUN_POINTING | 3,600 | 81,852 | 78,252 |
| leop_1yr/duration_s | 4,320,020 | 31,536,000 | 27,215,980 |
| leop_1yr/saa_s | 130,664 | 881,882 | 751,218 |
| leop_1yr/acquisition_gate_s | 342 | 247,258 | 246,916 |
| leop_1yr/battery_min_wh | 15.215 | 15.098 | -0.118 |
| leop_1yr/generated_wh | 10,808.465 | 50,288.809 | 39,480.344 |
| leop_1yr/consumed_wh | 8,847.621 | 30,866.103 | 22,018.481 |
| leop_1yr/generated_source_mb | 0.005 | 3.514 | 3.509 |
| leop_1yr/transferred_source_mb | 0.005 | 3.514 | 3.509 |
| leop_1yr/storage_max_source_mb | 10.005 | 10.006 | 0.001 |
| leop_1yr/contact_s | 36,754 | 244,016 | 207,262 |
| leop_1yr/mode_seconds:DETUMBLE | 2,460 | 2,460 | 0 |
| leop_1yr/mode_seconds:RELAY | 33,022 | 269,876 | 236,854 |
| leop_1yr/mode_seconds:COLD_AND_DARK | 122 | 122 | 0 |
| leop_1yr/mode_seconds:SLEWING | 3,616,666 | 375,688 | -3,240,978 |
| leop_1yr/mode_seconds:DETECTION | 1,296 | 894,054 | 892,758 |
| leop_1yr/mode_seconds:SAFE | 14 | 332,882 | 332,868 |
| leop_1yr/mode_seconds:SUN_POINTING | 666,440 | 29,660,918 | 28,994,478 |

The complete machine-readable OLD INPUT → OLD RESULT → MCR LOCATION → CORRECTED RUN → NEW RESULT map is `claim_migration.json`; initial file/line references are in `initial_dependency_inventory.json`. Independent studies are unchanged unless explicitly cited as dependencies. Prior PDFs are immutable snapshots, not active authority.

## Additional data-budget and requirements migration

| Metric | Superseded | Corrected | Change |
|---|---:|---:|---:|
| contact_count | 820 | 820 | 0 |
| visibility_capacity_bytes | 585638400 | 585638400 | 0 |
| relay_capacity_bytes | 428836800 | 428836800 | 0 |
| EMSC_v3_generated_bytes | 67452 | 46637364 | 46569912 |
| EMSC_v3_peak_bytes | 67452 | 75336 | 7884 |
| minimum_battery_pct_planning25Wh | 60.8608 | 60.390222222222256 | -0.47057777777774135 |

All seven annual event CSVs are byte-identical between old and corrected folders; annual telemetry differs. Corrected authority therefore reproduces contact totals while replacing their previously incompatible telemetry context. Exact per-requirement changes and figure mapping: `requirement_changes.json`, `figure_supersession.json`. The old record/queue calculations are invalidated; the292-byte codec, zero-count validity, geometry/radiation/grid arithmetic and independent thermal/detumble/RAAN evidence remain unchanged.
