# Iter026 terminal package — G42-A / G42-R / G42-BC

Date: 2026-09-12

## G42-A — bounded boundary-PSD adversarial comparator

Authoritative run: `34712491707`
Head: `f7f48725a3d57398426f8ac9341a1d11b9cc591f`
Aggregate job: `103605124717`
Summary artifact: `10304400253`
Digest: `sha256:002bea19226bd9b7283a08b36db3e72715762e074f10c40b7114d1e35ac3903c`

Frozen rule: four target shards, Sobol/LHS each admissible, each scientific trace gap `>1e-4`, and within-shard method difference `<=0.002`; all four shards required.

Terminal aggregate:

- shard 0: Sobol `0.03700325124270668`, LHS `0.03701733499594546`, difference `1.4083753238774976e-05`;
- shard 1: Sobol `0.1463716306513109`, LHS `0.14637041941069723`, difference `1.2112406136688403e-06`;
- shard 2: Sobol `0.5276672796201998`, LHS `0.5276813340757002`, difference `1.4054455500400742e-05`;
- shard 3: Sobol `0.8197294896504166`, LHS `0.819101112669069`, difference `0.0006283769813475448`.

All eight lanes were structurally valid/admissible. Minimum gap `0.03700325124270668 > 1e-4`; all four Sobol/LHS differences are below `0.002`.

Scientific classification: **`DERIVED_SCOPED_BOUNDARY_PSD_COMPARATOR_SUPPORT`**.

Scope ceiling: bounded 21-coordinate real-PSD 6x6 Markovian classical random-Hamiltonian Kossakowski family only. This is not a full real-PSD theorem and not an all-classical/all-semiclassical statement.

## G42-R — held-out calibration replication

Authoritative run: `34712524241`
Head: `3b53451c192c8bcaedd39105d1c9b9b3ae3aa6e6`
Aggregate job: `103604804647`
Summary artifact: `10303143301`
Digest: `sha256:81fa588873316be4c243657cf7e2ac2f0aa08f092de05c969188c39d70c20f10`

All 12/12 held-out positive-control lanes passed across effective ranks 1–6. Worst trace gap was `3.9203174236860917e-07` (rank 1); worst relative Kossakowski error was `7.245639283979663e-06`; all rank recoveries matched.

Scientific classification: **`PSD_BOUNDARY_HELDOUT_CALIBRATION_REPLICATED`**.

Interpretation: methodology robustness only; it does not alter the G42-A verdict and does not independently raise readiness.

## G42-BC — response-blind basis/chart audit

Authoritative run: `34712857575`
Head: `11b5a0604ada235a4504990966b89f8f89857471`
Aggregate job: `103606238137`
Summary artifact: `10304851327`
Digest: `sha256:e171c028ed31cd28fd19b1a1f1fd3a1dd91d9aa93a6be641bbfe580ad5b47e4c`

All 24/24 implementation-covariance lanes passed; maximum generator-covariance errors were of order `4.8e-16`, far below the frozen `1e-10` tolerance. However only 14/24 rotated controls remained inside the single frozen Cholesky box; 10/24 exited it. Rank-wise inside counts were: rank1 `1/4`, rank2 `1/4`, rank3 `4/4`, rank4 `2/4`, rank5 `2/4`, rank6 `4/4`.

Scientific classification: **`BOUNDED_CHART_ROTATION_COVERAGE_LIMIT_FOUND`**.

This is a response-blind coordinate-coverage limitation, not a failure of basis covariance and not a retroactive failure of the numerical bounded-chart G42-A result. It forbids promoting G42-A to basis-invariant evidence for the entire mathematical real-PSD family.

## Readiness and next gate

G42-A closes one real scoped adversarial rubric item, so programme readiness moves `60% -> 61%`. Theory established remains `0%`. The newly explicit single-chart basis-coverage blocker prevents any stronger PSD-family interpretation.

Next gate is prospectively preregistered as `Iter027 / G43-A`: a response-blind five-chart finite atlas tested on six new hidden PSD controls and six held-out local basis rotations (36 lanes). It cannot change G42-A and cannot raise readiness by itself.
