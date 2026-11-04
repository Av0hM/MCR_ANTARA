# Geometry verification

**VALIDATED RESULT, arithmetic and configuration scope only.** `tests/test_fpdu_contracts.py:GeometryTests` checks the current immutable revision, XYZ orientation, sensor faces/counts and separate timing fields.

| Calculation | Result | Source |
|---|---:|---|
| Main volume | 14 × 6 × 6 = 504 mm³ | Confirmed user dimensions |
| Five main volumes | 5 × 504 = 2520 mm³ | Same |
| Front volume | 2 × 6 × 6 = 72 mm³ | Same |
| Total material | 2592 mm³ / 1000 = 2.592 cm³ | Exact unit conversion |
| Main / total X material | 70 / 72 mm | No gaps or packaging included |
| Coated Z | 6 + 2 × 0.11 = 6.22 mm | Confirmed per-face thickness |
| SiPMs | 5 × 2 + 1 = 11 | Does not determine ADC count |

Appendix A.2 contains the XZ side view (viewing from −Y toward +Y) and YZ cross-section (from +X toward −X). Incoming arrow points toward −X. Main SiPMs attach at ±Y; Teflon appears at ±Z. Grease/sensor thickness and drawn gaps are schematic, not dimension inputs. Optional rear hardware is excluded.

No current custom FPDU CAD/ICD was recovered from the supplied COTS component archive. Historical Geant4/GDML represents a different stopping telescope. Material density and optical properties are unselected, so material volume cannot establish mass, light output, stopping range, resolution or 5–100 MeV response. Front coating and readout face remain open.

Geometry acceptance next: controlled CAD with dimensions/tolerances and reference frame, interface clearance, shielding location and all six volumes; independent CAD/GDML volume and material comparison; transport source at the +X entrance with inward −X direction. Only after optical-isolation selection should optical boundary properties be assigned.
