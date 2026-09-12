# ITER029 / G40-TM-C — trace-metric-aligned RTN optimizer calibration

Status: **PREREGISTERED BEFORE PRODUCTION**.

## Motivation

The existing RTN branch remains unresolved: G40-RC-D2 found persistent optimizer/objective-geometry nonrobustness on adversarial shard 3. That terminal result is preserved. G40-TM-C does not reinterpret or rescue it. It is a new response-blind calibration of a different optimizer whose objective is aligned directly with the frozen scientific metric.

## Frozen physical family and witness

Use exactly the finite hidden-classical symmetric RTN family, parameter bounds, four-time/six-probe trajectory, and candidate-axis-frame-covariant BLP witness already frozen in G40-RC-C. Use the eligible positive controls `CONTROLS_C2`; no RCG-002 target/result is used.

Strict admissibility remains axis-covariant BLP total positive increment `>0.02`.

## Frozen optimizer

Two independent designs per hidden control:
- `sobol_powell`
- `lhs_powell`

For each method/control:
- 24 response-blind starts in normalized 8D parameter space;
- rank starts by the **maximum trace-distance trajectory gap itself**, not residual L2;
- refine best 4 starts with bounded Powell minimizing that same max-trace metric;
- `maxfev=1600`, `xtol=1e-6`, `ftol=1e-8`;
- hidden coordinates are never inserted as starts.

The L2 residual may be reported diagnostically but cannot select the winner.

## Frozen PASS rule

A lane supports calibration iff:
- all reported quantities are finite;
- hidden positive control is itself strict-BLP eligible;
- recovered candidate has axis-covariant BLP `>0.02`;
- recovered maximum trace-distance trajectory gap `<0.002`.

Joint calibration PASS requires all 8 lanes (4 controls x 2 designs) to support. No threshold or family bound may be changed after production starts.

## Classification

PASS: `TRACE_METRIC_ALIGNED_RTN_OPTIMIZER_CALIBRATED`.

Otherwise: `TRACE_METRIC_ALIGNED_RTN_CALIBRATION_NOT_ESTABLISHED`, preserving lane-level failures.

## Authorization ceiling

PASS may authorize only a separately preregistered new prospective RTN adversarial gate. It cannot alter terminal G40-RC-A/G40-RC-D2, cannot raise programme readiness by itself, and cannot establish a universal non-Markovian/classical-mediator claim.
