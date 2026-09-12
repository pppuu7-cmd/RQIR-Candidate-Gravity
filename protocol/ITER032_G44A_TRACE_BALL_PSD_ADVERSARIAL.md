# ITER032 / G44-A — prospective basis-invariant PSD trace-ball adversarial gate

Status: **PREREGISTERED / IMPLEMENTABLE, BUT PRODUCTION LAUNCH LOCKED UNTIL TERMINAL G44-C PASS**.

## Authorization lock

Production is forbidden unless Iter030 / G44-C terminally classifies `BASIS_INVARIANT_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED` on all 12 frozen positive-control lanes. This preregistration is frozen before that result to reduce latency without weakening the gate sequence.

## Frozen comparator family

Exactly the G44-P/G44-C physical family:

`C=A^2`, `A=A^T`, `||A||_F<=2`, equivalently real PSD `tr(C)<=4`.

Use exactly the G44-C weighted-symmetric search map and bounded least-squares refinement. This bounded family is basis-invariant and analytically contains the entire old G42 Cholesky box, but it is not the unbounded mathematical PSD cone.

## Frozen RCG-002 toy targets

Use exactly the four target shards and convention inherited from G42-A:

- `scale,t0 = CASES[shard]`, `theta=scale*t0`;
- `U(t)=exp(-i theta*t Z⊗Z)`;
- the same four times `TIMES=[0.15,0.45,0.9,1.4]` and same six product probes.

No target, shard, time or probe may be changed after preregistration.

## Frozen optimizer

Two independent methods per shard: `sobol_lsq` and `lhs_lsq`.

For each method/shard:
- 32 response-blind starts generated inside the 21D unit search ball by the same 22D direction+radius construction as G44-C, with new shard-specific seeds disjoint from calibration;
- rank starts by trajectory residual L2 only, exactly as G44-C/G42-A calibration-to-adversarial transfer;
- refine best 6 with bounded `scipy.optimize.least_squares` over `z in [-1,1]^21`;
- `max_nfev=1200`, `ftol=xtol=gtol=1e-10`.

No target-derived comparator parameter vector is inserted as a start.

## Frozen admissibility

Best candidate must satisfy:
- min Kossakowski eigenvalue `>= -1e-10`;
- `tr(C) <= 4 + 1e-9`;
- max trace-preservation residual `<1e-10`;
- min Choi eigenvalue `>-1e-8`;
- min output-state eigenvalue `>-1e-8` on frozen probes/times;
- max output trace error `<1e-10`.

## Frozen prospective PASS rule

For every shard, both methods must be structurally valid/admissible and satisfy:
- best max trace-distance gap `>1e-4`;
- absolute Sobol/LHS best-gap difference `<=0.002`.

All four shards are required.

## Classification

PASS: `DERIVED_SCOPED_BASIS_INVARIANT_TRACE_BALL_PSD_COMPARATOR_SUPPORT`.

Structurally valid but any frozen shard rule not met: `G44A_FROZEN_SUPPORT_RULE_NOT_MET`.

Structural/numerical failure is separate and cannot be promoted to physics evidence.

## Scope ceiling

A PASS concerns only the bounded basis-invariant real-PSD Markovian classical random-Hamiltonian trace-ball `tr(C)<=4` against the frozen RCG-002 toy trajectories. It is not an unbounded-PSD theorem, not an all-classical or all-semiclassical no-go, and not evidence by itself for full quantum gravity or new physics.

Because this family strictly contains the old G42 bounded chart and removes its local-basis coordinate dependence, a terminal PASS may justify a programme-readiness review as a stronger scoped comparator closure. G44-C calibration alone cannot.
