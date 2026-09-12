# RQIR-CG research ledger

This is the clean scientific authority ledger for `RQIR-Candidate-Gravity`. Legacy mixed-project ledgers are not scientific authority.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, funnel/gate discipline and general mathematical tools, but not imported physical assumptions, ansatz coefficients, results or desired conclusions. Green CI is never automatically scientific PASS.

## Canonical readiness

- Internal programme readiness: **61%**.
- Theory established: **0%**.
- `58% -> 59%`: terminal closure of corrected G37-A3.
- `59% -> 60%`: terminal closure of G41-A finite high-rank positive-rate comparator layer.
- `60% -> 61%`: terminal closure of G42-A scoped bounded boundary-PSD adversarial comparator.
- Calibration, implementation, identifiability and diagnostic/chart-coverage gates do not themselves raise readiness.

## Authoritative recent gate ledger

| Iteration | Gate | Run / head | Classification | Scope ceiling |
|---|---|---|---|---|
| Iter017 | G35 | `34697766107` / `fbc71768...` | `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT` | Finite additive independent MF. |
| Iter017R | G35-R | `34702384573` / `1b93cbf1...` | `HELDOUT_OPTIMIZER_ROBUSTNESS_PASS_K2_K3_K4` | Method robustness only. |
| Iter018A-C | G36-P/C/A | `34702575861`, `34703606707`, `34703779268` | shared-noise implementation/calibration/scoped support | One shared Gaussian classical mode. |
| Iter019C-F | G37-C2/A3 | `34704249235`, `34708041385` | calibrated corrected nested family + `DERIVED_SCOPED_TRULY_NESTED_MF_PLUS_SHARED_BOUNDARY_PRESERVING_COMPARATOR_SUPPORT` | Finite K2-MF + one shared Markovian mode. |
| Iter020A-C | G38-P/C/A | `34704060723`, `34704210632`, `34704373278` | OU implementation/calibration/scoped support | Three-time OU toy trajectory. |
| Iter021A-E | G39-P/C/A2 | `34704548004`, `34704727102`, `34707920572` | rank2/rank3 implementation/calibration/scoped support | Finite rank3 multimode shared white noise. |
| Iter022A-F | G40-P/C/A | `34708162180`, `34708550582`, `34708971194` | RTN implementation/calibration; adversarial frozen support rule not met | Fixed-witness finite RTN. |
| Iter023A-D | G40-D/RC-C/RC-A/RC-D2 | `34709706322`, `34710049387`, `34710216045`, `34710444349` | fixed-witness fragility; axis-frame calibration; adversarial rule not met; persistent optimizer nonrobustness | No RTN physics PASS. |
| Iter024A-C | G41-P/C/A | `34710097236`, `34710257380`, `34710491309` | implementation + calibrated finite high-rank + `DERIVED_SCOPED_HIGH_RANK_RATE_COMPARATOR_SUPPORT` | Frame-indexed rank4/5/6 positive-rate families only. |
| Iter025A | G42-J | `34710643103` / `ec3d1a5e...` | `FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE` | Full 21-param real-PSD local identifiability only. |
| Iter025B | G42-C | `34710744967` / `7ebc18df...` | `FULL_PSD_OPTIMIZER_CALIBRATED` with scope correction | Strictly SPD-interior chart only; boundary excluded. |
| Iter025C | G42-C2 | `34710953936` / `858ad4b6...` | `PSD_BOUNDARY_OPTIMIZER_CALIBRATED` | Bounded PSD chart, ranks 2/4/5/6 controls. |
| Iter025D | G42-C3 | `34711048394` / `35f719fd...` | `PSD_BOUNDARY_RANK_COMPLETION_CALIBRATED` | Same bounded PSD chart, ranks 1/3 controls. |
| Iter026 | G42-A | `34712491707` / `f7f48725...` | `DERIVED_SCOPED_BOUNDARY_PSD_COMPARATOR_SUPPORT` | Bounded 21-coordinate real-PSD Markovian family only. |
| Iter026R | G42-R | `34712524241` / `3b53451c...` | `PSD_BOUNDARY_HELDOUT_CALIBRATION_REPLICATED` | Method robustness only. |
| Iter026B | G42-BC | `34712857575` / `11b5a060...` | `BOUNDED_CHART_ROTATION_COVERAGE_LIMIT_FOUND` | Single-chart basis coverage is not invariant. |
| Iter027 | G43-A | `34715739668` / `b69524b9...` | **RUNNING; PARTIAL COVERAGE LIMIT ALREADY OBSERVED** | Response-blind finite five-chart atlas only. |
| Iter028 | G44-P | `34716135086` / `daf40fca...` | **RUNNING** | Response-blind basis-invariant PSD trace-ball representation/covariance pre-gate. |
| Iter029 | G40-TM-C | `34716161178` / `aff54cae...` | **QUEUED/RUNNING** | Response-blind trace-metric-aligned RTN optimizer calibration only. |

## Decisive terminal results

### G40 RTN branch — unresolved optimizer blocker

G40-RC-A run `34710216045` failed the frozen all-shards support rule on shard 3: Sobol/LHS gap difference `0.0022523906566203067 > 0.002`. G40-RC-D2 run `34710444349` then used four independent 64-start searches on the unchanged shard-3 family/witness/target; best gaps were `0.7495354861`, `0.7450136685`, `0.7450127676`, `0.7450127451`, spread `0.0045227410 > 0.002`. Classification `PERSISTENT_OPTIMIZER_OR_OBJECTIVE_GEOMETRY_NONROBUSTNESS`. No RTN adversarial physics PASS exists. This terminal result remains authoritative and cannot be retroactively rescued.

### G41-A high-rank finite comparator

G41-A run `34710491309`, aggregate `103598462910`, artifact `10303600848`, digest `sha256:fe89d973dc1f24fe50fba09542e1b1b8e1d1fbae5e9cb1f33165b7213764dea7`: all 12 rank×shard cells passed frozen nonzero-gap and cross-method agreement. Classification `DERIVED_SCOPED_HIGH_RANK_RATE_COMPARATOR_SUPPORT`. This finite frame-indexed closure produced readiness `59% -> 60%`.

### G42-J identifiability

Run `34710643103`, aggregate `103598755854`, artifact `10303316491`, digest `sha256:07a895f0fb309a6e642cd6eb5429e368ddcad0c78367571cfa59b7c7bce8ea9e`: all four controls had Jacobian rank `21/21`, worst condition `5.905925058`, maximum two-step relative mismatch `1.262474e-9`, CPTP clean. Classification `FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE`.

### G42-C/C2/C3/R bounded-chart calibration

G42-C established only SPD-interior calibration because its log-Cholesky diagonal excluded the PSD boundary. G42-C2 run `34710953936`, artifact `10303587123`, and G42-C3 run `34711048394`, artifact `10303627020`, then prospectively calibrated the boundary-capable bounded Cholesky optimizer across effective ranks 1–6. G42-R run `34712524241`, aggregate `103604804647`, artifact `10303143301`, digest `sha256:81fa588873316be4c243657cf7e2ac2f0aa08f092de05c969188c39d70c20f10`, replicated on 12/12 held-out controls. This is calibration authority only, not an unbounded full-PSD theorem.

### G42-A bounded boundary-PSD adversarial closure

Run `34712491707`, head `f7f48725a3d57398426f8ac9341a1d11b9cc591f`, aggregate `103605124717`, artifact `10304400253`, digest `sha256:002bea19226bd9b7283a08b36db3e72715762e074f10c40b7114d1e35ac3903c`.

All 8 lanes were valid/admissible. Frozen all-shard support rule passed. Per-shard Sobol/LHS gaps and method differences:

- shard 0: `0.03700325124270668 / 0.03701733499594546`, diff `1.4083753238774976e-05`;
- shard 1: `0.1463716306513109 / 0.14637041941069723`, diff `1.2112406136688403e-06`;
- shard 2: `0.5276672796201998 / 0.5276813340757002`, diff `1.4054455500400742e-05`;
- shard 3: `0.8197294896504166 / 0.819101112669069`, diff `0.0006283769813475448`.

Classification `DERIVED_SCOPED_BOUNDARY_PSD_COMPARATOR_SUPPORT`. Scope ceiling is exactly the frozen bounded 21-coordinate real-PSD 6x6 Markovian classical random-Hamiltonian Kossakowski family. Readiness `60% -> 61%` for closing this scoped adversarial rubric item only.

### G42-BC basis/chart audit

Run `34712857575`, head `11b5a0604ada235a4504990966b89f8f89857471`, aggregate `103606238137`, artifact `10304851327`, digest `sha256:e171c028ed31cd28fd19b1a1f1fd3a1dd91d9aa93a6be641bbfe580ad5b47e4c`.

All 24/24 local-basis generator-covariance checks passed with maximum errors around `4.8e-16`, but only 14/24 rotated controls remained inside the single frozen Cholesky coordinate box; 10/24 exited. Classification `BOUNDED_CHART_ROTATION_COVERAGE_LIMIT_FOUND`. This does not retroactively change G42-A but forbids basis-invariant interpretation of that bounded-chart result for the entire mathematical real-PSD family.

Durable package: `results/ITER026_G42A_G42R_G42BC_TERMINAL.md`.

## Active frontier

### Iter027 / G43-A — held-out finite-atlas coverage

Protocol `protocol/ITER027_G43A_HELDOUT_MULTICHART_BASIS_COVERAGE.md`; launch/head `b69524b9fe8c33ff2f433f1d9dbc6ce54f8e4a06`; run `34715739668`.

36 response-blind lanes = six new hidden PSD controls ranks 1–6 × six held-out local basis rotations. Frozen atlas has five charts. Frozen terminal classifier: all covered -> `HELDOUT_MULTICHART_BASIS_COVERAGE_PASS`; clean validity/covariance with one or more uncovered -> `HELDOUT_MULTICHART_BASIS_COVERAGE_PARTIAL_LIMIT`; structural/covariance failure -> `MULTICHART_IMPLEMENTATION_OR_VALIDITY_FAIL`.

A response-blind uncovered lane has already appeared: rank-5/panel-3 is structurally valid, rank-preserving and basis-covariant with generator error `2.892896804343598e-16`, but none of the five frozen charts covers it. Best violation score is `0.023092545915790297`. Therefore full atlas PASS is already impossible; the gate remains live only to determine whether terminal result is the clean partial-coverage class or an implementation/validity failure. No chart/bound may be added post hoc.

### Iter028 / G44-P — basis-invariant PSD trace-ball representation

Prereg `protocol/ITER028_G44P_BASIS_INVARIANT_TRACE_BALL_PSD.md`, commit `dceaba1889fa190b915c22f8ad57c63f81591207`; implementation `a70f579a61639af6a8426e7c8bf3f01950aab463`; launch/head `daf40fca9e5e6dc6f98b7673d5c2d34a4cc75552`; run `34716135086`.

Frozen family `C=A^2`, `A=A^T`, `||A||_F<=2`, equivalently real PSD `tr(C)<=4`. This family is orthogonally basis-invariant and analytically contains the entire old G42 Cholesky box because its maximum squared Frobenius norm is `3.51 < 4`.

24 response-blind lanes = ranks 1–6 × four new local rotations. Frozen conditions: rank preserved, PSD floor, symmetric-square-root reconstruction `<1e-10`, trace-ball membership before/after rotation, generator covariance `<1e-10`, old-box nesting true. No RCG-002 target/result is used. At this ledger update 2/24 lanes are terminal and both support; this is non-terminal evidence only. PASS authorizes only a separately preregistered optimizer calibration in exactly the same trace-ball family.

### Iter029 / G40-TM-C — trace-metric-aligned RTN optimizer calibration

Prereg `protocol/ITER029_G40TMC_TRACE_METRIC_CALIBRATION.md`, commit `466b649cf1929fefb3cbc28305115fb9afcb9934`; implementation `423cc1c5bec5019c29a4d539273b16de31662d61`; launch/head `aff54cae0954eb06771337ab315672a049450923`; run `34716161178`.

Eight response-blind positive-control lanes = `sobol_powell`/`lhs_powell` × four controls. Search directly minimizes the scientific maximum trace-distance trajectory gap using 24 QMC starts and bounded Powell refinement of the best four. Strict recovered axis-covariant BLP must exceed `0.02`; trace gap must be `<0.002`. No hidden coordinate is inserted as a start, and no RCG-002 target/result is used.

This is a new method-calibration gate only. It preserves the old G40 nonrobustness verdict. PASS may authorize a separately preregistered prospective RTN adversarial gate but cannot itself raise readiness.

## Stable readiness rubric

Closed: independent scope discipline; coherent RCG-002 toy seed; finite MF K2/K3/K4; shared Gaussian finite layers; corrected nested MF+shared comparator; OU finite-correlation toy comparator; finite rank2/rank3 multimode shared noise; finite rank4/5/6 frame-indexed positive-rate comparator; full 21-param local identifiability; bounded PSD optimizer calibration across effective ranks 1–6; scoped bounded boundary-PSD adversarial comparator.

Not closed: basis-invariant/bound robustness before stronger PSD-family interpretation; robust RTN trace-metric-aligned optimization; broader non-Markovian/classically correlated comparators; externally anchored observables/holdouts; continuum/full candidate-gravity dynamics; any constitution gate for an actual gravity theory.

## Claim locks

Never promote finite/bounded-family gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen thresholds/families/witnesses/charts post hoc. Invalid or nonrobust historical gates remain invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions.
