# Preliminary OBC science RAM and nonvolatile allocation

| Quantity | Bytes / capacity | Interpretation |
|---|---:|---|
| One v3 assembly buffer |292|Packed record only|
| Two uint32 histogram banks |512|Candidate ping-pong accumulator, not selected ASIC/OBC architecture|
| Combined illustrative working payload |804|Excludes RTOS, stack, DMA, reconstruction, queue descriptors and other software|
| Dedicated science queue |262144 =256KiB|897 complete292-byte records;220 spare bytes before metadata|
| Baseline science flash |134217728 =128MiB|459649 complete records before metadata/reserves|
| Extended archival trade |16000000000 =16GB usable|54794520 complete records; not mandatory|

The preferred EMSC bounded diagnostic requires67452 bytes/231 record slots before delivery. MMSC16644 bytes/57 slots; MSC50808 bytes/174 slots. This is the smallest payload queue demonstrated by these fixtures only, not a qualified worst-case memory requirement. 256KiB is a preliminary science-queue engineering allocation; working buffers must be added outside that queue, not counted twice. Total OBC RAM remains unknown until FSW, reconstruction, DMA and other subsystem budgets are included. Component memory capacity has not been verified here.

128MiB is a reasonable candidate persistent queue to test, not a closed mission requirement. The geometric all-visit sensitivity needs62499388/124998776/187498164 bytes for1/2/3 readings. Three-reading retention exceeds128MiB by53280436 bytes before filesystem or other data. Two-reading retention leaves9218952 bytes before overhead. Without a known study horizon and delivery history, neither proves mission storage sufficiency. A full three-reading archive needs at least187498164 usable payload bytes plus unknown reserves. Use exact inventory volume, not an invented retention duration. 16GB is an extended trade, not required by present evidence.

For an explicitly specified production envelope V bytes/day and no contact for d days, additional accumulation is Vd plus initial backlog/burst; at the historical longest visibility gap use V×48458/86400. These are formulas, not measured rates. One missed eligible window and1/3/7-day outages are tested in the bounded legacy trace; its generated data are finite and concentrated at startup, so the same peak does not establish outage tolerance for sustained science. No RAM/flash overflow occurs in that tiny fixture. Constant production exceeding long-run delivery cannot be fixed by finite storage.

Housekeeping, diagnostic and calibration metadata rates are UNKNOWN, excluded from science-only totals. PDR must allocate filesystem/journal/ECC/bad-block/wear reserves, retain acknowledged-vs-unacknowledged records, handle sequence-wrap/reboot identity, atomic CRC-protected writes and recover incomplete tails after power loss. Erasure only after verified delivery/retention policy; no assumed reserve percentage. Test power interruption, media endurance/radiation behavior and worst-case background/reconstruction load. Dedicated queue is not total OBC memory.
Reproduction: `scripts/validate_telemetry_budget.py`, `scripts/complete_telemetry_budget.py`; derived artifacts and SHA-256 source inventory under `data/derived/telemetry_v3_2026-11-09/`. Original inputs preserved. No simulation campaign or external simulator modification. Arithmetic validation is not instrument qualification.

