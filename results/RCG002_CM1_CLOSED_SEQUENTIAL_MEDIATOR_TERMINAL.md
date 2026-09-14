# RCG002-CM1 — closed sequential mediator realization — TERMINAL

Date: 2026-09-14
Status: terminal scoped structural result; no physical nonlinear gravitational law selected.

## STATE_READ

Starting authoritative main: `613713ced67058e0010cc44ede60955ec455fdb7`, terminal NP1 state.

Before CM1, NP1 had established `RCG002_CURRENT_PRINCIPLES_ALLOW_CONTINUUM_CONNECTED_CHANNEL_EXTENSIONS_SCOPED` and overall `RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE`: normalized CPTP evolution, exact recovery of all one-/two-source coordinate faces, lower-body rephasing quotient, G97 total-translation compatibility, and an abstract finite-time evolution still leave the connected phase/noise extension nonunique.

The seed itself states that no microscopic formula for `chi` is asserted and that source/distance/time/G/hbar dependence must be derived rather than fitted. The construction contract requires minimal dynamics and causal/consistency gates. The covariant baseline remains linearized and leaves nonlinear diffeomorphism/Bianchi closure unresolved. No post-NP1 automation run had produced a newer durable GitHub scientific authority before CM1 was preregistered.

## CURRENT_FRONT BEFORE CM1

`NEW_CANDIDATE_VERSION_PRINCIPLE_FRONTIER` with physical selector rank `UNDEFINED_PHYSICAL_MAP_MISSING`, readiness 66%, theory established 0%.

CM1 tests one narrower possible structural rescue before inventing a new candidate version: whether demanding a single explicit closed sequential mediator, interacting with each source only through source-mediator two-body controls and returning to the same final state, is already enough to select the connected phase.

## PREREGISTRATION / PRODUCTION / PROVENANCE

Prospective contract: `1e1c6556b42769cb1d0ce67e964c7f151351ec1c`, `prereg/RCG002_CM1_CAUSAL_MEDIATOR_REALIZATION_NONUNIQUENESS.md`.

Implementation: `74caef5d4bba0a6a7106f68ab2efc3f44a543744`, `scripts/rcg002_cm1_closed_mediator.py`.

Production head: `6f45a31a3259000a3e3b832f616c03d74563767b`, workflow `.github/workflows/rcg002_cm1.yml`, run `34861269613`, attempt 1.

Jobs A/B/C/D/aggregate: `104033804455 / 104033804121 / 104033804463 / 104033804464 / 104033938938`.

All four scientific lanes completed before the aggregate was consumed. The matrix used `max-parallel=4`, `fail-fast=false`. No competing production run and no post-hoc change of mediator dimension, primitive set, ordering, face predicates, or interpretation ceiling was used.

Artifacts and independently recomputed ZIP SHA256:

- A `10355225608`: `c3546d9d8260833c60dc14dad171b1c9e72621b7f67f3401997ca801ecd57d08`;
- B `10354464514`: `05e02a2cc84a36745404b952f771c411346ca988a8f19df22cc48c2f1a06f0b3`;
- C `10354769236`: `45a24e7ed51af79045d90cf61e91acfbddc3bdaa3b63aec96905d74d16ba014e`;
- D `10354469412`: `cb9e3eb013d71125f06fc9da774e124448c14a5f6bcdc0b8525a0212b67a3b7d`;
- aggregate `10354769307`: `3a042de0435f945d54f446732562d15cbd042a80cbeb3f36333ecbf9bc927c02`.

Raw JSON SHA256 A/B/C/D/aggregate:
`88febeabe1fa1f11d166fddeed0a4b0ac393ebe3d4a9c6f717bb9ee8fe2e523e / 5bf445a1c6bfb0e2b9b1c6f9d2899e1bb2c8c7327ff9a8084eea85783e65b619 / 744b9a910af8f69427e3d4e1b3e2edcb0631ed07d0fa41483dcb1984b5c2c02c / 1d72f59710abf19416d501d55349ccbbd9449c70111c352ec7b1aff7f76feb6f / 91728aabcedfe2841c789c1bf50e5b9a5a9d16fee5c2edc8be551bd0a21037bf`.

Every individual raw lane object equals the corresponding lane embedded in the aggregate. Verified durable summary: `results/raw/RCG002_CM1_RAW_SUMMARY.json`, commit `391c4920438900414a3d885c4ac03882eb65fc72`.

## CORE_PROBLEM

NP1 used an abstract connected projector/random-unitary construction. A natural objection is that such a connected factor may disappear once a single mediator must acquire information sequentially from A, B, C and then close back to a branch-independent state.

CM1 therefore asks whether **closed sequential mediation itself is a selection principle**.

## FROZEN MEDIATOR OBJECT

Three binary branch labels `a,b,c in {0,1}` and a four-level mediator `M` initialized in `|0>`.

Let

`S|m> = |m+1 mod 4>`

and define for X=A,B,C the source-mediator two-body controlled shift

`V_X = |0><0|_X tensor I_M + |1><1|_X tensor S_M`.

The frozen sequence is

`V_A -> V_B -> V_C -> P_lambda -> V_C^{-1} -> V_B^{-1} -> V_A^{-1}`

with mediator-only

`P_lambda = diag(1,1,1,exp(i lambda))`.

There are no direct A-B, A-C, B-C gates and no primitive three-source gate. `lambda` is symbolic and remains an adversarial calibration parameter, not candidate physics.

## DERIVATION — EXACT SOURCE ACTION

For a computational branch `(a,b,c)`, the first three controlled shifts put the mediator in

`|a+b+c>`

because `a+b+c` lies in `{0,1,2,3}` and therefore no wrap occurs before the phase gate.

`P_lambda` acts nontrivially iff `a+b+c=3`, which for binary labels is equivalent to

`a*b*c = 1`.

The reverse shifts then give

`|a+b+c> -> |0>`

for every branch. Hence exactly

`U_CM1 |a b c>|0>_M = exp(i lambda a b c) |a b c>|0>_M`.

The mediator is not merely traced out: it returns to the **same pure state** for all eight branches. Thus it contains no final which-branch record and the induced source map is the coherent diagonal unitary

`diag(1,1,1,1,1,1,1,exp(i lambda))`

in branch order `000,...,111`.

Lane A checked all eight trajectories exactly and obtained phase-exponent vector

`(0,0,0,0,0,0,0,1)`

with exact bus reset on every branch for arbitrary real `lambda`.

## LOWER-FACE RECOVERY / CONNECTED PHASE

On each coordinate face `a=0`, `b=0`, or `c=0`, the product `abc` vanishes. Therefore the CM1 multiplier is exactly the identity on every one-/two-source lower face.

The binary third finite difference of the induced phase is

`Delta_A Delta_B Delta_C [lambda a b c] = lambda`.

Lane B independently checked that the same third finite difference is zero for every basis element

`1, a, b, c, ab, ac, bc`.

Therefore the arbitrary CM1 connected phase cannot be removed by any <=2-body phase redefinition already killed by the connected quotient.

The negative controls behaved prospectively as required:

- omitting A, B, or C together with its inverse makes the full multiplier identity and the third difference zero;
- putting the bus-only phase on level `|2>` instead of `|3>` changes all three lower two-source faces and gives third-difference coefficient `-3`, so it fails lower-face preservation;
- `lambda=0` is the identity control.

## UNITARITY / MEDIATOR CLOSURE / PRIMITIVE LOCALITY

Lane C constructed the exact cyclic-shift and controlled-shift matrices. It verified:

- `S^dagger S = I` exactly;
- each controlled shift has its exact inverse;
- `P_lambda` is unitary for real `lambda`;
- every source-dependent primitive acts on exactly one source label plus the mediator;
- the mediator returns to `|0>` for all branches;
- no residual branch record remains in the mediator.

The full source+bus computational dimension is 32, but the elementary source-dependent primitive is only a 2 x 4 = 8 dimensional source-bus gate.

This satisfies the frozen **operational** closed-mediator requirement. It does not make the mediator gravitational.

## G97 TRANSLATION BOOKKEEPING

If the internal branch labels and the mediator carry no spatial translation charge, each CM1 primitive has the tensor-product form

`I_spatial tensor U_label,bus`.

It therefore commutes with the already validated G97 total spatial translation generator acting on the probe+apparatus coordinate factor.

This is only the same total-translation bookkeeping prerequisite used in NP1. It is NOT energy conservation, nonlinear stress-energy conservation, diffeomorphism covariance, or Bianchi closure.

## CIRCUIT CAUSALITY AUDIT

The frozen sequence is explicitly finite and ordered. However, Lane D finds an important qualification: all controlled shifts are powers of the same Abelian cyclic shift, so reversing the order of the uncompute operations leaves the final operation unchanged and still resets the bus.

Thus CM1 does **not** provide a meaningful relativistic ordering theorem.

What is order-sensitive is the location of `P_lambda`: moving the phase gate before the C interaction means that the mediator has seen at most two active sources, never reaches level `|3>` at the phase event, and the connected third difference becomes exactly zero.

Accordingly the only justified causality label is

`FINITE_ORDERED_CIRCUIT_CAUSALITY_ONLY`.

No relativistic microcausality, finite propagation speed, retarded spacetime Green function, or light-cone support has been established.

## WHY THIS IS A NONUNIQUENESS RESULT, NOT A CONSTRUCTION OF PHYSICS

The mediator architecture can realize a connected phase for every real `lambda`, but nothing in the frozen RCG-002 principles selects the mediator level-3 phase itself.

Equivalently, a bus Hamiltonian capable of generating `P_lambda` would have to contain a new rule fixing its level-3 phase accumulation. That rule is precisely additional dynamical information. CM1 therefore converts the informal statement “perhaps an explicit mediator will fix the interaction” into an exact counterexample: **mediator closure and two-body source-bus realizability do not fix the interaction strength or phase law.**

The bus is an adversarial calibration object. It is not a proposed graviton, geometry variable, reference field, or hidden gravitational sector.

## PHYSICAL_NONLINEAR_COMPLETION_SPACE

Still **undefined**.

CM1 identifies no physical gravitational field variables, no source-history quotient, no field-redefinition quotient, and no nonlinear source-accessibility theorem. It therefore does not assign a dimension to the physical nonlinear completion space.

The surviving continuum is an operational mediator-realization freedom only.

## CANDIDATE_OWNED_DYNAMICAL_OBJECT

None is derived by CM1.

The exact source-bus unitary is `ALLOWED_BUT_NOT_SELECTED`, not `DERIVED_FROM_RCG002`. In particular, `P_lambda` and its `lambda` are deliberately unfixed calibration structure.

The seed's actual missing candidate-owned object remains a nonlinear source/state/evolution law that derives the connected phase/noise hierarchy from physical sources and spacetime dynamics.

## CONSERVATION_CHECK

Passed only at the inherited G97 total-spatial-translation bookkeeping level under the frozen assumption that label/bus operations are translation-neutral.

Not established:
- energy conservation;
- nonlinear `nabla_mu T^{mu nu}=0` in a physical spacetime realization;
- apparatus stress closure in a dynamical gravitational field;
- source equations compatible with a nonlinear field equation.

## BIANCHI / DIFF CHECK

`BLOCKED / NOT DEFINED` for CM1.

There is no candidate-owned nonlinear metric/connection/relational field equation in CM1, hence no meaningful nonlinear Bianchi identity or constraint-propagation theorem to test. Passing the finite mediator gate cannot substitute for this missing object.

## CTP / RETARDED CHECK

The final mediator state is branch-independent, so the frozen coherent operational map has exact unitary normalization and no final mediator which-path record.

This does not establish a spacetime CTP influence functional, retarded field response, largest-time equation, or relativistic causal support. The proper classification remains finite ordered circuit only.

## GAUGE / REPARAMETERIZATION CHECK

The connected Boolean third difference annihilates all <=2-body branch phase functions and therefore preserves the established lower-body rephasing quotient. The bus phase changes this connected invariant by `lambda`.

No spacetime gauge quotient is defined, so no stronger gauge-invariance claim is authorized.

## BASELINE DEGENERACY CHECK

CM1 is not a discriminator against classical GR, semiclassical gravity, stochastic gravity, gravitational EFT, or hybrid mediator theories. It is purely a structural adversarial witness.

A nonzero connected phase generated by this bus would therefore have no novelty interpretation. It only demonstrates that mediator realizability cannot be used as a selector by itself.

## SELECTOR_RANK

`UNDEFINED_PHYSICAL_MAP_MISSING`.

Operationally, CM1 shows one explicit continuous connected-phase coordinate survives the new mediator requirement. This is not a physical selector rank because `lambda` has no candidate-owned source/evolution map.

## ADVERSARIAL COUNTEREXAMPLES / CONTROLS

1. **All-real-lambda family** — exact closed bus realization for a continuum of connected phases with identical lower faces.
2. **Missing-source controls** — removing any source interaction kills the connected phase exactly.
3. **Wrong bus level** — level-2 phase contaminates two-source faces and is rejected.
4. **Early phase placement** — applying the phase before the third source is encountered kills the three-source connected contribution.
5. **Uncompute-order qualification** — reverse uncompute gives the same operation because the bus shifts commute; thus the architecture does not manufacture a false relativistic order claim.

## RESULT

`NONUNIQUENESS_SURVIVES_CLOSED_SEQUENTIAL_MEDIATOR_SCOPED`.

The preregistered hypothesis that explicit closed sequential mediation plus exact mediator reset could by itself select the connected phase is falsified in the frozen operational architecture.

Overall physical classification remains:

`RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE`.

## NEW_SCIENTIFIC_FACT

The NP1 underdetermination survives a strictly stronger operational realizability requirement: the connected phase can be generated by a **single finite mediator**, with no direct source-source gate, only source-mediator two-body controls, exact unitary primitives, exact reset to the same final mediator state, exact preservation of every lower source face, and compatibility with inherited total-translation bookkeeping.

Therefore “introduce a closed mediator” is not by itself a dynamical selection principle for RCG-002.

The missing information has been narrowed further: it must involve physical spacetime/source dynamics or another genuinely candidate-owned principle that fixes the mediator/field response, not merely the existence of an ancilla or causal-looking circuit.

## WHAT IS STILL NOT ESTABLISHED

- a physical source-to-field/history map;
- candidate-owned nonlinear field/state degrees of freedom;
- spacetime locality or relativistic microcausality;
- nonlinear stress-energy conservation;
- Bianchi/diffeomorphism/constraint closure;
- a positive physical influence kernel derived from those dynamics;
- a derived connected phase/noise hierarchy;
- a physical completion quotient or its dimension;
- discrimination from standard classical/semiclassical/EFT nonlinearities;
- any new physics or full quantum-gravity claim.

## CLAIM CEILING

CM1 is a finite-dimensional operational nonuniqueness witness only. It is not an all-mediators theorem and not a theorem about local relativistic field theories. It does not forbid a future RCG-002 version whose genuine physical dynamics selects a unique nonlinear response.

Readiness remains 66%. Theory established remains 0%.

## EXACT_NEXT_ADMISSIBLE_GATE

The next gate is still the **NEW CANDIDATE VERSION PRINCIPLE GATE**, now with a sharper exclusion:

Do not propose “there is a mediator” or “the mediator closes” as the new principle. CM1 shows those conditions leave `lambda` arbitrary.

A prospectively new RCG-002 version must instead supply exactly one independently motivated physical rule that fixes or dynamically derives the response. Before any connected-phase outcome is inspected it must specify:

1. physical field/state degrees of freedom;
2. the G97 closed total-source -> physical field/history map;
3. a nonlinear causal evolution equation or influence/state law;
4. nonlinear conservation and Bianchi/constraint compatibility;
5. spacetime retarded/microcausal structure appropriate to its scope;
6. a positive normalized influence kernel or justified coherent/noisy factorization;
7. recovery of the validated pairwise weak-field normalization;
8. connected phase/noise observables derived without fitting `lambda`, `gamma`, or an equivalent free connected coefficient.

If no such principle can be motivated independently from RCG-002, the correct terminal status for the current version is `RCG002_CURRENT_VERSION_NONLINEAR_DYNAMICS_UNDERDETERMINED` and any added dynamics must be labeled a prospectively new candidate version rather than a repair of the existing seed.
