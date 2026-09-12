# RQIR-CG research ledger

This is the clean scientific authority ledger for `RQIR-Candidate-Gravity`. Legacy mixed-project ledgers are not scientific authority for this project.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, funnel/gate discipline and general mathematical tools, but not imported physical assumptions, ansatz coefficients, results or desired conclusions.

## Authoritative result table

| Iteration | Gate | Run / head | Classification | Result ceiling |
|---|---|---|---|---|
| Iter010 | G28 | `34692403874` / `3d8d3f969a22c22c1526b00f42377c2d41f87a04` | `DERIVED_SCOPED_NEGATIVE_COMPARATOR_RESULT` | Finite single-axis Markovian family. |
| Iter011 | G29 | `34694101699` / `c4c6f0d35e4e57a2105facafee2bdddc8036a52f` | `DERIVED_SCOPED_ROBUSTNESS_SUPPORT` | Same finite family. |
| Iter012 | G30 | `34694264478` / `fa9be36b422b84614b03f96de7c37660059f2d74` | `FINITE_SEARCH_DIAGNOSTIC` | Historical minima non-authoritative after calibration failure. |
| Iter013 | G31 | `34695076098` / `f32ecf1949f1e7d6c577b201b73c517d4605fdb7` | `SCIENTIFIC_CALIBRATION_FAIL / GLOBAL_OPTIMIZER_NOT_VALIDATED` | Adversarial minima diagnostic only. |
| Iter014 | G32 | `34695441883` / `ea54a3ae9694366c13b775af44d46833` | `POSITIVE_CONTROL_OPTIMIZER_FAIL / LOCAL_BASIN_GEOMETRY_OR_CONDITIONING` | Direct trace-distance optimizer unreliable. |
| Iter014B | G32-J | `34695478444` / `706245fa183845556aa020bc99d2a4d86e4e3060` | `FULL_LOCAL_RANK / STRONGLY_ILL_CONDITIONED_DIAGNOSTIC` | Rank 11/11; strong conditioning. |
| Iter015 | G33 | `34695662002` / `d15d633f58fa63d378a85d6e5409c4bb0735a97e` | `POSITIVE_CONTROL_METHOD_CALIBRATED_K2` | Sobol/LHS smooth optimizer authority. |
| Iter016 | G34 | `34695835216` / `09d729764ca38a0d83f11b81dc59f157cd0cb734` | `DERIVED_SCOPED_K2_CALIBRATED_COMPARATOR_SUPPORT + POSITIVE_CONTROL_METHOD_CALIBRATED_K3_K4` | Finite additive independent MF family. |
| Iter017 | G35 | `34697766107` / `fbc71768da3cec0d6ea5a8cbb755a29036b16726` | `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT` | K3/K4 finite additive independent MF family. |
| Iter017R | G35-R | `34702384573` / `1b93cbf14b4705ae2699f559523d1c1b1ae28be5` | `HELDOUT_OPTIMIZER_ROBUSTNESS_PASS_K2_K3_K4` | Methodology robustness only. |
| Iter018A | G36-P | `34702575861` / `270a26300117aeebe23af126dd4e6c53c96cf3f9` | `CLASSICAL_SHARED_NOISE_IMPLEMENTATION_VALIDATED` | Single shared Gaussian classical noise. |
| Iter018B | G36-C | `34703606707` / `95335aa32e92dcd1cc76762cd6fd3717754a1057` | `POSITIVE_CONTROL_METHOD_CALIBRATED_SHARED_NOISE` | Shared-noise optimizer calibration. |
| Iter018C | G36-A | `34703779268` / `15ba7c90fd4794d3d31e41a5a08ee35511284faf` | `DERIVED_SCOPED_SHARED_NOISE_CALIBRATED_COMPARATOR_SUPPORT` | One shared Gaussian classical mode only. |
| Iter019A | G37-C old | `34703787083` / `59cf94512a65a54a37eba05ae3093b7ee85bead0` | `CALIBRATED_OWN_FAMILY / LATER_FOUND_NONNESTED` | Calibration valid for its own 18D family; not a superset of shared-only. |
| Iter019B | G37-A old | `34704008252` / `e0288f6e5dc58c43f71c790d5402bdb7bb9561c9` | `PROTOCOL_DESIGN_FAIL / NONNESTED_COMBINED_FAMILY` | Diagnostic only; not scientific FAIL of RCG-002. |
| Iter020A | G38-P | `34704060723` / `a1db86645204fd158057673e57518374e9434666` | `OU_COLORED_CLASSICAL_NOISE_IMPLEMENTATION_VALIDATED` | OU finite-correlation scalar classical noise; single-time reducible to phase variance. |
| Iter020B | G38-C | `34704210632` / `86eb78312d1cdcf58c4844e98b4065482b9fc4c8` | `POSITIVE_CONTROL_METHOD_CALIBRATED_OU_COLORED_TRAJECTORY` | Three-time OU trajectory optimizer. |
| Iter020C | G38-A | `34704373278` / `493da45d6a9b88e5cee32fca598fb657ea7a2ce4` | `DERIVED_SCOPED_OU_COLORED_TRAJECTORY_COMPARATOR_SUPPORT` | Three-time toy trajectory only; not full gravity dynamics/non-Markovian no-go. |
| Iter019C | G37-C2 | `34704249235` / `0852fe30aa6bb7542dbb5ff4ec17fe8fd6eb55c1` | `RUNNING / CORRECTED_NESTED_CALIBRATION` | Truly nested MF + shared-noise family; no adversarial authority yet. |
| Iter021A | G39-P | `34704548004` / `995f3c60b7648afe7a7d1a9b6ebb4c9e609dbf20` | `RUNNING / MULTIMODE_IMPLEMENTATION_PRE_GATE` | Rank-2/rank-3 correlated local-random-unitary classical noise; no RCG-002 authority yet. |

## Recent terminal aggregates

### G35 / G35-R

G35 aggregate job `103578278887`, artifact `10301201162`, digest `sha256:7e07e47311db7a279e2de47502d64a36cf31623c10c0da67f062ee8817bac199`: K3/K4 all four shards pass calibrated two-method, nesting and admissibility rules. G35-R aggregate job `103580063685`, artifact `10300682102`, digest `sha256:5724519f32faf1e10d011e97d10df283fa6225facdfdb9ad8b14e82577557b13`: 18/18 held-out positive controls pass.

### G36 shared classical noise

G36-C aggregate job `103579641822`, artifact `10301561148`, digest `sha256:5f82bf2eb2b74bf0ac2f2bbc6e5f252898da97420fa5e0da1f1fd91f6e5f5f0c`: 12/12 positive controls pass. G36-A aggregate job `103580126265`, artifact `10301491686`, digest `sha256:2a75483c5ed8261e62466581b7a00046dd5d7a81ddffc5e49e38e819f81832ce`: all four RCG-002 shards retain nonzero calibrated gaps under both methods.

### G37 old combined-family protocol failure

G37-A aggregate job `103581352127`, artifact `10301497283`, digest `sha256:26926f7123ad1f69f4d13d17354c5e02a48a817cf6028f4850acc03a5422c0ee`. Numerical lanes and cross-method agreement were valid, but nesting failed on shards 1 and 2. Code inspection showed the old family could not switch the K2 measurement-feedback component off, so it did not contain the shared-only parent. Classification is `PROTOCOL_DESIGN_FAIL / NONNESTED_COMBINED_FAMILY`, not physical FAIL. Durable note: `results/ITER019B_G37A_NONNESTED_PROTOCOL_FAIL_TERMINAL.md`.

### G38 colored finite-correlation trajectory

G38-P aggregate job `103580959913`, artifact `10301152567`, digest `sha256:8642947c6b1c03689c35ed472ed994fe1cca2b3724c9320e07108dff4f4e0980`: 12/12 OU implementation checks pass. Single-time OU output is identifiable only through integrated phase variance and is redundant with G36, motivating a multi-time gate.

G38-C aggregate job `103581251810`, artifact `10300863359`, digest `sha256:bd16f6d2fb356285d29725b2275fe3f1ca93b4bbb8287c2815e52a755f12cf2f`: 12/12 hidden three-time OU trajectories calibrated at `T=[0.25,0.5,1.0]`; worst max-per-time trace gap `1.4952140765689448e-13` (Sobol) and `2.3292762004080123e-14` (LHS).

G38-A aggregate job `103581860728`, artifact `10301542445`, digest `sha256:ed9a0728c9288e696e6ed62fba176b848a46790c5ec7fe2faad9dbf04d26aa00`: all four toy trajectories × two calibrated methods pass the frozen nonzero-gap and per-time cross-method agreement rules. Max-gap pairs are `(0.025545074758564972,0.0255450797621222)`, `(0.10046306945014429,0.1004630806848435)`, `(0.35877357179426705,0.3587736163604044)`, `(0.5996899264483135,0.5996899101531477)`. Durable note: `results/ITER020C_G38A_COLORED_TRAJECTORY_ADVERSARIAL_TERMINAL.md`.

## Active frontier

### G37-C2 corrected nested combined calibration

Run `34704249235`, launch head `0852fe30aa6bb7542dbb5ff4ec17fe8fd6eb55c1`. Corrected generator has an explicit `lambda_MF in [0,1]`, so `lambda_MF=0` exactly contains shared-only and `cA=cB=0` exactly contains MF-only. Frozen suite: 16 positive-control lanes including both exact boundaries + 4 admissibility lanes. Latest checked state: **19/20 terminal success (95%)**; only Sobol MF-only boundary shard 4 remains in progress. Aggregate and adversarial authorization remain blocked.

### G39-P multimode shared classical noise implementation

Run `34704548004`, head `995f3c60b7648afe7a7d1a9b6ebb4c9e609dbf20`. Twelve rank-2/rank-3 validation lanes are in progress. This finite low-rank positive-Kossakowski construction uses multiple shared classical white-noise modes and explicitly noncommuting local axes while preserving local-unitary factorization on each stochastic path. G39-P is implementation/admissibility only; optimizer calibration must precede any adversarial RCG-002 search.

## Stable readiness rubric

- independent scope/claim discipline: closed
- toy-channel coherent candidate construction: closed
- finite MF K2/K3/K4 calibration, robustness and scoped adversarial layers: closed
- shared single-mode classical-noise implementation/calibration/scoped adversarial layer: closed
- OU colored finite-correlation three-time trajectory implementation/calibration/scoped adversarial layer: closed
- corrected truly nested MF+shared family: active G37-C2
- multimode shared-classical-noise implementation: active G39-P
- multimode optimizer/adversarial layer: open
- higher-rank/general positive-Kossakowski classical comparator: open
- strict information-backflow/non-Markovian comparator: open
- externally anchored observable/holdout programme: open
- full candidate-gravity dynamics / continuum completion: open

Current internal programme readiness: **57%**. This is a construction/readiness metric, not a probability of physical correctness. Theory established remains **0%**.

## Claim locks

Never promote finite-family gaps to claims that all semiclassical gravity, all classical mediators or all alternatives to quantum gravity are excluded. Green CI alone is not scientific PASS. Do not weaken the frozen `2e-3` calibration/agreement or `1e-4` nonzero-gap rules post hoc. G30/G31 minima remain diagnostic. Old G37-A remains a protocol-design failure. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions.