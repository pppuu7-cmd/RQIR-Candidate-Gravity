# RCG-006 — bounded local metric field-redefinition / EFT-equivalence audit v0 (PREOUTCOME)

Date: 2026-09-17
Status: **PROSPECTIVELY FROZEN BEFORE ANY RCG006 GENERATOR-RANK / M_FR / IMAGE / EFT-QUOTIENT / DISCRIMINATOR OUTCOME**

Programme selection terminal:
`dc955720822d353d446186437ee2ca69458633bd`

Selected direction:
`FIELD_REDEFINITION_EQUIVALENCE_AUDIT`

Parent scientific terminal:
`aef9882924ffd128c6c30934e4f95394aae874fc`

Parent action-space quotient freeze:
`f4d6f11490c0e668aa934e25580abad3015f0ae1`

Version:
`RCG006_BOUNDED_LOCAL_METRIC_FIELD_REDEFINITION_EFT_EQUIVALENCE_AUDIT_V0`

This is a structural audit of the already-terminal RCG005 action space. It is not a new gravity theory family and cannot retroactively refit or reclassify RCG005.

## Frozen scientific questions

At first order in a perturbative local metric redefinition

`g_ab -> g_ab + epsilon Delta g_ab`,

with `Delta g_ab` a complete bounded local parity-even symmetric rank-2 tensor of engineering dimension four, determine exactly:

1. the universal generator-space quotient dimension `M`;
2. the exact first-order EH field-redefinition map `M_FR` into the frozen eight-dimensional RCG005 action quotient;
3. `rank(M_FR)`, kernel, image span and the quotient `Q_EFT = Q_RCG005 / Im(M_FR)`;
4. nested algebraic-only and full-generator image ranks;
5. `dim(RCG004_subspace intersect Im(M_FR))` and the residual nonredundant cubic quotient;
6. the exact status of frozen derivative axes `D1D1_CLASS_9` and `D1D1_CLASS_11` relative to the image;
7. whether the frozen RCG005 off-shell >2-derivative discriminator changes along admitted field-redefinition orbits.

## EFT order and invertibility lock

Only first order in `epsilon` is in scope. All `O(epsilon^2)` terms are forbidden.

Every admitted transformation is interpreted as perturbatively near-identity and order-by-order invertible. No nonlocal inverse, curvature division, background-specific inverse or singular transformation is admitted.

## Reference action and Lambda strata

Use the same lower-order reference convention as RCG005:

`S_ref = S_EH+Lambda`.

For a covariant-metric variation, freeze

`E_cov^{ab} = -(G^{ab} + Lambda g^{ab})`

up to the common nonzero EH normalization, so

`delta S_ref = integral sqrt(|g|) E_cov^{ab} Delta g_ab + boundary`.

Two strata are frozen **before outcome**:

### L0
`Lambda = 0`.

This is the primary closed map into the original frozen `Q_RCG005`.

### LS
`Lambda` symbolic with engineering dimension two.

The full first-order image is tracked in the direct sum

`Q_RCG005 + Lambda * Q_dim4_companion`.

The `Q_RCG005` projection must be reported separately from the `Lambda`-weighted curvature-squared / derivative companion sector. Nonzero LS leakage outside the original eight-dimensional RCG005 space must be reported as non-closure, never silently dropped or used to change the L0 rank.

No outcome-dependent switch between L0 and LS is permitted.

## Complete generator family

`Delta g_ab` is local, parity even, symmetric, pure metric and of engineering dimension four.

The raw generator is defined mechanically from **all** complete metric contractions leaving exactly two free symmetric output indices for the only two engineering partitions:

- `ALG (2,2)`: two Riemann tensors, including the output-metric times a fully contracted curvature-squared scalar;
- `DER (4)`: one twice-covariantly-differentiated Riemann tensor `nabla nabla Riemann`, including the output-metric times every complete scalar contraction.

For each partition enumerate every placement of the two free output slots and every perfect matching of all remaining tensor slots. The output pair is symmetrized exactly. Single-epsilon parity-odd structures are excluded; parity-even double-epsilon structures are reduced to the generalized-delta / metric-contraction span and checked as a control.

No memorized list such as `R R_ab`, `R_ac R^c_b`, `Box R_ab`, etc. defines the family; familiar tensors may appear only as regression controls after mechanical enumeration.

No arbitrary functions, inverse boxes or infinite derivative series are allowed.

## Universal generator equivalence

Before constructing the action map, quotient generator tensors only by universal exact identities:
- Riemann algebraic symmetries and pair exchange;
- algebraic Bianchi;
- differential Bianchi and its exact covariant derivatives;
- covariant-derivative commutators, retaining their generated curvature-squared tensors in the same generator class;
- exact four-dimensional dimension-dependent identities;
- exact duplicate contractions;
- output-index symmetry;
- exact parity-even double-epsilon reduction.

Forbidden generator quotient relations:
- equations of motion / on-shell substitution;
- Bianchi-I or any background-specific identity;
- finite-sample identity without exact reconstruction/certificate.

The Constructor must persist raw template counts, symmetry-class manifests, exact universal tensor coefficient matrices, relation/span hashes, deterministic pivot basis and the independent generator-space dimension `M`.

### Principal/lower-order separation for DER completeness

The derivative-generator quotient may be certified by an exact filtered construction. Its highest metric-jet part is reconstructed from universal normal-coordinate fourth metric jets (symmetric metric pair and symmetric four derivative indices). The antisymmetric derivative-order part is then reconstructed exactly from the covariant-derivative commutator into the ALG curvature-squared sector. Therefore a DER relation is accepted only if both its principal fourth-jet part and its exact lower ALG commutator remainder vanish in the combined universal generator space.

## Nested generator subspaces

Freeze before outcome:
- `FR_ALG`: algebraic curvature-squared generators only;
- `FR_FULL`: `FR_ALG` plus all derivative generators.

Report `rank(M_ALG)`, `rank(M_FULL)`, and quotient dimensions after each.

## Exact first-order action map

Construct

`M_FR : Q_generator -> Q_RCG005`

in L0 by exact contraction of `E_cov^{ab}` with every generator representative, followed by reduction through the **same frozen RCG005 v0 action equivalence** used to produce the eight-dimensional parent quotient. Field-redefinition equivalence itself is not applied until after this map exists.

For algebraic generators, the image is reduced in the frozen cubic raw/action quotient. For derivative generators, the `Riemann * nabla^2 Riemann` image is reduced by exact integration by parts and the frozen differential/commutator relations into the same 25-column derivative-plus-cubic raw parent space, then into the frozen 8D coordinates.

Persist:
- exact matrix shape and entries;
- rank;
- kernel dimension and basis;
- image RREF/span certificate;
- exact coordinates of every deterministic generator-basis image;
- matrix SHA256;
- image-span SHA256.

No float rank or SVD.

## Frozen parent coordinates

Do not regenerate the RCG005 quotient. Use the canonical frozen basis:
- derivative axes `D1D1_CLASS_9`, `D1D1_CLASS_11`;
- inherited RCG004 cubic axes with canonical class indices `[0,1,2,4,5,8]`.

The exact RCG005 relation-span hash must equal
`4b6f9b9713b076a10513adb1b10ab0bfc91b822acda441f976aee2f14a5fd38e`.

Any parent mismatch => `INVALID_RCG006_FIELD_REDEFINITION_AUDIT_PARENT_MISMATCH`.

## RCG004 intersection and derivative-axis status

Compute exactly:

`dim(RCG004_subspace intersect Im(M_FR))`.

Report the residual dimension of the inherited six-dimensional cubic quotient modulo that intersection.

For each of `D1D1_CLASS_9` and `D1D1_CLASS_11`, classify exactly as one of:
- `IN_IMAGE`;
- `NOT_IN_IMAGE_BUT_NONZERO_PROJECTION_MOD_IMAGE`;
- `INDEPENDENT_MOD_IMAGE`;
with exact rank/span witnesses. Do not infer from familiar operator names.

## EFT quotient

Define

`I_FR = Im(M_FR)`
`Q_EFT = Q_RCG005 / I_FR`.

Persist `dim Q_RCG005 = 8`, `dim I_FR`, `dim Q_EFT`, and a basis-independent quotient certificate. If explicit representatives are needed, choose the lexicographically first rational-RREF complement; this is a deterministic representation only, not a uniquely physical basis.

## Higher-derivative discriminator transport

Reconstruct the frozen RCG005 higher-derivative linear map `A_HD` from canonical parent data, including the exact A6/A5/A4 cascade sufficient to certify its kernel. First verify independently that

`ker(A_HD) = {0}`

on the frozen eight-dimensional parent space.

Then evaluate `A_HD * M_FR` and report:
- rank on `Im(M_FR)`;
- kernel dimension on the field-redefinition image;
- whether a nonzero admitted EFT orbit direction changes the representative-level higher-derivative classification.

Frozen structural classes:
- `CASE_I_IMAGE_ZERO` if `Im(M_FR)={0}`;
- `CASE_II_NONINVARIANT` if image is nonzero and `A_HD(Im(M_FR))` is nonzero, with orbit directions changing representative classification;
- `CASE_III_INVARIANT_ON_IMAGE` if image is nonzero but entirely derivative-order-null;
- `CASE_IV_MIXED` if exact substructure is mixed.

Because the zero correction/EH representative is second order, a nonzero image vector with nonzero `A_HD` is recorded explicitly as
`REPRESENTATIVE_NONZERO / EFT_QUOTIENT_ZERO`.

This does not contradict RCG005; it diagnoses representation dependence.

## Quotient-aware second-order question

Replay `S_SO = ker(A_HD)` exactly in the new formalism, then compute its image in `Q_EFT`. The zero/EH equivalence class is never counted as a nonzero survivor.

## Independent Critic

The Critic must not import Constructor final generator matrices or `M_FR`. It independently reconstructs:
- raw generator enumeration in reverse/different ordering;
- universal ALG quotient using an independent generic-curvature parametrization;
- DER principal quotient using independently constructed exact normal-coordinate metric fourth jets;
- commutator completion into ALG;
- first-order EH image span;
- exact image rank and `Q_EFT` dimension;
- `A_HD` orbit effect.

Compare exact spans/ranks, not column order or chosen pivot labels. Disagreement => INVALID until resolved.

## Frozen generic-jet validation

A separate held-out file freezes deterministic exact rational metric-jet seeds before production matrix ranks. Held-out jets validate reconstructed generator tensors and action-map representatives without refit. Finite jets alone are not a universal identity proof; terminal evidence requires the exact coefficient/reconstruction matrices above.

## Negative controls

The audit must detect at least:
1. one omitted raw generator;
2. one duplicate generator;
3. nonsymmetric output contamination;
4. wrong engineering dimension;
5. parity-odd contamination;
6. nonlocal/inverse-box contamination;
7. on-shell substitution before `M_FR`;
8. background-specific identity;
9. missing IBP/boundary term in the bulk map;
10. wrong `E_cov` sign convention;
11. wrong density variation convention;
12. generator-basis column permutation;
13. RCG005 coordinate permutation;
14. derivative-commutator sign flip;
15. accidental Bianchi-I restriction;
16. singular/noninvertible redefinition;
17. `O(epsilon^2)` contamination;
18. post-outcome generator addition;
19. zero EFT class misreported as a physical survivor;
20. any attempted retroactive rewrite of the RCG005 terminal.

## Bulk/boundary and matter firewalls

RCG006-v0 establishes only `BULK_ACTION_EQUIVALENCE` at first perturbative order. `BOUNDARY_OBSERVABLE_EQUIVALENCE` is out of scope.

Source remains `VACUUM_ZERO`. No conclusion is generalized to matter-coupled observables, because metric field redefinitions may shift matter couplings.

## Frozen scientific classifiers

Allowed terminal scientific classifications:
- `PASS_SCOPED_RCG006_FIELD_REDEFINITION_EQUIVALENCE_AUDIT_COMPLETE_INVARIANT_DISCRIMINATOR`;
- `PASS_SCOPED_RCG006_FIELD_REDEFINITION_EQUIVALENCE_AUDIT_COMPLETE_NONINVARIANT_DISCRIMINATOR`;
- `PASS_SCOPED_RCG006_FIELD_REDEFINITION_EQUIVALENCE_AUDIT_COMPLETE_MIXED_STRUCTURE`;
- `BLOCKED_RCG006_FIELD_REDEFINITION_AUDIT_*`;
- `INVALID_RCG006_FIELD_REDEFINITION_AUDIT_*`.

`PASS` means the structural audit completed under the frozen contract; it does not mean a gravity candidate passed.

## Claim locks

RCG005 remains exactly:
`FAIL_SCOPED_RCG005_COMPLETE_LOCAL_DIM6_PURE_METRIC_CLASS_HAS_NO_NONZERO_SECOND_ORDER_SURVIVOR`
under its frozen v0 representative-level convention.

RCG006 may establish that some failing representatives are EFT redundant and/or that the off-shell derivative-order discriminator is representation dependent. Neither statement retroactively changes RCG005.

Do not claim nonperturbative theory identity, equal global solution spaces, equal quantum measures, equal boundary observables or equal causal structures.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
