# Wave 30 — Residual Nullity Lower-Bound / Baseline-Quotient Certificate

Status: **FROZEN CLEAN RESULT**

Date: 2026-09-12

## Authority

- Branch: `residual-nullity-wave30`
- Frozen preregistration commit: `5ce5481274b5ed24e8e96be9d045af7e9f3eb3c3`
- Compute commit: `e0f1598efb0fd37a5b29668d2cdb75507fde07ff`
- GitHub Actions run: `34665126543`
- Primary jobs: 6/6 SUCCESS
- Aggregator: SUCCESS
- All preregistered signals: TRUE

## Numerical / algebraic result

- Frozen Wave-22 probe matrix rank: **6**
- Wave-22 condition number: **5.2499494917130765**
- Finite low-energy matching codimension lower bounds:
  - constants-only quadratic sector, `k <= 2`: codimension >= **4**
  - quadratic constants + first slopes, `k <= 4`: codimension >= **2**
  - optimistic `k <= 5` after one additional independent generalized-EH residual coefficient: codimension >= **1**

For latent `z in R^k`, embedding `P: R^k -> R^6`, and frozen probe matrix `H`,

`rank(H P) <= rank(P) <= k`, hence `codim(Im P) >= 6-k`.

Adding probe rows cannot exceed this latent-rank cap.

## Optimistic generalized-EH stress test

Starting from a full-rank four-parameter quadratic image:

- adding zero extra independent residual directions caps rank at 4;
- adding one extra independent direction caps rank at 5 and cannot close six dimensions;
- adding two extra directions makes rank 6 mathematically possible only if they are independent and transverse to the existing image.

Generic random transversality can saturate the allowed cap, but it cannot supply missing physical directions by itself.

## Scientific verdict

Within the declared finite low-energy matching problem, the F2 quadratic sector with constants plus first slopes is provably too low-dimensional to close the six-dimensional frozen RQIR proxy target after generalized-EH/baseline quotienting. Even granting one additional independent generalized-EH residual coefficient leaves at least one unresolved direction. At least two additional independent residual directions are therefore necessary beyond the four-coefficient quadratic truncation, and their physical existence/transversality must be derived rather than assumed.

This certificate does **not** claim that the full nonlocal F2 action has only four degrees of freedom. It applies only to the finite low-energy projection problem used for comparison to the frozen six-coordinate Wave-22 bank.

## Blocking object

`BLOCKED_FINITE_LOW_ENERGY_F2_MANIFOLD_CODIMENSION_AT_LEAST_2_AFTER_BASELINE_QUOTIENT;_ONE_EXTRA_EH_DIRECTION_STILL_LEAVES_CODIMENSION_AT_LEAST_1;_WAVE28_UV_DERIVATIVE_ENSEMBLE_UNCHANGED`

## Next target

Wave 31: audit whether the same-lineage published generalized-EH sector supplies two independently justified low-energy residual directions beyond the four-coefficient quadratic truncation, after classical GR baseline subtraction and without importing p6/R3 or cross-lineage objects. If not, park central-projection closure and return to the Wave-28 missing UV displaced-trajectory ensemble.