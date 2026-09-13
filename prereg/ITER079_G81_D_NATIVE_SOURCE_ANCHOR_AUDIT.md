# Iter079 / G81 — D native source-anchor availability audit

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13
Parallel status: **D-SPECIFIC SIBLING OF G80-C; COMMON BASE IS TERMINAL G76–G79 MAIN**

## Scope
Architecture D is the frozen non-Gaussian CTP cubic construction from G70, supplemented only by the G72 retarded cubic-support/CTP-normalization witness and its zero-Hessian/nonzero-cubic compatibility result. G73/G74 represent the local D deformation tangent in the cubic/three-point block and the exact same-shape cubic calibration nuisance N3 by identical tangent support.

G81 asks a deliberately restrictive question: **do retarded support, Sigma-leg permutations, CTP normalization or the already-frozen cubic jet structure themselves break the exact D/N3 calibration alias without adding a new calibration channel, new kernel shape, or new candidate-owned dynamics?**

No new physical observable is allowed in the scientific lanes. Direct calibration, altered kernel shape and advanced-support contamination appear only as controls.

## Frozen inputs
- G70 cubic functional: `DeltaGamma_3 = kappa3 sum_abc K3_abc DeltaT_a SigmaT_b SigmaT_c`, symmetric in the two Sigma legs.
- G72 finite discrete-time retarded support: `t_Delta >= max(t_Sigma1,t_Sigma2)` with exact Sigma-leg symmetry and `Gamma3[Delta=0]=0`.
- G72/G71 jet structure: cubic Hessian at zero/background exactly vanishes while the third derivative is nonzero.
- G74 exact same-shape cubic calibration nuisance: `N3` has the same local cubic tangent as D.
- Frozen G72 time grid `t in {0,1,2,3}` and deterministic rational retarded kernel construction.

## Independent streams
### A — exact same-kernel cubic alias
Reconstruct the frozen G72 retarded symmetric cubic kernel. Form source-resolved tangent rows from all nonzero allowed kernel entries. Use identical columns for D and N3. Require exact rank one, exact equality `D-N3=0`, and at least two nonzero allowed entries.

### B — native support, permutation and CTP-normalization information cannot lift the alias
Augment the source-resolved design with:
- Sigma-leg permuted observations;
- forbidden advanced-support rows, which are zero for the frozen retarded kernel;
- `Delta=0` CTP-normalization rows, which are zero for both coordinates.
Require exact rank to remain one. Verify Sigma permutation symmetry and exact absence of advanced support in the candidate kernel.

### C — frozen jet information cannot lift an exact multiplicative cubic alias
Use the frozen cubic representative `G3=k(d0*s0^2 + 2 d0*s0*s1 + d1*s1^2)`. At zero/background both D and N3 have zero Hessian, while their third-derivative response vectors are identical. Build the combined Hessian/third-derivative tangent design and require exact rank one.

### D — positive/negative separability controls
Frozen controls:
1. Modify exactly one allowed entry of a second cubic kernel while keeping the original D kernel fixed: rank must become two.
2. Append a deliberately **non-native** direct calibration row `(D,N3)=(0,1)`: rank must become two.
3. Give a nuisance control one forbidden advanced-support entry while D remains retarded: rank must become two.
4. Append only a zero pseudo-calibration row `(0,0)`: rank must remain one.

## Frozen aggregate rule
If A/B/C/D all validate their predicates, terminal classification is:
`BLOCKED_D_NATIVE_SOURCE_OBJECT_DOES_NOT_BREAK_EXACT_CUBIC_CALIBRATION_ALIAS_SCOPED`.

A failed frozen mathematical predicate => `SCIENTIFIC_FAIL_FROZEN_D_NATIVE_ANCHOR_AUDIT`.
Missing/invalid artifacts or controls => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
A valid BLOCKED result means only that the already-frozen D construction does not itself provide an independent source/observable direction against the exact G74 same-shape cubic calibration nuisance. It does not invalidate D. A later D-specific construction must explicitly add or derive a genuinely independent calibration/source response before G75-style identifiability can be promoted beyond an abstract design.

No architecture selection, no physical detectability threshold, no candidate-owned nonlinear law, no readiness increase, no new physics. Readiness stays 66%; theory established stays 0%.
