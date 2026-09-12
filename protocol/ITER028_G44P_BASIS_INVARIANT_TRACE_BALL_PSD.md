# ITER028 / G44-P — basis-invariant PSD trace-ball representation pre-gate

Status: **PREREGISTERED BEFORE PRODUCTION**.

## Motivation

G42-A closed a real scoped comparator layer, but G42-BC showed that the frozen single Cholesky coordinate box is not invariant under local basis rotations: 10/24 response-blind rotated controls left that box. G44-P is a new, broader representation pre-gate; it does not alter G42-A and is not a post-hoc rescue of its numerical result.

## Frozen family

Use a real symmetric 6x6 matrix `A` and define

`C = A^2`, with `A=A^T` and `||A||_F <= R`, `R=2.0`.

Therefore `C >= 0` and `tr(C)=||A||_F^2 <= 4`. Conversely every real PSD `C` with `tr(C)<=4` has the symmetric positive square root `A=sqrt(C)` and is represented exactly. The family definition is invariant under orthogonal basis changes because `tr(O C O^T)=tr(C)`.

The old G42 Cholesky box is analytically nested inside this family: with 6 diagonal entries bounded by 0.60 and 15 strict-lower entries bounded by 0.30, `||B||_F^2 <= 6(0.60)^2+15(0.30)^2 = 3.51 < 4`.

## Response-blind panel

24 lanes = effective ranks 1..6 x four held-out local `SO(3)_A x SO(3)_B` rotations. Hidden PSD controls use seeds disjoint from G42/G43 and are generated independently of RCG-002.

For every lane freeze:
- rank preserved at eigenvalue threshold `1e-10`;
- PSD floor `>= -1e-10`;
- exact symmetric-square-root reconstruction relative error `<1e-10`;
- `||sqrt(C)||_F <= 2 + 1e-12` before and after local basis rotation;
- generator local-basis covariance relative error `<1e-10`;
- analytic old-box nesting check must be true.

## Classification

`BASIS_INVARIANT_TRACE_BALL_PSD_REPRESENTATION_VALIDATED` iff all 24 lanes satisfy every frozen condition.

Otherwise classify as `TRACE_BALL_REPRESENTATION_OR_COVARIANCE_FAIL` with the exact failed condition preserved.

## Authorization ceiling

PASS authorizes only a separately preregistered positive-control optimizer calibration in the exact same trace-ball family. It does **not** authorize an RCG-002 adversarial run, a full unbounded-PSD theorem, an all-classical no-go, or any readiness increment by itself.
