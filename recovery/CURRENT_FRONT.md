# RQIR-Candidate-Gravity current front

Updated: 2026-09-14
Phase: `G97_CLOSED_TOTAL_SOURCE_PREPARATION_PASS / NCP1_POSITIVITY_RESTRICTIONS_TERMINAL / NP1_CONNECTED_EXTENSION_UNDERDETERMINATION_TERMINAL / CM1_CLOSED_MEDIATOR_NONUNIQUENESS_TERMINAL / VB1_CURRENT_VERSION_MODEL_DEFINITION_BOUNDARY_TERMINAL / V2P1_NO_PREOUTCOME_PRINCIPLE_SELECTED_TERMINAL / RSC1_INTERFACE_PACKAGE_NOT_CLOSED_TERMINAL / RSC_SSE1_SOURCE_STRESS_PREREQUISITE_BLOCKED_TERMINAL / RSC_CLOSED_SOURCE_ACTION_PROPOSAL_PREOUTCOME_FRONTIER`

## Canonical status

- Active seed lineage: `RCG-002 Relational controlled-phase channel`.
- Current frozen version: `RCG002_CURRENT_VERSION_NONLINEAR_DYNAMICS_UNDERDETERMINED`.
- Programme label: `CURRENT_VERSION_TERMINAL_AT_NONLINEAR_MODEL_DEFINITION_BOUNDARY`.
- RSC status: `NEAR_SURVIVOR_NOT_SELECTED`.
- Latest source-side classification: `BLOCKED_MISSING_CLOSED_SOURCE_ACTION_OR_EQUIVALENCE_PRINCIPLE`.
- Programme readiness: **66%**; theory established: **0%**. These are bookkeeping labels, not probabilities.
- Physical selector rank: `UNDEFINED_PHYSICAL_MAP_MISSING`.
- Physical nonlinear completion space: **UNDEFINED**.
- Latest clean-ledger addendum: `research_log/RQIRCG_RESEARCH_LEDGER_RSC_SSE1_ADDENDUM.md`.
- Scientific authority: newest `main`, this recovery file, dedicated clean-ledger addenda, terminal notes, and validated Actions artifacts.
- Independence lock remains active: no QGR/MSQGR/CRQN/KMQGB/RQIR/ISQGR candidate dynamics or preferred coefficients may be imported as RCG-002 selectors.

## Latest terminal — RSC-SSE1 source/stress equivalence prerequisite

Final classification:

`BLOCKED_MISSING_CLOSED_SOURCE_ACTION_OR_EQUIVALENCE_PRINCIPLE`.

Route A:

`BLOCKED_MISSING_CLOSED_SOURCE_ACTION_AND_CARRIER_SELF_SOURCE_RULE`.

Route B:

`BLOCKED_NO_PROVEN_CARRIER_READOUT_INVARIANT_STRESS_QUOTIENT`.

Authority:
- preregistration `46f6ae2b8ea3263ed081980783ed6221b7d52639`, `prereg/RCG002_RSC_SSE1_SOURCE_STRESS_EQUIVALENCE_PREREG.md`;
- terminal `05d81080dbde205a609ce392bd73b38edf2900d0`, `results/RCG002_RSC_SSE1_SOURCE_STRESS_EQUIVALENCE_TERMINAL.md`;
- clean-ledger addendum `0f54fe3accf49ed140d3496277d343d3060e4616`.

No `chi_ABC`, connected phase/noise, novelty observable or connected coefficient was computed or used.

### Exact Route-B certificate

For the RSC1 conserved improvement

`delta T^{mu nu}=(partial^mu partial^nu-eta^{mu nu}Box)F`

and the linearized source-carrier coupling

`I_int[h,T]=(1/2) Integral d^4x h_{mu nu}T^{mu nu}`,

boundary-controlled integration by parts gives exactly

`delta I_int=(1/2) Integral d^4x F R1[h]`,

where

`R1[h]=partial_mu partial_nu h^{mu nu}-Box h`.

`R1[h]` is invariant under the inherited linearized gauge transformation on the flat background. Therefore the coupling variation is not merely a linearized coordinate gauge mode.

The variation is not identically zero. For the explicit static compact-support control

`h_{mu nu}=eta_{mu nu}H`, `F=H`,

one has `R1=-3 nabla^2 H` and a nonzero coupling proportional to

`Integral dt d^3x |grad H|^2`

for nonconstant `H`.

Thus equality of integrated charges plus local conservation is insufficient to declare the whole conserved-improvement family physically equivalent. A physical quotient would have to define allowed transformations and prove invariance of the complete nonlinear carrier + preparation + operational readout.

### Route-A audit

A sufficient canonical-source construction would require a complete same-realization closed-system action/source constitution for probe + apparatus/support + binding/holding/control degrees of freedom, with local stress derived from that object and the nonlinear carrier self-source derived compatibly.

Current authority does not contain such an action/rule:
- G97 gives closed classical mechanical force/impulse bookkeeping and total momentum, not a covariant local matter+apparatus/support action;
- baseline v0 takes an abstract symmetric conserved `T_{mu nu}` as input and has no nonlinear carrier self-stress/action;
- RSC states a self-coupling principle but does not supply the exact same-realization closed source action or carrier self-source law.

Importing standard GR/Einstein-Hilbert nonlinear dynamics, a preferred pseudotensor, or another candidate's action as the selector remains forbidden. Standard theory may be used only as an explicit comparator/background where authorized.

### Scientific meaning

RSC1 showed that global closure does not fix local stress. SSE1 now proves that the obvious source-equivalence rescue also does not follow from charge equality: conserved improvements can change the actual source-carrier coupling.

The source blocker is therefore localized to a genuine model-defining object:

**a prospectively specified closed-system source/action constitution, or a proven carrier/readout-invariant source equivalence quotient.**

This is BLOCKED rather than FAIL because no fully specified RSC source principle has yet been contradicted.

## Retained RSC1 terminal

RSC1 remains `RSC_INTERFACE_PACKAGE_NOT_CLOSED_PREOUTCOME` with two independent blockers:

1. `BLOCKED_SOURCE_STRESS_INTERFACE_MISSING_DATUM`;
2. `BLOCKED_POSITIVE_INFLUENCE_INTERFACE_MISSING_DATUM`.

Its exact positive-kernel certificate remains authoritative: deterministic coherent carrier phases do not uniquely determine a normalized positive influence/noise completion.

The quantum state/measure/influence blocker remains independently open after all SSE1 source-side work.

## Retained V2P1 / VB1 / earlier terminals

V2P1 remains `NO_PREOUTCOME_PRINCIPLE_SELECTED`; no new version is authorized.

VB1 remains `RCG002_CURRENT_VERSION_NONLINEAR_DYNAMICS_UNDERDETERMINED`.

CM1 remains `NONUNIQUENESS_SURVIVES_CLOSED_SEQUENTIAL_MEDIATOR_SCOPED`, run `34861269613`.

NP1 remains `RCG002_CURRENT_PRINCIPLES_ALLOW_CONTINUUM_CONNECTED_CHANNEL_EXTENSIONS_SCOPED`, run `34816931926`.

NCP1 remains `FAIL_HIGHER_ORDER_ONLY_NOISE_RESCUE_SCOPED`, `FAIL_EXACT_GAUSSIAN_CUBIC_LOG_KERNEL_SCOPED`, `POSITIVE_NOISY_COMPLETIONS_NONUNIQUE_SCOPED`, overall `BLOCKED_PHYSICAL_EVOLUTION`, run `34792497014`.

G97 remains `PASS_CLOSED_TOTAL_SOURCE_PREPARATION_CONSERVATION_SCOPED`, run `34791265992`; it is closed classical source-preparation bookkeeping, not a local nonlinear stress/Bianchi/influence theory.

## Automation infrastructure incident

Operational note: `ops/RQIRCG_AUTOMATION_RUNTIME_INCIDENT_2026-09-14.md`, commit `5309a4b246692947cac4b6e1e82be1e6214d0154`.

This note has **no scientific authority**.

Observed scheduled-run metadata across RQIRCG and other long research automations showed a repeated approximately 63–67 second run-to-disable interval, with no corresponding post-CM1 RQIRCG GitHub Actions failure and no durable commit from the failed automation turns. Best-supported diagnosis: scheduled execution budget/runtime timeout or equivalent platform cap, not scientific failure.

Control-only repair: RQIRCG Constructor and Auditor prompts were shortened to bounded micro-iterations, broad historical rescans were removed, early durable handoff was prioritized, and both recurring automations were re-enabled. Scientific criteria and claim locks were unchanged. Confirmation requires future scheduled runs to remain enabled and leave bounded durable progress.

## Physical nonlinear completion space

**Undefined.**

RSC/SSE1 control functions and earlier NP1/CM1 coordinates are not automatically physical gravitational completion coordinates. Do not infer a physical dimension or selector rank from them.

## Exact next admissible fundamental gate

**`RSC_CLOSED_SOURCE_ACTION_PROPOSAL_PREOUTCOME_GATE`.**

This gate must remain before all connected outcomes. It may not select an action because it yields a convenient `chi_ABC` or other desired phase.

The gate should ask whether RCG-002's own relational/operational commitments independently motivate one minimal closed-system source/action constitution that specifies, in the same realization:

1. probe matter degrees of freedom;
2. apparatus/support/control/binding degrees of freedom required by G97 closure;
3. branch/history preparation;
4. source/action domain and symmetry;
5. local symmetric conserved total stress or equivalent source object;
6. carrier nonlinear self-source/action rule;
7. constraint/conservation propagation route;
8. exact weak-field reduction to the validated baseline;
9. no imported external-candidate dynamics and no free connected coefficient/function.

If no such package can be independently motivated without arbitrary new model data, record the source-side RSC proposal as still blocked; do not rescue it phenomenologically.

Even after a source-side PASS, the independent RSC quantum state/measure/influence gate remains mandatory before any connected prediction.

## Open layers and locks

Still open: closed source/action constitution; carrier nonlinear self-source; nonlinear constraint/Bianchi propagation in one realization; quantum state/measure/influence law; spacetime causality; physical completion quotient; external/comparator discrimination; externally anchored prediction.

Forbidden claims remain `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, established nonlinear RCG-002/RSC, universal classical/semiclassical/noisy no-go, family-wide uniqueness, green-CI-as-physics, post-hoc source selection or post-hoc connected coefficient selection.

Historical G72-G97/CPI1/NCP1/NP1/CM1/VB1/V2P1/RSC1 results and duplicate-G93 quarantine remain intact.
