# RCG-006 — exact analytic consequences of the terminal L0 M_FR map

Date: 2026-09-17
Status: **EXACT ANALYTIC CONSEQUENCES; IMPLEMENTATION CROSS-CHECKS RUN SEPARATELY**

Authority used:
- RCG006 scientific preregistration `fc3ff1f49c56f2befc039e09ebd8f388833dbff1`;
- frozen map contract `78789e048ab3d67fc8f2e901176ff3a352aad749`;
- terminal L0 map result `results/RCG006_MFR_L0_MAP_TERMINAL.md`, commit `12ca52947d1390a494634b7a6a2d98d9a7e4bf7d`;
- terminal RCG005 parent facts, including exact derivative block rank `2` and inherited cubic triaxial Hessian rank `6`.

No partial value from a non-terminal workflow is used here.

## Lemma 1 — the frozen parent discriminator is injective on the full 8D parent quotient

The frozen RCG006 implementation contract reconstructs the RCG005 higher-derivative discriminator on the eight parent coordinates as two disjoint exact blocks:

1. on derivative coordinates `0..1`, the sixth-order block is

`A6=[[-2,-2],[-2,0],[-2,0],[-2,-2],[-2,0],[-2,-2]]`,

with exact rank `2`;

2. on inherited cubic coordinates `2..7`, the canonical RCG004 triaxial Hessian block has exact rank `6`.

The fifth-order map is zero on the inherited cubic subspace and does not mix the two coordinate blocks in this frozen cascade.

Therefore the combined frozen discriminator has

**`rank(A_HD)=2+6=8`**

on an eight-dimensional domain, hence

**`ker(A_HD)={0}`**.

This is a rank theorem from already-terminal parent facts; it does not depend on the RCG006 image outcome.

## Lemma 2 — exact transport rank is forced by injectivity

The terminal RCG006 L0 map gives

`rank(M_FR)=7`.

Because `A_HD` is injective on the entire parent quotient,

`A_HD M_FR x = 0`

implies

`M_FR x = 0`.

Hence

**`ker(A_HD | Im(M_FR))={0}`**

and therefore

**`rank(A_HD M_FR)=rank(M_FR)=7`**.

Thus every nonzero first-order EH field-redefinition image direction is nonzero under the frozen representative-level higher-derivative discriminator.

The preregistered structural branch forced by these exact facts is

**`CASE_II_NONINVARIANT`**.

Equivalently, there exist directions with

`REPRESENTATIVE_NONZERO / EFT_QUOTIENT_ZERO`.

This is not a contradiction with RCG005. RCG005 classified representatives under its frozen v0 convention; RCG006 shows that this representative-level derivative-order discriminator is not invariant along admitted first-order EFT field-redefinition orbits.

## Lemma 3 — quotient-aware second-order survivor space is zero

The frozen representative-level second-order space is

`S_SO = ker(A_HD) = {0}`.

Its image in the one-dimensional EFT quotient is therefore also zero.

So the field-redefinition quotient does **not** manufacture a nonzero second-order gravity correction. Rather, it reveals that many representative-level higher-derivative failures are redundant orbit directions while one nonredundant EFT class remains.

## Lemma 4 — symbolic-Lambda ALG companion is surjective onto the 4D curvature-squared bulk quotient

The complete frozen ALG generator family contains output-metric tensors

`Delta g_ab = g_ab S`

for every mechanically enumerated parity-even curvature-squared scalar contraction `S` in the frozen dimension-four generator class.

Tracing gives exactly in four dimensions

`g^{ab} Delta g_ab = 4 S`.

Therefore the trace map from the complete ALG generator space onto the pointwise parity-even curvature-squared scalar span is surjective.

The exact four-dimensional pointwise scalar span has dimension `3`; quotienting the action by the Euler/Gauss-Bonnet topological density leaves a two-dimensional bulk companion.

Hence the symbolic-Lambda algebraic leakage has forced rank

**`rank(Lambda leakage_ALG)=2`**

in `Q_dim4_companion`.

This conclusion is basis-independent. The queued mechanical generalized-delta implementation remains an independent exact cross-check of the scalar rank, Euler direction and frozen pivot coordinates.

## Lemma 5 — DER symbolic-Lambda traces are bulk total divergences

Every DER generator trace is a fully metric-contracted scalar containing one twice-covariantly differentiated Riemann tensor. Because the metric is covariantly constant, the outermost covariant derivative can be factored from the fully contracted expression:

`metric contractions * nabla_a nabla_b Riemann = nabla_a(metric contractions * nabla_b Riemann)`.

Thus every DER trace contributes only a boundary-sensitive total divergence to the symbolic-Lambda term and has zero coordinate in the frozen **bulk** `Q_dim4_companion`.

Therefore the full symbolic-Lambda bulk leakage rank remains

**`rank(Lambda leakage_FULL)=2`**.

This does not alter the already-terminal `Lambda=0` result `rank(M_FR)=7`.

## Scientific consequence

Combining only terminal L0 authority and already-terminal parent ranks:

- `dim Q_RCG005 = 8`;
- `dim Im(M_FR) = 7`;
- `dim Q_EFT = 1`;
- the frozen representative-level discriminator is injective on the parent space;
- its transport along `Im(M_FR)` has rank `7`;
- the discriminator is therefore not invariant along admitted first-order EFT orbits;
- the one-dimensional nonredundant EFT quotient remains, but no nonzero representative lies in the frozen second-order kernel;
- at symbolic `Lambda`, a separate two-dimensional curvature-squared bulk companion is generated by algebraic traces, while derivative traces are boundary terms.

## Ceiling

These lemmas remain first-order local bulk-action statements. They do not establish boundary-observable equivalence, matter-coupled equivalence, quantum-measure equivalence, global solution-space equivalence, causal equivalence or nonperturbative theory identity.

They do not establish a new gravity theory or quantum gravity.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.

The queued A_HD and symbolic-Lambda workflows are implementation/provenance cross-checks required before full RCG006-v0 terminal assembly; their partial values must not be consumed.
