# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active iteration: `ITER015`
Phase: `INDEPENDENT_RQIR_DERIVATION / SMOOTH_OPTIMIZER_CALIBRATION`

## Canonical status

- Candidate-model/programme readiness: **46%**
- Theory established: **0%**
- Active seed: `RCG-002 Relational controlled-phase channel`
- Independent-from-QGR construction contract: **FROZEN**
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`

Readiness is an internal construction metric, not a probability that the model is correct. Neither G31 nor G32 raises readiness because positive-control optimizer calibration remains open.

## Iter013 / G31

Run `34695076098`, head `f32ecf1949f1e7d6c577b201b73c517d4605fdb7`, aggregate artifact `10297704949`, digest `sha256:cfe6a47700e929b4c3c515362db16e2b1618ca64723bfd96dbc38856d9522871`.

Classification: `SCIENTIFIC_CALIBRATION_FAIL / GLOBAL_OPTIMIZER_NOT_VALIDATED`.

The positive in-family K=2 recovery control failed with maximum gap `0.06046122957245775 > 0.002`. Therefore G31 adversarial K=2/3/4 minima remain diagnostics only and cannot be promoted to physics evidence.

## Iter014 / G32 terminal result

Authoritative run `34695441883`, head `ea54a3ae9694366c3bebe06c13b775af44d46833`, aggregate artifact `10299010209`, digest `sha256:86035287985cc1b1793df8298b919b47067b81aa22b757a5a841df9245389638`.

Twenty frozen positive-control lanes completed and were structurally valid.

- exact oracle replay: 4/4 PASS; maximum gap `0.0`;
- K=2 channel-swap symmetry: 4/4 PASS; max Liouvillian difference `9.947092584916169e-17`, max target gap `3.918320310696023e-16`;
- local perturbed-source recovery: only 2/4 PASS; maximum gap `0.02431103093558268`;
- deep global DE + polish: only 2/4 PASS; maximum gap `0.017872382285720974`;
- hybrid global/local: only 1/4 PASS; maximum gap `0.040425953741512866`;
- no tested global method calibrated on all four controls.

Classification: `POSITIVE_CONTROL_OPTIMIZER_FAIL / LOCAL_BASIN_GEOMETRY_OR_CONDITIONING`.

Interpretation: the model plumbing and K=2 parameterization can reproduce the hidden in-family target exactly, so G31 failure is not a basic representability bug. However trace-distance optimization remains unreliable, including locally at stronger controls. RCG-002 adversarial interpretation remains blocked.

## Iter014B / G32-J terminal result

Authoritative run `34695478444`, head `706245fa183845556aa020bc99d2a4d86e4e3060`, aggregate artifact `10298208349`, digest `sha256:e0a48b3cc49ab4ab3514b26de8c47cf2ad7b3e7fb72b7bb5c9e91e262a9490ee`.

- finite-difference derivative controls valid 4/4;
- effective local rank `11/11` on all four hidden K=2 controls;
- maximum two-step Jacobian discrepancy `1.2393500576443816e-09`;
- maximum retained-subspace condition number `4033.8739690901716`.

Classification: `FULL_LOCAL_RANK / STRONGLY_ILL_CONDITIONED_DIAGNOSTIC`.

This is a numerical/identifiability diagnosis only. It neither validates nor falsifies RCG-002. It motivates changing optimizer coordinates/objective while preserving the original final trace-distance acceptance rule.

## Active authorized gate — Iter015 / G33

Goal: test whether a smooth residual formulation with parameter normalization closes the same four positive controls without using the hidden truth as an optimizer initialization and without inspecting RCG-002.

Frozen requirements before execution:

1. map all 11 K=2 parameters affinely to unit-box coordinates `[0,1]`;
2. use a smooth real residual vector formed from the Hermitian density-matrix difference for bounded nonlinear least squares;
3. use only deterministic prospectively fixed global initial designs (Sobol/Latin-hypercube or fixed seeded starts), never the hidden source or its perturbation;
4. test multiple independent search constructions in parallel, including multistart least-squares and an independent smooth global-to-local route;
5. the optimizer may minimize the smooth residual, but scientific acceptance remains the unchanged trace-distance recovery gap `< 0.002` on all four hidden controls;
6. method calibration requires all four controls PASS under one prospectively specified method;
7. RCG-002 adversarial targets remain forbidden in G33. Only after a method calibrates may a later gate rerun K=2/3/4 adversarial targets under that exact method. G31/G32 gaps cannot be promoted retroactively.

## Claim locks

Forbidden:

- `NEW_PHYSICS_FOUND`;
- `FULL_QUANTUM_GRAVITY`;
- `RQIR_REQUIRES_RCG002`;
- claim that all classical/semiclassical mediators are excluded;
- treating green CI as scientific PASS;
- treating G31/G32 adversarial diagnostics as physics evidence;
- changing the frozen `2e-3` recovery threshold after seeing results;
- importing physical assumptions or desired conclusions from QGR/KMQGB/RQIR.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + EXACT_IN_FAMILY_REPRESENTABILITY_CONFIRMED + FINITE_COMPARATOR_SEARCH_UNCALIBRATED + G33_SMOOTH_CALIBRATION_REQUIRED`.