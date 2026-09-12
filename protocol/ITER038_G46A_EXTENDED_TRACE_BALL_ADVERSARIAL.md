# Iter038 / G46-A — prospective extended trace-ball adversarial gate

## Authorization
Production is forbidden unless terminal G46-C classifies `EXTENDED_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED_CAP8_CAP16`. This protocol is frozen after G46-C calibration but before any G46-A production result is viewed.

## Frozen comparator families/search map
Use the identical G46-C real-symmetric PSD trace-ball parameterization `C=A^2`, `A=A^T`, at the prospectively fixed caps:
- `tr(C)<=8`;
- `tr(C)<=16`.

Use the same two QMC methods, 32 starts, refine best 6, bounded trust-region least squares and max 1200 function evaluations. No cap/family/threshold change after production is permitted.

## Frozen RCG-002 toy targets
Use exactly the same four target shards, trajectory times, probe states and target convention as terminal G44-A:
`U(t)=cos(theta*t) I - i sin(theta*t) Z⊗Z`, with unchanged `CASES`.

## Frozen lane/pair/nesting rules
For every cap/method/shard lane:
- structural and physical admissibility must pass;
- maximum trace-distance gap `>1e-4`.

For every cap and shard:
- both Sobol and LHS lanes must pass;
- absolute Sobol/LHS best-gap difference `<=0.002`.

Because the cap16 physical family strictly contains cap8, for every shard require
`min_gap(cap16) <= min_gap(cap8) + 0.002`.
This is a prospectively frozen optimizer/nesting validity condition and must not be relaxed after viewing results.

All 16 lanes, all eight method-pairs and all four nesting checks are required.

Aggregate PASS classification:
`DERIVED_SCOPED_EXTENDED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP8_CAP16`.

Any lane, pair or nesting-rule failure means the frozen support rule is not established and must be preserved without retuning.

## Scope ceiling
This covers only finite bounded basis-invariant real-PSD Markovian random-Hamiltonian families up to `tr(C)<=16`. It is not an unbounded-PSD result and not a no-go against arbitrary classical mediators, memory, LOCC or semiclassical gravity. A terminal PASS may justify rubric review `62% -> 63%` only if G47-A has not already consumed that same rubric point; readiness increments must not double-count overlapping comparator coverage.
