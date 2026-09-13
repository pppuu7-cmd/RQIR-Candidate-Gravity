# G90–G91 explicit covariant nonlinear-underdetermination synthesis

Date: 2026-09-13
Status: **RETROSPECTIVE SYNTHESIS OF PROSPECTIVELY FROZEN SIBLING GATES**
New scientific gate: **NO**
Programme readiness: **66%**
Theory established: **0%**

## Terminal inputs
- G90 C covariant cubic lift: `BLOCKED_C_EXPLICIT_COVARIANT_CUBIC_INVARIANT_FAMILY_PRESERVES_FROZEN_QUADRATIC_DATA_SCOPED`.
- G91 D covariant quartic lift: `BLOCKED_D_EXPLICIT_COVARIANT_QUARTIC_INVARIANT_FAMILY_PRESERVES_FROZEN_CUBIC_DATA_SCOPED`.

G91 used an infrastructure-only recovery launch after a workflow self-path typo. The frozen preregistration, scientific implementation, predicates and aggregate rule were unchanged; terminal validation re-ran all frozen lanes before classification.

## C explicit covariant family
The prospectively frozen local scalar-density family is
- `sqrt(|g|) R^3`;
- `sqrt(|g|) R R_{mu nu}R^{mu nu}`.

Formal flat-background counting makes both start at `O(h^3)`, so the frozen C quadratic/two-point data are unchanged. On the frozen pointwise Ricci backgrounds
- `E: (1,1,1,1)` gives `(R^3,R Ricci^2)=(64,16)`;
- `P: (1,1,2,2)` gives `(216,60)`.

The exact determinant is `384`, hence the two invariant directions are pointwise independent on the frozen panel. The scalar-flat control gives a zero row and does not fake independence. The branch-difference lift is CTP-normalized on equal histories.

## D explicit covariant family
The prospectively frozen local scalar-density family is
- `sqrt(|g|) R^4`;
- `sqrt(|g|) R^2 R_{mu nu}R^{mu nu}`.

Both start at `O(h^4)`, so the frozen D cubic/three-point data remain unchanged. On the same frozen backgrounds
- `E` gives `(R^4,R^2 Ricci^2)=(256,64)`;
- `P` gives `(1296,360)`.

The exact determinant is `9216`, so the two quartic invariant directions are pointwise independent on the frozen panel. The branch-difference lift is CTP-normalized, and because the additions begin at fourth order the previously audited D cubic kernel/jet is not modified in this scoped construction.

## Scientific consequence
G86–G89 showed that reduced higher-order completion freedom exists and that inherited lower-order constraints have selection rank zero. G90–G91 strengthen that conclusion: the freedom persists inside explicit local generally covariant curvature-invariant families.

Therefore **bare general covariance plus the already-frozen lower-order C/D information is not, within these explicit families, a sufficient nonlinear selector**. A unique nonlinear candidate law requires information beyond simply demanding that the higher-order completion be a generally covariant local scalar density and preserve the existing lower perturbative jet.

## What is still not proved
This is not a classification of all generally covariant invariants. It does not establish inequivalence modulo arbitrary nonlinear field redefinitions, integrations by parts, topological/dimension-specific identities, or equations-of-motion-redundant operators. It does not establish causal/unitary/measure closure of the higher-order terms.

## Next admissible requirement
Any proposed candidate-owned nonlinear selection principle must be prospectively specified before coefficient values are computed and must add genuine higher-order information. At minimum it must:
1. reduce the surviving higher-order coefficient/kernel freedom with nonzero selection rank;
2. preserve the already-frozen C or D lower-order/CTP/causal constraints;
3. be architecture-owned rather than imported from QGR/KMQGB/RQIR desired conclusions;
4. survive explicit null/post-hoc controls;
5. state a falsifiable scope ceiling and not equate mathematical selection with physical truth.

## Claim lock
No unique nonlinear law has been selected. No readiness increase, architecture selection, quantization, physical higher-order observable or new physics follows. `THEORY_ESTABLISHED=0%` remains unchanged.
