> **Current-baseline supersession (2026-11-04):** Use [FPDU_APPROVED_BASELINE.md](FPDU_APPROVED_BASELINE.md), [2029_AUDIT_RECONCILIATION.md](2029_AUDIT_RECONCILIATION.md) and [REMAINING_OPEN_DECISIONS.md](REMAINING_OPEN_DECISIONS.md). The record below is retained as historical audit evidence. Silicon is removed, rear detection optional, main blocks longitudinal along X, eleven SiPMs on ±Y/main plus front, Teflon 0.11 mm per ±Z face. Coincidence references are 200/250/300 ns, shaping 20 ns, qualified dead time unknown. Optical isolation remains open. Earlier 20 ns coincidence/dead-time guesses and unresolved coating-thickness interpretation are superseded.

# FPDU baseline update changelog — 2026-11-04

## Scope and source of truth

The user authorized a payload documentation/configuration update after the initial audit. The current narrative specification is **Appendix A.2**, not a second standalone payload specification. `FPDU-2026-11-04` is a dated input revision, not a claimed formally approved hardware Rev. 2.2. Authoritative user inputs and the subsequent timing clarification take precedence over the historical Rev. 2.1 design description. The preceding audit documents remain dated snapshots with follow-up pointers.

The supplied **PRELIMINARY ESTIMATE is 400 Hz peak proton count rate under protons-only incidence, 250 µm (0.25 mm) aluminium shielding, assumed geometric factor 1 cm² sr and assumed 100% detection efficiency**. Its simulation, input spectrum and calculation remain unidentified. No all-particle trigger limit or demonstrated performance is inferred.

The user follow-up identifies current coincidence time as 20 ns, and suggests dead time may also be 20 ns. The update records the former as a current **CONFIRMED DESIGN INPUT**, the latter as tentative **REQUIRES VALIDATION**, with qualified dead time null. It does not sum shaping and ADC intervals or infer processing budget from the coincidence window.

## Exact file changes

| File | Change / reason |
|---|---|
| `sections/03_spacecraft_architecture.tex` | Updated scientific-payload subsection only: dimensions, Teflon, EJ-550, retained silicon/rear sensors, conditional rate with all assumptions, timing clarification and MCU/FPGA trade. |
| `appendices/B_payload_detail_visual.tex` | Updated canonical payload specification; geometry/material-volume table, dimensioned component diagram, signal chain, timing-budget table, conditional rate, units-correct count integral, validation limits and open decisions. Historical five-layer and Rev. 2.1 evidence explicitly separated. |
| `appendices/C_simulation_provenance.tex` | Added payload configuration/response compatibility paragraph. Wrapped one existing source path with `\path` to eliminate overflow on the affected provenance page; no numerical table edits. |
| `appendices/L_new_evidence.tex` | Reconciled the October single-block description with the November user update, preserving all non-payload claims. |
| `REVISION_NOTES_2029.md` | Added dated payload follow-up and audit/configuration pointers. |
| `config/payload/fpdu_2026-11-04.json` | Added versioned declarative geometry, rate assumptions/provenance, optics, timing and unknowns; no simulation adapter. |
| `config/payload/fpdu_2026-11-04.schema.json` | Added exact JSON Schema `const` contract for immutable input revision; unknowns cannot be silently assigned. |
| `config/payload/README.md` | Documents configuration ownership, null semantics, units, validation commands and non-consumption by existing models. |
| `scripts/validate_payload_config.py` | Dependency-free contract validator, material-volume calculator and fail-closed response-binding guard; no physics response function. |
| `tests/test_payload_config.py` | Nine bounded input/unit/label/compatibility tests, including distinction between confirmed coincidence and tentative dead time. |
| `tests/test_payload_legacy_accounting.py` | Three optional tests of unchanged legacy expected-count arithmetic: zero dead time, conservative merge/packet accumulation and exposure scaling. |
| `docs/audit/MODEL_REGISTRY.md` | Added dated current-input registry and pointer; original audit tables retained as snapshot. |
| `docs/audit/PAYLOAD_AUDIT.md` | Added follow-up pointer without erasing original findings. |
| `docs/audit/MCR_CLAIM_AUDIT.md` | Added follow-up pointer; documentation correction does not assert closure of physical validation findings. |
| `docs/audit/PAYLOAD_OPEN_DECISIONS.md` | Decision owners/evidence, timing clarification and proposed engineering sequence. |
| `docs/audit/PAYLOAD_SIMULATION_COMPATIBILITY.md` | Source-specific compatibility dispositions, missing physical interfaces and bounded future hardware/firmware verification procedures. |
| `docs/audit/PAYLOAD_UPDATE_CHANGELOG.md` | This change and verification record. |
| `output/pdf/ANTARA_MCR_FPDU_2026-11-04.pdf` | New complete compiled MCR; original tracked `main.pdf` preserved. Output directory is ignored by existing Git rules; artifact is available locally. |

No sibling simulation source, numerical CSV/figure, original PDF, RAAN, EPS, CONOPS, thermal, lifetime or grid-cell model was modified. SHA-256 comparison against the pre-edit snapshot confirmed all sibling Python source files and original tracked numerical/PDF/figure artifacts unchanged. The only pre-existing tracked file changes are the first five rows above; audit documents were already untracked at task start.

## Verification executed

| Check | Result and scope |
|---|---|
| `python3 scripts/validate_payload_config.py` | PASS. Main each 504 mm³; five main 2520 mm³; front 72 mm³; total 2592 mm³ =2.592 cm³. Material only, no packaging assumption. |
| `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v` | 9 passed, 3 explicitly skipped without optional legacy environment. Last run after final LaTeX edits passed. |
| Same unittest discovery with `ANTARA_LEGACY_SRC=/tmp/antara-payload-update/legacy/src` and `/home/sammo/miniconda3/envs/orekit_env/bin/python` | **12 passed**, including the three optional legacy arithmetic tests. No propagation in those tests. |
| Existing sibling `tests/test_execution_integrity.py`, selected `payload_per_bin_uncertainty_and_merge_accounting` and `payload_accumulation_and_final_flush` | **2 passed, 15 deselected**, 8.56 s. Source/test copy in `/tmp`; the latter uses a six-second horizon. A 90-second timeout bounded execution. 3448 dependency deprecation warnings (Orekit/JCC import wrappers), no test failures. |
| `latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=/tmp/antara-payload-update/latex main.tex` | PASS; complete **63-page PDF** (7 front-matter pages plus numbered 1–56). No undefined cross-references. |
| PDF visual review | Rendered and inspected all payload appendix pages (numbered 19–23), spacecraft payload pages (9–10), changed provenance pages (24,27) and reporting-baseline page (53). Fixed initial signal-label collision; diagrams and tables fit. Latest revised diagram re-rendered after final wording change. |
| Appendix numbering | Aux labels confirm operational logic A.1, payload A.2, provenance A.3, thermal A.4, budgets A.5, orbit/RF A.6. |
| `git diff --check` and preservation hashes | PASS; no whitespace errors or unintended tracked/source changes. |

Tests used an isolated copy of sibling `src/` and the selected existing test file. Existing Orekit data were linked read-only for the six-second fixture; `SPACEPY` and `MPLCONFIGDIR` pointed into `/tmp`, and bytecode/cache writing was disabled. No annual simulation, transport Monte Carlo or output regeneration was launched. Source code and test outcomes must not be mistaken for flight performance.

Remaining compilation warnings are inherited: two long source-path overflows in unchanged thermal/budget appendix text, Latin Modern bold-math font substitutions, underfull boxes and a duplicate `page.1` PDF destination from existing front-matter numbering. The build succeeds; these unrelated formatting warnings were not treated as payload qualification or expanded into a report-wide redesign.

Final PDF SHA-256: `d1905c2538b9fe02057eb059a3309cb0d08252306d34ee605a118673d9a3295e`.

## Figures, tables and claim changes

- Figure 4 is now a dimensioned main-block/front-piece concept, explicitly not an assembly or common-scale drawing. It shows no invented coated-face orientation.
- Figure 5 now shows the proposed scintillator → SiPM → ASIC → ADC → MCU/FPGA → classification/binning chain.
- Tables 14–16 cover geometry/retained interfaces, distinct timing terms and required validation evidence.
- The main payload description and Appendix A.2 contain the fully qualified rate statement; numerical outputs and response curves remain unchanged.
- The old response-integral statement was changed from a rate-like expression labeled counts to an explicitly time-integrated expected-count expression with directional effective area, flux units and live fraction. This is a dimensional documentation correction, not a calibrated response model.
- The silicon entrance and rear penetration tag, 5–100 MeV measurement requirement, mixed-field validation plan and provisional histogram concept remain. Fixed FPGA preference, fixed two/four-side readout and single-block mechanics are not asserted for the new geometry.

## Contradictions and next engineering work

Confirmed source mismatches: old L1–L5 geometry versus supplied blocks; old fixed FPGA language versus conditional MCU/FPGA choice; old ideal 0.314 cm² sr acceptance versus the separately assumed rate-estimate geometric factor; and multiple unrelated historical timing settings. The relationship between one optical assembly and five mechanical blocks is **unresolved**, not a confirmed physical contradiction. Shared-versus-per-bin dead-time suitability remains a suspected model issue pending hardware topology.

First freeze CAD/material/optical/channel interfaces, then recover rate provenance and timing definitions. Next test candidate timing/throughput/buffering with agreed margins, validate geometry-matched transport/optics/electronics and event reconstruction, and only then connect response-qualified histograms, telemetry and power to mission simulations. The [open-decisions register](PAYLOAD_OPEN_DECISIONS.md) assigns closure evidence; the [compatibility review](PAYLOAD_SIMULATION_COMPATIBILITY.md) specifies bounded tests and explicitly identifies tests that cannot yet be executed.
