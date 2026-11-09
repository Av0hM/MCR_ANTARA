# SCIENCE DITL EVIDENCE VALIDATION — corrected evidence 2026-11-09

Corrected source registry: `evidence/science-ditl/run_registry.json`. Recompute with `scripts/validate_corrected_ditl.py`; source hashes/headers are in `inventory.json`, numerical summaries and ledgers in `data/derived/ditl_correction_2026-11-09/`. Prior DITL conclusions are superseded, not silently retained.

| Run ID | Rows | Span (s) | Epoch | Verdict |
|---|---:|---:|---|---|
| `corrected_leop_24h_8363c5901b` | 7696 | 86400 | 2000-03-01T00:00:00+00:00 | COMPLETE TIMESTAMP SPAN |
| `corrected_no_leop_24h_a652068558` | 6553 | 86400 | 2000-03-01T00:00:00+00:00 | COMPLETE TIMESTAMP SPAN |
| `corrected_leop_1yr_015cfb89b1` | 1434872 | 3.1536e+07 | 2000-03-01T00:00:00+00:00 | COMPLETE TIMESTAMP SPAN |
| Metric | LEOP 24h | No-LEOP 24h | LEOP 365d |
|---|---:|---:|---:|
| Recorded timestamp span (s) | 86,400 | 86,400 | 31,536,000 |
| Sun Pointing (s) | 79,268 | 81,852 | 29,660,918 |
| Detection (s) | 2,676 | 2,674 | 894,054 |
| Relay (s) | 894 | 894 | 269,876 |
| Slewing (s) | 980 | 980 | 375,688 |
| Safe (s) | 0 | 0 | 332,882 |
| Geographic SAA (s) | 2,696 | 2,696 | 881,882 |
| Acquisition gate (s) | 758 | 758 | 247,258 |
| Minimum recorded battery (Wh) | 15.128 | 18.004 | 15.098 |
| Recorded solar integral (Wh) | 145.575 | 150.403 | 50,288.809 |
| Recorded load integral (Wh) | 85.167 | 85.719 | 30,866.103 |
| Native generation (source MB) | 0.009 | 0.009 | 3.514 |
| Native transfer (source MB) | 0.009 | 0.009 | 3.514 |

All three runs have complete timestamp spans, but producing revision/configuration, RAAN, mass, integrator, runtime elevation mask and battery capacity remain UNKNOWN. Altitude is recorded directly; 25 Wh percentages are planning-normalized only. All event absolute/relative origins agree on 2000-03-01. A 365-day span ends 2001-03-01; February 29 precedes its start. No 2029 recalibration is claimed.

No duplicate or nonmonotonic telemetry timestamps or nonfinite selected scalar values were found. Observed adaptive cadences do not establish the expected sample schedule. Left-held telemetry intervals exclude final-row duration. Transition sequence and timestamp offsets are separately recorded; elapsed coverage is not proof of correct logger/control semantics. Comparison classification: SENSITIVITY ONLY (recorded orbit/contact similarity, runtime identity unverified).

Native source-MB amounts are retained without silently choosing decimal versus binary scaling. Legacy model arrays and five-channel fields do not qualify current FPDU response. No accepted-event archive, reconstructed integer spectra, calibrated livetime, received packet archive or full hardware configuration is supplied. No MMSC/MSC/EMSC success metric is qualified by these outputs.

Record validity is separate from statistical precision and mission success. Zero-count exposures are retained. There is no arbitrary minimum reading duration. Ideal partitions conserve exposure and never bridge shutdown; real timing resolution remains unknown. If more than three acquisition fragments occur in a cell visit, preserving all contiguous intervals requires more than three records; this is flagged as an interface decision, not silently discarded exposure.

Queue calculations use full 2400 bytes/s, initially empty v3 queues, no RF derating, and only source-contact/telemetry-Relay intersections. Native initial store is not silently counted as v3 science. Exact cell crossing times and hardware partition boundaries are absent, so these are time-aligned workload sensitivities, not demonstrated emitted records. All-particle electronics throughput is independent of this histogram byte budget.

## Sampling and event reconciliation

Day-run timestamp differences are2/20s. Annual differences are2/60s with one50s interval, not the current source20s coarse default. This is an additional configuration distinction. Annual telemetry reports15161 mode changes versus16283 transition records (ordered transition chain itself is valid). Event Slewing totals512586s, transition-derived Slewing620804s, and left-held telemetry Slewing375688s; these are unresolved logger/control definitions, not equivalent metrics. Annual SAFE occupancy332882s has425 sampled entries. Contact duration and native transfer totals reconcile;2346 SAA events and2298 proton-pass records have different inclusion rules. Neither is automatically a qualified independent science-pass count.

## Recorded battery-state variation

| Run | Sum of increases (Wh) | Sum of decreases (Wh) |
|---|---:|---:|
| leop_24h | 44.813018 | 38.670457 |
| no_leop_24h | 43.846674 | 37.737849 |
| leop_1yr | 13507.688098 | 13501.667742 |

These adjacent-record differences close against final minus first recorded battery. They are not battery charge throughput, solar curtailment, efficiency or a recovered usable capacity. Those fields are absent and remain UNKNOWN.
