# RQIR-CG research ledger

This is the clean scientific authority ledger for `RQIR-Candidate-Gravity`. Legacy mixed-project ledgers are not scientific authority.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, funnel/gate discipline and general mathematical tools, but not imported physical assumptions, ansatz coefficients, results or desired conclusions. Green CI is never automatically scientific PASS. Frozen criteria/families/witnesses/charts are never weakened post hoc.

## Canonical readiness

- Internal programme readiness: **61%**.
- Theory established: **0%**.
- `58% -> 59%`: corrected G37-A3 scoped comparator closure.
- `59% -> 60%`: G41-A finite high-rank positive-rate comparator closure.
- `60% -> 61%`: G42-A bounded boundary-PSD adversarial comparator closure.
- Calibration, implementation, identifiability and coordinate-coverage gates do not themselves raise readiness.

## Authoritative gate ledger

| Gate | Run / head | Terminal classification / live state | Scope ceiling |
|---|---|---|---|
| G35 | `34697766107` | `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT` | Finite additive independent MF. |
| G36-A | `34703779268` | scoped shared-Gaussian-noise comparator support | One shared Gaussian classical mode. |
| G37-A3 | `34708041385` | `DERIVED_SCOPED_TRULY_NESTED_MF_PLUS_SHARED_BOUNDARY_PRESERVING_COMPARATOR_SUPPORT` | Finite K2 MF + one shared mode. |
| G38-A | `34704373278` | scoped OU colored-trajectory comparator support | Three-time OU toy trajectory. |
| G39-A2 | `34707920572` | rank2/rank3 multimode scoped support | Finite rank3 shared white noise. |
| G40-RC-A / D2 | `34710216045`, `34710444349` | frozen support not met; `PERSISTENT_OPTIMIZER_OR_OBJECTIVE_GEOMETRY_NONROBUSTNESS` | Historical RTN branch: no physics PASS. |
| G41-A | `34710491309` | `DERIVED_SCOPED_HIGH_RANK_RATE_COMPARATOR_SUPPORT` | Frame-indexed rank4/5/6 positive-rate family. |
| G42-J | `34710643103` | `FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE` | 21-param real-PSD local identifiability only. |
| G42-C/C2/C3/R | `34710744967`, `34710953936`, `34711048394`, `34712524241` | bounded-PSD optimizer calibrated and held-out replicated ranks1–6 | Calibration only. |
| G42-A | `34712491707` / `f7f48725...` | `DERIVED_SCOPED_BOUNDARY_PSD_COMPARATOR_SUPPORT` | Single bounded Cholesky chart. |
| G42-BC | `34712857575` / `11b5a060...` | `BOUNDED_CHART_ROTATION_COVERAGE_LIMIT_FOUND` | 14/24 rotated controls in chart; 10/24 outside. |
| G43-A | `34715739668` / `b69524b9...` | `HELDOUT_MULTICHART_BASIS_COVERAGE_PARTIAL_LIMIT` | Fixed five-chart atlas: 25/36 covered. |
| G44-P | `34716135086` / `daf40fca...` | `BASIS_INVARIANT_TRACE_BALL_PSD_REPRESENTATION_VALIDATED` | Basis-invariant bounded PSD trace-ball `tr(C)<=4`; representation only. |
| G40-TM-C | `34716161178` / `aff54cae...` | `TRACE_METRIC_ALIGNED_RTN_OPTIMIZER_CALIBRATED` | Prospective direct-trace RTN optimizer calibration only. |
| G44-C | `34716808171` / `a0061c97...` | **RUNNING: 7/12 terminal at latest durable sync** | Basis-invariant trace-ball optimizer calibration. |
| G40-TM-A | `34716863840` / `114b664e...` | **RUNNING: 2/8 terminal at latest durable sync** | Prospective finite symmetric RTN adversarial gate. |

## Recent decisive terminal provenance

### G42-A / G42-R / G42-BC

G42-A run `34712491707`, aggregate `103605124717`, artifact `10304400253`, digest `sha256:002bea19226bd9b7283a08b36db3e72715762e074f10c40b7114d1e35ac3903c`: all four frozen Sobol/LHS target pairs passed bounded-chart gap/agreement/admissibility. This produced readiness `60% -> 61%`.

G42-R run `34712524241`, aggregate `103604804647`, artifact `10303143301`, digest `sha256:81fa588873316be4c243657cf7e2ac2f0aa08f092de05c969188c39d70c20f10`: 12/12 held-out positive controls ranks1–6 passed.

G42-BC run `34712857575`, aggregate `103606238137`, artifact `10304851327`, digest `sha256:e171c028ed31cd28fd19b1a1f1fd3a1dd91d9aa93a6be641bbfe580ad5b47e4c`: 24/24 basis-covariance checks passed, but only 14/24 rotated controls stayed inside the single chart. This limits G42-A interpretation to its frozen bounded coordinate family.

### G43-A finite-atlas negative coverage result

Run `34715739668`, aggregate `103614423827`, artifact `10304965236`, digest `sha256:7b45a058f3ab45cc93f869a151b5f6dd4c9f32567964d8aaa7eaa170747cb4a9`.

All 36 response-blind lanes valid/covariant; only 25/36 covered by the frozen five-chart atlas. By rank: 1–3 each 6/6; rank4 3/6; rank5 1/6; rank6 3/6. Classification `HELDOUT_MULTICHART_BASIS_COVERAGE_PARTIAL_LIMIT`. No post-hoc chart additions. Durable note: `results/ITER027_G43A_MULTICHART_COVERAGE_TERMINAL.md`.

### G44-P basis-invariant trace-ball representation

Run `34716135086`, aggregate `103615055245`, artifact `10305175168`, digest `sha256:2e9f719f90f0d7df07eebed0c6150d12a7c5fde928c06aa19ab14a3b0ea814f4`.

All 24 response-blind lanes passed for `C=A^2`, symmetric `A`, `||A||_F<=2`, exactly real PSD `tr(C)<=4`. Basis covariance/reconstruction were numerical-clean across ranks1–6 and rotations. Old G42 box is analytically nested (`3.51<4`). Classification `BASIS_INVARIANT_TRACE_BALL_PSD_REPRESENTATION_VALIDATED`. Durable note: `results/ITER028_G44P_TRACE_BALL_PSD_TERMINAL.md`.

### G40-TM-C direct-trace RTN calibration

Run `34716161178`, aggregate `103614850103`, artifact `10305010398`, digest `sha256:1578827bf3cdc8a441eda3ed54bf4d5a9db51a69ebbf903f90420676c79c8ad5`.

All 8 response-blind positive-control lanes passed max-trace-gap `<0.002` with strict candidate-axis-frame BLP `>0.02`. Classification `TRACE_METRIC_ALIGNED_RTN_OPTIMIZER_CALIBRATED`. This does not alter historical G40-RC-A/G40-RC-D2; it prospectively authorizes G40-TM-A only. Durable note: `results/ITER029_G40TMC_TRACE_METRIC_CALIBRATION_TERMINAL.md`.

## Active frontier

### G44-C — run `34716808171`

12 positive-control lanes, ranks1–6 × Sobol/LHS, exact G44 trace-ball family. Frozen lane rules: trace gap `<0.002`, relative Kossakowski error `<0.02`, effective-rank recovery, PSD floor, `tr(C)<=4`.

Latest durable state: 7/12 terminal. Inspected examples all have `scientific_support=true`: rank1/Sobol gap `6.633536482533568e-12`, C error `8.919226019540083e-12`; rank3/Sobol gap `8.706013063248301e-12`, error `2.5530175940222584e-11`; exact radial-boundary rank6/Sobol gap `2.5427402038085165e-16`, error `1.0447115782320849e-15`, rank6/6, `tr(C)=4.0`.

Only terminal 12/12 PASS authorizes G44-A production. Calibration cannot raise readiness.

### G40-TM-A — run `34716863840`

8 prospective RTN adversarial lanes. Frozen pair rule per target shard: both methods strict-BLP; each gap `>1e-4`; Sobol/LHS gap difference `<=0.002`; all four shards.

Latest durable state: 2/8 terminal. Sobol shard0 gap `0.584587750080894`, BLP `0.5664696956410414`; Sobol shard1 gap `0.5724941626871984`, BLP `0.5634482323007587`; both lane-support true. Matching LHS results are still required. A terminal scoped PASS may justify readiness 61→62; any frozen rule failure leaves readiness 61.

## Prepared locked prospective gate

G44-A is frozen before G44-C terminal result:
- protocol `protocol/ITER032_G44A_TRACE_BALL_PSD_ADVERSARIAL.md`, commit `902a8bdf33881a48e4053cd1005a68efbb6d20db`;
- script `scripts/iter032_g44a_trace_ball_psd_adversarial.py`, commit `39575d036646c5d4f1c619dbfea5ae7a809e23ee`;
- workflow commit `beee08a4909f4a4b83bffa9397d3642899180e00`.

There is deliberately no launch marker. Production is forbidden unless G44-C terminally classifies `BASIS_INVARIANT_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED`. If authorized, G44-A uses the exact same `tr(C)<=4` family/search map and the same four G42-A RCG-002 toy target shards with frozen gap `>1e-4`, method agreement `<=0.002`, all four required.

## Open scientific layers

- terminal G44-C and, only if calibrated, prospective G44-A basis-invariant bounded-PSD comparator;
- terminal G40-TM-A finite non-Markovian RTN comparator;
- broader non-Markovian/classically correlated channels beyond finite RTN;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and any actual gravity-theory constitution gate.

## Claim locks

Never promote finite/bounded-family gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen thresholds/families/witnesses/charts post hoc. Invalid/nonrobust historical gates remain invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions.
