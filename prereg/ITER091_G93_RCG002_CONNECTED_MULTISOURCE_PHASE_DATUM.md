# Iter091 / G93 — RCG-002 connected multi-source phase datum audit

Status: PROSPECTIVE PREREGISTRATION — frozen before implementation/results.

## Scope lock
This gate uses only the RQIR-CG-owned RCG-002 relational controlled-phase seed and general algebraic tools. No QGR/KMQGB/MSQGR/RQIR physical ansatz, result, coefficient, or desired conclusion is imported.

## Question
Does the current RCG-002 controlled-phase architecture already contain a genuinely higher-order candidate-owned operational datum that can reduce the nonlinear completion freedom exposed by G86–G92?

## Frozen operational object
For three binary relational probes A,B,C, write the phase assigned to computational branch abc as theta_abc. Define the connected three-source phase by Möbius/inclusion-exclusion

Delta3(theta) = theta_111 - theta_110 - theta_101 - theta_011 + theta_100 + theta_010 + theta_001 - theta_000.

This object is evaluated algebraically; no microscopic gravity formula is inserted.

## Frozen scientific streams

### A — rephasing invariance
Verify exactly that Delta3 is invariant under addition of arbitrary constant, one-body phases f_A(a)+f_B(b)+f_C(c), and arbitrary pairwise phases f_AB(a,b)+f_AC(a,c)+f_BC(b,c). Test symbolic coefficients and a held-out rational panel.

PASS_A iff all such contributions cancel identically and a deliberately malformed sign pattern fails at least one invariance check.

### B — current RCG-002 pairwise controlled-phase content
Embed the existing two-probe RCG-002 controlled phase into all three pair channels with independent symbolic chi_AB, chi_AC, chi_BC, plus arbitrary one-body/local phases. Verify exactly whether Delta3 is zero.

PASS_B iff Delta3 == 0 identically for the current pairwise RCG-002 architecture.

Interpretation lock: zero is a NEGATIVE/ABSENCE result about a candidate-owned connected three-body datum; it is not a failure of the already established two-probe RCG-002 scoped channel.

### C — sensitivity positive control
Add a genuinely connected branch term kappa * a*b*c. Verify Delta3 = kappa exactly, and verify nonzero held-out rational kappa values are recovered without fit.

PASS_C iff symbolic recovery is exact and all held-out values match.

This is only an algebraic positive control. kappa is NOT an RQIR-CG physical parameter and may not be promoted into the candidate.

### D — rank / false-positive controls
Represent the eight branch phases as a linear design with columns: constant, 3 one-body, 3 pairwise, 1 connected-three-body. Verify the Delta3 functional annihilates the seven lower-order columns and has nonzero action on the connected column. Check exact rank and reject (i) a duplicated pair column labeled as connected and (ii) a zero connected column.

PASS_D iff these exact controls hold.

## Frozen aggregate rule
Scientific PASS of the audit requires PASS_A && PASS_B && PASS_C && PASS_D.

If all pass, terminal scientific classification is exactly:

`BLOCKED_RCG002_CURRENT_PAIRWISE_CHANNEL_HAS_NO_CANDIDATE_OWNED_CONNECTED_THREE_SOURCE_DATUM_SCOPED`

Scientific meaning: a clean connected operational observable exists, but the current RCG-002 seed supplies only one-/two-body phase structure, so it cannot yet map the G86–G92 nonlinear completion directions into a candidate-owned higher-order selector. The next gate must derive/add such a datum from RQIR-CG-owned dynamics rather than invent a fitted kappa.

If A/C/D fail because the algebraic construction itself is invalid, classify SCIENTIFIC_FAIL for this proposed observable. If execution/parsing/dependency fails before the frozen checks are evaluated, classify INFRASTRUCTURE/NUMERICAL FAIL and repair only the first causal technical defect without changing frozen science.

## Claim locks
Even aggregate PASS does NOT establish: new physics, gravity-mediated three-body interaction, nonlinear completion, coefficient selection, experimental confirmation, full quantum gravity, or theory establishment.

Readiness rule: G93 by itself does not increase programme readiness above the pre-gate 66%, because it diagnoses whether the selector datum exists; a BLOCKED terminal result leaves readiness unchanged.
