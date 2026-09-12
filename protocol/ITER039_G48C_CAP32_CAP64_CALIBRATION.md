# Iter039 / G48-C — prospective cap32/cap64 trace-ball optimizer calibration

## Purpose

Calibrate the already-used basis-invariant real-PSD trace-ball optimizer at wider finite trace caps before any RCG-002 adversarial production at those caps. This gate is response-blind and cannot increase candidate-program readiness.

## Frozen object

Use `C=A^2`, `A=A^T`, with weighted symmetric coordinates and radial trace-ball map exactly as in G46-C. Frozen caps: `{32,64}`.

Hidden positive controls: effective ranks `1..6`, generated independently of RCG-002 using the same deterministic hidden-control recipe and radial fractions as G46-C:
`(0.375,0.525,0.650,0.775,0.900,1.000)`.

Two independent QMC search methods: `sobol_lsq` and `lhs_lsq`.

Frozen search settings: 32 starts, refine best 6, bounded trust-region least squares, max 1200 function evaluations; same time/probe panel as G46-C.

## Frozen scientific thresholds

Every one of 24 lanes (`2 caps × 2 methods × 6 ranks`) must be structurally valid and satisfy simultaneously:

- max trajectory trace-distance recovery gap `< 0.002`;
- relative Kossakowski recovery error `< 0.02`;
- recovered effective rank equals hidden rank using eigenvalue threshold `1e-5`;
- minimum recovered Kossakowski eigenvalue `>= -1e-10`;
- recovered `tr(C) <= cap + 1e-8`.

No threshold, hidden-control family, rank panel, cap, optimizer setting or interpretation rule may be changed after production results are viewed.

## Frozen classifier

- all 24 lanes pass: `CAP32_CAP64_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED`;
- structural invalidity: `G48C_IMPLEMENTATION_OR_NUMERICAL_INVALID`;
- otherwise: `G48C_FROZEN_CALIBRATION_RULE_NOT_MET`.

A red/green CI state alone is not the scientific classifier.

## Claim locks

This is calibration only. PASS does not support RCG-002 separation, does not establish an unbounded-PSD limit, and does not raise readiness. Only terminal PASS may authorize a separately preregistered cap32/cap64 adversarial transport gate with explicit nesting against terminal cap16 results.
