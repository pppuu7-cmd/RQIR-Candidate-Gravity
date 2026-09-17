# RQIR-Candidate-Gravity current front

Updated: 2026-09-17 after canonical RCG006 generator freeze and terminal L0 first-order EH field-redefinition map subgate.

## Canonical programme/scientific phase

`RCG002_HISTORICAL_SCIENCE_TERMINAL / RCG003B_AXISYMMETRIC_FAIL / RCG004_COMPLETE_ALGEBRAIC_CUBIC_CLASS_TERMINAL_FAIL / RCG005_COMPLETE_LOCAL_DIM6_PURE_METRIC_CLASS_TERMINAL_FAIL / RCG006_FIELD_REDEFINITION_EQUIVALENCE_AUDIT_ACTIVE`

Historical RCG002/RCG003/RCG003B/RCG004/RCG005 terminals remain unchanged. This file is a current-front pointer, not a rewrite of historical result notes.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.

## RCG005 parent authority retained

Terminal: `results/RCG005_COMPLETE_LOCAL_DIM6_PURE_METRIC_CURVATURE_TERMINAL.md`.
Terminal commit: `aef9882924ffd128c6c30934e4f95394aae874fc`.
Classification: `FAIL_SCOPED_RCG005_COMPLETE_LOCAL_DIM6_PURE_METRIC_CLASS_HAS_NO_NONZERO_SECOND_ORDER_SURVIVOR` under the frozen representative-level, off-shell second-order convention.

RCG006 does not retroactively rewrite this result.

## RCG006 programme and scientific contract

Programme selection terminal: `dc955720822d353d446186437ee2ca69458633bd`.
Selected direction: `FIELD_REDEFINITION_EQUIVALENCE_AUDIT`.

Scientific preregistration: `prereg/RCG006_BOUNDED_LOCAL_METRIC_FIELD_REDEFINITION_EFT_EQUIVALENCE_AUDIT_V0.md`, commit `fc3ff1f49c56f2befc039e09ebd8f388833dbff1`.

Map implementation contract: `prereg/RCG006_FIELD_REDEFINITION_MAP_IMPLEMENTATION_CONTRACT.md`, commit `78789e048ab3d67fc8f2e901176ff3a352aad749`.

Scope remains first-order, local, perturbatively invertible, parity-even pure-metric field redefinitions. Bulk-action equivalence only. Boundary observables, matter couplings, global solution spaces, causal structures, quantum measures and nonperturbative theory identity remain out of scope.

## Canonical RCG006 generator space — terminal pre-map freeze

Result: `results/RCG006_GENERATOR_COMPLETENESS_FREEZE.md`.
Commit: `8c8314d2b857d6caa9719d6ba33e856ea0a697af`.
Classification: `PASS_RCG006_GENERATOR_COMPLETENESS_READY_TO_FREEZE`.

Exact generator quotient:
- `M_ALG = 6` algebraic curvature-squared symmetric rank-2 directions;
- `M_DER = 3` genuinely new derivative principal directions;
- **`M = 9`** total frozen generator directions.

Production generator basis is frozen and cannot be changed after seeing map/discriminator outcomes.

## Canonical L0 first-order EH map — terminal scoped subgate

Terminal note: `results/RCG006_MFR_L0_MAP_TERMINAL.md`.
Canonical raw/provenance: `results/raw/RCG006_MFR_L0_CANONICAL.json`.
Terminal note commit: `12ca52947d1390a494634b7a6a2d98d9a7e4bf7d`.

Canonical workflow run: `35250324503`, head `d781765b80d371033d1b6477f32693c2023838e6`.
Constructor, independent Critic and aggregate all completed success.

Classification: `PASS_SCOPED_RCG006_MFR_L0_MAP_SUBGATE`.

Exact facts:
- `M_FR` shape `8 x 9`;
- `rank(M_ALG)=5`;
- **`rank(M_FR)=7`**;
- `dim ker(M_FR)=2`;
- **`dim Q_EFT = 1`**;
- `dim(RCG004_subspace ∩ Im(M_FR)) = 5`;
- residual inherited cubic quotient dimension `1`;
- `D1D1_CLASS_9` is in `Im(M_FR)`;
- `D1D1_CLASS_11` is not in `Im(M_FR)`;
- modulo `Im(M_FR)`, `[D1D1_CLASS_11] = (3/4)[RCG004_CANONICAL_AXIS_8]`.

Canonical `M_FR` SHA256:
`7ac6ba6d1003c676899c0017409e3466a7f5e12fbb4114feee94580f1b0799bd`.

Canonical image-span SHA256:
`7c5e4b07d95881b907ed67a55742466c2889e99c20193806b834370a00f46788`.

This is a first-order bulk EFT-equivalence statement only. It is not a gravity-candidate PASS.

## Active authoritative gates

### A_HD orbit transport

Workflow: `.github/workflows/rcg006-ahd-transport.yml`.
Run: `35250686885`.
Head: `7af702935db7db904f08a0e70e6f8187dc61d859`.

Status at this recovery write: non-terminal/queued.

Frozen purpose: independently reconstruct the RCG005 higher-derivative discriminator `A_HD`, require rank `8` and kernel zero before consuming the RCG006 image, then compute `rank(A_HD M_FR)` and classify the preregistered structural branch.

Do not use partial values and do not launch a competing authoritative transport gate while this run is non-terminal.

### Symbolic-Lambda companion

Workflow: `.github/workflows/rcg006-lambda-companion.yml`.
Head: `56c0b6c2614f99c5cffb84bc99d2e56b45a84e05`.

This independent lane tracks `Lambda * Q_dim4_companion` leakage separately from the L0 eight-dimensional parent and verifies that derivative-generator traces are bulk total divergences. It cannot change the already-terminal L0 `M_FR` rank.

If its workflow is non-terminal, do not use partial substantive values and do not duplicate it.

## Current scientific interpretation

RCG006 has already shown that seven of the eight frozen RCG005 bulk action directions are first-order EH field-redefinition image directions, leaving a one-dimensional EFT quotient. Whether the frozen representative-level higher-derivative discriminator is invariant along those admitted EFT orbits is still pending the terminal `A_HD` transport gate.

Therefore no terminal RCG006 classifier may yet be promoted from this recovery file alone.

## Claim locks

- no `NEW_PHYSICS_FOUND`;
- no `FULL_QUANTUM_GRAVITY`;
- no `THEORY_ESTABLISHED`;
- no GR uniqueness theorem;
- no arbitrary modified-gravity no-go;
- no boundary-observable equivalence;
- no matter-coupled equivalence;
- no nonperturbative field-redefinition equivalence;
- no `chi_ABC` computation before separate authority.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.

## Next admissible action

1. If either active workflow is non-terminal, inspect only status/provenance and do not consume partial scientific values.
2. Once `A_HD` transport is terminal, validate Constructor/Critic/aggregate and persist its authority.
3. Once symbolic-Lambda companion is terminal, validate and persist its independent authority.
4. If both are valid, assemble the frozen RCG006-v0 terminal structural audit without adding or removing generators or changing classifiers.
5. Only after RCG006 terminalization choose any successor programme gate prospectively. `chi_ABC` remains unauthorized.
