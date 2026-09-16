# RQIRCG research ledger — RCG003 D3 / nonlinear-closure addendum

Date: 2026-09-17

## Programme transition

Fresh parent recovery was still `PROGRAMME_DISPOSITION_AUTHORITY_BLOCKED` before this iteration. The external explicit declaration supplied on 2026-09-17 was consumed once under canonical preregistration `e366de3c68b38dad0a2e3388e5cc8e7801cb1c41`.

- declaration record: `results/RCG002_D3_PROGRAMME_AUTHORITY_DECLARATION.md`, commit `464bbb6fd3c602a1fdc5194f0a6a03b8327fb7f4`;
- governance terminal: `results/RCG002_PROGRAMME_DISPOSITION_D3_TERMINAL.md`, commit `d9187a60d2e7545ae3f082762d4a747b9681b69f`;
- classification: `D3_AUTHORIZED_SCOPED_NEW_VERSION_FORMATION_ATTEMPT`.

Historical RCG-002 science was not rewritten. RSC remains `NEAR_SURVIVOR_NOT_SELECTED`; AD1 remains `ARCHITECTURE_DISPOSITION_NOT_UNIQUELY_SELECTED_PREOUTCOME`; `chi_ABC` remains unauthorized; theory established remains 0%.

## RCG003 prospective formation

Preregistration:

`prereg/RCG003_MINIMAL_NONLINEAR_VERSION_FORMATION_AND_CLOSURE_GATE.md`

commit `0bba0ea6e1d4e13635f70f3b5056e131afba6c7d`.

RCG003-v0 freezes a local classical 4D metric family whose cubic Ricci deformation sector is

`lambda R^3 + mu R R_{mu nu}R^{mu nu} + nu Tr(Ricci^3)`.

The cubic basis and its promotion to candidate dynamics are NEW_MODEL_POSTULATE. The Einstein-Hilbert term is REFERENCE/CONTROL only. Production source is vacuum. Matter, observable, quantum state and measure remain outside the gate.

All 22 formation slots required by the D3 formation protocol are explicitly classified.

## First hard structural gate

Discriminator: exact homogeneous conformal no-extra-time-derivative lock.

Implementation commits:
- constructor `f7f9c2f9bf69c226f26601d7045513c2f410ba9e`;
- independent Critic `68a726ef72a124fb4deba58e07b725635aa58d86`;
- aggregate `48eafce9606252702686b2b88aaa0b126d216f88`;
- workflow head `9e710f12f0b1bc79d6e2bc6bc2a77fe81b9a8aa5`.

GitHub Actions run `35152559990`: `success`.

Artifacts:
- constructor `10469790962`, `sha256:ac50a966dbcfbd51342b18be353d1724badb78f31c7812144c91128417a22c12`;
- Critic `10469348848`, `sha256:65ebf79c5e30996a89dcaeb346df19a6d36ff971da1b5a22780708b2c831f5ac`;
- terminal aggregate `10470035974`, `sha256:34fdedbc1734ee27227b3b96bc4d3b5a0f240e95709f169b91542a5e717cd9d1`.

Exact compatibility matrix in `(lambda,mu,nu)` coefficient order:

`[[1296,432,180],[1296,288,36]]`.

Results:
- raw dimension `3`;
- exact rank `2`;
- nullity/residual dimension `1`;
- primitive survivor `(7,-36,36)`;
- every preregistered control passed;
- independent Critic reproduced rank/nullspace and passed chronology, anti-fit, firewall and scope checks.

Terminal:

`results/RCG003_MINIMAL_NONLINEAR_CLOSURE_TERMINAL.md`

commit `ded5a44078c57909aeb6592b88bdac5c0917f85d`.

Primary classification:

`PASS_SCOPED_RCG003_CONFORMAL_SECOND_ORDER_NONZERO_DEFORMATION_EXISTS`.

Formation side classification:

`RCG003_MINIMAL_NONLINEAR_FAMILY_FORMED_FOR_VACUUM_STRUCTURAL_TEST_SCOPED`.

## Scientific meaning

The first new-version gate reduces the bounded candidate coefficient space from three raw dimensions to one. It does not establish the surviving ray as physical, globally unique or generally second order. The result is confined to the frozen classical vacuum homogeneous-conformal structural test.

## Next prospectively frozen discriminator

`prereg/RCG003B_AXISYMMETRIC_BIANCHI_I_DERIVATIVE_CLOSURE.md`

commit `dbb0b54465c628b533c646a5b3b74b8458eaf24e`.

RCG003B freezes the survivor `(7,-36,36)` without refit and tests exact acceleration-Hessian plus velocity-curl closure on axisymmetric Bianchi-I off-shell histories. It has not been evaluated in this addendum.

If it FAILS, the combined conformal+anisotropic derivative-order requirements reduce the current nonzero ray dimension from 1 to 0 inside RCG003-v0. If it PASSES, the residual ray remains one-dimensional and must face a different structural discriminator.

## Locks

No GR derivation, complete theory, full nonlinear constraint closure, matter completion, quantum gravity, experiment, `chi_ABC`, or new-physics claim follows. `THEORY_ESTABLISHED=0%`.
