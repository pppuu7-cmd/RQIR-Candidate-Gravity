# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_ATTACK`
Active production gates: `ITER032 / G44-A basis-invariant trace-ball adversarial` + `ITER033 / G45-P complex-PSD provenance boundary`

## Canonical status

- Candidate-model/programme readiness: **61%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is programme completion, not probability of correctness. Calibration/implementation/provenance/coverage gates do not raise readiness. Only a terminal new physics/comparator rubric closure can trigger a readiness review.

## Newly closed authority

### G44-C basis-invariant trace-ball optimizer calibration — PASS

Run `34716808171`, head `a0061c979963b8b891fdb886de79424711516993`, aggregate `103616615329`, artifact `10304911987`, digest `sha256:7e34d6843135c670230839027cffb3d65f5a6d0fb70b8ed8b82f880ef0daf7db`.

All 12 response-blind positive controls ranks1–6 × Sobol/LHS passed. LHS radial-boundary rank6: gap `3.4694469519536137e-16`, relative Kossakowski error `1.18731827336088e-15`, recovered rank6 and `tr(C)=4.0`. Classification `BASIS_INVARIANT_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED`. Calibration only; no readiness increment. Durable note: `results/ITER030_G44C_TRACE_BALL_CALIBRATION_TERMINAL.md`.

### G40-TM-A prospective RTN adversarial — FROZEN SUPPORT RULE NOT MET

Run `34716863840`, aggregate `103616629784`, artifact `10305770549`, digest `sha256:7ece1af4ca748acc2a0597b1c5f900e58e805de2cfdf2d01a7f2cc6fed1d3a4b`.

All 8 lanes were structurally valid, strict-BLP admissible and individually had large nonzero gaps, but the frozen Sobol/LHS agreement `<=0.002` failed in all four shards: differences `0.0200349612`, `0.0231292421`, `0.00517398865`, `0.00742134795`. Classification `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET`. No threshold weakening or retroactive optimizer rescue. This is method-robustness nonclosure for the frozen finite RTN experiment, not a universal RTN physics no-go. Durable note: `results/ITER031_G40TMA_TRACE_METRIC_RTN_ADVERSARIAL_TERMINAL.md`. Readiness remains 61%.

## Active gate 1 — G44-A basis-invariant trace-ball PSD adversarial

G44-A was frozen before G44-C terminal:
- scientific protocol `protocol/ITER032_G44A_TRACE_BALL_PSD_ADVERSARIAL.md`;
- script `scripts/iter032_g44a_trace_ball_psd_adversarial.py`;
- workflow `.github/workflows/rcg-iter032-g44a-trace-ball-psd-adversarial.yml`.

After consuming terminal G44-C PASS, launch marker commit `fbb9305039bc44086e100ba23fe4c90e2a13cd97` authorized production unchanged. Active run: **`34718045811`**.

8 lanes = Sobol/LHS × 4 frozen RCG-002 toy target shards. Frozen per-shard rule: both lanes admissible/supporting, gap `>1e-4`, absolute cross-method gap difference `<=0.002`; all four shards required. Scope is only the bounded basis-invariant real-PSD Markovian trace-ball `tr(C)<=4`; no universal classical/semiclassical no-go.

Latest state at this durable sync: 1 lane in progress, 7 queued, 0 terminal. A terminal scientific PASS may justify readiness `61% -> 62%` after rubric review; any frozen rule failure leaves readiness at 61%.

## Active gate 2 — G45-P complex-Hermitian PSD provenance boundary

Response-blind independent stream; **no RCG-002 target**.

- preregistration commit `fae8063aba169ad77f4928e4a8febaf4a2839d45` before implementation;
- implementation commit `83856b814b46b9af85b298dd48a57f860549cd37`;
- workflow commit `ac0f8147ffa90f645ea9d45b14679da991464eeb`;
- launch commit `35583bcaa013944017a18c56f8f05714b616ee81`;
- active run **`34718225194`**.

12 lanes = real-PSD classical controls, same-site complex PSD controls, cross-site complex PSD controls × 4 shards. Frozen question: does generic complex-Hermitian PSD GKSL structure leave the linear provenance span of all 21 real-symmetric Kossakowski dissipators plus six local-Hamiltonian commutators on the local-Pauli basis? This prevents incorrectly calling a broader quantum GKSL family a classical random-Hamiltonian comparator. A PASS is provenance-only and cannot raise readiness.

Latest state at this durable sync: run queued; matrix jobs not yet materialized.

## Stable scientific closures / limits

- G35 finite K2/K3/K4 additive MF scoped support.
- G36 shared Gaussian classical-noise scoped support.
- G37 corrected nested MF + shared-noise scoped support.
- G38 OU finite-correlation toy support.
- G39 finite rank2/rank3 multimode support.
- Historical G40 RTN branches plus G40-TM-A remain without robust prospective physics support; do not rescue post hoc.
- G41 rank4/5/6 frame-indexed positive-rate scoped support.
- G42 bounded PSD calibration + scoped bounded-chart adversarial support; readiness `60% -> 61%`.
- G42-BC single-chart basis coverage limit.
- G43 frozen five-chart atlas partial limit: 25/36 held-out controls covered.
- G44-P basis-invariant real-PSD trace-ball representation PASS.
- G44-C basis-invariant trace-ball optimizer calibration PASS.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, green-CI-as-scientific-PASS, post-hoc threshold/family/witness/chart weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_61_PERCENT + THEORY_ESTABLISHED_0 + G44C_CALIBRATED + G40TMA_FROZEN_SUPPORT_RULE_NOT_MET + G44A_RUNNING + G45P_RUNNING_RESPONSE_BLIND_PROVENANCE`.
