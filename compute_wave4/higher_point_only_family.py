#!/usr/bin/env python3
import json
from pathlib import Path

OUT=Path("wave4_results"); OUT.mkdir(exist_ok=True)

# Minimal layer-counting proxy after imposing an exactly GR-like quadratic action.
# Curvature starts O(h), so an R^n-type local invariant starts at O(h^n).
# We allocate only one schematic coefficient per curvature power n; the real EFT
# has more tensor contractions, so this is a strict UNDER-count of higher-point
# freedom, useful only to show that fixing the propagator does not close dynamics.

records=[]
for N in range(3,13):
    layers=[]
    for n in range(3,N+1):
        layers.append({"curvature_power":n,"first_h_order":n,"derivative_order":2*n,"changes_quadratic_action":False})
    records.append({"max_curvature_power":N,"minimum_schematic_free_coefficients":len(layers),"layers":layers})

summary={
 "test":"minimum higher-point-only local curvature family after GR two-point is fixed",
 "records":records,
 "at_N12_minimum_free_coefficients":records[-1]["minimum_schematic_free_coefficients"],
 "result":"Even after all quadratic/two-point modifications are removed, local curvature-cubic and higher interactions form a growing higher-point family. One coefficient per curvature power is only a lower bound on actual tensor-operator freedom.",
 "scope":"schematic lower-bound layer count, not an independent-operator Hilbert-series calculation"
}
(OUT/"higher_point_only_family.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
