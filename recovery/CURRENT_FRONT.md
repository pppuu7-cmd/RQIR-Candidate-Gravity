# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active gates: `ITER019F / G37-A3` and `ITER022B / G40-C`
Phase: `INDEPENDENT_RQIR_DERIVATION / BOUNDARY_PRESERVING_AND_INFORMATION_BACKFLOW_CLASSICAL_COMPARATORS`

## Canonical status

- Candidate-model/programme readiness: **58%**
- Theory established: **0%**
- Active seed: `RCG-002 Relational controlled-phase channel`
- Independent-from-QGR construction contract: **FROZEN**
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**

Readiness is an internal construction metric, not a probability of physical correctness. The increase from 57% to 58% records terminal closure of the prospectively repaired, calibrated finite rank-3 multimode shared-classical-white-noise adversarial comparator. It does not imply model truth or a general no-go theorem.

## Closed scoped comparator layers

- G35 run `34697766107`: calibrated finite K3/K4 additive independent measurement-feedback support.
- G35-R run `34702384573`: held-out K2/K3/K4 optimizer replication 18/18 PASS.
- G36-P/C/A: one shared Gaussian classical-noise implementation, calibration and scoped adversarial support closed.
- G38-P/C/A: OU finite-correlation three-time toy-trajectory implementation/calibration/scoped support closed. This is not by itself strict information-backflow evidence.
- G39-P/C/A2: finite rank-2/rank-3 multimode shared classical white-noise implementation, calibration and boundary-preserving scoped adversarial support closed.

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

New prospective gate keeps the original G37-A2 Sobol/LHS 19D search intact, but also retains both exact legal parent candidates: G36 shared-only at `lambda_MF=0` and G34 K2 MF-only at `lambda_MF=1, cA=cB=0`. Both boundary seeds may be refined, but exact parent points remain candidates and all candidates are ranked by final trace distance. Frozen rules: nonzero `>1e-4`, cross-method agreement `<=0.002`, exact embedding/nesting tolerance `1e-10`. No prior result is promoted. Latest checked state before G39 closure: **1/8 terminal, 7/8 in progress (12.5%)**.

## G39 rank-2/rank-3 multimode shared classical-noise family — CLOSED SCOPED GATE

G39-P run `34704548004` validated finite rank-2/rank-3 multimode shared classical white-noise implementation/admissibility. G39-C run `34704727102`, head `389b8723f81c8e94f864fcf1b82de4503c329c7e`, aggregate `103582784567`, artifact `10300663179`, digest `sha256:4f2365d8ef2d491478bfc6b184a0121d57aaeac1032755055f4574eeb3455959`, calibrated both ranks under Sobol/LHS.

The original G39-A run `34704846612` violated rank3⊇rank2 nesting and remains classified `NUMERICAL_OPTIMIZER_SEARCH_MISS / NESTING_VIOLATION`. G39-A-N run `34706674297`, artifact `10302540122`, digest `sha256:0f320730c3f2a275222a82167dcd6f301cbe688e40febc76b8b3d0ede83194b9`, proved exact rank2→rank3 containment and diagnosed the old search miss.

### G39-A2 parent-seeded repaired adversarial — PASS
Run `34707920572`, launch head `da65199d56e1cb1be5bff232f97230611dd9ef2e`, aggregate job `103592063859`, summary artifact `10302591508`, digest `sha256:bf8ac5713ec242ab494e501dde0d56f34db362b6d2a6e58b6c5a576dfac9557d`.

All 8 lanes passed the prospectively frozen rules. Rank-3 gaps (Sobol,LHS):
- shard 0: `(0.025499011417598586, 0.025499051947386945)`;
- shard 1: `(0.10036160336652522, 0.10036159991946002)`;
- shard 2: `(0.35873703855020184, 0.3587370386123476)`;
- shard 3: `(0.5982327597417393, 0.598232759851799)`.

For every shard, exact rank2 embedding, rank3≤rank2 nesting, nonzero `>1e-4`, rank3 cross-method agreement `<=0.002`, and parent cross-method agreement all passed. Classification: `DERIVED_SCOPED_MULTIMODE_RANK3_BOUNDARY_PRESERVING_COMPARATOR_SUPPORT`. Scope remains the calibrated finite rank-3 multimode shared classical white-noise family only.

## G40 strict classical information-backflow layer

### G40-P RTN information-backflow pre-gate — PASS
Run `34708162180`, launch head `0297f33faabeede29e0cb81c3161b278c18be9c0`, aggregate job `103592018677`, summary artifact `10302078122`, digest `sha256:720bc3d4a9c9841d1fd84bd7c00339fc6cbc9d6a37f9ba2bc24b7c8fd702e1c1`.

All 4 hidden-classical symmetric random-telegraph-noise validation lanes passed the frozen witness/admissibility rule. Minimum strong-control BLP total positive trace-distance increment was `0.5923274153651977` versus required `>0.02`; maximum weak-control BLP increment was `0.0` versus required `<1e-6`. Worst TP residual `4.440892098500626e-16`; minimum Choi eigenvalue `-3.732254805202328e-16`; maximum conditioned product-unitary factorization error `2.220988084178258e-16`; product-input output negativity `0.0`. Classification: `STRICT_CLASSICAL_RTN_INFORMATION_BACKFLOW_IMPLEMENTATION_VALIDATED`. This is implementation/witness evidence only and does not compare RCG-002.

### Active G40-C optimizer calibration
Run `34708292521`, launch head `80107b2d65c154d4e6a0cc52a2c1fffd8408dd8d`.

Prospectively frozen finite RTN family uses parameters `r,nu,cA,cB,thetaA,phiA,thetaB,phiB` with `gamma=r*nu*cA` and arbitrary local Pauli axes. Four hidden in-family controls are fit under independent Sobol/LHS constructions on fixed times `[0.35,0.80,1.60,3.00]` and six product-state probes. Each lane must recover maximum trace distance `<0.002` and retain BLP total positive increment `>0.02`; both methods must pass all four controls. G40-C is calibration only. No RCG-002 adversarial gate is authorized unless this terminally passes.

## Open layers

- terminal classification of G37-A3;
- terminal optimizer calibration of strict-BLP RTN G40-C, then a separate adversarial test only if PASS;
- higher-rank/general positive-Kossakowski classical comparator beyond finite G39 rank;
- externally anchored observable/holdout programme;
- full candidate-gravity dynamics / continuum completion.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, any claim that all classical/semiclassical mediators are excluded, treating green CI as scientific PASS, post-hoc threshold/family weakening, retroactive promotion of G30/G31 or invalid G37/G39 minima, or importing physical assumptions/results from QGR/KMQGB/RQIR.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + FINITE_COMPARATOR_SUPPORT_ONLY + READINESS_58_PERCENT + G37C2_CALIBRATED + G37A3_RUNNING + G39A2_SCOPED_RANK3_SUPPORT + G40P_STRICT_BLP_IMPLEMENTATION_PASS + G40C_RUNNING_OR_QUEUED`.
