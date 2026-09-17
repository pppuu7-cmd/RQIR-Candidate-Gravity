# RQIR-Candidate-Gravity current front

Updated: 2026-09-17 after terminal RCG006 L0 map, terminal A_HD transport, terminal symbolic-Lambda companion, discovery/launch of the preregistered RCG006B held-out closure obligation, and repaired RCG006C identity bridge.

## Canonical programme/scientific phase

`RCG002_HISTORICAL_SCIENCE_TERMINAL / RCG003B_AXISYMMETRIC_FAIL / RCG004_COMPLETE_ALGEBRAIC_CUBIC_CLASS_TERMINAL_FAIL / RCG005_COMPLETE_LOCAL_DIM6_PURE_METRIC_CLASS_TERMINAL_FAIL / RCG006_FIELD_REDEFINITION_EQUIVALENCE_AUDIT_ACTIVE_HELDOUT_PENDING`

Historical RCG002/RCG003/RCG003B/RCG004/RCG005 terminals remain unchanged.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.

## RCG005 parent authority retained

Terminal: `results/RCG005_COMPLETE_LOCAL_DIM6_PURE_METRIC_CURVATURE_TERMINAL.md`.
Commit: `aef9882924ffd128c6c30934e4f95394aae874fc`.
Classification: `FAIL_SCOPED_RCG005_COMPLETE_LOCAL_DIM6_PURE_METRIC_CLASS_HAS_NO_NONZERO_SECOND_ORDER_SURVIVOR` under the frozen representative-level convention.

RCG006 qualifies EFT interpretation but does not rewrite this historical result.

## RCG006 frozen contract

Scientific preregistration: `fc3ff1f49c56f2befc039e09ebd8f388833dbff1`.
Generator freeze: `8c8314d2b857d6caa9719d6ba33e856ea0a697af`.
Map contract: `78789e048ab3d67fc8f2e901176ff3a352aad749`.
Held-out preregistration: `43748579a78f40e0825d5ae01dc634d55ba7b928`.

Scope: first-order local perturbatively invertible parity-even pure-metric **bulk action** field redefinitions. Boundary observables, matter couplings, global solution spaces, causal structures, quantum measures and nonperturbative equivalence are out of scope.

## Generator space — terminal

`M_ALG=6`, `M_DER=3`, **`M=9`**.

## L0 first-order EH map — terminal

Terminal note: `results/RCG006_MFR_L0_MAP_TERMINAL.md`, commit `12ca52947d1390a494634b7a6a2d98d9a7e4bf7d`.
Run: `35250324503`.
Classification: `PASS_SCOPED_RCG006_MFR_L0_MAP_SUBGATE`.

Exact facts:
- `M_FR` is `8 x 9`;
- `rank(M_ALG)=5`;
- **`rank(M_FR)=7`**;
- `dim ker(M_FR)=2`;
- **`dim Q_EFT=1`**;
- `dim(RCG004 ∩ Im(M_FR))=5`;
- `[D1D1_CLASS_11]=(3/4)[RCG004_CANONICAL_AXIS_8]` modulo the image.

Map SHA256: `7ac6ba6d1003c676899c0017409e3466a7f5e12fbb4114feee94580f1b0799bd`.
Image-span SHA256: `7c5e4b07d95881b907ed67a55742466c2889e99c20193806b834370a00f46788`.

## A_HD orbit transport — terminal

Terminal note: `results/RCG006_A_HD_TRANSPORT_TERMINAL.md`, commit `344f81f90db90b2d3444222bea357221d0c54680`.
Run: `35250686885`.
Classification: `PASS_SCOPED_RCG006_FIELD_REDEFINITION_DISCRIMINATOR_NONINVARIANT`.

Exact facts:
- **`rank(A_HD)=8`**, `ker(A_HD)={0}`;
- **`rank(A_HD M_FR)=7`**;
- image-kernel dimension `0`;
- structural branch **`CASE_II_NONINVARIANT`**;
- quotient-aware second-order space remains zero.

Meaning: the RCG005 representative-level higher-derivative discriminator is not invariant along admitted first-order EFT-redundant field-redefinition orbits.

## Symbolic-Lambda companion — terminal

Terminal note: `results/RCG006_SYMBOLIC_LAMBDA_COMPANION_TERMINAL.md`, commit `a067bca23fd01bc002afe3e66e8164549986aee8`.
Canonical raw: `results/raw/RCG006_SYMBOLIC_LAMBDA_CANONICAL.json`, commit `6c3a2aa362ffec237e55db7a767b06d7afdb88b2`.
Run: `35250843261`.
Classification: `PASS_SCOPED_RCG006_SYMBOLIC_LAMBDA_BULK_COMPANION`.

Exact facts:
- `dim Q_dim4_companion=2`;
- `rank(Lambda leakage_ALG)=2`;
- `rank(Lambda leakage_FULL)=2`;
- all DER traces are zero in the bulk companion and remain boundary-sensitive total divergences.

This does not alter the L0 `rank(M_FR)=7` result.

## Active mandatory closure gate — RCG006B exact held-out

Held-out preregistration: `prereg/RCG006B_GENERIC_METRIC_JET_FIELD_REDEFINITION_HELDOUT.md`, commit `43748579a78f40e0825d5ae01dc634d55ba7b928`.
Execution contract: `prereg/RCG006B_HELDOUT_EXECUTION_CONTRACT.md`, commit `da1d1795a6ecf885a7f52a717d4979d962002240`.
Workflow: `.github/workflows/rcg006b-heldout.yml`.
Run: `35252660085`, head `55d2ddfe5d84a4e56857c9b7fd12719ca5e9dc43`.

At this recovery write Constructor and independent Critic are executing. Do not consume partial values and do not duplicate the gate.

Frozen banks:
- Constructor seed `0x5243473030364341`, 32 exact-rational samples;
- Critic seed `0x5243473030364352`, 32 samples;
- final cross-route seed `0x524347303036484f`, 16 samples.

This gate is a validation layer only; finite sampling is not a universal identity proof. It must validate frozen generator tensors, raw EH images and final quotient map with exact equality and no refit.

**Full RCG006-v0 terminalization is forbidden until RCG006B is terminal.**

## Independent identity bridge — RCG006C Weyl-cubed

Prospective preregistration: `1122988893e9d5f87771da8a6390f031be8fafca`.

Initial run failed before science on a SymPy zero-default factory; repair recorded at `bbd99b6061d22fc638317085ba0a51adc57b9bf3`.
Second run `35251589231` produced successful Constructor/Critic jobs but aggregate failed infrastructure-only because `sympy` was missing from the aggregate environment. Aggregate-only repair is recorded at `a8a7826fe570bb6a83ab1233314607b5fefc553c`.

Current repaired retry: run `35252716318`, head `6ac996aaf2201d659e4afc0d43a2242f74fbc069`.
Do not use partial values before terminal aggregate.

The bridge tests whether the already-existing one-dimensional `Q_EFT` is exactly the parity-even Weyl-cubed class. It is an operator-identity bridge, not candidate-theory formation.

Canonical quotient relation lock: `[D1D1_CLASS_11]=(3/4)[axis8]`; therefore if Weyl-cubed spans `[axis8]`, then `[Weyl^3]=(4/3)[D1D1_CLASS_11]`, not the inverse.

## Claim locks

No `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `THEORY_ESTABLISHED`, GR uniqueness, arbitrary modified-gravity no-go, boundary/matter/nonperturbative equivalence or `chi_ABC` computation.

## Next admissible action

1. Finish RCG006B; if INVALID, repair only implementation defects allowed by the frozen contract or qualify RCG006 accordingly. If PASS, persist held-out authority.
2. Then assemble the full RCG006-v0 terminal structural audit from generator + L0 map + A_HD + Lambda + held-out authorities.
3. Independently terminalize RCG006C only after its repaired aggregate is terminal.
4. Only after RCG006 terminalization open a **new prospective successor model-class selector**; do not automatically promote Weyl-cubed or choose quartic/additional-field/nonlocal classes post hoc.
5. `chi_ABC` remains unauthorized.
