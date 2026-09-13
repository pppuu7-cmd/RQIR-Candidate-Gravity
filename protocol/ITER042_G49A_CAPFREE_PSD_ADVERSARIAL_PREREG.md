# Iter042 / G49-A — preregistration: cap-free/direct-PSD RCG-002 transport

Status: **FROZEN BEFORE IMPLEMENTATION / PRODUCTION**.

Prerequisite: terminal G49-C run `34726705385` classified `CAPFREE_DIRECT_PSD_OPTIMIZER_CALIBRATED` with 12/12 response-blind lanes passing, including numerical-box inactivity.

## Scientific question

Does the already-calibrated direct real-PSD Markovian comparator retain a prospectively nonzero nearest-comparator gap on the unchanged four-shard RCG-002 toy trajectory panel when the physical trace cap is removed from the parameterization, while the purely numerical coordinate box remains demonstrably inactive?

## Frozen comparator family

- `A` is a real symmetric `6x6` matrix represented by the same 21 Frobenius-weighted physical-scale coordinates used by G49-C.
- `C=A^2`, spanning the real PSD Kossakowski cone.
- There is **no physical trace cap**.
- Numerical optimization only: each weighted coordinate is bounded to `[-8,8]` exactly as in G49-C.
- A lane is admissible only if its selected candidate satisfies numerical-box inactivity `max(abs(w_i))/8 < 0.80`.

No complex-PSD extension, hidden-memory extension, target-dependent ansatz, fitted witness, or family retuning is permitted.

## Frozen target and production matrix

Use exactly the RCG-002 target convention, four shards, `TIMES`, `PROBES`, trajectory metric, state/channel physicality conventions and `GAP_THRESHOLD=1e-4` inherited from the already-established G44-A/G46-A/G48-A comparator chain. No target or witness changes are permitted.

- methods: `{sobol_lsq,lhs_lsq}`
- shards: `{0,1,2,3}`
- total lanes: `8`
- `fail-fast:false`
- safe parallelism: up to `8`
- starts per lane: `32`
- refine best: `6`
- `max_nfev=1200`
- direct coordinate numerical box: `[-8,8]^21`

Starts are response-blind deterministic Sobol/LHS designs with shard/method-specific fixed seeds. They may depend on shard identity only through the preregistered RNG seed, never through inspected production outcomes.

## Frozen lane validity / support

A lane is structurally valid only if all expected candidates and diagnostics are finite.

A selected best candidate is admissible only if:

- `min_eig(C) >= -1e-10`;
- `max TP residual < 1e-10`;
- `min Choi eigenvalue > -1e-8`;
- `min output-state eigenvalue > -1e-8`;
- `max trace error < 1e-10`;
- numerical-box inactivity `max(abs(w_i))/8 < 0.80`.

`lane_support=true` requires admissibility and best trajectory gap strictly greater than the inherited frozen `GAP_THRESHOLD=1e-4`.

## Frozen aggregate rules

1. Exactly `8/8` lanes structurally valid.
2. For every shard, both Sobol and LHS lanes must be admissible and satisfy the nonzero-gap rule.
3. For every shard, absolute Sobol/LHS best-gap difference must be `<=0.002`.
4. Direct-PSD consistency with the terminal cap64 parent family must hold prospectively: for each shard, the best direct-PSD gap must satisfy `best_gap(direct, shard) <= best_gap(cap64_terminal, shard) + 0.002`.
5. Frozen terminal cap64 minima are:
   - shard0 `0.03700796699310312`
   - shard1 `0.14632813080599644`
   - shard2 `0.5275494895483135`
   - shard3 `0.6663863350263319`
6. No threshold/family/target/witness/optimizer changes after production output is inspected.

## Frozen classifications

- structural/numerical invalidity: `G49A_IMPLEMENTATION_OR_NUMERICAL_INVALID`
- structurally valid but any admissibility/support/agreement/consistency rule fails: `G49A_FROZEN_SUPPORT_RULE_NOT_MET`
- all frozen rules pass: `DERIVED_SCOPED_CAPFREE_DIRECT_PSD_COMPARATOR_SUPPORT`

## Interpretation lock

Even a full PASS is only scoped numerical evidence that the frozen four-shard RCG-002 toy target retains a nonzero nearest-comparator gap in this calibrated direct real-PSD parameterization, with inactive numerical coordinate bounds and cross-method/finite-parent controls. It is **not** a proof of the mathematical global infimum over the unbounded PSD cone, not a universal classical or semiclassical no-go theorem, not experimental confirmation, and not a gravity-theory constitution result.

Readiness does not automatically increase because this gate deepens the already-counted comparator-rubric dimension. Theory established remains `0%`.
