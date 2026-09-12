# Research Activity Ledger

Purpose: make cross-branch research progress visible from `main` without merging exploratory branches into the authority line.

## Current visible state

- Default branch: `main`.
- Research waves are intentionally developed on dedicated feature branches and committed there before/while GitHub Actions runs.
- Completed-wave certificates and immutable preregistrations remain on their source branches; this ledger records where to find them.

## Recent activity

| Wave | Branch | Authoritative run / commit | Status | Main result |
|---|---|---|---|---|
| 29 | `f2-central-projection-wave29` | run `34664963939` | PASS | F2 quadratic-curvature reconstruction supports two form factors; finite low-energy rank ≤4 with first slopes, not six. |
| 30 | `residual-nullity-wave30` | run `34665126543` | PASS | Codimension lower bounds: 4, 2, 1 for latent dimensions 2, 4, 5; rank-6 needs at least two additional independent directions beyond the four-coefficient quadratic sector. |
| 31 | `generalized-eh-wave31` | run `34665447413` | PASS | After EH baseline quotient, analytic linear-curvature bulk residual rank is 0; published generalized-EH sector does not supply two frozen independent bulk directions. |
| 32 | `f1-relevant-basis-wave32` | run `34665724676` | PASS | Critical exponents determine UV surface dimension but not its orientation; same spectrum permits nearly 90° different 3D relevant subspaces in 5D. |
| 33 | `frg-basis-ingest-wave33` | run `34666478508`, head `3fd040184a00e3dff1acad5749b73512cf61d121` | RUNNING/QUEUED | Executable 5x5 stability-matrix/eigenbasis ingest, complex-pair realification, seven symmetric trajectories, uncertainty stress and provenance firewalls. Appendix-F object remains `SURROGATE_NOT_J8`. |

## Current blocker

`BLOCKED_MISSING_REUSABLE_F1_RELEVANT_EIGENVECTOR_BASIS_OR_NUMERIC_APPROXIMATE_STABILITY_MATRIX_IN_SAME_CLOSURE`

The physical J8 calculation remains blocked until a same-realization numerical 5x5 stability matrix or normalized right-eigenvector basis is available. Critical exponents alone are not used as displacement directions.

## Logging policy from Wave 33 onward

Every completed wave will have:

1. an immutable preregistration commit on its research branch;
2. a GitHub Actions run with primary jobs plus fail-closed aggregator;
3. a certificate/result file committed to the research branch;
4. an entry in this `main` ledger with branch, run ID/commit and scientific verdict.

Exploratory equations are not merged into `main` merely to show activity; `main` records the audit trail while branch isolation preserves the blind/provenance design.
