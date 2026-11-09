# LEOP VS NO LEOP 24H VALIDATION — corrected evidence 2026-11-09

Corrected source registry: `evidence/science-ditl/run_registry.json`. Recompute with `scripts/validate_corrected_ditl.py`; source hashes/headers are in `inventory.json`, numerical summaries and ledgers in `data/derived/ditl_correction_2026-11-09/`. Prior DITL conclusions are superseded, not silently retained.

| Run ID | Rows | Span (s) | Epoch | Verdict |
|---|---:|---:|---|---|
| `corrected_leop_24h_8363c5901b` | 7696 | 86400 | 2000-03-01T00:00:00+00:00 | COMPLETE TIMESTAMP SPAN |
| `corrected_no_leop_24h_a652068558` | 6553 | 86400 | 2000-03-01T00:00:00+00:00 | COMPLETE TIMESTAMP SPAN |
| `corrected_leop_1yr_015cfb89b1` | 1434872 | 3.1536e+07 | 2000-03-01T00:00:00+00:00 | COMPLETE TIMESTAMP SPAN |
| Metric | LEOP | No LEOP | Difference (No−LEOP) | Percent vs LEOP |
|---|---:|---:|---:|---:|
| Recorded timestamp span (s) | 86,400 | 86,400 | 0 | 0.000% |
| Sun Pointing (s) | 79,268 | 81,852 | 2,584 | 3.260% |
| Detection (s) | 2,676 | 2,674 | -2 | -0.075% |
| Relay (s) | 894 | 894 | 0 | 0.000% |
| Slewing (s) | 980 | 980 | 0 | 0.000% |
| Safe (s) | 0 | 0 | 0 | undefined |
| Geographic SAA (s) | 2,696 | 2,696 | 0 | 0.000% |
| Acquisition gate (s) | 758 | 758 | 0 | 0.000% |
| Minimum recorded battery (Wh) | 15.128 | 18.004 | 2.876 | 19.008% |
| Recorded solar integral (Wh) | 145.575 | 150.403 | 4.828 | 3.317% |
| Recorded load integral (Wh) | 85.167 | 85.719 | 0.552 | 0.649% |
| Native generation (source MB) | 0.009 | 0.009 | 0 | 2.857% |
| Native transfer (source MB) | 0.009 | 0.009 | 0 | 2.857% |

All three runs have complete timestamp spans, but producing revision/configuration, RAAN, mass, integrator, runtime elevation mask and battery capacity remain UNKNOWN. Altitude is recorded directly; 25 Wh percentages are planning-normalized only. All event absolute/relative origins agree on 2000-03-01. A 365-day span ends 2001-03-01; February 29 precedes its start. No 2029 recalibration is claimed.

No duplicate or nonmonotonic telemetry timestamps or nonfinite selected scalar values were found. Observed adaptive cadences do not establish the expected sample schedule. Left-held telemetry intervals exclude final-row duration. Transition sequence and timestamp offsets are separately recorded; elapsed coverage is not proof of correct logger/control semantics. Comparison classification: SENSITIVITY ONLY (recorded orbit/contact similarity, runtime identity unverified).

Native source-MB amounts are retained without silently choosing decimal versus binary scaling. Legacy model arrays and five-channel fields do not qualify current FPDU response. No accepted-event archive, reconstructed integer spectra, calibrated livetime, received packet archive or full hardware configuration is supplied. No MMSC/MSC/EMSC success metric is qualified by these outputs.

Both day runs have equal total acquisition gate; startup removal is not evidence of more qualified science. Event startup and Slewing are distinct from telemetry occupancy.
