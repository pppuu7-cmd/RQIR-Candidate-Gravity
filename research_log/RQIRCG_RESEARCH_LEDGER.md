# RQIR-CG research ledger

This file is the clean authority ledger for `RQIR-Candidate-Gravity` only. The pre-existing `research_log/RESEARCH_ACTIVITY_LEDGER.md` contains legacy material from another research line and must not be used as scientific evidence for RQIR-CG.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, gate discipline and mathematical tools, but not imported physical assumptions, ansatz coefficients or desired conclusions.

## Latest authoritative results

| Iteration | Gate | Run / head | Classification | Result ceiling |
|---|---|---|---|---|
| Iter010 | G28 full-Bloch comparator audit | run `34692403874`, head `3d8d3f969a22c22c1526b00f42377c2d41f87a04` | `DERIVED_SCOPED_NEGATIVE_COMPARATOR_RESULT` | 24/24 nonzero gaps; finite single-axis Markovian family only. |
| Iter011 | G29 robustness suite | run `34694101699`, head `c4c6f0d35e4e57a2105facafee2bdddc8036a52f` | `DERIVED_SCOPED_ROBUSTNESS_SUPPORT` | 24/24 structural valid and support; finite single-axis Markovian family only. |
| Iter012 | G30 additive multi-channel comparator | run `34694264478`, head `fa9be36b422b84614b03f96de7c37660059f2d74` | `DERIVED_SCOPED_NEGATIVE_COMPARATOR_RESULT_WITH_MULTICHANNEL_ROBUSTNESS` | K=2/K=3 finite-search gaps remained about 0.025, but nearest-distance interpretation later blocked by calibration failure. |
| Iter013 | G31 global-search calibration | run `34695076098`, head `f32ecf1949f1e7d6c577b201b73c517d4605fdb7` | `SCIENTIFIC_CALIBRATION_FAIL / GLOBAL_OPTIMIZER_NOT_VALIDATED` | Positive K=2 recovery max gap `0.0604612 > 0.002`; adversarial minima diagnostic only. |
| Iter014 | G32 positive-control optimizer diagnosis | run `34695441883`, head `ea54a3ae9694366c3bebe06c13b775af44d46833` | `POSITIVE_CONTROL_OPTIMIZER_FAIL / LOCAL_BASIN_GEOMETRY_OR_CONDITIONING` | Exact representability and permutation plumbing pass, but local/global trace-distance searches fail some hidden controls. |
| Iter014B | G32-J positive-control Jacobian | run `34695478444`, head `706245fa183845556aa020bc99d2a4d86e4e3060` | `FULL_LOCAL_RANK / STRONGLY_ILL_CONDITIONED_DIAGNOSTIC` | Rank 11/11 on all controls; condition number up to ~4034. |

### Iter010 aggregate

Summary artifact `10297865845`: 24/24 structural passes; 24/24 nonzero full-sphere gaps; 0/24 off-plane improvements above frozen 1% criterion; minimum full-sphere gap `0.012499674481709782`.

### Iter011 aggregate

Summary artifact `10297528599`, digest `sha256:b7f80fc91bba1b45371ec1cec1865ddbc9dab3a1ab7c4138a94d4a5064287356`: 24/24 structurally valid; minimum continuous adversarial gap `0.02500020131464493`; minimum Choi eigenvalue `-7.229908172761597e-16`; minimum identifiability rank `6/6`; maximum finest RK4 cross-check error `1.0037722995948985e-11`.

### Iter012 aggregate

Summary artifact `10298417946`, digest `sha256:7c4095c8ddd329b53973fd1bc5b0b823455b2b543c26fe370aba748806b6f0b0`: 20/20 structurally valid; minimum K=2 finite-search gap `0.025014400602647237`; minimum K=3 finite-search gap `0.025028081208365957`. G31 subsequently showed the nearest-comparator optimizer was not calibrated, so these remain scoped finite-search diagnostics rather than certified distance bounds.

### Iter013 aggregate

Summary artifact `10297704949`, digest `sha256:cfe6a47700e929b4c3c515362db16e2b1618ca64723bfd96dbc38856d9522871`: 20/20 structurally valid, but the positive in-family K=2 recovery maximum gap was `0.06046122957245775` versus frozen `<0.002`. Therefore `scientific_interpretable=false` and all G31 adversarial minima are diagnostics only.

### Iter014 / G32 aggregate

Summary artifact `10299010209`, digest `sha256:86035287985cc1b1793df8298b919b47067b81aa22b757a5a841df9245389638`:

- 20/20 structural valid;
- oracle replay 4/4 PASS with maximum gap `0.0`;
- K=2 channel-swap symmetry 4/4 PASS; max Liouvillian difference `9.947092584916169e-17`, max target gap `3.918320310696023e-16`;
- local perturbed-source recovery 2/4 support, maximum gap `0.02431103093558268`;
- deep-global DE+polish 2/4 support, maximum gap `0.017872382285720974`;
- hybrid global/local 1/4 support, maximum gap `0.040425953741512866`;
- `plumbing_valid=true`, but no tested global method calibrated;
- aggregate diagnosis `LOCAL_BASIN_OR_OBJECTIVE_GEOMETRY_FAIL`.

Interpretation: the hidden in-family targets are exactly representable by the frozen K=2 parameterization, so the failure is not basic model plumbing. The direct trace-distance optimizer is nevertheless unreliable at stronger controls. Adversarial RCG-002 interpretation remains blocked.

### Iter014B / G32-J aggregate

Summary artifact `10298208349`, digest `sha256:e0a48b3cc49ab4ab3514b26de8c47cf2ad7b3e7fb72b7bb5c9e91e262a9490ee`:

- derivative controls valid 4/4;
- effective Jacobian rank `[11,11,11,11]` for 11 K=2 parameters;
- maximum two-step Jacobian discrepancy `1.2393500576443816e-09`;
- maximum retained-subspace condition number `4033.8739690901716`.

This rules out a simple local rank-deficiency explanation and points toward strong conditioning plus a difficult/non-smooth optimization landscape. Rank/conditioning are diagnostics only, not physics evidence.

## Current frontier

Optimizer calibration is still open. The next prospectively authorized gate is G33: normalize all K=2 parameters to a unit box and optimize a smooth density-matrix residual with bounded least-squares and independent global-to-local constructions. Hidden source coordinates are forbidden as initializers. The frozen scientific acceptance remains the original trace-distance recovery gap `<2e-3` on all four positive controls. RCG-002 adversarial targets remain forbidden until a single prospectively specified method passes all four controls; then the adversarial K=2/K=3/K=4 calculation must be rerun under that exact method.

## Stable readiness rubric

- independent scope/claim discipline: closed
- weak-field coherent candidate construction: closed at toy-channel level
- basis/rotation robustness of finite comparator: closed
- CPTP/PSD and numerical robustness of finite comparator: closed
- multi-channel comparator breadth through K<=3: closed
- exact in-family representability/plumbing: closed
- optimizer calibration / adversarial nearest-comparator reliability: **OPEN; G31/G32 failed calibration**
- correlated/general Kossakowski comparator: open
- non-Markovian comparator layer: open
- externally anchored observable/holdout programme: open
- full candidate-gravity dynamics / continuum completion: open

Current internal programme readiness: **46%**. This is a construction/readiness metric, not a probability of physical correctness.

## Claim locks

Do not promote finite-family gaps to claims that all semiclassical gravity, all classical mediators, or all alternatives to quantum gravity are excluded. Do not use green CI as a scientific verdict. Do not weaken the frozen `2e-3` positive-control criterion. G31/G32 adversarial diagnostics remain non-interpretable until a calibrated method exists and the adversarial targets are rerun prospectively.