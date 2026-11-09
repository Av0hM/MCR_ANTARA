# Ground-station contact validation

Reproduction: `scripts/validate_telemetry_budget.py`, `scripts/complete_telemetry_budget.py`; derived artifacts and SHA-256 source inventory under `data/derived/telemetry_v3_2026-11-09/`. Original inputs preserved. No simulation campaign or external simulator modification. Arithmetic validation is not instrument qualification.

820 unique, nonoverlapping contact intervals have valid absolute AOS/LOS timestamps and durations matching elapsed times. Every absolute-minus-elapsed timestamp implies **2000-03-01 UTC**. Station labels are `GS1_India`; current candidate defaults are Goa 15°N,74°E,70m,15° mask, RAAN30°, but no generating manifest proves those defaults for these exports. BITS Goa is the approved planning station. This is not verified 2029 availability, and the runtime mask must remain UNKNOWN (candidate 15°), not relabelled a proven 10°/15° study. No mask penalty is reapplied.

| Statistic | Reproduced value |
|---|---:|
| Contact count | 820 |
| Total visibility duration | 244016 s |
| Mean per 365-day accounting window | 668.536986301 s/day |
| Minimum daily visibility | 514 s |
| Maximum daily visibility | 784 s |
| Maximum LOS-to-next-AOS gap | 48458 s = 13.460556 h |
| Visibility ceiling at 19.2 kbps | 585638400 bytes |
| Minimum daily visibility ceiling | 1233600 bytes |
| Mean daily visibility ceiling | 1604488.767123 bytes |
| Contact ∩ event-log Relay | 178682 s |
| Eligible Relay ideal capacity | 428836800 bytes |
| Minimum daily Relay overlap | 312 s = 748800 bytes |
| Mean daily Relay overlap | 489.539726027 s |
| Simulator-recorded transfer | 3.514083862305 source-labelled MB |

Daily bins are UTC-aligned elapsed days [d×86400,(d+1)×86400); straddling contacts are split by overlap. The 365-day normalization is an explicit event-window accounting convention, not evidence of complete annual telemetry. The longest gap excludes unknown contact opportunities outside the recorded interval; first AOS is34844s and last LOS31526946s. Transition chain checks report zero from/to mismatches; zero-time transitions preserve recorded row order. No inferred Relay interval is extended beyond the final transition. Contacts and mode events are still an artifact group with unknown producing revision, not a matched runtime manifest.

`historical_contacts.csv` records each AOS/LOS, raw duration, Relay overlap, ideal capacities and original transfer. Queue/remaining/unused v3 fields are UNKNOWN for these historical contacts because matching v3 production does not exist. Do not combine the unrelated geometric study or partial telemetry with this annual contact series to fabricate a queue. Both 24h-named contact files are empty and their telemetry spans only an hour; neither proves no contacts in a full day.

