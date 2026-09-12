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
- G46-A, G48-C and G48-A deepen/calibrate the already-counted Markovian PSD rubric and do not add readiness points. Calibration, implementation, identifiability, provenance and coordinate-coverage gates do not themselves raise readiness.

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
| G49-C | `34726705385` / `db61900e...` | **ACTIVE / unclassified** | Response-blind cap-free/direct-PSD numerical calibration only. |

## G48-A terminal authority

Run `34724106251`, head `235e807fbb9f5bf00de42e66a5aa07df90a21116`, aggregate job `103636108319`, summary artifact `10307232484`, digest `sha256:4e58ab8c40a07546e47ea48eec5ffec8ec265e7216869c94702eda0eb50cd5b8`.

All `16/16` lanes are structurally valid. All eight method pairs pass the frozen nonzero-gap rule; cross-method differences are `1.64e-08` to `3.70e-07`, well inside `0.002`. All cap32-vs-terminal-cap16 and cap64-vs-cap32 nesting checks pass. Best finite-cap gaps remain nonzero for all four shards. Classification: `DERIVED_SCOPED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP32_CAP64`.

This is finite-cap evidence only. It does not establish an unbounded-PSD limit and is not an all-classical or all-semiclassical no-go theorem. Readiness remains 63%. Durable note: `results/ITER040_G48A_CAP32_CAP64_ADVERSARIAL_TERMINAL.md`.

## Active frontier — G49-C

G49-C was prospectively frozen only after terminal G48-A classification. Preregistration `2d472c4223602f77e13b054615e713c58f0b46c3`; implementation `05a41f62b36e0912f60c01f7aa1657130c3c66d4`; workflow `7c31d7d19f4847b12043e15ba1699740e0fd7af3`; launch/head `db61900e4113cf002f3d5c7b636b7e14d41e00c0`; run `34726705385`.

Frozen family: direct real-symmetric physical-scale `A`, `C=A^2`, no physical trace cap. The optimizer uses a numerical box `[-8,8]^21`, which must be inactive (`max |w_i| / 8 < 0.80`) for PASS. Response-blind controls use ranks 1..6 and `sqrt(tr(C))=[0.5,1,2,3,4,5]`, methods Sobol/LHS, 12 lanes. Per-lane thresholds are gap `<0.002`, relative Kossakowski error `<0.02`, exact requested effective rank, and frozen PSD/TP/CP/state/trace controls. RCG-002 is not used in this calibration.

Only terminal G49-C PASS may authorize a separately preregistered RCG-002 transport. Even that later transport cannot by itself become a mathematical unbounded-PSD theorem.

## Open scientific layers

- terminal G49-C and conditional direct-PSD RCG-002 transport;
- broader hidden-classical memory beyond the frozen stationary 3-state/12D family;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and an actual gravity-theory constitution gate.

## Claim locks

Never promote finite/bounded-family or numerical direct-PSD gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen thresholds/families/witnesses post hoc. Invalid/nonrobust historical gates remain invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions. `THEORY_ESTABLISHED` remains 0%.
