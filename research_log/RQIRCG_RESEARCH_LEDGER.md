# RQIR-CG research ledger

This is the clean scientific authority ledger for `RQIR-Candidate-Gravity`. Legacy mixed-project ledgers are not scientific authority.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, funnel/gate discipline and general mathematical tools, but not imported physical assumptions, ansatz coefficients, results or desired conclusions. Green CI is never automatically scientific PASS.

## Canonical readiness

- Internal programme readiness: **60%**.
- Theory established: **0%**.
- `58% -> 59%`: terminal closure of corrected G37-A3.
- `59% -> 60%`: terminal closure of G41-A finite high-rank positive-rate comparator layer.
- Calibration, implementation, identifiability and diagnostic gates do not themselves raise readiness.

## Authoritative recent gate ledger

| Iteration | Gate | Run / head | Classification | Scope ceiling |
|---|---|---|---|---|
| Iter017 | G35 | `34697766107` / `fbc71768...` | `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT` | Finite additive independent MF. |
| Iter017R | G35-R | `34702384573` / `1b93cbf1...` | `HELDOUT_OPTIMIZER_ROBUSTNESS_PASS_K2_K3_K4` | Method robustness only. |
| Iter018A-C | G36-P/C/A | `34702575861`, `34703606707`, `34703779268` | shared-noise implementation/calibration/scoped support | One shared Gaussian classical mode. |
| Iter019C-F | G37-C2/A3 | `34704249235`, `34708041385` | calibrated corrected nested family + `DERIVED_SCOPED_TRULY_NESTED_MF_PLUS_SHARED_BOUNDARY_PRESERVING_COMPARATOR_SUPPORT` | Finite K2-MF + one shared Markovian mode. |
| Iter020A-C | G38-P/C/A | `34704060723`, `34704210632`, `34704373278` | OU implementation/calibration/scoped support | Three-time OU toy trajectory. |
| Iter021A-E | G39-P/C/A2 | `34704548004`, `34704727102`, `34707920572` | rank2/rank3 implementation/calibration/scoped support | Finite rank3 multimode shared white noise. |
| Iter022A-E | G40-P/C2/C3 | `34708162180`, `34708550582`, `34708885346` | RTN implementation + corrected fixed-witness calibration | Calibration only. |
| Iter022F | G40-A | `34708971194` / `dab64180...` | `G40A_FROZEN_SUPPORT_RULE_NOT_MET` | Fixed-witness finite RTN subset. |
| Iter023A | G40-D | `34709706322` / `89dc08a4...` | `FIXED_WITNESS_FRAGILE_ON_PANEL` | Diagnostic only. |
| Iter023B | G40-RC-C | `34710049387` / `1f79d9c7...` | `AXIS_FRAME_COVARIANT_RTN_SEARCH_CALIBRATED` | Family-axis-covariant calibration only. |
| Iter023C | G40-RC-A | `34710216045` / `3e31a9fa...` | `G40RCA_FROZEN_SUPPORT_RULE_NOT_MET` | Axis-frame finite RTN; shard3 agreement failed. |
| Iter023D | G40-RC-D2 | `34710444349` / `ccf4274e...` | `PERSISTENT_OPTIMIZER_OR_OBJECTIVE_GEOMETRY_NONROBUSTNESS` | Diagnostic only; no repaired physics gate. |
| Iter024A | G41-P | `34710097236` / `e6c74225...` | `HIGH_RANK_CLASSICAL_KOSSAKOWSKI_IMPLEMENTATION_VALIDATED` | Rank4/5/6 implementation/provenance. |
| Iter024B | G41-C | `34710257380` / `2bac531b...` | `HIGH_RANK_RATE_OPTIMIZER_CALIBRATED` | Positive-rate search on frozen frames only. |
| Iter024C | G41-A | `34710491309` / `766ea138...` | `DERIVED_SCOPED_HIGH_RANK_RATE_COMPARATOR_SUPPORT` | Frame-indexed rank4/5/6 positive-rate families only. |
| Iter025A | G42-J | `34710643103` / `ec3d1a5e...` | `FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE` | Full 21-param real-PSD identifiability only. |
| Iter025B | G42-C | `34710744967` / `7ebc18df...` | `QUEUED / RUNNING` | Full 21-param real-PSD positive-control optimizer calibration. |

## Decisive new terminal results

### G40-RC-A and G40-RC-D2

G40-RC-A run `34710216045` was structurally valid but failed the frozen all-shards support rule solely on shard 3: Sobol/LHS gap difference `0.0022523906566203067 > 0.002`. G40-RC-D2 run `34710444349` then used four independent 64-start deep searches on the unchanged shard-3 family/witness/target. Best gaps were `0.7495354861`, `0.7450136685`, `0.7450127676`, `0.7450127451`; spread `0.0045227410 > 0.002`. Classification: `PERSISTENT_OPTIMIZER_OR_OBJECTIVE_GEOMETRY_NONROBUSTNESS`. The RTN branch has no adversarial physics PASS and no repaired gate is authorized without a separately calibrated trace-metric-aligned optimizer.

Durable notes: `results/ITER023C_G40RCA_TERMINAL.md`, `results/ITER023D_G40RCD2_TERMINAL.md`.

### G41-C / G41-A

G41-C run `34710257380`, aggregate `103597956597`, artifact `10302238984`, digest `sha256:567a1994b5892050379509066bf5075f1190831658638a77eaa26d36ef62ee82`: all 24 positive-control rank4/5/6 × shard × Sobol/LHS lanes passed with worst recovery around `1.6e-16`.

G41-A run `34710491309`, aggregate `103598462910`, artifact `10303600848`, digest `sha256:fe89d973dc1f24fe50fba09542e1b1b8e1d1fbae5e9cb1f33165b7213764dea7`: all 12 rank×shard cells passed nonzero-gap and cross-method agreement. Gaps ranged `~0.08004` to `~0.90799`; maximum Sobol/LHS difference was only `~5.2e-9`. Classification: `DERIVED_SCOPED_HIGH_RANK_RATE_COMPARATOR_SUPPORT`.

Scope remains finite frame-indexed positive-rate classical random-Hamiltonian families; arbitrary orientations/general PSD are not yet tested. Durable notes: `results/ITER024B_G41C_TERMINAL.md`, `results/ITER024C_G41A_TERMINAL.md`.

### G42-J full-PSD identifiability

Run `34710643103`, aggregate `103598755854`, artifact `10303316491`, digest `sha256:07a895f0fb309a6e642cd6eb5429e368ddcad0c78367571cfa59b7c7bce8ea9e`.

All four 21-parameter hidden controls passed: Jacobian rank `21/21` at both finite-difference steps, worst condition number `5.905925058`, maximum relative two-step difference `1.262474e-9`, and CPTP diagnostics clean. Classification: `FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE`. This authorizes only G42-C positive-control optimization calibration. Durable note: `results/ITER025A_G42J_TERMINAL.md`.

## Active frontier

**G42-C**, run `34710744967`, launch/head `7ebc18df416b62784e85ce6090ba6e8836619d92`.

Eight positive-control lanes: full real-PSD 6x6 classical Kossakowski family in 21 Cholesky coordinates, Sobol/LHS × four hidden controls, 32 starts, top-6 refinements, frozen four-time/six-product-probe observable design, max trace-distance recovery threshold `<0.002`. Exact hidden coordinates are not inserted as starts. No RCG-002 target.

Only terminal G42-C PASS may authorize a separately preregistered G42-A arbitrary-orientation/full-PSD adversarial gate using the identical family/search rules.

## Stable readiness rubric

Closed: independent scope discipline; coherent RCG-002 toy seed; finite MF K2/K3/K4; one-mode shared Gaussian noise; corrected nested MF+shared finite comparator; OU finite-correlation toy comparator; rank3 multimode shared white noise; high-rank rank4/5/6 frame-indexed positive-rate comparator; full 21-param real-PSD local identifiability.

Not closed: full-PSD optimizer calibration and adversarial comparator; robust RTN trace-metric-aligned optimization; externally anchored observables/holdouts; continuum/full candidate-gravity dynamics; any constitution gate for an actual gravity theory.

## Claim locks

Never promote finite-family gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen thresholds/families/witnesses post hoc. Invalid or nonrobust G30/G31/G37/G39/G40 results stay invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions.
