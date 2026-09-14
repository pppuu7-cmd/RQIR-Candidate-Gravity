# RCG002-CM1 — Closed sequential mediator realization nonuniqueness gate

Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION
Date: 2026-09-14
Project: RQIR-Candidate-Gravity only
Starting authority: main `613713ced67058e0010cc44ede60955ec455fdb7` and its terminal NP1 recovery state.

## Purpose

NP1 proves that normalized positive channels, exact recovery of all one-/two-source coordinate faces, rephasing quotient, the G97 total-translation generator, and existence of an abstract finite-time evolution do not select the connected three-source extension. CM1 tests one natural remaining structural rescue before a new physical law is introduced:

> Does requiring an explicit closed mediator that interacts sequentially with A, B, C through only source-mediator two-body controlled operations eliminate or restrict the NP1 connected-phase freedom?

This is a falsification/underdetermination gate. It is NOT a proposed gravitational mediator, NOT a new RCG-002 candidate version, and NOT permission to fit a connected coefficient.

## Frozen branch system

Use three binary internal source labels `a,b,c in {0,1}`. They label the three-source branch cube only. No spatial source-history map is inferred from them.

Use a four-level mediator/bus `M` with orthonormal basis `|0>,|1>,|2>,|3>` and initial state `|0>`.

Define the bus cyclic shift `S|m> = |m+1 mod 4>`. For source X in {A,B,C}, define the two-body controlled shift

`V_X = |0><0|_X tensor I_M + |1><1|_X tensor S_M`.

Freeze the time ordering

`V_A -> V_B -> V_C -> P_lambda -> V_C^{-1} -> V_B^{-1} -> V_A^{-1}`,

where the mediator-only phase is

`P_lambda = diag(1,1,1,exp(i lambda))`.

`lambda` remains a symbolic free real parameter. It is NOT fitted and NOT interpreted as a physical gravitational coefficient.

The frozen source-mediator architecture uses no direct A-B, A-C, or B-C gate and no primitive three-source interaction. All source-dependent operations are two-body source-bus controls; `P_lambda` acts on the bus only.

## Completion space before

Authoritative physical nonlinear completion space remains undefined after NP1. Within the NP1 operational connected-extension calibration, at least one connected phase direction and one connected dephasing direction survive. CM1 tests only whether explicit closed sequential mediation removes the phase freedom. It does not establish the dimension of the physical gravitational quotient.

## Frozen hypothesis

H_CM1: explicit closed sequential source-bus mediation plus exact mediator reset is sufficient to eliminate arbitrary connected phase freedom while keeping every one-/two-source coordinate face unchanged.

CM1 is designed to try to falsify H_CM1.

## Independent lanes

### Lane A — exact branch action
For all eight `(a,b,c)`, compute the exact bus trajectory through the frozen sequence, the final bus state, and the induced source amplitude. Check whether the bus returns exactly to `|0>` for every branch. Report the exact induced source-only diagonal multiplier as a function of symbolic `lambda`.

### Lane B — lower-face and connected-quotient audit
Check exactly all three coordinate faces `a=0`, `b=0`, `c=0`. The CM1 multiplier must equal identity on every vertex in those faces for it to preserve all lower one-/two-source face channels. Compute the third Boolean finite difference of the induced branch phase and compare it with all constant + one-body + pairwise phase functions.

Frozen negative controls:
1. set `lambda=0`: connected multiplier must be identity;
2. omit any one of `V_A,V_B,V_C` together with its inverse: no branch may make the bus visit `|3>` before `P_lambda`, so the connected third finite difference must vanish;
3. replace `P_lambda` by a phase on bus level `|2>`: this is expected to alter some two-source face and therefore must fail the lower-face-preservation predicate.

### Lane C — unitarity, two-body locality, mediator closure
Construct exact finite matrices for every frozen elementary gate. Verify unitarity exactly, verify that each source-dependent primitive acts only on one source label and the mediator, and verify the mediator's final reduced state is exactly the same pure `|0><0|` for all source branches. No residual which-branch record in M is allowed.

Also check, at the abstract G97 bookkeeping level, that if the branch-label operators and M carry no spatial translation charge, every CM1 primitive commutes with the already validated G97 total spatial translation generator. This is only a translation-bookkeeping control, not energy conservation or Bianchi closure.

### Lane D — order/causality-scope and adversarial audit
Verify that the frozen gate sequence is a finite ordered circuit and that reversing only the uncompute order fails exact reset or changes the operation where expected. Check that arbitrary `lambda` enters only through the prospectively frozen mediator-only phase and is not generated or selected by lower-face data.

Explicitly classify the causality notion as `FINITE_ORDERED_CIRCUIT_CAUSALITY_ONLY`. No relativistic microcausality, finite-speed spacetime propagation, stress-energy source map, or gravitational retarded Green-function claim is authorized.

## Frozen PASS / FAIL / BLOCKED / INVALID

`PASS_MEDIATOR_REQUIREMENT_SELECTS_CONNECTED_PHASE_SCOPED` only if all frozen closure/lower-face/unitarity conditions hold and they force `lambda` to a unique value or a discrete prospectively specified set without importing a new physical datum.

`NONUNIQUENESS_SURVIVES_CLOSED_SEQUENTIAL_MEDIATOR_SCOPED` if there is an exact continuum of `lambda` values for which all frozen CM1 structural predicates pass while the connected phase differs.

`FAIL_CLOSED_MEDIATOR_REALIZATION_SCOPED` if no nonzero `lambda` passes the exact frozen architecture and controls.

`BLOCKED_IMPLEMENTATION_OR_OBJECT` if the frozen architecture cannot be represented or independently checked as specified.

`INVALID` if implementation changes the mediator dimension, source-dependent primitive set, gate ordering, lower-face predicates, controls, or interpretation ceiling after substantive results are known.

## Interpretation ceiling

Even a surviving continuum proves only that finite-dimensional closed sequential mediator realizability in this frozen operational architecture is insufficient to select the RCG-002 connected phase. It does NOT prove nonuniqueness under relativistic locality, general covariance, nonlinear stress-energy conservation, Bianchi/constraint closure, a physical source-history map, a gravitational field equation, or any complete candidate version.

A passing mediator witness is a calibration counterexample, not candidate physics. `lambda` must not be promoted to a gravitational coefficient.

If nonuniqueness survives, the next admissible frontier remains the NEW CANDIDATE VERSION PRINCIPLE GATE: an independently motivated candidate-owned physical source/state/evolution principle with spacetime causal and nonlinear conservation/Bianchi content.

Readiness remains 66%; theory established remains 0% regardless of CM1 outcome.