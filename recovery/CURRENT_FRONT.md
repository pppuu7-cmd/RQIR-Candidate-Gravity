# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active gate: `ITER021D / G39-A-N`
Phase: `INDEPENDENT_RQIR_DERIVATION / MULTIMODE_CLASSICAL_COMPARATOR_VALIDITY`

## Canonical status
- Candidate-model/programme readiness: **57%**
- Theory established: **0%**
- Active seed: `RCG-002 Relational controlled-phase channel`
- Independent-from-QGR construction contract: **FROZEN**
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**

Readiness is an internal construction metric, not a probability of physical correctness. No readiness increase is granted for an adversarial result whose mandatory nesting sanity fails.

## Closed scoped comparator layers
- G35 run `34697766107`: `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT` for the finite additive independent measurement-feedback family.
- G35-R run `34702384573`: `HELDOUT_OPTIMIZER_ROBUSTNESS_PASS_K2_K3_K4`.
- G36-P/C/A: single shared Gaussian classical-noise implementation, optimizer calibration and scoped adversarial support closed.
- G38-P/C/A: OU finite-correlation three-time trajectory implementation, calibration and scoped adversarial support closed. This is not a strict information-backflow/non-Markovian no-go.

## G37 corrected nested MF + shared family
### G37-C2 calibration — PASS
Run `34704249235`, head `0852fe30aa6bb7542dbb5ff4ec17fe8fd6eb55c1`, aggregate job `103582186949`, summary artifact `10301617346`, digest `sha256:84a21c20a621f09f36098f5fb72d0acbec4387053295157ccb3aa780b75acc8d`.

Frozen positive-control calibration passed 16/16 hidden controls under the `<0.002` rule, and 4/4 admissibility lanes passed. Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_TRULY_NESTED_MF_PLUS_SHARED`. This authorizes adversarial testing only.

### G37-A2 adversarial — NUMERICAL/OPTIMIZER NESTING FAIL
Run `34704659119`, head `823587d7cea5fb0f673487edeb5f7f9e730ad129`, aggregate job `103583394963`, summary artifact `10301677814`, digest `sha256:16593751b5a591a229c1ffaf413f40722490c24f5df533800475b499f26efbb2`.

All 8 lanes were structurally valid and both methods retained nonzero gaps with cross-method agreement. However shard 2 produced combined best gap `0.3620191372` versus exact shared-only parent `0.3587370384`; this violates the prospectively frozen `+0.002` nesting slack. Since the corrected family mathematically contains the declared parent boundaries, this cannot be promoted to scientific RCG-002 support. Classification: `NUMERICAL_OPTIMIZER_NESTING_VALIDITY_FAIL`, not a physical/scientific FAIL of RCG-002. Thresholds and family are unchanged.

## G39 multimode shared classical-noise layer
### G39-C optimizer calibration — PASS
Run `34704727102`, head `389b8723f81c8e94f864fcf1b82de4503c329c7e`, aggregate job `103582784567`, summary artifact `10300663179`, digest `sha256:4f2365d8ef2d491478bfc6b184a0121d57aaeac1032755055f4574eeb3455959`.

Rank 2 and rank 3 each recovered all four frozen hidden positive controls under both Sobol-LSQ and LHS-LSQ. Worst recovery gaps were `3.05e-12`/`2.87e-12` for rank 2 and `2.49e-11`/`4.27e-12` for rank 3, far below the frozen `0.002` tolerance. Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_MULTIMODE_R2_R3`. This authorizes adversarial testing only.

### Original G39-A adversarial — OPTIMIZER/NESTING INVALID
Run `34704846612`, head `8f011454324652076876b9b79821e40155d8c573`, aggregate job `103583601316`, summary artifact `10300858098`, digest `sha256:9a8a4176d29795e84dc6c7c8eda595eb4ab9bdbb5a0392e3a64a1ac8110aff1b`.

All lanes were structurally valid and the nonzero gaps/cross-method comparisons were otherwise stable, but shard 3 returned rank-3 gaps about `0.61107` while rank-2 is about `0.59823`, violating the frozen rank3⊇rank2 nesting sanity by much more than `0.002`. The implementation permits an exactly zero third-mode rate, so rank 3 mathematically contains rank 2. Therefore the terminal run is classified `NUMERICAL_OPTIMIZER_SEARCH_MISS / NESTING_VIOLATION`; it is neither scientific support nor scientific refutation of RCG-002.

## Active G39-A-N diagnostic
Authoritative launch commit `30a3f202d21726f271cd874dc1afc3d27d54de14`, run `34706674297`.

Frozen diagnostic reproduces the rank-2 search, embeds its retained optimum exactly in rank 3 with third-mode rate fixed to zero, and then refines from that legal embedded point. Frozen tolerance is `1e-10`; target, family, optimizer bounds and all prior science thresholds are unchanged.

Latest checked state: **7 useful lanes in progress, 1 queued**. No avoidable compute idle while runner capacity is saturated.

Interpretation was frozen before results:
- all lanes pass => original G39-A nesting failure is an optimizer/search miss; only a prospectively repaired adversarial rerun with legal parent-boundary seeds is authorized next;
- exact embedding fails => implementation/nesting failure; stop G39 scientific interpretation and repair implementation only.

## Open layers
- valid corrected nested MF+shared adversarial classifier;
- valid repaired multimode rank2/rank3 adversarial classifier;
- higher-rank/general positive-Kossakowski classical-channel comparator;
- strict information-backflow/non-Markovian comparator layer;
- externally anchored observable/holdout programme;
- full candidate-gravity dynamics / continuum completion.

## Claim locks
Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, any claim that all classical/semiclassical mediators are excluded, treating green CI as scientific PASS, post-hoc threshold/family weakening, retroactive promotion of G30/G31 minima, or importing physical assumptions/results from QGR/KMQGB/RQIR.

Current correct status:
`RCG002_SCOPED_COHERENT_CANDIDATE + FINITE_COMPARATOR_SUPPORT_ONLY + G37C2_CALIBRATED + G37A2_OPTIMIZER_NESTING_FAIL + G39C_CALIBRATED + G39A_OPTIMIZER_NESTING_FAIL + G39A_N_DIAGNOSTIC_RUNNING`.
