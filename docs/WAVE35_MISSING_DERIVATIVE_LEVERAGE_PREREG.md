# Wave 35 preregistration — missing-derivative leverage and external FRG contract

Status: **FROZEN BEFORE COMPUTE**
Date: 2026-09-12
Branch: `missing-derivative-leverage-wave35`

## Input boundary

Use the certified Wave-34 conditional 3x3 Jacobian `A` as a known surrogate block only. A general 5x5 completion is partitioned

`M = [[A, B], [C, D]]`

with unknown blocks `B` (3x2), `C` (2x3), and `D` (2x2). These contain the 16 derivatives not fixed by Wave 34.

This is a synthetic information-leverage study, not an inference of physical FRG derivatives. No synthetic completion receives physical J8 credit.

## Frozen ensemble

Baseline completion: `B=C=0`; `D=diag(-2,+2)`, chosen only to provide a controlled five-dimensional object with three attractive real dimensions.

Random perturbations are Gaussian matrices normalized to unit Frobenius norm and scaled by `s * ||A||_F/sqrt(9)` for `s in {0.05,0.10,0.20,0.40}`.

Independent scenarios:
- `B_only`
- `C_only`
- `D_only`
- `BC`
- `BCD`

Use 400 deterministic-seed trials per scenario and scale. Record:
1. fraction retaining exactly three attractive eigenvalues counting a complex pair as two;
2. maximum-principal-angle distribution of the real relevant subspace relative to baseline;
3. spectral real-part displacement.

## Predeclared scientific tests

1. The 16 missing derivatives decompose exactly as 6 (`B`) + 6 (`C`) + 4 (`D`).
2. The same known `A` supports inequivalent full 5D relevant-subspace orientations once any missing block is varied.
3. Cross-block feedback (`B` and/or `C`) produces nonzero orientation leverage under the frozen isotropic ensemble.
4. `D` alone is also non-identifying: it can rotate/change the held-sector contribution without changing `A`.
5. Increasing frozen perturbation scale must not decrease the median orientation uncertainty for the full `BCD` ensemble beyond small Monte-Carlo tolerance.
6. Eigenvalue-count/topology changes are recorded rather than discarded; angle statistics are conditional on exactly three attractive real dimensions.
7. No ranking from this synthetic prior may be reported as a physical ranking of FRG derivatives.
8. The minimal physical input contract is: same-closure fixed point + ordered coordinates + numerical 5x5 stability matrix (all 25 derivatives) OR an equivalent normalized right-eigensystem, with closure/projection/regulator provenance and numerical precision.
9. Information firewall against polygon/KMQGB-derived QGR remains active.

## Interpretation

Wave 35 may prioritize which missing derivative *classes* are information-sensitive under a declared synthetic ensemble, but it cannot replace the missing same-realization FRG calculation. PASS means the external computation request is numerically and provenance-wise specified and its necessity is stress-tested.
