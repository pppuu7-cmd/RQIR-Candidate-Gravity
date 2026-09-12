# RQIR-Candidate-Gravity current front

Updated: 2026-09-13
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_ATTACK`
Active production: `ITER040 / G48-A cap32-cap64 adversarial transport`.

## Canonical status

- Candidate-model/programme readiness: **63%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is programme completion, not probability of correctness. `61% -> 62%` came from G44-A; `62% -> 63%` from terminal G47-A. G46-A and calibration gates deepen already-counted comparator robustness and do not add readiness points.

## Newly closed authority

### G48-C cap32/cap64 response-blind calibration — PASS

Run `34721391489`, launch/head `194db0cf51577a62080227a4f0ade3ed29f49a3a`, aggregate job `103628932444`, summary artifact `10307000228`, digest `sha256:a31ba73467efeb83cb15c045f8928cc6e84c9dbf09a407e0052ac877b3a01ce9`.

All `24/24` lanes are structurally valid and satisfy the frozen positive-control rule. cap32: 12/12 PASS, worst gap `2.8474088570401036e-11`, worst relative Kossakowski error `2.83680640607369e-10`, ranks 12/12. cap64: 12/12 PASS, worst gap `6.153799793735667e-10`, worst relative Kossakowski error `1.6423013282529114e-05`, ranks 12/12.

Frozen classification: `CAP32_CAP64_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED`. Calibration only: no readiness increment, no comparator-separation claim and no unbounded-PSD claim. Durable note: `results/ITER039_G48C_CAP32_CAP64_CALIBRATION_TERMINAL.md`.

### Retained comparator/provenance authority

- G46-A run `34719458597`: `DERIVED_SCOPED_EXTENDED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP8_CAP16`.
- G47-A run `34719377641`: `DERIVED_SCOPED_THREE_STATE_CLASSICAL_SWITCHING_COMPARATOR_SUPPORT`.
- G45-P run `34718225194`: complex-PSD GKSL leaves honest classical random-Hamiltonian provenance on frozen controls.
- G40-TM-A run `34716863840`: `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET`; RTN robustness remains unresolved.

## Active authorized gate

`ITER040 / G48-A`: separately prospectively frozen adversarial transport of the calibrated basis-invariant real-PSD trace-ball family to caps `{32,64}` against the unchanged four-shard RCG-002 toy trajectory panel.

Preregistration commit: `8cec8199300d8930cde6cbfb9e2331b24235c50b`.
Implementation commit: `ea0e0dc12efeee80e680e01d62fc62b7ea608258`.
Workflow commit: `5cbc3e89a9f10db63b2e82657b4cfde85f7f647f`.
Launch/head commit: `235e807fbb9f5bf00de42e66a5aa07df90a21116`.

Frozen matrix: caps `{32,64}` × `{sobol_lsq,lhs_lsq}` × shards `{0,1,2,3}` = 16 lanes, `fail-fast:false`. Same family/target convention/optimizer/admissibility thresholds as G46-A. Aggregate requires both methods to pass each lane, cross-method best-gap agreement `<=0.002`, cap32 nesting against terminal cap16 minima and cap64 nesting against cap32, both with tolerance `0.002`.

Even PASS remains finite-cap scoped Markovian evidence and does not authorize an unbounded limit or universal classical/semiclassical no-go.

## Stable scientific closures / limits

- G35–G39 finite MF/shared/OU/multimode scoped support layers.
- G40 RTN branch remains robustness-unresolved.
- G41 high-rank frame-indexed support.
- G42 bounded PSD scoped support plus single-chart coverage limit.
- G43 finite-atlas partial coverage limit.
- G44 basis-invariant real-PSD trace-ball representation/calibration/scoped support at cap4.
- G45 complex-PSD classical-provenance boundary.
- G46 bounded Markovian real-PSD support extended through caps 8/16.
- G47 explicit finite stationary three-state hidden-classical memory provenance/calibration/scoped support.
- G48-C response-blind optimizer calibration through finite caps 32/64.

## Open scientific layers

- terminal classification of G48-A wider finite-cap transport;
- broader hidden-classical memory beyond the frozen stationary 3-state/12D family;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and an actual gravity-theory constitution gate.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, green-CI-as-scientific-PASS, post-hoc threshold/family/witness weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_63_PERCENT + THEORY_ESTABLISHED_0 + G48C_CALIBRATED_CAP32_CAP64 + G48A_ACTIVE_FINITE_CAP_TRANSPORT + G47A_SCOPED_FINITE_MEMORY_SUPPORT + COMPLEX_PSD_PROVENANCE_BOUNDARY_RETAINED + RTN_ROBUSTNESS_NONCLOSURE_RETAINED`.
