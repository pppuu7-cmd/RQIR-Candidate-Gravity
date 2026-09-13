# Iter085 / G87 — D nonlinear-completion nonuniqueness audit

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13
Parallel status: **D-SPECIFIC SIBLING OF G86-C; COMMON BASE IS POST-G85 MAIN**

## Scope
G69 remains blocked because candidate-owned beyond-baseline nonlinear dynamics have not been defined. The D branch currently fixes a non-Gaussian CTP cubic/three-point sector with retarded support, Sigma-leg symmetry, CTP normalization and the audited zero-Hessian/nonzero-third-derivative jet. G87 asks a prior question that must be settled before choosing a nonlinear law:

> Do the frozen D data through cubic order uniquely determine the quartic nonlinear completion?

The audit is deliberately a nonuniqueness/underdetermination test. It does **not** select a quartic law. A valid demonstration that distinct quartic additions preserve the frozen lower jet is classified as `BLOCKED/UNDERDETERMINED`, not as a failure of D.

## Frozen lower D jet and completion witnesses
Use the frozen D cubic representative already employed in G71/G72:
`G3(d0,d1,s0,s1)=d0*s0^2 + 2*d0*s0*s1 + d1*s1^2`.

For the higher-order freedom, use a two-channel reduced slice `(x,y)` as an exact algebraic witness. Two prospectively frozen quartic additions are
- `A4(x,y)=x^4`, representing the reduced jet shape of a generally covariant local scalar-density addition of schematic curvature-quartic type `sqrt(-g) R^4`;
- `B4(x,y)=x^2 y^2`, representing the reduced jet shape of a distinct curvature-quartic scalar-density addition of schematic type `sqrt(-g) R^2 R_{mu nu}R^{mu nu}`.

Around a flat background, curvature-quartic additions begin at fourth perturbative order and therefore do not alter derivatives through cubic order. The reduced `(x,y)` slice is a finite witness only; no claim is made that it is a complete quartic invariant basis modulo integrations by parts, nonlinear field redefinitions, or dimension-specific identities.

For CTP normalization, lift each quartic witness as an action-difference term
`Delta A4=A4(x_+,y_+)-A4(x_-,y_-)` and similarly for `B4`. These additions vanish exactly on equal histories.

Frozen nonzero coefficients: `lambda in {-2,1,3}`.
Frozen invertible linear reparameterizations on `(x,y)`:
`R1=[[1,1],[0,1]]`, `R2=[[2,0],[1,1]]`, `R3=[[1,-1],[1,2]]`, `R4=[[-1,2],[1,1]]`.

## Independent streams
### A — exact lower-jet preservation
At the flat/background point, for each frozen nonzero lambda and for both quartic witnesses require:
- all derivatives of the quartic addition through total order three vanish exactly;
- the fourth-derivative tensor is nonzero;
- adding the quartic witness leaves the complete frozen D cubic jet of `G3` unchanged through third order.

### B — distinct quartic-jet shapes and coordinate robustness
Construct the symmetric fourth-derivative tensors of `A4` and `B4` and mode-1 flattenings.
Require:
- flattening rank of `A4` is exactly one;
- flattening rank of `B4` is exactly two;
- after every frozen invertible linear reparameterization, those ranks remain one and two respectively;
- the two fourth-order tensors are not proportional.

This proves only inequivalence under the frozen invertible linear coordinate class on the reduced jet slice.

### C — CTP normalization and preservation of the audited D cubic structure
For `Delta A4` and `Delta B4`, require exactly:
- vanishing on equal histories;
- odd sign under `+/-` branch exchange;
- zero derivatives through cubic order at the doubled flat background;
- nonzero fourth derivative.

Independently verify that the frozen D representative `G3` still has zero Hessian and nonzero third derivative at the background. The higher-order witness is block-separate and does not modify the G72 retarded cubic kernel used in the prior audits.

### D — adversarial order and trivial-family controls
Frozen controls:
1. a cubic addition `nu x^3` with `nu=1` must alter the third-order jet and therefore be rejected as a lower-jet-preserving quartic completion;
2. `A4` and `2 A4` must be detected as proportional/same quartic shape family rather than counted as two independent shape witnesses;
3. a zero quartic addition must not create a nonzero fourth-order completion direction;
4. singular coordinate transforms are rejected from the frozen reparameterization class.

## Frozen aggregate rule
All streams valid =>
`BLOCKED_D_FROZEN_CUBIC_DATA_ADMIT_MULTIPLE_QUARTIC_CTP_COMPLETIONS_SCOPED`.

Any failed frozen mathematical predicate => `SCIENTIFIC_FAIL_FROZEN_D_NONLINEAR_NONUNIQUENESS_PREDICATE`.
Missing/invalid controls/artifacts => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
A valid BLOCKED result means only that the frozen D cubic/three-point information does not, by itself, select a unique quartic nonlinear extension: higher-order freedom survives while the audited lower jet and CTP normalization remain unchanged. It does not establish a complete generally covariant nonlinear D theory, prove inequivalence modulo arbitrary nonlinear field redefinitions, prove retarded/unitary/measure closure of the quartic additions, or select either witness as physical.

Readiness remains 66%; theory established remains 0%.
