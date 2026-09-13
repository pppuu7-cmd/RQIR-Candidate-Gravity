# RQIR-Candidate-Gravity current front

Updated: 2026-09-13
Phase: `INDEPENDENT_RQIR_DERIVATION / G68_QUADRATIC_GRAVITY_BASELINE_CLOSED / G69_CANDIDATE_DYNAMICS_BLOCKED / G70_ARCHITECTURE_TRIAGE_CLOSED / G71_DISCRIMINATOR_AUDIT_CLOSED / G72_CD_MINIMAL_COMPLETIONS_CLOSED / G73_MULTIORDER_IDENTIFIABILITY_CLOSED / G74_NUISANCE_CONFOUNDING_CLOSED / G75_MINIMAL_ANCHOR_AUDIT_CLOSED / G76_NEAR_ALIAS_CONDITIONING_CLOSED / G77_STATISTICAL_NOISE_CLOSED / G78_ROW_REDUNDANCY_CLOSED / G79_GLS_NOISE_CLOSED / SOURCE_DEFINED_ANCHOR_FRONTIER`

## Canonical status
- Candidate-model/programme readiness: **66%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.
- `recovery/state.json` is currently absent; newest main + this file + clean ledger + durable results + validated Actions artifacts are authority.

## Terminal robustness fan-out from G75
G76–G79 are now terminal. G77/G78/G79 were prospectively frozen on independent sibling branches rooted at terminal G75 and were merged only after raw-artifact validation.

- G76 — run `34782314724`: `G75_EXACT_IDENTIFIABILITY_DEGRADES_CONTINUOUSLY_TOWARD_ALIAS_SCOPED`.
  Terminal note: `results/ITER074_G76_CD_NEAR_ALIAS_CONDITIONING_ROBUSTNESS_TERMINAL.md`.
- G77 — run `34782611134`: `G75_ANCHORED_ESTIMATOR_VARIANCE_GROWS_AS_ANCHORS_WEAKEN_SCOPED`.
  Terminal note: `results/ITER075_G77_CD_STATISTICAL_NOISE_ROBUSTNESS_TERMINAL.md`.
- G78 — run `34782616139`: `G75_ANCHORED_DESIGN_SINGLE_ROW_FAILURE_MODES_AND_MINIMAL_CUBIC_REDUNDANCY_SCOPED`.
  Terminal note: `results/ITER076_G78_CD_ROW_DELETION_REDUNDANCY_TERMINAL.md`.
- G79 — run `34782623331`: `G75_SPD_GLS_IDENTIFIABILITY_PERSISTS_WHILE_WEAK_ANCHOR_VARIANCE_GROWS_SCOPED`.
  Terminal note: `results/ITER077_G79_CD_GLS_CORRELATED_NOISE_ROBUSTNESS_TERMINAL.md`.

Retrospective synthesis: `results/G76_G79_PARALLEL_ROBUSTNESS_SYNTHESIS.md`.

## Scientific meaning of the closed fan-out
Inside the frozen G75 tangent-design layer, two independent alias-breaking directions restore exact rank, but that rank becomes ill-conditioned near the aliases; estimator uncertainty grows as anchors weaken under both iid and prospectively frozen SPD-correlated noise surrogates; and the design has explicit single-row failure modes plus a minimal algebraic cubic-redundancy repair.

This is still an abstract local-design result. It does not establish physically realizable anchors or physical detectability.

## Active scientific frontier — source-defined anchor realization
The next admissible layer is to replace abstract AQ/AD information rows by architecture-specific source/observable constructions. Surviving architecture C and D must be treated as separate prospectively frozen sibling gates because their completion mechanisms occupy different perturbative-order structures.

Before launching those gates, recover the exact C/D architecture definitions and their G71/G72 completion witnesses. Each sibling gate must freeze:
- the candidate-owned source/observable map being tested;
- the nuisance direction it is intended to distinguish;
- conservation/Ward/causal constraints applicable to that architecture;
- exact positive and negative controls;
- an interpretation ceiling forbidding architecture selection or physical-detectability claims from algebraic success alone.

## Open scientific layers
- candidate-owned deformation beyond standard local gravity baselines;
- physically/source-defined anchor realization for C and D;
- nonlinear generally covariant candidate-owned dynamics;
- nonlinear conserved-source/Bianchi/diffeomorphism completion;
- field/measure/quantization closure;
- externally anchored physical predictions beyond current finite weak-field scope.

## Claim locks
Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, green-CI-as-scientific-PASS, post-hoc weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:
`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_66_PERCENT + THEORY_ESTABLISHED_0 + G68_STANDARD_QUADRATIC_GRAVITY_BASELINE_SCOPED + G69_BLOCKED_CANDIDATE_DYNAMICS_UNDEFINED + G70_PARETO_BCDE + G71_PARETO_CD + G72_CD_MINIMAL_COMPLETIONS_EXIST_NO_UNIQUE_SELECTION + G73_MULTIORDER_LOCAL_IDENTIFIABILITY_SCOPED + G74_SAME_ORDER_NUISANCE_ANCHORS_REQUIRED_SCOPED + G75_TWO_INDEPENDENT_ANCHOR_DIRECTIONS_SUFFICIENT_SCOPED + G76_NEAR_ALIAS_CONDITIONING_DEGRADES_SCOPED + G77_WEAK_ANCHOR_VARIANCE_GROWTH_SCOPED + G78_SINGLE_ROW_FAILURE_MAP_SCOPED + G79_SPD_GLS_ROBUSTNESS_SCOPED + SOURCE_DEFINED_ANCHOR_FRONTIER`.
