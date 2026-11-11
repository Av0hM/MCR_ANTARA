# Approved FPDU implementation and MCR correction — 2026-11-04

## Outcome and limits

The MCR workspace now has one current approved payload pointer, explicit 2029 mission inputs, a logical 64-bin telemetry schema, tested accounting interfaces, a reconciled report and a compiled PDF. Original raw data and dated payload snapshots remain unchanged. No annual/multi-year simulation ran and no hardware performance was invented.

The authoritative simulator is the sibling `ANTARA_CODES-main` selected by its AGENTS.md. It is outside the writable workspace. Four targeted source corrections are supplied as a tested **unapplied patch**, not represented as deployed fixes. Production integration of visit/checkpoint/telemetry contracts and qualified detector response remains outstanding. Git metadata is read-only, so no branch, reset, commit or push was attempted.

## Phase record

| Phase | Accomplished | Tests / uncertainty |
|---|---|---|
| 0 discovery | Reviewed repository/source layouts, dirty state, audits, archived inputs and active report; preserved pre-existing identities | Source/epoch identities differ; no independently verified 2029 campaign manifest |
| 1 mission | `config/mission/antara_2029.json` with approved inputs and explicit source-epoch distinction | Configuration is not a completed simulation |
| 2 mechanics | New immutable approved-v2 config/schema and current pointer; geometry/axes/coating/readout updated | Arithmetic tests pass; material, optics and current CAD still open |
| 3 environment | Existing independent rate reproduction retained; exact polygon-domain equality added; MCR rate conditions reconciled | 22 files preserved; 7940 unique aligned cells; no shielding/accepted-trigger claim |
| 4 electronics | Separate timing fields, parameterized service/ADC/queue model, candidate trade | Unknown performance remains null; synthetic fixtures not devices |
| 5 reconstruction/data | Provisional log64 edges and logical record schema; typed counts, UTC/geodetic/quality metadata | Histogram/record tests pass; reconstruction and wire encoding unqualified |
| 6 geography/science | Explicit polygon, positive-area mask, interval visits and unique regional passages | Independent clipping/Shapely counts92/2020/7940; eligibility/independence definitions open |
| 7 software | Four source defects demonstrated and patched in disposable copy; reusable accounting/identity/background contracts added | 4 original failures→4 patch passes; 201 surrounding passes. Patch unapplied; integration gaps remain |
| 8 report | Payload diagrams/tables, source identity, count/coverage/SOC claims and historical warnings corrected; blank registers replaced | Complete XeLaTeX build and visual review; A.1–A.6 retained |
| 9 acceptance | All local tests, source regressions, independent polygon/reference/preservation checks | 74 local +4 patch +201 surrounding passes; no physical qualification inferred |
| 10 handoff | Final PDF, exact change list, traceability/supersession, patch hashes and validation logs | Remaining PDR decisions and production integration explicitly recorded |

## Executed commands and results

From this MCR checkout (absolute environment used; no packages installed):

```sh
ANTARA_LEGACY_SRC=/tmp/antara-master-implementation/simulator/src \
 SPACEPY=/tmp/antara-master-implementation \
 MPLCONFIGDIR=/tmp/antara-master-implementation/mpl PYTHONDONTWRITEBYTECODE=1 \
 /home/sammo/miniconda3/envs/orekit_env/bin/python -m unittest discover -s tests -v
```

**74 passed, 0 failed, 0 skipped.** Without `ANTARA_LEGACY_SRC`, three optional historical-model tests intentionally skip. The 74 include independent raw-spectrum/rate reproduction, threshold/interpolation/unit/duplicate/missing/extreme cases, geometry/timing contracts, conservation, visits, checkpoints, completeness, background and logical science records. An initial documentation-string assertion failed on LaTeX spacing and was corrected to match the actual table; no numerical tolerance was weakened.

```sh
ANTARA_SOURCE_ROOT=/home/sammo/Desktop/Projects/ANTARA_CODES-main \
 PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python \
 patches/simulation/test_accounting_patch.py

ANTARA_SOURCE_ROOT=/tmp/antara-master-implementation/simulator \
 PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python \
 patches/simulation/test_accounting_patch.py
```

**Original: 4 failures (expected red tests). Patched: 4 passes.** Test scope: differential-rate diagnostic, full-battery curtailment, all-RAAN/extreme-SOC summary structure and effective merged-bin metadata. AST extraction avoids top-level expensive campaign execution. Patch/source hashes are in `patches/simulation/source_identity.json`.

```sh
SPACEPY=/tmp/antara-master-implementation PYTHONDONTWRITEBYTECODE=1 \
 PYTHONPATH=/tmp/antara-master-implementation/simulator/src \
 MPLCONFIGDIR=/tmp/antara-master-implementation/mpl \
 timeout 180 /home/sammo/miniconda3/envs/orekit_env/bin/python -m pytest -q -p no:cacheprovider \
 /tmp/antara-master-implementation/simulator/tests/test_audit_repairs.py \
 /tmp/antara-master-implementation/simulator/tests/test_scientific_integrity.py \
 /tmp/antara-master-implementation/simulator/tests/test_telemetry_integrity.py \
 /tmp/antara-master-implementation/simulator/tests/test_pass_statistics.py \
 /tmp/antara-master-implementation/simulator/tests/test_slew_profile.py
```

**201 passed, 0 failed, 3448 warnings**, predominantly existing Java-wrapper deprecations. Initial run: 188 passed/13 failed because copied checkout lacked Orekit data; read-only linking of existing data corrected the environment, without source changes.

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error \
 -outdir=/tmp/antara-master-implementation/latex main.tex
git diff --check
```

Full build succeeds: **62 pages**. Active inclusion graph:20 files, zero unresolved explicit references, zero duplicate labels, zero overfull boxes. Remaining warnings are bold-math font substitution and underfull justification. Whole-report contact sheets and enlarged changed payload/closure pages were inspected; cross-section label collisions and orphaned closure text were corrected. Title-page anchor duplication was fixed. Final artifact: `output/pdf/ANTARA_MCR_APPROVED_FPDU_2026-11-04.pdf`; original PDFs preserved.

Independent Shapely polygon validity/closure and every candidate grid-cell intersection agree exactly with the dependency-free clipping implementation:92/2020/7940. Both raw rate-map key sets equal the7940-cell mask. SHA-256 comparison confirms **38 protected pre-existing files**, including all22 raw inputs, original figures/PDFs and immutable configs, unchanged. The sibling's pre-existing diff is byte-identical to its initial snapshot.

## Output semantics and scientific boundaries

The patch replaces an environment diagnostic mislabeled Hz with Hz/MeV density; it does not invent integration widths. Effective merged intervals are added alongside legacy fixed slots. Battery throughput excludes curtailed/unserved energy, and RAAN output distinguishes mean minima from actual worst minima while retaining each RAAN. See patch README for consumer migration. Historical outputs were not recalculated or overwritten.

New accounting functions require explicit units, bin-average spectra, durations and model hypotheses. They do not connect old five-layer efficiencies to the revised geometry. The reference visit counter does not define statistical independence. Checkpoint identity validation is a tested contract, not a claim that the archived loader has been fixed. Unknown response IDs are rejected.

## MCR figures, tables and superseded claims

Appendix A.2 now contains a dimensioned longitudinal assembly, correctly oriented YZ cross-section, optical interfaces and signal/data-flow diagram; geometry, timing, rate and telemetry tables carry source/qualification context. Section3 uses the same baseline. Section1 adopts the approved polygon while retaining all quantitative science thresholds. Sections4 and source appendices distinguish conditional samples, pooled orbits, mean run-minimum SOC, invalid historical rate sums and incomplete annual evidence. Historical silicon/CMG designs are explicitly labeled. Empty draft tables/heading were replaced by concrete registers and PDR gates.

`CLAIM_TRACEABILITY.md` maps numerical claims to actual sources and records superseded statements. `2029_AUDIT_RECONCILIATION.md` classifies every A01–A27 issue. Remaining decisions and the proposed engineering sequence are in `REMAINING_OPEN_DECISIONS.md`; no new mission-success percentage is asserted.

## Exact files changed in this implementation

The following inventory compares against the pre-implementation file-hash snapshot, so it includes new/untracked deliverables rather than only Git-tracked diffs. Earlier unrelated working-tree changes are not attributed to this implementation. Generated validation logs are audit evidence, not replacement simulation outputs.

| File | Change | Reason |
|---|---|---|
| `README.md` | modified | Correct active structure/build instructions and link current inputs, patch and audits. |
| `REVISION_NOTES_2029.md` | modified | Prepend current supersession while retaining prior revision notes. |
| `appendices/B_payload_detail_visual.tex` | modified | Current geometry, three TikZ views/flow, optics, timing, rates, telemetry and response gates. |
| `appendices/C_simulation_provenance.tex` | modified | Replace empty evidence table and old timing with concrete source identities/limits. |
| `appendices/D_thermal_structural_details.tex` | modified | Line-breakable source path only; no thermal model or value changed. |
| `appendices/F_orbit_rf_support.tex` | modified | Correct two-run pooling and polygon interpretation; wrap long path. |
| `appendices/G_source_detail.tex` | modified | Replace placeholder-only mission register with approved inputs and review gates. |
| `appendices/H_source_detail.tex` | modified | Explicit local historical warnings for silicon/five-layer/CMG descriptions. |
| `appendices/I_source_detail.tex` | modified | Withdraw invalid count claim, fix slew minimum and annual label, remove duplicate/empty text. |
| `appendices/J_source_detail.tex` | modified | Replace placeholder-only tables with concrete budget evidence and PDR conditions. |
| `appendices/L_new_evidence.tex` | modified | Reconcile polygon domain, current payload and accepted 2029 planning references. |
| `appendices/M_updated_raan_drag_study.tex` | modified | Correct mean-of-run-minima labels; original numerical values retained. |
| `config/mission/antara_2029.json` | new | Versioned current input/schema/pointer and explicit open fields; immutable older revision preserved. |
| `config/payload/README.md` | modified | Versioned current input/schema/pointer and explicit open fields; immutable older revision preserved. |
| `config/payload/current.json` | new | Versioned current input/schema/pointer and explicit open fields; immutable older revision preserved. |
| `config/payload/fpdu_2026-11-04-approved-v2.json` | new | Versioned current input/schema/pointer and explicit open fields; immutable older revision preserved. |
| `config/payload/fpdu_2026-11-04-approved-v2.schema.json` | new | Versioned current input/schema/pointer and explicit open fields; immutable older revision preserved. |
| `config/science/fpdu_histogram_v1.schema.json` | new | Versioned current input/schema/pointer and explicit open fields; immutable older revision preserved. |
| `config/science/saa_polygon_v1.json` | new | Versioned current input/schema/pointer and explicit open fields; immutable older revision preserved. |
| `docs/audit/2029_AUDIT_RECONCILIATION.md` | new | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/AP9_AE9_COUNT_RATE_VALIDATION.md` | modified | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/CLAIM_TRACEABILITY.md` | new | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/COUNT_RATE_EVIDENCE_INGESTION.md` | modified | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/COUNT_RATE_MCR_RECOMMENDATIONS.md` | modified | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/FPDU_APPROVED_BASELINE.md` | new | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/FPDU_COUNT_RATE_RECONCILIATION.md` | new | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/FPDU_ELECTRONICS_TIMING_TRADE.md` | new | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/FPDU_GEOMETRY_VALIDATION.md` | new | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/FPDU_RESPONSE_VALIDATION_PLAN.md` | new | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/IMPLEMENTATION_CHANGELOG.md` | new | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/MCR_CLAIM_AUDIT.md` | modified | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/MODEL_REGISTRY.md` | modified | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/PAYLOAD_AUDIT.md` | modified | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/PAYLOAD_OPEN_DECISIONS.md` | modified | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/PAYLOAD_SIMULATION_COMPATIBILITY.md` | modified | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/PAYLOAD_UPDATE_CHANGELOG.md` | modified | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/REMAINING_OPEN_DECISIONS.md` | new | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/SAA_POLYGON_AND_COVERAGE_CONTRACT.md` | new | Current reconciliation/validation/decision record or supersession pointer preserving prior audit. |
| `docs/audit/validation/2026-11-04-approved-v2/changed_files.json` | new | Persist bounded test/build/preservation evidence and change inventory. |
| `docs/audit/validation/2026-11-04-approved-v2/latex-build.log` | new | Persist bounded test/build/preservation evidence and change inventory. |
| `docs/audit/validation/2026-11-04-approved-v2/local-tests.log` | new | Persist bounded test/build/preservation evidence and change inventory. |
| `docs/audit/validation/2026-11-04-approved-v2/original-defect-results.txt` | new | Persist bounded test/build/preservation evidence and change inventory. |
| `docs/audit/validation/2026-11-04-approved-v2/patch-tests.log` | new | Persist bounded test/build/preservation evidence and change inventory. |
| `docs/audit/validation/2026-11-04-approved-v2/polygon-independent.json` | new | Persist bounded test/build/preservation evidence and change inventory. |
| `docs/audit/validation/2026-11-04-approved-v2/simulator-surrounding-tests.log` | new | Persist bounded test/build/preservation evidence and change inventory. |
| `docs/audit/validation/2026-11-04-approved-v2/summary.json` | new | Persist bounded test/build/preservation evidence and change inventory. |
| `main.tex` | modified | Preserve appendix structure; fix title-page PDF anchor and historical-material notice. |
| `output/pdf/ANTARA_MCR_APPROVED_FPDU_2026-11-04.pdf` | new | New complete compiled MCR; earlier PDFs preserved. |
| `patches/simulation/README.md` | new | Tested unapplied source correction, reproduction test, source hashes or application limits. |
| `patches/simulation/approved_baseline_accounting.patch` | new | Tested unapplied source correction, reproduction test, source hashes or application limits. |
| `patches/simulation/source_identity.json` | new | Tested unapplied source correction, reproduction test, source hashes or application limits. |
| `patches/simulation/test_accounting_patch.py` | new | Tested unapplied source correction, reproduction test, source hashes or application limits. |
| `scripts/fpdu_contracts.py` | new | Bounded unit/conservation/coverage/timing/record interfaces; no fabricated detector response. |
| `scripts/validate_payload_config.py` | modified | Default CLI to current pointer; explicit old file remains labeled superseded. |
| `sections/01_mission_context.tex` | modified | Replace contradictory rectangle with approved polygon; retain science thresholds. |
| `sections/03_spacecraft_architecture.tex` | modified | Synchronize main-body payload geometry/timing and conditional rate statements. |
| `sections/04_simulations.tex` | modified | Correct conditional-duty and mean-minimum-SOC semantics and planning-epoch qualification. |
| `tests/test_fpdu_contracts.py` | new | Focused current contract regressions and explicit historical-snapshot test labeling. |
| `tests/test_fpdu_record.py` | new | Focused current contract regressions and explicit historical-snapshot test labeling. |
| `tests/test_payload_config.py` | modified | Focused current contract regressions and explicit historical-snapshot test labeling. |

Machine-readable hashes: `validation/2026-11-04-approved-v2/changed_files.json`. Test/build totals and final PDF hash: `validation/2026-11-04-approved-v2/summary.json`.


## Simulation-evidence integration — 2026-11-09 (latest scope)

The user's final direction excludes incomplete 24h-labelled scenarios from the MCR comparison. Operational evidence uses only `leop_1yr`, explicitly incomplete at 4,320,020 seconds; its separate nearly year-long event exports are inconsistent even over the shared horizon. One-hour analysis and figures remain audit-only, not adopted report results. Thermal and detumble remain separate studies. No new simulation campaign or external simulator edit was performed.

### Phase outcomes

| Phase | Result and remaining limit |
|---|---|
| 0 inventory | 48 original files hashed and preserved; producing commits/runtime manifests remain unknown. Candidate current source hashes are references, not provenance proof. |
| 1 scenario comparison | Both 24h-labelled files contain one hour; calculations retained for audit, comparison excluded at user direction. |
| 2 integrated science | Continuous annual-labelled telemetry audited through day 50 + 20 s, no terminal snapshot. Rate/count sums and storage balance checked; legacy detector predictions do not qualify current FPDU. Event exports conflict. |
| 3 thermal | Seven-node 24h-labelled history reproduced; summary hot/cold columns are extrema of this same history. No independent hot/cold campaigns or selected-component margins established. |
| 4 detumble | 16,133/50,000 reported convergences; 33,867 infinite completion values preserved. Nonzero initial acceleration conflicts with current source; historical model identity unresolved. |
| 5 consistency | No combined unconditional feasibility margin; source epochs, independent thermal loads and obsolete detector response remain explicit. |
| 6–7 MCR/graphics | Existing sections 3–5 and appendices A.1/A.3/A.4/A.5/F updated, geometric-factor results and A.1–A.6 hierarchy preserved. Reproducible figures and provenance added. |
| 8 verification | 136 tests passed, 3 skipped, 16 subtests passed; complete 71-page XeLaTeX build. Changed tables/figures visually inspected. No overfull boxes or undefined references; font substitutions and underfull justification remain. |

### Exact commands and results

```sh
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python scripts/validate_simulation_evidence.py
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python -c 'from scripts.validate_simulation_evidence import write_comparisons; write_comparisons()'
MPLCONFIGDIR=/tmp/antara-evidence-20261109/mpl PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python scripts/plot_simulation_evidence.py
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python -m pytest -q -p no:cacheprovider tests
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=/tmp/antara-evidence-20261109/latex main.tex
git diff --check
```

The outdir preserves the pre-existing dirty root `main.pdf`. The final PDF is `output/pdf/ANTARA_MCR_SIMULATION_EVIDENCE_2026-11-09.pdf`; previous approved/geometric-factor PDFs remain unchanged. Test/build logs and final PDF hash are in `evidence/science-ditl/validation/`. Three skips concern optional historical-model source availability; no skips are represented as passes. Initial CSV-vector parsing was corrected to accept recorded whitespace-separated numeric arrays without evaluation; the final suite passes.

### Exact file scope

The complete machine-readable file list is `evidence/science-ditl/validation/changed_files.json`, including derived CSV/JSON/PNG artifacts. Source edits: README; sections 03/04/05; appendices A/C/D/E/K/L; claim traceability/open-decisions/this changelog; two analysis/plot scripts; one test module; six new evidence audits. Original raw files and original figures are excluded from the changed-file list. Pre-existing edits to section 01, appendix B, root PDF and geometric-factor artifacts were preserved. Git metadata was not changed.

### Review disposition

The report supports a conditional concept discussion, not closure of annual operational feasibility, current-FPDU science success, thermal compliance or ADCS reliability. Blocking evidence gaps are reconciled annual telemetry/event provenance and current detector response. PDR work includes selected thermal component limits, integrated heat schedules, reproducible detumble initial conditions/controller/timeout, packet/link accounting and hardware tests. Full paired 24h runs are no longer a prerequisite for this scoped integration.


## Telemetry v3 / science memory / full19.2kbps — 2026-11-09

Completed the scoped reference codec, source-identified data-budget analysis, conditional queue/memory trade and MCR update. Exact phase/file/command record: `TELEMETRY_MCR_CHANGELOG.md`; source hashes and ledgers: `data/derived/telemetry_v3_2026-11-09/`.173 tests passed,3 skipped,16subtests passed;74-page XeLaTeX PDF visually reviewed with zero overfull boxes/undefined references. No arbitrary minimum reading duration/count or link derating. Valid zero-count records retained. Annual visibility585638400bytes is separate from Relay opportunity428836800bytes and actual historical transfer; dates remain2000. No full-year simulation or external source modification.128MiB is conditional rolling storage, not enough to archive the187498164-byte three-reading grid sensitivity without delivery. Detailed RF qualification and sustained current-FPDU generation remain open.

## Section 3 subsystem feasibility requirements — 2026-11-09

### Discovery, implementation and reconciliation

Preserved the nine active Section 3 headings and all original technical paragraphs. Added nine requirement-table groups and subsystem feasibility assessments, backed by one versioned register containing 51 unique obligations. SDM/deployables remain under the existing thermal/structural heading; frames/time/ICD remain under the existing coordinate-system heading. No mission criteria, appendices, physical models, source datasets or simulator outputs were changed. Existing uncommitted work and root `main.pdf` were preserved; Git metadata was not changed.

Statuses: 4 SUPPORTED within limited model/software/documented-interface scope, 15 CONDITIONAL, 28 OPEN, 3 NOT EVALUATED, 1 NOT MET. The not-met item is the completeness/consistency obligation for supplied annual evidence, not a spacecraft performance failure. Thirty-two register rows flag concept-level closure gaps. The MSC all-operational-channel versus summary ≥4-channel wording remains explicitly unresolved without weakening either statement.

### Verification and presentation

Twelve new bounded tests cover traceability, unique IDs, preserved original prose/headings and baseline hashes, evidence paths, scoped status claims and unchanged mission constraints. Full regression: **185 passed, 3 skipped, 16 subtests passed**. Skips concern optional historical-source availability. No simulation campaign was run.

The complete **87-page** PDF was compiled with XeLaTeX/latexmk. All new Section 3 table pages (PDF pages 19–32), plus the opening page 18, were visually inspected. Continued table blocks use readable 10-point text and retain one table number per subsystem group. No overfull boxes, missing characters or undefined cross-references were reported. Existing font substitutions, underfull boxes and three ignored glue-shrinkage warnings in appendix longtables remain; these are not reported as a warning-free build.

Exact commands:

```sh
python3 scripts/render_section3_requirements.py
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python -m pytest -q -p no:cacheprovider tests
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=/tmp/antara-section3/latex main.tex
pdftotext -layout /tmp/antara-section3/latex/main.pdf /tmp/antara-section3/main.txt
pdftoppm -f 18 -l 32 -scale-to 1100 -png /tmp/antara-section3/latex/main.pdf /tmp/antara-section3/final
git diff --check
```

### Exact file scope and disposition

`data/derived/section3_requirements_2026-11-09/changed_files.json` lists every task file. The register, generator, nine LaTeX inputs, Section 3 source, twelve-test module and three new audit documents are the substantive implementation. Claim traceability, remaining decisions, this changelog and README are updated. Baseline snapshots, test/build logs and verification manifest accompany the new PDF at `output/pdf/ANTARA_MCR_SECTION3_REQUIREMENTS_2026-11-09.pdf`; older PDFs remain intact.

Concept-level blockers include current-FPDU response/effective acceptance and mixed-species throughput, science eligibility/independence, matched sustained data return, worst-case energy/reserve allocations, pointing/control authority, component thermal limits, complete mass and launch interfaces. PDR verification includes hardware timing, calibrated response, RF/net throughput, reset-safe storage, thermal correlation and structural/deployment tests. The report supports a conditional concept-review discussion, not unconditional subsystem compliance or mission-success closure.

## Authoritative DITL corrective migration — 2026-11-09

This entry supersedes earlier Science/DITL-dependent numerical findings and statuses in this changelog. Earlier records are retained as audit history. No original raw input, prior derived output or prior PDF was overwritten.

| Phase | Result / changed scope | Remaining uncertainty |
|---|---|---|
| 0–1 discovery | Found24CSV files in `evidence/new-science-ditl/`; inventoried headers, rows, timestamps, sizes and hashes; captured pre-edit dependency lines and snapshots. | No source/runtime manifest supplied. |
| 2 supersession | Added run registry, old-raw supersession notices and fail-loud guards on old analysis/plot entrypoints. | Old artifacts remain historical, not active evidence. |
| 3 validation | Day files reach86400s; annual31536000s; epoch2000-03-01; no duplicate/nonmonotonic timestamps. | Full timestamp span does not qualify unknown integrator, RAAN, hardware or interval semantics. |
| 4–6 recomputation | Recomputed all three runs; daily/annual mode, exposure, energy, battery, event, native data and contact results; regenerated8figures. | Annual telemetry15161 mode changes vs16283transition records; Slewing definitions differ. |
| 7 budgets | Time-aligned1/2/3-reading tier sensitivities, contact ledgers, queues, missed-contact and1/3/7-day outages, bitrate search. | Actual detector/timing/boundary and RF/net-throughput qualification remain open. |
| 8 dependencies | Old/new metric and figure migration maps; all annual event files are byte-identical, annual telemetry differs. | Independent grid/thermal/detumble/RAAN limitations are preserved. |
| 9–11 report/requirements | Corrected Sections3–5, A.1/A.3/A.5/A.6/F, source-detail archive and evidence appendix; revised11requirements' evidence. | OBC queue and annual evidence requirements are CONDITIONAL. |
| 12 tests |204passed,3skipped,16subtests passed; prior4-supported expectation failed after evidence reassessment and was corrected to the explicit3supported IDs. | Skips concern optional historical source availability; no hardware validation implied. |
| 13–15 build/review | Complete XeLaTeX build and visual inspection; exact final hash/pages/files recorded in verification manifest. | Existing font/underfull/glue-shrinkage warnings remain; no overfull boxes or undefined cross-references. |

### Quantitative correction

Annual acquisition gate changes342→247258s; recorded minimum battery15.21520→15.097556Wh; native science generation0.00492859→3.514083862sourceMB. The corrected annual visibility remains244016s over820contacts; Relay overlap remains178682s, or428836800ideal bytes. Those repeated values were independently recomputed from corrected-source files, not copied as authority. Preferred EMSC v3 volume changes67452→46637364bytes, nominal queue67452→75336bytes; the worst-start seven-day outage requires1010028bytes. The old unchanged-outage result is invalidated. The3-day outage already exceeds256KiB RAM.128MiB is a candidate nonvolatile allocation for this workload before reserves;16GB is optional. No current-FPDU science-success percentage is established.

### Commands and reproducibility

```sh
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python scripts/validate_corrected_ditl.py --inventory
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python scripts/validate_corrected_ditl.py --run leop_24h
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python scripts/validate_corrected_ditl.py --run no_leop_24h
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python scripts/validate_corrected_ditl.py --run leop_1yr
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python scripts/reconcile_corrected_ditl_events.py
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python scripts/complete_corrected_ditl_budget.py
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python scripts/render_corrected_ditl_report.py
MPLCONFIGDIR=/tmp/ditl-correction-mpl PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python scripts/plot_corrected_ditl.py
python3 scripts/render_section3_requirements.py
PYTHONDONTWRITEBYTECODE=1 /home/sammo/miniconda3/envs/orekit_env/bin/python -m pytest -q -p no:cacheprovider tests
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=/tmp/ditl-correction/latex main.tex
git diff --check
```

The annual command is CSV postprocessing only; no spacecraft simulation is launched. All numerical tables use full telemetry resolution; figure samples are display-only. The new epoch/configuration and timing distinctions are not silently normalized. The renderer regenerates core audit tables; signed-off interpretations and correction history are maintained in Markdown. Exact file scope, source preservation check, logs, figures and final PDF identity are in `data/derived/ditl_correction_2026-11-09/`. The old root PDF and all previous published snapshots remain intact.

## 2026-11-09 — A.1.2/A.1.3 operational interpretation

Expanded nominal startup/science/relay sequencing and supervisory fault/recovery prose at the user's request. Six explicitly proposed assumptions follow A.1.3, with evidence limits and verification needs. The 120 + 2460 = 2580 s startup reference is event-defined and not a flight deadline. Existing headings/diagrams are retained, with label-placement fixes. No raw data, simulator, mission threshold or hardware configuration changed. See `OPERATIONAL_SEQUENCE_ASSUMPTIONS.md` for exact file scope and verification. New reviewed PDF: `output/pdf/ANTARA_MCR_OPERATIONAL_ASSUMPTIONS_2026-11-09.pdf`; previous PDFs preserved.

## 2026-11-10 — Feasibility-focused dual-edition editorial revision

Rewrote Sections 2–5 around the existing analysis-supported feasibility findings and revised Section 1 presentation without changing approved science tables or requirements. Replaced subsystem verification matrices with three-column evidence/assessment tables, retained all 51 IDs, centralized PDR scope, and applied the annotated final-draft corrections. The corrected DITL source epoch is stated explicitly; detector, thermal, actuator, RF, mass and disposal constraints remain substantive. Both editions compile with XeLaTeX. See [full editorial change and validation record](FEASIBILITY_EDITORIAL_CHANGELOG_2026-11-10.md) for deliverables, deletion summary, unresolved issues and preservation checks.
