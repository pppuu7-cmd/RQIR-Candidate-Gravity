# Construction Protocol

## Independence constraint

The candidate built here is derived from the original RQIR reconstruction funnel only. During the derivation phase, do not import the architecture, equations, parameterization, or benchmark-specific repairs of the separately developed QGR candidate.

## Derivation stages

1. Freeze the authoritative RQIR requirements and gates.
2. Translate each gate into a mathematical constraint.
3. Identify the minimum state variables and degrees of freedom required to satisfy the full constraint set.
4. Derive the least-structured admissible dynamics compatible with those constraints.
5. Define the observable map before tuning any phenomenological parameters.
6. Separate design constraints from holdout tests.
7. Re-run the frozen RQIR validation without changing the gates.
8. Only after validation compare this candidate with the polygon-derived QGR candidate.

## Anti-overfitting rules

- No post-hoc modification of RQIR gates to rescue the model.
- Penalize arbitrary functions, free parameters, and unmotivated auxiliary fields.
- Every added degree of freedom must be traceable to a specific frozen requirement.
- A failed holdout test is recorded as a failure, not absorbed by redefining the target.

## Current status

Repository initialized. The next authority step is to import the exact frozen RQIR gate set and build the requirement-to-mathematics matrix.
