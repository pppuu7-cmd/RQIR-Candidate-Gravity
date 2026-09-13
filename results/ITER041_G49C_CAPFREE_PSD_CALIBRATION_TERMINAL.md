# Iter041 / G49-C — cap-free/direct-PSD response-blind calibration terminal result

Scientific classification: **CAPFREE_DIRECT_PSD_OPTIMIZER_CALIBRATED** (scoped calibration PASS).

## Authoritative provenance

- preregistration: `2d472c4223602f77e13b054615e713c58f0b46c3`
- implementation: `05a41f62b36e0912f60c01f7aa1657130c3c66d4`
- workflow: `7c31d7d19f4847b12043e15ba1699740e0fd7af3`
- launch/head: `db61900e4113cf002f3d5c7b636b7e14d41e00c0`
- authoritative run: `34726705385`
- aggregate job: `103642168161`
- summary artifact: `10307129893`
- summary digest: `sha256:ec1328e7dfa0de16be7e9d57549c81badff48c16193f9b957d566d996b80657b`

## Frozen result

All `12/12` response-blind lanes were structurally valid and satisfied the preregistered lane support rule, including exact requested effective rank, trajectory gap `<0.002`, relative Kossakowski error `<0.02`, PSD/TP/CP/output-state/trace controls, and numerical-box inactivity `max(abs(w_i))/8 < 0.80` for the selected candidate. Both Sobol and LHS methods passed for every requested rank 1..6.

Frozen cross-method best-gap pairs were:

- rank 1: `1.5113774791023392e-12`, `1.858103185509367e-12`; difference `3.467257064070278e-13`
- rank 2: `1.2496869033463797e-12`, `2.1581448684381203e-12`; difference `9.084579650917406e-13`
- rank 3: `2.7629030008391473e-12`, `2.988838041201596e-12`; difference `2.2593504036244892e-13`
- rank 4: `4.702077259541113e-12`, `4.7462942753178155e-12`; difference `4.42170157767022e-14`
- rank 5: `1.8459223995795374e-11`, `1.8893937897881937e-11`; difference `4.347139020865624e-13`
- rank 6: `2.0677903833643545e-15`, `2.6784130469081905e-15`; difference `6.106226635438361e-16`

All six pair differences are far inside the frozen `0.002` agreement tolerance.

## Interpretation lock

This is a response-blind optimizer calibration for the direct real-PSD parameterization `C=A^2` with no physical trace cap. It is **not** a mathematical proof of a global optimum over all unbounded PSD generators, not an all-classical/all-semiclassical no-go theorem, and not a gravity-theory constitution result.

The PASS authorizes only a separately prospectively frozen transport of this calibrated parameterization to the unchanged RCG-002 four-shard toy target. Programme readiness remains **63%** because calibration deepens an already-counted comparator rubric rather than closing a new programme layer. Theory established remains **0%**.
