# Iter045 / G50-A — Four-state hidden-classical switching adversarial transport preregistration

Status: **FROZEN BEFORE IMPLEMENTATION / BEFORE RCG-002 PRODUCTION RESULTS**

## Prerequisite
Terminal Iter044/G50-C classification must be `FOUR_STATE_CLASSICAL_SWITCHING_OPTIMIZER_CALIBRATED` for the exact finite 20D four-state stationary hidden-classical CTMC switching family. This prerequisite is satisfied by run `34734256210`, summary artifact `10310302963`.

## Scientific question
Can the exact calibrated 20D four-state hidden-classical switching family approximate the frozen RCG-002 controlled-phase target on the existing four-shard target panel, under the same family bounds and optimizer discipline used in response-blind calibration?

## Frozen comparator family
Exactly the Iter044/G50-C family, without enlargement or target-dependent reparameterization:
- 12 off-diagonal CTMC rates, each in `[0.015, 0.14]`;
- 8 local field-scale parameters, each in `[0.55, 1.45]`;
- four stationary hidden states;
- conditional Hamiltonians are local sums only;
- stationary hidden distribution derived from the CTMC generator;
- no direct two-body Hamiltonian term;
- no imported physical assumptions or results from QGR/KMQGB/RQIR.

## Frozen target panel
Use the already-established RQIR-CG RCG-002 convention and the four pre-existing CASES inherited by earlier comparator gates, corresponding to controlled-phase strengths `theta = [0.025, 0.10, 0.40, 1.40]`.

Training times: `[0.12, 0.35, 0.75, 1.25]`.
Prospective held-out times: `[0.23, 0.58, 1.05]`.
Product-state probe panel: exactly the family helper panel used by Iter043/044.

## Frozen optimization protocol
Eight independent lanes: `sobol_lsq` and `lhs_lsq` x four target shards, `fail-fast:false`.
Per lane:
- dimension 20;
- 32 QMC starts;
- retain 6 best starts for bounded least-squares refinement;
- max 800 function evaluations/refinement;
- same bounds and physical provenance checks as Iter044;
- target information is used only in this adversarial gate, after calibration has terminally passed.

## Frozen observables
For the best admissible candidate in each lane record:
1. maximum product-probe trace-distance gap on training times;
2. maximum product-probe trace-distance gap on held-out times;
3. full-superoperator residual norm on training times;
4. CTMC/provenance validity, TP residual and Choi minimum eigenvalue.

## Frozen thresholds and aggregate rule
- Nonzero scientific gap threshold: `1e-4` on **both** training and held-out maximum probe gaps.
- Sobol/LHS agreement for each shard: absolute train-gap difference `<=0.002` and absolute held-out-gap difference `<=0.003`.
- Structural validity requires 6 finite refined candidates in every lane.
- Admissibility requires physical provenance for the selected best candidate.

Terminal classifications:
- structural/numerical invalidity: `G50A_IMPLEMENTATION_OR_NUMERICAL_INVALID` (not a scientific result);
- any provenance/admissibility failure: `G50A_BLOCKED_ADMISSIBILITY`;
- if all 8 lanes are admissible, all 8 exceed `1e-4` on train and held-out, and all four Sobol/LHS pairs meet agreement thresholds: `DERIVED_SCOPED_FOUR_STATE_CLASSICAL_SWITCHING_COMPARATOR_SUPPORT`;
- otherwise: `G50A_FROZEN_SUPPORT_RULE_NOT_MET`.

The last outcome is a scoped negative/nonclosure result only; it does not imply that RCG-002 is realizable by the family unless an actual admissible near-zero witness is established and independently checked.

## Scope ceiling
Any positive separation result applies only to this finite bounded stationary four-state/20D hidden-classical CTMC switching family on the frozen four-shard RCG-002 panel and finite probe/time sets. It is not an all-classical, all-memory, all-semiclassical, or quantum-gravity no-go theorem.

## Claim locks
No `NEW_PHYSICS_FOUND`, no `FULL_QUANTUM_GRAVITY`, no `RQIR_REQUIRES_RCG002`, no general classical-memory exclusion, and no readiness increase merely for compute volume. Frozen family, targets, thresholds, controls and interpretation rules may not be weakened after production results are seen.
