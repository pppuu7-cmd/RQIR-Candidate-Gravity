# Wave 34 Certificate — Appendix-F Partial Projected Jacobian

Status: **PASS / PARTIAL_SURROGATE_NOT_J8**
Date: 2026-09-12
Canonical GitHub Actions run: `34666780799`
Canonical head SHA: `42093f78e6b0d8ad9fbd57ba6279f92c0cd1b677`

## Frozen scope

Wave 34 uses only the published Appendix-F F1, F2 and F4 analytic equations under the declared Truncation-4 surrogate assumptions. Active coordinates are `(mu, lambda3, g3)` while `lambda4=-0.11` and `g4=0.55` are held fixed. This is not the best full momentum-dependent F1 realization and is permanently classified `PARTIAL_SURROGATE_NOT_J8`.

## Reproducible result

All 7 primary jobs and the aggregator passed. All 17 predeclared signals are true.

The rounded published five-dimensional Truncation-4 anchor is not a fixed point of the restricted F1/F2/F4 subsystem. The nearby conditional root is

`(-0.31192663076350463, -0.02786754323776642, 0.42397331562523205)`.

The conditional 3x3 Jacobian is full rank and has eigenvalues

- `-1.3525494416669428 + 2.184361833478728 i`,
- `-1.3525494416669428 - 2.184361833478728 i`,
- `+1.129502433718305`.

Its condition number is `8.028426065606537`.

Across the predeclared ±5% and ±10% held-coordinate variants, all 25 conditional solves converged. The largest conditional-root displacement from the central held-coordinate choice is `0.12146183820729`.

## No-go result

A 3x3 conditional Jacobian fixes only 9 entries of a general 5x5 stability matrix, leaving 16 entries undetermined. Explicit five-dimensional completions sharing exactly the same reconstructed 3x3 block can have different numbers of attractive directions. Therefore this block cannot determine the full five-dimensional relevant-subspace orientation required for physical J8 displaced trajectories.

The partial projected flow has two attractive real dimensions and one repulsive dimension, whereas the published five-dimensional Truncation-4 surrogate spectrum has three attractive real dimensions. The projected spectrum is therefore not numerically substitutable for the published five-dimensional spectrum.

## Scientific verdict

Wave 34 establishes that useful local directional information can be reconstructed from a strict subset of the published Appendix-F equations, but it also demonstrates why this information cannot be promoted to the missing physical J8 orientation object. The remaining blocker is the same-realization five-dimensional stability matrix or an equivalent right-eigenvector basis.

## Next target

Wave 35 should specify the minimal external full-orientation computation and quantify, with synthetic block-completion ensembles, which missing cross-derivative blocks most strongly control the full five-dimensional relevant-subspace orientation.
