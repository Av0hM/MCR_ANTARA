# SAA polygon and coverage acceptance contract

Source: `PDR Sims/grid_common.py:27–31` in the supplied archive and corresponding Science SAA polygon. Current machine-readable contract: `config/science/saa_polygon_v1.json`. Coordinate order is **(longitude, latitude)**, east-positive WGS84 geodetic degrees, longitude normalized to [-180,180).

Closed vertices: (-90,-5), (-80,-20), (-60,-35), (-40,-35), (-20,-25), (-10,-15), (-20,-5), (-50,0), (-70,0), (-90,-5).

Global degree grid origin (-180,-90); a cell belongs when its planar longitude/latitude polygon intersection has **positive area**. Boundary-touch-only cells are excluded. This is a geometric mask, not equal-area sampling or a physical flux contour. The former (-270,-50) aligned allocation yields the same overlapping cells at these resolutions; 130° × 60° rectangle cardinalities are superseded.

| Resolution | Positive-overlap cells | Meaning |
|---|---:|---|
| 5° | 92 | Geometric MMSC-scale domain |
| 1° | 2020 | Geometric MSC-scale domain |
| 0.5° | 7940 | Geometric EMSC-scale domain |

The independent rectangle-clipping implementation in `scripts/fpdu_contracts.py` reproduces these counts. Both supplied count-rate CSV key sets exactly equal the 0.5° domain, with no missing/duplicate cells. This closes geographic alignment for this convention; it does not validate the unrecovered tier-disposition generator.

Accounting contract: interval-start geometry and positive duration; adjacent samples of the same cell form one visit; cell leave/re-entry creates another visit; multiple visits in one continuous regional SAA crossing share one passage ID. Leaving the region and returning creates another passage. Coarsen interval coordinates **before** visit counting, never sum fine-cell visit totals as coarse passes. Gaps/overlaps are errors, not zero exposure. Accumulate geometric and science-enabled seconds separately; incomplete intervals cannot establish an annual mission. The implementation assumes crossing times supplied by sampling/event detection; timestep convergence on a synthetic exact-boundary case is not convergence of real orbital sampling.

Do not equate: orbital revolution; regional crossing; cell visit; independent opportunity; science-enabled exposure; all-particle triggers; classified protons; statistically valid measurement; stored/downlinked record.

**OPEN DECISIONS:** statistical independence interval/conditions, flux-detectable eligibility, SAA core, channel qualification, background/systematic confidence method and temporal slice treatment. Proposed comparison should report both unique regional-passage-per-cell and contiguous visits, plus elapsed separation, while withholding an independence claim. Eligibility alternatives (all geometric cells versus predeclared flux-detectable cells) must expose both denominators, never drop zero/missing cells silently. MMSC/MSC/EMSC coverage/pass/channel/precision/time thresholds remain unchanged in section 1; pure Poisson N thresholds do not supersede their uncertainty requirements.

Acceptance tests cover continuous visits, leave/re-enter, coarsening/wrapping, touching boundaries, exact raw-cell sets, timestep variation, missing intervals/channels, zero/background-dominated counts and incomplete horizon. Full geometry-to-response-to-downlink acceptance remains open.
