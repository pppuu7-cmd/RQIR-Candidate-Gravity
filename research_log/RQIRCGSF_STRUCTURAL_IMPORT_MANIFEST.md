# RQIRCGSF structural import manifest

Status: controlled reconciliation/import into parent RQIRCG. This document imports validated structural constraints and obligations only. It does **not** retroactively make post-VB1 selected principles part of historical RCG-002.

## SOURCE_REPO

Source repository: `pppuu7-cmd/RQIRCG-structural-findings`.

Source role: `PROSPECTIVE NEW-PRINCIPLE / SUCCESSOR SEARCH`.

Source authoritative recovery head at import: `9eb6c8821c285a13d63a7a3d6859d2c1e0db2157`.

Parent repository starting head for this import: `b24e13491104622851df19b26033a11a931357c7`.

Historical parent lock remains:

`RCG002_CURRENT_VERSION_NONLINEAR_DYNAMICS_UNDERDETERMINED`

and

`CURRENT_VERSION_TERMINAL_AT_NONLINEAR_MODEL_DEFINITION_BOUNDARY`.

## SOURCE_RESULTS

Successor-only classical selection result:

- SF021 terminal commit `3216863317cf088b77d643c42a382800b4a3f004` is **not** the SF021 commit; the exact SF021 result file is `results/SF021_RHPI_GRAVITATIONAL_LAW_SELECTION_TERMINAL.md`, classification `RHPI_SELECTED_AS_CLASSICAL_GRAVITATIONAL_LAW_PRINCIPLE_SCOPED`. Its principle is successor-branch information only and is not imported as historical RCG-002 authority.

Validated structural results imported in this reconciliation:

- SF025 terminal commit `3216863317cf088b77d643c42a382800b4a3f004`, classification `POST_RHPI_QUANTUM_COMPOSITION_DOES_NOT_FIX_FINITE_ON_SHELL_MATCHING_SCOPED`.
- SF026 terminal commit `cb368a4fb226cc9c2c18f5b52880546922880bcd`, classifications `PAIRWISE_NULL_NOT_STABLE_UNDER_SELF_CONSISTENT_HISTORY_PULLBACK_SCOPED` and `FINITE_TIME_OBSERVABLE_BLOCKED_PENDING_BOUNDARY_COMPLETE_PROTOCOL`.

SF025 preregistration: `9ef45ce5858f9271a450abef4adcb798d8dd2c85`.
SF026 preregistration: `3a495200aa2e9afaf1c3f56f887a0b40fa810cb9`.
Shared executed script: `scripts/sf025_sf026_checks.py`, commit `36d3f61f35792177333ada9615983c595b3c9863`, SHA-256 `c9bea62cdb327cf7841959204b9f656163fd71a284f00176361f0a24da3399f8`.
SF025 raw commit: `76196971282e7e6ed7d9859d8b8f8fb547981a37`.
SF026 raw commit: `91b9aca1bf7477375d3de6dda42a3fda03e15fc0`.
No GitHub Actions run is claimed for SF025/SF026.

## SF025_IMPORT

Imported terminal structural statement:

`POST_RHPI_QUANTUM_COMPOSITION_DOES_NOT_FIX_FINITE_ON_SHELL_MATCHING_SCOPED`.

Scope retained exactly: in a formal low-energy perturbative quantum continuation, with the classical law fixed, incoming preparation fixed, lower-order calibration fixed, and covariance/causal factorization/perturbative unitarity/Ward consistency imposed, at least one finite physically nonredundant positive-loop on-shell matching direction remains in the exhibited class.

The curvature-cubic `Riemann^3` term used by SF025 remains a quarantined counterexample/witness. It is **not** imported as RCG dynamics, a preferred EFT term, or a successor matching value.

New parent quantum-law obligation:

> Any future quantum-side model-defining axiom must have nonzero selection power on the physical quantum-law/on-shell-matching fibre after the classical law and preparation/state data have been fixed.

The following conditions are no longer sufficient by repetition alone to count as a complete quantum selector:

- covariance;
- causal composition/factorization;
- perturbative unitarity;
- Ward identities;
- fixed classical limit;
- fixed incoming preparation.

If a proposed quantum principle admits the SF025 physical matching witness freedom in its declared scope, it is at most an admissibility/partial-restriction principle for that slot.

Critical slot separation imported from SF025:

`QUANTUM_STATE_MEASURE_SELECTION != QUANTUM_LAW_ON_SHELL_MATCHING_SELECTION`.

SF025 holds the incoming state/preparation fixed; therefore its remaining matching freedom must not be relabelled as `UNKNOWN_INITIAL_STATE`.

## SF026_IMPORT

Retained historical exact theorem from parent/VB1 scope:

For independently prescribed factorized histories and a linear-plus-quadratic/pairwise functional,

`Delta_A Delta_B Delta_C W2 = 0`.

Imported scope boundary:

`PAIRWISE_NULL_NOT_STABLE_UNDER_SELF_CONSISTENT_HISTORY_PULLBACK_SCOPED`.

When mutually interacting trajectories are solved self-consistently,

`q_i = q_i(s_A,s_B,s_C,t)`,

a microscopic pairwise Newtonian Hamiltonian/potential can yield a nonzero three-label connected **on-shell/open-action** dependence without any new three-body gravitational vertex.

Exact short-time released-action diagnostic:

`S_release(q0,T) = -V0*T + (1/3) A0*T^3 + O(T^5)`,

where

`A0 = (grad V)^T M^-1 (grad V)`.

For the frozen SF026 equal-mass collinear geometry

`q_A=a ell`, `q_B=(4+2b)ell`, `q_C=(10+3c)ell`,

raw exact arithmetic gives

`Delta3 V_N = 0`,

`Delta3 A = -(82/616005) G^2 m^3/ell^4`,

and therefore

`Delta3 S_release = -(82/1848015) (G^2 m^3/ell^4) T^3 + O(T^5)`.

This quantity is imported only as a classical baseline diagnostic. It is **not** `chi_ABC` and is not a measured quantum observable.

The distinct return-endpoint problem has a different coefficient,

`S_return = -V0*T - (1/24) A0*T^3 + O(T^5)`,

with frozen-geometry connected coefficient

`+(41/7392060) (G^2 m^3/ell^4) T^3 + O(T^5)`.

The sign difference is boundary-condition dependence, not contradictory predictions for one experiment.

## WHAT_CHANGES_IN_RQIRCG

Future successor-theory construction and audit must include two new cross-cutting structural obligations:

1. a quantum selector must act on the quantum-law/matching fibre, not merely on state/preparation or generic covariance/unitarity conditions;
2. a connected observable must be interpreted against a complete self-consistent lower-order baseline and a boundary-complete operational protocol.

The parent model-definition graph is therefore refined to keep distinct:

- classical-law slot;
- source/preparation slot;
- quantum-state/measure slot;
- quantum-law/on-shell-matching slot;
- operational-observable/readout slot.

These slots may constrain one another but must not be collapsed by nomenclature.

## WHAT_DOES_NOT_CHANGE

Historical RCG-002 remains terminal at the nonlinear model-definition boundary.

No historical terminal result is rewritten.

No RHPI, quantum selector, source principle, higher-curvature term, matching coefficient, apparatus protocol, or future successor dynamics is made part of old RCG-002.

Programme readiness remains 66% unless separately changed by an authorized gate.
Theory established remains 0%.
Physical selector rank remains `UNDEFINED_PHYSICAL_MAP_MISSING`.
Physical nonlinear completion space remains `UNDEFINED`.

## HISTORICAL_RCG002_LOCK

`RCG002_CURRENT_VERSION_NONLINEAR_DYNAMICS_UNDERDETERMINED` remains authoritative.

All genuinely new post-VB1 model content is labelled:

`POST-VB1 NEW INFORMATION`.

It is forbidden to state or imply:

`RCG-002 implies RHPI`.

The only permitted scoped wording is that RQIRCGSF independently selected RHPI as a sufficient classical reconstruction package in its audited successor-branch domain.

## SUCCESSOR_ONLY_CONTENT

The following remain successor-only until a future promotion gate:

- RHPI-S / ADM-Einstein classical gravitational-law principle from SF021;
- any future quantum-law selector;
- any future source constitution principle;
- any future state/measure rule;
- any future operational apparatus/readout model;
- any matching coefficient or nonlinear dynamics selected after VB1.

No successor-only content receives retroactive authority in RCG-002.

## NEW_SELECTOR_OBLIGATIONS

Any future proposed model-defining axiom must be audited for:

1. target-slot identity;
2. actual selection power on that slot rather than mere admissibility;
3. SF025 negative-control survival on the fixed-classical-law, fixed-preparation quantum-law fibre when the proposal claims quantum-law completeness;
4. explicit separation from state/preparation freedom;
5. no use of future `chi_ABC` or connected outcomes in selecting the axiom;
6. compatibility with SF026 self-consistent lower-order connected baseline obligations;
7. no substitution of an open action or coordinate potential for a measured operational observable.

## NEW_OBSERVABLE_OBLIGATIONS

The minimum future physical observable chain is:

`PREPARATION`
`-> FULL FINITE-TIME EVOLUTION`
`-> APPARATUS RECOIL / CONTROL`
`-> RECOMBINATION`
`-> READOUT / POVM`
`-> PHYSICAL PROBABILITY OR COHERENCE`.

A coordinate potential, instantaneous kernel, or open propagation action is insufficient by itself.

New interpretation firewall:

`NONZERO_CONNECTED_SIGNAL != NEW_THREE_BODY_GRAVITATIONAL_VERTEX`.

A future nonzero `chi_ABC` or connected coherence effect may be interpreted only after subtraction/comparison against the complete self-consistent authorized lower-order baseline using the **same** apparatus, preparation, endpoint/boundary data and measurement. At minimum the baseline ladder is:

1. evolving Newtonian pairwise baseline;
2. authorized 1PN/known-physics baseline;
3. then any prospectively selected successor contribution.

Boundary protocol may not be selected after viewing the connected signal.

## CLAIM_CEILING

This import does not establish:

- RHPI as historical RCG-002 content;
- a selected quantum law;
- a selected source constitution;
- a selected state/measure;
- a measured finite-time `chi_ABC`;
- a new three-body gravitational vertex;
- new physics;
- full quantum gravity;
- theory establishment.

It establishes only that validated SF025/SF026 structural results now constrain all future successor-theory selection and observable interpretation in the parent RQIRCG architecture while preserving provenance and the historical version boundary.

## FUTURE_PROMOTION_RULE

RQIRCGSF remains an independent successor-principle incubator.

A successor candidate may return to parent RQIRCG only through a separate future

`SUCCESSOR_PROMOTION_GATE`.

At minimum that gate must have sufficiently explicit, mutually compatible definitions of:

- `CLASSICAL LAW`;
- `SOURCE CONSTITUTION`;
- `QUANTUM LAW`;
- `STATE / MEASURE`;
- `OPERATIONAL MAP`.

Promotion need not claim full quantum gravity, but these model-defining slots may not remain hidden or be supplied by outcome-driven fitting.

`chi_ABC` remains unauthorized in the parent current-version line and no new quantum `chi_ABC` was computed in this integration.