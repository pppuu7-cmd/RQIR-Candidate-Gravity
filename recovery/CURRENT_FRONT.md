# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_ATTACK`
Active production gate: `ITER038 / G46-A extended trace-ball adversarial`

## Canonical status

- Candidate-model/programme readiness: **63%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is programme completion, not probability of correctness. `61% -> 62%` came from G44-A; `62% -> 63%` comes from terminal G47-A closing a distinct finite hidden-classical memory comparator layer. Calibration/provenance gates alone never raise readiness.

## Newly closed authority

### G47-A explicit three-state hidden-classical switching adversarial — PASS

Run `34719377641`, launch/head `4898523929c698030c49709b6210a21d8f5d2095`, aggregate `103622436777`, summary artifact `10305072882`, digest `sha256:f75f0a590cae9978b5abe2e56386f237d4e05323c94c4e4321cbb22ab1ef99dd`.

All 8/8 lanes pass structural/provenance and all four frozen Sobol/LHS pair-agreement rules. Gap pairs:
- s0 `0.6385600880482375 / 0.6385600884311459`, diff `3.8290837167664904e-10`;
- s1 `0.6784960973078257 / 0.6784961451118307`, diff `4.780400497672588e-08`;
- s2 `0.8235518631773218 / 0.8235518632703851`, diff `9.306333481617912e-11`;
- s3 `0.7695388395862157 / 0.7695390013607699`, diff `1.6177455419708053e-07`.

Classification `DERIVED_SCOPED_THREE_STATE_CLASSICAL_SWITCHING_COMPARATOR_SUPPORT`. Scope ceiling: only the frozen bounded 12D stationary three-state CTMC switching/product-unitary family; not arbitrary classical memory or a universal no-go. Durable note: `results/ITER037_G47A_THREE_STATE_SWITCHING_ADVERSARIAL_TERMINAL.md`. Readiness `62% -> 63%`.

### G47-C three-state switching optimizer calibration — PASS

Run `34719251400`, launch/head `2623e3e898f197cfdacce5a02532b416e886298e`, aggregate `103622040491`, artifact `10305347477`, digest `sha256:8d5f005501a97c2623da1e83d823732ec44210187bd3f84243873595bfdf09bf`.

All 8/8 response-blind positive controls pass. Worst training gap `5.4275615639463476e-11`, held-out gap `3.599259601883243e-11`, normalized parameter error `7.652303300674281e-10`, provenance 8/8. Classification `THREE_STATE_CLASSICAL_SWITCHING_OPTIMIZER_CALIBRATED`. Calibration only. Durable note: `results/ITER036_G47C_THREE_STATE_SWITCHING_CALIBRATION_TERMINAL.md`.

### G46-C extended basis-invariant trace-ball calibration — PASS

Run `34719083985`, launch/head `9c1f78dd72d70ad3f47a6fc54ef0c550a64a4290`, aggregate `103622183765`, artifact `10305154162`, digest `sha256:7d6193093c2dc423a479e747707c80af1975f4d87bfd646207d426830ecad0c6`.

All 24/24 response-blind lanes pass. Cap8: 12/12, worst gap `1.0900999144735261e-11`, worst relative C error `3.479885009977411e-11`. Cap16: 12/12, worst gap `2.393957298667677e-11`, worst relative C error `9.32022808014185e-11`. Classification `EXTENDED_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED_CAP8_CAP16`. Calibration only. Durable note: `results/ITER034_G46C_EXTENDED_TRACE_BALL_CALIBRATION_TERMINAL.md`.

### Earlier decisive closures / limits

- G44-A run `34718045811`: `DERIVED_SCOPED_BASIS_INVARIANT_TRACE_BALL_PSD_COMPARATOR_SUPPORT`; bounded real-PSD Markovian `tr(C)<=4`; readiness `61% -> 62%`.
- G45-P run `34718225194`: generic complex-PSD GKSL leaves honest classical random-Hamiltonian provenance on frozen controls; complex PSD cannot be relabelled classical without constructive proof.
- G47-P run `34719123666`: explicit three-state hidden-classical/product-unitary provenance validated; 6/6 non-semigroup witnesses.
- G40-TM-A run `34716863840`: `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET`; all four RTN Sobol/LHS pairs violated frozen agreement; no post-hoc rescue and no universal RTN no-go.

## Active gate — G46-A extended trace-ball adversarial

Preregistered only after terminal G46-C PASS.

- protocol `protocol/ITER038_G46A_EXTENDED_TRACE_BALL_ADVERSARIAL.md`, commit `6524210a531f80efe8596a6f3ab00000c2c1389b`;
- implementation `362a830a631b8fcf7f54912905d27dba0af43052`;
- workflow `62bf42fe811301f90b59e43114b05172f3462a5b`;
- launch/head `a2dd7fd3cf3b40f642077c62bd1c0020a97d12bb`;
- run **`34719458597`**.

16 lanes = caps `{8,16}` × Sobol/LHS × four frozen G44-A RCG-002 toy targets. Frozen rules: lane gap `>1e-4`, pair agreement `<=0.002`, and mathematically required cap nesting `best(cap16) <= best(cap8)+0.002` per shard. Latest durable state: **0/16 terminal, 16 queued**. A terminal PASS must not automatically add another readiness point if it only deepens the already-counted bounded Markovian PSD rubric; assess information gain and double-counting first.

## Stable scientific closures / limits

- G35–G39 finite MF/shared/OU/multimode scoped support layers.
- G40 RTN branch remains robustness-unresolved.
- G41 high-rank frame-indexed support.
- G42 bounded PSD scoped support plus single-chart coverage limit.
- G43 finite-atlas partial coverage limit.
- G44 basis-invariant real-PSD trace-ball representation/calibration/scoped support at cap4.
- G45 complex-PSD classical-provenance boundary.
- G47 explicit finite stationary three-state hidden-classical memory provenance/calibration/scoped support.

## Open scientific layers

- terminal G46-A extended cap8/cap16 bounded Markovian PSD attack;
- broader hidden-classical memory beyond the frozen stationary 3-state 12D family;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and an actual gravity-theory constitution gate.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, green-CI-as-scientific-PASS, post-hoc threshold/family/witness weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_63_PERCENT + THEORY_ESTABLISHED_0 + G44A_SCOPED_MARKOVIAN_PSD_SUPPORT + G47A_SCOPED_FINITE_MEMORY_SUPPORT + G46A_RUNNING_EXTENDED_PSD + COMPLEX_PSD_PROVENANCE_BOUNDARY_RETAINED + RTN_ROBUSTNESS_NONCLOSURE_RETAINED`.
