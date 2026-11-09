# Telemetry v3 MCR integration — 2026-11-09

## Disposition

The current report now defines a292-byte v3 reference record, nonoverlapping three/two/one reading policy with no arbitrary minimum acquisition duration, and separate record validity, accumulated precision and tier success. Valid zero-count exposure is retained. The approved ideal19200bit/s is used in full during visibility∩Relay, with no arbitrary derating. Conditional data-handling arithmetic is established; sustained mission science production, current detector response and physical RF throughput are not qualified.

## Phase results

| Phase | Work / results | Remaining boundary |
|---|---|---|
| 0 | Read current report/audits/source contracts; preserved dirty checkout and raw input hashes | No producing manifest for grid, contacts or complete annual telemetry |
| 1 | Full19.2kbps/2400bytes/s,100%science Relay allocation; explicit PDR RF deferral | AX100 configuration and net throughput unverified |
| 2 | Versioned292-byte codec/schema, explicit time/position/endian/CRC/status definitions | Linked metadata and clock/FSW implementation unqualified |
| 3 | User clarification applied: no minimum duration/count; valid zero intervals retained; segment boundaries conserve exposure | Hardware timing/boundaries unknown; offline partition fixture only |
| 4 | Grid totals reproduced; partial-telemetry tier visit/record sensitivities computed | No unverified horizon scaling or fake histogram events |
| 5 |820contacts244016s,514s minimum daily visibility,48458s longest internal gap | Historical2000epoch, runtime mask/RAAN unknown |
| 6 |585638400 visibility bytes;428836800 Relay-overlap bytes | Actual transfer3.514084 sourceMB remains separate |
| 7 |256KiB897record slots;128MiB459649;16GB optionaltrade | Metadata/FSW/retention budget unknown;128MiB cannot retain full187498164-byte grid sample |
| 8 | Time-aligned record-slot queues clear; preferred peak16644/50808/67452bytes; outages tested | Near-disabled legacy acquisition does not establish sustained production |
| 9 | uint16/mixed/sparse/delta/lossless alternatives described without assumed compression | Need current integer count distributions and overflow tests |
| 10 | Main sections3/4/5; AppendixA.2/A.3/A.5/A.6/F; historical rate notices updated | Current payload, science thresholds and unrelated models unchanged |
| 11 |173passed,3skipped,16subtests;74-page fullXeLaTeX PDF; zero overfull/undefined/multiply-defined labels | Existing font-substitution/underfull warnings retained, not hidden |
| 12 | Eight audit docs, exact source hashes, release/service ledgers, figures and finalPDF delivered | MCR supports conditional discussion, not unconditional data-balance closure |

Initial integration assertion exposed that MMSC's19gated geographic visits contain41continuous acquisition fragments. The analysis was corrected to allocate across each visit while preserving all gaps/exposure, rather than multiplying3 by41. Final preferred MMSC count is57. One-reading sensitivity has a41-record fragmentation floor, not19 falsely continuous records. No originals or historical numerical outputs were changed.

## Reproduction commands

From repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python scripts/validate_telemetry_budget.py
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python scripts/complete_telemetry_budget.py
MPLCONFIGDIR=/tmp/antara-evidence-20261109/mpl PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python scripts/plot_telemetry_budget.py
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python -m pytest -q -p no:cacheprovider tests
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=/tmp/antara-telemetry-v3/latex main.tex
git diff --check
```

The isolated LaTeX outdir preserves pre-existing root PDF/intermediate modifications. Final PDF: `output/pdf/ANTARA_MCR_TELEMETRY_V3_2026-11-09.pdf`. The prior simulation-evidence PDF remains unchanged (71pages). Test logs, build logs, source inventory, preservation check, verification summary and exact changed-file list are in `data/derived/telemetry_v3_2026-11-09/`. Three skips are optional legacy-model tests, not new codec failures.37new tests cover codec/CRC/status, zero/short exposures, aggregation, fragments, overflow, contacts/units, Relay-only queues, outages and provenance. Original48simulation files and9geometric-factor files are SHA-256 unchanged. Existing mission/payload configs and rootPDF remain unchanged. No Git mutation, external simulator edit, expensive simulation or hardware choice was performed.

## Exact changed files

- `config/payload/README.md` — explains immutable snapshot nulls versus the separate current v3 reference.

- `README.md`
- `appendices/B_payload_detail_visual.tex`
- `appendices/C_simulation_provenance.tex`
- `appendices/E_budgets_and_bom_details.tex`
- `appendices/F_orbit_rf_support.tex`
- `appendices/H_source_detail.tex`
- `appendices/I_source_detail.tex`
- `appendices/K_integrated_ditl_detail.tex`
- `config/science/README.md`
- `config/science/science_record_v3.json`
- `config/science/science_record_v3.schema.json`
- `docs/audit/CLAIM_TRACEABILITY.md`
- `docs/audit/GS_19K2_LINK_CLOSURE.md`
- `docs/audit/GS_PASS_CAPACITY_VALIDATION.md`
- `docs/audit/IMPLEMENTATION_CHANGELOG.md`
- `docs/audit/OBC_RAM_FLASH_SIZING.md`
- `docs/audit/REMAINING_OPEN_DECISIONS.md`
- `docs/audit/SCIENCE_RECORD_V3.md`
- `docs/audit/STATUS_MARKER_CODEBOOK.md`
- `docs/audit/STORAGE_BACKLOG_VALIDATION.md`
- `docs/audit/TELEMETRY_MCR_CHANGELOG.md`
- `docs/audit/TIER_RECORD_GENERATION.md`
- `output/pdf/ANTARA_MCR_TELEMETRY_V3_2026-11-09.pdf`
- `scripts/complete_telemetry_budget.py`
- `scripts/plot_telemetry_budget.py`
- `scripts/science_record_v3.py`
- `scripts/validate_telemetry_budget.py`
- `sections/03_spacecraft_architecture.tex`
- `sections/04_simulations.tex`
- `sections/05_feasibility_and_budgets.tex`
- `tests/test_science_record_v3.py`

All derived files are enumerated individually in `data/derived/telemetry_v3_2026-11-09/changed_files.json`; these include9release ledgers,9per-service queue ledgers,3tier segment tables, per-contact/daily capacities, outage and memory tables, source/verification manifests and two figures. This list distinguishes this task from preserved pre-existing geometric-factor and thermal work.

## MCR figures and claims

Tables18–19 define the record/status;29–31 cover grid/tier/memory;33 covers historical capacity. Figure11 shows daily visibility/Relay capacity; Figure15 shows bounded startup queue sensitivity. PDF pages17,21–22,32–33,46–50,67 carry the principal changes; source labels are the stable identifiers. The report preserves AppendixA.1–A.6. No mission-success percentage, empirical compression ratio, actualADC rate, guaranteedRAM/flash sufficiency or qualified net throughput was invented.
