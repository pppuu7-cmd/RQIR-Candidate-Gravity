# Wave 23 — Frozen Holdout Stress / Misspecification Audit

Status: PREREGISTERED BEFORE COMPUTE

## Immutable authority

Wave-22 frozen bank: `holdouts/WAVE22_FROZEN_BANK.json`.
Expected Git blob SHA: `c32bd52edd003589ef65e0240c757475f215f55f`.
Authority Wave-22 run: `34661882499`.
Authority Wave-22 scientific commit: `9009bb7e68e083cc819ebf0a3d6b6a111950e456`.

No row, threshold, nuisance definition, seed, or probe selection in the frozen bank may be altered by Wave 23.

## Question

Is the Wave-22 prospective exam robust to harmless coordinate choices and limited data loss, and can it detect a deliberately omitted seventh physical-shape direction rather than forcing all future physics into its six-dimensional residual class?

## Predeclared tests and gates

1. **Frozen-bank integrity:** computed Git-blob SHA exactly equals `c32bd52edd003589ef65e0240c757475f215f55f`; authority run and parameter order match.
2. **Orthogonal basis invariance:** 500 seeded random orthogonal parameter rotations (`seed=2301`) preserve rank 6 in every trial, preserve singular values to relative max error <= `1e-12`, and preserve predictions to max absolute error <= `1e-12` under the inverse coefficient rotation.
3. **Unit-rescaling invariance:** 500 seeded diagonal rescalings (`seed=2302`, each scale log-uniform over `[1e-2,1e2]`) preserve rank 6 and predictions to max absolute error <= `1e-12` when coefficients transform inversely.
4. **Jackknife:** all 10 leave-one-out banks retain rank 6; at least 80% of the 45 leave-two-out banks retain rank 6.
5. **Extended nuisance stress:** after profiling the three frozen sector-normalization nuisances plus one centered linear probe-order drift, rank remains 6 and profiled minimum singular value >= `0.03`.
6. **Omitted-physics detection:** a preregistered seventh higher-momentum/helicity-shape vector `g7` must have residual fraction >= `0.05` after best fit to the six frozen signal columns and >= `0.005` after best fit to signal + three sector-normalization nuisance columns.
7. **Candidate-information firewall:** no Wave-23 computation may read KMQGB/polygon candidate equations, synthesis directories, or candidate architecture.

## Frozen omitted-physics vector definition

For the ten frozen probes:
- `P2_q...`: `g7 = q^4`;
- `P0_q...`: `g7 = -0.7 q^4`;
- `V3_x..._h...`: `g7 = h x^4`;
- `A4_s..._t..._h...`: `g7 = h (s+t)^3`.

This is a finite proxy for a higher-order momentum/helicity shape absent from `[c3,d3,e4,f4,s2,s0]`; it is not claimed to be a specific UV theory.

## Interpretation

Passing Wave 23 certifies robustness of the finite prospective exam against parameter-coordinate changes, modest probe loss, an extra nuisance direction, and one explicit misspecification challenge. It does not prove completeness against every possible omitted operator or real experimental systematic.

## Fail-closed rule

Any gate failure leaves the Wave-22 bank frozen but marks the stronger Wave-23 robustness claim as unearned. Scientific thresholds may not be weakened after results are observed.
