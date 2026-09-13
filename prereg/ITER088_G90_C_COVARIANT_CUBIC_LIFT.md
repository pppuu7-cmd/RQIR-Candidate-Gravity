# Iter088 / G90 — C explicit covariant cubic lift of nonlinear underdetermination

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13
Parallel status: **C-SPECIFIC SIBLING OF G91-D; COMMON BASE IS POST-G89 MAIN**

## Scope
G86/G88 established nonlinear underdetermination and inherited-selection rank zero using a reduced cubic jet witness. G90 strengthens that result by replacing the reduced cubic shapes with an explicit local generally covariant curvature-invariant family.

This gate does not select a nonlinear C law. It asks whether two pointwise independent generally covariant cubic scalar densities can preserve the frozen C quadratic perturbative order simultaneously. A valid result is still `BLOCKED/UNDERDETERMINED`, but with a stronger covariant-family witness.

## Frozen covariant family
Use the local scalar densities
- `J1 = sqrt(|g|) R^3`;
- `J2 = sqrt(|g|) R (R_{mu nu} R^{mu nu})`.

Each is a generally covariant scalar density by construction. Their CTP lifts are branch differences `Delta J_i = J_i[g_+] - J_i[g_-]`, so equal-history normalization is exact.

Frozen formal flat-background counting parameter `t`:
- `sqrt(|g|)=1+s1 t+s2 t^2+s3 t^3+...`;
- `R=t r1+t^2 r2+t^3 r3+...`;
- `Q:=R_{mu nu}R^{mu nu}=t^2 q2+t^3 q3+...`.

Thus both `J1` and `J2` must begin at `O(t^3)` and have zero formal derivatives through order two at `t=0`.

## Frozen pointwise curvature backgrounds for independence
Evaluate the scalar parts in a normalized local frame with `sqrt(|g|)=1`.

- `E`: Ricci-operator spectrum `(1,1,1,1)`, hence `R=4`, `Q=4`.
- `P`: Ricci-operator spectrum `(1,1,2,2)`, hence `R=6`, `Q=10`.
- `Z`: scalar-flat control with spectrum `(1,-1,2,-2)`, hence `R=0`, `Q=10`.

The `E/P` evaluation matrix for `(R^3, R Q)` must have rank two. The scalar-flat `Z` control makes both chosen invariants vanish and therefore must not be counted as an independence witness by itself.

Frozen coefficient family: `lambda J1 + mu J2`, with sample points `(1,0),(0,1),(1,1),(2,-1),(-2,3)`.

## Independent streams
### A — formal perturbative-order lift
Expand both frozen densities through at least `O(t^5)` using symbolic coefficients. Require:
- coefficients of `t^0,t^1,t^2` vanish identically for both;
- the `t^3` coefficient of `J1` is `r1^3`;
- the `t^3` coefficient of `J2` is `r1 q2`;
- the formal third derivative at zero is generically nonzero while value/first/second derivatives vanish.

### B — explicit pointwise invariant independence
Require exact rank two of the `E/P` evaluation matrix
`[[R_E^3, R_E Q_E],[R_P^3,R_P Q_P]]`.
Require its determinant to be nonzero exactly.

Also require:
- `J1` and `2 J1` give rank one and are recognized as the same scalar shape family;
- `Z` gives the zero row and cannot create rank;
- adding `Z` to the valid `E/P` panel leaves rank two.

### C — CTP normalization and coefficient freedom
For the branch-difference family `lambda Delta J1 + mu Delta J2`, require for arbitrary `(lambda,mu)`:
- exact equal-history vanishing;
- odd sign under branch exchange;
- formal derivatives through order two in the common flat-background counting parameter vanish;
- every frozen sample coefficient pair preserves the lower `O(t^2)` data.

The inherited covariance/CTP construction itself must impose no algebraic equation selecting `(lambda,mu)` within this two-invariant family.

### D — lower-order contamination and independence controls
Frozen controls:
1. `sqrt(|g|) R^2` begins at `O(t^2)` and must be rejected as a C lower-jet-preserving cubic completion;
2. replacing `J2` by `2 J1` collapses the `E/P` evaluation rank to one;
3. a zero invariant contributes no new direction;
4. a one-background panel cannot certify two-dimensional invariant independence and must have row rank at most one.

## Frozen aggregate rule
All streams valid =>
`BLOCKED_C_EXPLICIT_COVARIANT_CUBIC_INVARIANT_FAMILY_PRESERVES_FROZEN_QUADRATIC_DATA_SCOPED`.

Any failed frozen predicate => `SCIENTIFIC_FAIL_FROZEN_C_COVARIANT_LIFT_PREDICATE`.
Missing/invalid controls/artifacts => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
A valid BLOCKED result strengthens G86/G88 by showing nonlinear freedom inside an explicit two-dimensional local generally covariant curvature-cubic family. It does **not** prove that these are the only invariants, prove inequivalence modulo arbitrary field redefinitions/integrations by parts, establish causal/unitary/measure closure, or select either invariant physically.

Readiness remains 66%; theory established remains 0%.
