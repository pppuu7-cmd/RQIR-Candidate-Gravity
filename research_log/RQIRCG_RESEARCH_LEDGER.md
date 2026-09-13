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
- G46-A, G48-C, G48-A and G49-C deepen/calibrate the already-counted Markovian PSD rubric and do not add readiness points. Calibration, implementation, identifiability, provenance and coordinate-coverage gates do not themselves raise readiness.

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
| G46-A | `34719458597` | `DERIVED_SCOPED_EXTENDED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP8_CAP16` | Fixed bounded real-PSD caps 8/16. |
| G48-C | `34721391489` / `194db0cf...` | `CAP32_CAP64_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED` | Response-blind finite cap32/cap64 calibration only. |
| G48-A | `34724106251` / `235e807f...` | `DERIVED_SCOPED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP32_CAP64` | Finite caps 32/64 only; not unbounded PSD. |
| G49-C | `34726705385` / `db61900e...` | `CAPFREE_DIRECT_PSD_OPTIMIZER_CALIBRATED` | Response-blind cap-free/direct-PSD numerical calibration only. |
| G49-A | not launched | **AUTHORIZED NEXT / preregistration required** | RCG-002 four-shard direct-PSD transport only. |

## G49-C terminal authority

Run `34726705385`, head `db61900e4113cf002f3d5c7b636b7e14d41e00c0`, aggregate job `103642168161`, summary artifact `10307129893`, digest `sha256:ec1328e7dfa0de16be7e9d57549c81badff48c16193f9b957d566d996b80657b`.

All `12/12` response-blind lanes are structurally valid and satisfy the frozen support rule, including exact requested rank, trajectory gap `<0.002`, relative Kossakowski error `<0.02`, PSD/TP/CP/state/trace admissibility, and numerical-box inactivity. Sobol/LHS both pass for each requested rank 1..6. Cross-method best-gap differences range from `6.106226635438361e-16` to `9.084579650917406e-13`, far inside the frozen `0.002` tolerance. Classification: `CAPFREE_DIRECT_PSD_OPTIMIZER_CALIBRATED`.

This is optimizer calibration only. It does not establish a mathematical optimum over the unbounded PSD cone. It authorizes only a separately preregistered RCG-002 transport. Readiness remains 63%. Durable note: `results/ITER041_G49C_CAPFREE_PSD_CALIBRATION_TERMINAL.md`.

## G48-A terminal authority

Run `34724106251`, head `235e807fbb9f5bf00de42e66a5aa07df90a21116`, aggregate job `103636108319`, summary artifact `10307232484`, digest `sha256:4e58ab8c40a07546e47ea48eec5ffec8ec265e7216869c94702eda0eb50cd5b8`.

All `16/16` lanes are structurally valid. All eight method pairs pass the frozen nonzero-gap rule; cross-method differences are `1.64e-08` to `3.70e-07`, well inside `0.002`. All cap32-vs-terminal-cap16 and cap64-vs-cap32 nesting checks pass. Best finite-cap gaps remain nonzero for all four shards. Classification: `DERIVED_SCOPED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP32_CAP64`.

This is finite-cap evidence only. It does not establish an unbounded-PSD limit and is not an all-classical or all-semiclassical no-go theorem. Readiness remains 63%. Durable note: `results/ITER040_G48A_CAP32_CAP64_ADVERSARIAL_TERMINAL.md`.

## Active frontier — authorized G49-A

Terminal G49-C has authorized a separately prospectively frozen cap-free/direct-PSD adversarial transport against the unchanged RCG-002 four-shard toy target. Before implementation the new gate must freeze the direct `C=A^2` family, numerical box inactivity, optimizer settings, target convention, probes/times, cross-method agreement, nonzero-gap rule, and consistency/nesting against terminal cap64 evidence. No target-dependent retuning is permitted.

Even a future G49-A PASS remains scoped numerical evidence on the frozen RCG-002 panel and cannot by itself become a mathematical unbounded-PSD theorem or universal classical/semiclassical no-go.

## Open scientific layers

- prospectively freeze and execute direct-PSD RCG-002 transport;
- broader hidden-classical memory beyond the frozen stationary 3-state/12D family;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and an actual gravity-theory constitution gate.

## Claim locks

Never promote finite/bounded-family or numerical direct-PSD gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen thresholds/families/witnesses post hoc. Invalid/nonrobust historical gates remain invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions. `THEORY_ESTABLISHED` remains 0%.
