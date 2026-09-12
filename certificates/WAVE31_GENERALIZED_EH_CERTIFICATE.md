# Wave 31 — Generalized-EH Residual-Rank / Baseline-Quotient Certificate

Status: **FROZEN CLEAN RESULT**

Date: 2026-09-12

## Authority

- Branch: `generalized-eh-wave31`
- Frozen evidence commit: `e1bd654ba96bb599afe346327da68ad85f787889`
- Frozen preregistration commit: `06b375711ff2288f6133e7084039c0214f89030c`
- Initial compute commit: `010c913ecea0269fca3072e6441831d8a219d82b`
- Infrastructure-only NumPy API repair: `ac30ea2515e7029f5122a05470ccd62c81f5a120`
- Clean GitHub Actions run: `34665447413`
- Primary jobs: 7/7 SUCCESS
- Aggregator: SUCCESS
- All preregistered signals: TRUE

The first run `34665411277` is retained as a fail-closed infrastructure record. Its only failure was use of removed `numpy.trapz`; the replacement with `numpy.trapezoid` changed no scientific formula, threshold, test function, or preregistered criterion.

## Result

1. Under the declared boundary/asymptotic conditions, for an analytic linear-curvature term
   `integral sqrt(g) F(Delta) R`,
   every positive integer power `Delta^n R`, `n>=1`, integrates to a boundary term. After quotienting the classical Einstein-Hilbert normalization, this finite local analytic linear-curvature sector contributes bulk residual rank **0**.
2. This statement does not remove nonanalytic kernels, explicit boundary observables, or genuinely nonlinear curvature dependence in `Rcal(Delta,R)`.
3. The frozen F2 public record supplies IR/UV consistency conditions for the generalized-EH object but not a unique finite low-energy basis containing two independent residual directions after GR baseline subtraction.
4. Synthetic endpoint-identifiability stress gives diagnostic rank **2**: identical endpoint constraints allow inequivalent interiors. Thus endpoint consistency does not determine a unique finite residual embedding.
5. Adding two arbitrary transverse columns to a rank-4 quadratic image closes rank six in 100% of 1000 random counterfactual trials. This is mathematical possibility only; the frozen F2 record does not supply those two independently reconstructed columns.
6. Already-counted `R^2` / `Ricci^2` form-factor directions are not recounted, `p^6/R^3` is not imported, and the information firewall passes.

## Scientific verdict

No frozen basis exists for crediting the published F2 generalized-EH sector with the two additional independent **bulk residual directions** required by Wave 30. Therefore the central-F2-projection route is parked at this point. This does not falsify the full generalized-EH sector; it means its currently frozen public realization is insufficient for the six-direction finite matching closure.

## Blocking object

`BLOCKED_NO_TWO_INDEPENDENT_PUBLISHED_GENERALIZED_EH_BULK_RESIDUAL_DIRECTIONS_AFTER_GR_BASELINE_QUOTIENT`

## Route decision

`PARK_F2_CENTRAL_PROJECTION_CLOSURE_AND_RETURN_TO_WAVE28_UV_DISPLACED_TRAJECTORY_OBJECT`

## Next target

Wave 32: audit reconstructibility of the F1 UV relevant-direction basis from published beta-function/stability information. Determine whether a same-lineage partial or full eigenbasis can be recovered without inventing missing higher-coupling flow derivatives. If a complete basis is not reconstructible, specify the minimal new FRG object required before displaced-trajectory computation can begin.