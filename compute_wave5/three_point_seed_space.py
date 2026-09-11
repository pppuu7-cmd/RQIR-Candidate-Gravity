#!/usr/bin/env python3
import json
from pathlib import Path

OUT=Path("wave5_results"); OUT.mkdir(exist_ok=True)

# Minimal 4D massless spin-2 cubic seed catalog used as research bookkeeping.
# The standard two-derivative Einstein cubic supplies mixed-helicity 3pt seeds.
# A six-derivative curvature-cubic/R^3 interaction supplies all-plus/all-minus
# seeds while leaving the quadratic propagator unchanged.
# This is a structural catalog, not a spinor-helicity derivation.

seeds=[
 {
  "id":"EH_2DER",
  "derivative_order":2,
  "schematic_origin":"Einstein-Hilbert cubic vertex",
  "helicity_sector":"mixed helicity (++-) and (--+)",
  "changes_two_point":False,
  "belongs_to_C5_root":True,
  "requires_extra_Wilson_coefficient":False,
  "causality_UV_extra_burden":"ordinary GR tree seed"
 },
 {
  "id":"R3_6DER",
  "derivative_order":6,
  "schematic_origin":"curvature-cubic / Riemann^3-type EFT interaction",
  "helicity_sector":"all-plus / all-minus",
  "changes_two_point":False,
  "belongs_to_C5_EFT_operator_space":True,
  "requires_extra_Wilson_coefficient":True,
  "causality_UV_extra_burden":"CEMZ-type constraints apply to sizeable higher-derivative graviton 3pt corrections in weakly coupled gravity"
 }
]

summary={
 "test":"massless spin-2 cubic seed-layer bookkeeping",
 "seeds":seeds,
 "distinct_seed_classes_count":len(seeds),
 "minimal_two_derivative_seed_count":sum(1 for s in seeds if s["derivative_order"]==2),
 "higher_derivative_seed_count":sum(1 for s in seeds if s["derivative_order"]>2),
 "result":"Tree constructibility can only be unique after the cubic seed class itself is fixed. Allowing an independent R^3-type seed adds a new Wilson datum even with an unchanged propagator.",
 "scope":"structural literature-informed catalog, not a complete classification of parity-violating/nonlocal/massive cubic structures"
}
(OUT/"three_point_seed_space.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
