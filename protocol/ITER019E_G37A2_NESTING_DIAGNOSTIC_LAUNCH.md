# ITER019E / G37-A2-N — frozen nesting diagnostic

Launch after terminal G37-A2 showed a nesting violation on shard 2 despite the corrected G37-C2 family claiming an exact shared-noise boundary.

Frozen before diagnostic results:
- family, target, optimizer bounds and all prior science thresholds are unchanged;
- reproduce the G36 shared-parent search under each original Sobol/LHS method and shard;
- map the retained shared-parent optimum exactly into the 19D G37-C2 chart with `lambda_MF=0`;
- require exact embedded gap agreement within `1e-10`;
- refine from that legal boundary seed using the existing G37-C2 residual and bounds and require it not to worsen by more than `1e-10`.

Interpretation:
- PASS => observed G37-A2 shared-parent nesting violation is an optimizer/search miss. A separate prospectively repaired adversarial rerun with legal parent-boundary seeds is then authorized.
- FAIL of exact embedding => implementation/nesting failure; stop scientific interpretation and repair implementation only.

This diagnostic cannot establish an RCG-002 nonzero-gap result by itself and cannot change any frozen threshold post hoc.
