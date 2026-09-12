# RQIR-Candidate-Gravity current front

Updated: 2026-09-13
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_ATTACK`
Active production: `ITER041 / G49-C cap-free direct-PSD response-blind calibration`, run `34726705385`.

## Canonical status

- Candidate-model/programme readiness: **63%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is programme completion, not probability of correctness. G46-A, G48-C and G48-A deepen the already-counted Markovian-PSD robustness rubric and do not add readiness points.

## Newly closed authority

### G48-A cap32/cap64 adversarial transport — scoped PASS

Run `34724106251`, head `235e807fbb9f5bf00de42e66a5aa07df90a21116`, aggregate job `103636108319`, summary artifact `10307232484`, digest `sha256:4e58ab8c40a07546e47ea48eec5ffec8ec265e7216869c94702eda0eb50cd5b8`.

All `16/16` lanes are structurally valid. All eight cross-method pairs satisfy the frozen nonzero-gap support rule and agree within `0.002` (actual differences `1.64e-08` to `3.70e-07`). All four cap32-vs-terminal-cap16 and all four cap64-vs-cap32 nesting checks pass. Classification: `DERIVED_SCOPED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP32_CAP64`.

Scope ceiling: finite basis-invariant real-PSD Markovian trace caps 32/64 on the frozen RCG-002 toy panel only. No unbounded-PSD or universal classical/semiclassical no-go claim is authorized. Durable note: `results/ITER040_G48A_CAP32_CAP64_ADVERSARIAL_TERMINAL.md`.

## Active authorized gate

### Iter041 / G49-C — cap-free/direct-PSD response-blind calibration

Preregistration commit: `2d472c4223602f77e13b054615e713c58f0b46c3`.
Implementation commit: `05a41f62b36e0912f60c01f7aa1657130c3c66d4`.
Workflow commit: `7c31d7d19f4847b12043e15ba1699740e0fd7af3`.
Launch/head commit: `db61900e4113cf002f3d5c7b636b7e14d41e00c0`.
Authoritative run: `34726705385`.

Family: real symmetric `A` in direct physical-scale weighted coordinates with `C=A^2`; no trace cap. A numerical coordinate box `[-8,8]^21` is allowed only if demonstrably inactive (`max |w_i| / 8 < 0.80`). Response-blind controls span ranks 1..6 and fixed `sqrt(tr(C)) = [0.5,1,2,3,4,5]`; methods Sobol/LHS; 12 lanes total, `fail-fast:false`, max parallel 6. Frozen lane criteria include gap `<0.002`, relative Kossakowski error `<0.02`, exact requested effective rank, PSD/TP/CP/state/trace admissibility, and box inactivity. RCG-002 is not used in calibration.

Even G49-C PASS is calibration only; it authorizes a later prospectively frozen RCG-002 transport but does not prove a mathematical optimum over all unbounded PSD generators.

## Retained comparator/provenance authority

- G48-C run `34721391489`: `CAP32_CAP64_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED`.
- G46-A run `34719458597`: `DERIVED_SCOPED_EXTENDED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP8_CAP16`.
- G47-A run `34719377641`: `DERIVED_SCOPED_THREE_STATE_CLASSICAL_SWITCHING_COMPARATOR_SUPPORT`.
- G45-P run `34718225194`: complex-PSD GKSL leaves honest classical random-Hamiltonian provenance on frozen controls.
- G40-TM-A run `34716863840`: `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET`; RTN robustness remains unresolved.

## Open scientific layers

- terminal G49-C classification and, only after PASS, cap-free/direct-PSD RCG-002 transport;
- broader hidden-classical memory beyond the frozen stationary 3-state/12D family;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and an actual gravity-theory constitution gate.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, green-CI-as-scientific-PASS, post-hoc threshold/family/witness weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_63_PERCENT + THEORY_ESTABLISHED_0 + G48A_SCOPED_FINITE_CAP_SUPPORT + G49C_ACTIVE_CAPFREE_CALIBRATION + G47A_SCOPED_FINITE_MEMORY_SUPPORT + COMPLEX_PSD_PROVENANCE_BOUNDARY_RETAINED + RTN_ROBUSTNESS_NONCLOSURE_RETAINED`.
