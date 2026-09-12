# RQIR-CG research ledger

This file is the clean authority ledger for `RQIR-Candidate-Gravity` only. The pre-existing `research_log/RESEARCH_ACTIVITY_LEDGER.md` contains legacy material from another research line and must not be used as scientific evidence for RQIR-CG.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, gate discipline and mathematical tools, but not imported physical assumptions, ansatz coefficients or desired conclusions.

## Latest authoritative results

| Iteration | Gate | Run / head | Classification | Result ceiling |
|---|---|---|---|---|
| Iter010 | G28 full-Bloch comparator audit | run `34692403874`, head `3d8d3f969a22c22c1526b00f42377c2d41f87a04` | `DERIVED_SCOPED_NEGATIVE_COMPARATOR_RESULT` | 24/24 nonzero gaps; off-XZ improvement count 0; finite single-axis Markovian family only. |
| Iter011 | G29 robustness suite | run `34694101699`, head `c4c6f0d35e4e57a2105facafee2bdddc8036a52f` | `DERIVED_SCOPED_ROBUSTNESS_SUPPORT` | 24/24 structural valid and support; finite single-axis Markovian family only. |
| Iter012 | G30 additive multi-channel comparator | run `34694264478`, head `fa9be36b422b84614b03f96de7c37660059f2d74` | `DERIVED_SCOPED_NEGATIVE_COMPARATOR_RESULT_WITH_MULTICHANNEL_ROBUSTNESS` | 20/20 structural valid; K=2 and K=3 adversarial minima remain about 0.025; finite additive independent-channel family only. |
| Iter013 | G31 global-search calibration | run `34695076098`, head `f32ecf1949f1e7d6c577b201b73c517d4605fdb7` | `SCIENTIFIC_CALIBRATION_FAIL / GLOBAL_OPTIMIZER_NOT_VALIDATED` | Positive in-family K=2 recovery failed (`max gap=0.0604612 > 0.002`); therefore K=2/3/4 adversarial minima are diagnostic only and scientifically uninterpretable. |

### Iter010 aggregate

Summary artifact `10297865845`: 24/24 structural passes; 24/24 nonzero full-sphere gaps; 0/24 off-plane improvements above frozen 1% criterion; minimum full-sphere gap `0.012499674481709782`.

### Iter011 aggregate

Summary artifact `10297528599`, digest `sha256:b7f80fc91bba1b45371ec1cec1865ddbc9dab3a1ab7c4138a94d4a5064287356`: 24/24 structurally valid; minimum continuous adversarial gap `0.02500020131464493`; minimum Choi eigenvalue `-7.229908172761597e-16`; minimum identifiability rank `6/6`; maximum finest RK4 cross-check error `1.0037722995948985e-11`.

### Iter012 aggregate

Summary artifact `10298417946`, digest `sha256:7c4095c8ddd329b53973fd1bc5b0b823455b2b543c26fe370aba748806b6f0b0`:

- 20/20 structurally valid;
- frozen local scientific-support flags 20/20;
- minimum K=2 adversarial gap `0.025014400602647237`;
- minimum K=3 adversarial gap `0.025028081208365957`;
- aligned split, K=3 CPTP/PSD admissibility, and exact in-family null controls all passed their frozen local criteria.

Scientific caution: G30 used finite-restart coordinate search. Therefore the nonzero gap is a scoped negative comparator result, not yet a certified nearest-distance bound.

Durable note: `results/ITER012_G30_MULTICHANNEL_SUMMARY.md`.

### Iter013 aggregate

Summary artifact `10297704949`, digest `sha256:cfe6a47700e929b4c3c515362db16e2b1618ca64723bfd96dbc38856d9522871`:

- 20/20 structurally valid;
- adversarial K=2 minimum gap `0.028426977805393647`;
- adversarial K=3 minimum gap `0.02749744988997753`;
- adversarial K=4 minimum gap `0.02631736559670728`;
- K=4 admissibility 4/4 local support;
- nesting consistency within frozen `2e-3` optimizer slack: PASS;
- **positive in-family K=2 recovery: FAIL**, maximum recovery gap `0.06046122957245775` versus frozen `<0.002` tolerance;
- `scientific_interpretable=false` and `scoped_scientific_support=false` by the prospectively frozen gate.

G31 is therefore a useful negative methodology result: the global-search implementation/budget is not calibrated well enough to support a nearest-comparator claim. The adversarial residuals must not be interpreted as physical evidence until a positive-control method is calibrated and the adversarial calculation is rerun under it.

## Infrastructure correction

Commits `86d740b6dd884cd49f401b526dbcb28dc6f5944d` and `2aef6779a8541e3beb4acf4e9be58dcb3ff1e2d7` removed broad `push: main` triggers from closed Iter003 and Iter009 workflows. Closed historical matrices no longer rerun on unrelated scientific commits.

## Current frontier

The dominant uncertainty is now optimizer validity rather than comparator breadth. G32 must diagnose the failed positive control without looking at or retuning against the RCG-002 adversarial target.

Authorized next gate: G32 positive-control diagnostic suite. It must independently test exact oracle replay, K=2 channel-swap symmetry, local recovery from frozen perturbations, a substantially enlarged global DE budget, and a hybrid global+local method. Existing recovery tolerance remains `2e-3`; oracle/symmetry checks use numerical-precision thresholds frozen before execution. If no positive-control search method passes, RCG-002 adversarial interpretation remains blocked. If one passes, a later gate must rerun the adversarial K=2/3/4 targets with that exact calibrated method; G31 gaps cannot be promoted retroactively.

## Stable readiness rubric

- independent scope/claim discipline: closed
- weak-field coherent candidate construction: closed at toy-channel level
- basis/rotation robustness of finite comparator: closed
- CPTP/PSD and numerical robustness of finite comparator: closed
- multi-channel comparator breadth through K<=3: closed
- optimizer calibration / adversarial nearest-comparator reliability: **scientific calibration FAIL, diagnostic active**
- correlated/general Kossakowski comparator: open
- non-Markovian comparator layer: open
- externally anchored observable/holdout programme: open
- full candidate-gravity dynamics / continuum completion: open

Current internal programme readiness: **46%**. No increase is granted for G31 because the gate failed. This is a construction/readiness metric, not a probability of physical correctness.

## Claim locks

Do not promote finite-family gaps to claims that all semiclassical gravity, all classical mediators, or all alternatives to quantum gravity are excluded. Do not use green CI as a scientific verdict. Record scientific negative results even when CI is green. After G31, specifically do not treat its K=2/3/4 adversarial minima as scientifically interpretable.