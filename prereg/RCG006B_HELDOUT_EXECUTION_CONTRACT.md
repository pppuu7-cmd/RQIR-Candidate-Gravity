# RCG-006B — execution contract for the already-preregistered exact held-out

Date: 2026-09-17
Status: **EXECUTION CONTRACT; NO NEW SCIENTIFIC CRITERIA**

Parent held-out preregistration: `43748579a78f40e0825d5ae01dc634d55ba7b928`.
Parent scientific preregistration: `fc3ff1f49c56f2befc039e09ebd8f388833dbff1`.
Canonical generator freeze: `8c8314d2b857d6caa9719d6ba33e856ea0a697af`.
Canonical L0 map terminal: `12ca52947d1390a494634b7a6a2d98d9a7e4bf7d`.

This file only makes the already-frozen held-out executable. It does not alter seeds, sample counts, generator family, quotient, map, PASS/FAIL logic or interpretation ceiling.

## Pre-outcome coordinate manifests recovered from frozen code identity

The held-out preregistration required lexicographic ordering in the implementation coordinate manifest before ranks were consumed. Those manifests already existed deterministically in the pre-outcome generator implementation:

- curvature coordinates: the 20 exact generic algebraic-curvature variables `p4.VN` used by the RCG004/RCG005/RCG006 universal tensor route;
- fourth metric jets: the 350 exact normal-coordinate variables `g6.H4K`, ordered as symmetric metric pair followed by fully symmetric four-derivative multi-index.

No coordinate is added, removed or reordered from those pre-outcome code-defined manifests. Their ordered string manifests and SHA256 hashes must be persisted by both held-out lanes.

No additional lower metric jets are needed for this validation implementation: derivative-generator **pre-IBP** first-order EH images are checked directly as `Riemann * nabla^2 Riemann` against the frozen fourth-jet bank, while the subsequent action-level IBP/relation quotient is checked as exact linear algebra rather than as pointwise equality of Lagrangian densities.

## Generator normalization lock

The physical output tensor represented by a free-output raw template is the exact normalized symmetrization

`T_(ab) = (T_ab + T_ba)/2`.

For an output-metric template it is `g_ab S`.

The pre-map rank code stored twice these physical component values because it used an unnormalized `p+q` symmetrization for span/rank construction. The factor two is common and rank/span-inert. For this held-out, divide that coefficient representation by exactly `2` before comparing to the physical tensor/action map. This is fixed by the ordinary normalized symmetrization and by the already-frozen M_FR contraction convention; it is not fitted to an outcome.

## Frozen banks

Use exactly the preregistered 64-bit recurrence and sample banks:
- Constructor seed `0x5243473030364341`, `32` samples;
- Critic seed `0x5243473030364352`, `32` samples;
- final cross-route seed `0x524347303036484f`, `16` samples.

A sample contains exactly the 20 curvature coordinates followed by the 350 fourth-jet coordinates. The all-zero-curvature regeneration rule from the parent held-out remains the only permitted resampling.

## Constructor validation route

For every Constructor-bank and final-bank sample:
1. evaluate all nine frozen production generator tensors by direct index contraction;
2. independently evaluate their frozen universal sparse coefficient representations and require exact component equality;
3. for every one of all `525` ALG and all `60` DER raw generators, require its exact universal coefficient representation to equal the exact combination of the frozen pivot columns, both algebraically and after held-out evaluation;
4. contract the exact EH tensor with each of the nine physical generator tensors and compare with an independently evaluated raw first-order EH image: cubic raw matching for ALG and pre-IBP `R*nabla^2 R` raw matching for DER;
5. reconstruct the frozen `25 -> 8` quotient map, require the canonical relation rank/hash, and require all nine quotient columns to equal the persisted canonical `M_FR` exactly;
6. for a deterministic held-out linear combination of the nine generators, compare the quotient coordinates from raw-25 reduction against direct multiplication by canonical `M_FR`.

## Independent Critic route

The Critic uses the separate Critic bank and regenerates the final bank independently. It reconstructs raw generators in reverse pairing order, independently locates the frozen physical raw templates, rebuilds the parent relation quotient, and checks the same tensor/action/quotient identities without importing any Constructor held-out artifact or tensor array.

Constructor and Critic may import the already-frozen scientific code and canonical terminal M_FR authority; they may not import each other's held-out outputs.

## Negative controls

Each lane must demonstrate that it detects at least:
- a sign-flipped EH Ricci contraction;
- a perturbed canonical quotient column;
- a perturbed generator-representation coefficient.

These are detection controls only and never alter the frozen result.

## Terminal classifier

`PASS_SCOPED_RCG006B_GENERIC_METRIC_JET_HELDOUT`

iff every exact comparison in the lane banks and final cross-route bank succeeds, the final-bank manifest/hash agrees across independent lanes, all negative controls are detected, and the canonical parent relation/map identities remain unchanged.

Any exact disagreement with valid infrastructure gives
`INVALID_RCG006B_HELDOUT_VALIDATION`.

No tolerance, refit, pivot change, generator addition/deletion or map change is permitted.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
