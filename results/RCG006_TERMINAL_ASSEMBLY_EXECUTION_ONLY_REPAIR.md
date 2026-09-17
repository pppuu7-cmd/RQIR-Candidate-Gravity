# RCG-006 — terminal assembly execution-only provenance repair

Date: 2026-09-17
Status: **PROSPECTIVE EXECUTION-ONLY REPAIR BEFORE RETRY**

Frozen scientific preregistration: `fc3ff1f49c56f2befc039e09ebd8f388833dbff1`.
Frozen terminal assembler: `scripts/rcg006_terminal_assemble.py`, commit `c566cab822b7403782715fd8797543b9afa15f0d`.
Initial assembly run: `35253070307`, head `a6ac95f0daa72c0ffb40441340ef1ef049a44523`.

The initial assembly stopped in the chronology guard before the assembler or scientific classifier executed. The failure was:

`fatal: Not a valid commit name a067bca23fd01bc002afe3e66e8164549986aee8`

The stale SHA was only an obsolete pointer for the already-terminal symbolic-Lambda result. Current repository history for `results/RCG006_SYMBOLIC_LAMBDA_COMPANION_TERMINAL.md` gives the reachable terminal authority commit:

`cc81ea497e11b9d8ab590ed3c36c8b1f2f4d1a43`.

The held-out terminal authority remains reachable at
`f537a7611b8a0787df65af3bdee4c0344e12fcf3`,
and the frozen terminal assembler remains reachable at
`c566cab822b7403782715fd8797543b9afa15f0d`.

Frozen repair: replace only the obsolete symbolic-Lambda chronology pointer `a067...` with the reachable commit `cc81ea...` and require this repair record to precede the retry. No canonical JSON, scientific input, classifier, rank, quotient, interpretation ceiling, PASS/FAIL/BLOCKED/INVALID rule or claim lock is modified.

The failed run has **no scientific classification** because the assembler never executed.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
