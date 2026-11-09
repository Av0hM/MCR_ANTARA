# GS PASS CAPACITY VALIDATION — corrected evidence 2026-11-09

Corrected source registry: `evidence/science-ditl/run_registry.json`. Recompute with `scripts/validate_corrected_ditl.py`; source hashes/headers are in `inventory.json`, numerical summaries and ledgers in `data/derived/ditl_correction_2026-11-09/`. Prior DITL conclusions are superseded, not silently retained.

| Run | Contacts | Contact s | Relay s | Ideal Relay bytes | Native transfer source MB |
|---|---:|---:|---:|---:|---:|
| leop_24h | 2 | 766 | 646 | 1,550,400 | 0.009078979 |
| no_leop_24h | 2 | 766 | 646 | 1,550,400 | 0.009338379 |
| leop_1yr | 820 | 244,016 | 178,682 | 428,836,800 | 3.514083862 |

All three runs have complete timestamp spans, but producing revision/configuration, RAAN, mass, integrator, runtime elevation mask and battery capacity remain UNKNOWN. Altitude is recorded directly; 25 Wh percentages are planning-normalized only. All event absolute/relative origins agree on 2000-03-01. A 365-day span ends 2001-03-01; February 29 precedes its start. No 2029 recalibration is claimed.

No duplicate or nonmonotonic telemetry timestamps or nonfinite selected scalar values were found. Observed adaptive cadences do not establish the expected sample schedule. Left-held telemetry intervals exclude final-row duration. Transition sequence and timestamp offsets are separately recorded; elapsed coverage is not proof of correct logger/control semantics. Comparison classification: SENSITIVITY ONLY (recorded orbit/contact similarity, runtime identity unverified).

Native source-MB amounts are retained without silently choosing decimal versus binary scaling. Legacy model arrays and five-channel fields do not qualify current FPDU response. No accepted-event archive, reconstructed integer spectra, calibrated livetime, received packet archive or full hardware configuration is supplied. No MMSC/MSC/EMSC success metric is qualified by these outputs.

AOS/LOS subtraction and timestamp epoch checks are explicit. Apply no duplicate mask penalty. Telemetry and transition-log Relay overlap are separate calculations in each summary.
