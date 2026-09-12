# Iter036 / G47-C — prospective three-state hidden-classical switching optimizer calibration

## Purpose
Response-blind optimizer calibration for a finite explicit three-state hidden-classical switching family whose provenance was validated by terminal G47-P. No RCG-002 target is used.

## Frozen finite family
The hidden CTMC has six directed transition rates. Conditional local-sum Hamiltonians use the three fixed response-blind direction templates from G47-P on A and B, with one positive amplitude scale for each subsystem/state pair. The 12-dimensional parameter vector is therefore:
- six directed transition rates;
- six local-field amplitude scales (`A0,A1,A2,B0,B1,B2`).

Frozen bounds:
- each transition rate in `[0.015, 0.14]`;
- each field amplitude scale in `[0.55, 1.45]`.
The hidden chain is initialized in its stationary distribution. Every parameter point retains the explicit hidden-classical/product-unitary construction.

## Frozen positive controls
Four deterministic hidden parameter vectors are generated from fixed seeds `1701..1704`, strictly inside the bounds and without inspecting any RCG target. Two independent QMC methods are required: `sobol_lsq` and `lhs_lsq`.
Total matrix: `4 controls x 2 methods = 8 lanes`.

## Frozen objective and optimizer
Fit the visible reduced superoperator trajectory at times `t={0.15,0.45,0.9,1.4}`.
- 16 QMC starts per lane;
- refine best 4 with bounded trust-region least squares;
- maximum 500 function evaluations per refinement;
- hidden control parameters are never inserted as optimizer starts.

## Frozen acceptance
For each lane:
- all objective values finite;
- recovered model passes the same explicit CTMC/provenance structural conditions as G47-P;
- maximum visible-channel Choi/TP diagnostics remain within G47-P tolerances;
- maximum trace distance over the frozen 16 product probes and four trajectory times between hidden-control and recovered channels `< 0.002`;
- relative 12-parameter recovery error `< 0.08` after the frozen coordinate normalization by parameter ranges;
- held-out visible-channel max trace distance at `t={0.27,0.67,1.17}` `< 0.003`.

Aggregate PASS requires all 8 lanes PASS.

PASS classification:
`THREE_STATE_CLASSICAL_SWITCHING_OPTIMIZER_CALIBRATED`.

Otherwise classify `THREE_STATE_CLASSICAL_SWITCHING_OPTIMIZER_CALIBRATION_NOT_ESTABLISHED` or structural/numerical failure as appropriate.

## Locks
This is calibration only: no RCG-002 target, no comparator-separation claim and no readiness increment. Only terminal PASS may authorize a separately preregistered adversarial G47-A using the identical 12-dimensional family/search map. Frozen bounds, controls, starts and thresholds must not be changed post hoc.
