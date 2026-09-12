# Iter040 / G48-A — preregistration

Status: **FROZEN BEFORE IMPLEMENTATION / PRODUCTION**

Prerequisite: terminal G48-C run `34721391489` classified `CAP32_CAP64_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED`.

## Scientific object

Transport the already-calibrated, basis-invariant real-PSD Markovian random-Hamiltonian trace-ball comparator to finite caps `tr(C)<=32` and `tr(C)<=64` against the unchanged four-shard RCG-002 toy trajectory panel used by G44-A/G46-A. This is an extension of a bounded comparator family, not an unbounded limit.

## Frozen matrix

- trace caps: `{32,64}`
- methods: `{sobol_lsq,lhs_lsq}`
- shards: `{0,1,2,3}`
- total production lanes: `16`
- `fail-fast:false`; safe parallelism up to 8

## Frozen implementation inheritance

Use the same mathematical family, target convention, probes/times, optimizer hyperparameters, admissibility checks and search-coordinate construction as terminal G46-A, with only the trace-cap set changed from `{8,16}` to `{32,64}`. No target-dependent retuning is permitted.

## Frozen lane rule

Each lane is valid only if structural checks are finite and the recovered comparator is admissible under the unchanged G46-A PSD/trace-preservation/CP/output-state/trace thresholds. `lane_support=true` requires admissibility and best trace-distance gap strictly above the unchanged `GAP_THRESHOLD` imported from the calibrated comparator protocol.

## Frozen aggregate rules

1. Exactly 16 structurally valid lanes.
2. For each `(cap, shard)`, both Sobol and LHS lanes must be admissible and support the nonzero-gap rule.
3. For each `(cap, shard)`, absolute Sobol/LHS best-gap difference must be `<=0.002`.
4. Finite-family nesting must hold prospectively:
   - `best_gap(cap32, shard) <= best_gap(cap16, shard) + 0.002`;
   - `best_gap(cap64, shard) <= best_gap(cap32, shard) + 0.002`.
   Terminal cap16 minima are frozen as:
   - shard0 `0.03700797230755979`
   - shard1 `0.14632856595800156`
   - shard2 `0.5275496176970684`
   - shard3 `0.6663860056257985`
5. No threshold/family/witness/target changes after production output is inspected.

## Frozen classifications

- structural/numerical invalidity: `G48A_IMPLEMENTATION_OR_NUMERICAL_INVALID`
- structurally valid but any support/agreement/nesting rule fails: `G48A_FROZEN_SUPPORT_RULE_NOT_MET`
- all frozen rules pass: `DERIVED_SCOPED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP32_CAP64`

## Interpretation lock

Even a full PASS means only that the frozen four-shard toy target retains a nonzero nearest-comparator gap inside the tested bounded real-PSD Markovian trace balls through caps 32/64, with non-retuned cross-method and nesting controls. It does **not** authorize an unbounded-PSD theorem, a universal classical/semiclassical no-go, experimental confirmation, or a gravity-theory constitution claim. Readiness does not automatically increase because this deepens an already-counted comparator-rubric dimension.