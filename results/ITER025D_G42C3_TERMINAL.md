# Iter025D / G42-C3 terminal result

## Provenance

- Run: `34711048394`
- Head / launch commit: `35f719fdad8af1e2f8fdd71727c84abec3857c2a`
- Aggregate job: `103601042911`
- Summary artifact: `10303627020`
- Summary artifact digest: `sha256:a9fa4ccaa8f6f79540311deb3f8a42be74661e2793d6dc7e5092570a7e52e3d1`

## Frozen gate

Rank-completion positive-control calibration for the same G42 boundary-capable bounded real-PSD Cholesky chart, covering the previously missing effective ranks 1 and 3 with four hidden controls and both Sobol/LHS methods. Same bounds, times/probes, 32 starts, top-6 refinements and frozen recovery/Kossakowski/rank rules as G42-C2.

## Raw aggregate classification

All 8/8 lanes passed.

- Sobol: 4/4 support; worst trace gap `4.2872736979461425e-07`; worst relative Kossakowski error `8.398809261492516e-06`; rank match 4/4.
- LHS: 4/4 support; worst trace gap `7.34537126692358e-07`; worst relative Kossakowski error `1.5813386032144557e-05`; rank match 4/4.

Classification: **`PSD_BOUNDARY_RANK_COMPLETION_CALIBRATED`**.

## Interpretation

Together G42-C2 and G42-C3 prospectively calibrate the frozen optimizer across effective PSD ranks 1–6 within the bounded Cholesky chart. This is methodology/positive-control evidence only, not RCG-002 comparator evidence and not an unbounded-PSD calibration theorem. Their joint PASS authorizes the separately preregistered G42-A adversarial gate.
