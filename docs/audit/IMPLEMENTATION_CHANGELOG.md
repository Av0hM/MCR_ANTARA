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
