# Prioritized engineering findings and verification sequence

Audit date: 2026-11-02. Audit only; simulation code, input configurations, scientific results and MCR source were not changed.

**Source notation:** `R:` means this MCR repository; `S:` means `/home/sammo/Desktop/Projects/ANTARA_CODES-main/`; `P:` means the `PDR Sims/` member tree in `/home/sammo/Downloads/PDR Sims-20261021T072428Z-1-001.zip`; `D:` means the `MCR DATA/` member tree in `/home/sammo/Downloads/MCR DATA-20261021T072514Z-1-001.zip`; `G:` means `PROJECT_ANTARA/saa_sim/` inside `P:AbhishekSims/PROJECT_ANTARA.zip`. Archive members were read from disposable copies under `/tmp/antara-audit/`. Line numbers refer to the inspected working files/archive members, not an assumed common version. See [repository map](REPOSITORY_MAP.md) for scope and source identities.

**Evidence terms:** Confirmed = demonstrated by inspected code, file comparison or arithmetic. Suspected = plausible consequence needing a discriminating test. Unestablished = the producing inputs/revision or required validation were not recovered. A passing regression is not physical validation.


## Review gate

No implementation or MCR edits are included. Priorities: **P0** blocks mission-success/evidence acceptance; **P1** materially changes scientific or engineering interpretation; **P2** improves reproducibility/report clarity. Confirmed findings establish a defect or mismatch in the named artifact; they do not prove every historical output is affected. Suspected issues require the listed test before claiming a numerical bias.

| ID | Priority/status | Evidence (file:line) | Consequence | Proposed fix and discriminating verification |
|---|---|---|---|---|
| A01 | P0 confirmed mismatch | R:sections/01_mission_context.tex:163–164; P:grid_common.py:15–24 | Coverage denominator has incompatible longitude definitions | Approve explicit bounds/wrap/polygon/eligibility; exact grid cardinality and boundary/wrap tests at all resolutions |
| A02 | P0 confirmed missing provenance | R:appendices/L_new_evidence.tex:11–22; P:Simulation Outputs/18-Month Simulation/tier_disposition_* CSV headers line 1 | Primary Map labels cannot be reproduced or accepted | Recover tier/spectrum/slice code, response and temporal exposure manifest; synthetic multi-cell/multi-channel cases covering each pass/precision/coverage requirement |
| A03 | P0 confirmed baseline mismatch | R:appendices/B_payload_detail_visual.tex:2–17; S:src/simulations/ditl/ANTARA_Science_Sim.py:900–998 | Revised one-block instrument yield is represented by superseded layered assumptions | Freeze response interface and geometry; energy/angle/species response and confusion matrices; injected-spectrum reconstruction closure |
| A04 | P0 confirmed historical count bug | D:ANTARA_Science_Sim.py:1784,1819,1841; R:I_source_detail.tex:197 | Summed rates reported as counts; invalid science precision | Correct rate×width×elapsed-time units after review; same exposure at multiple dt/bin widths must conserve counts; historical outputs retained/superseded |
| A05 | P1 confirmed diagnostic units bug | S:src/simulations/ditl/ANTARA_Science_Sim.py:813,837–843 | Differential-rate diagnostic used as Hz in dead-time/background arithmetic | Distinguish spectral rate density from integrated rate; known flat-spectrum analytic integral and units assertion |
| A06 | P1 suspected physical response error | S:Science:1139–1142,1083–1086 | Per-bin dead time may overstate telescope live fraction/counts | Establish shared vs independent trigger chain; common-trigger dead-time benchmark and bin-refinement invariance; high-rate bench test |
| A07 | P1 confirmed private counter bug | S:Science:1115–1119 | “Cell passes” vary with sample rate rather than independent visits | Unique passage-ID set per spatial cell; 100 contiguous samples=1 visit; leave/re-enter and coarsen-grid tests |
| A08 | P1 confirmed restart bug | P:count_cell_passes.py:299–308 | Incompatible orbit/grid can resume into old counts if n_steps matches | Full config/data hash and shape validation; reject same-length different-RAAN/epoch/dt checkpoints; split-run equivalence |
| A09 | P1 confirmed ingestion bug | P:step2_process_irene_outputs.py:72–79,103–128 | Duplicate records overwrite, hide missing cells; late malformed inputs/semantics unchecked | Validate every row and unique key, units, finite nonnegative flux, epoch, energy thresholds and product type; duplicate+missing/wrong-product fixtures |
| A10 | P1 confirmed metric-label problem | D:Science:1804–1833; R:sections/04_simulations.tex:7 | 62.7% is detection-conditional sample fraction, not total SAA science duty | Report science-enabled duration/SAA duration and separate conditional gate efficiency; weighted variable-step/zero-science-pass fixtures |
| A11 | P1 confirmed incomplete local annual artifact | S:results/science/leop_1yr_ANTARA_Science_telemetry.csv:last record; R:I_source_detail.tex:21,209 | File ends near day 50, no terminal row; old standalone stats mislabeled integrated | Require 8760 h horizon, zero terminal interval, continuous interval sum, archives/checkpoint linkage and config identity before annual acceptance |
| A12 | P1 confirmed summary semantics | S:src/simulations/power/ANTARA_MCR.py:994,1009–1045 | Minimum SOC is mean minima; mission stats only final RAAN | Export RAAN/run keyed stats, worst sample and mean minima separately; two-run fixture with distinct minima and all RAAN groups |
| A13 | P1 confirmed statistical limitation | S:MCR:225–243,98 | z interval from population SD and n=2 cannot establish asserted coverage/reliability | Define estimand and sampling model; synthetic known-distribution interval check; increase independent draws only after bounded correctness checks |
| A14 | P1 confirmed battery accounting model defect | S:MCR:813–841 | Throughput includes charging later discarded at full capacity; inflated cycle-aging proxy | Use actual accepted battery charge/discharge energy with explicit curtailment; full battery + surplus fixture must not gain cycles from dumped solar power |
| A15 | P1 confirmed configuration differences | S:MCR:287–337,758–774 vs R:sections/03_spacecraft_architecture.tex:5 | independently tracking wings/−Z panel and ramped degradation cannot qualify common +Z EOL fixed-array margin | Explicit per-study geometry/EOL registry; attitude cosine cases and end-of-life energy closure with common loads |
| A16 | P1 confirmed censoring/altitude limitation | S:MCR:701–721,959–978; R drag CSV:5 | Endpoint at 334.93 km not cutoff success; radial altitude differs from ellipsoidal altitude | Record termination reason, elapsed time and altitude definition; analytic event-root and time-cap tests; separate disposal model later |
| A17 | P1 confirmed misleading old orbit interpretation | R:appendices/F_orbit_rf_support.tex:12; D:Detailed-ConOps and Mission Design/orbit_classification.csv | >8000 pooled annual SAA-only records incorrectly presumed impossible | Document two-run pooling; independent grouping and unique-key checks (already reproduced); retain approximate classifier caveat |
| A18 | P1 confirmed response-branch defect | S:Science:929,962–978,1042–1045,1181–1186 | rear-veto mask never true, per-step event label always Type1 | Revise under agreed response model; high-energy-only/topology fixtures and branch coverage; do not “fix” new rear-tag design as universal veto |
| A19 | P1 suspected downstream bin/uncertainty hazard | S:Science:1146–1157,1209–1215 | merged-bin edges remain old; background can look like precision; zero-count precision clipped | Export effective response/bin/exposure metadata; zero-signal/high-background/calibration-floor and merged-flux conservation tests |
| A20 | P1 confirmed geometric-only yield limitation | P:count_cell_passes.py:322–327; P:step2:133–149 | modeled dwell and ideal rates lack pointing/live/storage/downlink and calibrated channels | Couple interval-level science exposure to response; one pass crossing several cells, SAA-edge and same-pass coarsening fixtures |
| A21 | P1 confirmed range-label defect | P:AbhishekSims/plot_wrt_thickness.py:57–82 | last hit layer boundary labeled stopping endpoint | Score primary endpoint and escaped flag; compare with proxy for stopped/penetrating/secondary-dominated tracks |
| A22 | P1 confirmed dose-interpretation limitation | G:src/SteppingAction.cc:33; G:src/RunAction.cc:90–96; G:geometry/payload-3.gdml:9907 | global energy divided by world/scoring-container mass isn't sensitive-volume dose | Separate volume/species dose tallies; energy/mass closure in two-volume fixture; determine actual mass denominator before quantifying bias |
| A23 | P1 confirmed historical output mismatch | D:Science:1757–1775; R:I_source_detail.tex:155–171 | old packet formula saturates even at zero signal; gross contacts mistaken for delivery margin | zero-signal packet fixture, consistent MiB/MB/bit units, scheduled link throughput test; compare actual .002558663 MiB with generated .059936523 MiB |
| A24 | P2 confirmed documentation gap | R:README.md:5; R:sections/05_feasibility_and_budgets.tex:6,12; R:appendices/J_source_detail.tex:7–60 | references direct reviewers to absent archive/original tables | Repair inventory/cross-references after review; active-TeX dependency and required-table checks |
| A25 | P2 confirmed redundancy/supersession | R:I_source_detail.tex:69–77,102–110; R:H_source_detail.tex:48,197,259 | repeated science paragraph and obsolete battery/payload/CMG claims remain easy to quote | Keep historical provenance in clearly identified snapshots; remove duplication and link each accepted claim to approved evidence |
| A26 | P2 unestablished run identity | S working-tree diffs; R:C_simulation_provenance.tex:139–145 | source HEAD alone omits dirty settings, seeds/backends/data | Immutable manifest; snapshot/hash comparison and output-to-input graph checks |
| A27 | P2 confirmed numerical mismatch | R:appendices/I_source_detail.tex:182–184; D:Day-In-Life and Subsystem performance/ANTARA_Science_slew_events.csv | reported minimum slew 5.4° excludes raw .442496° minimum without a stated filter | regenerate min/max from the 18-row event table; explicit filtering/count check |

Within this table `S:Science` and `S:MCR` abbreviate `S:src/simulations/ditl/ANTARA_Science_Sim.py` and `S:src/simulations/power/ANTARA_MCR.py`. `R:I_source_detail.tex` etc. abbreviate R's `appendices/` files. “last record” is used instead of inventing a line number for an endpoint-inspected 1.4 GB file.

## Existing tests executed safely

An exact disposable copy of S's `src/` and `tests/` was made under `/tmp/antara-audit/test-checkout/`; existing Orekit data were linked read-only. No source patches were made to make tests pass. Interpreter: `/home/sammo/miniconda3/envs/orekit_env/bin/python` (Python 3.10 environment). Test cache disabled, bytecode disabled, results and Matplotlib cache isolated in `/tmp`.

Initial collection failed because SpacePy tried to write `/home/sammo/.spacepy/spacepy.rc` on the read-only filesystem. Repeating with its documented `SPACEPY=/tmp/antara-audit` override resolved this environment problem; it is not a simulation failure. Command (from MCR checkout):

```sh
SPACEPY=/tmp/antara-audit PYTHONDONTWRITEBYTECODE=1 \
PYTHONPATH=/tmp/antara-audit/test-checkout/src MPLCONFIGDIR=/tmp/antara-audit/mpl \
timeout 180 /home/sammo/miniconda3/envs/orekit_env/bin/python -m pytest -q -p no:cacheprovider \
 /tmp/antara-audit/test-checkout/tests/test_audit_repairs.py \
 /tmp/antara-audit/test-checkout/tests/test_scientific_integrity.py \
 /tmp/antara-audit/test-checkout/tests/test_telemetry_integrity.py \
 /tmp/antara-audit/test-checkout/tests/test_pass_statistics.py \
 /tmp/antara-audit/test-checkout/tests/test_slew_profile.py
```

**Result: 201 passed, 3448 warnings, 15.38 s**, exit success. Warnings predominantly come from Java-wrapper deprecations. Log: `/tmp/antara-audit/tests-rerun.log` (temporary diagnostic, not a scientific result). These cover bounded numerical/accounting/frame/config tests, not complete mission or detector validation. No full annual, Monte Carlo campaign, Geant4 run, long-term drag or IRENE execution was launched.

A further bounded selection from `tests/test_execution_integrity.py` using `-k "payload_per_bin or payload_environment"` completed with **1 passed, 16 deselected, 1.33 s** (same environment, 120 s timeout). This exercised existing per-bin uncertainty/merge accounting. Total existing tests passed across these two successful commands: **202**. It does not address the missing Rev 2.1 or shared dead-time validation.

Independent read-only checks also performed:

- All four R CSV hashes equal S copies; 685,798 classification records have unique keys and exact seven-RAAN pooled totals.
- Old D annual table's 76,235 records also reproduce all seven pooled class totals; no “single-year” assumption imposed on two runs.
- Grid overlap cardinality recomputed at 5°/1°/.5° → 92/2020/7940; full allocation .5° is 67200.
- Every supplied tier-disposition row counted; blank categories preserved rather than imputed; EMSC duplicate artifact identity checked.
- Historical DITL CSV/event summaries recomputed, including actual science/downlink totals and conditional fraction denominator.
- Annual-named S telemetry endpoint inspected; no full-duration pass inferred.
- Active TeX inclusion graph: 20 files, no duplicate active labels and no unresolved explicit `\ref` targets (LastPage supplied by package); unused additions excluded.
- Existing 61-page PDF text spot-checked and physical page 55 rendered; no report rebuild or exhaustive visual certification.
- Five of nine MCR images matched byte-for-byte to PDR archive figures; other generator chains left unestablished.

## Proposed engineering fixes and verification gates

1. **Freeze evidence before repair.** Preserve dirty source snapshots, archive hashes, detailed campaign outputs and all run metadata. Recover missing tier/spectrum code and original mean IRENE output. Publish the artifact graph and name the owner of each unestablished result. Gate: every accepted headline has source/config/output identity or is explicitly excluded.
2. **Approve measurement and coverage contracts.** Resolve longitude endpoints, eligible-region/core definitions, independent pass identity, effective energy channels, geometric vs science-enabled exposure, accepted vs delivered data and units. Gate: small exact synthetic grids/count/exposure cases match independent calculations.
3. **Repair accounting and ingestion first.** Rate×ΔE×dt, unique passage counts, checkpoint identity, duplicate/missing IRENE handling, bin metadata, battery curtailment and run-keyed summary semantics. Gate: timestep/bin-refinement invariance, time/energy/packet conservation, negative-input cases, restart equivalence and existing regressions pass.
4. **Implement the approved Rev 2.1 response.** Preserve the legacy model for historical reproduction. Build transport/optical/electronics response, stopping/penetrating classifier, mixed-species confusion matrix and measured dead-time model. Gate: truth-tagged and injected-spectrum closure, background/calibration-aware uncertainties, acceptance validated against geometry/bench data.
5. **Reconcile the coupled mission configuration.** Use explicit 2029/3-kg settings where supported by validated environmental inputs, final geometry/load/actuator/usable-battery assumptions, resolved fallbacks and station masks. Gate: bounded LEOP/nominal cases, boundary events, restart, horizon accounting and .5×/1×/2× timestep comparisons; no long run until these pass.
6. **Rebuild science success metrics from validated products.** Retain passage IDs and full region denominators, calibrate per-channel counts and exposure, include zero-science passes/excluded data and received-packet coverage. Gate: independent MMSC/MSC/EMSC evaluator reproduces every classification, including borderline/zero-count/missing-channel cases.
7. **Reassess engineering trades.** Run approved parameter/epoch/RAAN/solar/drag and response uncertainty studies with justified sample counts; separate end-of-life EPS, operational mission length, cutoff survival/censoring and physical reentry. Gate: comparable configurations, actual worst-case margins and documented uncertainty, not mean minima presented as extrema.
8. **Run long scenarios only after these gates.** Archive continuous interval sums, exact requested horizon, terminal marker and complete event/data hashes. Treat timeout as partial output; never rename partial results as annual validation.
9. **Revise MCR after findings review.** Generate accepted tables/figures from frozen datasets, correct pooled-run/conditional-fraction semantics, remove redundant paragraphs, retain explicitly superseded historical material and state remaining validation limits. Gate: every numerical claim resolves to an approved artifact and all report links/inclusions resolve.
