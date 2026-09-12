# RQIR-CG research ledger

This file is the clean authority ledger for `RQIR-Candidate-Gravity` only. The pre-existing `research_log/RESEARCH_ACTIVITY_LEDGER.md` contains legacy material from another research line and must not be used as scientific evidence for RQIR-CG.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, gate discipline and mathematical tools, but not imported physical assumptions, ansatz coefficients, results or desired conclusions.

## Latest authoritative results

| Iteration | Gate | Run / head | Classification | Result ceiling |
|---|---|---|---|---|
| Iter010 | G28 full-Bloch comparator audit | `34692403874` / `3d8d3f969a22c22c1526b00f42377c2d41f87a04` | `DERIVED_SCOPED_NEGATIVE_COMPARATOR_RESULT` | Finite single-axis Markovian family only. |
| Iter011 | G29 robustness suite | `34694101699` / `c4c6f0d35e4e57a2105facafee2bdddc8036a52f` | `DERIVED_SCOPED_ROBUSTNESS_SUPPORT` | Finite single-axis family. |
| Iter012 | G30 additive multichannel comparator | `34694264478` / `fa9be36b422b84614b03f96de7c37660059f2d74` | `FINITE_SEARCH_DIAGNOSTIC` | Historical gaps non-authoritative after later calibration failure. |
| Iter013 | G31 global-search calibration | `34695076098` / `f32ecf1949f1e7d6c577b201b73c517d4605fdb7` | `SCIENTIFIC_CALIBRATION_FAIL / GLOBAL_OPTIMIZER_NOT_VALIDATED` | Adversarial minima diagnostic only. |
| Iter014 | G32 optimizer diagnosis | `34695441883` / `ea54a3ae9694366c13b775af44d46833` | `POSITIVE_CONTROL_OPTIMIZER_FAIL / LOCAL_BASIN_GEOMETRY_OR_CONDITIONING` | Direct trace-distance optimizer unreliable. |
| Iter014B | G32-J Jacobian | `34695478444` / `706245fa183845556aa020bc99d2a4d86e4e3060` | `FULL_LOCAL_RANK / STRONGLY_ILL_CONDITIONED_DIAGNOSTIC` | Rank 11/11; condition number up to ~4034. |
| Iter015 | G33 smooth K2 calibration | `34695662002` / `d15d633f58fa63d378a85d6e5409c4bb0735a97e` | `POSITIVE_CONTROL_METHOD_CALIBRATED_K2` | Sobol-LSQ and LHS-LSQ calibrated. |
| Iter016 | G34 multichannel comparator | `34695835216` / `09d729764ca38a0d83f11b81dc59f157cd0cb734` | `DERIVED_SCOPED_K2_CALIBRATED_COMPARATOR_SUPPORT + POSITIVE_CONTROL_METHOD_CALIBRATED_K3_K4` | Finite additive independent measurement-feedback family. |
| Iter017 | G35 K3/K4 adversarial | `34697766107` / `fbc71768da3cec0d6ea5a8cbb755a29036b16726` | `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT` | K3/K4 four-shard + admissibility PASS; same finite family only. |
| Iter017R | G35-R held-out replication | `34702384573` / `1b93cbf14b4705ae2699f559523d1c1b1ae28be5` | `HELDOUT_OPTIMIZER_ROBUSTNESS_PASS_K2_K3_K4` | Methodology robustness only. |
| Iter018A | G36-P shared-noise implementation | `34702575861` / `270a26300117aeebe23af126dd4e6c53c96cf3f9` | `CLASSICAL_SHARED_NOISE_IMPLEMENTATION_VALIDATED` | Convex mixture of product unitaries; implementation/provenance only. |
| Iter018B | G36-C shared-noise calibration | `34703606707` / `95335aa32e92dcd1cc76762cd6fd3717754a1057` | `POSITIVE_CONTROL_METHOD_CALIBRATED_SHARED_NOISE` | 12/12 hidden in-family controls PASS; authorizes G36-A only. |
| Iter018C | G36-A shared-noise adversarial | `34703779268` / `15ba7c90fd4794d3d31e41a5a08ee35511284faf` | `DERIVED_SCOPED_SHARED_NOISE_CALIBRATED_COMPARATOR_SUPPORT` | Four RCG-002 shards × two methods PASS; shared Gaussian classical noise only. |
| Iter019A | G37-C combined comparator calibration | `34703787083` / `59cf94512a65a54a37eba05ae3093b7ee85bead0` | `RUNNING / FROZEN_PROSPECTIVE_CALIBRATION` | K2 measurement-feedback + shared Gaussian classical-noise finite family; no adversarial interpretation yet. |

## Key new terminal aggregates

### Iter017 / G35

Aggregate job `103578278887`, summary artifact `10301201162`, digest `sha256:7e07e47311db7a279e2de47502d64a36cf31623c10c0da67f062ee8817bac199`. All 24 required artifacts structurally valid. K=3 and K=4 each passed all four shards for both calibrated methods, frozen nonzero-gap and cross-method rules, nesting sanity and 4/4 admissibility. Durable note: `results/ITER017_G35_CALIBRATED_K3K4_TERMINAL.md`.

### Iter017R / G35-R

Aggregate job `103580063685`, summary artifact `10300682102`, digest `sha256:5724519f32faf1e10d011e97d10df283fa6225facdfdb9ad8b14e82577557b13`. 18/18 held-out controls passed across K=2/K=3/K=4 and Sobol/LHS. Worst trace-distance recovery `5.6435139378164e-13` versus frozen `<0.002`. Durable note: `results/ITER017R_G35R_HELDOUT_OPTIMIZER_REPLICATION_TERMINAL.md`.

### Iter018A / G36-P

Aggregate job `103576905242`, artifact `10300760790`, digest `sha256:3a03b7462ccf026c6cc7cdef88fbe0c9f4710c3040f467a5caf9fa5e3e4d228d`. 12/12 implementation/provenance checks passed for shared Gaussian Hamiltonian noise as a convex mixture of product unitaries.

### Iter018B / G36-C

Aggregate job `103579641822`, summary artifact `10301561148`, digest `sha256:5f82bf2eb2b74bf0ac2f2bbc6e5f252898da97420fa5e0da1f1fd91f6e5f5f0c`. All 12 positive controls passed; worst trace-distance recovery `5.288760714311301e-15` versus `<0.002`. Durable note: `results/ITER018B_G36C_SHARED_NOISE_CALIBRATION_TERMINAL.md`.

### Iter018C / G36-A

Aggregate job `103580126265`, summary artifact `10301491686`, digest `sha256:2a75483c5ed8261e62466581b7a00046dd5d7a81ddffc5e49e38e819f81832ce`.

All eight frozen RCG-002 adversarial lanes passed. Gap pairs (Sobol,LHS): shard0 `(0.025499008832948887,0.025499011169133425)`, shard1 `(0.10036159822213998,0.10036158741640057)`, shard2 `(0.3587370385387613,0.35873703839655824)`, shard3 `(0.5980266528346264,0.5980268730784868)`. All are `>1e-4` and each pair agrees within `0.002`. Durable note: `results/ITER018C_G36A_SHARED_NOISE_ADVERSARIAL_TERMINAL.md`.

This remains scoped to one shared Gaussian classical Hamiltonian-noise process and is not a general classical/semiclassical no-go.

## Active frontier — Iter019A / G37-C

Run `34703787083`, launch head `59cf94512a65a54a37eba05ae3093b7ee85bead0`.

Prospectively calibrate the stronger combined finite Markovian comparator: calibrated K=2 additive independent single-axis measurement-feedback GKSL plus validated shared Gaussian classical Hamiltonian noise. Six hidden in-family controls × Sobol/LHS plus four independent admissibility lanes are frozen before inspection. Every positive-control trace distance must be `<0.002`; TP/CP/PSD/trace/Hermiticity admissibility must pass all four lanes. Latest checked state: 14/16 scientific lanes terminal success, two shard-4 positive-control lanes still in progress; aggregate pending.

Only terminal G37-C scientific PASS authorizes a separate combined-family RCG-002 adversarial test. Failure blocks that interpretation; thresholds/family cannot be weakened post hoc.

## Stable readiness rubric

- independent scope/claim discipline: closed
- weak-field coherent candidate construction: closed at toy-channel level
- basis/rotation robustness and finite comparator validity: closed at tested layers
- K2/K3/K4 measurement-feedback optimizer calibration and prospective adversarial reruns: closed
- held-out optimizer replication: closed methodology support
- shared-classical-noise implementation/provenance: closed
- shared-classical-noise optimizer calibration: closed
- shared-classical-noise adversarial comparator against RCG-002: closed, scoped
- combined measurement-feedback + shared-noise calibration: active G37-C
- combined-family adversarial comparator: blocked pending G37-C PASS
- broader correlated/general positive-Kossakowski comparator: open
- non-Markovian comparator layer: open
- externally anchored observable/holdout programme: open
- full candidate-gravity dynamics / continuum completion: open

Current internal programme readiness: **56%**. This is a construction/readiness metric, not a probability of physical correctness.

## Claim locks

Do not promote finite-family gaps to claims that all semiclassical gravity, all classical mediators, or all quantum-gravity alternatives are excluded. Do not use green CI as scientific PASS. Do not weaken frozen `2e-3` calibration/agreement or `1e-4` nonzero-gap criteria after seeing results. G30/G31 adversarial minima remain diagnostics only. Do not import physical assumptions or desired conclusions from QGR/KMQGB/RQIR.
