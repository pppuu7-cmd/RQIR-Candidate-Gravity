# Iter069 / G71 — unresolved architecture discriminator attack

Status: PREREGISTERED BEFORE IMPLEMENTATION
Date: 2026-09-13

## Authority and scope
Source of truth is newest main plus terminal G70 authority. This gate uses only the frozen mathematical architecture definitions already encoded by G70 streams B/C/D/E. It does not import physical assumptions, ansatz, results or desired conclusions from QGR, KMQGB or RQIR.

G70 terminal Pareto set is `{B,C,D,E}`. G71 asks which previously UNRESOLVED discriminator properties are logically implied by those frozen architecture definitions without adding candidate-owned dynamics.

## Frozen streams
Run four independent lanes with fail-fast:false.

### B — entire/pole-free linear form factor
Frozen object: `F(z)=exp(z^2)` multiplying the already transverse linear response.
Test:
1. exact complex zero set of F is empty;
2. F alone contains no retarded/advanced boundary-value prescription;
3. F alone contains no field-level path-integral/CTP measure or quantum rule.
Interpretation: no-new-finite-linear-poles remains SUPPORTED; retarded-causal and field-level-quantum properties remain BLOCKED_BY_MISSING_STRUCTURE, not FAIL.

### C — finite Gaussian CTP architecture
Frozen object: the G70 finite Gaussian CTP data `(D_R,N)` with lower-triangular retarded D_R and Gram noise N.
Test:
1. retarded and finite Gaussian quantum-rule properties are retained exactly;
2. the frozen C object contains no spacetime tensor embedding that defines a gravitational Ward identity;
3. the finite matrix object contains no momentum-domain denominator whose zeros could establish or exclude gravitational propagator poles.
Interpretation: Ward and finite-pole properties remain BLOCKED_BY_MISSING_EMBEDDING, not FAIL.

### D — non-Gaussian CTP cubic extension
Frozen object: the G70 cubic functional term `Gamma_3 = kappa3 * K_{abc} Delta_a Sigma_b Sigma_c` with nonzero symmetric K in b,c, added on top of the baseline quadratic CTP sector.
Exact target:
- all second derivatives of Gamma_3 with respect to fields vanish at the zero-field/background expansion point;
- therefore the cubic extension leaves the quadratic inverse propagator/Hessian unchanged at that point;
- hence it introduces no new *linearized* finite propagator poles by itself.
Controls:
- a deliberately quadratic extension must give a nonzero Hessian and be rejected by the cubic-Hessian-zero predicate;
- a constant/linear extension must not be misclassified as a cubic discriminator.
Retarded-causal status remains BLOCKED unless a retarded three-point kernel/order prescription is explicitly present in the frozen object.

### E — relational source-dependent transverse kernel
Frozen object: G70 source-dependent transverse scalar deformation built from conserved-source projectors.
Test:
1. transverse/Ward and no-new-finite-linear-poles properties retained;
2. source dependence alone does not define retarded support/boundary conditions;
3. source dependence alone does not define a field-level measure/CTP/path-integral quantum rule.
Interpretation: causal and quantum properties remain BLOCKED_BY_MISSING_STRUCTURE, not FAIL.

## Frozen aggregate rule
Each lane emits `valid`, property updates, exact checks and scope guards.

If every lane is valid and D proves exact zero quadratic Hessian while its quadratic control is nonzero, aggregate recomputes the Pareto set using the same G70 property ordering, treating BLOCKED as G70 UNRESOLVED for Pareto scoring.

Expected logically permitted outcomes are not frozen to a desired Pareto identity. The aggregate must compute it from lane outputs. If the computed non-dominated set shrinks, report that exact set only.

Allowed positive classification ceiling:
`BEYOND_BASELINE_UNRESOLVED_PROPERTY_AUDIT_SCOPED` plus computed Pareto set.

Invalid artifact/control failure => `INFRASTRUCTURE_OR_GATE_INVALID`.
A frozen logical predicate failure => `SCIENTIFIC_FAIL_FROZEN_ARCHITECTURE_PREDICATE`.
Missing structure => `BLOCKED_BY_MISSING_STRUCTURE`, never converted into FAIL.

## Claim locks
No architecture is selected as gravity. No candidate dynamics is authored. No NEW_PHYSICS_FOUND, FULL_QUANTUM_GRAVITY, ghost/unitarity theorem, literature novelty claim, experimental claim or readiness increase follows from G71 alone.
Programme readiness remains 66% and theory established remains 0% unless a later independently preregistered rubric gate authorizes otherwise.
