# ITER028 / G44-P — terminal basis-invariant PSD trace-ball validation

Run: `34716135086`
Head: `daf40fca9e5e6dc6f98b7673d5c2d34a4cc75552`
Aggregate job: `103615055245`
Summary artifact: `10305175168`
Summary digest: `sha256:2e9f719f90f0d7df07eebed0c6150d12a7c5fde928c06aa19ab14a3b0ea814f4`

## Frozen result

All 24 response-blind rank × basis-rotation lanes passed every preregistered condition.

Family: `C=A^2`, `A=A^T`, `||A||_F<=2`, equivalently real PSD `tr(C)<=4`.

Per-rank support counts were 4/4 for every effective rank 1 through 6. Worst reconstruction errors remained of order `2.34e-15`; worst local-basis generator-covariance error remained of order `4.19e-16`. All rotated controls stayed inside the invariant trace ball. The old G42 bounded Cholesky box is analytically nested because its maximal squared Frobenius norm is `3.51 < 4`.

Terminal classification:

`BASIS_INVARIANT_TRACE_BALL_PSD_REPRESENTATION_VALIDATED`

## Scientific interpretation lock

This is representation/provenance/covariance validation only. It does not establish comparator separation and does not raise programme readiness.

PASS authorizes the separately preregistered Iter030 / G44-C positive-control optimizer calibration in the exact same trace-ball family. No RCG-002 adversarial gate is authorized until G44-C itself terminally passes.
