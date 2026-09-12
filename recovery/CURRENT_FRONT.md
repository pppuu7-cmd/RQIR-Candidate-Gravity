# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active gates: `ITER019F / G37-A3` and `ITER021E / G39-A2`
Phase: `INDEPENDENT_RQIR_DERIVATION / BOUNDARY_PRESERVING_CLASSICAL_COMPARATOR_SEARCH`

## Canonical status

- Candidate-model/programme readiness: **57%**
- Theory established: **0%**
- Active seed: `RCG-002 Relational controlled-phase channel`
- Independent-from-QGR construction contract: **FROZEN**
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**

Readiness is an internal construction metric, not a probability of physical correctness. No readiness increase is granted for a comparator gate with unresolved optimizer/nesting validity.

## Closed scoped comparator layers

- G35 run `34697766107`: calibrated finite K3/K4 additive independent measurement-feedback support.
- G35-R run `34702384573`: held-out K2/K3/K4 optimizer replication 18/18 PASS.
- G36-P/C/A: one shared Gaussian classical-noise implementation, calibration and scoped adversarial support closed.
- G38-P/C/A: OU finite-correlation three-time toy-trajectory implementation/calibration/scoped support closed. This is not strict information-backflow non-Markovian evidence.

## G37 truly nested MF + one shared-noise family

### G37-C2 calibration — PASS
Run `34704249235`, head `0852fe30aa6bb7542dbb5ff4ec17fe8fd6eb55c1`, aggregate job `103582186949`, summary artifact `10301617346`. Sixteen hidden positive controls and four admissibility lanes passed. `lambda_MF=0` exactly removes the complete MF generator because `Lgen(chi=0)` has zero coherent and dissipative rates; `cA=cB=0` gives the MF-only boundary. Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_TRULY_NESTED_MF_PLUS_SHARED`.

### G37-A2 adversarial — optimizer validity failure
Run `34704659119`, head `823587d7cea5fb0f673487edeb5f7f9e730ad129`, aggregate `103583394963`, summary artifact `10301677814`, digest `sha256:16593751b5a591a229c1ffaf413f40722490c24f5df533800475b499f26efbb2`.

All eight lanes were structurally valid and both methods retained nonzero gaps with cross-method agreement, but shard 2 returned about `0.3620191372` while a legal shared-only parent point is about `0.3587370384`, violating the frozen parent nesting rule. Classification remains `NUMERICAL_OPTIMIZER_NESTING_VALIDITY_FAIL`, not scientific support or refutation of RCG-002.

### G37-A2-N diagnostic — exact embedding PASS / surrogate refinement FAIL
Run `34707889631`, launch head `fd2eb2be2f7fc7184f83f6e629db5810bad7c317`, aggregate `103591262282`, summary artifact `10302207524`, digest `sha256:fcd02773fc689b03a1564b1f04eeb8c5b28570e645b83aa644902c7242120e44`.

Eight diagnostic lanes were structurally valid. The exact G36 shared-parent embedding into G37 agrees in trace distance to at worst `1.1102230246251565e-16`, proving implementation-level containment. However LSQ refinement from a legal parent point can worsen the final trace-distance objective by as much as `0.003282498938826206`; therefore the prospectively frozen aggregate `diagnostic_support=false`. Correct classification: `EXACT_PARENT_EMBEDDING_VALID + SURROGATE_OBJECTIVE_REFINEMENT_FAIL`. The failure exposes objective mismatch; it is not a physics failure and is not retroactively converted to diagnostic PASS.

### Active G37-A3 boundary-preserving repair
Run `34708041385`, launch head `28d6fa6343dabb068aba5a462f6026d8ec1a6a4f`.

New prospective gate keeps the original G37-A2 Sobol/LHS 19D search intact, but also retains both exact legal parent candidates: G36 shared-only at `lambda_MF=0` and G34 K2 MF-only at `lambda_MF=1, cA=cB=0`. Both boundary seeds may be refined, but exact parent points remain candidates and all candidates are ranked by final trace distance. Frozen rules: nonzero `>1e-4`, cross-method agreement `<=0.002`, exact embedding/nesting tolerance `1e-10`. No prior result is promoted.

## G39 rank-2/rank-3 multimode shared classical-noise family

### G39-P / G39-C — PASS
G39-P run `34704548004` validated finite rank-2/rank-3 multimode shared classical white-noise implementation/admissibility. G39-C run `34704727102`, head `389b8723f81c8e94f864fcf1b82de4503c329c7e`, aggregate `103582784567`, artifact `10300663179`, digest `sha256:4f2365d8ef2d491478bfc6b184a0121d57aaeac1032755055f4574eeb3455959`, calibrated both ranks under Sobol/LHS. Worst recovery gaps were `3.05e-12`/`2.87e-12` for rank 2 and `2.49e-11`/`4.27e-12` for rank 3.

### Original G39-A — optimizer nesting invalid
Run `34704846612`, head `8f011454324652076876b9b79821e40155d8c573`, aggregate `103583601316`, artifact `10300858098`, digest `sha256:9a8a4176d29795e84dc6c7c8eda595eb4ab9bdbb5a0392e3a64a1ac8110aff1b`.

Rank 3 violated exact rank3⊇rank2 nesting on shard 3: rank2 about `0.59823276`, rank3 about `0.61107`. Classification: `NUMERICAL_OPTIMIZER_SEARCH_MISS / NESTING_VIOLATION`; neither scientific support nor refutation.

### G39-A-N diagnostic — PASS
Run `34706674297`, head `30a3f202d21726f271cd874dc1afc3d27d54de14`, aggregate `103588218746`, artifact `10302540122`, digest `sha256:0f320730c3f2a275222a82167dcd6f301cbe688e40febc76b8b3d0ede83194b9`.

All 8 diagnostic lanes passed. Exact rank2→rank3 zero-third-rate embedding reproduced the rank2 objective with maximum gap difference `0.0`; seeded rank3 refinement was no worse than embedded by more than `3.9312997301976793e-13`. This establishes the original G39-A nesting failure as an optimizer/search miss only; it does not itself establish adversarial support.

### Active G39-A2 parent-seeded repair
Run `34707920572`, launch head `da65199d56e1cb1be5bff232f97230611dd9ef2e`.

The original rank3 Sobol/LHS designs remain intact. Each method/shard also reproduces the rank2 optimum, embeds it exactly at zero third-mode rate, retains the exact point as a candidate and refines from it. Winner selection is by final trace distance. Frozen rules: exact embedding/nesting `1e-10`, nonzero `>1e-4`, cross-method agreement `<=0.002`. No family or threshold change.

## Open layers

- terminal classification of G37-A3 and G39-A2;
- higher-rank/general positive-Kossakowski classical comparator beyond finite G39 rank;
- strict information-backflow/non-Markovian comparator layer with a prospectively calibrated witness;
- externally anchored observable/holdout programme;
- full candidate-gravity dynamics / continuum completion.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, any claim that all classical/semiclassical mediators are excluded, treating green CI as scientific PASS, post-hoc threshold/family weakening, retroactive promotion of G30/G31 or invalid G37/G39 minima, or importing physical assumptions/results from QGR/KMQGB/RQIR.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + FINITE_COMPARATOR_SUPPORT_ONLY + G37C2_CALIBRATED + G37A2_OPTIMIZER_FAIL + G37A2N_EXACT_EMBEDDING_PASS_SURROGATE_FAIL + G37A3_RUNNING + G39C_CALIBRATED + G39A_OPTIMIZER_FAIL + G39AN_DIAGNOSTIC_PASS + G39A2_RUNNING`.
