# Iter062 / G64 — source-coupling rank audit (FROZEN BEFORE IMPLEMENTATION)

Objective: test, in exactly the frozen TT/scalar rational response representatives already qualified by G61–G63, whether both auxiliary second-order modes are algebraically source-coupled in every nonexceptional two-pole case and whether this two-mode source-coupling rank is invariant under a preregistered panel of invertible real field redefinitions.

No candidate coefficient ray is selected. No QGR/KMQGB/RQIR physical input is imported.

## Frozen inputs
TT residues `(-1/2,+1/2)` with additional root `4/b` for `b != 0`; scalar residues `(+1/6,-1/6)` with additional root `-2/(3a+b)` for `3a+b != 0`. Use the same 12 rational `(a,b)` rays as G62/G63.

## Frozen predicates
A. Exact canonical two-mode realization: both residues are nonzero; the minimal two-pole realization has source-coupling rank 2 when the two distinct simple poles are retained. Reconstruct the rational response exactly.
B. Held-out census: all 24 nonexceptional sector cases across the 12 frozen rays must have two distinct retained pole contributions with nonzero residues. Any coincident-pole case is classified separately, not silently counted PASS.
C. Invariance: under the eight frozen invertible real 2x2 matrices used in G63, transform quadratic form and source vector covariantly and verify exact response reconstruction plus unchanged controllable/source-coupled realization rank.
D. Controls: exceptional one-pole limits must reduce to rank 1; deliberately zeroing either canonical source coupling must be detected as rank loss; a duplicated-pole fake must not be accepted as a generic rank-2 realization.

## Frozen interpretation
Full PASS only if A–D pass: `FOUR_DERIVATIVE_LINEARIZED_TWO_MODE_SOURCE_COUPLING_RANK_TWO_SCOPED`.
Failure of a scientific predicate is scientific FAIL. Invalid algebra/input is BLOCKED/INVALID as reported. Infrastructure errors are not scientific FAIL and may receive minimal technical repair without changing this preregistration.

Scope ceiling: algebraic minimal-realization/source-coupling statement in two frozen linearized conserved-sector representatives only. PASS does not establish a physical ghost, instability, quantum-unitarity failure, coefficient selection, or global higher-derivative no-go theorem. Programme readiness remains 66% and theory established remains 0% solely from this gate.