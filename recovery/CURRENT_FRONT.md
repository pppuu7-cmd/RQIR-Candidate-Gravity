# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_ATTACK`
Active production gates: `ITER034 / G46-C extended trace-ball calibration` + `ITER036 / G47-C three-state hidden-classical switching calibration`

## Canonical status

- Candidate-model/programme readiness: **62%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is programme completion, not probability of correctness. Calibration/implementation/provenance/coverage gates do not raise readiness. The increase `61% -> 62%` is authorized only by terminal G44-A closing a new scoped basis-invariant comparator layer.

## Newly closed authority

### G44-A basis-invariant trace-ball PSD adversarial — PASS

Run `34718045811`, launch/head `fbb9305039bc44086e100ba23fe4c90e2a13cd97`, aggregate job `103620135891`, summary artifact `10305246941`, digest `sha256:6b872735ae3fc2ad3512c44cda92b1567f413242d81f43cee09f7687d6a1f5d8`.

All 8/8 Sobol/LHS lanes passed structural/admissibility and the frozen pair rules. Gap pairs by shard:
- s0 `0.037007977715339695 / 0.0370079787290966`, diff `1.0137569048107586e-09`;
- s1 `0.14632856614507492 / 0.14632854102560847`, diff `2.511946645133989e-08`;
- s2 `0.5275494416263767 / 0.5275492466713227`, diff `1.9495505398925417e-07`;
- s3 `0.6620257715176718 / 0.6628923292652587`, diff `0.0008665577475868158`.

Classification `DERIVED_SCOPED_BASIS_INVARIANT_TRACE_BALL_PSD_COMPARATOR_SUPPORT`. Scope is only bounded real-PSD Markovian random-Hamiltonian `tr(C)<=4`; no unbounded/all-classical/semiclassical no-go. Durable note: `results/ITER032_G44A_TRACE_BALL_PSD_ADVERSARIAL_TERMINAL.md`. Readiness `61% -> 62%`.

### G45-P complex-Hermitian PSD provenance boundary — PASS

Run `34718225194`, launch/head `35583bcaa013944017a18c56f8f05714b616ee81`, aggregate `103620231708`, summary artifact `10305418039`, digest `sha256:728b361f4a317e3ffa3f444f1f4cb5198f3dda21ce1411fdf4f4affdf581f80b`.

All 12/12 response-blind lanes valid. Real-PSD controls remain inside classical real-Kossakowski + local-H span at machine precision. Same-site and cross-site complex-PSD panels each show 4/4 frozen provenance obstructions. Classification `COMPLEX_PSD_EXTENDS_BEYOND_CLASSICAL_RANDOM_HAMILTONIAN_PROVENANCE_ON_FROZEN_CONTROLS`. Generic complex-PSD GKSL must not be relabelled classical without an explicit constructive provenance proof. Provenance-only; no readiness increment. Durable note: `results/ITER033_G45P_COMPLEX_PSD_PROVENANCE_TERMINAL.md`.

### G47-P explicit three-state hidden-classical switching provenance — PASS

Run `34719123666`, launch/head `f3f4f178d465f302976968ba64cfbdc8a2d4d7c3`, aggregate `103621684322`, summary artifact `10305452269`, digest `sha256:b54e8db29ca0749710c70707bb2bb531aa504ee9a9912379cc0aa5752977d671`.

All 6/6 response-blind shards pass explicit CTMC + local-sum/product-unitary provenance. Max factorization error `2.4754502541992043e-16`, max TP residual `2.118459146238855e-15`, min Choi eig `1.0448912891480442e-14`, max product-output negativity `0`. All 6/6 show the prospectively frozen reduced non-semigroup witness; defect range `1.075578758977815..1.258601775030117` versus threshold `1e-4`.

Classification `THREE_STATE_CLASSICAL_SWITCHING_PRODUCT_UNITARY_PROVENANCE_VALIDATED`. This is implementation/provenance only, not a target-separation result and not BLP information-backflow proof. Durable note: `results/ITER035_G47P_THREE_STATE_CLASSICAL_SWITCHING_TERMINAL.md`.

### G40-TM-A prospective RTN adversarial — frozen support rule not met

Run `34716863840`, aggregate `103616629784`, artifact `10305770549`, digest `sha256:7ece1af4ca748acc2a0597b1c5f900e58e805de2cfdf2d01a7f2cc6fed1d3a4b`. All 8 lanes individually valid/nonzero-gap, but all four Sobol/LHS pair differences exceed frozen agreement `0.002`. Classification `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET`; no post-hoc rescue and no universal RTN no-go.

## Active gate 1 — G46-C extended basis-invariant trace-ball calibration

Preregistered response-blind before implementation. Frozen caps are geometric enlargements `tr(C)<=8` and `tr(C)<=16`, not selected from G44-A target optima. No RCG-002 target.

- protocol commit `fdba3fa00bfa883bcd525e641ace2a4bad91e7a3`;
- implementation `24e359fed57adcc254b9dcf86a7e76f6c3cb3acd`;
- workflow `529df10a1a23259c23872d4240f69bad4bf5f678`;
- launch/head `9c1f78dd72d70ad3f47a6fc54ef0c550a64a4290`;
- run **`34719083985`**.

24 lanes = 2 caps × ranks1–6 × Sobol/LHS. Latest durable sync: **7/24 terminal = 29.2%**, 4 in progress, 13 queued. Inspected cap8/rank6/Sobol exact boundary control has `tr(C)=8`, gap `3.194598192689347e-14`, relative C error `2.8246672629571763e-13`, rank6/6 and `scientific_support=true`.

Only terminal 24/24 aggregate PASS may authorize a separately preregistered G46-A adversarial gate. Calibration alone cannot change readiness.

## Active gate 2 — G47-C three-state hidden-classical switching optimizer calibration

Authorized only after terminal G47-P PASS. No RCG-002 target.

- preregistration `3995072ef3acc064cd0bbe460c446094fdee9864`;
- implementation `3e700e64ef039406a4f7a9fc17cef8e7721b1c3a`;
- workflow `47cd42ba7361fb20982efbda120ec90d2e828b65`;
- launch/head `2623e3e898f197cfdacce5a02532b416e886298e`;
- run **`34719251400`**.

8 response-blind positive-control lanes = four frozen 12D hidden CTMC/local-field controls × Sobol/LHS. Frozen training/held-out recovery and parameter/provenance rules must all pass. Latest durable state at launch: run queued. Only terminal PASS may authorize separately preregistered G47-A target use.

## Stable scientific closures / limits

- G35 finite K2/K3/K4 additive MF scoped support.
- G36 shared Gaussian classical-noise scoped support.
- G37 corrected nested MF + shared-noise scoped support.
- G38 OU finite-correlation toy support.
- G39 finite rank2/rank3 multimode support.
- G40 RTN remains method-robustness unresolved under its prospective adversarial rule.
- G41 rank4/5/6 frame-indexed positive-rate scoped support.
- G42 bounded PSD scoped support; G42-BC single-chart basis-coverage limit.
- G43 frozen five-chart atlas partial limit.
- G44-P/G44-C representation+calibration; G44-A basis-invariant `tr(C)<=4` scoped comparator support.
- G45-P generic complex-PSD provenance boundary.
- G47-P explicit three-state hidden-classical memory provenance validation.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, green-CI-as-scientific-PASS, post-hoc threshold/family/witness/chart weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_62_PERCENT + THEORY_ESTABLISHED_0 + G44A_SCOPED_BASIS_INVARIANT_TRACE_BALL_SUPPORT + G45P_COMPLEX_PSD_PROVENANCE_BOUNDARY + G47P_EXPLICIT_CLASSICAL_MEMORY_PROVENANCE_PASS + G46C_RUNNING + G47C_RUNNING`.
