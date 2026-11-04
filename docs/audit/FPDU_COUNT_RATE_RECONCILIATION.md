# Count-rate reconciliation

Current input archive: `data/raw/payload_count_rate_2026/` (22 original files preserved). Detailed inventory/configuration/transformation evidence remains in `COUNT_RATE_EVIDENCE_INGESTION.md` and `AP9_AE9_COUNT_RATE_VALIDATION.md`. Independent calculator: `scripts/validate_count_rate_evidence.py`; reproduced outputs and hashes: `data/derived/payload_count_rate_2026_audit/validation_summary.json`.

| Map | Proton maximum Hz | Electron maximum Hz | Same-cell sum maximum Hz |
|---|---:|---:|---:|
| Mean | 358.9201185 | 67779.6550717 | 68055.6347230 |
| 99th percentile | 975.6586990 | 503419.7425156 | 504245.0636023 |

**MODEL PREDICTION:** idealized incident-rate proxies. **VALIDATED RESULT:** numerical reproduction and exact coordinate alignment, not accepted detector rates. Both maps have 7,940 unique cells matching the approved positive-area-overlap polygon grid at 0.5°. The earlier uncertainty about missing cells in an unspecified expected domain is now resolved for this explicit polygon convention.

All source records use MJD 61041, 2026-01-01 at 600 km. These are approved preliminary inputs for 2029 planning, not regenerated 2029 radiation outputs. AP9 proton / AE9 electron integral omnidirectional flux is interpolated log–log at 5.5 / 0.35 MeV. Positive integral flux F [cm⁻² s⁻¹] becomes isotropic directional intensity F/(4π) [cm⁻² s⁻¹ sr⁻¹]; multiplying G=1 cm² sr and ideal efficiency=1 gives Hz. No second angular integral is appropriate. Original area-proxy columns without division by 4π are not telescope rates.

The script models **no** 250 µm aluminium transport, measured acceptance, electron rejection, optics, digitization or dead time. The 250 µm = 0.25 mm aluminium entrance is a separate design input. The proton energy grid has integral thresholds through 20 MeV, not a finite 20 MeV spectrum endpoint; no F(>100 MeV) is available. Thus these tables cannot derive a 5–100 MeV differential measurement or accurately subtract >100 MeV particles.

The historical approximately 400 Hz **PRELIMINARY ESTIMATE** was conditional on protons only, 250 µm aluminium, G=1 cm² sr and 100% efficiency. Its generator/spectrum/percentile remain unidentified. It is near the mean-map maximum but that numerical similarity does not establish common provenance; the 99th-percentile proton maximum is ~2.44 times 400 Hz. Do not adjust G or efficiency to reconcile them. Per-cell rates control preliminary planning.

The pointwise percentile maps and their sum do not define a joint percentile, time-domain burst envelope or guaranteed upper bound. Electrons may create triggers before classification. Actual peak front-end trigger rate remains unknown: require shielding/threshold transport, effective geometry, species response, coincidence logic, bursts and noise. A corrected 2029 environment run is required for a physically epoch-matched claim, but not for labeled provisional planning use of these accepted inputs.

Anisotropy AP8 UP-MAX 2028 evidence and AP8/AE8 PDF material are separate model/epoch evidence; they cannot silently replace AP9/AE9 assumptions. The source ODS MAX formula defect remains preserved and identified in the ingestion audit.
