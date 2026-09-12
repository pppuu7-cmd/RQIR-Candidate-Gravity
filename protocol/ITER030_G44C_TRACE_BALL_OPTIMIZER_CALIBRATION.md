# ITER030 / G44-C — basis-invariant PSD trace-ball optimizer calibration

Status: **PREREGISTERED / IMPLEMENTABLE, BUT PRODUCTION LAUNCH LOCKED UNTIL TERMINAL G44-P PASS**.

## Authorization lock

G44-C production is forbidden unless Iter028 / G44-P terminally classifies `BASIS_INVARIANT_TRACE_BALL_PSD_REPRESENTATION_VALIDATED` on all 24 frozen lanes. This file is frozen before that terminal result in order to reduce latency without weakening the gate sequence.

## Frozen family

Exactly the G44-P family:

`C = A^2`, `A=A^T`, `||A||_F <= 2`, equivalently real PSD `tr(C)<=4`.

Use 21 weighted symmetric coordinates `w`: diagonal entries are stored directly and strict-lower off-diagonals as `sqrt(2) A_ij`, so `||w||_2 = ||A||_F`. Search variables `z in [-1,1]^21` map surjectively to the closed trace ball by

`w = 2 z / max(1, ||z||_2)`.

This is a representation choice for optimization only; the physical family remains the basis-invariant trace ball.

## Positive controls

Six response-blind hidden controls, one each at effective ranks 1..6, generated independently of RCG-002 with disjoint seeds. Hidden positive square roots `A_h >=0` are scaled to frozen Frobenius norms:

`[0.75, 1.05, 1.30, 1.55, 1.80, 2.00]`

for ranks 1..6 respectively. Thus the panel includes rank-deficient PSD boundary controls and one exact radial trace-ball boundary control. Exact hidden coordinates are never inserted as starts.

## Observable design

Reuse the already frozen four times and six product probes used by G42 calibration. This gate contains no RCG-002 target/result.

## Frozen search

Two independent QMC designs per rank:
- `sobol_lsq`
- `lhs_lsq`

Each design produces 32 starts inside the 21D unit ball using a 22D QMC point: 21 dimensions generate a Gaussian direction and the 22nd fixes radial CDF `r=u^(1/21)`. Refine the best 6 starts by trajectory L2 residual with bounded `scipy.optimize.least_squares`, search variables `z in [-1,1]^21`, maximum 1200 function evaluations, `ftol=xtol=gtol=1e-10`.

## Frozen lane PASS

A lane supports calibration iff all quantities are finite and the best candidate satisfies simultaneously:
- max trace-distance trajectory gap `<0.002`;
- relative Kossakowski error `<0.02`;
- recovered effective rank at eigenvalue threshold `1e-5` equals hidden rank;
- min Kossakowski eigenvalue `>= -1e-10`;
- `tr(C) <= 4 + 1e-9`.

Joint G44-C PASS requires all 12 lanes = six ranks × two methods.

## Classification

PASS: `BASIS_INVARIANT_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED`.

Otherwise: `TRACE_BALL_PSD_OPTIMIZER_CALIBRATION_NOT_ESTABLISHED`, preserving exact failing ranks/methods.

## Authorization ceiling

PASS authorizes only a separately preregistered prospective G44-A RCG-002 adversarial comparator gate using the identical trace-ball family and search map. G44-C itself cannot raise programme readiness or establish a basis-invariant/full/unbounded PSD no-go.
