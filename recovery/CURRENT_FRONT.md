# RQIR-Candidate-Gravity current front

Updated: 2026-09-13
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_ATTACK`
Active production: **ITER042 / G49-A cap-free/direct-PSD RCG-002 adversarial transport**, run `34729309699`.

## Canonical status

- Candidate-model/programme readiness: **63%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is programme completion, not probability of correctness. G46-A, G48-C, G48-A and G49-C deepen/calibrate the already-counted Markovian-PSD robustness rubric and do not add readiness points.

## Newly closed authority

### Iter041 / G49-C cap-free/direct-PSD response-blind calibration — scoped PASS

Run `34726705385`, head `db61900e4113cf002f3d5c7b636b7e14d41e00c0`, aggregate job `103642168161`, summary artifact `10307129893`, digest `sha256:ec1328e7dfa0de16be7e9d57549c81badff48c16193f9b957d566d996b80657b`.

All `12/12` response-blind lanes are structurally valid and pass the frozen support rule. Both Sobol and LHS pass at requested ranks 1..6; all six cross-method gap differences are `<=0.002` (actual maximum `9.084579650917406e-13`). Classification: `CAPFREE_DIRECT_PSD_OPTIMIZER_CALIBRATED`.

Frozen lane support included exact requested effective rank, trajectory gap `<0.002`, relative Kossakowski error `<0.02`, PSD/TP/CP/output-state/trace controls, and numerical-box inactivity `max(abs(w_i))/8 <0.80`. Scope ceiling: response-blind calibration of direct real-PSD `C=A^2`, not a mathematical global optimum over the unbounded PSD cone. Durable note: `results/ITER041_G49C_CAPFREE_PSD_CALIBRATION_TERMINAL.md`.

### G48-A cap32/cap64 adversarial transport — scoped PASS

Run `34724106251`, head `235e807fbb9f5bf00de42e66a5aa07df90a21116`, aggregate job `103636108319`, summary artifact `10307232484`, digest `sha256:4e58ab8c40a07546e47ea48eec5ffec8ec265e7216869c94702eda0eb50cd5b8`.

All `16/16` lanes structurally valid; all eight cross-method pairs pass nonzero-gap/agreement rules and all cap32/cap64 nesting checks pass. Classification: `DERIVED_SCOPED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP32_CAP64`. Finite-cap scope only.

## Active gate — Iter042 / G49-A

Scientific object: transport the already response-blind calibrated direct real-PSD family `C=A^2` to the unchanged four-shard RCG-002 toy trajectory panel, with no physical trace cap and with numerical box inactivity required.

Prospective preregistration commit: `67c57014859408175d235059db305e56991b23c5`.
Implementation commit: `f9a71c862cd44e55a14d4cfd183a8d56161b2dc2`.
Workflow commit: `5f1d33dd24c11454c0bd801d7c78e37b114cbf9c`.
Launch/head: `1d7154fb328f514bc5e10c8e1dc192b56d3cafd3`.
Authoritative run: `34729309699`.

Frozen matrix: methods `{sobol_lsq,lhs_lsq}` x shards `{0,1,2,3}` = `8` lanes, `fail-fast:false`, safe parallelism 8. Same direct 21-coordinate `C=A^2` family and numerical box `[-8,8]^21` as G49-C; same 32 starts / refine 6 / `max_nfev=1200`; same RCG-002 target/probes/times and inherited `GAP_THRESHOLD=1e-4`. Lane PASS requires physical admissibility plus `box_fraction<0.80` and gap `>1e-4`. Aggregate requires 8/8 structural validity, both methods supporting every shard, method agreement `<=0.002`, and direct-PSD best gap no worse than terminal cap64 best gap + `0.002` for every shard.

Frozen classifications: `G49A_IMPLEMENTATION_OR_NUMERICAL_INVALID`, `G49A_FROZEN_SUPPORT_RULE_NOT_MET`, or `DERIVED_SCOPED_CAPFREE_DIRECT_PSD_COMPARATOR_SUPPORT`.

Interpretation lock: even full PASS is scoped numerical evidence on the frozen RCG-002 panel, not a proof of the global infimum over the unbounded PSD cone and not a universal classical/semiclassical no-go theorem.

## Retained comparator/provenance authority

- G48-C run `34721391489`: `CAP32_CAP64_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED`.
- G46-A run `34719458597`: `DERIVED_SCOPED_EXTENDED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP8_CAP16`.
- G47-A run `34719377641`: `DERIVED_SCOPED_THREE_STATE_CLASSICAL_SWITCHING_COMPARATOR_SUPPORT`.
- G45-P run `34718225194`: complex-PSD GKSL leaves honest classical random-Hamiltonian provenance on frozen controls.
- G40-TM-A run `34716863840`: `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET`; RTN robustness remains unresolved.

## Open scientific layers

- terminally classify active G49-A without retuning;
- broader hidden-classical memory beyond the frozen stationary 3-state/12D family;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and an actual gravity-theory constitution gate.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, green-CI-as-scientific-PASS, post-hoc threshold/family/witness weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_63_PERCENT + THEORY_ESTABLISHED_0 + G49C_CAPFREE_CALIBRATION_PASS + G49A_CAPFREE_TRANSPORT_RUNNING + G48A_SCOPED_FINITE_CAP_SUPPORT + G47A_SCOPED_FINITE_MEMORY_SUPPORT + COMPLEX_PSD_PROVENANCE_BOUNDARY_RETAINED + RTN_ROBUSTNESS_NONCLOSURE_RETAINED`.
