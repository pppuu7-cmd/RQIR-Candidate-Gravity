# ITER023A / G40-D — preregistered RTN witness/basis-fragility diagnostic

Purpose: diagnose the terminal G40-A failure without retroactively changing or promoting G40-A.

Frozen before results:
- same finite 8-parameter hidden-classical RTN family, bounds, target trajectories, four shards, Sobol/LHS designs, 16 starts, top-4 LSQ refinement, times/probes and `max_nfev=600` as G40-A;
- no G40-A threshold or result is changed;
- evaluate every refined candidate against a fixed four-element witness panel formed by conjugating the original G40 BLP pair by `I⊗I`, `H⊗H`, `(S H)⊗(S H)`, `(H S)⊗(H S)`;
- BLP diagnostic threshold remains `>0.02` for every panel member;
- report fixed-witness BLP, panel maximum BLP, witness attaining the maximum, candidate gap, and whether a candidate excluded by the original witness becomes panel-admissible;
- separately report the best panel-admissible gap for each method/shard and the Sobol/LHS difference when both exist.

Interpretation rule:
- `FIXED_WITNESS_FRAGILE_ON_PANEL` if at least one candidate has original BLP `<=0.02` but panel max `>0.02`;
- `NO_PANEL_ESCAPE_FOUND` if no such candidate exists in the frozen refined candidate set;
- `MIXED` is allowed across shards.

This is a diagnostic only. It cannot convert terminal G40-A into PASS, cannot support an all-BLP/all-classical claim, and cannot authorize threshold/witness retuning. Any later rotation-covariant scientific gate must be separately calibrated and preregistered before use on RCG-002.
