# RQIR-Candidate-Gravity current front

Updated: 2026-09-13
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_ATTACK`

## Canonical status
- Candidate-model/programme readiness: **63%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

## Newly closed authority — Iter044 / G50-C
Scientific classification: `FOUR_STATE_CLASSICAL_SWITCHING_OPTIMIZER_CALIBRATED`.

Provenance: prereg `0de6cd29346ce68888c68ed1965ea0c7af224fb8`; implementation `1eed19071661ec143bf6e3feb350374031dab557`; workflow `a48d0386277de272ffa3b564c3c3d0674ef68492`; authoritative head `4528497f9b34add2bff84bc55db399673ca07c8f`; run `34734256210`; aggregate job `103662830407`; summary artifact `10310302963`; digest `sha256:c600d52b399ca493b537b65507696dda6193be17a3f155f78cbcc85ca8573bba`.

All `8/8` raw lanes were consumed and satisfy the frozen response-blind calibration rule. Across lanes: worst train max trace gap `6.1950671201431e-12`; worst held-out max trace gap `4.109242107956982e-12`; worst normalized parameter error `1.7639089906452824e-10`; worst TP residual `1.776516304761236e-15`; minimum Choi eigenvalue `5.956647395842122e-11`. Sobol/LHS train-gap differences for controls 0..3 are `3.5660541684399162e-12`, `7.034200708641959e-13`, `2.5531430413522786e-12`, `1.386020869958981e-13`, all far below frozen `0.002`.

Scope lock: calibration only for the exact finite bounded stationary 20D four-state hidden-classical CTMC switching/local-sum-Hamiltonian family. It does not establish RCG-002 separation or any general classical-memory/no-go result. Durable note: `results/ITER044_G50C_FOUR_STATE_SWITCHING_CALIBRATION_TERMINAL.md` (result commit `cb008662a4b432bd202885207c6d61590dc56349`).

## Active prospective gate — Iter045 / G50-A
Goal: adversarial transport of the **exact calibrated G50-C family** to the frozen four-shard RCG-002 panel, with independent training and held-out-time checks.

Preregistration commit: `da2ed3bb190fcfc8b3e8225361b98490513630bf` (created before implementation and before target production results).
Implementation commit: `c9fb66bb69ac27d1546f083aec6c95db2033a9e7`.
Workflow commit: `1e689724050b8e7e9734c21395e453fae4da8f2d`.
Launch/head: `2122211ff1c08c03ca637c42b8299fd3a9fd6806`.
Authoritative production run: `34736777512`.

Frozen production: 8 independent lanes = Sobol/LHS × four existing RCG-002 shards; exact 20D G50-C bounds; 32 starts; 6 refinements; 800 max evaluations. Frozen target strengths are `[0.025, 0.10, 0.40, 1.40]`; training times `[0.12,0.35,0.75,1.25]`; held-out times `[0.23,0.58,1.05]`. Scoped support requires admissible candidates with both train and held-out max probe gaps `>1e-4`, plus cross-method agreement `<=0.002` train and `<=0.003` held-out for every shard.

No scientific classification is authorized before terminal raw artifacts and aggregate are consumed.

## Retained authority
- G50-P run `34734173762`: `FOUR_STATE_CLASSICAL_SWITCHING_PROVENANCE_MEMORY_QUALIFIED`.
- G49-A run `34729309699`: `DERIVED_SCOPED_CAPFREE_DIRECT_PSD_COMPARATOR_SUPPORT`.
- G49-C run `34726705385`: `CAPFREE_DIRECT_PSD_OPTIMIZER_CALIBRATED`.
- G48-A run `34724106251`: `DERIVED_SCOPED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP32_CAP64`.
- G47-A run `34719377641`: `DERIVED_SCOPED_THREE_STATE_CLASSICAL_SWITCHING_COMPARATOR_SUPPORT`.
- G45-P run `34718225194`: complex-PSD GKSL leaves honest classical random-Hamiltonian provenance on frozen controls.
- G40-TM-A run `34716863840`: `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET`; RTN robustness unresolved.

## Next allowed gates
1. Consume terminal Iter045/G50-A raw artifacts and aggregate; classify scientifically, not by CI color.
2. If G50-A provides scoped support, the four-state target-separation rubric may close; do not extrapolate beyond the exact finite family.
3. Externally anchored held-out observables remain an independent high-value direction if definable without imported project physics.
4. Continuum/full candidate-gravity dynamics and gravity-theory constitution remain open.

## Claim locks
Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, green-CI-as-scientific-PASS, post-hoc threshold/family/witness weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:
`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_63_PERCENT + THEORY_ESTABLISHED_0 + G50P_FOUR_STATE_MEMORY_QUALIFIED + G50C_OPTIMIZER_CALIBRATED + ITER045_G50A_RUNNING + G49A_CAPFREE_DIRECT_PSD_SCOPED_SUPPORT + G47A_FINITE_MEMORY_SUPPORT + RTN_ROBUSTNESS_NONCLOSURE_RETAINED`.
