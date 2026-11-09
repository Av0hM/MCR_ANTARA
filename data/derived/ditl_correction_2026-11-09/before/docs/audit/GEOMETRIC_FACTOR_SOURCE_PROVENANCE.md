# Geometric-factor source provenance

Audit date: 2026-11-06. All nine supplied files preserved; eight scientific artifacts and one compiled Python cache. No simulator or raw data modified. Reproduction is arithmetic validation, not detector or mission validation.

## Complete source inventory

| Relative to `evidence/geometric_factor_2026-11-05/` | Bytes | SHA-256 |
|---|---:|---|
| `__pycache__/grid_common.cpython-311.pyc` | 17643 | `b687832610e86f71afbe6cb652f4418440f1df460a428d6a043c7a18842f51d2` |
| `cell_pass_counts.csv` | 305077 | `e379d5bb77f39d8f5ec72f11cc056ea02fbcf837ff2181b5481a9811f434db4b` |
| `cell_proton_count_rate_hz.npy` | 537728 | `f0176d2d903a413cad50cb1fa06c58df9aa5a3a0e2e12b77c1301559331b9af1` |
| `cell_proton_rate_heatmap.png` | 93733 | `0d7de918277f6ba2feecd4aa1c7140210bcd21d882dbb7c0adf73c54ccf2f78b` |
| `cell_proton_rates.csv` | 25173294 | `a91820e5a3e356ae4252dc191b20faadb6e2ef2af9aef41f41b87d040bafc530` |
| `cell_saa_flag.npy` | 67328 | `2a7f9c1bae62b5c7ff38a5c94ddeee68dbc4e88d3a97ca013da092e44d47e261` |
| `required_G_coarse_channels.csv` | 1276 | `eb8d1f9f25fd2b2a13f3124dcab47d12c7e80f2e417f57f4c634c919c611ea9f` |
| `required_G_fine_bins.csv` | 18479 | `ba745caa5524f09187beb70a02f6669f9fb1959a4e522e45a30c15e8864e66fe` |
| `required_geometric_factor.py` | 11200 | `eb9a0fdb18061b81de094a2028ed5a6c2fc809a593ca69fc63bcd0d33f5de468` |

The `.pyc` file is inventoried only, not executed or treated as scientific evidence. Machine-readable inventory: `data/derived/geometric_factor_2026-11-05_audit/source_inventory.json`.

## Provenance chain and gaps

| Artifact / question | Established evidence | Status |
|---|---|---|
| Dwell table | Byte-identical to `PDR Sims/Simulation Outputs/18-Month Simulation/cell_pass_counts.csv` in `/home/sammo/Downloads/PDR Sims-20261021T072428Z-1-001.zip` | Archive identity confirmed; 18-month label is not runtime verification |
| Dwell generator family | Archive `count_cell_passes.py` accumulates sampled cell time and continuous cell-entry counts | Exact executed revision/configuration/checkpoint unavailable |
| Duration / RAAN | Candidate source lines 98,108,156 default to 3 days, RAAN 15°, 2026-01-01; 1 s sampling and 600 km orbit | Defaults cannot establish actual run duration/RAAN/epoch |
| Actual dwell | 7,940 cells; 98–294 s/cell; total 1,453,556 s; 15–40 recorded visits/cell | Confirmed table values, not independent science observations |
| Radiation generator family | Archive `step1_generate_irene_inputs.py:44–53` requests AP9 mean, Integral, GDZ 600 km, 2026-01-01; only thresholds 5 and 100 MeV | Candidate family only; supplied table has 65 thresholds |
| Rate converter | Archive `step2_process_irene_outputs.py:43–44,133` reads a mean-named file and uses G=0.314 | Cannot be exact unmodified generator: supplied rate/flux ratio proves G=1 |
| Actual radiation epoch / percentile | No raw IRENE spectrum, run configuration, model/database version, ephemeris or runtime manifest for the 65-threshold table | UNVERIFIED; neither mean nor percentile, nor 2026/2029 generation is independently established |
| Intended use | Preliminary requirement study for the approved 2029 mission | Does not relabel historical inputs as 2029-generated |
| Rate semantics | All 65 integral-rate columns equal corresponding flux/(4π), to floating-point tolerance; isotropic G=1 cm² sr | Ideal incident-rate proxy, unit efficiency, not trigger/accepted counts |
| Energy semantics | 65 thresholds over 5–100 MeV; adjacent integral differences | Incident-spectrum intervals, not reconstructed channels |
| Geographic mask | Exact positive-area intersection with approved polygon at 0.5° | 7,940 unique cells; scientific eligibility remains separate |
| NPY maps | 120×560 arrays, same flags and same rate values at every CSV cell | Numerically consistent with CSV |
| PNG | AP9-labeled integral-above-5 MeV rate proxy at G=1, consistent quantity with headline column (peak 370.658470 Hz); producer runtime absent | Not a G map or detector response; supplied title is clipped; not reused in MCR |

The dwell sum is pooled cell occupancy, **not mission elapsed time**. It exceeds the entire duration of an unscaled three-day single-spacecraft run. This establishes that the available default source cannot alone explain the table; it does not prove 18 months or justify extrapolation. No duration multiplier is applied.

The candidate grid source spans longitude −270…10° for array indexing, latitude −50…10°, in 0.5° cells. All supplied polygon cells lie within canonical −90…−10° longitude and −35…0° latitude. Vertices and positive-area boundary rule match `config/science/saa_polygon_v1.json`; touching-only cells are excluded. Coordinates are geographic degrees, interpreted as geodetic by the candidate pipeline, not magnetic coordinates.

Archive member hashes are in `upstream_archive_inventory.json` next to the reproduced outputs. Candidate files were inspected read-only in `/tmp/antara-payload-update/PDR Sims/`. The older verified MJD 61041 AP9/AE9 dataset in `data/raw/payload_count_rate_2026/` is a distinct dataset and does not fill the missing provenance of these 65 energy thresholds.

## Reproducibility boundary

The supplied CSV-to-required-G calculation is reproducible locally. Exact orbit propagation and radiation regeneration are not reproducible from this evidence bundle. Request the executed source/config, full ephemeris, IRENE headers/database/version, spectrum output, duration/completion manifest, restart identity, and any scaling or pooling applied to dwell. No annual campaign was launched.
