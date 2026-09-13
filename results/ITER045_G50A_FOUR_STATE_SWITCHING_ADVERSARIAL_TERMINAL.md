# Iter045 / G50-A terminal result

Date: 2026-09-13

## Frozen gate
Prospectively preregistered at `da2ed3bb190fcfc8b3e8225361b98490513630bf` before implementation and target production. Implementation `c9fb66bb69ac27d1546f083aec6c95db2033a9e7`; workflow `1e689724050b8e7e9734c21395e453fae4da8f2d`; authoritative production head `2122211ff1c08c03ca637c42b8299fd3a9fd6806`.

Exact family: the already-qualified/calibrated finite bounded stationary 20D four-state hidden-classical CTMC switching/local-sum-Hamiltonian family. Frozen target strengths `[0.025, 0.10, 0.40, 1.40]`; training times `[0.12,0.35,0.75,1.25]`; prospectively held-out times `[0.23,0.58,1.05]`; Sobol/LHS search; 32 starts, 6 refinements, 800 maximum evaluations. Scientific support required admissible candidates with both train and held-out max product-probe trace-distance gaps `>1e-4` in every lane, Sobol/LHS agreement `<=0.002` train and `<=0.003` held-out for every shard.

## Authoritative production
Run `34736777512`; aggregate job `103670129595`; summary artifact `10311238232`; digest `sha256:a2897d320cae758c6665565f6159c2fb2f50e10d8db8a738f6c622613949282a`.

All eight raw lane artifacts were consumed. All are structurally valid, admissible, provenance-valid and satisfy the frozen support rule. Raw artifacts: `10311425999` lhs shard0; `10310579970` sobol shard0; `10311670389` lhs shard1; `10311615565` sobol shard1; `10311435920` lhs shard2; `10311356180` sobol shard2; `10310862760` lhs shard3; `10311123872` sobol shard3.

Per-shard Sobol/LHS train gaps are approximately: shard0 `0.5312233384`; shard1 `0.575453150`; shard2 `0.745706013`; shard3 `0.831250`; held-out gaps are approximately `0.441038930`, `0.483684321`, `0.659779416`, `0.864186`. Largest cross-method disagreement is `3.0134559614314327e-7` train and `6.34423147127805e-7` held-out, far inside the frozen agreement thresholds.

Provenance controls remain valid in every lane. Worst raw maximum TP residual is `1.33352576428069e-15`; minimum Choi eigenvalue across best candidates is positive (`3.712713157033707e-12`); CTMC stationary and column-sum residuals are at floating-point scale.

## Scientific classification
`DERIVED_SCOPED_FOUR_STATE_CLASSICAL_SWITCHING_COMPARATOR_SUPPORT`

This closes the four-state finite-hidden-memory target-separation rubric for the exact frozen 20D comparator family and the frozen RCG-002 finite panel. It is a negative comparator result for that family, not a theorem against arbitrary classical memory, semiclassical gravity, or quantum-gravity models.

## Scope ceiling
No all-classical/no-go statement is authorized. No continuum/full-dynamics conclusion is authorized. `THEORY_ESTABLISHED` remains 0%. The next high-information layer is robustness of this exact separation under independent local basis rotations / coordinate representations, followed by a genuinely independent observable or full-dynamics/constitution gate rather than further cap escalation.