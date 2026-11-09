# Thermal evidence validation

One telemetry history, one extrema summary and four original plots were supplied. 43,201 unique labels span0–86400s at2s spacing. Every K/°C pair satisfies T°C=TK−273.15; all summary extrema and extrema timestamps reproduce from this history. Its 'hot_case'/'cold_case' columns are **not separate HOT and COLD runs**. Their ±10°C columns are arithmetic allowances, not demonstrated margins to actual hardware limits.

| Node | Minimum °C | Maximum °C | Time-weighted mean °C |
|---|---|---|---|
| +X | -20.775172 | 19.913685 | -8.907486 |
| -X | -17.220090 | 26.911357 | -5.479560 |
| +Y | -15.865257 | 19.950717 | -9.506988 |
| -Y | -25.957601 | 31.239020 | -7.624734 |
| +Z | -22.401387 | 29.600945 | 0.717747 |
| -Z | -23.301149 | 19.918552 | -16.551927 |
| internal | -14.060918 | 21.159372 | -6.048409 |

Means use trapezoidal integration over recorded labels; no extra interval is appended after86400. Internal heat is1.9–4.9W. Largest simultaneous face-to-face temperature spread is31.703814°C. This lumped-node spread is not structural stress or a spatial finite-element temperature gradient. No selected-component limit mapping is supplied; time beyond qualified limits and compliance margins are UNKNOWN, not zero.

## Model and provenance

Candidate `ThermalSimulator.py` is hashed in the source-reference manifest. It defines six faces plus internal bus,3U10×10×34cm with X long axis,600km97.6°e.001RAAN15°3kg, default2000-03-01 and24h; actual run config/epoch is UNKNOWN. Orbit DP853 and thermalRK4 with10substeps per2s step are **candidate defaults**, not measured numerical convergence. No time-step sensitivity rerun performed. Initial source default293.15K conflicts with nonuniform first logged temperatures (e.g. internal293.156795K); a historical advance-before-log offset is suspected, not corrected without exact source.

Thermal balance C dT/dt=absorbed solar+albedo+EarthIR+internal−emission+conductive exchanges. Candidate solar1361W/m² at1AU, deep-space2.7K, latitude-dependent albedo0.25equator/0.62pole andIR260/205W/m², with flat fallbacks0.30/237. Internal1.8kg×800J/kg/K; face coupling0.05W/K. Face optical properties and masses are engineering assumptions, not measured flight finishes; full scalar defaults are archived in `candidate_source_defaults.json`.

Candidate internal schedule is independent of DITL: baseline1.5W, charging0.4W, eclipse heater0.8W, relay increment3W and detection1.2W. LVLH or prescribed tumbling is configurable. Nominal/HOT/COLD config factories exist, but no distinct bounding-case outputs/manifests accompany this delivery. The surface-cell representation also needs reconciliation with the approved fixed+Z/two-deployable solar geometry. Do not add DITL electrical loads directly as identical thermal dissipation.

## Interpretation and next tests

This is a reproduced model temperature envelope, not thermal feasibility closure. Negative internal temperatures raise a component/heater validation question; without selected hardware limits no failure or safety margin is asserted. Obtain actual run case, attitude, optical properties, conductances and node-component mapping, then bounded thermal timestep/energy-balance convergence and coupled DITL heat schedules; separate hot/cold environment cases and TVAC correlation follow. Structural modal/vibration/shock qualification is untouched.

Figures `validated_history.png` and `validated_envelope.png` show the single history, internal heat, min/max and weighted means. No invented component-limit or independent hot/cold plot is supplied.
