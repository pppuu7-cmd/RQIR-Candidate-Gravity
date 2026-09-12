# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active gate: `ITER025C / G42-C2 PSD-boundary optimizer calibration`
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_CALIBRATION`

## Canonical status

- Candidate-model/programme readiness: **60%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is an internal construction/completion metric, not a probability of physical correctness. `59% -> 60%` is attributed only to terminal closure of G41-A finite high-rank adversarial support. G42 identifiability/calibration results do not themselves raise readiness.

## Stable recent terminal results

### G40 RTN branch — no physics PASS

G40-RC-A run `34710216045`, aggregate `103597733387`, artifact `10302543565`, digest `sha256:c86ad2349bd28c0ad7d031c34f4bed38ee4a4a3681d5c6b14199b80ae9db4f73`, failed the frozen all-shards agreement rule only on shard 3. G40-RC-D2 run `34710444349`, aggregate `103598231631`, artifact `10303515884`, digest `sha256:da1e87331e79a9f6883b3827ca80400f35e364a672eaba0f0826aec94ac5286c`, confirmed `PERSISTENT_OPTIMIZER_OR_OBJECTIVE_GEOMETRY_NONROBUSTNESS`: four-method shard-3 gap spread `0.0045227410 > 0.002`. No repaired RTN adversarial gate is authorized without a separately calibrated trace-metric-aligned optimizer.

### G41-C / G41-A — finite high-rank frame-indexed layer closed

G41-C run `34710257380`, aggregate `103597956597`, artifact `10302238984`, digest `sha256:567a1994b5892050379509066bf5075f1190831658638a77eaa26d36ef62ee82`: 24/24 positive-control lanes passed.

G41-A run `34710491309`, aggregate `103598462910`, artifact `10303600848`, digest `sha256:fe89d973dc1f24fe50fba09542e1b1b8e1d1fbae5e9cb1f33165b7213764dea7`: all 12 rank×shard cells passed nonzero-gap and Sobol/LHS agreement. Classification `DERIVED_SCOPED_HIGH_RANK_RATE_COMPARATOR_SUPPORT`. Scope is only finite frame-indexed positive-rate rank-4/5/6 classical random-Hamiltonian families. This result produced readiness `59% -> 60%`.

### G42-J — full 21-parameter interior identifiability PASS

Run `34710643103`, aggregate `103598755854`, artifact `10303316491`, digest `sha256:07a895f0fb309a6e642cd6eb5429e368ddcad0c78367571cfa59b7c7bce8ea9e`. All four controls gave Jacobian rank `21/21` at both derivative steps; worst condition number `5.905925058`; max relative two-step mismatch `1.262474e-9`; CPTP diagnostics clean. Classification `FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE`.

### G42-C — terminal PASS, but scientific scope is SPD interior only

Run `34710744967`, head `7ebc18df416b62784e85ce6090ba6e8836619d92`, aggregate `103599128599`, artifact `10302903611`, digest `sha256:daa9c9f1ac0bf70094fd47783c7b0dece89243593348befff801054f799e258a`.

All 8 positive-control lanes passed (`Sobol worst ~2.78e-14`, `LHS worst ~1.05e-15`). However, the frozen log-Cholesky diagonal bounds `[-2,-0.5]` make every candidate strictly positive definite. Therefore workflow label `FULL_PSD_OPTIMIZER_CALIBRATED` is retained only for provenance; scientific authority is **bounded SPD-interior optimizer calibration**, not calibration of the rank-deficient PSD boundary. Durable scope correction: `results/ITER025B_G42C_TERMINAL.md`. G42-A was deliberately NOT launched from this result.

## Active gate — G42-C2 PSD-boundary calibration

Preregistered protocol: `protocol/ITER025C_G42C2_PSD_BOUNDARY_CALIBRATION.md`.
Launch/head: `858ad4b6848362bf430eaab849fb0ed4166f9cde`.
Run: `34710953936`.

Boundary-capable coordinates: real lower-triangular `B` with `C=B B^T`, direct diagonal bounds `[0,0.60]` and lower off-diagonal bounds `[-0.30,0.30]`, so rank-deficient PSD points are included exactly. Positive controls have intended Kossakowski ranks `2,4,5,6`.

Frozen search: Sobol/LHS × four rank controls, 32 starts, top-6 least-squares refinements, max 1000 evaluations, same four times × six product probes. Exact hidden coordinates are not starts.

Each lane must simultaneously satisfy:
- maximum output-state trace-distance gap `<0.002`;
- relative Kossakowski Frobenius error `<0.02`;
- recovered effective rank at eigenvalue threshold `1e-5` equals hidden rank.

Only terminal 4/4 Sobol + 4/4 LHS PASS may authorize a separately preregistered boundary-capable arbitrary-orientation PSD adversarial gate. Until then the broad PSD comparator is **not established**.

## Stable closed finite-comparator layers

- G35/G35-R: finite K2/K3/K4 additive independent measurement-feedback calibration/scoped support.
- G36: one shared Gaussian classical-noise implementation/calibration/scoped support.
- G37: corrected truly nested MF + one shared-noise finite comparator support.
- G38: OU finite-correlation toy comparator support.
- G39: finite rank2/rank3 multimode shared white-noise support.
- G40: RTN implementation/calibration succeeded, adversarial support unresolved due persistent optimizer/objective nonrobustness.
- G41: rank4/5/6 frame-indexed positive-rate implementation/calibration/scoped adversarial support.
- G42-J/C: full 21-parameter local identifiability and SPD-interior calibration; PSD-boundary calibration pending G42-C2.

## Open scientific layers

- terminal G42-C2 PSD-boundary calibration;
- only after G42-C2 PASS: prospective boundary-capable arbitrary-orientation PSD adversarial test;
- separately calibrated trace-metric-aligned RTN optimizer if that branch is reopened;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and any constitution gate for an actual gravity theory.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, treating green CI as scientific PASS, post-hoc threshold/family/witness weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_60_PERCENT + THEORY_ESTABLISHED_0 + FINITE_COMPARATOR_SUPPORT_ONLY + G40_RTN_ADVERSARIAL_UNRESOLVED_OPTIMIZER_NONROBUSTNESS + G41A_SCOPED_HIGH_RANK_RATE_PASS + G42J_FULL_LOCAL_RANK_PASS + G42C_SPD_INTERIOR_CALIBRATED + G42C2_PSD_BOUNDARY_QUEUED_OR_RUNNING`.
