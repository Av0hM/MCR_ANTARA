# Bounded time-aligned backlog validation

Reproduction: `scripts/validate_telemetry_budget.py`, `scripts/complete_telemetry_budget.py`; derived artifacts and SHA-256 source inventory under `data/derived/telemetry_v3_2026-11-09/`. Original inputs preserved. No simulation campaign or external simulator modification. Arithmetic validation is not instrument qualification.

Only the partial annual telemetry supplies time-aligned mode/visibility/acquisition samples. The new v3 records were not actually produced by this legacy simulator. Record-slot releases occur at ideal reading exit times; queue starts empty and contains only the new science stream, excluding the historical unexplained10 source-MB initial store. Service is the intersection of visibility and Relay at19200bit/s. No simultaneous Detection/Relay is assumed; no second mask or throughput factor. Pausable FIFO byte-stream service may span contacts; framing/resume protocol is PDR work. The table reports mathematical record slots, not fabricated detector packets.

| case | generated_bytes | transferred_bytes | remaining_bytes | peak_required_bytes | minimum_byte_balance_bitrate_bps |
|---|---|---|---|---|---|
| MMSC_1 | 11972 | 11972 | 0 | 11972 | 2.9375000000976286 |
| MMSC_2 | 13432 | 13432 | 0 | 13432 | 3.291666667154753 |
| MMSC_3 | 16644 | 16644 | 0 | 16644 | 4.076923076990424 |
| MSC_1 | 16936 | 16936 | 0 | 16936 | 4.148148148578253 |
| MSC_2 | 33872 | 33872 | 0 | 33872 | 8.28169014121071 |
| MSC_3 | 50808 | 50808 | 0 | 50808 | 12.416666667103343 |
| EMSC_1 | 22484 | 22484 | 0 | 22484 | 5.502762431296285 |
| EMSC_2 | 44968 | 44968 | 0 | 44968 | 10.989473684547995 |
| EMSC_3 | 67452 | 67452 | 0 | 67452 | 16.480000000318398 |

Byte balance is checked: generated=transferred+remaining+dropped. CSVs give releases and, per eligible service window, queue before, transferred, backlog after and unused capacity. The minimum-rate search is horizon-specific with integer-byte service; it is not a hardware throughput measurement or sustainable annual rate. Preferred EMSC's ideal-rate ratio is reported in JSON, but must not be quoted as a mission communications margin.

The largest partial-telemetry Relay gap is48456s; generation during that specific gap is zero. The worst queue occurs before earlier delivery, not during the largest geometric gap. Removing one eligible service window or a worst-start1/3/7-day outage leaves the preferred EMSC peak67452bytes because all fixture generation already precedes delivery. This behavior cannot characterize continuing operational science. The annual contact table lacks matching generation; its queue values remain UNKNOWN.

Compression/uint16 alternatives cannot be empirically sized from fractional expected-count arrays. Do not round legacy predictions into events. Per-bin counters must never wrap; close a record early on capacity limits, preserve exposure, and flag any genuinely lost events in linked quality metadata. Hardware counter service, metadata size, exact geographic crossings and readout continuity remain open. Zero-count valid intervals are retained, not suppressed as an optimization.


The byte-service fixture assumes transfer credit frees the modeled queue immediately; acknowledgement/retry retention is not modeled. Overflow accounting is a byte-budget diagnostic, not a flight record-dropping policy. Atomic record persistence and loss flags require separate FSW tests.
