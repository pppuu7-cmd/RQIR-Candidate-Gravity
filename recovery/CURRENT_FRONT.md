# RQIR-Candidate-Gravity current front

Updated: 2026-09-13
Phase: `INDEPENDENT_RQIR_DERIVATION / G68_QUADRATIC_GRAVITY_BASELINE_CLOSED / G69_CANDIDATE_DYNAMICS_BLOCKED / G70_ARCHITECTURE_TRIAGE_CLOSED / G71_DISCRIMINATOR_AUDIT_CLOSED / G72_CD_MINIMAL_COMPLETIONS_CLOSED / G73_MULTIORDER_IDENTIFIABILITY_CLOSED / G74_NUISANCE_CONFOUNDING_CLOSED / G75_MINIMAL_ANCHOR_AUDIT_CLOSED / G76_G79_ROBUSTNESS_FANOUT_CLOSED / G80_G81_NATIVE_ANCHOR_BLOCKED / G82_G83_REFERENCE_CONSTRUCTION_CLOSED / G84_G85_REFERENCE_LEAKAGE_ROBUSTNESS_CLOSED / NONLINEAR_COMPLETION_UNIQUENESS_FRONTIER`

## Canonical status
- Candidate-model/programme readiness: **66%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.
- `recovery/state.json` is currently absent; newest main + this file + clean ledger + durable results + validated Actions artifacts are authority.

## Identifiability/reference branch closure through G85
G80/G81 established that already-native C/D source-functionals do not break their exact same-shape nuisance aliases. G82/G83 established one explicit external nuisance-reference construction per architecture. G84/G85 then relaxed perfect candidate-blindness.

- G84 run `34783862061`: `C_REFERENCE_CONSTRUCTION_REMAINS_IDENTIFIABLE_UNDER_FROZEN_LEAKAGE_UNTIL_SAME_SHAPE_LIMIT_SCOPED`.
  Exact rank two survives the frozen non-boundary C leakage family and gains down to `1e-6`; conditioning worsens continuously toward `rho=-1` or zero gain; Ward/source and high-precision controls pass.
- G85 run `34783869306`: `D_REFERENCE_CONSTRUCTION_REMAINS_IDENTIFIABLE_UNDER_FROZEN_LEAKAGE_UNTIL_SAME_SHAPE_LIMIT_SCOPED`.
  Exact rank two survives the frozen non-boundary D leakage family and gains down to `1e-6`; conditioning worsens continuously toward `rho=+1` or zero gain; retarded/Sigma/CTP/jet and high-precision controls pass.

Retrospective synthesis: `results/G82_G85_REFERENCE_ROBUSTNESS_SYNTHESIS.md`.

These are **construction-robustness** results only. Physical source/reference preparation remains unestablished.

## Active scientific frontier — nonlinear completion uniqueness
Further abstract reference-channel rank scans now have diminishing scientific value. The main unresolved blocker remains G69: candidate-owned beyond-baseline dynamics are not defined.

The next admissible work is to ask, independently for C and D, whether their frozen lower-order perturbative data determine a unique nonlinear generally covariant completion.

### C gate requirements
- preserve the frozen C quadratic/two-point response data and Ward-compatible sector;
- exhibit or rule out higher-order generally covariant invariant additions whose first nonzero perturbative contribution starts at cubic order and therefore leaves the frozen Hessian unchanged;
- test exact lower-jet equality and higher-jet inequality between at least two prospectively frozen completions;
- include field-redefinition/boundary-term controls where possible;
- classify surviving nonuniqueness as underdetermination/BLOCKED, not architecture failure.

### D gate requirements
- preserve the frozen D cubic/three-point jet, retarded-support/CTP structural constraints at the audited order;
- exhibit or rule out higher-order invariant additions whose first nonzero perturbative contribution starts at quartic order and therefore leaves the frozen third-order jet unchanged;
- test exact lower-jet equality and higher-jet inequality between at least two prospectively frozen completions;
- include trivial rescaling/reparameterization controls;
- classify surviving nonuniqueness as underdetermination/BLOCKED, not architecture failure.

## Open scientific layers
- nonlinear completion uniqueness/underdetermination for C and D;
- candidate-owned generally covariant dynamics;
- nonlinear conserved-source/Bianchi/diffeomorphism completion;
- physical source/reference preparation and realizability;
- field/measure/quantization closure;
- externally anchored physical predictions beyond current finite weak-field scope.

## Claim locks
Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, green-CI-as-scientific-PASS, post-hoc weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:
`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_66_PERCENT + THEORY_ESTABLISHED_0 + G68_STANDARD_QUADRATIC_GRAVITY_BASELINE_SCOPED + G69_BLOCKED_CANDIDATE_DYNAMICS_UNDEFINED + G70_PARETO_BCDE + G71_PARETO_CD + G72_CD_MINIMAL_COMPLETIONS_EXIST_NO_UNIQUE_SELECTION + G73_MULTIORDER_LOCAL_IDENTIFIABILITY_SCOPED + G74_SAME_ORDER_NUISANCE_ANCHORS_REQUIRED_SCOPED + G75_TWO_INDEPENDENT_ANCHOR_DIRECTIONS_SUFFICIENT_SCOPED + G76_G79_ROBUSTNESS_QUALIFIED_SCOPED + G80_G81_NATIVE_ANCHOR_BLOCKED_SCOPED + G82_G83_EXTERNAL_REFERENCE_CONSTRUCTION_SUFFICIENT_SCOPED + G84_G85_IMPERFECT_DECOUPLING_ROBUSTNESS_SCOPED + NONLINEAR_COMPLETION_UNIQUENESS_FRONTIER`.
