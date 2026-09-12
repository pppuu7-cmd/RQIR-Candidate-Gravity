# RQIR-CG research ledger

This is the clean scientific authority ledger for `RQIR-Candidate-Gravity`. Legacy mixed-project ledgers are not scientific authority.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, funnel/gate discipline and general mathematical tools, but not imported physical assumptions, ansatz coefficients, results or desired conclusions. Green CI is never automatically scientific PASS. Frozen criteria/families/witnesses/charts are never weakened post hoc.

## Canonical readiness

- Internal programme readiness: **63%**.
- Theory established: **0%**.
- `58% -> 59%`: corrected G37-A3 scoped comparator closure.
- `59% -> 60%`: G41-A finite high-rank positive-rate comparator closure.
- `60% -> 61%`: G42-A bounded boundary-PSD adversarial comparator closure.
- `61% -> 62%`: G44-A basis-invariant real-PSD `tr(C)<=4` comparator closure.
- `62% -> 63%`: G47-A explicit finite hidden-classical memory comparator closure.
- G46-A and G48-C deepen/calibrate the already-counted Markovian PSD rubric and do not add readiness points. Calibration, implementation, identifiability, provenance and coordinate-coverage gates do not themselves raise readiness.

## Authoritative gate ledger

| Gate | Run / head | Terminal classification / live state | Scope ceiling |
|---|---|---|---|
| G35 | `34697766107` | `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT` | Finite additive MF. |
| G36-A | `34703779268` | scoped shared-Gaussian-noise comparator support | One shared Gaussian classical mode. |
| G37-A3 | `34708041385` | `DERIVED_SCOPED_TRULY_NESTED_MF_PLUS_SHARED_BOUNDARY_PRESERVING_COMPARATOR_SUPPORT` | Finite K2 MF + one shared mode. |
| G38-A | `34704373278` | scoped OU colored-trajectory comparator support | Three-time OU toy trajectory. |
| G39-A2 | `34707920572` | rank2/rank3 multimode scoped support | Finite rank3 shared white noise. |
| G40-RC-A / D2 | `34710216045`, `34710444349` | `PERSISTENT_OPTIMIZER_OR_OBJECTIVE_GEOMETRY_NONROBUSTNESS` | Historical RTN branch: no physics PASS. |
| G41-A | `34710491309` | `DERIVED_SCOPED_HIGH_RANK_RATE_COMPARATOR_SUPPORT` | Frame-indexed rank4/5/6 positive-rate family. |
| G42-A | `34712491707` | `DERIVED_SCOPED_BOUNDARY_PSD_COMPARATOR_SUPPORT` | Single bounded Cholesky chart. |
| G42-BC | `34712857575` | `BOUNDED_CHART_ROTATION_COVERAGE_LIMIT_FOUND` | Single-chart coverage limit. |
| G43-A | `34715739668` | `HELDOUT_MULTICHART_BASIS_COVERAGE_PARTIAL_LIMIT` | Fixed five-chart atlas 25/36. |
| G44-P | `34716135086` | `BASIS_INVARIANT_TRACE_BALL_PSD_REPRESENTATION_VALIDATED` | Real-PSD basis-invariant cap4 representation. |
| G44-C | `34716808171` | `BASIS_INVARIANT_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED` | Calibration only. |
| G40-TM-A | `34716863840` | `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET` | Finite RTN robustness nonclosure. |
| G44-A | `34718045811` | `DERIVED_SCOPED_BASIS_INVARIANT_TRACE_BALL_PSD_COMPARATOR_SUPPORT` | Bounded real-PSD Markovian `tr(C)<=4`. |
| G45-P | `34718225194` | `COMPLEX_PSD_EXTENDS_BEYOND_CLASSICAL_RANDOM_HAMILTONIAN_PROVENANCE_ON_FROZEN_CONTROLS` | Provenance boundary only. |
| G47-P | `34719123666` | `THREE_STATE_CLASSICAL_SWITCHING_PRODUCT_UNITARY_PROVENANCE_VALIDATED` | Explicit finite hidden-classical memory provenance. |
| G46-C | `34719083985` | `EXTENDED_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED_CAP8_CAP16` | Calibration only. |
| G47-C | `34719251400` | `THREE_STATE_CLASSICAL_SWITCHING_OPTIMIZER_CALIBRATED` | Calibration only. |
| G47-A | `34719377641` | `DERIVED_SCOPED_THREE_STATE_CLASSICAL_SWITCHING_COMPARATOR_SUPPORT` | Frozen bounded 12D stationary 3-state CTMC family only. |
| G46-A | `34719458597` | `DERIVED_SCOPED_EXTENDED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP8_CAP16` | Fixed bounded real-PSD caps 8/16; not unbounded PSD. |
| G48-C | `34721391489` / `194db0cf...` | `CAP32_CAP64_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED` | Response-blind finite cap32/cap64 calibration only. |
| G48-A | launch head `235e807f...` | **ACTIVE / unclassified** | Finite cap32/cap64 adversarial transport only. |

## G48-C terminal authority

Run `34721391489`, aggregate job `103628932444`, summary artifact `10307000228`, digest `sha256:a31ba73467efeb83cb15c045f8928cc6e84c9dbf09a407e0052ac877b3a01ce9`.

All `24/24` response-blind positive-control lanes are structurally valid and meet the preregistered calibration rule. cap32: 12/12 PASS, worst gap `2.8474088570401036e-11`, worst relative Kossakowski error `2.83680640607369e-10`, ranks 12/12. cap64: 12/12 PASS, worst gap `6.153799793735667e-10`, worst relative Kossakowski error `1.6423013282529114e-05`, ranks 12/12. Classification `CAP32_CAP64_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED`.

This is calibration only; readiness stays 63%. Durable note: `results/ITER039_G48C_CAP32_CAP64_CALIBRATION_TERMINAL.md`.

## Active frontier

`Iter040 / G48-A` was prospectively frozen only after terminal G48-C classification. Preregistration commit `8cec8199300d8930cde6cbfb9e2331b24235c50b`; implementation `ea0e0dc12efeee80e680e01d62fc62b7ea608258`; workflow `5cbc3e89a9f10db63b2e82657b4cfde85f7f647f`; launch/head `235e807fbb9f5bf00de42e66a5aa07df90a21116`.

Frozen matrix: caps `{32,64}` × Sobol/LHS × four RCG-002 shards = 16 lanes. Same G46-A target/family/optimizer/admissibility thresholds. Aggregate requires both methods to meet the nonzero-gap rule and agree within `0.002`, plus cap32 nesting against terminal cap16 minima and cap64 nesting against cap32 within `0.002`. No retuning is authorized.

## Open scientific layers

- terminal G48-A wider finite-cap transport, without claiming an unbounded limit;
- broader hidden-classical memory beyond the frozen stationary 3-state/12D family;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and an actual gravity-theory constitution gate.

## Claim locks

Never promote finite/bounded-family gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen thresholds/families/witnesses post hoc. Invalid/nonrobust historical gates remain invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions. `THEORY_ESTABLISHED` remains 0%.
