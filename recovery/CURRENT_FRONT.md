# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active iteration: `ITER014`
Phase: `INDEPENDENT_RQIR_DERIVATION / OPTIMIZER_CALIBRATION_DIAGNOSTIC`

## Canonical status

- Candidate-model/programme readiness: **46%**
- Theory established: **0%**
- Active seed: `RCG-002 Relational controlled-phase channel`
- Independent-from-QGR construction contract: **FROZEN**
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`

Readiness is an internal construction metric, not a probability that the model is correct. G31 does not raise readiness because its positive recovery calibration failed.

## Latest terminal result — Iter013 / G31

Authoritative workflow run `34695076098`, head `f32ecf1949f1e7d6c577b201b73c517d4605fdb7`, aggregate artifact `10297704949`, digest `sha256:cfe6a47700e929b4c3c515362db16e2b1618ca64723bfd96dbc38856d9522871`.

Twenty lanes completed and all were structurally valid. The stronger differential-evolution adversarial searches returned nonzero minima and K=4 admissibility controls passed, but the prospectively frozen positive in-family recovery control failed decisively:

- maximum K=2 positive-control recovery gap: `0.06046122957245775`;
- frozen recovery tolerance: `< 0.002`;
- minimum K=2 adversarial gap: `0.028426977805393647`;
- minimum K=3 adversarial gap: `0.02749744988997753`;
- minimum K=4 adversarial gap: `0.02631736559670728`;
- nesting consistency within frozen `2e-3` optimizer slack: PASS;
- `scientific_interpretable = false`;
- `scoped_scientific_support = false`.

Classification:
`SCIENTIFIC_CALIBRATION_FAIL / GLOBAL_OPTIMIZER_NOT_VALIDATED`.

This is **not** evidence against RCG-002 and is **not** evidence that the comparator family closes the residual. It means G31 demonstrated that the search procedure cannot yet be trusted to find a known in-family solution. Consequently G31 adversarial gaps are retained as diagnostics only and cannot be promoted to physics evidence.

## Active authorized gate — Iter014 / G32

Goal: isolate whether the G31 recovery failure comes from parameterization/objective plumbing, local basin geometry, symmetry/permutation handling, or insufficient global-search budget.

Frozen requirements before result inspection:

1. exact oracle replay of the hidden K=2 source parameters; the same objective evaluated at the true source must be numerically zero;
2. channel-swap symmetry replay for K=2 must preserve the generated Liouvillian/target to numerical precision;
3. local bounded optimization from prospectively fixed perturbations around the true source must recover below the existing `2e-3` tolerance;
4. substantially enlarged global differential-evolution budgets must be tested on the same four hidden positive controls without inspecting adversarial RCG-002 targets;
5. an independent hybrid global+local search must be tested on the same positive controls;
6. adversarial RCG-002 interpretation remains blocked until a prospectively defined positive-control method passes. If a calibrated method is found, RCG-002 adversarial K=2/3/4 searches must be rerun under that method in a later gate; old G31 minima cannot be retroactively promoted.

## Claim locks

Forbidden:

- `NEW_PHYSICS_FOUND`;
- `FULL_QUANTUM_GRAVITY`;
- `RQIR_REQUIRES_RCG002`;
- claim that all classical/semiclassical mediators are excluded;
- treating green CI as a scientific PASS;
- treating G31 adversarial gaps as scientifically interpretable after its failed positive calibration;
- importing physical assumptions or desired conclusions from QGR/KMQGB/RQIR.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + FINITE_COMPARATOR_SEARCH_UNCALIBRATED + G32_OPTIMIZER_DIAGNOSTIC_REQUIRED`.