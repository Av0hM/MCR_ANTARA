# Response and reconstruction verification plan

No current response is qualified. `require_qualified_response()` rejects historical five-layer, Rev. 2.1 single-block and current design identifiers alike until a validated response is registered. Configuration is not a response implementation.

1. Freeze controlled CAD/ICD: six scintillator volumes, common material, ±Y SiPMs, ±Z Teflon, entrance Al, gaps, surfaces and optional rear decision. Compare independent geometry volumes/axes before transport.
2. Compare optical isolation alternatives without preselecting one:

| Option | Consequence to evaluate | Calibration/interface evidence |
|---|---|---|
| Isolated blocks | Potential deposition localization and independent multiplicity; light yield depends on separators | Separator material/thickness, surface finish, channel gains, leakage maps and mechanical tolerances |
| Partial coupling | Cross-talk may encode position but mixes energy deposition across blocks | Wavelength/angle-dependent boundaries, inter-block transfer, spatial scans and response stability |
| Common coupling if feasible | Shared light could increase collection yet obscure longitudinal deposition | Optical feasibility, sensor weighting, position degeneracy, inversion conditioning and temperature dependence |

3. Transport species/energy/angle grids for the exact 250 µm entrance and full structure. Include proton 5–100 MeV plus below/above bounds and electrons/other relevant species; record incident truth, deposits, escape and secondary ancestry separately. Do not treat last hit-layer boundary as stopping endpoint or global/world dose as sensitive-volume dose.
4. Model light output only with selected scintillator/quenching/optical properties; validate collection, SiPM noise/gain/saturation and temperature behavior with bench data. Front 5.5–15 MeV and dE/dx functions require deposition/path-length evidence, not just thickness.
5. Select/test acquisition architecture: discriminator thresholds, coincidence, ADC response, channel aggregation, dead time and finite buffers. Measure trigger→accepted→classified→lost flows and livetime under mixed fields and burst traces.
6. Calibrate response matrix/unfolding and trained-model candidates on separate calibration sets. Held-out detector observables must be the inputs; truth energy is only the evaluation target. Test monoenergetic and injected continuous spectra, migration, species confusion, saturation, calibration shifts, uncertainty coverage and low-count/background cases.
7. Define eligible cells, independent observations, calibrated operational channels and temporal slices with science owners; preserve all committed tier thresholds. Couple actual interval exposure/pointing/livetime to response and storage/downlink before computing mission success.

Provisional log64 reporting edges are a software format choice, not detector resolution. Histogram tests include final-edge inclusion, under/overflow and invalid counts; merging exports changed edges/widths. A Poisson relative-error proxy is insufficient for calibration/systematic/background-dominated cases. No Monte Carlo or physical validation is fabricated here.
