# RCG002-NP1 — connected-channel extension nonuniqueness theorem — TERMINAL

Date: 2026-09-14
Status: terminal scoped structural result; physical nonlinear evolution remains undefined.

## STATE_READ
Frozen starting main: `94467fdacc93f65102333fa01b7a34bb0d857a79`.
Current authoritative frontier before NP1: G97 closed total-source preparation plus NCP1 positivity restrictions/nonuniqueness, with `BLOCKED_PHYSICAL_EVOLUTION`, selector rank `UNDEFINED_PHYSICAL_MAP_MISSING`, readiness 66%, theory established 0%.

The RCG-002 seed explicitly states that no microscopic formula for `chi` is asserted and that future source/distance/time/G/hbar dependence must be derived rather than freely fitted. The covariant baseline states that no form of `Delta Gamma` is chosen. The current recovery and NCP1 authority state that no candidate-owned nonlinear law exists. NP1 does not modify those prior verdicts.

## TARGET
Test whether the already-authoritative operational channel constraints, normalized CPTP evolution, preservation of all lower-order coordinate faces, and G97 total-translation compatibility are sufficient to fix the connected three-source nonlinear channel.

This is not a search over preferred coefficients. It is a sufficiency theorem: if a continuum of inequivalent extensions satisfies all those frozen requirements, then current RCG-002 principles cannot determine the nonlinear continuation without a new principle.

## PREREGISTRATION / PRODUCTION
Preregistration: `1c63d49ccfbc0978c0d791fabd335a00186fa4f4`, `prereg/RCG002_NP1_CONNECTED_CHANNEL_EXTENSION_NONUNIQUENESS.md`.
Implementation: `85f858b693d2d97ff3ba5c6f2adce733b1bb5c94`, `scripts/rcg002_np1_connected_extension.py`.
Production head: `aec4224051ec7858a5ac47e4c6f2b5cde2ddbcf2`, workflow `.github/workflows/rcg002_np1.yml`, run `34816931926`, attempt 1.
Jobs A/B/C/D/aggregate: `103889466939 / 103889467028 / 103889466952 / 103889466721 / 103889592848`.
All four scientific lanes completed before aggregate evaluation. `max-parallel=4`, `fail-fast=false`. No competing production run and no post-hoc criterion change.

Artifacts:
- A `10335754857`, ZIP SHA256 `d0a9d337dbf14718f48872b11d623b04dff64b7cf5f0b0def3ee6ecf24a944fc`;
- B `10336587388`, ZIP SHA256 `18e295ca9f62796f30ce8dc250ca60685473d1496b8b3b0f4b4cb6f8c6507ac8`;
- C `10337465262`, ZIP SHA256 `d57f661fe66f993ab0cc8ad04f099fed5802f9500cb5886643b8945db21adb26`;
- D `10337395169`, ZIP SHA256 `14f6d95f92695fbf967b51604412a93e2836beda2490cc2a026242c56a2bc3d0`;
- aggregate `10337205608`, ZIP SHA256 `4b0b7d101410d21824400b13e4f14a5797e4336545659b05a5281602d29728c1`.

All five ZIP digests were independently recomputed after completion and match GitHub. Raw A/B/C/D JSON files exactly equal the corresponding objects embedded in the aggregate. Durable archive: `results/raw/RCG002_NP1_RAW_BUNDLE.json`, commit `772ca5b3d8c82fc3f303d48dea40023e1f42fbe6`.

## FROZEN FAMILY
Branch cube `B={0,1}^3`; for branch `x=(a,b,c)`, define

`q(x)=a*b*c`.

Let `F0` be any normalized positive-semidefinite Schur kernel on the eight branch labels whose restrictions to the three lower coordinate faces reproduce the already-fixed lower-order channel.

For arbitrary real `lambda` and `gamma>=0`, define

`C_lambda,gamma(x,y)=exp(i lambda [q(x)-q(y)]) exp(-gamma [q(x)-q(y)]^2)`

and

`F_lambda,gamma = F0 .* C_lambda,gamma`.

The family is an adversarial mathematical completion. It is not proposed as gravity.

## LANE A — POSITIVITY / CPTP THEOREM
Seven cube vertices have q=0 and exactly one, `111`, has q=1. Put `r=exp(-gamma)`, hence `0<r<=1` for finite gamma>=0. Removing the diagonal phase congruence leaves a real correlation kernel whose only nonzero sector after quotienting the six redundant q=0 directions is

`[[7, sqrt(7) r], [sqrt(7) r, 1]]`.

Its trace is 8 and determinant is exactly

`7(1-r^2)>=0`.

Equivalently, the two q-sector Gram vectors can be chosen as

`v0=(1,0)`,
`v1=(r, sqrt(1-r^2))`.

Thus the real damping kernel is PSD. Multiplication by `D_x=exp(i lambda q(x))` is a diagonal unitary congruence and preserves PSD. Therefore `C_lambda,gamma` is PSD with unit diagonal for every real lambda and gamma>=0.

By the Schur product theorem, if `F0>=0` then

`F_lambda,gamma = F0 .* C_lambda,gamma >=0`.

The unit diagonal is preserved. Therefore the multiplier defines a normalized Schur channel and maps every admissible base Schur channel to another admissible normalized Schur channel.

Positive control: gamma=0 makes C rank one and exactly a diagonal-unitary phase difference. Negative control: the frozen unit-diagonal matrix `[[1,1,1],[1,1,-1],[1,-1,1]]` has determinant -4 and correctly fails PSD.

This is an operational complete-positivity statement, not a relativistic gravitational consistency theorem.

## LANE B — EXACT LOWER-FACE PRESERVATION AND MOEBIUS INVARIANT
On any of the coordinate faces `a=0`, `b=0`, or `c=0`, q vanishes on every branch state in that face. Hence

`C_lambda,gamma(x,y)=1`

identically within every frozen lower face, for all lambda and gamma. Therefore all one-/two-source face restrictions of `F0` are preserved exactly.

For the connected phase function

`phi_conn(a,b,c)=lambda*a*b*c`,

the binary third finite difference is

`Delta_A Delta_B Delta_C phi_conn = lambda`.

For the most general constant + one-body + two-body polynomial

`c0 + cA a + cB b + cC c + cAB ab + cAC ac + cBC bc`,

the same third finite difference is exactly zero. Therefore lambda cannot be removed by the lower-body phase/rephasing quotient already annihilated by `chi_ABC`.

At the `111 <-> 000` coherence, lambda changes phase while gamma changes log-magnitude. The exact observable-coordinate Jacobian is

`[[1,0],[0,-1]]`,

with determinant -1. Hence the two directions are linearly independent at the operational-channel level.

This establishes an **operational extension-space lower bound of two dimensions** in the frozen family. It does not establish a two-dimensional physical gravitational quotient.

## LANE C — G97 TRANSLATION COMPATIBILITY AND FINITE-TIME EVOLUTION
Let `Q=|111><111|` act only on internal branch labels and let `P_tot` be the G97 common spatial translation generator acting on the closed probe+apparatus coordinates. On the tensor-product space,

`[P_tot,Q]=0`

exactly. Thus the connected multiplier can preserve the same total-translation generator closed by G97. This is stronger than merely preserving the two-source faces, but it is still not nonlinear stress-energy conservation.

A finite laboratory-time connected phase can be produced abstractly by

`H(t)=6 lambda t(1-t) Q`, `0<=t<=1`,

whose integral is exactly lambda. Since all H(t) are proportional to Q, time ordering produces `exp(i lambda Q)` up to the chosen sign convention.

For an independent real Gaussian random variable X with variance `2 gamma`, averaging the diagonal unitary `exp(i X Q)` gives

`E exp(i X Delta q)=exp(-gamma Delta q^2)`.

Therefore the entire connected factor has an explicit finite-time random-unitary CPTP realization. This proves that **ordinary normalized finite-time operational evolution plus total translation symmetry still does not select lambda or gamma**.

It does NOT prove relativistic microcausality, locality, Bianchi closure, or a physical gravitational mediator. The construction is deliberately an adversarial completion, not a rescue model.

## LANE D — CANDIDATE-OWNERSHIP AUDIT
All frozen authority predicates passed:
- seed: no microscopic formula for chi is asserted;
- seed: future dependence must be derived, not fitted;
- construction contract: minimal dynamics is a required construction layer;
- covariant baseline: no form of Delta Gamma is chosen;
- recovery: no candidate-owned nonlinear law exists;
- recovery: `RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE` remains an allowed/active conclusion;
- NCP1: physical evolution remains blocked;
- NCP1: new nonlinear principle remains required if no native law is found.

Ownership classification:

`DERIVED_FROM_RCG002`
- normalized operational quantum evolution;
- relational controlled-phase quotient architecture;
- recovery of validated lower-order weak-field branch;
- closed total-source translation/conservation prerequisite from G97.

`ALLOWED_BUT_NOT_SELECTED`
- connected phase lambda;
- connected dephasing gamma;
- other positive higher-order channel completions.

`REQUIRES_NEW_PRINCIPLE`
- microscopic nonlinear source/state/evolution law;
- a rule fixing the connected phase/noise hierarchy;
- nonlinear stress-energy/Bianchi/constraint completion;
- a physical source-to-branch-history and spacetime-causal realization.

The marker audit is supporting provenance. The nonuniqueness theorem itself comes from lanes A-C and does not depend on absence-by-text alone.

## PHYSICAL_NONLINEAR_COMPLETION_SPACE
Still **undefined**. NP1 does not identify the physical gravitational completion quotient, its dimension, field-redefinition classes, or source accessibility. It establishes only that the current operational constraints admit at least two independent connected-channel directions before a gravitational source/evolution principle is supplied.

Therefore it is invalid to convert the operational lower bound `>=2` into a physical selector dimension.

## SELECTOR_RANK
`UNDEFINED_PHYSICAL_MAP_MISSING`.

The phase lambda would be directly visible to a connected phase contrast and gamma to a connected coherence-magnitude contrast, but neither is a candidate-owned prediction. Observability of a freely choosable channel coordinate is not selection of gravitational dynamics.

## ADVERSARIAL CONSEQUENCE
Any admissible lower-order Schur channel `F0` can be multiplied by the entire `C_lambda,gamma` continuum without changing any frozen lower coordinate face. The connected phase coordinate is invariant against every <=2-body rephasing, and the connected dephasing coordinate cannot be absorbed into that phase. Both preserve the G97 total-translation generator in the frozen internal-label construction.

Consequently the following requirements are jointly insufficient to fix nonlinear RCG-002 evolution:
1. lower-order controlled-phase data;
2. normalized CPTP Schur evolution;
3. exact one-/two-source face recovery;
4. lower-body phase quotient invariance;
5. G97 total-translation compatibility;
6. existence of an abstract finite-time normalized evolution.

Adding these constraints cannot determine the desired `chi_ABC` prediction because lambda remains arbitrary.

## RESULT
`RCG002_CURRENT_PRINCIPLES_ALLOW_CONTINUUM_CONNECTED_CHANNEL_EXTENSIONS_SCOPED`.

Overall physical classification:

`RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE`.

This is stronger than merely saying that a coefficient has not yet been computed: a continuum of inequivalent operational extensions survives all tested current principles. The missing information is genuinely dynamical/source information, not another algebraic rank or positivity constraint of the same type.

## NEW_SCIENTIFIC_FACT
Within the current RCG-002 architecture, even exact complete positivity, exact preservation of all lower-order faces, invariance of the connected phase against lower-body rephasings, G97 total-translation compatibility, and a finite-time CPTP realization do not determine the nonlinear connected channel. At least two independent operational directions survive: connected phase and connected dephasing.

Therefore the present RCG-002 object is rigorously shown, in this scoped operational sense, to be **an underdetermined nonlinear interface architecture rather than a physically determined nonlinear theory** unless a new candidate-owned principle is added.

This is a programme-internal theorem; no claim of literature novelty is made.

## CLAIM CEILING
No all-theories nonuniqueness theorem; no rejection of future RCG-002 versions; no gravitational realization of the adversarial family; no nonlinear Bianchi/diffeomorphism closure; no spacetime causality theorem; no unique physical completion dimension; no new physics; no full quantum gravity.

Readiness remains 66%. Theory established remains 0%.

## EXACT NEXT ADMISSIBLE GATE
A **candidate-version principle gate**, not another channel-parameter scan.

Before any new coefficient is evaluated, propose exactly one independently motivated candidate-owned nonlinear source/state/evolution principle and freeze:
- physical degrees of freedom and source map on the closed G97 system;
- state/evolution law;
- conservation and nonlinear Bianchi/constraint compatibility;
- causal/retarded structure;
- positive influence kernel or coherent factorization/noise rule;
- lower-order recovery;
- the prediction for connected phase/noise observables.

The new principle must fix or dynamically derive the NP1 lambda/gamma freedom rather than set it by convention. If no independent RCG-002 motivation exists, terminalize the current version as `RCG002_CURRENT_VERSION_NONLINEAR_DYNAMICS_UNDERDETERMINED` and treat any added rule as a prospectively new candidate version.
