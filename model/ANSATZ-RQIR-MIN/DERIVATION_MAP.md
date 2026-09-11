# Derivation Map — ANSATZ-RQIR-MIN v0.1

Every RQIR-facing quantity must descend from the single action in `MODEL.md`.

| Target object | Parent definition | Current derivation state | Next authority needed |
|---|---|---|---|
| Physical matter state | `rho_phys` on constrained matter x gravity space | specified | explicit gauge/constraint realization |
| `J=<T>` | first functional derivative / expectation of renormalized stress tensor | defined | choose renormalization/smearing convention |
| `N` | centered symmetrized second stress-tensor correlator | defined | derive in one toy matter sector and verify positivity after smearing |
| `D` | stress-tensor commutator kernel | defined | derive ordering/sign convention in same toy sector |
| `chi^R` | retarded commutator response | defined | causal-support certificate |
| `h` mean response | retarded graviton propagator convolved with `J` | skeleton derived | tensor projector and normalization derivation |
| metric covariance | intrinsic gravity covariance + `G_R * N * G_A` sourced term + higher orders | skeleton derived | no-double-counting/renormalization derivation |
| Q1 clock observable | relational phase/proper-time functional | not derived | explicit gauge-completed clock construction |
| Q2 superposed-source response | same action evaluated on coherent source preparation | not derived | finite source toy model |
| Q3 source rule | action + CTP hierarchy | structural derivation present | explicit perturbative map |
| Q4 quantum-information channel | reduced gravity-mediated channel | not derived | integrate mediator / channel derivation |
| Q5 geometry fluctuations | metric two-point/curvature proxy | structural derivation present | relational curvature observable |
| Q6 causal/process object | retarded propagator/process map | not derived | detector/process construction |
| Q7 EFT correction | curvature EFT expansion | specified | order-by-order power counting and C5 comparison |

## Dependency graph

`state space -> covariant action -> CTP functional -> J/N/D/chiR -> gravity response/covariance -> relational observables -> comparator residual -> Paper I -> Paper II -> Paper III`

No arrow may be bypassed by inserting a detector kernel chosen for favorable discrimination.

## First derivation sprint

1. Fix metric signature, curvature and kappa conventions.
2. Expand Einstein-Hilbert + matter action to the first nontrivial weak-field order.
3. Derive the linearized field equation and conserved-source projector.
4. Recover the Newtonian Poisson equation.
5. Write the physical retarded Green object and causal support statement.
6. Derive one smeared source example giving `J,N,D,chiR` in one convention.
7. Perform the C5 equivalence/degeneracy audit before introducing any deformation.
