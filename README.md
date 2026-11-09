# ANTARA Mission Concept Review

Build the active report with `latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex`. The reviewed PDF is `output/pdf/ANTARA_MCR_OPERATIONAL_ASSUMPTIONS_2026-11-09.pdf`; older PDFs remain historical.

Sections 1–5 contain the decision-first MCR. Appendix A preserves six technical-support groups A.1–A.6, including current payload A.2. Later source-detail appendices explicitly distinguish historical designs from current decisions. External archives referenced by the audits are not claimed to be a local `source_archive/` folder.

- Current mission: `config/mission/antara_2029.json`.
- Current payload pointer: `config/payload/current.json`.
- Change/test/build record: [implementation changelog](docs/audit/IMPLEMENTATION_CHANGELOG.md).
- Prior findings: [2029 reconciliation](docs/audit/2029_AUDIT_RECONCILIATION.md).
- Physical closure: [remaining decisions](docs/audit/REMAINING_OPEN_DECISIONS.md).

Run bounded local checks with `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`. Three optional historical-model tests require the Orekit environment and `ANTARA_LEGACY_SRC`; they explicitly skip otherwise. No annual simulation is needed.

The approved mechanical concept, planning inputs and tested software contracts do not establish a calibrated detector or complete mission success. The sibling authoritative simulator is separate; `patches/simulation/` contains tested, unapplied accounting corrections and reproduction instructions. Historical raw data and configuration revisions are preserved.

The corrected Science/DITL exports are selected by `evidence/science-ditl/run_registry.json`. Both day runs span24h and the annual run spans365days, with event epoch2000-03-01. Old raw files and earlier summaries are superseded. See [corrected run validation](docs/audit/CORRECTED_DITL_RUN_VALIDATION.md). Runtime manifests and mode/slew semantics remain unresolved.

The current [telemetry v3 audit](docs/audit/TELEMETRY_MCR_CHANGELOG.md) defines the292-byte reference, full ideal19.2kbps Relay capacity and conditional science-memory allocations. It retains zero-count valid exposures and imposes no arbitrary minimum reading duration.
