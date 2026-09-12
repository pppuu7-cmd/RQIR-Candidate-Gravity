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
- Calibration, implementation, identifiability, provenance and coordinate-coverage gates do not themselves raise readiness. Overlapping comparator enlargements must not be double-counted.

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
| G44-A | `34718045811` / `fbb93050...` | `DERIVED_SCOPED_BASIS_INVARIANT_TRACE_BALL_PSD_COMPARATOR_SUPPORT` | Bounded real-PSD Markovian `tr(C)<=4`. |
| G45-P | `34718225194` / `35583bca...` | `COMPLEX_PSD_EXTENDS_BEYOND_CLASSICAL_RANDOM_HAMILTONIAN_PROVENANCE_ON_FROZEN_CONTROLS` | Provenance boundary only. |
| G47-P | `34719123666` / `f3f4f178...` | `THREE_STATE_CLASSICAL_SWITCHING_PRODUCT_UNITARY_PROVENANCE_VALIDATED` | Explicit finite hidden-classical memory provenance. |
| G46-C | `34719083985` / `9c1f78dd...` | `EXTENDED_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED_CAP8_CAP16` | Response-blind calibration cap8/cap16. |
| G47-C | `34719251400` / `2623e3e8...` | `THREE_STATE_CLASSICAL_SWITCHING_OPTIMIZER_CALIBRATED` | Response-blind calibration of frozen 12D family. |
| G47-A | `34719377641` / `48985239...` | `DERIVED_SCOPED_THREE_STATE_CLASSICAL_SWITCHING_COMPARATOR_SUPPORT` | Frozen bounded 12D stationary 3-state CTMC family only. |
| G46-A | `34719458597` / `a2dd7fd3...` | **RUNNING/QUEUED: 0/16 terminal at latest sync** | Fixed bounded real-PSD caps 8/16; pair + nesting rules frozen. |

## Recent decisive provenance

### G47-A finite hidden-classical memory comparator closure

Run `34719377641`, aggregate `103622436777`, artifact `10305072882`, digest `sha256:f75f0a590cae9978b5abe2e56386f237d4e05323c94c4e4321cbb22ab1ef99dd`.

All four prospectively frozen Sobol/LHS pairs pass: s0 `0.6385600880482375/0.6385600884311459`; s1 `0.6784960973078257/0.6784961451118307`; s2 `0.8235518631773218/0.8235518632703851`; s3 `0.7695388395862157/0.7695390013607699`. Worst disagreement `1.6177455419708053e-07 << 0.002`. Classification `DERIVED_SCOPED_THREE_STATE_CLASSICAL_SWITCHING_COMPARATOR_SUPPORT`. Durable note `results/ITER037_G47A_THREE_STATE_SWITCHING_ADVERSARIAL_TERMINAL.md`. This moves readiness 62→63.

### G47-C optimizer calibration

Run `34719251400`, aggregate `103622040491`, artifact `10305347477`, digest `sha256:8d5f005501a97c2623da1e83d823732ec44210187bd3f84243873595bfdf09bf`. 8/8 positive controls pass; worst train gap `5.4275615639463476e-11`, held-out `3.599259601883243e-11`, normalized parameter error `7.652303300674281e-10`, provenance 8/8. Classification `THREE_STATE_CLASSICAL_SWITCHING_OPTIMIZER_CALIBRATED`. Durable note `results/ITER036_G47C_THREE_STATE_SWITCHING_CALIBRATION_TERMINAL.md`.

### G46-C extended trace-ball calibration

Run `34719083985`, aggregate `103622183765`, artifact `10305154162`, digest `sha256:7d6193093c2dc423a479e747707c80af1975f4d87bfd646207d426830ecad0c6`. 24/24 response-blind lanes pass. Cap8 worst gap `1.0900999144735261e-11`, worst relative C error `3.479885009977411e-11`; cap16 worst gap `2.393957298667677e-11`, worst relative C error `9.32022808014185e-11`; rank match 12/12 each. Classification `EXTENDED_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED_CAP8_CAP16`. Durable note `results/ITER034_G46C_EXTENDED_TRACE_BALL_CALIBRATION_TERMINAL.md`.

### G44-A / G45-P / G40-TM-A retained

G44-A run `34718045811` closed bounded basis-invariant real-PSD cap4 support and moved readiness 61→62. G45-P run `34718225194` established that generic complex-PSD GKSL leaves honest classical random-Hamiltonian provenance on frozen controls. G40-TM-A run `34716863840` remains a preserved method-robustness nonclosure, not a universal RTN no-go.

## Active frontier — G46-A

Run `34719458597`, launch/head `a2dd7fd3cf3b40f642077c62bd1c0020a97d12bb`.

16 prospective lanes = real-PSD caps 8/16 × Sobol/LHS × four unchanged G44-A RCG-002 target shards. Frozen requirements: every lane admissible and gap `>1e-4`; every method pair agrees `<=0.002`; for every shard `best(cap16) <= best(cap8)+0.002` because cap16 contains cap8. Latest sync: 0/16 terminal, 16 queued. Terminal PASS deepens bounded Markovian PSD coverage but does not automatically create another readiness increment because G44-A already occupies that rubric dimension.

## Open scientific layers

- terminal G46-A extended bounded real-PSD attack;
- broader hidden-classical memory beyond the frozen stationary 3-state/12D family;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and an actual gravity-theory constitution gate.

## Claim locks

Never promote finite/bounded-family gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen thresholds/families/witnesses post hoc. Invalid/nonrobust historical gates remain invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions. `THEORY_ESTABLISHED` remains 0%.
