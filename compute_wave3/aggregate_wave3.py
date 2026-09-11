#!/usr/bin/env python3
import json
from pathlib import Path

root=Path("wave3_downloads")
items={}
for p in root.rglob("*.json"):
    try:
        items[p.stem]=json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        items[p.stem]={"parse_error":str(e)}
required={"spectral_purity_two_point","nonlocal_uv_softening_vs_positive_spectrum","time_symmetric_prescription_support","higher_point_visibility"}
missing=sorted(required-set(items))
sig={}
if "spectral_purity_two_point" in items:
    d=items["spectral_purity_two_point"]
    sig["spectral_purity_fixes_two_point_to_GR"]=bool(d.get("does_spectral_purity_fix_two_point_to_GR"))
    sig["spectral_purity_does_not_fix_higher_points"]=not bool(d.get("does_it_fix_interactions_or_higher_points",True))
if "nonlocal_uv_softening_vs_positive_spectrum" in items:
    sig["exponential_UV_softening_conflicts_with_positive_extra_spectrum_same_GR_residue"]=not items["nonlocal_uv_softening_vs_positive_spectrum"].get("positive_spectral_representation_possible_under_assumptions",True)
if "time_symmetric_prescription_support" in items:
    d=items["time_symmetric_prescription_support"]
    sig["time_symmetric_prescription_has_negative_time_support"]=d.get("symmetric_negative_time_L2_fraction",0)>0.45
    sig["retarded_prescription_negative_time_support_zero"]=d.get("retarded_negative_time_L2_fraction",1)<1e-12
if "higher_point_visibility" in items:
    recs=items["higher_point_visibility"].get("records",[])
    cubic=next((r for r in recs if r.get("curvature_power")==3),{})
    sig["curvature_cubic_changes_higher_points_not_two_point"]=cubic.get("minimum_h_order")==3 and not cubic.get("affects_two_point_quadratic_action",True)
summary={"campaign":"post-freeze-escape-route-wave3","missing":missing,"signals":sig,"all_required_present":not missing,"scope":"two-point spectral/prescription/higher-point escape-route filters; not a UV-completion theorem"}
Path("wave3_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
if missing:
    raise SystemExit(2)
