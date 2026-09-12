# ITER021D / G39-A-N launch

Prospectively frozen purpose: diagnose the terminal Iter021C G39-A rank3-vs-rank2 nesting violation without changing the comparator family, target, parameter bounds, optimizer tolerances, nonzero-gap threshold, agreement threshold, or nesting slack.

Frozen object: exact legal rank-2 optimum embedded into rank 3 by copying the first 14 unit-cube coordinates and setting the third mode rate exactly to zero. The remaining third-mode axis/coupling coordinates are irrelevant at zero rate.

Frozen checks for each of 2 methods x 4 shards:
1. embedded rank-3 gap and residual reproduce the retained rank-2 optimum within 1e-10;
2. rank-3 least-squares refinement started from that legal embedded point is not worse than the embedded point by more than 1e-10;
3. all values finite.

Interpretation frozen before results:
- all lanes PASS => original G39-A nesting violation is OPTIMIZER/NUMERICAL SEARCH MISS; original G39-A cannot be promoted to scientific support until a prospectively repaired adversarial search is rerun;
- exact embedding failure => IMPLEMENTATION/NESTING FAIL; stop G39 scientific interpretation and repair implementation only;
- no threshold or family weakening is permitted post hoc.
