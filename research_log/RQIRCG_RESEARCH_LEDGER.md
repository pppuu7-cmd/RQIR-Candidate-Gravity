# RQIR-CG research ledger

This is the clean scientific authority ledger for `RQIR-Candidate-Gravity`. Legacy mixed-project ledgers are not scientific authority.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, funnel/gate discipline and general mathematical tools, but not imported physical assumptions, ansatz coefficients, results or desired conclusions. Green CI is never automatically scientific PASS. Frozen criteria/families/witnesses/charts are never weakened post hoc.

## Canonical readiness

- Internal programme readiness: **62%**.
- Theory established: **0%**.
- `58% -> 59%`: corrected G37-A3 scoped comparator closure.
- `59% -> 60%`: G41-A finite high-rank positive-rate comparator closure.
- `60% -> 61%`: G42-A bounded boundary-PSD adversarial comparator closure.
- `61% -> 62%`: G44-A basis-invariant real-PSD trace-ball `tr(C)<=4` comparator closure.
- Calibration, implementation, identifiability, provenance and coordinate-coverage gates do not themselves raise readiness.

## Authoritative gate ledger

| Gate | Run / head | Terminal classification / live state | Scope ceiling |
|---|---|---|---|
| G35 | `34697766107` | `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT` | Finite additive independent MF. |
| G36-A | `34703779268` | scoped shared-Gaussian-noise comparator support | One shared Gaussian classical mode. |
| G37-A3 | `34708041385` | `DERIVED_SCOPED_TRULY_NESTED_MF_PLUS_SHARED_BOUNDARY_PRESERVING_COMPARATOR_SUPPORT` | Finite K2 MF + one shared mode. |
| G38-A | `34704373278` | scoped OU colored-trajectory comparator support | Three-time OU toy trajectory. |
| G39-A2 | `34707920572` | rank2/rank3 multimode scoped support | Finite rank3 shared white noise. |
| G40-RC-A / D2 | `34710216045`, `34710444349` | `PERSISTENT_OPTIMIZER_OR_OBJECTIVE_GEOMETRY_NONROBUSTNESS` | Historical RTN branch: no physics PASS. |
| G41-A | `34710491309` | `DERIVED_SCOPED_HIGH_RANK_RATE_COMPARATOR_SUPPORT` | Frame-indexed rank4/5/6 positive-rate family. |
| G42-J | `34710643103` | `FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE` | 21-param real-PSD local identifiability only. |
| G42-C/C2/C3/R | `34710744967`, `34710953936`, `34711048394`, `34712524241` | bounded-PSD optimizer calibrated and held-out replicated | Calibration only. |
| G42-A | `34712491707` | `DERIVED_SCOPED_BOUNDARY_PSD_COMPARATOR_SUPPORT` | Single bounded Cholesky chart. |
| G42-BC | `34712857575` | `BOUNDED_CHART_ROTATION_COVERAGE_LIMIT_FOUND` | 14/24 rotated controls in chart. |
| G43-A | `34715739668` | `HELDOUT_MULTICHART_BASIS_COVERAGE_PARTIAL_LIMIT` | Fixed five-chart atlas: 25/36 covered. |
| G44-P | `34716135086` | `BASIS_INVARIANT_TRACE_BALL_PSD_REPRESENTATION_VALIDATED` | Basis-invariant bounded real-PSD `tr(C)<=4`. |
| G40-TM-C | `34716161178` | `TRACE_METRIC_ALIGNED_RTN_OPTIMIZER_CALIBRATED` | Prospective direct-trace RTN calibration only. |
| G44-C | `34716808171` | `BASIS_INVARIANT_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED` | Calibration only. |
| G40-TM-A | `34716863840` | `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET` | Pairwise method robustness failed; no RTN physics PASS. |
| G44-A | `34718045811` / `fbb93050...` | `DERIVED_SCOPED_BASIS_INVARIANT_TRACE_BALL_PSD_COMPARATOR_SUPPORT` | Bounded real-PSD Markovian `tr(C)<=4` only. |
| G45-P | `34718225194` / `35583bca...` | `COMPLEX_PSD_EXTENDS_BEYOND_CLASSICAL_RANDOM_HAMILTONIAN_PROVENANCE_ON_FROZEN_CONTROLS` | Provenance boundary only. |
| G47-P | `34719123666` / `f3f4f178...` | `THREE_STATE_CLASSICAL_SWITCHING_PRODUCT_UNITARY_PROVENANCE_VALIDATED` | Explicit finite 3-state hidden-classical memory provenance only. |
| G46-C | `34719083985` / `9c1f78dd...` | **RUNNING** | Response-blind calibration for fixed real-PSD caps 8 and 16. |
| G47-C | `34719251400` / `2623e3e8...` | **RUNNING/QUEUED** | Response-blind calibration for frozen 12D explicit 3-state switching family. |

## Recent decisive terminal provenance

### G44-A basis-invariant bounded real-PSD comparator closure

Run `34718045811`, aggregate `103620135891`, artifact `10305246941`, digest `sha256:6b872735ae3fc2ad3512c44cda92b1567f413242d81f43cee09f7687d6a1f5d8`.

All four prospectively frozen Sobol/LHS pairs pass. Gaps by shard: s0 `0.037007977715339695 / 0.0370079787290966`; s1 `0.14632856614507492 / 0.14632854102560847`; s2 `0.5275494416263767 / 0.5275492466713227`; s3 `0.6620257715176718 / 0.6628923292652587`. Worst pair disagreement `0.0008665577475868158 < 0.002`. Classification `DERIVED_SCOPED_BASIS_INVARIANT_TRACE_BALL_PSD_COMPARATOR_SUPPORT`. Durable note `results/ITER032_G44A_TRACE_BALL_PSD_ADVERSARIAL_TERMINAL.md`. This alone moves readiness 61→62.

### G45-P complex-PSD provenance boundary

Run `34718225194`, aggregate `103620231708`, artifact `10305418039`, digest `sha256:728b361f4a317e3ffa3f444f1f4cb5198f3dda21ce1411fdf4f4affdf581f80b`.

All 12 response-blind lanes valid. Real-PSD controls remain inside the real-Kossakowski + local-Hamiltonian provenance span at numerical precision; same-site and cross-site complex panels each show 4/4 frozen obstructions. Classification `COMPLEX_PSD_EXTENDS_BEYOND_CLASSICAL_RANDOM_HAMILTONIAN_PROVENANCE_ON_FROZEN_CONTROLS`. Generic complex-PSD GKSL is not authorized as a classical comparator without an independent constructive provenance proof. Durable note `results/ITER033_G45P_COMPLEX_PSD_PROVENANCE_TERMINAL.md`.

### G47-P explicit hidden-classical memory provenance

Run `34719123666`, aggregate `103621684322`, artifact `10305452269`, digest `sha256:b54e8db29ca0749710c70707bb2bb531aa504ee9a9912379cc0aa5752977d671`.

All 6/6 explicit three-state CTMC switching shards pass local-sum/product-unitary provenance, CP/TP and product-output checks; 6/6 also pass the frozen reduced non-semigroup witness. Max factorization error `2.4754502541992043e-16`; max TP residual `2.118459146238855e-15`; min Choi eig `1.0448912891480442e-14`; max product-output negativity `0`; semigroup defect range `1.075578758977815..1.258601775030117`. Classification `THREE_STATE_CLASSICAL_SWITCHING_PRODUCT_UNITARY_PROVENANCE_VALIDATED`. Durable note `results/ITER035_G47P_THREE_STATE_CLASSICAL_SWITCHING_TERMINAL.md`. No readiness increment.

### G40-TM-A retained negative robustness result

Run `34716863840`, aggregate `103616629784`, artifact `10305770549`, digest `sha256:7ece1af4ca748acc2a0597b1c5f900e58e805de2cfdf2d01a7f2cc6fed1d3a4b`. All lanes individually valid/nonzero-gap, but all four Sobol/LHS pair differences violate frozen agreement. Classification `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET`. No post-hoc rescue; not a universal RTN no-go.

## Active frontier

### G46-C — run `34719083985`

Response-blind calibration for prospectively fixed real-PSD trace caps 8 and 16. 24 lanes = caps × ranks1–6 × Sobol/LHS. Prereg `fdba3fa00bfa883bcd525e641ace2a4bad91e7a3`, implementation `24e359fed57adcc254b9dcf86a7e76f6c3cb3acd`, workflow `529df10a1a23259c23872d4240f69bad4bf5f678`, launch `9c1f78dd72d70ad3f47a6fc54ef0c550a64a4290`.

Latest durable sync: 7/24 terminal, 4 in progress, 13 queued. Inspected cap8/rank6/Sobol exact boundary control passes with gap `3.194598192689347e-14`, relative C error `2.8246672629571763e-13`, rank6/6 and `tr(C)=8`. Only terminal 24/24 aggregate PASS may authorize separately preregistered G46-A; calibration cannot raise readiness.

### G47-C — run `34719251400`

Response-blind optimizer calibration for the explicit frozen 12D three-state hidden-classical switching family. Prereg `3995072ef3acc064cd0bbe460c446094fdee9864`, implementation `3e700e64ef039406a4f7a9fc17cef8e7721b1c3a`, workflow `47cd42ba7361fb20982efbda120ec90d2e828b65`, launch `2623e3e898f197cfdacce5a02532b416e886298e`.

8 lanes = four deterministic hidden positive controls × Sobol/LHS. Training trace-gap, held-out trace-gap, normalized parameter-recovery and provenance rules are all frozen. No RCG-002 target. Only terminal PASS may authorize separately preregistered G47-A; no readiness increment from calibration.

## Open scientific layers

- terminal G46-C then, only if calibrated, prospectively separate G46-A for fixed caps8/16;
- terminal G47-C then, only if calibrated, prospectively separate G47-A for explicit finite three-state hidden-classical memory;
- broader classical memory families beyond one fixed finite CTMC construction;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and an actual gravity-theory constitution gate.

## Claim locks

Never promote finite/bounded-family gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen thresholds/families/witnesses post hoc. Invalid/nonrobust historical gates remain invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions. `THEORY_ESTABLISHED` remains 0%.
