# RCG-002 / RSC-CSA1 terminal — closed-source action proposal pre-outcome gate

Classification: `BLOCKED_SOURCE_ACTION_OBJECT_UNDERDEFINED`

Secondary structural result: `CLOSED_VARIATIONAL_SOURCE_RULE_NOT_UNIQUE_WITHOUT_CONSTITUTIVE_CURVATURE_COUPLING_RULE_SCOPED`

RSC status after gate: `NEAR_SURVIVOR_NOT_SELECTED`

Starting authority: `063d3a203e370e417fc5325aa1d12f557fea35b3`
Preregistration: `49a1a84ff03bab1c3fb84290423a68a426918c9c`

No `chi_ABC`, connected phase/noise, novelty observable, preferred nonlinear coefficient, or held-out connected outcome was computed or used.

## STATE READ

The starting recovery front required `RSC_CLOSED_SOURCE_ACTION_PROPOSAL_PREOUTCOME_GATE` after SSE1 established:

- G97 closed total-momentum bookkeeping does not define a unique local stress;
- conserved improvements can change the actual linearized carrier coupling;
- no closed probe+apparatus/support action or carrier self-source rule exists in current RCG-002 authority.

The current seed specifies an operational controlled-phase channel and explicitly leaves the microscopic formula for `chi` open. The construction contract requires minimal degrees/dynamics, normalized quantum evolution, causal/gauge discipline and holdout before novelty. The covariant baseline supplies only a linearized spin-2 field coupled to an abstract conserved `T_{mu nu}`. G97 supplies closed classical preparation bookkeeping, not a covariant local matter action.

No newer authoritative automation or GitHub Actions result superseded SSE1 before CSA1 began.

## TARGET HYPOTHESIS

Test whether current RCG-002 commitments already select a specific closed-system source/action constitution, or whether a new constitutive principle is still required.

## FROZEN FRAMEWORK

The preregistration froze `CVS` — Closed Variational Source:

> the physical RSC source must be obtained by varying the same closed action/constitutive functional that generates the probe+apparatus/support preparation, and any carrier self-source must belong to the same prospectively specified variational/constraint constitution.

CVS was not assumed to be sufficient.

## FROZEN FALSE-POSITIVE CALIBRATION

The preregistration froze the synthetic covariant family

`S_xi[g,phi] = Integral sqrt(-g) [ -1/2 g^{mu nu} partial_mu phi partial_nu phi - V(phi) - 1/2 xi R phi^2 ] d^4x`.

This family is a mathematical calibration only. It is not an RCG-002 probe ontology and is not imported candidate dynamics.

The purpose was to test whether the generic rule

`closed covariant action -> Hilbert stress by metric variation`

is by itself a unique physical source selector.

## EXACT CALIBRATION DERIVATION

Use the Hilbert definition

`T_{mu nu} = -(2/sqrt(-g)) delta S_m / delta g^{mu nu}`

with the frozen sign convention in the displayed action.

For the nonminimal term

`S_nm = -(xi/2) Integral sqrt(-g) R phi^2 d^4x`,

metric variation gives the standard geometric identity

`Delta T_{mu nu}^{(xi)} = xi [ G_{mu nu} phi^2 + (g_{mu nu} Box - nabla_mu nabla_nu) phi^2 ]`.

On exactly flat spacetime,

`g=eta`, `R=0`, `G_{mu nu}=0`,

so two values `xi_1`, `xi_2` have identical flat-space matter equations because the `xi R phi` contribution to the matter equation vanishes, while their stress tensors differ by

`T_{mu nu}^{(xi_2)} - T_{mu nu}^{(xi_1)}`

`= Delta xi (eta_{mu nu} Box - partial_mu partial_nu) phi^2`,

where `Delta xi = xi_2-xi_1`.

This difference is identically conserved on the flat background:

`partial^mu [ (eta_{mu nu} Box - partial_mu partial_nu) F ] = 0`

for any sufficiently regular scalar `F`, by commutation of partial derivatives.

Thus the frozen covariant action family has:

1. the same exact flat-space matter dynamics for all `xi`;
2. the same flat-space translation symmetry structure;
3. stress tensors differing by the same conserved-improvement type isolated in RSC1/SSE1.

## CARRIER-COUPLING CHECK

Couple the linearized carrier in the inherited baseline form

`I_int = (1/2) Integral h^{mu nu} T_{mu nu} d^4x`.

The difference between two `xi` values is

`Delta I_int = (Delta xi/2) Integral h^{mu nu} (eta_{mu nu} Box - partial_mu partial_nu) phi^2 d^4x`.

After boundary-controlled integration by parts,

`Delta I_int = -(Delta xi/2) Integral phi^2 R1[h] d^4x`,

where

`R1[h] = partial_mu partial_nu h^{mu nu} - Box h`.

SSE1 already established that `R1[h]` is gauge invariant under the inherited flat-background linearized gauge transformation and is not identically zero.

Therefore the action-level ambiguity is not removed merely by:

- using a covariant action;
- defining stress by metric variation;
- requiring flat-space conservation;
- matching the same flat-space matter dynamics.

The generic CVS framework does not select `xi`.

## WHAT THIS DOES AND DOES NOT PROVE

The calibration does **not** prove that the physical RCG-002 probe/apparatus system is a scalar field or possesses exactly the displayed `xi R phi^2` operator.

It proves a narrower and relevant statement:

> A rule that says only “write a closed covariant action and use its Hilbert stress” is not a unique source-selection principle. Additional constitutive information specifying the physical degrees and their permitted curvature couplings is required.

Because current RCG-002 authority does not specify the actual probe+apparatus/support field ontology/action at all, it also supplies no candidate-owned rule selecting the analogue of `xi=0`, `xi!=0`, or another improvement representative.

Choosing “minimal coupling” by name would therefore add new model-defining information. It may be proposed prospectively in a later gate, but it is not derived by current authority.

## CURRENT REPOSITORY OBJECT AUDIT

### Seed

`candidates/RCG_002_RELATIONAL_CONTROLLED_PHASE_CHANNEL.md` defines relational two-level probes and the operational channel. It explicitly leaves the microscopic source/distance/time/`G`/`hbar` dependence of `chi` to a future candidate. It does not define a covariant probe/apparatus action.

### Construction contract

`docs/CONSTRUCTION_CONTRACT.md` requires the search order `requirements -> formal constraints -> minimal degrees -> minimal dynamics -> observable map`. It does not fix the source degrees or a minimal-coupling rule.

### Covariant baseline

`candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md` takes a symmetric conserved `T_{mu nu}` as input and supplies linearized spin-2 dynamics. It explicitly has no nonlinear metric completion or nonlinear self-source action.

### G97

`results/ITER095_G97_CLOSED_TOTAL_SOURCE_PREPARATION_TERMINAL.md` gives a closed probe+apparatus mechanics model with exact total momentum conservation. It does not provide the covariant local action or metric variation defining a unique `T_{mu nu}`.

### RSC1/SSE1

These results localize the same missing object: a same-realization source constitution plus a separate positive operational influence/state law.

No current authority closes that gap.

## PASS CHECK

The frozen PASS `RSC_CLOSED_SOURCE_ACTION_PRINCIPLE_SELECTED_PREOUTCOME` is **not met**.

Missing mandatory items:

- actual physical source degrees/ontology for the probe+apparatus/support realization;
- complete closed source action or equivalent constitutive functional;
- candidate-owned rule fixing admissible curvature/nonminimal couplings or a proven physical quotient;
- carrier nonlinear action/self-source rule in the same constitution.

## FAIL CHECK

The stronger frozen FAIL `CURRENT_RCG002_COMMITMENTS_DO_NOT_SELECT_CLOSED_SOURCE_ACTION_SCOPED` is not used as the aggregate classification because the scalar calibration is deliberately synthetic rather than the actual RCG-002 source realization.

It is sufficient to falsify the generic claim that metric variation of an unspecified covariant action automatically supplies a unique source, but it does not by itself constitute two fully realized RCG-002 probe+apparatus models.

Therefore the correct aggregate status is `BLOCKED`, not a universal/scoped physical no-go.

## FINAL CLASSIFICATION

`BLOCKED_SOURCE_ACTION_OBJECT_UNDERDEFINED`

with structural sub-result

`CLOSED_VARIATIONAL_SOURCE_RULE_NOT_UNIQUE_WITHOUT_CONSTITUTIVE_CURVATURE_COUPLING_RULE_SCOPED`.

## NEW SCIENTIFIC FACT

The source-side RSC problem is now one layer sharper than SSE1:

- SSE1: conservation/global closure and stress-equivalence claims do not select the local source;
- CSA1: even adding the generic variational/Hilbert-stress prescription does not select the source unless the physical source ontology and allowed curvature couplings are fixed prospectively.

The missing datum is therefore not merely “an action exists.” It is a **candidate-owned source constitution**: physical degrees + permitted local couplings + source derivation + carrier self-source rule.

## COMPLETION SPACE / SELECTION RANK

Physical nonlinear completion space remains `UNDEFINED`.

Physical selector rank remains `UNDEFINED_PHYSICAL_MAP_MISSING`.

The synthetic `xi` direction is a calibration coordinate, not a claimed physical RCG-002 completion coordinate.

## CLAIM CEILING

CSA1 does not establish:

- impossibility of an RSC source action;
- uniqueness/nonuniqueness of all gravitational source definitions;
- full nonlinear Bianchi/diffeomorphism closure;
- quantum positivity or state/measure closure;
- a connected three-source phase;
- new physics or quantum gravity.

Programme readiness remains 66%; theory established remains 0%.

## EXACT NEXT GATE

`RSC_SOURCE_CONSTITUTION_PRINCIPLE_TRIAGE_PREOUTCOME_GATE`.

Before any connected outcome, freeze a small set of independently motivated candidate-owned constitutive rules for the physical closed source, and compare them only on pre-outcome criteria.

The next gate must decide whether any rule can prospectively fix:

1. the probe/apparatus/support physical degrees;
2. which local curvature/nonminimal couplings are permitted;
3. how those coefficients are fixed independently of gravitational connected outcomes;
4. the derived local total stress/source;
5. the carrier self-source/action relation;
6. weak-field baseline recovery;
7. conservation/constraint propagation.

A rule such as “minimal coupling” may be considered only as an explicitly new prospectively motivated principle. It may not be smuggled in as a convention or selected because it gives a convenient `chi_ABC`.

Even a future source-side PASS does not remove the independent `BLOCKED_POSITIVE_INFLUENCE_INTERFACE_MISSING_DATUM` from RSC1.

`chi_ABC` remains unauthorized.
