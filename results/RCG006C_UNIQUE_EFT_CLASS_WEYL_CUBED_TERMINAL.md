# RCG-006C — unique EFT quotient class is parity-even Weyl-cubed

Date: 2026-09-17
Status: **TERMINAL SCOPED IDENTITY BRIDGE**

Prospective preregistration: `1122988893e9d5f87771da8a6390f031be8fafca`.
Parent L0 field-redefinition map terminal: `12ca52947d1390a494634b7a6a2d98d9a7e4bf7d`.

The initial workflow failed before science on an exact-zero accumulator implementation defect; the prospective repair is recorded in `results/RCG006C_WEYL_BRIDGE_EXECUTION_ONLY_REPAIR.md`. A later aggregate-only failure was caused solely by a missing SymPy dependency and is recorded in `results/RCG006C_WEYL_BRIDGE_AGGREGATE_EXECUTION_REPAIR.md`. Neither repair changed the scientific object or classifier.

Canonical repaired run: `35252716318`, head `6ac996aaf2201d659e4afc0d43a2242f74fbc069`.

Jobs:
- Constructor `105308702775` — success;
- independent bivector Critic `105308702994` — success;
- aggregate `105309520064` — success.

Artifacts:
- Constructor `10512180305`, digest `sha256:30ee8781395e1cfa87d4cde9fe24cf63448529eb0804d9fc3d2aafe2d61013e0`;
- Critic `10511056595`, digest `sha256:7b770a7c77af501a4f4857bad551ac732afda9152c43fa415b97fa1fea9540d6`;
- aggregate `10511391763`, digest `sha256:e241ed69c6e08a6cbea443d3ba6441857835da6d1271d6d6f2a13772bc89e52e`.

Canonical raw/provenance: `results/raw/RCG006C_WEYL_CUBED_BRIDGE_CANONICAL.json`.

Classification:

**`PASS_SCOPED_RCG006C_UNIQUE_EFT_CLASS_IS_PARITY_EVEN_WEYL_CUBED`**.

## Exact identity bridge

The Constructor mechanically constructs the four-dimensional Weyl tensor from the exact generic algebraic Riemann tensor and then contracts the parity-even cubic invariant. In the frozen six-dimensional RCG004 cubic quotient basis `[0,1,2,4,5,8]`, its coordinates are

`(-17/18, 7, -1/2, -6, 6, 1)`.

The independent Critic computes the same invariant as the cubic trace of the Weyl operator on the six-dimensional bivector space and obtains

`(-17/144, 7/8, -1/16, -3/4, 3/4, 1/8)`,

which is exactly `1/8` of the Constructor vector. The two routes therefore agree on the same nonzero projective invariant and, crucially, on the same one-dimensional EFT quotient ray without sharing the final contraction normalization.

Both routes independently extend the seven-dimensional `Im(M_FR)` to full rank eight. Therefore the mechanically constructed parity-even Weyl-cubed invariant is not field-redefinition redundant and spans the unique one-dimensional quotient

`Q_EFT = Q_RCG005 / Im(M_FR)`.

The exact quotient relations are

**`[Weyl^3] = [RCG004_CANONICAL_AXIS_8]`**

and

**`[Weyl^3] = (4/3)[D1D1_CLASS_11]`**

modulo `Im(M_FR)`.

Equivalently, the previously frozen relation remains

`[D1D1_CLASS_11] = (3/4)[Weyl^3]`.

## Scientific meaning

The one nonredundant first-order local parity-even pure-metric bulk EFT correction class left after the complete RCG006-v0 field-redefinition quotient at this engineering dimension is precisely the parity-even Weyl-cubed class.

This is an operator-identity result, not a candidate-theory viability result. It does not make the Weyl-cubed coefficient nonzero, preferred, ghost-free, stable, causal, ultraviolet complete, quantum-consistent or phenomenologically supported.

It also does not authorize treating Weyl-cubed as the next RQIRCG candidate model class without a separate prospective selector.

## External consistency note

This exact repository result is structurally consistent with the standard four-dimensional gravitational EFT organization in which Ricci/scalar-curvature operators can be removed by local field redefinitions in vacuum while Weyl-tensor operators carry the nonredundant pure-gravity content. That literature agreement is corroboration only; the exact bridge verdict above comes from the frozen repository calculation.

## Ceiling

Bulk action, first perturbative order, local pure metric only. No boundary-observable equivalence, matter equivalence, global solution-space equivalence, causal equivalence, quantum-measure equivalence or nonperturbative theory identity is established.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
