# Tested accounting patch — NOT applied to authoritative simulator

Target: `/home/sammo/Desktop/Projects/ANTARA_CODES-main`, as inspected with its pre-existing dirty changes. `source_identity.json` records exact original and patched SHA-256 values. The sandbox only permits writing the MCR workspace and `/tmp`; no sibling source was overwritten, no permission escalation was attempted, and no annual run was launched.

`approved_baseline_accounting.patch` changes only:

- Science environment diagnostic: exports differential rate density in Hz/MeV; removes unsupported Hz dead-time/background arithmetic without inventing integration widths. The payload continues to consume the same environment spectrum. No current six-scintillator response is fabricated.
- Science legacy merging: exports effective interval metadata (first merged slot spans original edges 0–3; slots 1–2 inactive). Existing fixed-slot counts remain for backward compatibility. Consumers must use this metadata; nominal edge arrays are retained as original reporting slots, not claimed effective widths.
- MCR battery accounting: throughput uses charge/discharge energy actually accepted at the battery boundary. Curtailed energy and unmet demand are excluded. Aging coefficients and power/orbit physics remain unchanged.
- MCR statistics: separates `mean_run_min_soc` and `worst_min_soc`; collects statistics for every RAAN with a RAAN key rather than final RAAN only. This does not qualify the old two-run confidence interval methodology.

Existing source outputs are deliberately not regenerated. Header/diagnostic changes are an output-API change; consumers of removed environment `count_rate`, `dark_counts`, `total_count_rate` keys must migrate to the density field or an explicit integrated model. The active payload consumer reads spectra and retains its legacy physical limitations.

## Reproduction

Copy the authoritative `src/` and `tests/` into a disposable checkout and link existing Orekit data read-only at `orekit-data/orekit-data-main`. Verify original hashes before applying. Run `git apply --check` then `git apply` only inside the disposable copy or an authorized clean implementation branch. Do not force application onto different source.

```sh
ANTARA_SOURCE_ROOT=/path/to/checkout PYTHONDONTWRITEBYTECODE=1 \
 /home/sammo/miniconda3/envs/orekit_env/bin/python \
 patches/simulation/test_accounting_patch.py
```

The test file belongs to this MCR checkout; use its absolute path when running elsewhere. Original source: **4 failures**, demonstrating the four defects/metadata omissions. Patched source: **4 passes**. Surrounding bounded simulator suites: **201 passes** (see audit validation logs). The initial surrounding run had missing Orekit-data failures; the corrected environment passed without code changes. AST extraction avoids executing the expensive top-level MCR study merely to test arithmetic. Structural statistics/metadata checks are supplemented by independent numerical contract tests; this is not full end-to-end campaign validation.

Unchanged source limitations include sample-count private cell counters, old response/event-type branches, per-bin dead-time physics, clipped zero-count uncertainty, and archived grid checkpoint loader. Their replacement contracts and acceptance tests are in `scripts/fpdu_contracts.py`, but production integration/migration is still required. Do not label those defects repaired in the sibling source.
