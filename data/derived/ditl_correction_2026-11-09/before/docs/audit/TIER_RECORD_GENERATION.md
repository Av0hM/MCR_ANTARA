# Tier record-generation analysis

Reproduction: `scripts/validate_telemetry_budget.py`, `scripts/complete_telemetry_budget.py`; derived artifacts and SHA-256 source inventory under `data/derived/telemetry_v3_2026-11-09/`. Original inputs preserved. No simulation campaign or external simulator modification. Arithmetic validation is not instrument qualification.

## Unmatched grid-study sensitivity

7940 unique aligned 0.5-degree cells sum to 214039 visits and 1453556 s geometric dwell. The file matches an archive labelled 18 months, but its actual horizon/epoch/RAAN/completion/scaling are unknown. Do not normalize by 3 days, 18 months, a year or the sum of dwell. Aggregated fine-cell pass counts cannot reconstruct coarse continuous visits without chronology.

| readings | records | bytes | MiB | ideal_required_relay_seconds |
|---|---|---|---|---|
| 1 | 214039 | 62499388 | 59.604061126708984 | 26041.411666666667 |
| 2 | 428078 | 124998776 | 119.20812225341797 | 52082.823333333334 |
| 3 | 642117 | 187498164 | 178.81218338012695 | 78124.235 |

These assume a valid record for every geometric visit and are not science-enabled production. No intrinsic particle rate is changed by tier selection.

## Partial telemetry diagnostic, separate evidence identity

1,861,462 contiguous sampled intervals span 50 days +20 s. Its epoch is unknown; conflicting absolute event exports are not used to timestamp it. Gate conditions use the recorded science-generation flag, which is checked against Detection and in-SAA. Cells use global edges anchored at latitude −90/longitude −180, wrapping longitude; each sample owns its interval. Exact crossings between samples are unobserved, so this is sampled-cell attribution, not qualified geographical record validity. The current FPDU response is not simulated.

| tier | geometric_visits | science_enabled_visits | acquisition_segments | preferred_readings_per_visit | records | bytes | mean_bytes_per_elapsed_day | max_calendar_day_bytes | max_one_second_records |
|---|---|---|---|---|---|---|---|---|---|
| MMSC | 2191 | 19 | 41 | 1 | 41 | 11972 | 239.4388914866135 | 11972 | 1 |
| MMSC | 2191 | 19 | 41 | 2 | 46 | 13432 | 268.63875630205416 | 13432 | 1 |
| MMSC | 2191 | 19 | 41 | 3 | 57 | 16644 | 332.87845889602363 | 16644 | 1 |
| MSC | 9822 | 58 | 58 | 1 | 58 | 16936 | 338.7184318591118 | 16936 | 1 |
| MSC | 9822 | 58 | 58 | 2 | 116 | 33872 | 677.4368637182235 | 33872 | 1 |
| MSC | 9822 | 58 | 58 | 3 | 174 | 50808 | 1016.1552955773353 | 50808 | 2 |
| EMSC | 18951 | 77 | 77 | 1 | 77 | 22484 | 449.67791815778634 | 22484 | 1 |
| EMSC | 18951 | 77 | 77 | 2 | 154 | 44968 | 899.3558363155727 | 44968 | 1 |
| EMSC | 18951 | 77 | 77 | 3 | 231 | 67452 | 1349.033754473359 | 67452 | 2 |

All cases preserve 342 s gated exposure. At MMSC, 19 geometric visits have 41 continuous acquisition fragments; a single record cannot truthfully bridge their off intervals. Thus the target-one sensitivity still needs 41 records; target-two needs 46, preferred-three 57. MSC/EMSC have one segment per sampled visit. Equal subdivisions are ideal possible boundaries, not demonstrated hardware cadence. Event times to subdivide actual counts are absent; only record slots/volumes are computed. No fake histogram records are emitted.

Mean uses the actual partial elapsed horizon; maximum is the observed calendar-day sum. All gated production occurs early, so a low 50-day average is not steady-state evidence. Peak one-second releases (not inferred from a mean) are 2 records/s for preferred MSC/EMSC and 1 for MMSC. There is no demonstrated physical peak production limit. The adaptive policy converges to the three-reading sensitivity only if its boundaries are realizable; otherwise one/two cases bracket it subject to fragmentation. Final adaptive rate remains unqualified.

