# Iter033 / G45-P — Complex Hermitian PSD Kossakowski provenance boundary

## Purpose
Response-blind implementation/provenance audit for a broader complex-Hermitian positive-semidefinite 6x6 Kossakowski layer on the six strictly local Pauli generators
`{X_A,Y_A,Z_A,X_B,Y_B,Z_B}`.

This gate does **not** use RCG-002 targets. Its purpose is to prevent an invalid enlargement of the classical comparator class: generic complex Hermitian PSD Kossakowski matrices are legitimate GKSL objects, but they must not be called classical shared random-Hamiltonian noise unless classical/local-product provenance is actually retained.

## Frozen panels
Four deterministic shards are evaluated for each panel (`12` lanes total):
1. `real_psd_control`: real symmetric PSD Kossakowski controls generated from real noise modes. These are the explicit classical random-Hamiltonian controls.
2. `same_site_complex`: complex PSD controls with a frozen relative phase between two Pauli components on the same subsystem.
3. `cross_site_complex`: complex PSD controls with a frozen relative phase between one generator on A and one on B.

The panel definitions and RNG seeds are fixed in the implementation before production results are viewed.

## Frozen diagnostics
For every lane:
- Kossakowski Hermiticity residual <= `1e-12`;
- minimum Kossakowski eigenvalue >= `-1e-10`;
- maximum trace-preservation residual over `t={0.1,0.5,1.0}` <= `1e-10`;
- minimum Choi eigenvalue over the same times >= `-1e-8`;
- finite generator/channel diagnostics.

Additional provenance diagnostics:
- channel unitality residual `||E_t(I)-I||`;
- generator distance from the generator built from `Re(C)`;
- least-squares residual after projecting that generator difference onto the six-dimensional **local Hamiltonian commutator** span;
- least-squares residual after projecting onto the full fifteen-dimensional two-qubit Hamiltonian commutator span;
- product-input output negativity scan on 16 deterministic product states at `t=0.7`.

For `real_psd_control`, require:
- unitality residual <= `1e-10`;
- generator difference from `Re(C)` <= `1e-12`;
- explicit simultaneous-noise local-product unitary factorization error <= `1e-12`;
- product-output negativity <= `1e-9`.

For each complex lane, define a **classical-provenance obstruction witness** if at least one of the following prospectively frozen conditions holds:
- unitality residual > `1e-6`; or
- residual after projection onto the local-Hamiltonian commutator span > `1e-6`; or
- product-output negativity > `1e-8`.

## Aggregate interpretation
`COMPLEX_PSD_EXTENDS_BEYOND_CLASSICAL_RANDOM_HAMILTONIAN_PROVENANCE_ON_FROZEN_CONTROLS` iff:
- all 12 lanes are structurally/admissibly valid;
- all four real controls pass their classical provenance rules; and
- at least one same-site complex lane and at least one cross-site complex lane exhibit a frozen classical-provenance obstruction witness.

If all lanes are valid but one required complex panel has no obstruction witness, classify `COMPLEX_PSD_PROVENANCE_BOUNDARY_PARTIAL_OR_UNRESOLVED`.
Structural/admissibility failure is `STRUCTURAL_NUMERICAL_FAIL` and is not a physics result.

## Claim locks
- No RCG-002 target is used.
- No comparator-separation claim is authorized by this gate.
- No statement that all complex PSD GKSL channels are nonclassical is authorized.
- No statement that the complex-Hermitian PSD family is a classical mediator family is authorized.
- No readiness increase from this implementation/provenance gate alone.
