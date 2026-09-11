#!/usr/bin/env python3
import json
from pathlib import Path

root=Path("wave5_downloads")
items={}
for p in root.rglob("*.json"):
    try: items[p.stem]=json.loads(p.read_text(encoding="utf-8"))
    except Exception as e: items[p.stem]={"parse_error":str(e)}
required={"boundary_contact_constructibility","loop_counterterm_power_count","three_point_seed_space","constructibility_decision_matrix"}
missing=sorted(required-set(items)); sig={}
if "boundary_contact_constructibility" in items:
    d=items["boundary_contact_constructibility"]
    sig["boundary_free_condition_removes_proxy_contact_data"]=d.get("D24_contact_directions",0)>0 and d.get("records",[])[-1].get("directions_surviving_generic_boundary_free_condition",1)==0
if "loop_counterterm_power_count" in items:
    sig["tree_constructibility_not_loop_closure"]=len(items["loop_counterterm_power_count"].get("records",[]))>=3
if "three_point_seed_space" in items:
    d=items["three_point_seed_space"]
    sig["higher_derivative_cubic_seed_is_independent_datum"]=d.get("higher_derivative_seed_count",0)>0
if "constructibility_decision_matrix" in items:
    d=items["constructibility_decision_matrix"]
    sig["minimal_seed_plus_boundary_free_can_isolate_tree_but_not_full_quantum_without_loop_rule"]=d.get("tree_unique_rows",0)>d.get("full_quantum_unique_rows",0)>0
summary={"campaign":"post-freeze-constructibility-wave5","missing":missing,"signals":sig,"all_required_present":not missing,"external_authority":"GR BCFW/constructibility and two-loop counterterm facts are literature inputs; scripts only formalize residual-data logic and power counting","scope":"constructibility closure map, not a proof of UV quantum gravity"}
Path("wave5_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
if missing: raise SystemExit(2)
