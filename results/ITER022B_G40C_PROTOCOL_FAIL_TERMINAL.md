# ITER022B / G40-C — terminal classification

Run: `34708292521`
Head: `80107b2d65c154d4e6a0cc52a2c1fffd8408dd8d`
Aggregate job: `103592442138`
Summary artifact: `10302841233`
Summary digest: `sha256:d9a7f85a11c0178b2bd77b4700f43af4411ef7f2e654914197c4228941ce29c3`

## Frozen aggregate

- 8/8 lanes structurally valid.
- Sobol: 3/4 scientific support; worst max trajectory trace gap `6.968784036465157e-14`; minimum recovered BLP `0.009095291786343718`.
- LHS: 3/4 scientific support; worst max trajectory trace gap `0.23376009861349822`; minimum recovered BLP `0.022161811061063297`.
- Aggregate `scientific_support=false` under unchanged recovery `<0.002` and BLP `>0.02` rules.

## Root cause

The failure is dominated by frozen shard 3. Direct evaluation of the preregistered hidden target shows its own BLP total positive trace-distance increment is `~0.0090952917864`, below the declared strict-BLP family threshold `0.02`. Sobol recovers that target essentially exactly (`max trace gap 6.97e-14`) and therefore correctly reproduces its sub-threshold BLP. LHS on the same invalid control additionally suffers an optimizer basin miss (`max trace gap 0.2337600986`, recovered BLP `0.0730982283`).

Classification:

`PROTOCOL_DESIGN_FAIL / OUT_OF_FAMILY_POSITIVE_CONTROL + LHS_OPTIMIZER_MISS_ON_INVALID_CONTROL`

This is not a scientific failure or success of RCG-002, and it does not invalidate G40-P's implementation/witness PASS. No old lane is retroactively promoted and neither frozen threshold is weakened.

## Authorized next step

A separate prospective control-eligibility gate must certify every new hidden control has BLP `>0.02` before any G40-C2 optimizer calibration is launched. Only after that eligibility PASS may calibration be retried as a new gate.
