# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active iteration: `ITER017`
Phase: `INDEPENDENT_RQIR_DERIVATION / CALIBRATED_K3_K4_ADVERSARIAL_COMPARATOR`

## Canonical status

- Candidate-model/programme readiness: **52%**
- Theory established: **0%**
- Active seed: `RCG-002 Relational controlled-phase channel`
- Independent-from-QGR construction contract: **FROZEN**
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`

Readiness is an internal construction metric, not a probability that the model is correct. The increase to 52% reflects closure of the calibrated K=2 adversarial rerun plus K=3/K=4 optimizer-calibration subgates. It does not broaden the physical scope of the comparator result.

## Iter016 / G34 terminal result

Authoritative run `34695835216`, head `09d729764ca38a0d83f11b81dc59f157cd0cb734`, aggregate job `103562681303`, aggregate artifact `10299385844`, digest `sha256:622e04cfdc1859561bd958962cadd293403defb8f8265641410c7119de2843c4`.

All 24 lanes were structurally valid.

### K=2 prospective calibrated adversarial rerun

Both G33-calibrated methods retained nonzero gaps and agreed within the frozen `0.002` scale on all four shards. Gaps ranged from `0.026070816008971712` to `0.5324532595059579`.

Classification: `DERIVED_SCOPED_K2_CALIBRATED_COMPARATOR_SUPPORT`.

This is limited to the finite additive independent single-axis Markovian measurement-feedback GKSL comparator family and is not a general no-go theorem.

### K=3 positive controls

- Sobol-LSQ 4/4 PASS; worst gap `4.864663671077271e-11`.
- LHS-LSQ 4/4 PASS; worst gap `3.1874163425023643e-11`.

Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_K3`.

### K=4 positive controls

- Sobol-LSQ 4/4 PASS; worst gap `8.088582075956358e-13`.
- LHS-LSQ 4/4 PASS; worst gap `2.658734486319925e-12`.

Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_K4`.

Historical G30/G31 adversarial minima remain diagnostics only and are not promoted retroactively.

## Active authorized gate — Iter017 / G35

Run independent fronts in parallel:

1. prospective calibrated RCG-002 adversarial reruns for K=3 with Sobol-LSQ and LHS-LSQ across all four shards;
2. prospective calibrated RCG-002 adversarial reruns for K=4 with the same two independently calibrated methods;
3. independent numerical physical-admissibility audits for prospectively sampled K=3 and K=4 additive generators/evolutions.

Frozen scientific rules, fixed before G35 inspection:

- nonzero adversarial gap: `> 1e-4`;
- cross-method agreement on each shard: `<= 0.002`;
- nesting sanity: increasing K may not worsen the calibrated minimum by more than `0.002` relative to the immediately smaller calibrated K frontier;
- admissibility: TP residual `<1e-10`, Choi minimum eigenvalue `>-1e-8`, evolved-state minimum eigenvalue `>-1e-8`, trace error `<1e-10`;
- final distance authority remains trace distance;
- no historical G30/G31 minima are reused;
- no threshold changes after result inspection.

Only after terminal G35 classification may a correlated/general positive-Kossakowski comparator gate be opened.

## Claim locks

Forbidden:

- `NEW_PHYSICS_FOUND`;
- `FULL_QUANTUM_GRAVITY`;
- `RQIR_REQUIRES_RCG002`;
- claim that all classical/semiclassical mediators are excluded;
- treating green CI as scientific PASS;
- changing frozen thresholds after seeing results;
- importing physical assumptions or desired conclusions from QGR/KMQGB/RQIR.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + K2_K3_K4_OPTIMIZER_CALIBRATED + K2_SCOPED_CALIBRATED_COMPARATOR_SUPPORT + G35_K3K4_ADVERSARIAL_REQUIRED`.