# Iter033 / G45-P — terminal result

Run `34718225194`, launch/head `35583bcaa013944017a18c56f8f05714b616ee81`.
Aggregate job `103620231708`; summary artifact `10305418039`; digest `sha256:728b361f4a317e3ffa3f444f1f4cb5198f3dda21ce1411fdf4f4affdf581f80b`.

This response-blind gate used no RCG-002 target. It audited whether generic complex-Hermitian PSD Kossakowski matrices on the six local Pauli generators may be treated as the same classical shared random-Hamiltonian family as real-symmetric PSD matrices.

All 12/12 lanes were structurally/admissibly valid.

- `real_psd_control`: 4/4 provenance controls pass, obstruction count 0; maximum residual after projection onto the full real-Kossakowski + local-Hamiltonian span `1.0491377545756667e-15`; max unitality residual `3.8538635855967375e-16`.
- `same_site_complex`: 4/4 valid, obstruction count 4; max full-span residual `0.5999999999999999`; max unitality residual `0.5096015967570404`.
- `cross_site_complex`: 4/4 valid, obstruction count 4; max full-span residual `0.4242640687119284`; max unitality residual `1.9442411326939686e-16`.

Classification:

`COMPLEX_PSD_EXTENDS_BEYOND_CLASSICAL_RANDOM_HAMILTONIAN_PROVENANCE_ON_FROZEN_CONTROLS`

## Consequence

The generic complex-Hermitian PSD GKSL family must not be relabelled as a classical random-Hamiltonian comparator without an additional constructive classical/product-unitary provenance proof. The current classical Markovian comparator authority therefore remains the real-symmetric PSD subset (and separately validated explicit classical-memory constructions).

This is a provenance boundary, not a comparator-separation result, and it does not change programme readiness by itself.
