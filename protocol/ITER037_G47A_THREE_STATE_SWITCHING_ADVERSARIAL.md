# Iter037 / G47-A — prospective adversarial three-state hidden-classical switching comparator

## Authorization
Production is forbidden unless terminal G47-C classifies `THREE_STATE_CLASSICAL_SWITCHING_OPTIMIZER_CALIBRATED`. G47-P and G47-C are already terminal prerequisites; this protocol is frozen before any G47-A production target result is inspected.

## Frozen comparator family/search map
Use exactly the calibrated 12D G47-C family:
- six directed CTMC transition rates in `[0.015,0.14]`;
- six local-field amplitude scales in `[0.55,1.45]` on the fixed G47-C direction templates;
- stationary hidden initialization;
- two QMC methods `sobol_lsq`, `lhs_lsq`;
- 16 starts, refine best 4, bounded trust-region least squares, max 500 function evaluations.

Every candidate retains explicit three-state hidden-classical/product-unitary provenance. No expansion of bounds/family is permitted after viewing results.

## Frozen RCG-002 toy targets
Use exactly the G44-A target convention and the same four frozen target shards:
`U(t)=cos(theta*t) I - i sin(theta*t) Z⊗Z`, with `theta` derived from the unchanged `CASES` table used by G44-A/G42-A, at the same four trajectory times.

The optimization residual is the full visible superoperator trajectory, matching the G47-C optimizer calibration object. The scientific gap metric is the maximum trace distance over the frozen 16 product probes and four times.

## Frozen lane/pair rules
For every method/shard lane:
- structural/provenance validity must pass;
- gap `> 1e-4`.

For every target shard:
- both Sobol and LHS lanes must satisfy the lane rule;
- absolute Sobol/LHS best-gap difference `<= 0.002`.

All four shards are required.

Aggregate PASS classification:
`DERIVED_SCOPED_THREE_STATE_CLASSICAL_SWITCHING_COMPARATOR_SUPPORT`.

Any method-agreement or lane-support failure classifies the frozen support rule as not established; thresholds and family must not be changed post hoc.

## Scope ceiling
This is only one explicit finite 12D three-state stationary CTMC classical-memory family. A PASS is not a no-go against arbitrary classical memory, non-Markovian channels, LOCC, semiclassical gravity or all classical mediators. A terminal PASS may trigger a rubric review of programme readiness `62% -> 63%`; no increase is authorized before terminal aggregate classification.
