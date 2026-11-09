# Science Record v3 — preliminary MCR reference

CONFIRMED DESIGN INPUT: 292-byte uncompressed logical record, excluding radio framing; 64 uint32 reporting bins. Encoding choices below are explicitly defined engineering reference conventions, not qualified flight interfaces. Definition: `config/science/science_record_v3.json`; input schema alongside it; codec `scripts/science_record_v3.py`. Previous logical v1 remains historical and is not silently mutated.

| Offset | Field | Bytes |
|---|---|---:|
| 0 | Entry time, uint64 | 8 |
| 8 | Exit time, uint64 | 8 |
| 16 | Latitude, int32 | 4 |
| 20 | Longitude, int32 | 4 |
| 24 | Altitude, int32 | 4 |
| 28 | 64 × uint32 counts | 256 |
| 284 | Sequence, uint32 | 4 |
| 288 | Mode/health, uint16 | 2 |
| 290 | CRC16 | 2 |
| | Total | **292** |

Little-endian integers, no padding. Time: unsigned microseconds since 1970-01-01T00:00:00Z under POSIX UTC convention; leap seconds are not representable. Split/flag leap-second acquisition and retain time-correlation metadata; do not silently map ambiguous timestamps. Actual clock accuracy is unqualified. Coordinates: WGS84 geodetic degrees ×10^7, longitude [-180,180), midpoint position of the interval; altitude signed millimetres above WGS84 ellipsoid. The signed altitude field reaches about ±2147 km; it is not a general deep-space format. Position scaling is encoding precision, not navigation accuracy.

Exposure is half-open [entry,exit), with strictly positive duration. A record belongs to a single geographic cell under a versioned tier grid and actual acquisition state. Split on a cell crossing, shutdown, state change or discontinuity; never bridge an acquisition gap. 65 provisional logarithmic edges 5–100 MeV are retained as `FPDU-log64-5-100-v1`; 64 bins do not establish 64 resolved channels. Bin/configuration/calibration/response identity and record version reside in a mandatory session manifest, keyed by sequence epoch. No version byte is invented within the 292 bytes. Sequence-wrap/reboot epochs must remain recoverable; orphaned records cannot establish scientific meaning.

CRC-16/IBM-3740 (CCITT-FALSE): polynomial 0x1021, init 0xFFFF, nonreflected input/output, xorout 0; check `123456789` = 0x29B1. Covers bytes 0–289; CRC stored little endian. Integrity is not authentication or FEC. Flight protocol remains PDR work.

## Reading policy and three distinct acceptance levels

**No numerical minimum acquisition duration or count threshold is imposed.** Prefer three readings per eligible cell visit; use two or one when actual acquisition boundaries/timing permit fewer; no valid exposure means no record. Valid zero-count intervals must be preserved. Actual timer resolution, readout latency, counter swaps and continuity constrain boundaries and remain unverified. The codec's microsecond time unit is not a demonstrated hardware timing capability.

1. Record validity: ordering, geographic attribution, valid detector state, exposure, integer counts and integrity.
2. Statistical precision: accumulate accepted counts with background and uncertainty in each channel. In an ideal independent Poisson zero-background case, sigma=1/sqrt(sum N), not an average of per-record fractional errors. Zero counts remain in exposure and require appropriate interval/upper-limit treatment, not an infinite value silently discarded.
3. Tier success: unchanged coverage, independent passages, energy-channel, precision and temporal requirements. Splitting one visit does not create independent orbital passages. An individual record need not meet a whole-tier uncertainty target.

The reference scheduler partitions already closed segments using supplied realizable boundaries; it is not a flight look-ahead algorithm. Flight closure needs rolling accumulators, timer/cell triggers, uninterrupted counter handoff and bounded event buffers, not routine raw-event downlink. Gaps may impose a record-fragmentation floor even when a one-record sensitivity is requested; no counts/exposure are discarded to force a record total. The current fixture has at most three gated fragments in a geometric visit.

The 292-byte record does not carry full livetime, background, loss or calibration fields. Preserve those in linked session/interval metadata and separate fault logs; health bits cannot substitute for them. Their byte budget is unknown and excluded explicitly from the science-only sizing. Never serialize fractional legacy expected counts as measured integer events or silently round them.

## Alternatives

Uint16: 164 bytes, 43.84% smaller in arithmetic only; overflow validation required. Mixed uint16/uint32 with a 64-bit width mask: 172+2k bytes for k wide bins (fallback to v3 when larger). Sparse uint32 with a 64-bit presence mask: 44+4k bytes for k nonzero bins. These are candidate logical layouts, not approved compressed revisions. Timestamp deltas need recoverable bases/ranges; cell IDs cannot replace required within-cell position and altitude. Lossless block compression requires independently recoverable blocks, CRC and power-loss handling. No compression ratio is assumed: no serialized current-FPDU integer-count archive exists. Supplied histograms are floating legacy expectations, so they cannot establish overflow or compression savings for v3. Zero-count records are useful data, not missing records.

Reproduction: `scripts/validate_telemetry_budget.py`, `scripts/complete_telemetry_budget.py`; derived artifacts and SHA-256 source inventory under `data/derived/telemetry_v3_2026-11-09/`. Original inputs preserved. No simulation campaign or external simulator modification. Arithmetic validation is not instrument qualification.

