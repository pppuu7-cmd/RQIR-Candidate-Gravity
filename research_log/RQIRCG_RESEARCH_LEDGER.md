# RQIR-CG research ledger

This file is the clean authority ledger for `RQIR-Candidate-Gravity` only. The pre-existing `research_log/RESEARCH_ACTIVITY_LEDGER.md` contains legacy material from another research line and must not be used as scientific evidence for RQIR-CG.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, gate discipline and mathematical tools, but not imported physical assumptions, ansatz coefficients or desired conclusions.

## Latest authoritative results

| Iteration | Gate | Run / head | Classification | Result ceiling |
|---|---|---|---|---|
| Iter010 | G28 full-Bloch comparator audit | run `34692403874`, head `3d8d3f969a22c22c1526b00f42377c2d41f87a04` | `DERIVED_SCOPED_NEGATIVE_COMPARATOR_RESULT` | Finite single-axis Markovian family only. |
| Iter011 | G29 robustness suite | run `34694101699`, head `c4c6f0d35e4e57a2105facafee2bdddc8036a52f` | `DERIVED_SCOPED_ROBUSTNESS_SUPPORT` | 24/24 structural valid/support in finite single-axis family. |
| Iter012 | G30 additive multi-channel comparator | run `34694264478`, head `fa9be36b422b84614b03f96de7c37660059f2d74` | `FINITE_SEARCH_DIAGNOSTIC` | Historical K=2/K=3 gaps cannot be treated as nearest distances after later calibration failure. |
| Iter013 | G31 global-search calibration | run `34695076098`, head `f32ecf1949f1e7d6c577b201b73c517d4605fdb7` | `SCIENTIFIC_CALIBRATION_FAIL / GLOBAL_OPTIMIZER_NOT_VALIDATED` | Positive K=2 recovery failed; adversarial minima diagnostic only. |
| Iter014 | G32 positive-control optimizer diagnosis | run `34695441883`, head `ea54a3ae9694366c3bebe06c13b775af44d46833` | `POSITIVE_CONTROL_OPTIMIZER_FAIL / LOCAL_BASIN_GEOMETRY_OR_CONDITIONING` | Exact representability/plumbing pass; direct trace-distance search unreliable. |
| Iter014B | G32-J positive-control Jacobian | run `34695478444`, head `706245fa183845556aa020bc99d2a4d86e4e3060` | `FULL_LOCAL_RANK / STRONGLY_ILL_CONDITIONED_DIAGNOSTIC` | Rank 11/11; condition number up to ~4034. |
| Iter015 | G33 smooth positive-control calibration | run `34695662002`, head `d15d633f58fa63d378a85d6e5409c4bb0735a97e` | `POSITIVE_CONTROL_METHOD_CALIBRATED_K2` | Sobol-LSQ and LHS-LSQ each recover all four hidden K=2 targets far below frozen 0.002 tolerance. |

## Key aggregates

### Iter013 / G31

Aggregate artifact `10297704949`, digest `sha256:cfe6a47700e929b4c3c515362db16e2b1618ca64723bfd96dbc38856d9522871`: positive K=2 recovery max gap `0.06046122957245775 > 0.002`; G31 adversarial minima scientifically uninterpretable.

### Iter014 / G32

Aggregate artifact `10299010209`, digest `sha256:86035287985cc1b1793df8298b919b47067b81aa22b757a5a841df9245389638`: oracle replay and channel-swap plumbing 4/4 PASS, but local/direct global trace-distance optimizers fail some positive controls.

### Iter014B / G32-J

Aggregate artifact `10298208349`, digest `sha256:e0a48b3cc49ab4ab3514b26de8c47cf2ad7b3e7fb72b7bb5c9e91e262a9490ee`: rank `[11,11,11,11]`, max FD discrepancy `1.2393500576443816e-09`, max retained-subspace condition number `4033.8739690901716`.

### Iter015 / G33

Aggregate artifact `10298088690`, digest `sha256:92f1d470f516bd6b85e7d475581762b10ca6871d3ec4c85fc0e73f218f0faa19`:

- all 12 lanes structurally valid;
- `sobol_lsq`: 4/4 scientific support, worst trace gap `1.6005292984593422e-12`;
- `lhs_lsq`: 4/4 scientific support, worst trace gap `1.6222740678511114e-12`;
- `de_smooth_lsq`: 3/4, worst gap `0.012008310266765621`;
- calibrated authority methods: `sobol_lsq`, `lhs_lsq`.

The successful methods use affine unit-box coordinates, smooth density-matrix residuals, and global low-discrepancy/design multistarts followed by bounded least squares. Hidden source coordinates were not supplied as optimizer initializers. Scientific acceptance remained the original trace-distance `<0.002` condition. This closes the K=2 optimizer-calibration subgate but does not retroactively validate any historical adversarial gap.

## Current frontier

G34 is prospectively authorized as a parallel three-front gate:

- rerun RCG-002 K=2 adversarial targets under both independently calibrated K=2 methods; both methods must retain a nonzero residual and agree within the frozen `0.002` calibration scale for scoped comparator support;
- calibrate the same smooth/unit-box multistart methodology prospectively on four hidden in-family K=3 controls using both Sobol-LSQ and LHS-LSQ extensions;
- independently calibrate K=4 in the same way.

K=3/K=4 adversarial interpretation remains forbidden until that K has its own positive-control calibration. If calibration passes, adversarial reruns are a later gate; historical G30/G31 minima are never promoted retroactively.

## Stable readiness rubric

- independent scope/claim discipline: closed
- weak-field coherent candidate construction: closed at toy-channel level
- basis/rotation robustness of finite comparator: closed
- CPTP/PSD and numerical robustness of finite comparator: closed
- exact K=2 in-family representability/plumbing: closed
- **K=2 smooth optimizer calibration: closed**
- calibrated K=2 adversarial comparator rerun: active G34
- K=3/K=4 optimizer calibration: active G34
- correlated/general Kossakowski comparator: open
- non-Markovian comparator layer: open
- externally anchored observable/holdout programme: open
- full candidate-gravity dynamics / continuum completion: open

Current internal programme readiness: **48%**. This is a construction/readiness metric, not a probability of physical correctness.

## Claim locks

Do not promote finite-family gaps to claims that all semiclassical gravity, all classical mediators, or all alternatives to quantum gravity are excluded. Do not use green CI as a scientific verdict. Do not weaken the frozen `2e-3` positive-control criterion. Do not reuse G30/G31 adversarial minima as authority; calibrated adversarial tests must be recomputed prospectively.