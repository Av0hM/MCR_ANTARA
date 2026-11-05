# Simulator patch integration — access-blocked preflight

## Disposition

**NOT INTEGRATED.** Step 1 completed; Step 2 stopped under the user's explicit instruction to stop if the authoritative repository is not writable. No integration branch/worktree, patch application, stash, reset, commit, production test run or new simulation output was created. MCR LaTeX, numerical claims, PDF, configurations, original patch and raw results are unchanged.

The active filesystem policy grants writes only under `/home/sammo/Desktop/Projects/MCR_ANTARA` and `/tmp`. The authoritative `/home/sammo/Desktop/Projects/ANTARA_CODES-main` and its `.git` are outside those writable roots. Ordinary ownership/mode (`sammo`, directory mode755) does not override the session sandbox. This is a policy limitation, not a claimed Unix permission failure: no forbidden write probe or approval escalation was attempted. A linked worktree under `/tmp` still modifies the authoritative `.git/worktrees` and refs, so it is not an authorized workaround. A detached copy would provide only isolated verification, not production integration.

Resume from a session that explicitly permits writes to the authoritative source and its Git metadata. The task authorization is already clear; the missing prerequisite is filesystem access.

## Reviewed evidence

Read `AGENTS.md` in the authoritative source; `IMPLEMENTATION_CHANGELOG.md`, `CLAIM_TRACEABILITY.md`, `REMAINING_OPEN_DECISIONS.md`; patch README, source identity, full patch and previous validation summary. Science DITL is authoritative; Master remains excluded from new repair work.

- Authoritative branch: `main`.
- Base commit: `51933bb902288de095f362546c73b006fe702882`.
- Existing worktrees: only the authoritative main checkout, at this commit.
- MCR checkout commit: `2350bcc653c5359235bafc40ea96a2682ef755e8`; clean at this task's initial inspection.
- Patch: `patches/simulation/approved_baseline_accounting.patch`.
- Patch SHA-256: `e1fe0570e8e8a5ad1fb3bf1bb6eb4277c043861faded760ba565397cca37de87`.
- Existing tracked-diff SHA-256 (exact `git diff --binary` bytes, including trailing newline): `fa8880f3a26f061588af89c2978d7bd9cc15de5cad15e5a63012e63401030f37`.
- No staged changes; 1157 untracked path entries, summarized below. None removed or altered.

### Source identity

| Expected changed file | Current SHA-256 | Comparison with patch prerequisite |
|---|---|---|
| `src/simulations/ditl/ANTARA_Science_Sim.py` | `92baa85028d79c9ebb347e5a8a5c17325c814b7ef42ad3dbefbefc3076724413` | Exact original match |
| `src/simulations/power/ANTARA_MCR.py` | `cdb98ac45806865244a275ba5c0cd40434394af26cd2ca85f9596f31f8a63fd0` | Exact original match |

Both match `patches/simulation/source_identity.json` exactly. **The patch was generated against the current file contents**, including the dirty MCR power settings; it is not simply a patch against pristine HEAD. Read-only `git apply --check` returned0 with no output/conflicts. This verifies textual applicability, not successful deployment or runtime compatibility.

### Existing working-tree changes

```text
M src/simulations/helper/antara_models.py
 M src/simulations/pointing/ANTARA_pointing_budget.py
 M src/simulations/power/ANTARA_MCR.py
?? build/
?? figures/pointing/
?? src/antara_simulations.egg-info/
?? tmp/
```

Tracked differences from HEAD:

- Helper `MissionConfig`: default RAAN15°→30°.
- Pointing study: inclination97.4°→97.6°, duration1day→365days, step10s→30s, elevation mask10°→15°, altitude comment corrected. The existing duration comment still says1day; no correction made here.
- MCR power study: duration365→3650days, inclination97.4°→97.6°, mass4→3kg.

Untracked groups: `build/`, `figures/pointing/`, `src/antara_simulations.egg-info/`, `tmp/` (including prior validation environments/results). They are not alternative authoritative implementations and must not be overwritten. The pointing and MCR entry points are expensive and must not be imported/executed as a smoke test.

## Patch scope and prerequisites

1. Environment diagnostic: remove dimensionally invalid Hz/dead-time arithmetic on nodal differential values; export `spectral_rate_density_hz_per_mev`. Consumers of removed diagnostic keys need checking. No new detector efficiency or integral width is supplied.
2. Legacy merged bins: add effective intervals and inactive-slot metadata. Consumers must use the effective metadata; this does not qualify the new FPDU response.
3. Battery throughput: count only accepted charge/discharge; exclude curtailed energy and unmet load. No aging coefficient or orbit/power constant changes.
4. Statistics: retain every RAAN's statistics, add RAAN identity, distinguish mean run minima from worst minimum. Existing two-run confidence intervals remain unqualified.

These software-accounting assumptions remain compatible with the approved baseline: no geometry, timing, geographic eligibility, scientific threshold or radiation output is changed. The patch does **not** make historical defaults a2029 run, replace legacy response physics, or integrate the separate visit/checkpoint contracts.

## Safe integration plan once writable

Create a dedicated branch/worktree at the recorded base only after rechecking hashes/status. A clean worktree at HEAD omits the current uncommitted state: preserve a separate snapshot of all three tracked diffs and an inventory of untracked files, then deliberately reproduce the reviewed dirty source prerequisites in the isolated worktree without modifying the original checkout. Keep those prerequisite changes distinguishable from the accounting patch. Do not stash/reset the main checkout or automatically add generated/untracked directories.

Recheck exact source hashes, run `git apply --check`, apply the patch in the isolated integration branch, and verify expected post-patch hashes from `source_identity.json`. Run the tests/gates in `SIMULATOR_REGRESSION_RESULTS.md`. Inspect the final diff for only intended accounting/API changes plus explicitly preserved prerequisite settings. Resolve checkpoint/consumer compatibility before acceptance; passing AST tests alone is insufficient. Production deployment remains a separate recorded outcome from isolated branch tests.

## Next bounded detector-response experiment

First implement a geometry-only ray/path-length fixture for the six approved volumes: launch rays from the+X entrance toward−X through a gap-free **test fixture**, then a configurable-gap fixture. Check ordered front/main intersections, 2+5×14=72mm on-axis active path, off-axis chord lengths, misses, ±Y sensor and ±Z reflector placement, and entrance-only0.25mm aluminium. Gap-free is a numerical fixture, not a selected packaging design. This tests the transport interface and coordinate convention without inventing material, optical isolation or efficiency.

The first physical transport experiment follows material/CAD closure: a bounded monoenergetic proton scan bracketing5/5.5/15MeV and extending to100MeV, with explicit material/physics-list/seed/event budget, scoring each volume's deposition, escape and energy balance. Keep incident truth separate from observable inputs. It cannot qualify optical/electronics response, reconstructed energy or an upper trigger rate by itself. No such run was launched here.
