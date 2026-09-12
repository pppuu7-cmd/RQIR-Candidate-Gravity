# ITER031 / G40-TM-A — prospective trace-metric RTN adversarial gate

Status: **PREREGISTERED / IMPLEMENTABLE, BUT PRODUCTION LAUNCH LOCKED UNTIL TERMINAL G40-TM-C PASS**.

## Authorization lock

Production is forbidden unless Iter029 / G40-TM-C terminally classifies `TRACE_METRIC_ALIGNED_RTN_OPTIMIZER_CALIBRATED` on all 8 frozen positive-control lanes. This preregistration is frozen before that aggregate result to reduce latency without altering the gate sequence.

Terminal historical results remain immutable: G40-RC-A did not satisfy its frozen all-shards rule, and G40-RC-D2 established persistent optimizer/objective-geometry nonrobustness for the old residual-L2 search. G40-TM-A is a new prospective experiment, not a reinterpretation of those runs.

## Frozen family and witness

Use exactly the finite hidden-classical symmetric RTN family, bounds, four-time/six-product-probe trajectory, and candidate-axis-frame-covariant BLP witness used by G40-RC-C and G40-TM-C.

Strict candidate admissibility: axis-covariant BLP total positive increment `>0.02`.

## Frozen RCG-002 toy targets

Use exactly the four shard definitions inherited from G40-RC-A via `CASES` and target convention

`U(t)=exp(-i theta*t Z⊗Z)`.

No target, shard, time, probe, family bound, or witness may be modified after this preregistration.

## Frozen optimizer

Exactly the G40-TM-C search:
- methods `sobol_powell` and `lhs_powell`;
- 24 response-blind starts in normalized 8D parameter space per method/shard;
- starts ranked by the scientific maximum trace-distance trajectory gap itself;
- refine best 4 by bounded Powell minimizing that same maximum trace-distance gap;
- `maxfev=1600`, `xtol=1e-6`, `ftol=1e-8`.

No parent/hidden/target-derived RTN parameter vector is injected as a start.

## Frozen prospective PASS rule

For each of four shards, both methods must produce structurally valid strict-BLP candidates and satisfy simultaneously:
- best gap `>1e-4`;
- recovered candidate axis-covariant BLP `>0.02`;
- absolute Sobol/LHS best-gap difference `<=0.002`.

All four shards are required.

## Classification

PASS: `DERIVED_SCOPED_TRACE_METRIC_RTN_COMPARATOR_SUPPORT`.

If all lanes are valid but any shard fails the nonzero-gap/agreement rule: `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET`.

Structural/numerical failure is separate and must not be promoted to a physics verdict.

## Scope ceiling

Finite symmetric hidden-classical RTN family with this candidate-axis-frame-covariant BLP witness and frozen toy trajectory only. Even PASS is not an all-non-Markovian, all-classical-mediator, semiclassical-gravity, new-physics, or full-QG result.

A terminal PASS may close one scoped non-Markovian comparator rubric item and only then justify a readiness review; calibration alone cannot.
