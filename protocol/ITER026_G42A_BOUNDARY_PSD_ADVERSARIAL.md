# Iter026 / G42-A — boundary-capable arbitrary-orientation PSD adversarial gate

Status: **PREREGISTERED BEFORE TARGET PRODUCTION**.

## Preconditions

G42-C2 and G42-C3 must both be terminal scientific PASS. This protocol is authorized by their frozen joint lock only after consuming their terminal aggregates.

- G42-C2 run `34710953936`: `PSD_BOUNDARY_OPTIMIZER_CALIBRATED`.
- G42-C3 run `34711048394`: `PSD_BOUNDARY_RANK_COMPLETION_CALIBRATED`.

## Question

Can the same frozen boundary-capable bounded real-PSD 6x6 classical random-Hamiltonian Kossakowski family, now calibrated across effective ranks 1–6, reproduce the four frozen RCG-002 toy trajectories used by the prior comparator campaign?

This is a finite two-qubit, multi-time/product-probe comparator test. It is not a theorem about all classical mediators, all LOCC/separable dynamics, arbitrary non-Markovian channels, or continuum gravity.

## Frozen comparator coordinates

Use exactly the G42-C2/C3 map `C = B B^T` with lower-triangular real `B`:

- diagonal coordinates: `[0, 0.60]`;
- off-diagonal coordinates: `[-0.30, 0.30]`;
- all 21 lower-triangular coordinates are optimized;
- rank-deficient PSD boundary is therefore included exactly.

The chart is bounded. A PASS/FAIL applies only to this bounded chart and must never be restated as an unbounded full-PSD no-go.

## Frozen targets and observables

Use the same four RCG-002 target shards as G41-A: `theta = scale * t0` from the frozen `CASES` object, with unitary `exp(-i theta t Z⊗Z)`.

Use exactly:

- times `[0.15, 0.45, 0.9, 1.4]`;
- the six frozen product probes used in G42 calibration;
- scientific metric = maximum trace distance over all time×probe outputs;
- smooth residual vector over real+imaginary output differences is optimizer surrogate only.

## Frozen search

Two independently constructed start designs:

- `sobol_lsq`;
- `lhs_lsq`.

For each method×target shard:

- 32 starts in the same 21-D bounds;
- retain top 6 by squared smooth residual;
- bounded least-squares refinement, `max_nfev=1000`;
- final candidate is selected by smallest scientific trace-distance gap, then residual norm.

Adversarial start seeds are fixed independently of the positive controls and target values. No hidden comparator coordinates exist or are inserted.

## Frozen admissibility

For the selected candidate require:

- all coordinates/results finite;
- `C` minimum eigenvalue `>= -1e-10`;
- max trace-preservation residual `< 1e-10`;
- minimum Choi eigenvalue across frozen times `> -1e-8`;
- minimum output-state eigenvalue across frozen time×probe outputs `> -1e-8`;
- max output trace error `< 1e-10`.

## Frozen scientific rule

Per target shard:

1. both Sobol and LHS lanes must be structurally/admissibly valid;
2. each best scientific gap must be `> 1e-4`;
3. absolute Sobol/LHS gap difference must be `<= 0.002`.

All four shards must satisfy all three clauses for scoped support.

Terminal classification:

- `DERIVED_SCOPED_BOUNDARY_PSD_COMPARATOR_SUPPORT` iff all four shards pass;
- otherwise `G42A_FROZEN_SUPPORT_RULE_NOT_MET` (or structural/numerical invalid classification if applicable).

No threshold, bound, target, probe, time, start count, or optimizer rule may be changed after production results are viewed.

## Interpretation ceiling

Even a PASS means only that the tested RCG-002 toy trajectories retained a nonzero calibrated gap against this bounded Markovian real-PSD classical random-Hamiltonian semigroup family. It does **not** establish new physics, full quantum gravity, a universal classical-mediator no-go, or superiority over arbitrary quantum/non-Markovian comparator families.
