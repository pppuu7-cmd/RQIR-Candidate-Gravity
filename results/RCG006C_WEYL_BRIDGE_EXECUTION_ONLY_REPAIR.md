# RCG-006C — execution-only repair after infrastructure failure

Date: 2026-09-17
Status: **PROSPECTIVE EXECUTION-ONLY REPAIR BEFORE RETRY**

Frozen scientific preregistration remains commit `1122988893e9d5f87771da8a6390f031be8fafca` without modification.

Initial workflow run: `35251277832`, head `e6bc0bca1021a237c0c65ec2debed85368af540b`.

The Constructor failed before producing any scientific artifact/value at initialization of the exact polynomial accumulator:

`TypeError: Rational.__new__() missing 1 required positional argument: 'p'`.

Cause: Python `defaultdict(sp.Rational)` calls the SymPy `Rational` constructor with zero arguments. This is an execution defect only; the intended additive identity is exact rational zero.

Frozen repair:
- replace every `defaultdict(sp.Rational)` in the RCG006C Constructor and Critic implementation with `defaultdict(lambda: sp.Rational(0))`;
- change no tensor formula, contraction, generator/basis, parent image, hypothesis, PASS/FAIL/BLOCKED/INVALID criterion, interpretation ceiling or normalization convention;
- rerun the exact same frozen gate after the repair.

The failed initial run has no scientific classification. Any independent local calculation performed for debugging is non-authoritative and cannot replace the repaired Constructor/Critic/aggregate workflow.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
