# Simulator regression results — integration access gate

## Current attempt

Production integration stopped at Step2 because the authoritative source and Git metadata are outside the writable roots. No regression suite, restart run, smoke simulation or annual campaign was executed in this attempt. Automated regression totals for this attempt: **0 passed, 0 failed, 0 framework-skipped**; the requested suites are **NOT RUN / access-gated**, not silently counted as passing or skipped tests.

Read-only preflight checks did execute:

| Check | Result |
|---|---|
| Two target SHA-256 comparisons against recorded original identity | 2/2 exact matches |
| `git apply --check` on current authoritative dirty tree | Exit0, no conflicts/output |
| Base/branch/worktree and staged/unstaged/untracked inspection | Recorded in integration report; no staged changes |
| Sandbox scope review | Authoritative source and `.git` not writable; no forbidden write probe |

Exact commands executed (source-root commands ran in `/home/sammo/Desktop/Projects/ANTARA_CODES-main`):

```sh
git status --short
git rev-parse HEAD
git branch --show-current
git worktree list
ls -ld . .git
cat AGENTS.md
git diff -- src/simulations/helper/antara_models.py src/simulations/pointing/ANTARA_pointing_budget.py src/simulations/power/ANTARA_MCR.py
git diff --cached --stat
git ls-files --others --exclude-standard
sha256sum src/simulations/ditl/ANTARA_Science_Sim.py src/simulations/power/ANTARA_MCR.py
git apply --check /home/sammo/Desktop/Projects/MCR_ANTARA/patches/simulation/approved_baseline_accounting.patch
rg --files tests
```

Python standard-library `hashlib.sha256` additionally checked the patch and target contents; `subprocess` captured exact revisions, status and patch-check exit code for the integration report. `rg` inspected available checkpoint/test filenames and local geometry/accounting/coverage test names. These are applicability/inventory checks, not runtime regressions.

## Prior isolated evidence — not rerun or integrated here

Source: `validation/2026-11-04-approved-v2/summary.json` and adjacent logs; exact historical commands are in `IMPLEMENTATION_CHANGELOG.md`.

| Prior suite | Passed | Failed | Skipped | Scope |
|---|---:|---:|---:|---|
| Original targeted source | 0 | 4 expected | 0 | Red tests demonstrating defects |
| Patched disposable source | 4 | 0 | 0 | AST/targeted accounting checks; no full MCR campaign |
| Local MCR/config/accounting/evidence suite | 74 | 0 | 0 | Includes3 optional legacy checks enabled against disposable source |
| Surrounding simulator suites | 201 | 0 | 0 | Prior isolated checkout;3448 predominantly Java-wrapper warnings |

The historical first surrounding run had13 missing-Orekit-data failures; linking existing data read-only resolved them. The old pass totals are not fresh production-integration results. Exact original target hashes still match, but that alone does not validate every environment/dependency or consumer.

## Deferred acceptance gates and commands

Run only after access is corrected and an isolated integration branch/worktree reproduces the reviewed dirty prerequisites. Use fresh results/cache directories and the repository's Orekit environment. Commands below are **planned, not executed**; run from the authorized integration worktree, setting `ANTARA_SOURCE_ROOT` to its absolute path and `ANTARA_LEGACY_SRC` to its `src` directory.

1. Targeted regression before/after: run the MCR repository's `patches/simulation/test_accounting_patch.py` with the Orekit interpreter and `ANTARA_SOURCE_ROOT`. Expect4 original failures then4 patched passes. Check exact patched hashes. Exercise the merged intervals through real `PayloadModel.generate_data`, not just source structure.
2. Surrounding and restart:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src \
 SPACEPY=/tmp/antara-integration-checks \
 MPLCONFIGDIR=/tmp/antara-integration-checks/mpl \
 timeout 180 /home/sammo/miniconda3/envs/orekit_env/bin/python -m pytest -q -p no:cacheprovider \
 tests/test_audit_repairs.py tests/test_scientific_integrity.py \
 tests/test_telemetry_integrity.py tests/test_pass_statistics.py \
 tests/test_slew_profile.py tests/test_checkpoint_roundtrip.py \
 tests/test_execution_integrity.py
```

Record collection/pass/fail/skip totals; timeout means incomplete validation, not success. Verify continuous-versus-resumed telemetry/histograms, preserved configuration identity, open-pass state, final flush and zero-duration terminal row. The patch does not integrate the archived grid checkpoint-identity contract: production acceptance of that separate loader remains outstanding.

3. From the MCR checkout, run the existing local suite with `ANTARA_LEGACY_SRC` pointing to the integration worktree, `PYTHONDONTWRITEBYTECODE=1`, isolated SpacePy/Matplotlib paths and the same interpreter:

```sh
/home/sammo/miniconda3/envs/orekit_env/bin/python -m unittest discover -s tests -v
```

This covers geometry/current configuration, count-rate evidence, histogram conservation, rate×energy-width×time dimensions and reference visits/checkpoints. Contract tests are not evidence that the production private sample counter or archived grid loader has been repaired. Add production-facing visit tests before asserting integration:100 contiguous samples=one visit; leave/re-enter, same-passage multiple cells, coarsening and timestep variation.

4. Short integration case, in the isolated worktree with existing Orekit data linked read-only:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src \
 SPACEPY=/tmp/antara-integration-checks \
 MPLCONFIGDIR=/tmp/antara-integration-checks/mpl \
 timeout 120 /home/sammo/miniconda3/envs/orekit_env/bin/python \
 src/simulations/ditl/ANTARA_Science_Sim.py \
 --scenario no_leop_24h --duration-hours 0.016666666666666666 --step-sec 2 --no-plots
```

This is an approximately60-second software smoke case, not annual or qualified2029 evidence; record actual runtime epoch rather than infer it from the baseline file. Check summed positive intervals against the requested horizon, zero-duration terminal row, finite telemetry, output schema and no writes to historical results. Use a separate synthetic constant-spectrum payload fixture if the short orbit segment has no science exposure: require analytic counts proportional to bin width and elapsed exposure, conserved merged counts, and correct effective intervals. Do not interpret zero science during this short segment as response validation.

5. Review diagnostic consumers and exported statistics headers. The environment key removal and renamed SOC column are API changes. Verify no retained consumer expects the old keys. Check every RAAN group and distinct worst/mean minima with a small synthetic fixture; do not execute top-level MCR or pointing campaigns to test imports.

## Acceptance categories

- **Successfully integrated corrections:** none in this attempt.
- **Passing only in an isolated environment:** the historical4/74/201 suites above; no new production claim.
- **Hardware-dependent assumptions:** material/optical isolation, acceptance, species response, coincidence architecture, ADC/processing performance and qualified dead time remain unresolved.
- **Requires new simulator outputs:** corrected battery throughput/cycle-aging proxy, affected SOC summaries/statistics, revised diagnostic/merged-bin metadata products. Old outputs remain historical. Checkpoint/cell-visit production integration needs its own evidence. No MCR number changes until relevant bounded checks and explicitly authorized reruns are verified.

Next bounded detector-response experiment is specified in `SIMULATOR_PATCH_INTEGRATION.md`: first validate geometry/path-length observables without guessed material, then a small controlled proton transport scan after material/CAD closure.
