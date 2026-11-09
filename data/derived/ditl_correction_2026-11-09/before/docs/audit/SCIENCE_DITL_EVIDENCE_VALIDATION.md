# Science/DITL evidence validation

## Incomplete annual telemetry and incompatible event exports

The annual-labelled telemetry accounts for4,320,020s, ending with a positive20s interval starting at4,320,000s and no terminal snapshot. All1,861,462 timestamps/intervals are monotonic and continuous (2s/20s sampling); this does not establish an annual completion. Do not add a fabricated terminal interval or horizon flush.

Recorded mode seconds: {"COLD_AND_DARK": 122.0, "DETUMBLE": 2460.0, "SUN_POINTING": 666440.0, "DETECTION": 1296.0, "RELAY": 33022.0, "SLEWING": 3616666.0, "SAFE": 14.0}. Slewing dominates this artifact; the differing event export reports only67,844s of slews over the overlapping50-day window, versus3,616,666s in telemetry. These are not reconciled operational predictions.

| Quantity | Telemetry through4,320,020s | Events ending within that window |
|---|---:|---:|
| Geographic SAA dwell s |130664|120568|
| Contact visibility/duration s |36754|33668|
| Transferred source MB |0.004928588867|0.477813720703|
| Serialized science source MB |0.004928588867|0.396621704102 (SAA attribution)|
| Legacy expected proton counts |25181522.3440|424178217.1487|

Full event exports extend nearly365days and contain820 contacts,2346 SAA records,2298 proton-pass summaries and7928 slew records. Their total downlink is3.5140838623 sourceMB; that is a separate export statistic, not annual telemetry closure. Their UTC events establish2000-03-01 epoch. Even overlap filtering fails consistency: possible mixed revisions/exports are suspected, exact cause unknown. Per-file hashes and separate telemetry/event manifests prevent accidental pooling.

## Time and science accounting

Telemetry's geometric SAA exposure130664s is distinct from1246s labelledDetection inside SAA and342s acquisition-enabled exposure (171 two-second rows). Thus model acquisition/SAA is342/130664=0.26174%; do not call this qualified science duty or mix it with event-row fractions. Source `science_fraction` uses sample counts and lacks verified independent-pass semantics. No current-FPDU valid-observation total is established.

Expected-count arrays contain64 entries. Their summed counts equal summed rate×interval to a maximum per-row difference1.21e-7 counts, attributable to text precision. Individual-bin differences reach5714.15 because source periphery merging relocates counts; summed conservation alone does not verify effective energy-bin metadata. The counts are deterministic legacy expectations, not stochastic events, measured energies or independently reconstructed protons. Current source uses differential intensity×G×efficiency×bin width×exposure for the histogram, but a separate environment diagnostic still has historically problematic dimensional semantics; do not use it as integrated counts. Current-source G≈0.314159, legacy five-layer response, arbitrary efficiency lookup,20ns coincidence and250ns per-bin dead time cannot qualify approved six-scintillator FPDU with unknown dead time and200ns coincidence target. No physical assumption was transferred.

## Serialization/storage/downlink

Telemetry cumulative generation and transfer agree with sums of incremental columns (≤1e-15 sourceMB). Storage balance initial10+generated−transferred agrees within1.78e-15. Max storage10.004928589; final10.0. Source totals represent5168 serialized bytes if interpreted with the histogram serializer's2^20 conversion. The `science_histogram_bytes` column sums4080: four positive serialization rows occur outside the acquisition gate, accounting for missing boundary-flush metadata. This is not automatically lost science; verify flush attribution and schema. No packet payload archive is supplied to validate serialization contents, integrity, losses or delivery of identified records.

RF source computes Mbps×seconds/8 while histograms divide bytes by2^20. Its *_mb fields therefore have a potential MB/MiB convention mismatch (factor1.048576). Report raw source units; do not claim byte-accurate real downlink. `downlinked_mb` is modeled transfer credit, not received packets. The combined source contact opportunity at19.2kbit/s is only a hypothetical gross capacity, not flight throughput. Ground-contact/pointing gates and adaptive link factors must be reconciled with the correct run.

Battery minimum15.215199Wh and final25Wh; recorded solar10808.46544Wh/load8847.62130Wh are integrations over this incomplete artifact, not a validated energy margin. Charging taper, curtailment and source identity prevent deriving efficiency or lifetime from these totals. Saturation/recovery/control stability needs run-matched histories and timestep checks.

## Figures and disposition

Derived partial-annual storage plot is explicitly incomplete and inconsistent with event exports. Supplied unprefixed figures are not linked to a verified run and are not adopted. No reconstructed-spectrum figure is fabricated. Historical24h six-pass/two-contact/62.7% examples remain clearly distinct from the new one-hour files. The MCR preserves their historical status without attributing those numbers to this delivery.

Open: full24h exports/manifests; matched annual event+telemetry identities; terminal closure; event/row boundary semantics; shared dead-time/response validation; packet-unit and flush metadata; independent visits and calibrated scientific eligibility. No expensive campaign or authoritative source modification was performed.

## Adopted operational scope

The user subsequently directed the MCR to use only `leop_1yr` and ignore the short24h-named exports. Their audit records/derived plots remain preserved but are not referenced as operational comparison results in the final MCR. The annual mode/exposure chart and storage diagnostic use only annual-labelled telemetry. Storage curves use decimated plot samples; all numerical summaries use all records. A full-year claim remains blocked by missing terminal/completion evidence and mismatched event exports.
