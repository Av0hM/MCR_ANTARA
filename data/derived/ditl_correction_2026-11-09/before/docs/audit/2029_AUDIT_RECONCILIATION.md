# 2029 audit reconciliation

Authority: unified master instruction, 2026-11-04. The local MCR checkout is the report repository. `../ANTARA_CODES-main` is the authoritative simulation source; its AGENTS.md selects Science DITL and excludes Master from further development. No current FPDU custom CAD/ICD or geometry-matched response was recovered.

## Discovery and preservation

MCR branch `master`; simulator branch `main`. Existing tracked MCR modifications: `REVISION_NOTES_2029.md`, `appendices/B_payload_detail_visual.tex`, `appendices/C_simulation_provenance.tex`, `appendices/L_new_evidence.tex`, `sections/03_spacecraft_architecture.tex`. Existing untracked config/data/docs/output/scripts/tests were retained. Simulator already had modified helper configuration, pointing budget and MCR power source; their differences were snapshotted before work. No reset, commit, checkout or branch creation was attempted because Git metadata and the sibling source are outside writable permissions. Source corrections are delivered as an unapplied patch against the inspected dirty working tree, not HEAD alone.

The original seven audits and payload/count-rate follow-ups were reviewed. Scope includes actual source layouts, legacy/PDR archives, raw 22-file radiation evidence, current configurations/tests and active MCR inclusion graph. Similar filenames were not presumed equivalent. Existing raw data, earlier configuration revisions and scientific numerical outputs remain unchanged.

## Epoch reconciliation

| Evidence | Actual inspected identity | Permitted interpretation |
|---|---|---|
| Approved mission | `config/mission/antara_2029.json`, UTC 2029-01-01 | Current design/runtime-override contract, not a completed run |
| Science default | `S:src/simulations/helper/antara_models.py:83–85`, March 2000 | Cannot label an unknown run 2029 from report date |
| Local MCR runtime | `S:src/simulations/power/ANTARA_MCR.py:537`, January 2026 | Latest supplied RAAN CSVs are team-accepted 2029 planning references; generating epoch unverified |
| Raw AP9/AE9 maps | All records MJD 61041, 600 km | 2026-01-01 source; approved provisional 2029 planning input |
| Anisotropy source | AP8 UP-MAX, January 2028, different orbit/directional settings | Separate study; not AP9/AE9 current-response validation |
| Annual-named Science telemetry | Ends near day 50; no terminal row | Partial historical evidence, not annual validation |

No ephemeris/environment/backend/run manifest was recovered that independently closes all 2029 identities. The team's acceptance does not require relabeling historical data. A manifest and a bounded runtime verification remain prerequisites for an epoch-calibrated claim; no long run was launched.

## Issue-by-issue disposition

Source line references and original consequences are retained in `ISSUES.md`; statuses below supersede its pre-implementation review gate.

| ID | Current state | Evidence / remaining work |
|---|---|---|
| A01 | PARTIALLY RESOLVED | Approved polygon replaces contradictory rectangle; exact 92/2020/7940 counts and 7940-cell key sets tested. Science eligibility/independence still open. |
| A02 | STILL VALID | Tier-classification generator/response/temporal manifest unavailable; Primary Map labels not accepted as compliance. |
| A03 | SUPERSEDED | Latest six-scintillator/11-SiPM geometry supersedes single-block Rev. 2.1 and retained silicon. No response qualified; compatibility rejection tested. |
| A04 | PARTIALLY RESOLVED | Historical rate sums explicitly withdrawn in MCR; rate×bin-width×time reference contract tested. Historical archive preserved, not silently repaired. |
| A05 | PARTIALLY RESOLVED | Failing source regression reproduced; tested patch exports spectral density, removes dimensionally invalid Hz/dead-time diagnostic. Authoritative sibling not patched. |
| A06 | BLOCKED BY DESIGN DECISION | Shared versus per-channel trigger topology and qualified dead time unknown. Shared-chain hypothesis and bin-invariance tests only. |
| A07 | PARTIALLY RESOLVED | Reference VisitAccounting distinguishes visit and regional-passage identity; repeated samples tested. Legacy private source counter still increments samples; integration/migration outstanding. |
| A08 | PARTIALLY RESOLVED | Reference checkpoint identity requires epoch/grid/dt/response/input hashes/state shapes and rejects mismatch. Archived grid loader unchanged; full integration/split-run validation pending. |
| A09 | PARTIALLY RESOLVED | Independent ingestion rejects duplicate/malformed/missing-aligned rows; exact approved domain now tested. Original archive conversion scripts preserved with known limitations. |
| A10 | PARTIALLY RESOLVED | 62.7% relabeled detection-conditional sample fraction; interval accounting contract tested. Historical full time-weighted science duty not reconstructed or invented. |
| A11 | STILL VALID | Local annual artifact incomplete; terminal/horizon checks tested. No annual rerun or full-year validation claimed. |
| A12 | PARTIALLY RESOLVED | Source failure reproduced and patch separates mean run-minimum/worst minimum, retains every RAAN statistics group. MCR labels corrected; patch unapplied. |
| A13 | STILL VALID | Two-run z interval cannot establish reliability/99% coverage. No new sampling model or fabricated draws. |
| A14 | PARTIALLY RESOLVED | Source full-battery failure reproduced; accepted-energy throughput patch and boundary tests pass. No aging-physics change; patch unapplied. |
| A15 | STILL VALID | Panel/attitude/degradation configurations remain distinct; no unrelated EPS geometry changed. |
| A16 | STILL VALID | Censored endpoint and radial/ellipsoidal definitions retained; operational lifetime/cutoff/reentry distinguished. |
| A17 | RESOLVED AND TESTED | Prior independent raw grouping reproduced two-run pooling; incorrect >8000 impossibility sentence corrected. Classifier approximation remains explicit. |
| A18 | SUPERSEDED | Legacy rear-veto/first-bin event-label defects do not define new optional rear architecture. Historical code preserved, not claimed repaired; new classifier blocked by response design. |
| A19 | PARTIALLY RESOLVED | Patch adds effective merged intervals and inactive-slot metadata; reference merging conserves counts/widths; background/zero tests avoid fake precision. Legacy sigma proxy remains unqualified. |
| A20 | BLOCKED BY DESIGN DECISION | Geometry-only yields cannot qualify science. Need response, eligibility, independence, pointing/live exposure and data-return contracts. |
| A21 | STILL VALID | Old last-hit-layer stopping proxy not corrected or reused; endpoint/escape scoring required in new transport. |
| A22 | STILL VALID | Historical global/container-dose interpretation remains invalid for sensitive-volume qualification; transport scoring requires revision. |
| A23 | SUPERSEDED | Historical packet-count assumptions not current telemetry. New logical schema has no invented encoding/cadence; historical delivered/generated mismatch remains documented. |
| A24 | PARTIALLY RESOLVED | Current evidence table now concrete; claim index and build checks added. External source artifacts and final subsystem tables remain incompletely sourced. |
| A25 | PARTIALLY RESOLVED | Repeated DITL fraction paragraph removed; current payload/silicon/timing replaced; historical appendix warnings retained. Old reports remain explicitly superseded evidence. |
| A26 | UNVERIFIED | No independently verified 2029 generating manifest recovered. Team acceptance of RAAN planning data preserved separately from source runtime epoch. |
| A27 | RESOLVED AND TESTED | Prior raw 18-event minimum 0.442496° replaces unsupported 5.4° minimum; no new slew simulation. |

## Boundary of completion

Local configurations, reference accounting contracts, tests and MCR corrections are implemented. The authoritative simulator patch is tested in isolation and delivered but **not applied**. Visit/checkpoint/telemetry reference interfaces still require simulator integration and historical checkpoint migration decisions. No calibrated response, actual electronics trigger upper bound, independent science eligibility or full mission-success result is claimed.
