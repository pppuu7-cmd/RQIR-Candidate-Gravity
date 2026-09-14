# RCG002-V2P1 — new-version principle proposal and pre-outcome triage — PREREGISTRATION

Date: 2026-09-14
Status: PROSPECTIVELY FROZEN BEFORE ANY CONNECTED-PHASE/NOISE CALCULATION
Starting authority: `b4358c038d319c55370b3fba615b25f6477151b1` (VB1 terminal current-version boundary).

## HYPOTHESIS

The current frozen RCG-002 version is terminally underdetermined at the nonlinear model-definition boundary. A prospectively new version may be opened only if exactly one candidate-owned physical principle survives a pre-outcome triage that does not inspect, optimize, fit, or compare the resulting connected phase/noise prediction.

## DECISION OBJECT

Select at most one principle for a new RCG-002 descendant using only structural/model-definition criteria. This gate does NOT calculate `chi_ABC`, any connected dephasing, any nonlinear coefficient, or any external novelty observable.

If no proposal survives, classify `NO_PREOUTCOME_PRINCIPLE_SELECTED`.
If more than one proposal survives all mandatory criteria without a prospectively justified tie-break, classify `AMBIGUOUS_NEW_VERSION_PRINCIPLE`.
If exactly one survives, authorize only a successor derivation gate for that principle; selection is not a physics PASS.

## INDEPENDENCE FIREWALL

Do not import equations, preferred coefficients, successful nonlinear patches, or candidate dynamics from QGR, MSQGR/CRQN, KMQGB, RQIR, ISQGR, or any other candidate project.

Standard GR/QFT/EFT may be used only after triage as an external comparator/background. Similarity discovered after independent selection does not invalidate the selection, but such similarity cannot be used as a selection argument.

## FROZEN PROPOSALS

### P1 — RSC: Relational Self-Coupling Closure

Retain the already-authoritative linearized spin-2 field/source architecture of RCG-002 baseline v0 and the closed G97 total-source preparation. Add one new version-defining principle:

> The physical gravitational carrier must couple to the closed total source including the carrier's own dynamically generated stress/constraint contribution through the same interaction law, and this self-coupling must close iteratively without introducing new independent nonlinear coupling constants, new fields, or new dimensionful scales beyond the inherited weak-field parameters. The completion must remain local, two-derivative in its classical field equations, reduce exactly to the validated linearized baseline, and admit a gauge/constraint-consistent causal initial-value formulation in its stated domain.

This principle does NOT assume an Einstein-Hilbert action, the Einstein equations, or any connected phase value. Those would be downstream derivation/comparator questions.

### P2 — MPI: Minimum Positive Influence Extension

Keep the source histories operational and define the new nonlinear channel as the normalized positive influence kernel closest to the inherited lower-order kernel under a prospectively fixed information-geometric/Choi-distance criterion, subject to exact lower-face recovery and no-signalling/positivity constraints.

No field equation is supplied a priori. This is intentionally an operational selection proposal.

### P3 — CRM: Closed Relational Mediator Law

Introduce one physical mediator coupled only pairwise to the three relational sources, require exact mediator reset and finite causal ordering, and require the mediator free/internal Hamiltonian to be fixed entirely by the already validated pairwise calibration, with no direct three-source gate.

This is stronger than bare CM1 because it asks pairwise calibration to fix the mediator dynamics; however it may fail if pairwise data do not determine the relevant higher mediator spectrum/matrix elements.

### P4 — CIC: Causal Influence-Cumulant Closure

Take the physical object to be a normalized closed-time-path influence functional on the G97 closed source histories. Require causal/retarded support, positivity/normalization, lower-order recovery, and a recursion in which all higher connected cumulants are fixed by the already-authoritative lower-order response/noise data with no new independent cumulant functions or coefficients.

The recursion itself must be derivable from the RCG-002 relational/operational commitments; an unspecified recursion does not count.

## FROZEN TRIAGE CRITERIA

Each criterion is assessed without computing a connected phase/noise outcome.

C1 — RCG-002 grounding: independently motivated by the existing RCG-002 relational/operational architecture or an already-authoritative missing-obligation frontier, not by a desired result.

C2 — Physical degrees of freedom: identifies a physical field/state/mediator object rather than only an abstract channel selector.

C3 — Closed-source map: provides or canonically inherits a G97 closed total-source -> physical state/history map without omitting apparatus/support bookkeeping.

C4 — Genuine nonlinear generator: supplies a nonlinear evolution/influence mechanism, not only admissibility constraints, a search rule, or the linear/Gaussian baseline.

C5 — Conservation/constraint route: defines an internal route by which nonlinear conservation and gauge/Bianchi/constraint compatibility can be tested in the same realization.

C6 — Causality route: defines a spacetime-retarded/microcausal or otherwise physically causal initial-value notion appropriate to the claimed scope; finite circuit ordering alone is insufficient.

C7 — Positive state/evolution route: defines a route to normalized positive quantum/influence evolution without choosing a connected coefficient from the desired outcome.

C8 — Weak-field recovery: the validated pairwise weak-field branch is recovered by construction or by a prospectively testable exact limit.

C9 — No free connected datum: the principle does not leave an independent connected coefficient/function/mediator matrix element that must be fitted or chosen after the fact.

C10 — Parsimony / independence: no unnecessary new field, scale, arbitrary metric on channel space, imported candidate dynamics, or post-hoc selector.

## MANDATORY PASS RULE

A proposal survives triage only if C1, C2, C3, C4, C8, C9 and C10 are PASS, and C5-C7 are at least `DEFINED_TEST_ROUTE` in the proposal itself. `DEFINED_TEST_ROUTE` is not a downstream PASS.

Exactly one survivor authorizes a new version principle. Multiple survivors => `AMBIGUOUS_NEW_VERSION_PRINCIPLE`; zero survivors => `NO_PREOUTCOME_PRINCIPLE_SELECTED`.

## FROZEN NEGATIVE / FALSE-POSITIVE CONTROLS

- A rule that simply fixes `lambda`, `gamma`, a cubic coefficient, or a mediator phase fails C1/C9.
- Bare mediator existence/reset/order fails C9 by CM1.
- Positivity/CPTP/lower-face recovery alone fails C4/C9 by NP1/NCP1.
- Standard GR/EFT equations copied as the selector fail the independence firewall even if physically consistent.
- A principle selected because its later `chi` is nonzero, large, elegant, experimentally favorable, or matches a desired formula is INVALID.
- A purely operational optimization with an arbitrary distance functional must justify that functional from RCG-002 or fail C1/C10.

## POSITIVE CLASSIFIER CONTROL

A hypothetical rule would count as a survivor if it prospectively specifies a physical source-to-state map, a nonlinear causal generator with no free connected coefficients, a testable conservation/constraint route, normalized positive evolution route, and exact lower-order recovery, all without importing dynamics or looking at `chi`.

Thus the criteria do not prohibit new principles by construction.

## INTERPRETATION CEILING

Passing this gate authorizes only the label `PROSPECTIVE_NEW_VERSION_PRINCIPLE_SELECTED` and a downstream derivation/falsification gate. It does not establish the selected dynamics, uniqueness among all possible principles, GR, new physics, quantum gravity, a physical completion-space dimension, or a nonzero connected signal.

## NEXT-GATE LOCK

If a unique principle is selected, the immediate next gate must derive its classical nonlinear field/state equations and conservation/constraint/causality structure before any connected three-source phase/noise is computed. External standard-theory comparison is allowed only after the independent structural derivation is frozen.