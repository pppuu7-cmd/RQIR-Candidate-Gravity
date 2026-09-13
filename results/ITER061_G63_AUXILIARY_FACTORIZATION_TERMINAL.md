# Iter061 / G63 — auxiliary second-order factorization terminal result

Classification: `FOUR_DERIVATIVE_LINEARIZED_AUXILIARY_TWO_MODE_INDEFINITE_INERTIA_SCOPED`

Frozen preregistration: `f448a07cccfa6a1914f8e74416dcb330dc1e2ed1` (before implementation).
Implementation: `4cf527a9c7166a2c51adcb50b7eeb7da08f59eb2`.
Production head: `4bc52cc3cf7b34075cdab83fc758756034a2d714`.
Authoritative run: `34764255219`.

Raw artifacts consumed:
- A job/artifact `103742305251/10320022178`, digest `sha256:181239451b1754b8ff47f3c9371f9d3eefdab5ac45ce10ef6fd6c400296b1b97`.
- B `103742305375/10319654009`, digest `sha256:bff82ef23ba8b706d454d3649e4a09f1780a9f7481a454ade538bf22933290f9`.
- C `103742305320/10319434714`, digest `sha256:4320cc4993303bea9a9de66a55fae3fa8e9c10e714a430b24515971f0c1a2695`.
- D `103742305423/10319149479`, digest `sha256:8d037579a8804e7ec70c6637a0f928b02b8c7ffd863a7f9fba56f8b57e1b7cf7`.
- Aggregate job/artifact `103742340642/10319009822`, digest `sha256:9bdb66ab443a353cad3d143789f6161d2cdfd6a468c93bdc0b4b857a4bb51b2e`.

Frozen result:
- A reconstructs both frozen sector responses exactly with two second-order auxiliary modes. TT residues are `(-1/2,+1/2)`, scalar residues `(+1/6,-1/6)`, and the auxiliary quadratic form has inertia `(1,1)` in each nonexceptional sector.
- B: all 12 frozen rational rays / 24 nonexceptional sector cases pass exact reconstruction and inertia `(1,1)`.
- C: 16/16 frozen real-congruence transformations preserve the indefinite inertia.
- D: both exceptional one-pole limits pass; deliberately definite-sign and zero-coupling fake controls are rejected.
- Aggregate is valid with A/B/C/D all true.

Scientific implication: in the same frozen linearized conserved-sector representatives used by G61–G62, the nonexceptional two-pole response admits an exact two-mode second-order auxiliary representation whose real quadratic form has one positive and one negative direction, invariant under the preregistered invertible real congruences. This is an algebraic source-coupled auxiliary-form statement only. It is **not** a physical-ghost theorem, instability or quantum-unitarity result; it selects no candidate coefficients and is not a global higher-derivative no-go theorem.

Programme readiness remains 66%; theory established remains 0%.