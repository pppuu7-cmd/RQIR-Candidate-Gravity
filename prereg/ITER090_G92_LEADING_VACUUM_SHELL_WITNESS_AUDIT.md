# Iter090 / G92 — leading Einstein-vacuum shell witness audit — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN BEFORE IMPLEMENTATION / BEFORE RESULTS**
Programme readiness entering gate: **66%**
Theory established entering gate: **0%**

## Motivation
G90/G91 established explicit off-shell local generally covariant two-invariant completion families using Ricci-scalar/Ricci-tensor densities. Their scope ceiling explicitly left field-redefinition/on-shell redundancy open. This gate asks a narrower prospective question: do those exact frozen witness families remain nontrivial on the leading Einstein-vacuum shell `R_{mu nu}=0` (hence `R=0`), or do they vanish there?

This is a robustness/qualification gate only. The leading Einstein-vacuum shell is not asserted to be the complete nonlinear RQIR-CG shell, and failure on this shell does not erase the valid off-shell G90/G91 results.

## Frozen witness definitions
C family from G90:
- `J1 = R^3`
- `J2 = R * Ricci2`, where `Ricci2 = R_{mu nu}R^{mu nu}`.

D family from G91:
- `K1 = R^4`
- `K2 = R^2 * Ricci2`.

Leading Einstein-vacuum shell substitution:
- `R -> 0`
- `Ricci2 -> 0`.

Independent curvature control uses a trace-free algebraic Weyl-spectrum surrogate `lambda=(l1,l2,l3)` with `l1+l2+l3=0` and
- `W2=sum(lambda_i^2)`
- `W3=sum(lambda_i^3)`
- `W4=sum(lambda_i^4)`.
The frozen nonzero samples are `(1,2,-3)`, `(2,-5,3)`, `(1,-4,3)`. This control is only to show that imposing Ricci-flatness does not algebraically force all higher-curvature information to vanish; it is not a full 4D tensor-realizability theorem.

## Frozen lanes and interpretation rules
### Lane A — C shell projection
Require exact `J1=J2=0` under `R=Ricci2=0`, for symbolic coefficients and all frozen coefficient samples. Expected classification only if exact: `C_G90_RICCI_ONLY_WITNESSES_VANISH_ON_LEADING_EINSTEIN_VACUUM_SHELL_SCOPED`.

### Lane B — D shell projection
Require exact `K1=K2=0` under the same shell. Expected classification only if exact: `D_G91_RICCI_ONLY_WITNESSES_VANISH_ON_LEADING_EINSTEIN_VACUUM_SHELL_SCOPED`.

### Lane C — independent curvature control
Require trace-free frozen spectra and at least one exact nonzero `W3` and nonzero `W4` on every frozen nonzero spectrum; require the zero spectrum to give `W2=W3=W4=0`. Expected classification: `RICCI_FLAT_SHELL_DOES_NOT_FORCE_ALL_ALGEBRAIC_WEYL_INVARIANTS_ZERO_SCOPED`.

### Lane D — false-positive controls
Require: (i) generic off-shell substitutions make at least one C and one D witness nonzero; (ii) setting only `R=0` already zeros these specific families because each carries an explicit `R` factor; (iii) a deliberately constant invariant control remains nonzero on shell and therefore must not be misclassified as shell-vanishing. Expected classification: `VACUUM_SHELL_AUDIT_FALSE_POSITIVE_CONTROLS_SCOPED`.

## Frozen aggregate rule
Only if A/B/C/D are valid with exactly the classifications above, aggregate classification is:
`BLOCKED_G90_G91_RICCI_ONLY_COVARIANT_WITNESSES_VANISH_ON_FROZEN_LEADING_EINSTEIN_VACUUM_SHELL_SCOPED`.

Scientific interpretation if valid:
- G90/G91 remain valid explicit **off-shell** covariant underdetermination witnesses.
- Their chosen Ricci-only invariant pairs do **not** by themselves establish independent deformation directions after quotienting by the leading Ricci-flat vacuum shell.
- The next admissible covariant robustness step must use a prospectively frozen family with genuine Riemann/Weyl content and/or an explicit field-redefinition/boundary-identity quotient.

## Scope locks
A valid aggregate is NOT:
- proof that G90/G91 are wrong;
- proof that all Ricci-containing operators are physically redundant in every setting;
- proof that the full RQIR-CG nonlinear shell is Ricci-flat;
- proof of S-matrix equivalence or a complete field-redefinition quotient;
- a unique nonlinear theory or new physics result.

Readiness remains 66% regardless of PASS/BLOCKED outcome unless a separate rubric gate is prospectively defined later. `THEORY_ESTABLISHED=0%` remains locked.
