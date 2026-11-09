# Detumble evidence validation

## Summary arithmetic

50,000 rows;16,133 reported successful (32.266%),33,867 nonconverged. All nonconverged completion values are infinity; do not drop them from the success denominator. Among the16,133 successful rows only: median951.5s,95th percentile2569.0s,worst3026.5s. Whole-population median/95th convergence cannot be established because fewer than half converge and individual censor times are absent. No all-run reliability confidence interval is justified without the sampling design/independence contract.

25,473 rows hit the reported rate cap. All50,000 peak wheel-momentum values are zero; this does not prove an unloaded flight wheel. Initial spin magnitudes span0.00079694–59.99821467deg/s; initial acceleration magnitudes span0.00001317–0.99995368deg/s². All vector norms reproduce their scalar columns. First row is a baseline6,−5.5,4.5deg/s with0.12,−0.015,0.08deg/s², reported1009s completion. These are not the integrated DITL2460s event, and must not be combined as repeated trials of one identical model.

## Source compatibility and missing identity

No original trial pickle, configuration, seed, timeout log, quaternion histories or time histories were supplied. Exact producer revision remains UNKNOWN. Current authoritative `leop_detumble_mc.py` (hashed, read-only) rejects nonzero initial acceleration and derives it from torques; supplied50,000 rows all contain nonzero acceleration. Thus current source is **not a compatible generating implementation**. The prior base51933bb source likewise rejects these inputs. Do not rerun it with changed assumptions and claim reproduction.

Candidate current source uses synthetic magnetic field rather than orbit-specific IGRF; its nominal rotation of a +Z inertial field about Z leaves that vector unchanged. This limits that candidate environmental variation; it is not proof of the unknown historical generator. Candidate defaults:0.2A m² dipole,30µT field,BDOT gain3e4,2deg/s handover,0.1deg/s stable-rate, wheel torque0.001N m andmomentum0.01317N m s;0.5s trial step and seed42 CLI default. None is assigned as verified runtime input. Initial attitude distribution, actual field model, gains, sampling law, timeout/failure reasons and independent seeds remain UNKNOWN. Empirical spin/acceleration ranges do not prove a particular random distribution.

No angular-rate convergence histories, control effort, saturation timeline or power histories exist in this delivery; they cannot be reconstructed from summary columns. A derived empirical completion curve retains all50,000 rows as denominator and ends at32.266%; the spin-bin plot includes per-bin sample counts in `validation/spin_groups.csv`. Original figures remain preserved. No artificial convergence trace is drawn.

## PDR verification

Retain reaction wheels+magnetorquers; no CMG reinstatement. Obtain the historical generator and timeout/initial-condition manifest; replace independent acceleration initialization only in an explicitly approved physics revision. Then verify angular momentum/energy, bounded timestep convergence, axis/field geometry, actuator saturation and magnetic authority using representative orientations and orbit fields. Record successes, timeouts and numerical failures distinctly. Actual acquisition power, handover and flight reliability require coupled-model and hardware evidence. A single2460s DITL startup is not Monte Carlo reliability.
