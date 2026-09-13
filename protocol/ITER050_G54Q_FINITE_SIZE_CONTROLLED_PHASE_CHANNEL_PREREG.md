# ITER050 / G54-Q — finite-size controlled-phase channel integration (preregistration)

This protocol is frozen **before implementation and before any production output**. It is authorized only after terminal PASS of G52-H and G53-W.

## Question
Can the independently validated weak-field pair-energy quotient (G52-H) and isotropic Gaussian finite-size kernel (G53-W) be integrated into one finite-size two-qubit controlled-phase channel without fitting to comparator outcomes?

For branch separations `d_ij` and a common relative Gaussian width `s>0`, define

`K(d,s) = erf(d/(sqrt(2)*s))/d`,

`phi_ij = alpha K(d_ij,s)`, with `alpha = G m_A m_B T / hbar`, and

`chi_fs = phi_00 + phi_11 - phi_01 - phi_10`.

The diagonal branch unitary is `diag(exp(i phi_00), exp(i phi_01), exp(i phi_10), exp(i phi_11))`.

## Frozen production panel
Eight deterministic lanes. The ordered width ratios are `min(d_ij)/s in {1,1.5,2,3,4,6,8,12}`. Each lane uses a fixed positive non-null geometry obtained from the base separations `(0.45,0.62,0.57,0.48) m` by a deterministic lane-specific positive scale and small deterministic non-degenerate perturbation; masses are around `1e-14 kg` and times around `1 s`, all fixed in implementation before output.

## Independent implementations and frozen rules
For every lane:

1. Compute all four kernels analytically from `erf` and independently by Fourier quadrature
   `K_num(d,s) = (2/pi) integral_0^infinity exp(-x^2/2) sinc(x d/s) dx / s`.
   Maximum relative kernel discrepancy must be `<=1e-10`.
2. Compute `chi_fs` from the four branch phases and reconstruct the full diagonal unitary from one global phase, two local branch phases and one controlled phase. Maximum elementwise reconstruction discrepancy `<=1e-12`.
3. Add fixed deterministic arbitrary branch-local phase shifts `c+a_i+b_j`; the extracted controlled phase must remain invariant to absolute error `<=1e-12`.
4. Exchange A/B (`d01 <-> d10`); `chi_fs` must be invariant to relative error `<=1e-12`.
5. Build the unitary superoperator and Choi matrix independently. TP residual must be `<=1e-12`; Hermiticity residual `<=1e-12`; minimum Choi eigenvalue `>=-1e-12`; Choi rank must be numerically one using eigenvalue floor `1e-10` relative to the largest eigenvalue.
6. Equal-distance geometry is an exact nonlocal null: `|chi_fs|<=1e-12`.
7. Point-particle convergence: define `chi_point = alpha*(1/d00+1/d11-1/d01-1/d10)`. For lanes with `min(d)/s >= 8`, relative discrepancy `|chi_fs-chi_point|/max(|chi_point|,1e-30) <=1e-10`.
8. All values must be finite; compactness `max(G m/(d c^2)) <1e-12`.
9. No target/comparator fitting, no post-hoc geometry/width/threshold changes.

## Frozen aggregate rule
Terminal PASS requires exactly 8 structurally valid lanes and every applicable rule above to pass. The aggregate also requires monotonic decrease of `|chi_fs-chi_point|/max(|chi_point|,1e-30)` over the ordered width-ratio panel, allowing `1e-13` numerical slack.

Frozen PASS label:
`FINITE_SIZE_WEAK_FIELD_CONTROLLED_PHASE_CHANNEL_INTEGRATED_SCOPED`

Otherwise, if structurally valid but any scientific predicate fails:
`G54Q_FROZEN_INTEGRATION_RULE_NOT_MET`.

Implementation/runtime/artifact corruption is infrastructure/numerical failure and may be minimally repaired without changing this frozen scientific contract.

## Interpretation and readiness lock
A PASS establishes only internal consistency of the finite weak-field isotropic-Gaussian branch-channel construction on this frozen panel. It does not establish covariant continuum gravity, a field measure, experimental confirmation, or full quantum gravity. G54-Q alone does **not** increase programme readiness above 65%. Theory established remains 0%.