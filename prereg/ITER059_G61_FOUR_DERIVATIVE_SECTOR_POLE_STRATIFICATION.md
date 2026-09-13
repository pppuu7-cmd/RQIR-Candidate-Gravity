# Iter059 / G61 — four-derivative conserved-sector pole stratification

Preregistered: 2026-09-13, **before implementation and production evidence**.

## Scientific question
Given G60's candidate-independent two-dimensional local four-derivative linearized gauge-invariant quotient, determine the exact generic and exceptional algebraic pole/degeneracy stratification after adding the already-qualified G59 two-derivative massless-spin-2 baseline, without selecting any candidate coefficient ray.

This is a structural conserved-sector audit only. It does not authorize coefficients, a physical action, a ghost/no-go theorem, nonlinear completion or a quantum theory.

## Frozen scope and conventions
- 4D Minkowski `eta=diag(-1,1,1,1)`.
- One symmetric tensor `h_ab` with the G59 linear gauge symmetry.
- Two-derivative baseline is the G59 projective Fierz-Pauli ray `(1,-2,2,-1)`, with overall normalization fixed to `+1` only to define the algebraic root convention.
- Four-derivative quotient coordinates are `(a,b)` multiplying `R^2` and `Ricci^2`. The Gauss-Bonnet direction is already quotiented by G60.
- Canonical non-null momentum is `p=(q,0,0,0)` with symbolic `z=q^2`.
- Frozen conserved representatives: traceless spatial tensor `h_12=1` (TT sector representative) and transverse spatial trace `h_11=h_22=h_33=1` (scalar-sector representative).
- Only exact symbolic identities and rational held-out checks count.
- No candidate coefficient values are chosen.

## Frozen target identities
Direct evaluation from the G59 baseline bilinear form and G60 curvature definitions must derive, up to one common nonzero normalization per representative,
- TT response polynomial: `z*(-2 + b*z/2)`;
- scalar response polynomial: `z*(6 + 3*(3*a+b)*z)`.

Therefore the prospectively frozen exceptional strata are:
- no additional TT algebraic root iff `b=0`;
- no additional scalar algebraic root iff `3*a+b=0`;
- both additional roots absent simultaneously iff `(a,b)=(0,0)`.

These are algebraic sector roots in the frozen linearized quotient. No physical mass, norm, stability or quantum-state interpretation is authorized by this gate.

## Stream A — exact direct derivation
Recompute the G59 baseline bilinear and G60 `R^2`,`Ricci^2` quadratic responses directly from tensors, not by inserting the target formulas. PASS iff the two frozen symbolic response polynomials are obtained exactly and both retain the common massless factor `z`.

## Stream B — exceptional-stratum census
Frozen rational projective rays:
`(1,0),(0,1),(1,-3),(1,-1),(1,1),(2,-1),(1,-2),(2,1),(-1,1),(-2,3)`.
For every ray classify TT-extra-root present iff `b!=0` and scalar-extra-root present iff `3*a+b!=0`. PASS iff direct symbolic factorization agrees for every ray, `(1,0)` is TT-exceptional only, `(1,-3)` is scalar-exceptional only, and no nonzero frozen ray removes both.

## Stream C — quotient-basis covariance
Apply three frozen invertible coefficient changes
`U1=[[1,1],[0,1]]`, `U2=[[0,1],[1,0]]`, `U3=[[2,1],[1,1]]`.
Transform both coefficient coordinates and sector linear forms covariantly. PASS iff the zero/nonzero exceptional classification of `b` and `3a+b`, and both derived roots when present, are invariant after transform/back-transform for all frozen rays.

## Stream D — held-out direct evaluations and false-positive control
Held-out coefficient pairs `(3,2),(2,-5),(-3,4),(5,-1),(-2,-1),(4,-7)` and `q in {1,2,3,5}`. Compare direct tensor evaluation with the derived sector polynomials exactly. A deliberately wrong scalar combination `2*a+b` must be rejected on at least four held-out coefficient pairs; a deliberately wrong TT coefficient `a` must be rejected on at least four.

## Aggregate interpretation
All A/B/C/D must be valid and PASS.

If all pass, terminal classification:
`FOUR_DERIVATIVE_LINEARIZED_SECTOR_ADDITIONAL_ROOT_STRATIFICATION_SCOPED`.

If a mathematically valid frozen predicate fails: `SCIENTIFIC_FAIL_G61_<STREAMS>`. Runtime/implementation faults are `INFRASTRUCTURE_OR_IMPLEMENTATION_FAIL` and permit only minimal repair with this preregistration unchanged.

## Claim ceiling
Even full PASS establishes only that, in the frozen local four-derivative linearized quotient with the G59 baseline, every nonzero `(a,b)` direction produces at least one additional algebraic root across the two canonical conserved representatives, with exact exceptional lines `b=0` and `3a+b=0`. It does **not** prove a physical ghost, instability, nonunitarity, a global higher-derivative no-go theorem, or exclude nonlocal/additional-field/nonlinear mechanisms. Programme readiness remains 66% and `THEORY_ESTABLISHED=0%`.
