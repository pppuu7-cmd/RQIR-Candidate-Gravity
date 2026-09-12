# RQIR-CG research ledger

This is the clean scientific authority ledger for `RQIR-Candidate-Gravity`. Legacy mixed-project ledgers are not scientific authority for this project.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, funnel/gate discipline and general mathematical tools, but not imported physical assumptions, ansatz coefficients, results or desired conclusions.

## Authoritative result table

| Iteration | Gate | Run / head | Classification | Result ceiling |
|---|---|---|---|---|
| Iter010 | G28 | `34692403874` / `3d8d3f969a22c22c1526b00f42377c2d41f87a04` | `DERIVED_SCOPED_NEGATIVE_COMPARATOR_RESULT` | Finite single-axis Markovian family. |
| Iter011 | G29 | `34694101699` / `c4c6f0d35e4e57a2105facafee2bdddc8036a52f` | `DERIVED_SCOPED_ROBUSTNESS_SUPPORT` | Same finite family. |
| Iter012 | G30 | `34694264478` / `fa9be36b422b84614b03f96de7c37660059f2d74` | `FINITE_SEARCH_DIAGNOSTIC` | Historical minima non-authoritative. |
| Iter013 | G31 | `34695076098` / `f32ecf1949f1e7d6c577b201b73c517d4605fdb7` | `SCIENTIFIC_CALIBRATION_FAIL / GLOBAL_OPTIMIZER_NOT_VALIDATED` | Adversarial minima diagnostic only. |
| Iter014 | G32 | `34695441883` | `POSITIVE_CONTROL_OPTIMIZER_FAIL / LOCAL_BASIN_OR_OBJECTIVE_GEOMETRY_FAIL` | Direct optimization unreliable. |
| Iter014B | G32-J | `34695478444` / `706245fa183845556aa020bc99d2a4d86e4e3060` | `FULL_LOCAL_RANK / STRONGLY_ILL_CONDITIONED_DIAGNOSTIC` | Rank full; conditioning strong. |
| Iter015 | G33 | `34695662002` / `d15d633f58fa63d378a85d6e5409c4bb0735a97e` | `POSITIVE_CONTROL_METHOD_CALIBRATED_K2` | Sobol/LHS smooth optimizer authority. |
| Iter016 | G34 | `34695835216` / `09d729764ca38a0d83f11b81dc59f157cd0cb734` | `DERIVED_SCOPED_K2_CALIBRATED_COMPARATOR_SUPPORT + POSITIVE_CONTROL_METHOD_CALIBRATED_K3_K4` | Finite additive independent MF family. |
| Iter017 | G35 | `34697766107` / `fbc71768da3cec0d6ea5a8cbb755a29036b16726` | `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT` | K3/K4 finite additive independent MF. |
| Iter017R | G35-R | `34702384573` / `1b93cbf14b4705ae2699f559523d1c1b1ae28be5` | `HELDOUT_OPTIMIZER_ROBUSTNESS_PASS_K2_K3_K4` | Methodology robustness. |
| Iter018A | G36-P | `34702575861` / `270a26300117aeebe23af126dd4e6c53c96cf3f9` | `CLASSICAL_SHARED_NOISE_IMPLEMENTATION_VALIDATED` | One shared Gaussian classical mode. |
| Iter018B | G36-C | `34703606707` / `95335aa32e92dcd1cc76762cd6fd3717754a1057` | `POSITIVE_CONTROL_METHOD_CALIBRATED_SHARED_NOISE` | Optimizer calibration only. |
| Iter018C | G36-A | `34703779268` / `15ba7c90fd4794d3d31e41a5a08ee35511284faf` | `DERIVED_SCOPED_SHARED_NOISE_CALIBRATED_COMPARATOR_SUPPORT` | One shared Gaussian classical mode. |
| Iter019A | G37-C old | `34703787083` / `59cf94512a65a54a37eba05ae3093b7ee85bead0` | `CALIBRATED_OWN_FAMILY / LATER_FOUND_NONNESTED` | Not a shared-only superset. |
| Iter019B | G37-A old | `34704008252` / `e0288f6e5dc58c43f71c790d5402bdb7bb9561c9` | `PROTOCOL_DESIGN_FAIL / NONNESTED_COMBINED_FAMILY` | Diagnostic only. |
| Iter019C | G37-C2 | `34704249235` / `0852fe30aa6bb7542dbb5ff4ec17fe8fd6eb55c1` | `POSITIVE_CONTROL_METHOD_CALIBRATED_TRULY_NESTED_MF_PLUS_SHARED` | Corrected finite MF + one shared-noise family. |
| Iter019D | G37-A2 | `34704659119` / `823587d7cea5fb0f673487edeb5f7f9e730ad129` | `NUMERICAL_OPTIMIZER_NESTING_VALIDITY_FAIL` | No adversarial scientific verdict. |
| Iter019E | G37-A2-N | `34707889631` / `fd2eb2be2f7fc7184f83f6e629db5810bad7c317` | `EXACT_PARENT_EMBEDDING_VALID + SURROGATE_OBJECTIVE_REFINEMENT_FAIL` | Methodology diagnosis only. |
| Iter019F | G37-A3 | `34708041385` / `28d6fa6343dabb068aba5a462f6026d8ec1a6a4f` | `RUNNING / BOUNDARY_PRESERVING_REPAIR` | Prospective repaired finite-family adversarial gate. |
| Iter020A | G38-P | `34704060723` / `a1db86645204fd158057673e57518374e9434666` | `OU_COLORED_CLASSICAL_NOISE_IMPLEMENTATION_VALIDATED` | OU finite-correlation classical noise. |
| Iter020B | G38-C | `34704210632` / `86eb78312d1cdcf58c4844e98b4065482b9fc4c8` | `POSITIVE_CONTROL_METHOD_CALIBRATED_OU_COLORED_TRAJECTORY` | Three-time optimizer calibration. |
| Iter020C | G38-A | `34704373278` / `493da45d6a9b88e5cee32fca598fb657ea7a2ce4` | `DERIVED_SCOPED_OU_COLORED_TRAJECTORY_COMPARATOR_SUPPORT` | Three-time toy trajectory only. |
| Iter021A | G39-P | `34704548004` / `995f3c60b7648afe7a7d1a9b6ebb4c9e609dbf20` | `MULTIMODE_CLASSICAL_NOISE_IMPLEMENTATION_VALIDATED` | Finite rank2/rank3 shared classical white noise. |
| Iter021B | G39-C | `34704727102` / `389b8723f81c8e94f864fcf1b82de4503c329c7e` | `POSITIVE_CONTROL_METHOD_CALIBRATED_MULTIMODE_R2_R3` | Optimizer calibration only. |
| Iter021C | G39-A | `34704846612` / `8f011454324652076876b9b79821e40155d8c573` | `NUMERICAL_OPTIMIZER_SEARCH_MISS / NESTING_VIOLATION` | No adversarial scientific verdict. |
| Iter021D | G39-A-N | `34706674297` / `30a3f202d21726f271cd874dc1afc3d27d54de14` | `RANK3_CONTAINMENT_VALID / ORIGINAL_SEARCH_MISS_DIAGNOSED` | Diagnostic only. |
| Iter021E | G39-A2 | `34707920572` / `da65199d56e1cb1be5bff232f97230611dd9ef2e` | `RUNNING / PARENT_SEEDED_REPAIR` | Prospective repaired finite rank3 adversarial gate. |

## Recent decisive diagnostics

### G37-A2 and G37-A2-N

G37-A2 aggregate job `103583394963`, summary artifact `10301677814`, digest `sha256:16593751b5a591a229c1ffaf413f40722490c24f5df533800475b499f26efbb2`: all lanes were finite and cross-method stable, but shard 2 gave about `0.3620191372` while a legal shared-parent point is about `0.3587370384`, violating the frozen +0.002 nesting sanity.

G37-A2-N aggregate job `103591262282`, artifact `10302207524`, digest `sha256:fcd02773fc689b03a1564b1f04eeb8c5b28570e645b83aa644902c7242120e44`: exact shared-parent embedding agrees with the G36 parent gap to at worst `1.1102230246251565e-16`, but LSQ refinement can worsen trace distance by `0.003282498938826206`. Because the LSQ residual norm is a smooth surrogate and the scientific metric is trace distance, the binary frozen diagnostic did not pass. The scientifically correct methodology classification is `EXACT_PARENT_EMBEDDING_VALID + SURROGATE_OBJECTIVE_REFINEMENT_FAIL`; no physics inference follows. This motivated prospective G37-A3, which preserves exact parent candidates and ranks all candidates by trace distance.

### G39-A and G39-A-N

Original G39-A aggregate `103583601316`, artifact `10300858098`, digest `sha256:9a8a4176d29795e84dc6c7c8eda595eb4ab9bdbb5a0392e3a64a1ac8110aff1b`: shard 3 returned rank3 ≈`0.61107` versus rank2 ≈`0.59823276`, despite exact zero-rate containment.

G39-A-N aggregate `103588218746`, artifact `10302540122`, digest `sha256:0f320730c3f2a275222a82167dcd6f301cbe688e40febc76b8b3d0ede83194b9`: 8/8 diagnostic lanes PASS. Exact rank2→rank3 embedding gap difference is `0.0`; seeded rank3 refinement is no worse than embedded by more than `3.9312997301976793e-13`. This diagnoses the original G39-A failure as an optimizer/search miss and authorizes the separately preregistered G39-A2.

## Active frontier

### G37-A3 — run `34708041385`

Boundary-preserving repaired adversarial gate. It retains the complete original G37-A2 combined Sobol/LHS search and additionally retains exact G36 shared and G34 K2-MF parent boundary candidates, plus refinements from both. Winner selection is by final trace distance. Frozen thresholds: nonzero `>1e-4`, cross-method `<=0.002`, parent embedding/nesting `1e-10`.

### G39-A2 — run `34707920572`

Parent-seeded repaired rank3 adversarial gate. It retains all original rank3 starts and an exact zero-third-rate rank2 boundary candidate plus seeded refinement. Frozen thresholds: nonzero `>1e-4`, cross-method `<=0.002`, exact embedding/nesting `1e-10`.

## Stable readiness rubric

Closed: independent scope/claim discipline; toy-channel coherent seed; finite MF K2/K3/K4 calibration and scoped comparator layer; one-mode shared classical-noise implementation/calibration/scoped comparator; OU three-time toy-trajectory implementation/calibration/scoped comparator; corrected G37 family calibration; G39 rank2/rank3 implementation and calibration.

Not closed: valid terminal repaired G37 adversarial classifier; valid terminal repaired G39 adversarial classifier; higher-rank/general positive-Kossakowski classical comparator; strict information-backflow/non-Markovian comparator; externally anchored observables/holdouts; continuum/full candidate-gravity dynamics.

Current internal programme readiness: **57%**. This is a construction/readiness metric, not a probability of physical correctness. Theory established remains **0%**. Do not raise readiness until a stable rubric gate closes.

## Claim locks

Never promote finite-family gaps to claims that all semiclassical gravity, all classical mediators or all alternatives to quantum gravity are excluded. Green CI alone is not scientific PASS. Do not weaken the frozen `2e-3` calibration/agreement or `1e-4` nonzero-gap rules post hoc. G30/G31 minima remain diagnostic. Old G37-A is a protocol-design failure. G37-A2/G39-A are optimizer-validity failures, not physics verdicts. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions.
