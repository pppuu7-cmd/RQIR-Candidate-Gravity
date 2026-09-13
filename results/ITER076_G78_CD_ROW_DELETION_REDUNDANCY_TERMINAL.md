# Iter076 / G78 — C/D anchored-design row-deletion redundancy — TERMINAL

Date: 2026-09-13

Classification: `G75_ANCHORED_DESIGN_SINGLE_ROW_FAILURE_MODES_AND_MINIMAL_CUBIC_REDUNDANCY_SCOPED`
Scientific status: **PASS, scoped**
Programme readiness: **66%**
Theory established: **0%**

## Frozen authority
- sibling base: terminal G75 commit `c91151054a460cb804f054fc4eb81eedff08945a`
- preregistration: `de3ade19f09494623c7d0bcc91bff9f80bb640d7`
- implementation: `6bf9c09925ee42d3c0afe72ee8f3fa4691a588fa`
- production head: `6bd35ee2b5dc4e97d66138bfd6d236bb39862e3b`
- branch: `g78-row-deletion-redundancy`
- run: `34782616139`
- jobs: A `103792259978`, B `103792259785`, C `103792259864`, D `103792259890`, aggregate `103792304860`
- artifacts/digests:
  - A `10324918299`, `sha256:e616f4228048f698511856e5a01878369c5da33ad2d158d2c67cf8113b87ee53`
  - B `10325955002`, `sha256:8fa650b04f75c47d52bca7c3eeaaff717b623307e04c8691e4e1bc9d3fa6670d`
  - C `10325675983`, `sha256:803505f08dda4316998dfe86078b68430242da2be97ec543c3518cc65f48d36e`
  - D `10325621772`, `sha256:a13cba53f48324f3cd8f2c9eff388e0c85549d89c8b1545e805c875330d698c7`
  - aggregate `10325651143`, `sha256:65f959d3fd514e096a4bdc83d49e179621ea183530d5ae5d006943da41daa95b`

## Frozen result
All four raw streams and the frozen aggregate were independently rechecked against the preregistered predicates before terminal classification.

- A `SINGLE_ROW_DELETION_FAILURE_MAP_SCOPED`: full anchored rank is four. Deleting any one of the four ordinary quadratic rows preserves rank four, whereas deleting the sole cubic target row, AQ, or AD reduces rank to three.
- B `DISTINCT_CUBIC_ROW_ADDS_SINGLE_FAILURE_REDUNDANCY_SCOPED`: adding one prospectively frozen distinct cubic-response row preserves full rank if either cubic row is deleted individually; deleting both cubic rows reduces rank to three.
- C `ROW_REDUNDANCY_FALSE_POSITIVE_CONTROLS_SCOPED`: duplicated AQ without AD, duplicated AD without AQ, and a same-shape cubic pseudo-row each remain rank three and therefore do not fake redundancy.
- D `HELDOUT_SINGLE_ROW_FAILURE_PATTERN_SCOPED`: the exact `[4,4,4,4,3,3,3]` single-row-deletion rank pattern is reproduced on all three held-out momentum panels.

## Scientific interpretation
Inside the exact G75 tangent design, the four ordinary quadratic rows contain single-row redundancy, but the sole cubic target-support row and both independent alias-breaking anchors are single points of algebraic failure. One additional linearly distinct cubic-response row is sufficient to remove the cubic single-row failure in the frozen construction. This is scientifically independent from G76/G77 because G78 was frozen directly from terminal G75.

## Scope ceiling
This result does **not** establish that the algebraic rows correspond to physically realizable measurements, define detector redundancy requirements, select C or D, determine physical coefficients, define candidate-owned RCG-002 dynamics, establish nonlinear/quantum closure, or establish new physics.
