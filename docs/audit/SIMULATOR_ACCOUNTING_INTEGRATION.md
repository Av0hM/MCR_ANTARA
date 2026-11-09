# Accounting integration disposition — 2026-11-05

**BLOCKED BEFORE INTEGRATION; not ready to merge.** This record is stored in the writable MCR repository, not in the authoritative simulator. No integration branch/worktree was created, no patch applied, and no production source or Git metadata changed.

## Verified current identity

- Authoritative source: `/home/sammo/Desktop/Projects/ANTARA_CODES-main`.
- Branch: `main`; base/current commit: `51933bb902288de095f362546c73b006fe702882`.
- Only existing worktree: the authoritative main checkout. No staged changes.
- Patch: `/home/sammo/Desktop/Projects/MCR_ANTARA/patches/simulation/approved_baseline_accounting.patch`.
- Patch SHA-256: `e1fe0570e8e8a5ad1fb3bf1bb6eb4277c043861faded760ba565397cca37de87`.
- Current tracked-diff SHA-256: `fa8880f3a26f061588af89c2978d7bd9cc15de5cad15e5a63012e63401030f37`.
- Both patch targets exactly match the recorded original prerequisites in `patches/simulation/source_identity.json`.
- Fresh read-only `git apply --check` returned exit0, no output/conflicts. This establishes applicability only, not runtime compatibility or deployment.

| Current source file | SHA-256 |
|---|---|
| `src/simulations/ditl/ANTARA_Science_Sim.py` | `92baa85028d79c9ebb347e5a8a5c17325c814b7ef42ad3dbefbefc3076724413` |
| `src/simulations/helper/antara_models.py` | `3c10b328a48b7a9705e61d17d4e445a67266567ed7a5dd25fc20b13c9a209ed5` |
| `src/simulations/pointing/ANTARA_pointing_budget.py` | `8d8ffb5f6d56b1195465ddd63853b0ef2af8ed90f8710512308dadf7f5640aab` |
| `src/simulations/power/ANTARA_MCR.py` | `cdb98ac45806865244a275ba5c0cd40434394af26cd2ca85f9596f31f8a63fd0` |

Current status, preserved without stash/reset/overwrite:

```text
 M src/simulations/helper/antara_models.py
 M src/simulations/pointing/ANTARA_pointing_budget.py
 M src/simulations/power/ANTARA_MCR.py
?? build/
?? figures/pointing/
?? src/antara_simulations.egg-info/
?? tmp/
```

No source configuration changes were made. Existing helper, pointing and power modifications and all untracked groups remain untouched. The expected patch scope remains the Science DITL and MCR power files only; exact original/expected post-patch hashes remain in the existing source-identity manifest. Expected post-patch hashes were **not observed in production** because no patch was applied.

## Precise access blocker

The active session still starts in `/home/sammo/Desktop/Projects/MCR_ANTARA`. Writable roots are that MCR directory and `/tmp`; `/home/sammo/Desktop/Projects/ANTARA_CODES-main` and its `.git` are outside the permitted roots. Selecting the simulator as a command working directory grants read access, not write permission. A linked worktree in `/tmp` would still modify the authoritative Git metadata and is therefore not a permitted workaround.

No forbidden write probe, escalation or detached-copy workaround was attempted. The user's instruction to stop if repository access remains unavailable takes effect before Steps2–5. Resume in a session whose writable workspace includes the authoritative simulator **and its Git metadata**. Task authorization already exists; filesystem scope must change.

## Scope and compatibility still awaiting integration verification

The patch changes the environment diagnostic from invalid Hz arithmetic to explicit Hz/MeV density; adds effective merged-bin interval metadata; excludes curtailed/unserved energy from battery throughput; and separates mean run-minimum SOC from worst minimum while preserving all RAAN statistics groups. These change diagnostic/output semantics and require consumer review and fresh tests. No new API compatibility conclusion is made in this access-blocked attempt.

Payload geometry, detector physics, timing, science thresholds, eligibility and radiation outputs are unchanged. Cell-visit and grid-checkpoint contract integration remain separate outstanding work. Historical isolated test passes are not production acceptance. No MCR numerical claim or scientific output was altered; corrected numerical outputs will require verified, separately bounded reruns after integration.

## Files changed in this attempt

Only two new MCR audit records: `docs/audit/SIMULATOR_ACCOUNTING_INTEGRATION.md` and `docs/audit/SIMULATOR_ACCOUNTING_TEST_RESULTS.md`. No authoritative simulator files changed. There is no isolated integration branch to merge.
