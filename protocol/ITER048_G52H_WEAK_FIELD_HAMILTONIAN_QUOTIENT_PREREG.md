# ITER048 / G52-H — weak-field pair-energy to controlled-phase quotient bridge (preregistration)

This protocol is frozen **before implementation and before production output**.

## Question

Can the RCG-002 controlled phase be obtained directly as the nonlocal quotient of the four branch-pair weak-field interaction phases, rather than inserted as an independent two-qubit phase parameter?

For branch separations `d_ij`, use the weak-field pair-energy phase

`phi_ij = G m_A m_B T / (hbar d_ij)`

(sign convention is irrelevant to the quotient test). Define

`chi_cross = phi_00 + phi_11 - phi_01 - phi_10`.

The full diagonal two-qubit unitary must factor exactly into a global phase, two local branch phases, and one controlled phase `chi_cross`.

## Frozen panel and rules

Eight deterministic positive geometries/mass/time controls are fixed in implementation. For every lane:

1. Reconstruct the full diagonal unitary from `global + local_A + local_B + controlled-phase`; max elementwise discrepancy `<=1e-12`.
2. Compare `chi_cross` with `G m_A m_B T/hbar * (1/d00 + 1/d11 - 1/d01 - 1/d10)`; relative discrepancy `<=1e-12`.
3. Add deterministic arbitrary branch-local phase shifts `c + a_i + b_j`; `chi_cross` must remain invariant to absolute error `<=1e-12`.
4. Exchange A and B (`d01 <-> d10`); `chi_cross` must remain invariant to relative error `<=1e-12`.
5. Equal-distance geometry is a null control: `|chi_cross|<=1e-12`.
6. All controls must remain safely weak-field: frozen compactness ceiling `max(G m/(d c^2)) < 1e-12`.
7. No fitting to RCG-002 adversarial/comparator results and no post-hoc thresholds.

## Frozen classification

All 8 lanes valid and all rules pass:

`WEAK_FIELD_PAIR_ENERGY_TO_CONTROLLED_PHASE_QUOTIENT_BRIDGE_VALIDATED`

Otherwise:

`G52H_FROZEN_RULE_NOT_MET`

## Readiness rule frozen before output

G52-H alone cannot change readiness. A single **microscopic weak-field bridge rubric** is authorized to move programme readiness `64% -> 65%` only if **both** G52-H and the separately preregistered G53-W finite-size wavepacket bridge terminate PASS under their frozen rules. Any FAIL/BLOCKED leaves readiness at 64% and is retained.

## Interpretation lock

Even a PASS is only a weak-field branch-energy-to-channel quotient bridge. It is not a covariant 4D gravity derivation, not a full quantum-gravity theory, and not experimental confirmation.
