# Wave 35 Certificate — Missing-Derivative Information Leverage

Status: **PASS / SYNTHETIC_INFORMATION_LEVERAGE_NOT_J8**
Date: 2026-09-12
Canonical GitHub Actions run: `34667039023`
Canonical head SHA: `fd840e45006e7869ce6c794dedc40e03f7ecb4a0`

## Scope

Wave 35 partitions a general 5x5 completion around the certified Wave-34 conditional 3x3 block as

`M = [[A,B],[C,D]]`,

where `B` is 3x2 (6 entries), `C` is 2x3 (6 entries), and `D` is 2x2 (4 entries). Thus the Wave-34 block leaves exactly 16 derivatives unspecified.

All ensembles are synthetic and prior-dependent. No result in this certificate is a physical estimate of an FRG derivative or a physical ranking of derivative importance.

## Result

All 8 primary jobs and the aggregator passed. All 14 predeclared signals are true.

Each missing block class carries nonzero information about the full five-dimensional relevant-subspace orientation under the declared ensemble. Varying `B`, `C`, or `D` while keeping `A` fixed produces inequivalent five-dimensional relevant subspaces and/or topology changes.

For the full `BCD` ensemble, the median maximum principal angles relative to the baseline completion are:

- scale 0.05: `0.024288467635021998 rad`,
- scale 0.10: `0.047875162075600775 rad`,
- scale 0.20: `0.09833750578377835 rad`,
- scale 0.40: `0.2025236879742146 rad`.

The median orientation uncertainty is nondecreasing with perturbation scale within the frozen `0.01 rad` Monte-Carlo tolerance.

## External physical-input contract

Physical J8 requires either a same-realization numerical 5x5 stability matrix or an equivalent normalized right-eigensystem, accompanied by:

1. the same-closure fixed point;
2. ordered coordinates `(mu, lambda3, lambda4, g3, g4)`;
3. closure and vertex-identification assumptions;
4. projection and regulator provenance;
5. derivative / finite-difference provenance;
6. numerical precision and tolerances.

Critical exponents alone do not satisfy this contract.

## Scientific verdict

Wave 35 demonstrates why the 16 derivatives outside the Wave-34 3x3 block are not optional bookkeeping: they contain orientation information required by the physical displaced-trajectory problem. The synthetic leverage study does not determine their values. The blocker therefore remains an external same-realization five-dimensional orientation object.

Current blocker:

`BLOCKED_FULL_5D_SAME_REALIZATION_STABILITY_MATRIX_OR_RIGHT_EIGENSYSTEM_STILL_REQUIRED`.
