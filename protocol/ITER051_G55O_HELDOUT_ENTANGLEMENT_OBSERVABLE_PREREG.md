# Iter051 / G55-O — held-out entanglement observable transport preregistration

Date frozen: 2026-09-13
Status: **FROZEN BEFORE IMPLEMENTATION/PRODUCTION**

## Objective
Test whether the already-qualified RCG-002 finite-size weak-field controlled-phase channel transports prospectively held-out geometries into a basis-independent two-qubit entanglement observable without comparator fitting or reuse of G54 geometry cases.

This is an RQIR-CG-internal prediction/consistency test only. It imports no physical assumptions/results from RQIR/KMQGB/QGR.

## Frozen held-out panel
Six independent lanes with `R/s = [1.25, 1.75, 2.50, 3.50, 5.00, 10.0]`. Each lane uses a deterministic four-branch geometry distinct from every Iter050/G54-Q lane:
`d = [0.41, 0.67, 0.59, 0.46] * scale * perturbation`, with lane-specific scales `[0.86,0.96,1.07,1.20,1.38,1.61]` and fixed perturbations embedded in implementation. Masses/times are deterministic lane functions and are not tuned to outcomes.

## Observable
Input state is fixed to `|++>`. The channel is the diagonal four-branch RCG-002 unitary obtained from the finite-size Gaussian kernel. The held-out observable is bipartite entanglement negativity of the output density matrix.

Two independent calculations are required:
1. direct density-matrix evolution + partial transpose eigenspectrum;
2. closed-form controlled-phase prediction `N = |sin(chi/2)|/2`, where `chi = phi00 + phi11 - phi01 - phi10`.

## Frozen controls and thresholds
Each lane must satisfy simultaneously:
- direct-vs-closed-form negativity absolute difference `<= 1e-12`;
- negativity nonnegative and `<= 0.5 + 1e-12`;
- density trace residual `<= 1e-12`;
- minimum density eigenvalue `>= -1e-12`;
- local Z-phase invariance of negativity `<= 1e-12` under fixed lane-independent nontrivial local phases;
- A/B exchange invariance `<= 1e-12`;
- equal-distance null geometry negativity `<= 1e-12`;
- analytic Gaussian kernel vs independent Fourier integral relative error `<= 1e-10`;
- weak-field compactness `< 1e-12`;
- all reported quantities finite.

Aggregate requires all 6 lanes structural-valid and all frozen predicates true. No threshold, panel, observable or formula may change after result inspection.

## Frozen interpretation
PASS label: `HELDOUT_FINITE_SIZE_ENTANGLEMENT_OBSERVABLE_TRANSPORT_VALIDATED_SCOPED`.
FAIL label: `G55O_FROZEN_HELDOUT_OBSERVABLE_RULE_NOT_MET`.
Technical/runtime/serialization failures are not scientific FAIL and may receive minimal implementation-only repair without changing frozen science.

A terminal PASS closes the current **independent observable/witness** roadmap rubric and authorizes internal programme readiness `65% -> 66%`. It does **not** establish a covariant gravity theory, experimental confirmation, all-classical no-go, or complete QG.

After terminal classification, the next programme-critical gate is continuum/covariant candidate-gravity constitution; do not open it before G55-O is terminal.