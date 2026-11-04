# Current approved-baseline update

The current source is `config/payload/current.json` → `FPDU-2026-11-04-approved-v2`. Main blocks run along X; particles enter +X and travel −X; main SiPMs are on ±Y and Teflon is 0.11 mm per ±Z face. Eleven SiPMs, removed silicon, optional rear, unknown optical isolation. Shaping is 20 ns; coincidence references 200/250/300 ns; qualified dead time unknown. Earlier notes below are historical and superseded where inconsistent.

See `docs/audit/IMPLEMENTATION_CHANGELOG.md` for exact changes/tests and `2029_AUDIT_RECONCILIATION.md` for evidence limits. 2026 radiation and team-accepted RAAN products remain preliminary references for 2029, retaining generating-epoch provenance. The authoritative simulator patch is delivered but unapplied.

---

# ANTARA revision and evidence boundaries

- Epoch target: 2029-01-01. Older simulation runs are provisional and were not recomputed.
- Maximum spacecraft design mass: 3 kg.
- FPDU design source: ANTARA FPDU Payload Redesign — Verified Baseline, Rev 2.1 (2026-09-18). Supersedes Payload_1 five-layer stopping stack.
- SPENVIS/GRAS workflow is a proposed verification plan; no completed orbit-specific output invented.
- 5–100 MeV and MMSC/MSC/EMSC are committed science requirements, not demonstrated compliance.
- Five-year lifetime remains preliminary, with acknowledged methodological uncertainty.
- Source-detail appendices retain historical inconsistencies as documentary evidence.
- No unmeasured energy resolution, particle purity, efficiency or telemetry throughput asserted.

## Payload follow-up — 2026-11-04

Appendix A.2 now incorporates the authoritative five-block plus front-scintillator inputs and EJ-550 coupling. Rev. 2.1 single-block and legacy five-layer results remain historical evidence. Electronics are MCU/FPGA candidates; current coincidence input is 20 ns, while a separately suggested 20 ns dead time remains tentative. See `docs/audit/PAYLOAD_UPDATE_CHANGELOG.md` and `config/payload/README.md`. No orbit, power, operations, thermal, lifetime or grid model was changed.
