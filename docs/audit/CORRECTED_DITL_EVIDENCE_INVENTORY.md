# Corrected DITL evidence inventory

Candidate folder: `evidence/new-science-ditl/`. Original files remain untouched. Exact headers, timestamp extrema, byte sizes and SHA-256 hashes: `data/derived/ditl_correction_2026-11-09/inventory.json`. No producing code or runtime manifest was supplied. Full identity is not inferred from current design.

| Scenario/file | Rows | Bytes | SHA-256 |
|---|---:|---:|---|
| `leop_24h_ANTARA_Science_telemetry.csv` | 7696 | 7603039 | `8363c5901b5f46df36c3287a054e0c93923ca2ea78d9f8beb87f3e3b8f956a85` |
| `leop_24h_ANTARA_Science_mode_transitions.csv` | 42 | 3098 | `e17dc5a340319f8e85a984226ce8a1a7880558b01b17f68998851beb5db5db2a` |
| `leop_24h_ANTARA_Science_saa_passes.csv` | 6 | 1134 | `00e315da31105e681a395f44dd3db4a9dd44c1f55a69b0e5c2f0e325b8e2382d` |
| `leop_24h_ANTARA_Science_proton_passes.csv` | 6 | 31507 | `db18822b19cafa18ed073e02fdeb7f082d7cf3530bf592b23e8dbb3d4838279f` |
| `leop_24h_ANTARA_Science_gs_contacts.csv` | 2 | 324 | `7574fc13a1c7e1037163802f0106306c5c1dedc0ed592827b13724d3779f9837` |
| `leop_24h_ANTARA_Science_slew_events.csv` | 20 | 1371 | `40bb24fe6fec4c5d1e3b638c0b6ca65f5ebb40782d5fcd667dc3c1187be3dc92` |
| `leop_24h_ANTARA_Science_detumble_events.csv` | 1 | 441 | `06fbe4ad701d603e66663e2d971edee8142bf6829c05670b9ed9b920d13e9d16` |
| `leop_24h_ANTARA_Science_rejected_transitions.csv` | 0 | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| `no_leop_24h_ANTARA_Science_telemetry.csv` | 6553 | 6771073 | `a652068558a96c200ca9e84c7a88bcd9ade869a945b019848bb4179c6c287585` |
| `no_leop_24h_ANTARA_Science_mode_transitions.csv` | 40 | 2970 | `9f85cb30d1299e9254e0b467b2556e09897980069923223eb66d4e95eb4e1650` |
| `no_leop_24h_ANTARA_Science_saa_passes.csv` | 6 | 1132 | `289e2d814f8f23579e1ca6f44dbf515098fb041e03a29967913c7bb1eb3d3415` |
| `no_leop_24h_ANTARA_Science_proton_passes.csv` | 6 | 30668 | `78165c6400db2b85b52b3306ba257ffa60083f31a40aa8819c44babc9c133bb0` |
| `no_leop_24h_ANTARA_Science_gs_contacts.csv` | 2 | 322 | `64cd1094631abc3b7c6ec8a0f4a235a87358d6e2e5b8bd2c78eabf26087b500c` |
| `no_leop_24h_ANTARA_Science_slew_events.csv` | 20 | 1370 | `ef0d3e310ebb0b9358e3970624aec55acc97e492f53616af2106667334660483` |
| `no_leop_24h_ANTARA_Science_detumble_events.csv` | 0 | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| `no_leop_24h_ANTARA_Science_rejected_transitions.csv` | 0 | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| `leop_1yr_ANTARA_Science_telemetry.csv` | 1434872 | 1673705738 | `015cfb89b1d2a563494bc70c88c8a3a2fd040d66224a3b2fbc46c5287c86182e` |
| `leop_1yr_ANTARA_Science_mode_transitions.csv` | 16283 | 1228659 | `dcf3cd00b1e32f90b11a191ebd28d1008fc1f007355ccd28ce41545d70bdf7e7` |
| `leop_1yr_ANTARA_Science_saa_passes.csv` | 2346 | 403039 | `d4ac1da955d2516d10d94c448904cbd05c076d4d2b78bdbe9bd9e236432625c6` |
| `leop_1yr_ANTARA_Science_proton_passes.csv` | 2298 | 11759096 | `ed4d1ea73e0c8255ff305b3f9300578c5d92ed2f18bfac974f665ab5c6b63ea2` |
| `leop_1yr_ANTARA_Science_gs_contacts.csv` | 820 | 100382 | `83603a40e7626c6572a3c9a02aee78b731d7c73fb3b44fd7623000b7f89d688a` |
| `leop_1yr_ANTARA_Science_slew_events.csv` | 7928 | 543786 | `58f1603f8dcbd7e68162ba54548446b94ecdf11dbb807851279984c463de2458` |
| `leop_1yr_ANTARA_Science_detumble_events.csv` | 1 | 441 | `06fbe4ad701d603e66663e2d971edee8142bf6829c05670b9ed9b920d13e9d16` |
| `leop_1yr_ANTARA_Science_rejected_transitions.csv` | 0 | 1 | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |

Registry: `evidence/science-ditl/run_registry.json`. All three telemetry files span zero to their named horizons; source/state semantics and cross-file consistency still require validation. Empty one-byte event files have no schema and establish no positive event evidence. Initial downstream references are captured before edits in `initial_dependency_inventory.json`.
