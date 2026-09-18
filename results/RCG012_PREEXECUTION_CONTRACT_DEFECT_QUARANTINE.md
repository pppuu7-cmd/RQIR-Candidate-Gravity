# RCG012 pre-execution contract defect and quarantine

Date: 2026-09-19

Status: **PRE-EXECUTION INVALIDATION / NO SCIENTIFIC RESULT**

Frozen gate under review:
`RCG012_MINIMAL_EXPLICIT_NEW_MODEL_CONTENT_BASIS_PREOUTCOME_GATE`

Prereg:
`db72a4cb44177a7a35063050b023bfb49ee01a01`

Launch head:
`4d9411e8234985a8e0123578dcee42bf607fd53d`

Canonical queued run:
`35405271943`

At defect discovery:
- workflow status: `queued`;
- Constructor: queued;
- Critic: queued;
- no job steps;
- no artifacts;
- therefore no substantive RCG012 value had been observed.

## Defect

The frozen RCG012 prereg defines only three purportedly independent blocks:

- S = source constitution;
- Q = state/measure/preparation;
- G = quantitative generator,

and its PASS branch requires that no fourth independent block be needed.

However the already-authoritative
`docs/RQIRCG_MODEL_DEFINITION_SLOT_GRAPH.md`
explicitly records five logically distinct model-definition slots:

1. `CLASSICAL LAW`;
2. `SOURCE / PREPARATION CONSTITUTION`;
3. `QUANTUM STATE / MEASURE / BOUNDARY`;
4. `QUANTUM LAW / ON-SHELL MATCHING`;
5. `OPERATIONAL OBSERVABLE / READOUT`.

The graph states:

`The five slots are logically distinct even when one mathematical package relates them`

and:

`No PASS in one slot grants automatic PASS in another.`

It further records the critical lock:

`STATE_MEASURE_SELECTION != QUANTUM_LAW_MATCHING_SELECTION`.

Promotion minimum explicitly includes all five compatible slots.

## Why this invalidates the RCG012 PASS branch

RCG012 silently places multiple already-distinct obligations inside G.

In particular:
- classical-law content is not separately audited;
- quantum-law/on-shell-matching content is not separately audited from Q;
- operational-map/readout content is not represented as an independent downstream obligation.

Therefore a synthetic S+Q+G object can pass the RCG012 classifier merely because G is declared exact, while still hiding several model-definition slots that the durable graph forbids collapsing by label.

The frozen statement

`no fourth independent block is required by the frozen contract`

is therefore not established by the authority set actually frozen into the gate.

This is a **pre-execution contract/classifier defect**, not a scientific FAIL and not evidence against any physical principle.

## Static Critic correction

The earlier static Critic verdict

`WELL_POSED_FOR_MINIMAL_EXPLICIT_CONTENT_BASIS_EXECUTION`

is withdrawn for this gate because its C6 fourth-block challenge considered only causal/order/normalization and failed to audit the authoritative five-slot non-collapse rule.

## Quarantine

Run `35405271943` is quarantined prospectively before execution.

If GitHub later executes it, all produced RCG012 Constructor/Critic/Aggregate/Auditor outputs are **NONAUTHORITATIVE_FOR_SCIENCE** because the frozen classifier can certify a basis that is too coarse relative to prior durable authority.

Do not rerun or repair this exact gate in place.

## Classification

`INVALID_RCG012_PREEXECUTION_CONTRACT_COLLAPSES_DISTINCT_MODEL_DEFINITION_SLOTS`

Mapped to frozen invalid taxonomy:

`INVALID_RCG012_IMPLEMENTATION_OR_PROVENANCE`.

No scientific RCG012 PASS/BLOCKED result exists.

## Locks

Unchanged:
- `A=span{alpha}`;
- selector rank `0`;
- residual dimension `1`;
- parent principle undefined;
- parent functional undefined;
- source object undefined;
- no value derivation;
- no bridge;
- no alpha sensitivity;
- `alpha=UNSELECTED`;
- `chi_ABC=UNAUTHORIZED_NOT_COMPUTED`;
- `THEORY_ESTABLISHED=0%`.

## Authorized replacement direction

Open a **new prospectively frozen repair gate**, not an execution-only retry.

The replacement must first project the authoritative five-slot graph onto the parent-principle target and explicitly prove which slots are:
- required at parent-principle definition time;
- downstream-only for physical observable/promotion;
- non-collapsible.

Only after that projection is terminal may a minimal basis theorem be attempted.
