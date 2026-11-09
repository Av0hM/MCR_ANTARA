# Corrected DITL authority — 2026-11-09

This current correction supersedes all earlier Science/DITL-dependent statistics and evidence statuses below. Earlier entries are retained as historical audit history, not active numerical claims. Independent physics/design/RAAN/thermal/detumble findings are unaffected. Current sources: `CORRECTED_DITL_RUN_VALIDATION.md`, `DITL_CORRECTION_IMPACT_MATRIX.md`, `STORAGE_BACKLOG_VALIDATION.md`, and `evidence/science-ditl/run_registry.json`.

All three corrected timestamp spans are complete (86400/86400/31536000 s), epoch2000-03-01. Annual acquisition247258 s; minimum recorded battery15.097556 Wh; full ideal Relay428836800 bytes; preferred EMSC v3 slot volume46637364 bytes; nominal peak75336 bytes; seven-day outage peak1010028 bytes. Runtime config and transition/slew semantics remain unresolved. No2029 calibration or qualified science success follows.

Current requirement status totals: {'CONDITIONAL': 17, 'OPEN': 28, 'SUPPORTED': 3, 'NOT EVALUATED': 3}. ANT-OBC-FR-002 is CONDITIONAL (outage spill needed); ANT-GSO-FR-003 is CONDITIONAL (coverage corrected, logger/source closure open), replacing its earlier NOT MET truncation rationale. Full updated register: `SUBSYSTEM_REQUIREMENT_TRACEABILITY.md`.

---

## Prior audit history (DITL-dependent entries superseded)

# Section 3 subsystem feasibility requirements — 2026-11-09

## Discovery and authority

The active inclusion is `main.tex` → `sections/03_spacecraft_architecture.tex`. Its nine existing headings are EPS; COMMS; Scientific Payload; ADCS; OBC; Spacecraft Coordinate System; Thermal and Structural Configuration; Ground Segment and Mission Operations; Outstanding MCR Evidence. No separate SDM subsection exists. Deployables/SDM are covered under STR; navigation/time/ICD under INT and OBC; fault management under OBC/ADCS/GSO. Headings and numbering are unchanged. The old `*_additions.tex` templates are not included by main.tex and were not promoted into live requirements.

Existing Section 1 mission IDs MM-M-01…05, MS-M-01…05 and EM-M-01…06 remain authoritative. No previous ANT-*-FR IDs were found, so the new stable child IDs do not collide with an existing obligation. Each child row allocates a parent mission condition, interface or budget; it is not a replacement science criterion. Existing Appendix A.1–A.6 tables and engineering evidence remain intact and are referenced, not duplicated as another independent baseline.

## Method and scope

Source of truth: `config/requirements/section3_feasibility_v1.json`. Renderer: `scripts/render_section3_requirements.py`. Generated LaTeX: nine files in `sections/requirements/`. Full register: `SUBSYSTEM_REQUIREMENT_TRACEABILITY.md`. Every row carries exact text, parent, tier relevance, driver/interface, source paths, verification method, evidence scope/status, open decision, concept closure and PDR verification. Labels use the complete stable ID. Main tables abbreviate statuses with an explicit legend: S SUPPORTED, C CONDITIONAL, O OPEN, NM NOT MET, NE NOT EVALUATED. Ten-point text and continued table blocks avoid tiny fonts or clipped rows.

SUPPORTED means only the stated model/software/documented-interface condition, never subsystem hardware qualification. Open derived limits are explicit, not invented tolerances. Missing concept-level allocations block unconditional conclusions; hardware correlation/qualification is later PDR work. The exact original Section 3 paragraphs are preserved and checked by automated tests. Added assessments interpret the original design-maturity statement conditionally rather than deleting its narrative.

## Status by subsystem

| Subsystem | IDs | S | C | O | NM | NE |
|---|---|---:|---:|---:|---:|---:|
| EPS | ANT-EPS-FR-001 … ANT-EPS-FR-006 | 0 | 3 | 3 | 0 | 0 |
| COM | ANT-COM-FR-001 … ANT-COM-FR-005 | 1 | 1 | 2 | 0 | 1 |
| PLD | ANT-PLD-FR-001 … ANT-PLD-FR-011 | 1 | 4 | 6 | 0 | 0 |
| ADCS | ANT-ADCS-FR-001 … ANT-ADCS-FR-006 | 0 | 1 | 5 | 0 | 0 |
| OBC | ANT-OBC-FR-001 … ANT-OBC-FR-007 | 1 | 3 | 2 | 0 | 1 |
| INT | ANT-INT-FR-001 … ANT-INT-FR-003 | 1 | 0 | 2 | 0 | 0 |
| THM | ANT-THM-FR-001 … ANT-THM-FR-004 | 0 | 1 | 3 | 0 | 0 |
| STR | ANT-STR-FR-001 … ANT-STR-FR-004 | 0 | 1 | 3 | 0 | 0 |
| GSO | ANT-GSO-FR-001 … ANT-GSO-FR-004 | 0 | 0 | 2 | 1 | 1 |
| SYS | ANT-SYS-FR-001 … ANT-SYS-FR-001 | 0 | 1 | 0 | 0 | 0 |

Total: **51 requirements; 4 supported, 15 conditional, 28 open, 1 not met, 3 not evaluated**. Thirty-two rows are flagged as essential concept-level allocation/evidence gaps, not thirty-two independent spacecraft failures. The not-met item is GSO-003: the supplied annual artifact group is incomplete and inconsistent. No new hardware failure or detumble reliability threshold is inferred.

## Numerical and evidence reconciliation

- MMSC: retain5° grid,≥70% global/≥90% core coverage,≥3 independent passes/cell,≥2 channels,≤50% uncertainty,4–6month window and≥150 operational received passes.
- MSC: retain1° grid,≥90% detectable-cell coverage,≥5 independent passes/cell,≤25% in two lowest channels,all operational channels,monthly products and>3σ change flag,12–14months and≥900 operational passes. Section1's summary also says≥4 channels; no silent choice between that and detailed all-operational wording is made. PLD-003 remains OPEN pending owner reconciliation, without lowering either statement.
- EMSC: retain0.5° grid,≥95% of cells above AP9 1%-of-mission-peak eligibility,≥5 independent passes/cell,≥3channels,≤10% in one/≤15% in remaining operational channels,primary-map≤15% rule,18–20months,≥2400 operational passes andtwo9–10month submaps. A per-bin95th-percentile required-G study is not this mission acceptance test.
- Poisson examples N≈4 and N≥16 are counting-only approximations, not total flux-uncertainty or new confidence requirements. No new confidence probability is invented. Eligibility, core and independence remain unresolved acceptance definitions.
- Current payload geometry/timing and v3 record are unchanged. No minimum reading duration/count or 400Hz throughput ceiling is imposed. Zero-count validity, actual mixed-species triggers, unknown dead time, bin/exposure conservation and aggregate precision remain distinct.
- Full19200bit/s modeled Relay opportunity remains an MCR assumption, without arbitrary derating. Historical contact dates remain2000; partial telemetry is not made annual. 256KiB/128MiB/16GB remain candidate science-memory allocations, not verified total OBC memory or mandatory retention.
- Thermal limits, pointing tolerances, allowable DoD, transients, actuator authority and launch spectra/frequencies are OPEN where no selected-interface evidence exists. Reported temperatures, averaged power and a single successful detumble are not compliance thresholds.

## Verification and change boundary

Twelve bounded requirements tests verify unique IDs/text/labels, complete traceability and source paths, all nine tables/assessments, exact original prose and headings, unchanged mission/config hashes, supported-scope qualifications, channel ambiguity, and no invented minimum-duration/link-derating rule. Full suite/build results and exact files are in `data/derived/section3_requirements_2026-11-09/`. The complete MCR is rebuilt in an isolated output directory and visually checked across every new requirements table. No numerical datasets, physical models or simulation source were edited; no simulation campaign was launched.
