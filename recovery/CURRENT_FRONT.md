# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active gates: `ITER030 / G44-C basis-invariant trace-ball calibration` + `ITER031 / G40-TM-A prospective RTN adversarial`
Prepared locked next gate: `ITER032 / G44-A basis-invariant trace-ball adversarial`
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_ATTACK`

## Canonical status

- Candidate-model/programme readiness: **61%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is programme completion, not probability of correctness. Calibration/implementation/coverage gates do not raise readiness. Only a terminal new physics/comparator rubric closure can trigger a readiness review.

## Newly closed authority

### G43-A finite multichart atlas — PARTIAL LIMIT

Run `34715739668`, head `b69524b9fe8c33ff2f433f1d9dbc6ce54f8e4a06`, aggregate `103614423827`, artifact `10304965236`, digest `sha256:7b45a058f3ab45cc93f869a151b5f6dd4c9f32567964d8aaa7eaa170747cb4a9`.

All 36 response-blind lanes were structurally valid and basis-covariant. The frozen five-chart atlas covered only **25/36**: ranks 1/2/3 = 6/6 each, rank4 = 3/6, rank5 = 1/6, rank6 = 3/6. Classification `HELDOUT_MULTICHART_BASIS_COVERAGE_PARTIAL_LIMIT`. No chart may be added post hoc. Durable note: `results/ITER027_G43A_MULTICHART_COVERAGE_TERMINAL.md`.

### G44-P basis-invariant PSD trace-ball representation — PASS

Run `34716135086`, head `daf40fca9e5e6dc6f98b7673d5c2d34a4cc75552`, aggregate `103615055245`, artifact `10305175168`, digest `sha256:2e9f719f90f0d7df07eebed0c6150d12a7c5fde928c06aa19ab14a3b0ea814f4`.

Frozen family: `C=A^2`, `A=A^T`, `||A||_F<=2`, equivalently real PSD `tr(C)<=4`. All 24 rank1–6 × local-basis-rotation lanes passed representation, rank, trace-ball and covariance conditions. The old G42 box is analytically contained because max `||B||_F^2=3.51<4`. Classification `BASIS_INVARIANT_TRACE_BALL_PSD_REPRESENTATION_VALIDATED`. No readiness increment. Durable note: `results/ITER028_G44P_TRACE_BALL_PSD_TERMINAL.md`.

### G40-TM-C trace-metric RTN calibration — PASS

Run `34716161178`, head `aff54cae0954eb06771337ab315672a049450923`, aggregate `103614850103`, artifact `10305010398`, digest `sha256:1578827bf3cdc8a441eda3ed54bf4d5a9db51a69ebbf903f90420676c79c8ad5`.

All 8 response-blind positive-control lanes passed direct max-trace-distance recovery with strict axis-covariant BLP. Classification `TRACE_METRIC_ALIGNED_RTN_OPTIMIZER_CALIBRATED`. Historical G40-RC-A/G40-RC-D2 negative/nonrobust verdicts remain immutable; this is a new prospective optimizer calibration, not a retroactive repair. No readiness increment. Durable note: `results/ITER029_G40TMC_TRACE_METRIC_CALIBRATION_TERMINAL.md`.

## Active gate 1 — G44-C basis-invariant trace-ball optimizer calibration

Prereg `protocol/ITER030_G44C_TRACE_BALL_OPTIMIZER_CALIBRATION.md` frozen before G44-P terminal. Launch/head `a0061c979963b8b891fdb886de79424711516993`; run `34716808171`.

12 positive-control lanes = ranks 1–6 × Sobol/LHS. Same exact physical family `tr(C)<=4`; six hidden controls include rank-deficient boundaries and exact radial boundary rank6. Frozen lane rules: max trace gap `<0.002`, relative C error `<0.02`, rank recovery, PSD floor and trace-ball membership.

Latest live state at this update: **7/12 terminal = 58.3%**, one additional lane in progress. All inspected completed lanes support. Examples: rank1/Sobol gap `6.6335e-12`, relative C error `8.9192e-12`, rank 1/1; rank3/Sobol gap `8.7060e-12`, error `2.5530e-11`, rank 3/3; rank6 radial-boundary/Sobol gap `2.5427e-16`, error `1.0447e-15`, `tr(C)=4.0`, rank 6/6.

Only terminal 12/12 PASS may authorize G44-A production.

## Active gate 2 — G40-TM-A prospective RTN adversarial

Prereg `protocol/ITER031_G40TMA_TRACE_METRIC_RTN_ADVERSARIAL.md` and implementation/workflow were frozen before G40-TM-C aggregate. Launch/head `114b664e328fdfb9328bcd7606d8e9d9a58ce5bd`; run `34716863840`.

8 prospective lanes = Sobol/LHS direct-trace optimizer × four frozen G40-RC-A RCG-002 toy target shards. Same finite symmetric hidden-classical RTN family, same candidate-axis-frame BLP witness, same target convention. Frozen pair rule per shard: both strict-BLP candidates, each gap `>1e-4`, Sobol/LHS gap difference `<=0.002`; all four shards required.

Latest live state: **2/8 terminal = 25%**. Sobol shard0 gap `0.584587750080894`, BLP `0.5664696956410414`; Sobol shard1 gap `0.5724941626871984`, BLP `0.5634482323007587`; both lane-support true. These are early non-terminal results. Cross-method agreement is not known until matching LHS lanes finish.

A terminal PASS here would close a new scoped non-Markovian RTN comparator layer and may justify readiness `61% -> 62%` after rubric review. Any rule failure leaves readiness at 61%.

## Prepared but locked — G44-A

Frozen before G44-C terminal:
- protocol `protocol/ITER032_G44A_TRACE_BALL_PSD_ADVERSARIAL.md`, commit `902a8bdf33881a48e4053cd1005a68efbb6d20db`;
- script `scripts/iter032_g44a_trace_ball_psd_adversarial.py`, commit `39575d036646c5d4f1c619dbfea5ae7a809e23ee`;
- workflow `.github/workflows/rcg-iter032-g44a-trace-ball-psd-adversarial.yml`, commit `beee08a4909f4a4b83bffa9397d3642899180e00`.

Production launch marker is deliberately absent. If and only if G44-C terminally PASSes, G44-A may be launched unchanged: same basis-invariant `tr(C)<=4` family/search map, same four G42-A target shards, gap `>1e-4`, Sobol/LHS agreement `<=0.002`, all four shards.

## Stable scientific closures

- G35 finite K2/K3/K4 additive MF scoped support.
- G36 shared Gaussian classical-noise scoped support.
- G37 corrected nested MF + shared-noise scoped support.
- G38 OU finite-correlation toy support.
- G39 finite rank2/rank3 multimode support.
- G40 historical RTN adversarial unresolved due old optimizer nonrobustness; new G40-TM-A is prospective and active.
- G41 rank4/5/6 frame-indexed positive-rate scoped support.
- G42 bounded PSD calibration + scoped bounded-chart adversarial support; readiness `60% -> 61%`.
- G42-BC single-chart basis coverage limit.
- G43 finite-atlas partial coverage limit.
- G44-P basis-invariant trace-ball representation PASS; G44-C calibration active.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, green-CI-as-scientific-PASS, post-hoc threshold/family/witness/chart weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_61_PERCENT + THEORY_ESTABLISHED_0 + G42A_SCOPED_BOUNDED_PSD_SUPPORT + G43A_FINITE_ATLAS_PARTIAL_LIMIT + G44P_BASIS_INVARIANT_TRACE_BALL_REPRESENTATION_PASS + G44C_RUNNING + G40TMC_CALIBRATED + G40TMA_RUNNING + G44A_PREPARED_LOCKED`.
