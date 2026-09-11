#!/usr/bin/env python3
import json
from pathlib import Path

root=Path("wave4_downloads")
items={}
for p in root.rglob("*.json"):
    try: items[p.stem]=json.loads(p.read_text(encoding="utf-8"))
    except Exception as e: items[p.stem]={"parse_error":str(e)}
required={"cemz_scale_proxy","quadratic_curvature_state_cost","soft_contact_nullspace","higher_point_only_family"}
missing=sorted(required-set(items)); sig={}
if "quadratic_curvature_state_cost" in items:
    sig["no_extra_local_DOF_selects_EH_point_in_scanned_metric_quadratic_basis"]=bool(items["quadratic_curvature_state_cost"].get("unique_no_extra_point_on_grid"))
if "soft_contact_nullspace" in items:
    sample=items["soft_contact_nullspace"].get("sample_D24",[])
    sig["finite_soft_order_leaves_higher_contact_nullspace"]=all(r.get("residual_contact_nullspace",0)>0 for r in sample if r.get("soft_constraints_through_degree",99)<24)
if "higher_point_only_family" in items:
    sig["GR_two_point_does_not_close_higher_point_local_family"]=items["higher_point_only_family"].get("at_N12_minimum_free_coefficients",0)>0
if "cemz_scale_proxy" in items:
    sig["higher_derivative_cubic_has_finite_onset_scale"]=len(items["cemz_scale_proxy"].get("rows",[]))>0
summary={"campaign":"post-freeze-higher-point-wave4","missing":missing,"signals":sig,"all_required_present":not missing,"external_theory_dependency":"CEMZ causality constraint is literature input; wave computes only dimensional onset scaling","scope":"higher-point cost/underconstraint filters; not a UV-completion theorem"}
Path("wave4_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
if missing: raise SystemExit(2)
