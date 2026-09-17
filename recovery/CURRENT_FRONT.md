# RQIR-Candidate-Gravity current front

Updated: 2026-09-17 after canonical RCG006 generator freeze, terminal L0 first-order EH field-redefinition map, and terminal higher-derivative-discriminator transport.

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
- `M_ALG = 6`;
- `M_DER = 3`;
- **`M = 9`** total frozen generator directions.

## Canonical L0 first-order EH map — terminal scoped subgate

Terminal note: `results/RCG006_MFR_L0_MAP_TERMINAL.md`.
Canonical raw/provenance: `results/raw/RCG006_MFR_L0_CANONICAL.json`.
Terminal note commit: `12ca52947d1390a494634b7a6a2d98d9a7e4bf7d`.
Canonical workflow run: `35250324503`.

Classification: `PASS_SCOPED_RCG006_MFR_L0_MAP_SUBGATE`.

Exact facts:
- `M_FR` shape `8 x 9`;
- `rank(M_ALG)=5`;
- **`rank(M_FR)=7`**;
- `dim ker(M_FR)=2`;
- **`dim Q_EFT = 1`**;
- `dim(RCG004_subspace ∩ Im(M_FR)) = 5`;
- `D1D1_CLASS_9` is in `Im(M_FR)`;
- `D1D1_CLASS_11` is not in `Im(M_FR)`;
- modulo `Im(M_FR)`, `[D1D1_CLASS_11] = (3/4)[RCG004_CANONICAL_AXIS_8]`.

Canonical `M_FR` SHA256:
`7ac6ba6d1003c676899c0017409e3466a7f5e12fbb4114feee94580f1b0799bd`.

Canonical image-span SHA256:
`7c5e4b07d95881b907ed67a55742466c2889e99c20193806b834370a00f46788`.

## Canonical A_HD orbit transport — terminal scoped subgate

Terminal note: `results/RCG006_A_HD_TRANSPORT_TERMINAL.md`.
Canonical raw/provenance: `results/raw/RCG006_A_HD_TRANSPORT_CANONICAL.json`.
Terminal note commit: `344f81f90db90b2d3444222bea357221d0c54680`.
Canonical workflow run: `35250686885`, head `7af702935db7db904f08a0e70e6f8187dc61d859`.

Classification:
`PASS_SCOPED_RCG006_FIELD_REDEFINITION_DISCRIMINATOR_NONINVARIANT`.

Exact facts:
- **`rank(A_HD)=8`**;
- **`ker(A_HD)={0}`**;
- `rank(M_FR)=7`;
- **`rank(A_HD M_FR)=7`**;
- image-kernel dimension under `A_HD` is `0`;
- structural branch **`CASE_II_NONINVARIANT`**;
- quotient-aware second-order space dimension remains `0`.

Scientific meaning: the RCG005 representative-level higher-derivative discriminator is not invariant along admitted first-order local EFT field-redefinition orbits. RCG005 remains historically valid under its frozen representative convention; RCG006 prevents promoting that criterion to an EFT-class statement.

## Active authoritative gate — symbolic-Lambda companion

Workflow: `.github/workflows/rcg006-lambda-companion.yml`.
Run: `35250843261`.
Head: `56c0b6c2614f99c5cffb84bc99d2e56b45a84e05`.

At this recovery write Constructor and independent Critic are completed success, while aggregate remains non-terminal. Do not consume partial substantive values or launch a competing authoritative Lambda gate.

Purpose: track `Lambda * Q_dim4_companion` leakage separately from the L0 eight-dimensional parent and verify derivative-generator traces as bulk total divergences. It cannot change the terminal L0 `M_FR` rank.

## Independent successor identity bridge — RCG006C

Prospective preregistration: `prereg/RCG006C_UNIQUE_EFT_CLASS_WEYL_CUBED_BRIDGE.md`, commit `1122988893e9d5f87771da8a6390f031be8fafca`.

Initial run `35251277832` failed infrastructure-only before scientific output due to a SymPy zero-default factory defect. Prospective execution-only repair is recorded in `results/RCG006C_WEYL_BRIDGE_EXECUTION_ONLY_REPAIR.md`, commit `bbd99b6061d22fc638317085ba0a51adc57b9bf3`.

Repaired canonical retry: run `35251589231`, head `2051bbe0c4e0cf23343043dcd933759313a047a2`.
At this recovery write Constructor is completed success and Critic/aggregate are non-terminal. Do not consume partial workflow values. Independent debugging calculations are non-authoritative.

This bridge tests whether the already-existing one-dimensional `Q_EFT` is exactly the parity-even Weyl-cubed class; it is an identity/interpretation bridge, not new-family formation.

## Current scientific interpretation

RCG006 has canonically established that seven of the eight frozen RCG005 bulk action directions are first-order EH field-redefinition image directions, leaving a one-dimensional EFT quotient, and that the old representative-level higher-derivative discriminator is non-invariant along those redundant orbits.

Full RCG006-v0 terminal assembly still awaits the terminal symbolic-Lambda companion. RCG006C is separately non-terminal and cannot be promoted from local debugging or incomplete workflow values.

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

1. Validate and persist the terminal symbolic-Lambda companion once aggregate is terminal.
2. If valid, assemble the frozen RCG006-v0 terminal structural audit with the already-terminal L0 map and A_HD transport; do not alter generators or classifiers.
3. Independently validate the repaired RCG006C Weyl-cubed bridge only after its Critic and aggregate are terminal.
4. Only after RCG006 terminalization may a successor model-class selector be opened prospectively. No implicit quartic/additional-field/nonlocal selection is allowed.
5. `chi_ABC` remains unauthorized.
