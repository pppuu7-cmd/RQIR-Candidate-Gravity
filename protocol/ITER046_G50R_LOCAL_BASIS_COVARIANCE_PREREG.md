# Iter046 / G50-R — prospective local-basis covariance audit

Created prospectively after terminal Iter045/G50-A and before implementation or production results.

## Goal
Test whether the already-terminal G50-A separation for the exact frozen 20D four-state hidden-classical switching family is a coordinate/basis artifact. No new fitting, family enlargement, target modification, or threshold tuning is allowed.

## Frozen inputs
- Authoritative G50-A run `34736777512`, head `2122211ff1c08c03ca637c42b8299fd3a9fd6806`.
- Exactly the eight terminal best-candidate parameter vectors (Sobol/LHS x shards 0..3) from the consumed G50-A raw artifacts.
- Same target strengths, training times, held-out times and product-probe panel as G50-A.
- Four deterministic local-rotation seeds `[4601,4602,4603,4604]`. Each seed generates independent Haar-like SU(2) matrices for subsystems A and B by complex Gaussian QR with deterministic phase/determinant normalization. The two-qubit rotation is `U_A kron U_B`.

## Frozen computation
Matrix jobs: 4 rotation seeds x 4 shards = 16 independent lanes, `fail-fast:false`. Each lane audits both terminal search-method candidate vectors.

For every method candidate and time point:
1. Build the canonical comparator and target superoperators.
2. Rotate both by the same local unitary using superoperator conjugation.
3. Rotate every canonical product probe by the same local unitary.
4. Recompute train and held-out maximum trace-distance gaps.
5. Independently compute each rotated output by conjugating the canonical input/output density matrices rather than using the rotated superoperator; compare the two implementations.
6. Check output traces and positivity on the transformed product-probe panel. CP itself is inherited analytically from the already provenance-qualified canonical channel under unitary pre/post composition; the numerical product-output checks are implementation controls, not a standalone proof of global CP.

## Frozen thresholds / rule
A lane is valid only if finite and complete. A method passes a lane only if all are true:
- `abs(rotated_train_gap - canonical_train_gap) <= 1e-9`;
- `abs(rotated_holdout_gap - canonical_holdout_gap) <= 1e-9`;
- maximum direct-output vs rotated-superoperator trace-distance discrepancy `<= 1e-10`;
- maximum output trace residual `<= 1e-10`;
- minimum transformed output eigenvalue `>= -1e-10`;
- rotated train and held-out gaps remain `>1e-4`.

Terminal PASS requires all 16 lanes and both method candidates in each lane to pass. Frozen PASS label:
`DERIVED_SCOPED_G50A_LOCAL_BASIS_COVARIANT_SUPPORT`.

Any finite, correctly executed threshold violation is a scientific/robustness FAIL for this gate, not infrastructure failure. Runtime/import/artifact corruption is infrastructure failure and may be minimally repaired without changing the frozen science.

## Interpretation ceiling
PASS would establish only local-unitary basis covariance of the exact finite G50-A separation and implementation consistency. It would not extend the comparator family, create an all-classical/no-go theorem, establish continuum/full dynamics, or validate a gravity theory. `THEORY_ESTABLISHED` remains 0% regardless of this gate.