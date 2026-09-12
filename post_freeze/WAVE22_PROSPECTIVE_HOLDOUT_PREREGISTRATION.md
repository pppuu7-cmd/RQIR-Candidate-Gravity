# Wave 22 — Prospective Candidate-Blind QGR Holdout Bank

Status: PREREGISTERED BEFORE COMPUTE

## Purpose

Freeze a discriminator bank before any concrete polygon-derived QGR equations are imported. The bank must resolve the physical residual directions already exposed by frozen RQIR Wave 17–20 and remain useful after nuisance profiling and modest perturbations.

## Information firewall

Allowed: frozen `RQIR_ONLY_ACTION_LEVEL_ENDPOINT_V1`, established GR/EFT/amplitude consistency structure, and generic finite proxy kinematics.
Forbidden: KMQGB candidate equations, candidate ansatz, candidate architecture, parameter values inferred from a future QGR-P, or post-hoc changes after candidate inspection.

External provenance anchors:
- Bern, Kosmopoulos, Zhiboedov, arXiv:2103.12728: four-graviton unitarity/crossing bounds relate an R^3 coefficient that corrects the graviton 3-point amplitude to higher-order data without making the coefficient generically unique.
- Calderón-Infante, Castellano, Herráez, arXiv:2501.14880: higher-curvature quantum-gravity EFTs naturally carry structured Wilson-coefficient expansions.

These sources motivate *axes of testing*, not numerical coefficients in the proxy bank.

## Frozen residual proxy basis

`theta = [c3, d3, e4, f4, s2, s0]`

Interpretation:
- `c3,d3`: independent cubic/transverse higher-point directions;
- `e4,f4`: quartic/higher-point contact directions;
- `s2,s0`: finite-q physical spin-2 / spin-0 dressing directions.

The proxy is not claimed to be a complete basis of quantum gravity.

## Frozen observation pool

Twelve probes are generated deterministically:
- 2 spin-2 finite-q probes;
- 2 spin-0 finite-q probes;
- 4 finite-kinematic 3-point probes;
- 4 finite-kinematic 4-point probes.

The exact sensitivity functions are frozen in `compute_wave22/common.py`.

## Selection rule

Choose exactly 10 of 12 probes by exhaustive D-optimal search maximizing `log det(X^T X + 1e-12 I)` with lexicographic tie breaking inherited from combination order.

## Predeclared primary gates

1. Full pool rank = 6.
2. Selected 10-probe bank rank = 6.
3. Selected-bank condition number <= 8.
4. After profiling three sector-normalization nuisance columns (2pt, 3pt, 4pt), signal rank remains 6.
5. Profiled minimum singular value >= 0.15.
6. In 1000 seeded 2% sensitivity-perturbation trials, full-rank fraction >= 0.99.
7. Fifth percentile of profiled minimum singular value under perturbation >= 0.15.
8. The 2pt-only subbank cannot identify all cubic/quartic directions, while the selected cross-order bank resolves all four `[c3,d3,e4,f4]` directions.
9. A preregistered synthetic comparator set sharing lower-order normalization produces nonzero, prospectively distinguishable holdout vectors.
10. Anti-overfit firewall verifies that Wave-22 computation does not read KMQGB candidate/polygon dynamics.

## Interpretation

Passing Wave 22 means a candidate-blind finite proxy exam has enough independent directions to test future representatives of the RQIR equivalence class. It does not prove that real experiments have the assumed precision, nor that this finite proxy spans every quantum-gravity deformation.

## Fail-closed rule

Any missing artifact, rank loss, threshold failure, candidate-information leak, or post-hoc modification makes the campaign non-clean. A future candidate may be *tested against* this bank but may not change the frozen bank.
