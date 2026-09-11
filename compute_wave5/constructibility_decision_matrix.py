#!/usr/bin/env python3
import itertools, json
from pathlib import Path

OUT=Path("wave5_results"); OUT.mkdir(exist_ok=True)

# Logic matrix separating tree constructibility from full quantum closure.
# Inputs:
# - minimal_seed: only the two-derivative Einstein spin-2 cubic seed is allowed;
# - boundary_free: recursion has no independent boundary/contact datum;
# - loop_closure: an additional principle fixes all loop/EFT counterterm data.
# The first two conditions are enough for a GR-like tree-constructibility claim
# only when supported by the external BCFW theorems. The third is intentionally
# absent from standard tree constructibility.

rows=[]
for minimal_seed,boundary_free,loop_closure in itertools.product([False,True], repeat=3):
    tree_unique=minimal_seed and boundary_free
    full_quantum_unique=tree_unique and loop_closure
    if not minimal_seed:
        blocker="independent higher-derivative three-point seed/Wilson data remain"
    elif not boundary_free:
        blocker="independent boundary/contact data remain"
    elif not loop_closure:
        blocker="tree S-matrix may be fixed, but loop/EFT counterterm data are not selected by tree constructibility"
    else:
        blocker="none in this logic proxy; actual existence/consistency of a loop-closure principle must still be proven"
    rows.append({
        "minimal_two_derivative_seed_only":minimal_seed,
        "boundary_free_recursion":boundary_free,
        "independent_loop_closure_principle":loop_closure,
        "tree_level_unique_in_proxy":tree_unique,
        "full_quantum_unique_in_proxy":full_quantum_unique,
        "remaining_blocker":blocker,
    })

summary={
 "test":"constructibility decision matrix",
 "rows":rows,
 "tree_unique_rows":sum(1 for r in rows if r["tree_level_unique_in_proxy"]),
 "full_quantum_unique_rows":sum(1 for r in rows if r["full_quantum_unique_in_proxy"]),
 "result":"Minimal seed + boundary-free recursion can isolate a tree-level GR-like S-matrix, but a separate loop/all-order principle is still required for microscopic quantum closure.",
 "scope":"logical state matrix. BCFW validity for GR is external literature authority, not proved by this script."
}
(OUT/"constructibility_decision_matrix.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
