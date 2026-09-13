# Iter089 / G91 — D explicit covariant quartic lift of nonlinear underdetermination

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13
Parallel status: **D-SPECIFIC SIBLING OF G90-C; COMMON BASE IS POST-G89 MAIN**

## Scope
G87/G89 established nonlinear underdetermination and inherited-selection rank zero using a reduced quartic jet witness. G91 strengthens that result by replacing the reduced quartic shapes with an explicit local generally covariant curvature-invariant family.

This gate does not select a nonlinear D law. It asks whether two pointwise independent generally covariant quartic scalar densities can preserve the frozen D cubic perturbative order and audited cubic structure simultaneously.

## Frozen covariant family
Use the local scalar densities
- `K1 = sqrt(|g|) R^4`;
- `K2 = sqrt(|g|) R^2 (R_{mu nu} R^{mu nu})`.

Each is a generally covariant scalar density by construction. Their CTP lifts are branch differences `Delta K_i = K_i[g_+] - K_i[g_-]`, hence equal-history normalization is exact.

Frozen formal flat-background counting parameter `t`:
- `sqrt(|g|)=1+s1 t+s2 t^2+s3 t^3+s4 t^4+...`;
- `R=t r1+t^2 r2+t^3 r3+t^4 r4+...`;
- `Q:=R_{mu nu}R^{mu nu}=t^2 q2+t^3 q3+t^4 q4+...`.

Thus both `K1` and `K2` must begin at `O(t^4)` and have zero formal derivatives through order three at `t=0`.

## Frozen pointwise curvature backgrounds for independence
Evaluate the scalar parts in a normalized local frame with `sqrt(|g|)=1`.

- `E`: Ricci-operator spectrum `(1,1,1,1)`, hence `R=4`, `Q=4`.
- `P`: Ricci-operator spectrum `(1,1,2,2)`, hence `R=6`, `Q=10`.
- `Z`: scalar-flat control with spectrum `(1,-1,2,-2)`, hence `R=0`, `Q=10`.

The `E/P` evaluation matrix for `(R^4,R^2 Q)` must have exact rank two. `Z` makes both chosen invariants vanish and cannot establish independence by itself.

Frozen coefficient family: `lambda K1 + mu K2`, with sample points `(1,0),(0,1),(1,1),(2,-1),(-2,3)`.

## Independent streams
### A — formal perturbative-order lift
Expand both frozen densities through at least `O(t^6)`. Require:
- coefficients of `t^0,t^1,t^2,t^3` vanish identically for both;
- the `t^4` coefficient of `K1` is `r1^4`;
- the `t^4` coefficient of `K2` is `r1^2 q2`;
- formal derivatives through third order at zero vanish and the fourth derivative is generically nonzero.

### B — explicit pointwise invariant independence
Require exact rank two and nonzero determinant of the `E/P` evaluation matrix for `(R^4,R^2 Q)`.

Also require:
- `K1` and `2 K1` give rank one and are recognized as one scalar shape family;
- `Z` gives a zero row and cannot create rank;
- adding `Z` to the valid `E/P` panel leaves rank two.

### C — CTP normalization and preservation of frozen D cubic structure
For `lambda Delta K1 + mu Delta K2`, require for arbitrary coefficients:
- exact equal-history vanishing;
- odd sign under branch exchange;
- formal derivatives through order three in the common flat-background counting parameter vanish;
- every frozen sample coefficient pair preserves the lower `O(t^3)` data.

Independently reconstruct the frozen D cubic kernel and require it to remain unchanged, retarded and Sigma-symmetric. The frozen D Hessian must remain zero and its third derivative nonzero.

### D — lower-order contamination and independence controls
Frozen controls:
1. `sqrt(|g|) R^3` begins at `O(t^3)` and must be rejected as a D cubic-jet-preserving quartic completion;
2. replacing `K2` by `2 K1` collapses the `E/P` evaluation rank to one;
3. a zero invariant contributes no new direction;
4. a one-background panel cannot certify two-dimensional invariant independence and must have row rank at most one.

## Frozen aggregate rule
All streams valid =>
`BLOCKED_D_EXPLICIT_COVARIANT_QUARTIC_INVARIANT_FAMILY_PRESERVES_FROZEN_CUBIC_DATA_SCOPED`.

Any failed frozen predicate => `SCIENTIFIC_FAIL_FROZEN_D_COVARIANT_LIFT_PREDICATE`.
Missing/invalid controls/artifacts => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
A valid BLOCKED result strengthens G87/G89 by showing nonlinear freedom inside an explicit two-dimensional local generally covariant curvature-quartic family while preserving the audited D cubic structure. It does **not** prove that these are the only invariants, prove inequivalence modulo arbitrary field redefinitions/integrations by parts, establish a quartic retarded/unitary/measure closure, or select either invariant physically.

Readiness remains 66%; theory established remains 0%.
