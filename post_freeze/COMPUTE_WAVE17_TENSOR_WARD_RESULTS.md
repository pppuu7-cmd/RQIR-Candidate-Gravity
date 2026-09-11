# Compute Wave 17 — Tensor Ward/Gauge Results

**Run:** `34658827796`  
**Branch:** `rqir-tensor-ward-wave17`  
**Commit:** `5b853bb1617eb7a28c25a15e891f44b17d55cf79`  
**Status:** 8/8 primary jobs + aggregator SUCCESS; all predeclared signals true.

## Main rank result

For the six symmetric-tensor projector directions

`P2, P1, P0s, P0w, P0sw, P0ws`, generic sources give rank 6. Imposing explicit conserved sources gives

- conserved-source rank = **2**;
- conserved-source nullity = **4**;
- surviving physical sectors = `P2` and `P0s`;
- longitudinal/mixed column norms are at numerical-noise scale (~1e-16).

Thus the frozen conservation/Ward gate has real tensor-level constraining power, but it leaves two independent transverse structures.

## GR/IR normalization

Using

`f2(x)=c2+a1 x+a2 x^2`, `f0(x)=c0+b1 x+b2 x^2`,

with exact GR IR constraints `c2=1`, `c0=-1/2`:

- constraint rank = **2**;
- remaining parameter nullity = **4**;
- at `x=0.45`, tested controlled deformations give width `Δf2 = 0.12645`, `Δf0 = 0.12105` while preserving the exact IR normalization.

Therefore the weak-field/GR limit fixes the massless residue combination but not finite-momentum form-factor shape.

## Prospective tensor holdout

A one-observable finite-q design calibration has rank 1 and nullity 1 in the two slope variables `[a,b]`. Two candidates were constructed with design width only `1.11e-16` but untouched holdout width

**0.8086034019545179**,

with holdout sensitivity to the design-null direction **1.1551477170778832**.

The surviving freedom is therefore physical/observable, not a pure gauge direction.

## Comparator result

A conventional low-energy EFT control spans both surviving transverse slope directions. Pole exclusion also fails to select a unique form because pole-free form-factor families remain. Tensor projectors, Ward decoupling, GR residue matching, generic form factors and pole/spectral technology receive no novelty credit by themselves.

## Authoritative verdict

`frozen_RQIR_tensor_gates_have_real_rank_power = true`

`frozen_RQIR_plus_GR_IR_uniquely_fix_transverse_form_factors = false`

`residual_tensor_freedom_is_gauge_only = false`

`residual_tensor_freedom_is_already_C5_EFT_compatible = true`

`candidate_new_QG_primitive_found = false`

Next step: compare independently motivated extra-hypothesis classes acting on the physical transverse form factors. Any relation chosen only because it removes the observed Wave-17 null direction is rejected as retrofit.
