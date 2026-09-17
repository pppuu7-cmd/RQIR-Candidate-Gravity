# RCG-006 — exact field-redefinition action-map implementation contract (PRE-MAP-OUTCOME)

Date: 2026-09-17
Status: **FROZEN AFTER GENERATOR COMPLETENESS FREEZE AND BEFORE ANY M_FR RANK/IMAGE OUTCOME**

Scientific preregistration: `fc3ff1f49c56f2befc039e09ebd8f388833dbff1`.
Generator completeness freeze: `8c8314d2b857d6caa9719d6ba33e856ea0a697af`.
Parent RCG005 quotient freeze: `f4d6f11490c0e668aa934e25580abad3015f0ae1`.

## Production generator order

Nine columns, frozen as:
- ALG raw pivots `[16,19,46,52,436,439]`;
- DER raw pivots `[1,30,46]`.

No post-map generator changes are permitted.

## L0 EH contraction convention

For covariant metric redefinitions use, up to one common nonzero EH normalization,

`E_cov^{ab} = -R^{ab} + (1/2) g^{ab} R`

at `Lambda=0`.

Every generator image is constructed in raw complete-contraction coordinates before any RCG005 quotient reduction.

For a free-output generator tensor `T_ab`:
- the `-R^{ab}T_ab` term is represented by tracing slots 0 and 2 of an added Riemann factor and joining its remaining Ricci slots 1 and 3 to the two free generator output slots;
- the `+(1/2)R g^{ab}T_ab` term is represented by scalar-tracing the added Riemann factor with `(0,2),(1,3)` and joining the two generator output slots, coefficient `+1/2`.

For an output-metric generator `T_ab=g_ab S`, combine the two terms exactly in four dimensions, giving the raw scalar-curvature image `+R S`.

Overall common EH normalization does not affect image span, but this sign convention is frozen and all exact coordinates are persisted.

## ALG image route

For ALG generators, retain generator Riemann slots 0..7 and use an added EH Riemann factor in slots 8..11. The resulting perfect matching is reduced only through the canonical frozen RCG005 cubic symmetry-class map.

## DER image route

A DER generator uses local slots `(d0,d1,R0,R1,R2,R3)`. Map them to the frozen RCG005 `R*nabla^2R` raw convention

`d0->4, d1->5, R0->6, R1->7, R2->8, R3->9`,

with the EH Riemann in slots 0..3.

After the exact EH contraction, every resulting `R*nabla^2R` scalar raw matching is bulk-reduced by the same parent one-integration-by-parts convention used by RCG005:

`0->1, 1->2, 2->3, 3->4, 4->0, 5->5, 6->6, 7->7, 8->8, 9->9`,

with the mandatory overall IBP coefficient `-1`.

Derivative-order commutator/cubic mixing is not separately guessed here; it is subsequently handled by the already-frozen full RCG005 25-column relation space.

## Frozen parent 25 -> 8 quotient transform

Reconstruct exactly the canonical RCG005 relation matrix on

`12 D1D1 canonical classes + 13 cubic canonical classes`.

Validity requires:
- exact relation rank `17`;
- exact relation RREF SHA256 `4b6f9b9713b076a10513adb1b10ab0bfc91b822acda441f976aee2f14a5fd38e`.

Use the frozen eight coordinate axes in raw 25-space:
- positions `9,11` for the derivative axes;
- positions `12+[0,1,2,4,5,8]` for inherited RCG004 axes.

Take the 17 nonzero independent rows of the exact RREF relation matrix. Concatenate the eight standard basis columns with the transpose of those 17 rows to form a `25 x 25` exact change-of-basis matrix. It must have rank 25. Its inverse gives the unique eight frozen quotient coordinates as the first eight components for every raw action vector.

No field-redefinition quotient is used in this reduction.

## Exact L0 outputs

Persist the exact `8 x 9` `M_FR` matrix, its SHA256, exact rank/kernel, ALG-only rank, full image RREF/span hash, and each generator column.

## Symbolic-Lambda companion (LS)

The `-Lambda g^{ab} Delta g_ab` term is tracked separately and never silently projected into the original eight-dimensional RCG005 quotient.

For ALG traces:
- mechanically enumerate the 105 scalar `Riemann^2` metric contractions;
- construct their exact universal generic-curvature matrix;
- mechanically generate the four-dimensional parity-even Euler/Gauss-Bonnet density by the antisymmetrized generalized-delta contraction rather than by choosing a remembered basis vector;
- quotient the pointwise scalar span by this exact bulk topological-density direction;
- use a deterministic exact pivot complement to define `Q_dim4_companion` coordinates.

For DER traces, every one-curvature/two-derivative scalar is classified as a bulk total divergence by factoring its outermost covariant derivative after all remaining indices are metric-contracted; verify this for every raw trace matching. Thus its LS bulk companion coordinate is zero, while the discarded divergence is recorded as boundary-sensitive and outside `BULK_ACTION_EQUIVALENCE`.

Persist companion dimension and exact `Lambda` leakage matrix/rank. L0 and LS results are reported separately; LS leakage cannot alter L0 `M_FR` rank.

## RCG004 intersection and EFT quotient

Let `I_FR=Im(M_FR)` in frozen 8D coordinates. The inherited RCG004 subspace is the span of coordinate axes 2..7.

Compute exact intersection dimension using rank identities. Compute `Q_EFT=Q_RCG005/I_FR` and choose the explicit complement by greedily scanning standard axes 0..7 and retaining the lexicographically first axes that increase rank over `I_FR` until a full complement is obtained.

## Frozen higher-derivative discriminator reconstruction

Rebuild `A_HD` without using the RCG006 image outcome:
- the RCG005 exact sixth-order map acts on coordinates 0..1 with
  `A6=[[-2,-2],[-2,0],[-2,0],[-2,-2],[-2,0],[-2,-2]]`;
- fifth-order map is zero on the inherited cubic subspace;
- reconstruct the canonical exact RCG004 `54 x 6` triaxial Hessian matrix directly from the frozen RCG004 quotient representatives `[0,1,2,4,5,8]` using the canonical RCG004 Constructor tensor route; require rank 6 and canonical matrix SHA256 `7014978a97fce634d93f00e414903597245b8e4268b2c575dd1764547f96ced9`.

The block-combined parent `A_HD` must have rank 8 and kernel zero before it is applied to `M_FR`.

Then compute `rank(A_HD*M_FR)` and the exact image-kernel dimension. A nonzero image with nonzero `A_HD` image is the preregistered representative-dependence branch, but no branch is selected before computation.

## Critic independence

The Critic must not import Constructor `M_FR` or its final matrix. It may independently regenerate all raw generator images in reverse ordering and independently reconstruct the parent quotient relation span. Compare final image subspaces by mutual rank containment, not column equality.

## No outcome yet

At this commit no `M_FR` column, rank, image, `Q_EFT` dimension, RCG004 intersection dimension, derivative-axis status or discriminator-invariance outcome has been computed canonically.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
