# Iter072 / G74 — C/D same-order nuisance confounding — TERMINAL

Date: 2026-09-13

Classification: `CD_IDENTIFIABILITY_REQUIRES_SAME_ORDER_NUISANCE_ANCHORS_SCOPED`

## Authority
- preregistration: `ed068632bdb099ffdcb47535afe5e8c42ff399b0`
- implementation: `b1e1d84a4c2af4f9fe5e9f921efefd61e07163b3`
- production head: `b85789c5f55b0cbbbc95f82431215b084a9a13b1`
- run: `34779124616`
- jobs: A `103782753310`, B `103782753553`, C `103782753443`, D `103782753538`, aggregate `103782797267`
- artifacts/digests:
  - A `10324745362`, `sha256:6b8433c4bcb3095a63025bad54c5c7ea21c85fb771840cdfab2f37f69e0e3a80`
  - B `10323474735`, `sha256:704c4f990ad6bd87fcd0b6199b344e700f33445dd1935675dbd568eb0d0eaa6b`
  - C `10324470487`, `sha256:dd82e16373b90de90dbb6e5c3a934335e3eb26dde2fbeb18d313924993e7927e`
  - D `10324765386`, `sha256:08f77d67979b1cc65d9c1bb9ea219fc0a50a7ee904e44ce3d8306f63a934200f`
  - aggregate `10324670462`, `sha256:cf4256e218ba4c451c0c1e44543873f76763c3db96b5d9dab22434b496c221a8`

## Frozen result
All four raw streams were consumed and the frozen aggregate validated their preregistered classifications.

- A: `BASELINE_AND_CONSTANT_NUISANCE_INDEPENDENCE_SCOPED` — C,D retain rank 2 and constant quadratic normalization does not alias C.
- B: `C_SAME_SHAPE_SLOPE_CONFOUNDED_DISTINCT_CURVATURE_SEPARABLE_SCOPED` — C is exactly proportional to the same-shape quadratic slope nuisance N1, while the frozen z^2 curvature nuisance is distinguishable.
- C: `D_SAME_SHAPE_CUBIC_CALIBRATION_CONFOUNDED_SCOPED` — D is exactly aliased by same-shape cubic calibration N3 but remains independent of the tested quadratic nuisances.
- D: `COMBINED_ALIAS_AND_ADDITIONAL_OBSERVABLE_CONTROL_SCOPED` — adding exact aliases cannot increase identifiable C/D content; an auxiliary second cubic observable with a different nuisance response restores algebraic independence in the frozen control.

## Scientific interpretation
G73 multi-order rank is not nuisance-robust against exact same-order, same-shape nuisance tangents. Independent nuisance anchors or additional observables carrying linearly distinct responses are required before C/D local identifiability can be interpreted as physically usable.

This is a scoped identifiability result only. It does not invalidate C or D, select an architecture, determine a physical coefficient, define candidate-owned RCG-002 dynamics, or establish new physics.

Programme readiness remains 66%; theory established remains 0%.
