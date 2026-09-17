# RCG-005B — generic local metric-jet principal-symbol held-out (PREOUTCOME)

Date: 2026-09-17
Status: **FROZEN BEFORE RCG005 QUOTIENT / PRIMARY NULLSPACE / SURVIVOR OUTCOME**

Parent RCG005 scientific preregistration:
`prereg/RCG005_COMPLETE_PARITY_EVEN_LOCAL_DIM6_PURE_METRIC_CURVATURE_CLASS_V0.md`
commit `1ac1c032dcbbd8e3f0a527a470acc0a44ddffa08`.

## Purpose

Detect any nonzero RCG005 primary survivor whose apparent second-order closure is an artifact of homogeneity/diagonality of restored-lapse triaxial Bianchi-I.

This held-out is independent of the primary minisuperspace geometry and may not be used to choose primary coefficients.

## Generic-point convention

Use a generic spacetime point `p` in local coordinates. Normalize only the zeroth-order metric at `p` to a fixed nondegenerate Lorentzian matrix by an invertible coordinate choice. Do **not** impose field equations, curvature symmetries beyond exact geometric identities, homogeneity, isotropy, conformal flatness, Killing symmetry or diagonal higher jets.

Preferred implementation: normal-coordinate-compatible local metric jets at `p`, so first metric derivatives may be set to zero by coordinate choice while independent second and higher derivatives remain generic subject only to index symmetries and exact commutation identities. If a different generic local coordinate convention is used, it must be frozen in code before evaluating a survivor and shown exactly equivalent for the principal higher-derivative symbol.

## Frozen zeroth-order metric

At the evaluation point use
`g_mu_nu = diag(-1,2,3,5)`
unless the implementation performs an exact invertible normalization to Minkowski signature first. The convention chosen in code must be fixed before outcome and recorded in the artifact.

## Deterministic exact seeds

Use exactly these first three held-out seed labels and deterministic rational value rule for every independent jet variable after canonical ordering:

- `H1`: value of variable number `j` is `(2*j+1)/(j+2)`;
- `H2`: value is `(-1)^j * (3*j+2)/(2*j+3)`;
- `H3`: value is `(5*j+1)/(3*j+4)`.

Index `j` starts at `1` in lexicographic canonical variable order. Denominators must be checked nonzero. These are exact rationals, not floating samples.

The canonical variable ordering and its SHA256 must be persisted **before** evaluation of the primary survivor restriction. No additional seed may be added after seeing a failure/survival unless a separate prospective amendment is committed first. If all three seeds accidentally encounter an algebraic denominator singularity caused by the chosen coordinate implementation, classify the held-out `INVALID` rather than adapt values post-outcome.

## Held-out observable

For the entire primary survivor subspace `K_SO`, construct the exact coefficient map of every metric-Euler-Lagrange derivative term of order `>2`, equivalently the full higher-derivative principal/subprincipal coefficient map required to decide second-order closure at the generic point.

Restrict the held-out map to `K_SO` and compute exact rank and residual nullity separately for `H1,H2,H3`, then for the stacked map.

A candidate direction survives only if the symbolic/rational held-out coefficient map vanishes exactly at all frozen seeds and any required exact reconstruction checks pass.

Finite seeds are not by themselves a proof of a universal tensor identity. Therefore any nonzero held-out survivor requires an exact symbolic or reconstructed polynomial/tensor certificate before PASS. Conversely a single exact nonzero frozen-seed witness is sufficient to falsify that direction because a universal identity must vanish at every valid exact jet.

## Classification

If primary `dim K_SO=0`:
`NOT_APPLICABLE_PRIMARY_NULLITY_ZERO`.

If primary `dim K_SO>0` and stacked frozen held-out restriction has zero residual dimension with valid provenance:
`FAIL_SCOPED_RCG005_PRIMARY_SURVIVORS_FAIL_FROZEN_GENERIC_GEOMETRY_HELDOUT`.

If nonzero residual dimension remains, retain the entire exact residual subspace; do not select one vector. PASS still requires exact symbolic/reconstruction certification that the relevant `>2` derivative tensor coefficients vanish identically, not merely at the three seeds.

## Locks

No refit.
No additional post-outcome seed.
No EOM use.
No field-redefinition quotient.
`VACUUM_ZERO`.
`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
