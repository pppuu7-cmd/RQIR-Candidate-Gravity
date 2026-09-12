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
- Calibration, implementation, identifiability, provenance and coordinate-coverage gates do not themselves raise readiness.

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
| G42-BC | `34712857575` | `BOUNDED_CHART_ROTATION_COVERAGE_LIMIT_FOUND` | 14/24 rotated controls in chart; 10/24 outside. |
| G43-A | `34715739668` | `HELDOUT_MULTICHART_BASIS_COVERAGE_PARTIAL_LIMIT` | Fixed five-chart atlas: 25/36 covered. |
| G44-P | `34716135086` | `BASIS_INVARIANT_TRACE_BALL_PSD_REPRESENTATION_VALIDATED` | Basis-invariant bounded real-PSD trace-ball `tr(C)<=4`; representation only. |
| G40-TM-C | `34716161178` | `TRACE_METRIC_ALIGNED_RTN_OPTIMIZER_CALIBRATED` | Prospective direct-trace RTN optimizer calibration only. |
| G44-C | `34716808171` | `BASIS_INVARIANT_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED` | Calibration only; 12/12 response-blind positive controls. |
| G40-TM-A | `34716863840` | `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET` | All 4 Sobol/LHS pairs failed frozen agreement; no robust RTN physics support. |
| G44-A | `34718045811` / `fbb93050...` | **RUNNING** | Prospective basis-invariant `tr(C)<=4` RCG-002 toy comparator attack. |
| G45-P | `34718225194` / `35583bca...` | **RUNNING/QUEUED** | Response-blind complex-PSD provenance boundary only. |

## Recent decisive terminal provenance

### G44-C basis-invariant trace-ball calibration

Run `34716808171`, aggregate `103616615329`, artifact `10304911987`, digest `sha256:7e34d6843135c670230839027cffb3d65f5a6d0fb70b8ed8b82f880ef0daf7db`.

All 12 positive-control lanes ranks1–6 × Sobol/LHS passed the prospectively frozen recovery, PSD, rank and trace-ball rules. The exact radial-boundary rank6 control passed both methods at machine precision; LHS gap `3.4694469519536137e-16`, relative Kossakowski error `1.18731827336088e-15`, recovered rank6 and trace 4.0. Classification `BASIS_INVARIANT_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED`. Durable note `results/ITER030_G44C_TRACE_BALL_CALIBRATION_TERMINAL.md`. Calibration does not change readiness.

### G40-TM-A prospective RTN negative robustness result

Run `34716863840`, aggregate `103616629784`, artifact `10305770549`, digest `sha256:7ece1af4ca748acc2a0597b1c5f900e58e805de2cfdf2d01a7f2cc6fed1d3a4b`.

All eight lanes were structural/admissible and individually produced large nonzero gaps, but every frozen Sobol/LHS pair violated agreement `<=0.002`: shard differences `0.020034961192257117`, `0.023129242052469023`, `0.005173988648269678`, `0.007421347945446466`. Classification `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET`. This is a method-robustness nonclosure for the finite frozen RTN experiment, not a universal RTN physical no-go. No post-hoc rescue is authorized. Durable note `results/ITER031_G40TMA_TRACE_METRIC_RTN_ADVERSARIAL_TERMINAL.md`. Readiness stays 61%.

### Earlier basis-coverage chain

G42-A run `34712491707` terminal scoped bounded-chart support produced readiness `60% -> 61%`. G42-BC then proved the chart coverage ceiling (14/24 in-chart), G43-A showed a frozen five-chart atlas still covered only 25/36 held-out rotations, and G44-P replaced coordinate-chart coverage with the basis-invariant real-PSD trace-ball `tr(C)<=4`. Those methodological limits remain immutable and are not failures of the underlying PSD mathematical family.

## Active frontier

### G44-A — run `34718045811`

Prospectively frozen before G44-C terminal. Launch was authorized only after consuming G44-C PASS; launch commit `fbb9305039bc44086e100ba23fe4c90e2a13cd97`.

8 lanes = Sobol/LHS × 4 frozen RCG-002 toy target shards. Per-shard PASS requires both lanes admissible and supporting, each gap `>1e-4`, and Sobol/LHS gap agreement `<=0.002`; all four shards required. Scope ceiling: bounded basis-invariant real-PSD Markovian Kossakowski trace-ball `tr(C)<=4` only. At latest durable sync: one lane in progress, seven queued, zero terminal.

A terminal PASS may justify readiness 61→62 after rubric review. A rule failure leaves readiness 61.

### G45-P — run `34718225194`

Independent response-blind provenance stream; no RCG-002 target.

Preregistration was frozen before implementation: final prereg commit `fae8063aba169ad77f4928e4a8febaf4a2839d45`; implementation `83856b814b46b9af85b298dd48a57f860549cd37`; workflow `ac0f8147ffa90f645ea9d45b14679da991464eeb`; launch `35583bcaa013944017a18c56f8f05714b616ee81`.

12 lanes compare explicit real-PSD random-Hamiltonian controls with same-site and cross-site complex-Hermitian PSD GKSL controls. The frozen obstruction diagnostic projects the entire complex generator against the full linear span of 21 real-symmetric Kossakowski dissipators plus six local-Hamiltonian commutators. This gate asks whether broadening to complex PSD silently leaves honest classical random-Hamiltonian provenance. PASS is provenance-only and cannot increase readiness.

## Open scientific layers

- terminal G44-A basis-invariant bounded-real-PSD comparator attack;
- clean characterization of the complex-PSD provenance boundary from G45-P before any decision whether a broader comparator is scientifically admissible;
- new genuinely independent non-Markovian classical families, not post-hoc RTN rescue;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and an actual gravity-theory constitution gate.

## Claim locks

Never promote finite/bounded-family gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen thresholds/families/witnesses/charts post hoc. Invalid/nonrobust historical gates remain invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions. `THEORY_ESTABLISHED` remains 0%.
