# Geometric-factor physical interpretation

## What each factor means

A required G from the supplied rates/exposure is a conditional counting requirement. Achievable geometric G integrates accepted straight trajectories and projected aperture. Effective G additionally includes energy/species-dependent transport, detection and selection. Scientific sensitivity also includes livetime, backgrounds and reconstruction. Mission success further requires eligible cells, independent passages, temporal conditions and delivered records. None of the latter quantities is measured by this study.

The current approved geometry remains five 6×6×14 mm blocks and a separate 6×6×2 mm front scintillator: 72 mm nominal active length and 2.592 cm³ active volume. Entry is through +X, inward −X; main SiPMs on ±Y, 11 total; Teflon on ±Z, 0.11 mm per face; EJ-550 grease; no silicon, optional unselected rear detector. Material, gaps, front reflector treatment and optical isolation remain open. The study's EJ-200 density/stopping model is illustrative, not an approved material. No collimator is approved.

## Ideal geometry comparison

For two equal aligned square planes of side a, separation s, G=∫∫s²/(s²+Δy²+Δz²)² dA1 dA2. The kernel includes both cosine projections; isotropic intensity times G gives rate. The source uses n⁴ midpoint samples; the independent calculation reduces the integral to 4∫₀ᵃ∫₀ᵃ(a−u)(a−v)s²/(s²+u²+v²)² du dv and uses Gauss–Legendre quadrature. Units are cm² sr. The s→0 one-sided aperture limit is πa².

| Hypothetical acceptance condition, a=0.6 cm | G (cm² sr) |
|---|---:|
| Unrestricted one-sided planar entrance (s→0) | 1.130973 |
| Second equal plane at 0.2 mm | 1.059847 |
| Cross both faces of 2 mm front element | 0.619075 |
| Equal limiting plane at 4.8 mm | 0.297433 |
| Cross front and farthest plane at 72 mm | 0.002488494 |

These are alternatives, not selected designs. A 4.8 mm collimator-to-front distance applies only to that plane pair; a full-depth condition would require its distance plus the stack depth. G=0.3 is a study evaluation value, not demonstrated flight acceptance. The 72 mm two-plane value is approximately 145–201 times below broad-band 10% requirements, or 23–32 times below 25% requirements. This does not rule out early-stopping-event science with another validated trigger topology. Conversely, some fine-bin requirements exceed even π×0.36 for a front-only single aperture; that indicates tension under these exposure/efficiency/entry assumptions, not a universal physical lower bound or a selected redesign.

For the source's artificial s=0.02 cm floor, n=30 returns 1.097735638 versus converged 1.059847049, a 3.575% excess. The floor itself changes the physical zero-separation aperture. Independent n=80/160 values agree within 1e-9 relative for tested separations; reduced-midpoint n=480 agrees within 1e-4. At 7.2 cm, n=30 is already close (0.002488506). Source quadrature is not uniformly adequate across depth.

## Ray tracing versus transport

The bounded ray fixture uses six contiguous, aligned boxes, no gaps: numerical depth u=−X, transverse coordinates Y/Z. On-axis active path is 72 mm; an entrance-centered 45° track exits a side after 4.243 mm total path and does not reach the rear. For straight rays in a convex aligned prism, hitting entrance and exit squares implies crossing every intervening box. Thus the two-plane integral equals all-through ray acceptance for this fixture. It does not model stopped particles, side-entry triggers or mechanical gaps. This is an analytic geometry equivalence, not a Monte Carlo response result.

The optional study model assigns an incident-bin midpoint to a stopping layer using on-axis CSDA range and uses that layer's **entry-plane** G. It does not require containment to actual stopping depth or handle angular path-length changes, scattering, straggling, side escape, threshold/coincidence logic, reflectors, structures or optical sharing. A single G by stopping-layer index cannot qualify six-volume response. Midpoint allocation near stopping transitions also needs energy-grid convergence.

Transport-and-trigger acceptance and calibrated effective G remain **uncomputed**. Differences from ideal G cannot be quantified without inventing response; they are not set to unity. Required next bounded experiment: ray-box agreement against the analytic two-plane integral, then fixed-grid proton energies 5,5.4,5.5,6,10,20,40,100 MeV and selected angles through geometry-matched entrance Al, with material/gaps/trigger choices explicitly versioned. Score deposited energies, track exits, stopping volumes and trigger observables; keep truth energy separate from reconstructed estimates. Add electrons for background/trigger capacity. Obtain bench/calibration data before effective-G claims.

## Shielding and energy convention

The default required-G tables impose a **hard incident-energy cutoff of 5.4 MeV**. They do not transport through aluminium. The default is hardcoded without derivation. The source docstring example `--window-al-um 250` misleadingly suggests automatic cutoff derivation; actual derivation also requires `--cut-from-window`. The optional source CSDA routine yields **5.952391 MeV** for 250 µm Al with its density 2.699 g/cm³ (areal density 0.067475 g/cm²). Neither 5.4 nor 5.5 is reproduced by this approximation. No baseline value was silently replaced.

Its Bethe approximation omits correction terms, scattering and straggling; it integrates down to 0.3 MeV with an empirical low-energy range floor. Its docstring assertion of ~2% validation against PSTAR water has no accompanying evidence and does not validate aluminium or the unselected scintillator. `exit_energy` also returns zero for residual range ≤0.002 g/cm², a separate numerical threshold. Do not promote this to a transmission curve.

[NIST's stopping-power methodology](https://physics.nist.gov/PhysRefData/Star/Text/programs.html) describes low-energy fitting and corrections absent from this simplified model. A bounded [PSTAR](https://physics.nist.gov/PhysRefData/Star/Text/PSTAR.html) comparison must check aluminium projected/CSDA ranges around 5–7 MeV, density/areal thickness, low-energy integration and interpolation. Then transport must quantify angular thickness, straggling and scattering. PSTAR range alone does not establish a detector efficiency or sharp physical cutoff.

The table energy is interpreted as incident spectrum before the modeled entrance cutoff; no evidence establishes post-shielding or reconstructed energies. Input integral thresholds extend through 100 MeV; subtraction isolates finite bands but does not provide a differential calibrated spectrum. No double transport is present in the default arithmetic. The raw spectrum is absent, so upstream shielding cannot be independently excluded: obtain the IRENE generating settings before combining this table with additional attenuation. Do not apply both a shielded rate and the same shield response twice.
