# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active gate: `ITER025B / G42-C full-PSD optimizer calibration`
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_CALIBRATION`

## Canonical status

- Candidate-model/programme readiness: **60%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is an internal construction metric, not a probability of physical correctness. The `59% -> 60%` increment is attributed only to terminal closure of the G41-A finite high-rank adversarial comparator layer. G40 diagnostics and G42 identifiability/calibration do not themselves raise readiness.

## Newly closed

### G40-RC-A — terminal frozen support-rule failure

Run `34710216045`, head `3e31a9faa8b05a9bf5d6971a4ca4d94e6386b633`, aggregate `103597733387`, artifact `10302543565`, digest `sha256:c86ad2349bd28c0ad7d031c34f4bed38ee4a4a3681d5c6b14199b80ae9db4f73`.

Classification: `G40RCA_FROZEN_SUPPORT_RULE_NOT_MET`. Shards 0/1/2 passed the finite axis-frame-covariant RTN rule; shard 3 violated frozen Sobol/LHS agreement (`0.0022523906566203067 > 0.002`). No threshold change. Durable note: `results/ITER023C_G40RCA_TERMINAL.md`.

### G40-RC-D2 — terminal persistent optimizer/objective nonrobustness

Run `34710444349`, head `ccf4274e73414d665a5c0d7f3501957760384c37`, aggregate `103598231631`, artifact `10303515884`, digest `sha256:da1e87331e79a9f6883b3827ca80400f35e364a672eaba0f0826aec94ac5286c`.

Four independent 64-start searches on shard 3 gave best gaps `0.7495354861`, `0.7450136685`, `0.7450127676`, `0.7450127451`; spread `0.0045227410 > 0.002`. Classification: `PERSISTENT_OPTIMIZER_OR_OBJECTIVE_GEOMETRY_NONROBUSTNESS`. No repaired RTN adversarial gate is authorized. Durable note: `results/ITER023D_G40RCD2_TERMINAL.md`.

### G41-C — terminal high-rank rate calibration PASS

Run `34710257380`, head `2bac531b1c68d0fc735b8135b579662b1318fe52`, aggregate `103597956597`, artifact `10302238984`, digest `sha256:567a1994b5892050379509066bf5075f1190831658638a77eaa26d36ef62ee82`.

All 24 positive-control lanes passed for ranks 4/5/6 × four shards × Sobol/LHS. Classification: `HIGH_RANK_RATE_OPTIMIZER_CALIBRATED`. Calibration applies only to positive rates on frozen deterministic mode frames, not arbitrary orientations. Durable note: `results/ITER024B_G41C_TERMINAL.md`.

### G41-A — terminal scoped high-rank comparator PASS

Run `34710491309`, head `766ea13802d62e75fd988ec79f55f6b251296d9c`, aggregate `103598462910`, artifact `10303600848`, digest `sha256:fe89d973dc1f24fe50fba09542e1b1b8e1d1fbae5e9cb1f33165b7213764dea7`.

All 12 `(rank, shard)` cells passed frozen nonzero-gap `>1e-4` and Sobol/LHS agreement `<=0.002`. Gaps ranged approximately `0.08004` to `0.90799`; maximum method difference was only about `5.2e-9`. Classification: `DERIVED_SCOPED_HIGH_RANK_RATE_COMPARATOR_SUPPORT`.

Scope ceiling: finite frame-indexed positive-rate rank-4/5/6 classical random-Hamiltonian families only. This does not test arbitrary mode orientations or the full real-PSD 6x6 Kossakowski family. Durable note: `results/ITER024C_G41A_TERMINAL.md`.

### G42-J — terminal full-PSD identifiability PASS

Run `34710643103`, head `ec3d1a5e407d149ebf39d44968bf1bf1085db8d7`, aggregate `103598755854`, artifact `10303316491`, digest `sha256:07a895f0fb309a6e642cd6eb5429e368ddcad0c78367571cfa59b7c7bce8ea9e`.

All four full-PSD hidden controls passed: 21/21 Jacobian rank at both derivative steps, worst condition number `5.905925058`, max two-step relative Jacobian mismatch `1.262474e-9`, CPTP diagnostics clean. Classification: `FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE`. This is identifiability only and does not raise readiness. Durable note: `results/ITER025A_G42J_TERMINAL.md`.

## Active gate — G42-C

Preregistered protocol: `protocol/ITER025B_G42C_FULL_PSD_OPTIMIZER_CALIBRATION.md`.
Launch commit: `7ebc18df416b62784e85ce6090ba6e8836619d92`.
Run: `34710744967`.

Eight positive-control lanes: Sobol/LHS × four G42-J hidden controls. Full 21-coordinate Cholesky parameterization of a real-PSD 6x6 classical random-Hamiltonian Kossakowski matrix. Frozen bounds, 32 starts, top-6 least-squares refinements, max `1000` evaluations, four times × six product probes, recovery threshold `<0.002`. Exact hidden coordinates are not inserted as starts. No RCG-002 target.

If and only if G42-C terminally passes, a separate prospective G42-A adversarial gate may be preregistered with the identical family/search rules. Until then arbitrary-orientation/full-PSD comparator evidence is **not established**.

## Stable closed finite-comparator layers

- G35/G35-R: K2/K3/K4 additive independent measurement-feedback calibration/scoped support.
- G36-P/C/A: one shared Gaussian classical-noise implementation/calibration/scoped support.
- G37-C2/A3: corrected truly nested MF + one shared-noise finite comparator support.
- G38-P/C/A: OU finite-correlation three-time toy comparator support.
- G39-P/C/A2: finite rank2/rank3 multimode shared white-noise comparator support.
- G40: strict RTN implementation/calibration succeeded, but adversarial support remained unresolved due persistent optimizer/objective nonrobustness; no RTN physics PASS.
- G41-P/C/A: rank-4/5/6 implementation, positive-rate calibration and scoped frame-indexed adversarial support.
- G42-J: full 21-parameter real-PSD local identifiability established; optimizer calibration pending G42-C.

## Open scientific layers

- terminal G42-C full-PSD optimizer calibration;
- only after G42-C PASS: prospective arbitrary-orientation/full-PSD adversarial test;
- a separately calibrated trace-metric-aligned RTN optimizer if that branch is ever reopened;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and any constitution gate for an actual gravity theory.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, treating green CI as scientific PASS, post-hoc threshold/family/witness weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_60_PERCENT + THEORY_ESTABLISHED_0 + FINITE_COMPARATOR_SUPPORT_ONLY + G37A3_SCOPED_PASS + G40_RTN_ADVERSARIAL_UNRESOLVED_OPTIMIZER_NONROBUSTNESS + G41A_SCOPED_HIGH_RANK_RATE_PASS + G42J_FULL_PSD_IDENTIFIABLE + G42C_RUNNING`.
