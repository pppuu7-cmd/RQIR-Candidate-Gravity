# Current Scientific Front

**Repository:** `RQIR-Candidate-Gravity`  
**Active branch:** `rqir-derived-model-v0`  
**Independence rule:** do not inspect or import the separately developed polygon-derived QGR candidate until the independent RQIR branch formally opens the blind-comparison checkpoint.

## Frozen authority

Use `docs/RQIR_V1_AUTHORITY_SNAPSHOT.md` and `model/REQUIREMENTS_MATRIX.md`.

## Current RQIR-only reconstruction result

The active authority result is now:

`model/RQIR_DERIVED_EQUIVALENCE_CLASS_V0.md`.

Frozen RQIR strongly constrains admissible gravity interfaces but, without an extra microscopic postulate, does not presently select one unique C5-distinct theory.

Conditional minimum-complexity result:

`frozen RQIR + metric-only + local covariance + two-derivative leading dynamics + ordinary quantization -> low-energy quantum GR/EFT (C5-like)`.

Authority: `model/CONDITIONAL_MINIMAL_COMPLETION_001.md`.

## ANSATZ-RQIR-MIN v0.1

Status: **DRAFT / CONTROL ROOT**.

- QG-001: PASS
- QG-002: PASS
- Newtonian QG-003 subcheck: PASS, full gate BLOCKED
- explicit weak-field normalization: `nabla^2 Phi = 4 pi G rho`
- scientific role: least-structured C5-like representative, not a novel theory claim

Canonical files:

- `model/ANSATZ-RQIR-MIN/MODEL.md`
- `model/ANSATZ-RQIR-MIN/FOUNDATIONAL_DERIVATION_001.md`
- `model/ANSATZ-RQIR-MIN/MINIMALITY_RESULT_001.md`
- `model/ANSATZ-RQIR-MIN/GATE_STATUS.yaml`

## ANSATZ-RQIR-QLC v0.1

Status: **DRAFT / OPERATIONAL REPRESENTATION**.

Core channel language:

`d_Y = K d_X + d_0`

`V_Y = K V_X K^T + Y_G`

`Y_G + i hbar/2 (Omega_Y - K Omega_X K^T) >= 0`.

One-mode CP calculation:

`y_min = hbar |1-eta|/2`.

However the first novelty mechanism has been rejected:

1. a pure Gaussian unitary dilation reproduces the CP-saturating law exactly;
2. generic L3 ordered/retarded response is also available to an ordinary quantum mediator;
3. mere L4 higher cumulants or L5 process quantumness are likewise not novelty criteria.

Therefore QG-007 remains **BLOCKED**.

Canonical negative-result files:

- `model/ANSATZ-RQIR-QLC/FOUNDATIONAL_DERIVATION_002.md`
- `model/ANSATZ-RQIR-QLC/FOUNDATIONAL_DERIVATION_003.md`
- `model/ANSATZ-RQIR-QLC/FOUNDATIONAL_DERIVATION_004.md`
- `model/RQIR_CG_NO_GO_001_GAUSSIAN_INTERFACE.md`
- `model/RQIR_CG_NO_GO_002_UNDERDETERMINATION.md`

## Extra-axiom audit

`model/NEXT_AXIOM_SEARCH.md` separates `RQIR-FORCED` structure from `EXTRA-HYPOTHESIS` candidates.

The two lowest-cost possible closures were audited:

- H7 relational process composition: **not RQIR-forced**;
- H2 higher-order Ward/positivity/causality closure: **not uniquely closing in general**.

Authorities:

- `model/AXIOM_AUDIT_H7_PROCESS_COMPOSITION.md`
- `model/AXIOM_AUDIT_H2_CROSS_ORDER_CLOSURE.md`

## Immediate scientific frontier

Issue #4 controls the next work:

> Find a sector-specific C5-distinct L4/L5 obstruction or quantitative cross-order relation using only frozen RQIR plus explicitly declared physical assumptions.

If no such obstruction is found, preserve `RQIR-EQUIV-CLASS-V0` as the final RQIR-only reconstruction output. A genuinely new microscopic model would then require an independently motivated `EXTRA-HYPOTHESIS`, clearly labeled as such.

Do not add a field, arbitrary nonlocal kernel, intrinsic decoherence law, nonlinear source rule or modified process composition merely to manufacture novelty.
