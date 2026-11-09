# Corrected DITL authority — 2026-11-09

This current correction supersedes all earlier Science/DITL-dependent statistics and evidence statuses below. Earlier entries are retained as historical audit history, not active numerical claims. Independent physics/design/RAAN/thermal/detumble findings are unaffected. Current sources: `CORRECTED_DITL_RUN_VALIDATION.md`, `DITL_CORRECTION_IMPACT_MATRIX.md`, `STORAGE_BACKLOG_VALIDATION.md`, and `evidence/science-ditl/run_registry.json`.

All three corrected timestamp spans are complete (86400/86400/31536000 s), epoch2000-03-01. Annual acquisition247258 s; minimum recorded battery15.097556 Wh; full ideal Relay428836800 bytes; preferred EMSC v3 slot volume46637364 bytes; nominal peak75336 bytes; seven-day outage peak1010028 bytes. Runtime config and transition/slew semantics remain unresolved. No2029 calibration or qualified science success follows.

Current requirement status totals: {'CONDITIONAL': 17, 'OPEN': 28, 'SUPPORTED': 3, 'NOT EVALUATED': 3}. ANT-OBC-FR-002 is CONDITIONAL (outage spill needed); ANT-GSO-FR-003 is CONDITIONAL (coverage corrected, logger/source closure open), replacing its earlier NOT MET truncation rationale. Full updated register: `SUBSYSTEM_REQUIREMENT_TRACEABILITY.md`.

---

## Prior audit history (DITL-dependent entries superseded)

> **Current-baseline supersession (2026-11-04):** Use [FPDU_APPROVED_BASELINE.md](FPDU_APPROVED_BASELINE.md), [2029_AUDIT_RECONCILIATION.md](2029_AUDIT_RECONCILIATION.md) and [REMAINING_OPEN_DECISIONS.md](REMAINING_OPEN_DECISIONS.md). The record below is retained as historical audit evidence. Silicon is removed, rear detection optional, main blocks longitudinal along X, eleven SiPMs on ±Y/main plus front, Teflon 0.11 mm per ±Z face. Coincidence references are 200/250/300 ns, shaping 20 ns, qualified dead time unknown. Optical isolation remains open. Earlier 20 ns coincidence/dead-time guesses and unresolved coating-thickness interpretation are superseded.

# MCR numerical and narrative claim audit

> **2026-11-04 payload follow-up:** The audit below is the unchanged 2026-11-02 finding snapshot, with original source line references. The current narrative specification is [Appendix A.2](../../appendices/B_payload_detail_visual.tex), updated with five main blocks plus a front scintillator, EJ-550 coupling and candidate MCU/FPGA processing. Current coincidence input is 20 ns; a separately suggested 20 ns dead time is tentative. See [compatibility review](PAYLOAD_SIMULATION_COMPATIBILITY.md), [open decisions](PAYLOAD_OPEN_DECISIONS.md) and [change log](PAYLOAD_UPDATE_CHANGELOG.md). Documentation updates do not close the historical physics/model findings.

Audit date: 2026-11-02. Audit only; simulation code, input configurations, scientific results and MCR source were not changed.

**Source notation:** `R:` means this MCR repository; `S:` means `/home/sammo/Desktop/Projects/ANTARA_CODES-main/`; `P:` means the `PDR Sims/` member tree in `/home/sammo/Downloads/PDR Sims-20261021T072428Z-1-001.zip`; `D:` means the `MCR DATA/` member tree in `/home/sammo/Downloads/MCR DATA-20261021T072514Z-1-001.zip`; `G:` means `PROJECT_ANTARA/saa_sim/` inside `P:AbhishekSims/PROJECT_ANTARA.zip`. Archive members were read from disposable copies under `/tmp/antara-audit/`. Line numbers refer to the inspected working files/archive members, not an assumed common version. See [repository map](REPOSITORY_MAP.md) for scope and source identities.

**Evidence terms:** Confirmed = demonstrated by inspected code, file comparison or arithmetic. Suspected = plausible consequence needing a discriminating test. Unestablished = the producing inputs/revision or required validation were not recovered. A passing regression is not physical validation.


## Overall disposition

The active main report already qualifies many results correctly: 2029 is a target epoch, detector response is provisional, AP9-named integrated flux is not live AP9, and 300 km termination is not atmospheric reentry. Those qualifications should be retained. The principal remaining problems are metric semantics, incompatible baselines and missing reproducible derivations. Historical appendices carry warnings, so their superseded content is not automatically an active flight requirement; nevertheless main-text references sometimes direct readers back to it.

Read [DATA_PROVENANCE](DATA_PROVENANCE.md) for numerical derivations and [ISSUES](ISSUES.md) for proposed verification. No MCR edits were made.

| ID | Location | Claim/problem | Status and proposed disposition |
|---|---|---|---|
| C01 | sections/01_mission_context.tex:163–164,241,314,357 | “270°W to 10°E”, 130° span, 312/7800/31200 cells | **Confirmed contradiction.** Approve exact longitude bounds/wrap and regenerate requirement denominators; don't silently infer −120° or another intended boundary. |
| C02 | sections/04_simulations.tex:7; I_source_detail.tex:71,104 | 62.7% science-active fraction “across passes” | Value reproduces, denominator is only Detection-mode steps, averaged across five nonempty science records. It excludes the sixth pass and non-Detection acquisition time. Label exactly and add elapsed-time science/SAA exposure. |
| C03 | I_source_detail.tex:197–198 | 13k–108k counts “well above all mission tier thresholds” | **Confirmed unsupported conclusion and historical counting bug.** Source sums rates without dt; pass-level totals cannot qualify per-cell/per-channel/independent-pass requirements. |
| C04 | I_source_detail.tex:21–23,201–216 | completed year-long integrated simulation; 11.22 W/.987 SOC/787 cycles | Numbers trace to old standalone annual RAAN power stats, not integrated Science. Local leop_1yr file is only ~50 days and incomplete; this does not exclude other runs, but supplied proof is inadequate. |
| C05 | appendices/F_orbit_rf_support.tex:12; sections/02_mission_overview.tex:34; README_REVISED.md:9 | old >8000 SAA-only totals necessarily invalid / awaiting counter repair | **Confirmed interpretation error in the report.** D raw table has 76,235 records and two runs per RAAN; all old class sums match. E.g. RAAN 0 has 8280 SAA-only across two one-year runs, not one. Class geometry remains approximate; distinguish pooling from a broken orbit counter. |
| C06 | sections/04_simulations.tex:13; M_updated_raan_drag_study.tex:6–17 | “minimum SOC” 54.4–74.7% | Correct transcription, but master code averages each run's minimum. Label mean run-minimum, also report worst run/time. At 180° stats minimum-of-minima is .710527 rather than .734463. |
| C07 | M_updated_raan_drag_study.tex:36–37; I_source_detail.tex:211–216 | 99% confidence intervals | Main appendix correctly cautions; actual candidate formula uses population SD and z for n=2, and only last RAAN. Cannot imply 99% population coverage/reliability. Specify estimand, sample count and a justified uncertainty method. |
| C08 | sections/03_spacecraft_architecture.tex:5 | “power studies performed using end-of-life assumptions” | **Overbroad.** MCR code uses time-varying degradation 1→.95 plus constant loss factors. Other solar scripts differ. A full-run average is not automatically worst-case EOL power. |
| C09 | sections/03_spacecraft_architecture.tex:5 vs sections/04_simulations.tex:13 | 11.05/11.40 W at 0°/30° vs newest 11.02/10.82 W | Old values trace to D annual matrix; latest values to R cutoff matrix. Not arithmetic contradictions if labeled historical, but both need explicit run identity and configuration. Avoid deriving one common EPS margin from them. |
| C10 | sections/02_mission_overview.tex:19; M:17 | 0°/30° favorable vs highest mean at 180° | Not necessarily logically contradictory; “favorable” lacks stated objective and mission-wide robustness criterion. Rank with comparable durations/constraints/uncertainty and launch-feasible cases. |
| C11 | appendices/B_payload_detail_visual.tex:2–17 vs current S:Science:900–998; H_source_detail.tex:197–243 | Rev 2.1 one-block vs five-layer detector | **Confirmed architecture mismatch.** Main design is clear; simulation yield still uses superseded detector. Historical warning does not make response predictions representative of Rev 2.1. |
| C12 | H_source_detail.tex:48,58–60,92; sections/03:5; E_budgets_and_bom_details.tex:12 | 22.5/25/28.8 Wh and “conservative” 25 Wh | Historical 25>22.5 is not conservative against that capacity; latest text separates rated/planning values. Preserve this distinction and obtain selected usable BOL/EOL capacity before margins. |
| C13 | H_source_detail.tex:259–280; sections/03:18 | CMG vendor unit vs desired RW+MTQ; .4° pointing | Main text correctly leaves supplier selection open. Configured model accuracy/vendor text cannot qualify the intended actuator architecture. |
| C14 | I_source_detail.tex:139–142,169–171; H:177–185 | no brownouts, ~1.5 MB daily capacity and 4× return margin | No brownout reproduced only for historical assumptions. Contact capacity is not achieved relay throughput: archived downlink totals only .002558663 MiB. Need scheduled valid tracking, packet overhead and closure. |
| C15 | I_source_detail.tex:155–156 | .060 MB/day “consistent with 300–400 KB/day” | Two different availability/packet assumptions; no documented scaling establishes consistency. Binary/decimal units mixed. Current fixed histogram packet model differs from old byte-rate formula. |
| C16 | I_source_detail.tex:189–198 | “measured” flux 50–70% of AP9 predictions | These are modeled outputs with configured reference spectrum and attenuation factors; no independent measurement/model-comparison validation. Main sections correctly qualify this; rename historical terminology on review. |
| C17 | appendices/L_new_evidence.tex:5–22 | table and plots imply tier classifications | Table counts reproduce and main text appropriately denies global success. MMSC/MSC embedded images are hash-matched to **tier_slice** plots, not distinct **tier_disposition** plots. Clarify captions and retain provenance. |
| C18 | B_payload_detail_visual.tex:79–84 | response integral presented as observable counts | Equation has no explicit time/exposure integral. It is a rate if R is response area and Φ is per second, unless R explicitly absorbs exposure. Define units and live exposure rather than imply counts from instantaneous flux. |
| C19 | F_orbit_rf_support.tex:3–8; C_simulation_provenance.tex:42 | annual 4 kg/97.4°, shared RAAN 15° | Correct for archived/committed snapshots, not current dirty source (3 kg/97.6°/3650-day campaign; shared RAAN 30°). Attach snapshot hash to each table. |
| C20 | sections/05_feasibility_and_budgets.tex:9; L:55–72 | 1536.3 g subtotal / <3 kg target | Sum correct but missing payload/deployer and panel quantities. Main text acknowledges this; not a closed mass margin. Original workbook/source datasheets require archival qualification. |
| C21 | I_source_detail.tex:69–77 and 102–110 | same science-fraction paragraph repeated | **Confirmed redundancy**; retain one qualified passage after findings review. |
| C22 | sections/05:9 | payload/deployment mass omission stated twice | Editorial redundancy; consolidate once after evidence review. |
| C23 | README.md:5 vs actual tree; sections/05:6,12 vs J_source_detail.tex | source_archive claimed present; original MOP/risk/traceability tables said retained | Directory absent; J contains placeholders rather than the asserted original risk/threshold tables. Fix navigation/content inventory after review. |
| C24 | sections/01:96–101 | observed satellite anomalies/lost communication and operational protective benefit | Specific examples/citations and evidence for actionable prediction are absent. Treat as motivation/aspiration, not demonstrated service capability. |
| C25 | I_source_detail.tex:182–184; H_source_detail.tex:318–320,344 | slew angle range 5.4°–175.8° | **Confirmed numerical transcription/filter mismatch.** All 18 archived slew rows have minimum .442496° and maximum 175.808369°. No filter defining 5.4° as the minimum was supplied. Correct or explicitly document selection. |

## Claims that remain requirements, not evidence of compliance

5–100 MeV calibrated directional flux; 2/3 effective channels; 70/90/95% coverage; independent-pass thresholds; 10–50% uncertainties; 2029 analysis epoch; <3 kg complete mass; five-year operational objective; launch-compatible SSO; final RF capacity and usable battery energy. Reported completion of software or plotted primary cells cannot substitute for these verification products.

## Positive evidence and limits

- Latest orbit class tables are internally consistent, with unique record keys and correct pooled sums.
- Latest power/lifetime summary values are transcribed accurately as modeled outputs, with explicit cutoff caveats.
- Old DITL event counts, minimum battery and most rounded descriptive statistics reproduce from archived data.
- All science-disposition row counts in L reproduce exactly, and their geographic limitation is already acknowledged.
- No calibrated response/thermal/structural/hardware qualification or disposal compliance is inferred from these facts.
