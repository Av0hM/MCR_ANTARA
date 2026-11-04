> **Approved-baseline follow-up:** The original ingestion audit below is preserved. The unified implementation now accepts this 2026 source as a preliminary 2029 planning reference, verifies its exact polygon cell domain, and incorporates qualified statements in the MCR. See [count-rate reconciliation](FPDU_COUNT_RATE_RECONCILIATION.md) and [implementation record](IMPLEMENTATION_CHANGELOG.md). No raw rate or flux output was changed.

# Count-rate evidence ingestion — 2026-11-04

## Scope and preservation

Recursively inspected `data/raw/payload_count_rate_2026/`: **22 files**. The files were initially inside a named extracted subfolder and subsequently appeared directly in the raw directory during inspection; the final inventory below records the present paths. The audit did not move or edit them. SHA-256 checks against the pre-analysis snapshot confirm all 22 originals unchanged. No MCR LaTeX, payload configuration, grid model or DITL simulator was changed in this task. Existing payload-update changes in the working tree predate this ingestion and were preserved.

The independent validator is [scripts/validate_count_rate_evidence.py](../../scripts/validate_count_rate_evidence.py). Reproductions and the machine-readable inventory/statistics are in [data/derived/payload_count_rate_2026_audit](../../data/derived/payload_count_rate_2026_audit/). They are audit products, not replacement source evidence or detector simulation outputs.

## Environment and source identity

All four IRENE flux text files and all six CSVs contain **7,940 cells**, all at **MJD 61041.0 = 2026-01-01 00:00 UTC**, **600 km**, **GDZ/WGS84 geodetic** coordinates. Latitude and longitude are in degrees; longitude is east-positive (negative values here). This is one fixed-date geographic grid, not a propagated mission trajectory. The folder/report creation dates do not establish a different physical epoch. Nothing in these exports establishes a 2029 environment run or calibration.

| Setting | Evidence and interpretation |
|---|---|
| Software | Raw text headers lines 1–14: IRENE **1.58.001** |
| Species/model | AP9 H+ protons; AE9 e− electrons |
| Flux | **Integral above threshold**, **omnidirectional**, particles cm⁻² s⁻¹; neither per-MeV nor per-steradian |
| Proton output energies (MeV) | 0.1, 0.15, 0.22, 0.33, 0.5, 0.75, 1.1, 1.65, 2.5, 3.75, 5.6, 8.4, 11, 14, 17, 20 |
| Electron output energies (MeV) | 0.1, 0.15, 0.25, 0.4, 0.65, 1, 1.5, 2.3, 3.5, 5.3, 8 |
| Configured statistic | Both `irene_config_*.txt:2` request `FluxOut: percentile, 99`. Mean outputs are present, but the exact mean-generating config/command is absent. |
| Ephemeris | Config line 7 references `C:\IreneSpectrum\grid_ephemeris.txt`; that file and its grid/domain generator are absent. |
| Model database | Config line 9 names a Windows `modelData` directory; database contents/hashes and executable/run logs are absent. |
| Other settings | No explicit magnetic-field settings, seeds, shielding, angular distribution, geometry or detector response parameters are supplied in these nine-line configs. Headers establish omnidirectional output; do not invent unresolved settings from software defaults. |

The `.txt.pct` files each contain only `100`. Their role is not documented in this package. They do not establish a 100th-percentile flux result, a valid worst-case bound or physical validation. The 99 designation is supported by the actual config and `_pctile_flux_99` filenames, not these sidecars. Mean/percentile modes and output naming are described in the [IRENE 1.58.001 User’s Guide, pp. 15, 17–18, 44](https://www.vdl.afrl.af.mil/programs/ae9ap9/files/package/IRENE_Users_Guide.pdf).

## Provenance chain

1. The AP9/AE9 configs request integral flux on the absent ephemeris using the external model database. The four raw text outputs preserve software/model/energy/unit/coordinate metadata. Their upstream generation cannot be rerun solely from these 22 files.
2. `output_csv_converter_protons.py:6–23` and `output_csv_converter_electrons.py:6–23` read the energy header, create `flux_<E>MeV` columns, discard comments and export numerical rows. Both supplied converters are hardcoded to percentile files. All four exported CSVs, including mean files, numerically match their corresponding raw texts exactly. The mean conversion operation is reproducible, although the exact historical converter invocation is not archived.
3. `count_rate_per_cell.py:62–63` defaults to **protons >5.5 MeV** and **electrons >0.35 MeV**. Lines 36–53 interpolate integral flux, lines 68–70 compare row keys, lines 73–77 form species/summed flux proxies and divide by 4π, and line 79 writes six significant digits.
4. Both supplied rate CSVs are independently reproduced from the raw text data. Running the supplied rate script separately against the supplied flux CSVs also produces byte-identical rate CSVs in `/tmp`. See [validation](AP9_AE9_COUNT_RATE_VALIDATION.md) for arithmetic and limitations.

## Additional evidence is a different model family

- **`Anisotropy proton.txt`**: SPENVIS 4.6.14.3582, generated 17 October 2026; AP-8 MAX and UP-MAX anisotropy, 180 look directions. Explicit orbit start is **2028-01-01**, end 2028-01-31; mission interval extends to 2028-02-01. Circular nominal 600 km, inclination 97.79°, RAAN 99.80°. Its `28489` date uses the explicitly declared **1950-01-01 origin**, not the standard IRENE MJD origin. It includes integral directional and differential directional fluxes over 29 energies, 0.1–400 MeV. This is not a directional AP9 correction for the 2026 grid or approved 2029 orbit.
- **`aniso_flux.png`**: visually inspected; directional surface is labeled integral proton flux **>0.10 MeV**, cm⁻² s⁻¹ sr⁻¹, versus polar/azimuth angles. It is consistent in subject with the anisotropy text, but the plotting generator/exact image provenance is absent. Do not derive a correction factor for >5.5 MeV AP9 from this image.
- **`Trapped particle fluxes_peak.pdf`**: both pages inspected. SPENVIS report generated 19 October 2026, **AP-8 MAX**, GSFC 12/66 internal field updated to 1970.0, no external field. Integral per-energy peak fluxes; different energies can peak at different positions/times. These are not an AP9 spectral vector at a common cell. The PDF does not establish its mission epoch; do not assign the anisotropy document's epoch merely from project title.
- **`Trapped electron fluxes_peak.pdf`**: both pages inspected. **AE-8 MAX**, Jensen & Cain 1960 field, no external field; explicitly no local-time variation, and an AE-4 50% non-exceedance annotation. This is not AE9 percentile-99 evidence. The print timestamp is not an environment epoch.
- **`radiation_outputs_protons_final_mean_flux.ods`**: one sheet; all 7,940 data rows exactly match the mean proton CSV. One additional summary formula in **N7942** is `MAX(N1;N7941)`, cached as **199.929387**. It compares the header and last data cell, not the column range. The actual maximum of column N (`flux_3.75MeV`) is **5144.51739 particles cm⁻² s⁻¹**. This is a confirmed erroneous whole-column-maximum calculation if used as such; it does not contaminate the independently matched data rows or rate CSVs. Original workbook preserved.

## Inventory

Paths below are relative to `data/raw/payload_count_rate_2026/`. Full hashes permit independent preservation checks.

| File | Bytes | SHA-256 |
|---|---:|---|
| `Anisotropy proton.txt` | 136233 | `67c845b74885114275f866b8a65ceb5a4ef5559b05d8f52359474f10fbaac8a4` |
| `Trapped electron fluxes_peak.pdf` | 200865 | `f4955d1778153c1fe8521b4eb0b1016999c276149d7a2a42d91ead07a8a7020a` |
| `Trapped particle fluxes_peak.pdf` | 191097 | `76989e1bf1d3c802aaf459633acf53c1b9215aa4169abe05b542a531206d1601` |
| `aniso_flux.png` | 35373 | `f03acaef6d11f95536fa17ca79e080718a6036becc27d0e3c9ee533179a44695` |
| `count_rate_per_cell.py` | 3691 | `71ba163b8d3b0b25d34d07864e8e321e51e08ffda3731f8c4fa42bf7e82a213d` |
| `count_rate_per_cell_mean.csv` | 556658 | `97831148b8976c729974cc0548c21b9807d3da4872809a342a79aee47a517be5` |
| `count_rate_per_cell_peak99.csv` | 578387 | `a9bcc88be7ade3cbfd94297f5725f760be8a85e298ed346579671f9df509a7b8` |
| `irene_config_electron.txt` | 368 | `2eaaacb95c58b447be9dc0f4719e60ca29e4f5859f779643d26cb59ebb0bfced` |
| `irene_config_proton.txt` | 400 | `faa704f2fd9dcdd3d0fc13882a5d2d51c78768b13ae05a537a6086503932bc88` |
| `output_csv_converter_electrons.py` | 763 | `9806b144f4ce9c2ac129c9cceb9e8d28ce3eaab4eb1151f821c0cd12cdc8c754` |
| `output_csv_converter_protons.py` | 759 | `b4a2b70e765ea50b9cd0467a222458c9da0ec48688737ed50d4beb81751e8345` |
| `radiation_outputs_electrons_final.txt.pct` | 5 | `90b53df56816c127246136d4403aba3b26cec599b2b950fb2ba78d6c1fb4e6bf` |
| `radiation_outputs_electrons_final_mean_flux.csv` | 1028572 | `1ae362fdbf8053ce1ba18554097f81da7bdbeefafc46c1afac1cd98163db1183` |
| `radiation_outputs_electrons_final_mean_flux.txt` | 1689487 | `cf87c2867924c613a9eef486336d228f3088cc5fbae611e5b955d6ada842c1be` |
| `radiation_outputs_electrons_final_pctile_flux_99.csv` | 1023452 | `6a5482d32acc8a352306f40dd6c7f7c1c0416c99b0d532000b6c7e59d7e35e10` |
| `radiation_outputs_electrons_final_pctile_flux_99.txt` | 1689492 | `cdffe70777f08381d81ca6a795098f8c9a56c22d39f209c72fa64e40c4d51798` |
| `radiation_outputs_protons_final.txt.pct` | 5 | `90b53df56816c127246136d4403aba3b26cec599b2b950fb2ba78d6c1fb4e6bf` |
| `radiation_outputs_protons_final_mean_flux.csv` | 1610580 | `eda99f7691a48d1c8e118903ea3d4f56b5465d3d6b703d3a51cabd44088f187a` |
| `radiation_outputs_protons_final_mean_flux.ods` | 1389255 | `fc3f36da95039d5509162ab77397bec9f2abc0473e000b769de467a77e3dccf0` |
| `radiation_outputs_protons_final_mean_flux.txt` | 2285033 | `a68d1e39a09f9b8fd631ebcb7dc48d138307ddd7e3c01ba3eb7515a60c32a2b2` |
| `radiation_outputs_protons_final_pctile_flux_99.csv` | 1610477 | `4e36ff6925b981d5a5c9cd3f3718483a8b63a51a3309d6e89d9a5fc27f616a4b` |
| `radiation_outputs_protons_final_pctile_flux_99.txt` | 2285038 | `a33f840384c3a34077f37330260ea2dc491f3699ecee647cbad8765301549da8` |
