# Accounting integration test disposition — 2026-11-05

## Fresh checks actually executed

Source-root commands ran read-only in `/home/sammo/Desktop/Projects/ANTARA_CODES-main`:

```sh
pwd
git rev-parse --show-toplevel
git rev-parse HEAD
git branch --show-current
git status --short
git diff --cached --stat
git worktree list
sha256sum src/simulations/ditl/ANTARA_Science_Sim.py src/simulations/power/ANTARA_MCR.py /home/sammo/Desktop/Projects/MCR_ANTARA/patches/simulation/approved_baseline_accounting.patch
git apply --check /home/sammo/Desktop/Projects/MCR_ANTARA/patches/simulation/approved_baseline_accounting.patch
```

Results: recorded base/branch unchanged; both target hashes match original prerequisites; patch checksum matches the supplied checksum; apply-check exit0 with no conflicts. Python `hashlib.sha256` additionally recorded all four relevant current source files and exact `git diff --binary` bytes. No staged changes were present. The writable-scope check used the active session policy, not Unix ownership or a forbidden write probe.

## Fresh regression results

**No regression tests executed: 0 passed, 0 failed, 0 framework-skipped.** The following are NOT RUN because integration stopped at the explicit write-access gate:

| Requested verification | Current disposition |
|---|---|
| Four targeted patch regressions | Not run |
| Surrounding simulator tests | Not run |
| MCR accounting/configuration and count-rate checks | Not run |
| Checkpoint round-trip and telemetry integrity | Not run |
| Synthetic constant-spectrum payload test | Not run |
| Short isolated-output DITL smoke case | Not run |
| Post-patch consumer/API and numerical behavior review | Deferred until permitted integration |

No fresh warnings or numerical results exist to report. No annual, multi-year, pointing or top-level MCR study was launched. The previous isolated4-targeted/201-surrounding/74-local pass totals remain historical evidence only (`validation/2026-11-04-approved-v2/summary.json`), not tests rerun for this attempt.

After access is corrected, use the exact bounded verification plan in `SIMULATOR_REGRESSION_RESULTS.md`, rechecking source identities before reproducing dirty prerequisites in an isolated branch. Test real consumer behavior, effective intervals, analytic flux×energy-width×exposure counts, merged-count conservation, full-battery curtailment, each RAAN's output and mean-versus-worst minima. Compare uninterrupted/resumed outputs, terminal-row and horizon accounting. Use a fresh results directory and record the actual runtime epoch; do not infer2029 execution from a planning configuration.

The existing cell-visit and grid-checkpoint reference tests do not prove those contracts are integrated into production. Hardware-dependent material, optical, detector-response and dead-time assumptions remain unqualified. No merge-readiness claim is possible without the requested fresh regression and bounded integration evidence.

## Next bounded detector-response experiment

Validate a synthetic geometry/path-length fixture for rays entering+X toward−X through the2mm front and five14mm main blocks. Check ordered intersections,72mm on-axis active path, off-axis chords/misses and entrance-only0.25mm aluminium. A gap-free test fixture is not a selected packaging design. Once material/CAD inputs close, perform a small documented proton transport scan across threshold and science energies, scoring per-volume deposition, escape and energy balance without substituting truth energy for reconstructed energy. No response experiment was run here.
