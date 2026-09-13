# Iter065 / G67 — source-saturated pole/residue viability audit (FROZEN)

Prospectively preregistered on 2026-09-13 before G67 implementation or production output.

## Scientific question
Do the additional poles and opposite relative residues identified algebraically in G61–G62 remain visible after saturation with the **complete G65 conserved symmetric-source space**, or can they disappear as representative-sector artifacts / uncoupled directions?

This gate is restricted to the frozen local linearized four-derivative class already defined by G60–G66. It does not select coefficients or assert a physical ghost.

## Frozen conventions
- Minkowski metric: `eta=diag(-1,1,1,1)`.
- Frozen momenta: `k1=(1,2,3,4)`, `k2=(2,-1,1,3)`, `k3=(3,1,-2,4)`.
- Use the exact G65 transverse projectors `P2` and `P0` and exact rational arithmetic.
- Conserved-source bilinear contraction:
  `S(A,B)=A^{mu nu} B_{mu nu}=sum_{mu,nu} eta_mu eta_nu A_munu B_munu` in the frozen diagonal-metric representation.
- Four-derivative coefficient rays:
  `(1,1),(2,-1),(1,-2),(-1,1),(-2,3),(3,2),(2,-5),(-3,4)`.
- Held-out mixed-source seeds: deterministic G65 `sym_seed(n)` with `n in {10,11,12,13}`, projected with the G65 transverse projector before saturation. Each mixed lane must itself verify conservation and nonzero `P2` and `P0` saturated numerators; a zero numerator makes the lane invalid rather than silently removable.
- Held-out nonsingular evaluation points: `z in {1/7,3/7,5/6,-5/7}`. A lane that coincides with a pole is invalid; no replacement point may be selected post hoc.

Frozen sector denominators from G61:
- `P_TT(z)=z*(-2 + b*z/2)` with extra root `r_TT=4/b` for `b!=0`.
- `P_S(z)=z*(6 + 3*(3a+b)*z)` with extra root `r_S=-2/(3a+b)` for `3a+b!=0`.

Frozen inverse-sector partial fractions from G62:
- for `b!=0`: `1/P_TT = -1/(2z) + 1/[2(z-r_TT)]`;
- for `3a+b!=0`: `1/P_S = 1/(6z) - 1/[6(z-r_S)]`.

## Stream A — TT source-saturated residues
For every frozen momentum, every seed `n={10,11,12,13}`, and every nonexceptional frozen coefficient ray:
1. construct a pure conserved `P2` source;
2. require exact conservation and exact `P0(T)=0`;
3. require nonzero source-saturated numerator `N2=S(T,P2(T))`;
4. require the source-saturated residues at `z=0` and `z=r_TT` to equal exactly `(-N2/2,+N2/2)` and therefore have exact ratio `-1`.

## Stream B — scalar source-saturated residues
For every frozen momentum, every seed, and every nonexceptional ray:
1. construct a pure conserved `P0` source;
2. require exact conservation and exact `P2(T)=0`;
3. require nonzero saturated numerator `N0=S(T,P0(T))`;
4. require the source-saturated residues at `z=0` and `z=r_S` to equal exactly `(+N0/6,-N0/6)` and therefore have exact ratio `-1`.

## Stream C — held-out generic conserved-source reconstruction
For every frozen momentum, all four mixed-source seeds, all eight coefficient rays and all four frozen nonsingular `z` values:
- require conservation and nonzero `N2,N0`;
- construct the direct tensor response `R=P2(T)/P_TT + P0(T)/P_S`;
- compute the exact source-saturated direct amplitude `S(T,R)`;
- independently reconstruct the amplitude from the frozen TT + scalar partial fractions and require exact equality.
No fitting, normalization or retuning is allowed.

## Stream D — discrete-Lorentz invariance of saturation
Use the exact G65 metric-preserving signed spatial permutation / time-reversal panel. For held-out conserved mixed sources:
- transform `k` and `T` covariantly;
- require exact invariance of `N2`, `N0`, pole locations and the source-saturated amplitude at the frozen nonsingular `z` values;
- require transformed sources to remain exactly conserved.

## Stream E — exceptional and false-positive controls
All controls must be detected:
1. `b=0` (`a=1,b=0`) must remove the TT extra pole and reduce the TT inverse response to the single massless term `-1/(2z)`;
2. `3a+b=0` (`a=1,b=-3`) must remove the scalar extra pole and reduce the scalar inverse response to `1/(6z)`;
3. a pure `P0` source must have zero TT saturated numerator and must not falsely activate TT residues;
4. a pure `P2` source must have zero scalar saturated numerator and must not falsely activate scalar residues;
5. a frozen generic unprojected nonconserved source must be rejected by the conserved-source admissibility guard;
6. an intentionally Euclidean (no Minkowski index raising) saturation convention must disagree with the frozen Minkowski saturation for at least one frozen mixed-source lane.

## Aggregate rule
PASS iff A/B/C/D/E are all structural-valid and pass their frozen predicates.

Allowed PASS classification only:
`FOUR_DERIVATIVE_LINEARIZED_SOURCE_SATURATED_OPPOSITE_RESIDUE_COUPLING_SCOPED`.

A valid frozen-predicate violation is `SCIENTIFIC_FAIL_G67_<streams>`. Missing/malformed/duplicate artifacts are `INFRASTRUCTURE_OR_ARTIFACT_INVALID`.

## Claim ceiling
PASS would establish only that, inside the frozen **local linearized four-derivative class**, additional sector poles with opposite relative residues remain coupled to nonzero components of the complete conserved-source response and survive exact source saturation. It is **not** a theorem of negative norm, physical ghost propagation, instability, nonunitarity, coefficient exclusion, nonlinear inconsistency, a global gravity no-go theorem, new physics, or full quantum gravity.

Programme readiness remains **66%** and theory established remains **0%** regardless of G67 PASS/FAIL unless a separately preregistered rubric authorizes a change.
