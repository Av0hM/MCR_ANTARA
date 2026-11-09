# A.1.2–A.1.3 operational interpretation — 2026-11-09

The user requested substantive operational prose extrapolated from supplied data, followed by explicit assumptions. This is a documentation-only interpretation; it does not change flight architecture, simulation behavior, raw data or scientific acceptance thresholds.

## Evidence and assumptions

Source authority: `evidence/science-ditl/run_registry.json`, corrected-run inventory and validation reports, `docs/audit/SCIENCE_RECORD_V3.md`, and `docs/audit/GS_19K2_LINK_CLOSURE.md`. Corrected LEOP event records supply 120 s startup followed by 2,460 s detumbling: 2,580 s / 43 min to the event-defined end of detumbling. Sampled startup occupancy is 122 s. These are historical 2000-epoch scenario observations, not a flight deadline, 2029 prediction or reliability statistic.

The report now distinguishes these observations from six proposed operating assumptions, recorded directly after A.1.3:

| ID | Interpretation | Remaining verification |
|---|---|---|
| OP-A1 | Boot/time/health checks and deployment interlocks precede dependent activities. | Startup software and hardware readiness. |
| OP-A2 | Detumble exits on state guards, followed by Sun-pointing recovery. | Rate/stability limits and deployment-condition coverage. |
| OP-A3 | Scheduling accounts for slew, settling and recovery resources. | Timing reconciliation, pointing and energy allocations. |
| OP-A4 | Science/Relay arbitration considers opportunity loss and backlog. | Priority policy, outage handling and any concurrency claim. |
| OP-A5 | Overrides preserve valid acquisition intervals and recoverable records. | Power-loss atomicity and transfer integrity. |
| OP-A6 | Fault clearance and distinct recovery guards prevent repeated switching. | Component-derived thresholds and fault-injection testing. |

No numerical battery, thermal, pointing, timing or recovery limit has been invented. No minimum reading duration is imposed. Zero-count intervals remain valid; readings must conserve exposure and counts. The full ideal 19.2 kbps remains a planning opportunity, not verified application throughput.

## Changes and verification

- `appendices/A_operational_logic_visual.tex`: expanded A.1.2 startup, science and relay procedure; A.1.3 priority, interruption and recovery; appended assumptions table; retained all subsection headings and existing diagram identities; corrected diagram return-label placement and kept diagrams within their sections.
- `README.md`: points to the new reviewed PDF.
- `docs/audit/IMPLEMENTATION_CHANGELOG.md`: records this extension.
- This audit and `output/pdf/ANTARA_MCR_OPERATIONAL_ASSUMPTIONS_2026-11-09.pdf` are new.

Six bounded document checks passed: unchanged subsection sequence, preserved labels, unique six assumption IDs, startup arithmetic, assumption placement, and no arbitrary acquisition minimum. `git diff --check` passed. XeLaTeX through latexmk succeeded (91 pages); no overfull boxes or undefined references. Existing font-substitution/underfull warnings remain. New Appendix pages were rendered and visually reviewed. No simulation was run; earlier PDFs and raw evidence remain unchanged.

Build command:

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=/tmp/antara-a1/latex main.tex
```
