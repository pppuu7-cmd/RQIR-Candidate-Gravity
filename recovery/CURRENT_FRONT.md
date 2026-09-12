# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active gates: `ITER025C / G42-C2 PSD-boundary calibration` + `ITER025D / G42-C3 PSD rank-completion calibration`
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_CALIBRATION`

## Canonical status

- Candidate-model/programme readiness: **60%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is programme completion, not a probability of physical correctness. `59% -> 60%` came only from terminal G41-A scoped adversarial closure. Calibration/diagnostic/identifiability gates do not raise readiness by themselves.

## Current closed authority

### G40 RTN

G40-RC-A run `34710216045` failed the frozen all-shards support rule on shard 3. G40-RC-D2 run `34710444349` then showed persistent optimizer/objective nonrobustness: four deep-search best gaps `0.7495354861`, `0.7450136685`, `0.7450127676`, `0.7450127451`, spread `0.0045227410 > 0.002`. There is no RTN adversarial physics PASS. Any future RTN reopening requires a separately calibrated trace-metric-aligned optimizer.

### G41 high-rank frame-indexed comparator

G41-C run `34710257380`: 24/24 positive-control lanes passed. G41-A run `34710491309`, aggregate `103598462910`, artifact `10303600848`, digest `sha256:fe89d973dc1f24fe50fba09542e1b1b8e1d1fbae5e9cb1f33165b7213764dea7`: all 12 rank×shard cells passed frozen nonzero-gap and Sobol/LHS agreement. Classification `DERIVED_SCOPED_HIGH_RANK_RATE_COMPARATOR_SUPPORT`, limited to finite frame-indexed positive-rate rank-4/5/6 classical families. This closure produced readiness `59% -> 60%`.

### G42-J identifiability

Run `34710643103`, aggregate `103598755854`, artifact `10303316491`, digest `sha256:07a895f0fb309a6e642cd6eb5429e368ddcad0c78367571cfa59b7c7bce8ea9e`: four controls passed Jacobian rank `21/21` at both derivative steps, worst condition `5.905925058`, max two-step relative mismatch `1.262474e-9`, CPTP clean. Classification `FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE`.

### G42-C SPD-interior calibration

Run `34710744967`, aggregate `103599128599`, artifact `10302903611`, digest `sha256:daa9c9f1ac0bf70094fd47783c7b0dece89243593348befff801054f799e258a`: 8/8 positive-control lanes passed. However its log-Cholesky diagonal bounds `[-2,-0.5]` make every candidate strictly positive definite. Therefore scientific authority is **bounded SPD-interior optimizer calibration**, not full PSD-boundary calibration. Durable scope correction: `results/ITER025B_G42C_TERMINAL.md`. No G42-A was launched from G42-C.

## Active gate 1 — G42-C2

Protocol: `protocol/ITER025C_G42C2_PSD_BOUNDARY_CALIBRATION.md`.
Launch/head: `858ad4b6848362bf430eaab849fb0ed4166f9cde`.
Run: `34710953936`.

Coordinates: `C=B B^T` with direct Cholesky diagonals `[0,0.60]` and off-diagonals `[-0.30,0.30]`; PSD boundary is included exactly. Positive controls have intended ranks 2/4/5/6. Search is Sobol/LHS × four controls, 32 starts, top-6 refinements, same four times × six product probes.

Each lane must satisfy simultaneously: trace gap `<0.002`; relative Kossakowski error `<0.02`; recovered effective rank at eigenvalue threshold `1e-5` equals hidden rank. Initial terminal rank-6 Sobol lane passed with trace gap `1.3497e-16`, relative C error `8.041e-16`, recovered rank `6/6`.

## Active gate 2 — G42-C3

Protocol: `protocol/ITER025D_G42C3_PSD_RANK_COMPLETION.md`.
Launch/head: `35f719fdad8af1e2f8fdd71727c84abec3857c2a`.
Run: `34711048394`.

Purpose: complete missing boundary-rank calibration with two rank-1 and two rank-3 positive controls, under exactly the same boundary-capable coordinates, bounds, times/probes, Sobol/LHS designs, 32 starts, top-6 refinements and recovery/rank rules as G42-C2.

## Authorization lock

A broad boundary-capable arbitrary-orientation PSD adversarial gate is authorized **only if both G42-C2 and G42-C3 terminally PASS**. Failure of either blocks it. This requirement was frozen before G42-C2 aggregate completion; neither run may be post-hoc retuned.

## Stable finite-comparator layers

- G35: finite K2/K3/K4 additive independent measurement-feedback support.
- G36: one shared Gaussian classical-noise support.
- G37: corrected nested MF + shared-noise finite support.
- G38: OU finite-correlation toy support.
- G39: finite rank2/rank3 multimode white-noise support.
- G40: RTN calibration succeeded but adversarial support unresolved due optimizer nonrobustness.
- G41: rank4/5/6 frame-indexed positive-rate scoped adversarial support.
- G42: full local identifiability + SPD-interior calibration established; PSD-boundary calibration active.

## Open scientific layers

- terminal G42-C2 + G42-C3 boundary calibration;
- only after joint PASS: prospective boundary-capable arbitrary-orientation PSD adversarial test;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and any actual gravity-theory constitution gate.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, treating green CI as scientific PASS, post-hoc threshold/family/witness weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_60_PERCENT + THEORY_ESTABLISHED_0 + FINITE_COMPARATOR_SUPPORT_ONLY + G40_RTN_UNRESOLVED_OPTIMIZER_NONROBUSTNESS + G41A_SCOPED_HIGH_RANK_RATE_PASS + G42J_FULL_LOCAL_RANK_PASS + G42C_SPD_INTERIOR_CALIBRATED + G42C2_PSD_BOUNDARY_RUNNING + G42C3_RANK_COMPLETION_QUEUED`.
