# RQIR-Candidate-Gravity current front

Updated: 2026-09-14
Phase: `G95_STRUCTURAL_BLOCKED / G96_ATTRIBUTED_TERMINAL / G97_CLOSED_TOTAL_SOURCE_PREPARATION_PASS / NCP1_NOISY_COMPLETION_RESTRICTIONS_AND_NONUNIQUENESS_TERMINAL / CANDIDATE_OWNED_NONLINEAR_EVOLUTION_FRONTIER`

## Canonical status
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Programme readiness: **66%**; theory established: **0%**. These are bookkeeping labels, not probabilities.
- Scientific authority: newest main, this recovery file, dedicated `research_log/RQIRCG_RESEARCH_LEDGER.md`, `research_log/RQIRCG_RESEARCH_LEDGER_G95_G96_ADDENDUM.md`, and newest `research_log/RQIRCG_RESEARCH_LEDGER_NCP1_ADDENDUM.md`, terminal notes, validated Actions artifacts.
- Legacy mixed-project ledgers are not scientific authority. `recovery/state.json` remains absent.
- Independence lock remains active. No other candidate programme supplies dynamics or preferred coefficients.

## Latest terminal — NCP1 noisy nonlinear completion positivity
Preregistration: `a796519c7859c33eb1f590740860cf7f388563e1`.
Implementation: `5fa99c16b9b6e7d81fb338e22d1daf9c8886efe0`, `scripts/rcg002_ncp1.py`.
Production head: `2c761add0d4f4b055f426701a8fec76bbb2c667c`; run `34792497014`, attempt 1, all four matrix jobs and aggregate completed.
Raw archive: `8262b502b292b431863e2b862338679e324a767c`, `results/raw/RCG002_NCP1_RAW_BUNDLE.json`.
Terminal proof/qualification: `f5895e17c3113fe1a933c7411bf69319a0e91f25`, `results/RCG002_NCP1_NOISY_COMPLETION_TERMINAL.md`.
Clean ledger addendum: `14b345a2134a1646ac7fffa5e68b3681287ed624`.
Bundle artifact: `10328693336`, SHA256 `b86d7ad7f1c4f9320bca8c79e929a7892018ee58a83f10affff194bcb1ad8b32`.
Raw A/B/C/D artifacts: `10328810576 / 10328533762 / 10327644292 / 10328164412`.
All five archive digests and raw/aggregate equality were independently verified after completion. Full hashes, production/code identities, timestamps and exact polynomial witnesses are durable in the terminal/raw records. All 21 production controls passed; no partial values, duplicated production run, scientific retry or post-hoc cutoff increase were used.

### Scientific result
- `PASS_STRUCTURAL_NCP1`: exact positivity restrictions and calibrated positive nonuniqueness.
- `FAIL_HIGHER_ORDER_ONLY_NOISE_RESCUE_SCOPED`: a cubic phase cycle cannot be repaired by coherence losses starting only at fourth or higher history-amplitude order. The 3-by-3 determinant has leading term `-k^2*epsilon^6/4`.
- `FAIL_EXACT_GAUSSIAN_CUBIC_LOG_KERNEL_SCOPED`: on all real scalar histories, exact `exp(-nu*d^2+i*k*d*s^2)` is unitarily congruent to stationary `exp(-nu*t^2-i*k*t^3/12)`; Bochner plus Marcinkiewicz excludes k!=0 for finite nu>=0.
- `POSITIVE_NOISY_COMPLETIONS_NONUNIQUE_SCOPED`: complete nonpolynomial Gaussian/centered-Poisson calibration kernels share the quadratic/cubic jet but differ at fourth order and above. No member is selected as physics.
- Overall physical status: `BLOCKED_PHYSICAL_EVOLUTION`.
- Selector rank: `UNDEFINED_PHYSICAL_MAP_MISSING`, NOT zero.

For frozen k=1, exact moment certificates first fail at polynomial degrees 2, 4, 10 for nu=1/10, 1/2, 1. For nu=2 all degrees through 32 pass: the finite test is explicitly INCONCLUSIVE there, not physical PASS; the global theorem has its own independently verified domain. Gaussian k=0 controls pass the entire frozen range.

These statements do not exclude all noisy completions, finite physical history sets, perturbative expansions, nonanalytic noise, or restricted protocols. The positive counterexamples change higher odd phase terms as well as higher even damping terms; they do not repair the exact cubic-only phase at every order. The scalar ray exists in the G72 algebra but its physical source accessibility has not been derived.

Both calibration channels may preserve the G97 total translation generator by depending on Q=x1-X. This does NOT establish energy conservation, a causal gravitational dilation, nonlinear stress-energy conservation, or Bianchi closure. Positivity and total momentum alone do not select native nonlinear evolution. No physical gravitational quotient or its dimension is established.

## G95 terminal
`BLOCKED_MINIMAL_FINITE_HISTORY_STRUCTURAL_SPACE_EMPTY_SCOPED`.
Run `34791085566`; aggregate `10328282400`, digest `sha256:fe9cd5526cb5f96d73647bee43eed2783a9d1cb112d6d0c9768f4e74e41153fe`.
Exact finite 3-cell one-Delta structural rank is 10/10, nullity 0. Scope only; no general RCG-002/noisy/continuum no-go.

## G96 terminal
`G95_STRUCTURAL_OBSTRUCTION_ATTRIBUTED_SCOPED`.
Run `34791191689`; aggregate `10327927078`, digest `sha256:85bc13233b9a812b9d4114116e838e4729a34a31d3b210ecf5605525fd9ab17b`.
Nullities none/C0/C1/P/C0+C1/C0+P/C1+P/full = 10/4/5/7/1/2/3/0. Full `{C0,C1,P}` is the unique minimal zero-nullity family set. Every leave-one-family-out basis remains incoherent under the frozen noiseless cocycle/rank-one test. G95 is not weakened.

## G97 terminal
`PASS_CLOSED_TOTAL_SOURCE_PREPARATION_CONSERVATION_SCOPED`.
Authority: prereg `2a4c403882d156d56d918275c96aea3c19d53a61`; implementation `eb04d32b68d0f0ced8651df8599ba18b008bd105`; production `7274e539c0f6c4900da1bff7dd1d622508e45091`; run `34791265992`; artifacts A/B/C/D `10328211643 / 10327842336 / 10327937114 / 10328641718`; aggregate `10327777470`, digest `sha256:7f906cad27023f582530c8eb7f90fd449f11902fdd6d455cf54eec0ae69facba`.
Raw artifacts consumed before the original classification. Exact closed-source results: total momentum derivative 0; probe-only `-F1-F2` is cancelled by apparatus `F1+F2`; internal branch kicks preserve total momentum and are invertible; external holding gives `-lambda`, with `lambda=0` restoring closure.
Claim lock: classical source-preparation mechanics only. This is not nonlinear gravity, Bianchi closure, or a positive gravitational influence kernel.

## Exact next admissible fundamental gate
**Candidate-owned nonlinear causal source/state/evolution law on the closed G97 source system.**

It must be independently motivated and prospectively frozen before connected-phase outcomes are inspected. In the same realization it must specify the state and causal evolution, recover validated pairwise weak-field normalization, derive a normalized positive influence kernel or justified coherent factorization/noise split, and verify nonlinear conservation/Bianchi/constraint compatibility. NCP1 requires compatible higher noise AND phase terms if the cubic response is retained; an exact finite polynomial log kernel cannot simply be asserted as a complete global channel.

At present no such candidate-owned law exists in authoritative RQIR-CG state. Selector rank remains undefined at the physical nonlinear level; no coefficient is selected. The nonlinear gravitational completion space is not narrowed merely by counting these formal consistency tests.

Do not import dynamics from RQIR/KMQGB/QGR/MSQGR/ISQGR; fit a connected coefficient; promote G96 ablations, G97 mechanics, CPI1 control terms, or NCP1 calibration noise to gravitational dynamics to obtain a PASS. A new law requires a new independently motivated, prospectively specified candidate version or new physical datum. If that input is absent, retain `RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE`.

## Compute state
G95, G96, G97 and NCP1 are terminal. NCP1 was one four-lane GitHub matrix run, not a recurring automation. The scheduling check found no active RQIRCG auto-research task; none was activated by this run.

Do not duplicate NCP1, extend its moment cutoff post hoc, or use more arbitrary cumulant scans as a substitute for the native physical evolution principle. Productive parallel jobs should support one frozen physical decision object; an empty queue can reflect an unresolved scientific dependency rather than insufficient compute.

## Open layers and locks
Candidate-owned nonlinear evolution; nonlinear source/Bianchi/constraint closure; physical influence kernel; physical completion quotient; spacetime causality; state/measure completion; externally held-out predictions.

CPI1/G72-G97 historical outcomes remain intact, as does the recorded non-authoritative duplicate-G93 quarantine in earlier terminal/ledger authority. Forbidden claims remain `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, established nonlinear RCG-002, general semiclassical/classical/noisy no-go, family-wide uniqueness, or green-CI-as-physics. Readiness 66%; theory established 0%.
