# Iter066 / G68 — standard quadratic-gravity baseline equivalence / novelty audit — TERMINAL

Terminal classification: `G60_G67_LOCAL_FOUR_DERIVATIVE_ESCAPE_BASELINE_EQUIVALENT_TO_STANDARD_QUADRATIC_GRAVITY_SCOPED`

## Frozen provenance
- preregistration: `a006f9b951ae14804a3e2fa8dcb3b80f6f2513a6`
- implementation: `862aaf3abf00f73bffd4bb6679219ab1a7024422`
- production head / launch: `024b458c3616d21cbf03578514ca072b39e1006d`
- run: `34771096136`
- aggregate job: `103760764362`
- aggregate artifact: `10321738469`
- aggregate digest: `sha256:d35eb8d780dba15a8376d06cb79b34931c2194e657164c2c2068540eb05fe3da`

The preregistration preceded implementation and production. No frozen momentum, coefficient triple, Gauss-Bonnet shift, source panel, target formula or control was changed after production output.

## Fixed external baseline anchors
1. K. S. Stelle, *Renormalization of higher-derivative quantum gravity*, Phys. Rev. D 16, 953 (1977), DOI `10.1103/PhysRevD.16.953`.
2. A. Salvio, *Quadratic Gravity*, Front. Phys. 6, 77 (2018), DOI `10.3389/fphy.2018.00077`.

These references were frozen before implementation and used only to classify the already-derived local curvature-squared theory space.

## Raw streams consumed
- A independent Gauss-Bonnet quotient reconstruction: job `103760717151`; artifact `10321503881`; digest `sha256:04d40899373234dad40922b99e8ef7aee8834a5212895b974b5b6755a3757182`. On all five held-out momenta the curvature-invariant Hessian space had exact rank 2, nullity 1, and the unique projective null relation `(1,-4,1)`.
- B exact general-curvature coefficient quotient map: job `103760717289`; artifact `10321573868`; digest `sha256:21882782223fb877a50cae87dc9b39d3e5de4a1de8eae25462502ddacf861c4c`. Result: 155/155 exact checks PASS, including the frozen map `b=beta+4 gamma`, `a=alpha-gamma` and four nonzero Gauss-Bonnet shifts per held-out coefficient triple.
- C independent `(R^2,C^2)` basis equivalence: job `103760717271`; artifact `10321387766`; digest `sha256:426172aff5f4dc670584bfb387c680e47ce1d43711eff7d5e1e7f53cbcdb337d`. Result: 47/47 exact checks PASS; basis transformation determinant exactly `2`.
- D sector/source-response reproduction: job `103760717254`; artifact `10322361159`; digest `sha256:95aea0518ec5376821753f8f288c05a291cf29826258fb358811cf13cd95937d`. Result: exact sector forms `P_TT=z*(b*z-4)/2` and `P_S=3*z*(3*a*z+b*z+2)` plus 384 frozen source-response reconstructions; `invalid_frozen_lanes=0`.
- E scope / false-equivalence controls: job `103760717316`; artifact `10322460431`; digest `sha256:ba33676e06b0cc5b5763e341a0bc6849c8896f05fa7468990e2cd9267e9ce157`. All frozen controls PASS: GB shift invariance, duplicate-basis rank-one detection, explicit six-derivative term outside the curvature-squared baseline, explicit rational/nonlocal term outside the local polynomial class, and local-layer scope guard.

Aggregate consumed exactly one valid artifact from each stream and returned A/B/C/D/E=`true`.

## Scientific interpretation
Within the frozen local linearized four-derivative class, the complete two-dimensional G60 escape space is exactly the standard four-dimensional curvature-squared quadratic-gravity space modulo the Gauss-Bonnet direction. The G61–G67 TT/scalar pole, residue, projector, gauge-sector and source-saturated structure is reproduced by that baseline without requiring a candidate-specific RCG-002 ingredient.

Therefore **novelty is not established in the G60–G67 local linearized four-derivative layer**. This is a useful negative result: that layer must not be presented as new RCG-002 physics.

This result does not show that RCG-002 as a whole is standard, false, inconsistent or non-quantum-gravitational. Candidate-owned nonlocal, higher-derivative, nonlinear, state-dependent, relational or quantum-measure dynamics remain logically open but must be defined and separately tested.

Programme readiness remains **66%**. Theory established remains **0%**.
