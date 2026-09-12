# Iter038 / G46-A — terminal result

Date: 2026-09-13 (research cycle)

## Frozen authority

Protocol: `protocol/ITER038_G46A_EXTENDED_TRACE_BALL_ADVERSARIAL.md`.
Frozen object: basis-invariant real-symmetric PSD Kossakowski comparator `C=A^2`, `A=A^T`, with trace caps 8 and 16; two independent QMC initializations (`sobol_lsq`, `lhs_lsq`); four unchanged RCG-002 toy target shards; 32 starts, best 6 refined, max 1200 evaluations.

Frozen requirements: every lane admissible with maximum trace-distance gap `>1e-4`; Sobol/LHS pair disagreement `<=0.002`; cap nesting `best(cap16) <= best(cap8)+0.002` for every shard.

## Provenance

- launch/head commit: `a2dd7fd3cf3b40f642077c62bd1c0020a97d12bb`
- run: `34719458597`
- aggregate job: `103623455694`
- aggregate artifact: `10304948789` (`rcg038-g46a-summary`)
- artifact digest: `sha256:187128fcab86e209f622f8e1eabd13dc8630d5361c2a9ccc44eb40ccb905e263`

## Raw aggregate

All `16/16` lane artifacts are structurally valid. All eight cap/shard Sobol-LHS pairs satisfy the frozen agreement rule and all four cap-nesting checks pass.

Pair best-gap values:

- cap8 s0: `0.03700797329872096 / 0.03700798184215059`, diff `8.543429630414323e-09`
- cap8 s1: `0.14632857027196491 / 0.14632861118932036`, diff `4.09173554483111e-08`
- cap8 s2: `0.527549433168062 / 0.5275636202752797`, diff `1.4187107217678019e-05`
- cap8 s3: `0.6663864390506281 / 0.6663867399862362`, diff `3.009356080996284e-07`
- cap16 s0: `0.03700797230755979 / 0.037008002442549655`, diff `3.0134989864594175e-08`
- cap16 s1: `0.14632856595800156 / 0.14632859530390996`, diff `2.9345908397759857e-08`
- cap16 s2: `0.5275496176970684 / 0.5275496633213744`, diff `4.562430599985845e-08`
- cap16 s3: `0.6663860056257985 / 0.6663867566742838`, diff `7.510484852923938e-07`

Cap nesting passes on all four shards. Cap16 does not materially reduce the best gap relative to cap8 on this frozen grid.

## Scientific classification

`DERIVED_SCOPED_EXTENDED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP8_CAP16`

This is a DERIVED scoped comparator result for finite bounded real-PSD Markovian random-Hamiltonian trace balls through `tr(C)<=16`. It is not an unbounded-PSD theorem, not a no-go against arbitrary classical memory/semiclassical gravity, and not a gravity-theory constitution result.

Because G44-A already earned the bounded Markovian PSD rubric point, G46-A deepens that same rubric dimension and does **not** raise programme readiness beyond 63%.

## Next authorized gate

Before any cap32/cap64 adversarial production, run a response-blind optimizer calibration at caps 32 and 64 with the same rank-1..6 hidden controls, Sobol/LHS methods, recovery/rank/PSD thresholds and no RCG-002 target access. Only terminal calibration PASS may authorize a prospectively frozen cap32/cap64 adversarial transport.
