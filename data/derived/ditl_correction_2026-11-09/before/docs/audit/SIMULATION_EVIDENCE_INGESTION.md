> **Scope update (user direction, 2026-11-09):** Exclude the short24h-named outputs from MCR operational evidence. Use only the `leop_1yr` group for operations, retaining its incomplete-telemetry and incompatible-event limitations. Thermal and detumble remain separate studies. One-hour calculations below are retained as an audit trail, not adopted comparison results.

# Simulation evidence ingestion — 2026-11-09

## Scope and inventory

48 original supplied artifacts (1,551,767,598 bytes) were read and SHA-256 inventoried before analysis. Full paths, sizes and hashes: `evidence/science-ditl/manifests/original_inventory.json`. This includes 24 Science CSVs, 12 Science figures, two thermal CSVs/four figures and one detumble CSV/five figures. Original `evidence/science_ditl/` paths are retained; the canonical `science-ditl/` directory contains manifests, derived validation and figures, with a raw-path index. No original is moved or rewritten. Unprefixed Science figures have no matching raw run manifest and remain unadopted historical images.

The MCR working tree starts at commit23170a89a9b47265bb2bb8dcd97a10ffe7eb9bfd, branchmaster. Prior geometric-factor edits and the user's existing Section1/main.pdf modifications are preserved. The active LaTeX includes the geometric-factor revision. README's older PDF pointer is updated only on delivery. No AGENTS.md exists in the MCR tree/ancestors; external simulator AGENTS.md was read. External source is read-only and was neither executed as a simulation nor modified.

## Distinct evidence identities

| Group | Observed span | Disposition |
|---|---|---|
| leop_24h telemetry/events | 0–3600 s;1801 telemetry rows, zero-duration terminal | Complete one-hour export; not a24h result |
| no_leop_24h telemetry/events | 0–3600 s;1801 rows, zero-duration terminal | Complete one-hour export; not a24h result |
| leop_1yr telemetry | 0–4,320,020 s accounted intervals;1,861,462 rows; no terminal | Incomplete annual-labelled artifact; ~50days |
| leop_1yr event exports | Events extend to31,533,008 s; absolute timestamps imply2000-03-01 UTC | Nearly365-day event span, no completion manifest; incompatible with telemetry even in overlap |
| Thermal | 43,201 labels0–86400 s,2s spacing; seven nodes | Single history; epoch/runtime identity and initial state convention unresolved |
| Detumble summary | 50,000 trial rows, no chronological histories | Historical synthetic summary; generating revision/seed/censor times unknown |

Per-group machine-readable JSON manifests are under each canonical area's `manifests/`. Unknown producing commit, runtime settings, seed, attitude, integrator or constants are explicitly UNKNOWN. Current source hashes and literal defaults are retained separately in `source_reference_inventory.json` and `candidate_source_defaults.json`; **they are candidate explanations, not verified generating configurations**. The current source's2000-03-01 default cannot date the two one-hour runs or thermal output. Annual event absolute-minus-elapsed times establish that export's2000 epoch; the incompatible telemetry cannot inherit its full run identity automatically.

The exact scenario names suggest presets, but actual requested durations are unknown because CLI overrides are absent. The two complete one-hour traces must not be filled to24h or rebranded as nominal-day evidence. No simulation campaign was launched.

## Reproduction and preservation

`scripts/validate_simulation_evidence.py` streams the1.4GB annual telemetry in25,000-row chunks, checks strict interval continuity and aggregates only supplied observations. It produces derived JSON/CSV summaries without rewriting inputs. `scripts/plot_simulation_evidence.py` generates the adopted plots. All original hashes are checked again at completion. Figure captions distinguish source-label time, recorded exposure, model predictions and qualified measurement gaps. Software tests validate accounting only.
