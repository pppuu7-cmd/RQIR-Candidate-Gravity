# RCG-006C — aggregate-only execution repair

Date: 2026-09-17
Status: **PROSPECTIVE INFRASTRUCTURE-ONLY REPAIR**

Parent preregistration: `1122988893e9d5f87771da8a6390f031be8fafca`.
Previous execution-only zero-default repair: `bbd99b6061d22fc638317085ba0a51adc57b9bf3`.
Repaired workflow run: `35251589231`, head `2051bbe0c4e0cf23343043dcd933759313a047a2`.

In that run:
- Constructor completed success and uploaded its artifact;
- independent Critic completed success and uploaded its artifact;
- aggregate failed before reading/comparing scientific values because `sympy` was not installed in the aggregate environment:

`ModuleNotFoundError: No module named 'sympy'`.

Frozen repair: add only `pip install sympy==1.13.3` to the aggregate job before executing the unchanged aggregate script. No scientific code, tensor formula, coordinate, parent image, PASS/FAIL/BLOCKED criterion, normalization or interpretation ceiling is modified.

The failed aggregate has no scientific verdict. Constructor/Critic artifacts remain non-authoritative until a terminal aggregate confirms the frozen comparison.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
