# Feasibility-focused MCR editorial revision — 10 November 2026

## Deliverables

- `output/pdf/ANTARA_MCR_REQUIREMENTS_FEASIBILITY_2026-11-10.pdf`
- `output/pdf/ANTARA_MCR_NARRATIVE_FEASIBILITY_2026-11-10.pdf`

Both use shared technical sources and XeLaTeX. This revision changes presentation and engineering interpretation, not numerical engineering results or mission requirements.

## Substantially rewritten sections

- **Section 1:** scientific evidence interpretation; Narrative Edition expresses duration, mapping and science obligations as prose, retaining the comparison table. All ten original scientific tables remain verbatim in the Requirements Edition, including every approved requirement ID and threshold.
- **Section 2:** concise orbit and lifecycle account. Repeated open-evidence blocks removed; mass and decay constraints moved to their substantive assessments.
- **Section 3:** every subsystem now leads with design, applicable assumptions, calculated results and their feasibility significance. All 51 subsystem obligations and IDs remain unchanged. Tables now contain Requirement, Simulation / Analysis Result and Feasibility Assessment. A shared editorial module supplies evidence wording and assessments to both editions. Missing performance analyses remain NOT YET ASSESSED; supported results are scoped to calculations or reference software, not entire subsystems. The body-frame convention is conditional rather than described as a simulation result.
- **Section 4:** corrected LEOP day, No-LEOP day and LEOP year made central. One source-context passage identifies the 1 March 2000 epoch, unspecified inputs and interval interpretation. Separate paragraphs explain startup, acquisition, operational continuity, battery behavior and return capacity. Existing DITL table results remain unchanged; Cold and Dark (122/0/122 seconds) and Detumble (2460/0/2460 seconds) are added directly from the existing summaries so all mode durations account for each complete horizon.
- **Section 5:** principal integrated conclusion covering all nine requested areas. Operations are supported for the evaluated scenario; overall mission feasibility remains conditional. Component thermal compliance and complete mechanical/mass feasibility are not yet assessed. The RAM-only seven-day outage shortfall is explicit. One “Further Design Development and PDR Scope” subsection consolidates maturation activities, following a separate list of substantive concept questions.
- **Running footer:** replaced internal “Source transcription | Technical review pending” with the edition name.

## Repetitive verification language removed

- Removed all 51 repeated verification-method clauses and the mission-driver/status-code columns from subsystem tables.
- Removed repeated flight-qualification disclaimers and per-subsystem hardware/PDR test prescriptions from feasibility summaries.
- Collapsed the three overlapping communications throughput/PDR paragraphs into one capacity assessment with the gross/net distinction retained.
- Removed the repeated “Outstanding MCR Evidence,” “MCR Open Items,” and “Limitations of Current Evidence” blocks; necessary constraints now accompany the relevant conclusion or the consolidated concept-question list.
- Removed main-body archive paths, registry-management instructions and repeated source-history warnings. Detailed provenance and prior evidence remain in supporting appendices and audit records.
- Reduced the day-run figure caption to its plotted meaning and normalization. Removed its repeated configuration warning; that context appears in the source-context paragraph.

## Annotated PDF disposition

Reference: `/home/sammo/Desktop/ANTARA_MCR_FINAL_DRAFT.pdf`. Extracted mark locations and text are retained in `FEASIBILITY_ANNOTATION_REFERENCE.txt`. Red passages on pages 16–17, 31–32 and 35 were removed or replaced; yellow and pink passages across pages 18–33 informed the subsystem-table, RF, payload and DITL rewrites. Ink marks at appendix headings do not specify a technical deletion, so their supporting analysis is retained.

Essential meanings retained in shorter form despite red marks: the 3 kg limit, propagation cutoff versus reentry, distinct study configurations and ANT-SYS-FR-001. Removing these entirely would discard a mission constraint, misstate the orbit result or violate the requirement-ID preservation instruction. The marked repeat caveats have not been reproduced as new blanket disclaimers.

## Genuine unresolved technical questions

1. Current FPDU energy-dependent response over 5–100 MeV, material/optical selection, effective geometric factor, background discrimination, reconstruction uncertainty and mixed-species trigger/dead-time demand.
2. Eligible science-cell/core definitions, independent-pass accounting, the existing MSC channel-count inconsistency, and fragmented acquisition versus the preferred three contiguous readings.
3. Intended reaction-wheel/magnetorquer actuator selection and authority, pointing/settling allocations and compatible deployment conditions. The separate detumble Monte Carlo cannot provide reliability for this architecture.
4. Selected-cell operating/DoD limits, startup reserve, peak bus loads and consistent array/EOL assumptions. Positive modeled battery energy alone does not assign these margins.
5. Component thermal limits and node mapping, plus mission-coupled hot/cold cases; the available history is an independent heat-schedule calculation.
6. Complete spacecraft mass, panel quantity, packaged/deployment clearances and launch-provider structural loads.
7. Selected RF link budget, net throughput and station availability/outage envelope. The ideal gross 19.2 kbps service is not measured net science throughput.
8. Complete OBC memory/execution/interface allocations and persistent recovery. Seven-day modeled outage requires nonvolatile spill; separate no-downlink grid retention exceeds the 128 MiB candidate.
9. Common simulation configuration and transition/slew semantics for combined mission margins; actual disposal endpoint beyond the drag propagation cutoff.

Routine implementation and qualification tasks are consolidated separately in Section 5 and do not invalidate supported MCR scenario results.

## Validation and preservation

- Both editions compile with XeLaTeX, with no overfull boxes, undefined references/citations, duplicate labels or missing-character warnings.
- 150 unit tests ran successfully; three optional external legacy-model tests skipped. Snapshot checks that prohibited any prose change were replaced by requirement/table/evidence preservation checks. Numerical-model tests were retained.
- `python3 -m scripts.verify_feasibility_editions` passes: shared compiled Sections 4 and 5 match; both subsystem presentations contain the same obligations and evidence; Narrative Edition has no subsystem requirement matrices or IDs.
- All 51 subsystem register entries and ten original scientific tables are unchanged. Hashes of 162 configuration, evidence and media files match the pre-edit snapshot. Existing corrected DITL numeric rows are verbatim; added startup rows match the existing summaries.
- Source snapshots and checks are in `data/derived/feasibility_editorial_2026-11-09/`; the date denotes the start of the editing session.
- Visual review covers the revised main-body tables, figures and section transitions in both editions, using page renders and detailed representative pages.

**No numerical engineering result, mission-success criterion or approved mission requirement was changed.** Results removed from repetitive prose remain in their supporting analyses. No new simulation run or engineering margin was introduced.
