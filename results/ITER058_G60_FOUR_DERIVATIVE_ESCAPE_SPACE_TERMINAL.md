# Iter058 / G60 — four-derivative escape-space terminal result

Date: 2026-09-13

## Authority
- Preregistration: `f8adae8c8147fb284f4662eec6f227e2a443a92f`
- Implementation: `f3b40a8aa5b1a7d42f9926d33a1cba93ce13c875`
- Production head: `834420e772d06fc45b00d74e3a834b5237f01b25`
- Run: `34755807784`
- Aggregate job: `103719901539`
- Aggregate artifact: `10317032484`
- Aggregate digest: `sha256:f30284e1556c959fb5a68d8908284f47554c7d46bcd720fa3fc22ecfbec93427`

Raw lanes consumed:
- A job `103719862145`, artifact `10316947563`, digest `sha256:8e915efd6372cca7a1824b3deeb79669aedef3146e2c24ea8a1d6151133389b0`
- B job `103719862166`, artifact `10316922791`, digest `sha256:142666aa8aae02d18b8863d58eeb1ec265196ed19281594c37f0434009470d02`
- C job `103719862047`, artifact `10317206109`, digest `sha256:69d65d0738569d581a3d6a251998b0dc6633450c62d4d5bdc2aab238018ac529`
- D job `103719862231`, artifact `10317595782`, digest `sha256:2fbfab2aef429a3775f6b10aa8d0ececc1d58f081cfe263695430a7ef38fe185`

## Frozen-result audit
A: exact invariant span rank `2`, nullity `1`, projective Gauss-Bonnet relation `(1,-4,1)` exactly.

B: all `6/6` held-out momentum cases have exact-zero gauge shifts for all curvature-squared invariants; non-gauge controls change at least one invariant in `6/6`.

C: conserved-source response matrix has exact rank `2` over `24` rows; duplicated-direction control rank is exactly `1`.

D: all three symmetric-tensor coordinate transforms and all three invariant-coordinate transforms preserve the required ranks/relation; deliberate insufficient observation has rank `1` and is correctly detected.

Aggregate artifact is valid and all A/B/C/D frozen predicates pass.

## Terminal scientific classification
`FOUR_DERIVATIVE_LINEARIZED_GAUGE_INVARIANT_ESCAPE_SPACE_TWO_DIMENSIONAL_SCOPED`

This is a SCIENTIFIC PASS under the prospective G60 preregistration, not an inference from green CI.

## Scope ceiling
The result establishes only a two-dimensional local four-derivative linearized gauge-invariant structural escape space modulo the 4D Gauss-Bonnet/boundary relation, in the frozen one-symmetric-tensor Minkowski audit. It does not select coefficients, authorize a candidate action, prove stability/ghost-freedom/unitarity, supply nonlinear completion, or establish a quantum measure. `THEORY_ESTABLISHED=0%` and programme readiness remains `66%`.

## Next authorized question
Before any coefficient choice, map the generic and exceptional pole/sector structure of this two-dimensional escape space on the conserved-source linearized quotient. The next gate must remain candidate-independent and prospectively frozen; it may classify additional-pole/degeneracy strata but may not select a physical deformation or promote a global no-go theorem.
