# RQIR-Candidate-Gravity current front

Updated: 2026-09-13
Phase: `INDEPENDENT_RQIR_DERIVATION / HELDOUT_OBSERVABLE_CLOSED / G56F_FROZEN_FAIL / G56D_DIAGNOSTICS_RUNNING`

## Canonical status
- Candidate-model/programme readiness: **66%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

## Recent closed authority
### Iter050 / G54-Q — finite-size controlled-phase channel integration
Classification: `FINITE_SIZE_WEAK_FIELD_CONTROLLED_PHASE_CHANNEL_INTEGRATED_SCOPED`.
Preregistration `aa3efc459c43ccf9055b3d6ddf8fa32cc1ac06b0`. Initial run `34741756333` is implementation-invalid only; serialization-only repair `33efdabc9169d498eb90d32c1ebce3481df2df2e`. Authoritative retry head `d4f5b37ac0c00842aaf85344850ee99d46dacdff`; run `34743980333`; aggregate job `103688387613`; artifact `10312897870`; digest `sha256:554436be119b3a60cd7880b5cd2c6c5f70878afad91ac1ebfe8706df20b5d428`.
Scope: finite weak-field isotropic-Gaussian controlled-phase channel only.

### Iter051 / G55-O — held-out entanglement observable transport
Classification: `HELDOUT_FINITE_SIZE_ENTANGLEMENT_OBSERVABLE_TRANSPORT_VALIDATED_SCOPED`.
Preregistration `a824171b4e2fafa3ec61a0aa160d5d8a652a3343`; authoritative head `4e233f480561399fbbe80beb1cd984ec01a06e4b`; run `34744407575`; aggregate job `103689556743`; aggregate artifact `10313850057`; digest `sha256:e750229e99a129f6d2eac338bff600c77339108a748291cd9d76ab43113f6973`.
All 6/6 raw lanes were consumed and are structural-valid/supportive. Frozen interpretation closes the independent observable/witness rubric and sets internal roadmap readiness to 66%.

### Iter052 / G56-F — Gaussian continuum field closure
Terminal classification: `G56F_FROZEN_CONTINUUM_FIELD_CLOSURE_RULE_NOT_MET`.
Preregistration `f27b25d290fae7e45f4584b5a66c902d33c0e568`; implementation `0b459d3a36826387194a25655d5014d397c039bc`; production head `fc8bed7571d88bf48a3cb168e71067185a5ad1e6`; run `34746540910`; aggregate job `103695482197`; aggregate artifact `10313798716`; digest `sha256:57de2f010d09a2f0d584f4238c98d98e0eb28261582515cbfbea7f03539a4b1b`.
6/6 lanes are structural-valid, but case 3 (`u=r/s=2.0`) fails only the frozen wrong-width (`1.3s`) negative-control predicate: observed relative difference `0.029913948838822833` vs required `>=0.05`. In that same lane the actual source/kernel identity metrics pass strongly: worst Cartesian Laplacian relative error `1.0614870158684851e-09`, orientation spread `1.6777244871146735e-10`, Gauss-flux error `3.1327862526353556e-10`, normalization error `0.0`.
G56-F remains FAIL exactly as preregistered; no threshold is relaxed and no PASS is inferred. The observed failure is localized to negative-control discriminability, not to an observed source/kernel identity violation. Terminal note: `results/ITER052_G56F_GAUSSIAN_CONTINUUM_FIELD_CLOSURE_TERMINAL.md`.

## Active diagnostics — Iter053 / G56-D
These are explicitly **non-rescue diagnostics** and cannot alter G56-F or readiness.

Preregistration commit `325b4a44328c9f00b9a1a6643cdf79c47e90b22b`; implementation commit `b8e1498b8ee08b351a06780558a9212792331466`; workflow/launch head `fa9c90366b10970e55d18277caf0e16edca96d31`; run `34748468285`.

Three parallel independent streams are frozen:
1. D1 finite-difference convergence at five `h/s` values on the original six-lane panel;
2. D2 exact wrong-width discriminability/crossing map for `q=1.3`;
3. D3 80-digit held-out arbitrary-precision radial identity test.

Aggregate diagnosis can only localize the G56-F failure. It cannot retroactively rescue G56-F or earn a readiness point.

## Current frontier
Wait for terminal raw artifacts from G56-D, then decide whether a *new separately preregistered* continuum field-closure gate is scientifically justified with a prospectively non-degenerate control. Only a later constitution/covariance rubric may move readiness beyond 66%.

Open layers remain: generally covariant candidate-gravity dynamics and gravity-theory constitution; field/measure/quantization closure beyond weak-field branch kernels; externally anchored physical predictions beyond current finite weak-field toy/bridge scope.

## Claim locks
Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, green-CI-as-scientific-PASS, post-hoc threshold/family/witness weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:
`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_66_PERCENT + THEORY_ESTABLISHED_0 + G55O_HELDOUT_OBSERVABLE_PASS + G56F_FROZEN_RULE_FAIL_CONTROL_BLIND_SPOT + G56D_DIAGNOSTICS_RUNNING + COVARIANT_DYNAMICS_OPEN + FIELD_MEASURE_OPEN`.