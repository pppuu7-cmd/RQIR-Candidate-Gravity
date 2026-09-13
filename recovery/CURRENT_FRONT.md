# RQIR-Candidate-Gravity current front

Updated: 2026-09-13
Phase: `INDEPENDENT_RQIR_DERIVATION / G68_QUADRATIC_GRAVITY_BASELINE_CLOSED / G69_CANDIDATE_DYNAMICS_BLOCKED / G70_ARCHITECTURE_TRIAGE_CLOSED / G71_DISCRIMINATOR_AUDIT_CLOSED / G72_CD_MINIMAL_COMPLETIONS_CLOSED`

## Canonical status
- Candidate-model/programme readiness: **66%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.
- `recovery/state.json` is currently absent from the repository; this file plus `recovery/RECOVERY_DELTA_ITER068_G70.md`, newest commits, clean ledger and validated Actions artifacts are the available recovery authorities.

## Closed chain G68-G71
### G68
`G60_G67_LOCAL_FOUR_DERIVATIVE_ESCAPE_BASELINE_EQUIVALENT_TO_STANDARD_QUADRATIC_GRAVITY_SCOPED`, run `34771096136`. Local linearized four-derivative escape is standard curvature-squared quadratic gravity modulo 4D Gauss-Bonnet; novelty is not established in that layer.

### G69
`BLOCKED_CANDIDATE_OWNED_BEYOND_BASELINE_DYNAMICS_NOT_YET_DEFINED`, run `34771370710`. BLOCKED, not scientific FAIL.

### G70
`BEYOND_BASELINE_ARCHITECTURE_TRIAGE_COMPLETE_NO_UNIQUE_SELECTION`. Scientific streams run `34772158456`; infrastructure-only aggregate failure recovered analysis-only by run `34772248100`, job/artifact `103763840814/10322650703`, digest `sha256:a4c97a45ebfa26ddfb707614c9817f0c8d2f9a8303616664517399dc635d8f0a`. Pareto set `{B,C,D,E}`.

### G71
`BEYOND_BASELINE_UNRESOLVED_PROPERTY_AUDIT_SCOPED`. Prereg `f607a18b2d0830fcb2088da85b214161f72df219`; implementation `0e4be4fac1abf9ad4beabc075ba0e8fae92ef768`; production `3992d4578c94024e4179a71b7fb73d0ef8e6a9ba`; run `34772999854`; aggregate job/artifact `103765950139/10322965913`, digest `sha256:b65ca45de2de3a5d67dc704532f7cf142412e0908454771872ae760403b2c05c`. B/E dominated by D; Pareto narrowed to `{C,D}`.

## G72 — latest closed authority
Classification: `CD_ORTHOGONAL_MINIMAL_COMPLETIONS_EXIST_NO_UNIQUE_SELECTION_SCOPED`.

Preregistration `7c4d928517b7695a647d1a10f1eb9a956a87666d`; implementation `330c9398c7e3f11cfbf28d1496932496e92ec86e`; initial production head `ac89c7ab9f4aa05551ad89c551cab5990be02a5e`; initial run `34773142384`.

Initial C1/D1/D2 raw lanes are valid scoped PASS. C2 was technically invalid because its implementation imposed `z>0`, which excluded the preregistered negative-control root `z=-1/a`; the initial aggregate was therefore `INFRASTRUCTURE_OR_GATE_INVALID`, not scientific FAIL.

Control-only repair commit `e0d55cf86742cdba6198ad298f65fe565b7cf43e` changed only the symbol-domain assumption; frozen target, factor, control, thresholds and interpretation were unchanged. Recovery launch head `332773ca1f4e7cb7e447b321f2816b199432e796`; run `34776292245`; job `103774910076`.

Authoritative artifacts:
- C1 `10322009009`, digest `sha256:282869cec38e11e15b4e381caba4813642262deb82a53f4b805fb15483ad3c8f` — exact tested Ward completion, bare-source control rejected.
- D1 `10322492558`, digest `sha256:4adb59042704a71b0dc82119278d9af4c25b07566aa7894fdaefc36c8103785a` — exact tested retarded cubic support / CTP normalization, advanced control rejected.
- D2 `10322458302`, digest `sha256:56fd9c603f6ce7262e57a87974442b9621c01a2a0165d291bea2b6855c5da487` — cubic Hessian zero, quadratic control nonzero.
- Recovered C2 `10324140766`, digest `sha256:2e796de3c027e8350ac99217a01653385826514669815d91efa71f9739e7c3de` — `exp(-ell2*z)` has no finite complex zeros and polynomial control has exact root `-1/a`.
- Frozen aggregate recovery `10323627498`, digest `sha256:9dcee4947e89222c48247043cd3114b316371770a51b9a583edc42c599ae31a2`.

Scientific meaning: both remaining Pareto architectures admit the prospectively frozen minimal completion witnesses. G72 therefore does **not** select C or D. The completion objects remain HYPOTHESIS/CONSTRUCTION and are not inherited RCG-002 dynamics.

Terminal note: `results/ITER070_G72_CD_MINIMAL_COMPLETION_EXISTENCE_TERMINAL.md`.

## Next allowed gate
Use the closed G72 constructions only as frozen hypothesis objects and ask a discriminator that cannot be answered by repeating the same existence checks. The highest-value immediate target is perturbative-order identifiability: determine whether C's quadratic/two-point modification and D's cubic/three-point modification are distinguishable only when the observable panel spans both perturbative orders, with explicit rank-loss controls when either order is omitted. This is an identifiability statement, not architecture selection or a physical law.

## Open scientific layers
- candidate-owned deformation beyond standard local gravity baselines;
- nonlinear generally covariant candidate-owned dynamics;
- nonlinear conserved-source/Bianchi/diffeomorphism completion;
- field/measure/quantization closure;
- externally anchored physical predictions beyond current finite weak-field scope.

## Claim locks
Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, green-CI-as-scientific-PASS, post-hoc weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:
`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_66_PERCENT + THEORY_ESTABLISHED_0 + G68_STANDARD_QUADRATIC_GRAVITY_BASELINE_SCOPED + G69_BLOCKED_CANDIDATE_DYNAMICS_UNDEFINED + G70_PARETO_BCDE + G71_PARETO_CD + G72_CD_MINIMAL_COMPLETIONS_EXIST_NO_UNIQUE_SELECTION`.
