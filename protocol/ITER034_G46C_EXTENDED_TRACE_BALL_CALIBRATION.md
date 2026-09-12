# Iter034 / G46-C — prospective extended trace-ball calibration

## Purpose
Response-blind optimizer calibration for two strictly prospectively fixed enlargements of the already validated G44 real-symmetric PSD random-Hamiltonian trace ball.

The caps are fixed geometrically as `tr(C)<=8` and `tr(C)<=16`, i.e. consecutive factor-two/factor-four enlargements of the closed G44 cap `4`. They are **not** chosen from any G44-A fitted optimum or target result. No RCG-002 target is used in this gate.

## Frozen family
`C=A^2`, `A=A^T`, with `||A||_F <= sqrt(T)` for trace cap `T in {8,16}`. This is exactly the real-symmetric PSD trace ball `tr(C)<=T` and retains explicit classical Gaussian random-Hamiltonian provenance.

## Frozen positive controls
For each cap and each effective rank `r=1..6`, generate one deterministic hidden PSD control with fixed orthogonal seed and radial fractions of the cap radius
`(0.375, 0.525, 0.650, 0.775, 0.900, 1.000)` for ranks 1..6 respectively. Rank 6 is an exact radial-boundary control.

Two independent search methods are required: `sobol_lsq` and `lhs_lsq`.
Total production matrix: `2 caps x 6 ranks x 2 methods = 24 lanes`.

## Frozen optimizer
- 32 QMC starts per lane;
- refine best 6 with bounded trust-region least squares;
- max 1200 function evaluations per refinement;
- hidden coordinates are never inserted as optimizer starts;
- common trajectory times/probes inherited from the calibrated G44 implementation.

## Frozen lane acceptance
Every lane must be structurally finite and satisfy:
- maximum trace-distance recovery gap `< 0.002`;
- relative Kossakowski recovery error `< 0.02`;
- recovered effective rank equals hidden rank using eigenvalue threshold `1e-5`;
- minimum Kossakowski eigenvalue `>= -1e-10`;
- recovered `tr(C) <= cap + 1e-8`.

Aggregate PASS requires all 24 lanes PASS.

Classification on PASS:
`EXTENDED_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED_CAP8_CAP16`.
Otherwise:
`EXTENDED_TRACE_BALL_PSD_OPTIMIZER_CALIBRATION_NOT_ESTABLISHED` or structural/numerical failure as appropriate.

## Interpretation / locks
This is calibration only and cannot raise programme readiness. A PASS may authorize a **separately preregistered** adversarial gate using the identical physical family/search map. A failure must not be repaired by changing caps, controls, starts, thresholds, ranks or target conventions post hoc. No universal classical/no-go/new-physics claim is authorized.
