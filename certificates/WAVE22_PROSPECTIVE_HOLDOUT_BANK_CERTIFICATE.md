# Wave 22 Prospective Holdout Bank Certificate

**Status:** FROZEN CANDIDATE-BLIND FINITE-PROXY EXAM  
**Authoritative corrected commit:** `9009bb7e68e083cc819ebf0a3d6b6a111950e456`  
**Authoritative Actions run:** `34661882499`

## Preregistered result

All required artifacts were present and all preregistered primary signals passed:

- full 12-probe pool rank = 6;
- selected 10-probe bank rank = 6;
- selected condition number = `5.249949491713074` <= 8;
- after profiling independent 2pt/3pt/4pt normalization nuisances, signal rank remains 6;
- profiled minimum singular value = `0.19974483383518615` >= 0.15;
- 1000 seeded 2% sensitivity-perturbation trials: full-rank fraction = `1.0` >= 0.99;
- fifth percentile profiled minimum singular value = `0.193224078910377` >= 0.15;
- 2pt-only data do not identify all four `[c3,d3,e4,f4]` higher-order directions, while the selected cross-order bank does;
- preregistered synthetic residual classes are separated; minimum pairwise L2 distance = `0.13468715343342882`;
- future-candidate information firewall passes;
- sector coverage and IR-residual-vanishing diagnostics pass.

## Frozen selected probes

1. `P2_q0.65`
2. `P0_q0.35`
3. `P0_q0.75`
4. `V3_x0.5_h-1`
5. `V3_x0.7_h1`
6. `V3_x0.9_h-1`
7. `A4_s0.25_t0.15_h1`
8. `A4_s0.4_t0.2_h-1`
9. `A4_s0.55_t0.25_h1`
10. `A4_s0.7_t0.3_h-1`

The exact rows are frozen separately in `holdouts/WAVE22_FROZEN_BANK.json`.

## Scientific meaning

This is a candidate-blind finite-proxy discriminator over six declared RQIR residual directions `[c3,d3,e4,f4,s2,s0]`. It is suitable for prospective testing of a future frozen polygon-derived QGR candidate without re-selecting probes after seeing its predictions.

It is **not** an experimental sensitivity forecast and does not prove that six directions span every possible quantum-gravity deformation.

## Correction provenance

Initial run `34661797111` exposed an infrastructure-only JSON serialization bug: multidimensional NumPy arrays were sent through `.item()` before ndarray handling. No scientific matrix, probe, selection rule, seed, perturbation level or threshold changed. Commit `9009bb7e...` only reversed serializer dispatch order. Corrected run `34661882499` is authoritative.
