# Iter060 / G62 — relative-residue algebraic audit

Preregistered: 2026-09-13, before implementation and production evidence.

## Scientific question
Given the terminal G61 sector polynomials, determine the exact relative partial-fraction residue structure of the two frozen conserved-sector rational responses, without selecting a candidate coefficient ray and without assigning a physical-particle interpretation.

## Frozen scope
Use only the G61 candidate-independent sector polynomials
- `P_TT(z)=z*(b*z-4)/2`;
- `P_scalar(z)=3*z*((3*a+b)*z+2)`.
Define the algebraic response as `1/P(z)` for each representative. Overall common nonzero normalization of a representative may change both residues together and therefore cannot change their relative sign.

Let `c=3*a+b`.

For a simple root `r`, residue is frozen as `1/P'(r)`.

## Frozen target identities
For `b != 0`:
- TT roots are `0` and `4/b`;
- TT residues are exactly `-1/2` and `+1/2` respectively;
- their ratio is exactly `-1`.

For `c != 0`:
- scalar roots are `0` and `-2/c`;
- scalar residues are exactly `+1/6` and `-1/6` respectively;
- their ratio is exactly `-1`.

Exceptional strata:
- `b=0`: TT has only the massless finite algebraic root in this polynomial degree;
- `c=0`: scalar has only the massless finite algebraic root in this polynomial degree.
No interpretation as a physical ghost, norm, state or mass is authorized.

## Stream A — exact symbolic residue derivation
Derive roots and residues directly from the frozen G61 polynomials using differentiation and exact symbolic simplification. PASS iff the target roots/residues/ratios are obtained exactly under the respective non-exceptional assumptions.

## Stream B — held-out rational-ray census
Frozen coefficient pairs:
`(1,1),(2,-1),(1,-2),(-1,1),(-2,3),(3,2),(2,-5),(-3,4),(5,-1),(4,-7),(7,3),(-5,2)`.
For every non-exceptional sector compute roots and residues exactly and verify relative residue ratio `-1`. For exceptional sectors verify absence of a second finite root. PASS iff all sector/ray classifications match.

## Stream C — quotient-coordinate covariance
Use frozen invertible changes `U1=[[1,1],[0,1]]`, `U2=[[0,1],[1,0]]`, `U3=[[2,1],[1,1]]`. Transform coefficient coordinates and the linear forms `b` and `c=3a+b` covariantly; back-transform and recompute roots/residue ratios for all frozen rays. PASS iff exceptional/non-exceptional classification, roots after back-transform and relative residue ratios are invariant exactly.

## Stream D — exceptional and false-positive controls
Check exact exceptional rays `(1,0)` for TT and `(1,-3)` for scalar. Verify polynomial degree reduction and absence of the second finite root. On every non-exceptional held-out sector, deliberately wrong same-sign residue hypothesis `ratio=+1` must be rejected. Also verify multiplying a sector polynomial by frozen nonzero factors `{-3,-1,2,5}` rescales both residues but leaves their ratio exactly `-1`.

## Aggregate interpretation
All A/B/C/D must be valid and PASS.

If all pass, terminal classification:
`FOUR_DERIVATIVE_LINEARIZED_SECTOR_RELATIVE_RESIDUE_OPPOSITION_SCOPED`.

If any mathematically valid frozen predicate fails: `SCIENTIFIC_FAIL_G62_<STREAMS>`. Runtime/implementation faults are `INFRASTRUCTURE_OR_IMPLEMENTATION_FAIL` and permit only minimal repair with this preregistration unchanged.

## Claim ceiling
Even full PASS establishes only an exact algebraic relative-residue property of the two frozen linearized conserved-sector representatives. It does not prove a physical ghost, negative norm, instability, nonunitarity, a global higher-derivative no-go theorem, or select a candidate coefficient ray. Programme readiness remains 66%; `THEORY_ESTABLISHED=0%`.
