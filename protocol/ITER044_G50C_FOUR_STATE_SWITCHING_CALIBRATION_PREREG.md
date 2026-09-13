# Iter044 / G50-C — Four-state hidden-classical switching optimizer calibration

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION**
Date: 2026-09-13
Prerequisite: terminal Iter043/G50-P `FOUR_STATE_CLASSICAL_SWITCHING_PROVENANCE_MEMORY_QUALIFIED`.

## Purpose
Response-blind numerical calibration of a finite 20-parameter four-state stationary hidden-classical CTMC switching family among local-sum Hamiltonians. This gate tests whether the chosen optimizer/search budget can recover synthetic in-family channels before any RCG-002 adversarial transport.

## Frozen parameterization
- 12 independent positive off-diagonal CTMC rates for 4 hidden states, bounds `[0.015, 0.14]`;
- 4 fixed normalized local-field directions on subsystem A and 4 fixed normalized local-field directions on subsystem B;
- one positive scalar field magnitude per A direction and per B direction: 8 scales total, bounds `[0.55, 1.45]`;
- total dimension: 20;
- stationary hidden initialization;
- conditional Hamiltonians are exactly local sums.

Synthetic hidden controls are deterministic, response-blind interior points generated from fixed seeds and are never used as optimizer starts.

## Frozen numerical design
Methods: `sobol_lsq`, `lhs_lsq`.
Controls: `0,1,2,3`.
Training times: `(0.12,0.35,0.75,1.25)`.
Holdout times: `(0.23,0.58,1.05)`.
Product probes: same 16 local product states as G50-P.
Starts per lane: 32.
Refined starts per lane: 6.
Maximum least-squares evaluations per refinement: 800.

A lane passes only if the best candidate simultaneously satisfies:
- provenance/physical admissibility controls inherited from G50-P;
- training max probe trace-distance gap `< 0.002`;
- holdout max probe trace-distance gap `< 0.003`;
- normalized parameter error `< 0.10`.

Aggregate requires all 8 lanes (2 methods × 4 controls) structurally valid and passing, and for each control the two methods' training gaps differ by `<=0.002`.

Frozen terminal classifications:
- `FOUR_STATE_CLASSICAL_SWITCHING_OPTIMIZER_CALIBRATED` if aggregate rule passes;
- `G50C_FROZEN_CALIBRATION_RULE_NOT_MET` if structurally valid but support rule fails;
- implementation/numerical invalid if frozen predicates cannot be validly evaluated.

## Interpretation lock
PASS is calibration only. It authorizes a separately prospectively frozen RCG-002 adversarial transport against this exact 20D four-state family. It is not target separation and not a universal classical-memory/no-go theorem.

Programme readiness remains 63% on calibration PASS; readiness can change only if a later scientific comparator/separation rubric closes.