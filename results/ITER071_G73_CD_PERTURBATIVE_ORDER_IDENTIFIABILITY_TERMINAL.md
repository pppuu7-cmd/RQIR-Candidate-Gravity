# Iter071 / G73 terminal result

Date: 2026-09-13
Classification: `CD_ORDER_SEPARATED_DIRECTIONS_JOINTLY_IDENTIFIABLE_ONLY_WITH_MULTIORDER_PANEL_SCOPED`
Scientific status: **PASS, scoped**
Programme readiness: **66%**
Theory established: **0%**

## Frozen authority
Preregistration: `535c98499af94c8457767972c40c17304d500509`
Implementation: `ee16c8ed2c0d0d31527bb098c715c59ac26fa8df`
Production head: `0cdbf009e1d0691aaf5d756b32e80326b593c781`
Run: `34776467784`
Aggregate job: `103775419685`
Aggregate artifact: `10323586719`
Aggregate digest: `sha256:6b3864119e485658b193f4c1c0eedd496c91ea2a295468ba879c15d4c67da5bd`

Raw artifacts consumed before classification:
- A artifact `10324136045`, digest `sha256:2b8844fc8692e905b03d8817e5066fdfdec1f97021e1e081c0440697735316a4`: exact joint rank 2; quadratic-only rank 1; cubic-only rank 1.
- B artifact `10323742027`, digest `sha256:2c92c70d8e3b46ed4413e5836bbb87fcb0c3a36a0503b0e7eb17e8a66f04300c`: exact quadratic/cubic jet-order separation.
- C artifact `10323956508`, digest `sha256:010d7f73281ef1b8a945683604e29ddc7f2a9fc63042adc434a8a4e30bdbde27`: rank 2 preserved under all four frozen invertible rational reparameterizations.
- D artifact `10323164946`, digest `sha256:d2a3ba09ab7469795309579641e4b65076261a3fa1a07aae6470747850ebd146`: zero-momentum and single-order rank-loss controls detected; order-leakage control detected.

## Scientific classification
For the prospectively frozen G72 representatives, the C deformation tangent occupies the quadratic/two-point block and the D deformation tangent occupies the cubic/three-point block. Their joint local Jacobian has exact rank 2 only when the observable panel spans both perturbative orders. Omitting either order reduces rank to 1. The result is invariant under the frozen invertible parameter-basis changes.

## Scope ceiling
This is a local identifiability statement for frozen hypothesis representatives only. It does **not** select C or D, establish candidate-owned RCG-002 dynamics, determine physical coefficients, validate nonlinear completion or quantization, or establish new physics.

## Next admissible question
G73 assumed the relevant same-order baseline/nuisance directions were absent or independently fixed. The next useful discriminator is therefore an exact same-order nuisance-confounding audit: determine which nuisance tangent shapes alias C or D, which do not, and what nuisance anchors are minimally required before either architecture direction can be claimed identifiable.
