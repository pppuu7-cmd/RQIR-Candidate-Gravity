#!/usr/bin/env python3
import json
from pathlib import Path

root=Path("wave2_downloads")
items={}
for p in root.rglob("*.json"):
    try:
        items[p.stem]=json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        items[p.stem]={"parse_error":str(e)}

required={"spin2_positive_spectral","ward_transverse_form_factors","causal_retarded_shape","local_q4_tt_poles"}
missing=sorted(required-set(items))
sig={}

if "spin2_positive_spectral" in items:
    d=items["spin2_positive_spectral"]
    sig["positive_TT_spectrum_finite_data_nonunique"]=any(not r.get("unique",True) for r in d.get("records",[]))
    sig["finite_Q_TT_shape_nonunique_after_low_energy_fix"]=any(r.get("width",0)>1e-10 for r in d.get("finite_Q_after_two_low_energy_coefficients",[]))
if "ward_transverse_form_factors" in items:
    d=items["ward_transverse_form_factors"]
    sig["Ward_projectors_numerically_transverse"]=d.get("projector_Ward_max_abs_error",1)>0 and d.get("projector_Ward_max_abs_error",1)<1e-10
    sig["Ward_leaves_regular_form_factor_freedom"]=any(r.get("free_after_Ward_and_low_order_fixes",0)>0 for r in d.get("regular_form_factor_counting",[]) if r.get("fixed_regular_orders_each_sector",0)>=2)
if "causal_retarded_shape" in items:
    d=items["causal_retarded_shape"]
    sig["causal_low_frequency_data_leave_finite_frequency_shape_freedom"]=not d.get("all_finite_frequency_parts_unique",True)
if "local_q4_tt_poles" in items:
    d=items["local_q4_tt_poles"]
    sig["simple_local_q4_TT_has_no_healthy_nonzero_coefficient_in_scan"]=not d.get("healthy_nonzero_a_found",True)

summary={
 "campaign":"post-freeze-gravity-specific-wave2",
 "missing":missing,
 "signals":sig,
 "all_required_present":not missing,
 "scope":"gravity-specific finite/analytic filters, not a UV-complete quantum-gravity theorem",
}
Path("wave2_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
if missing:
    raise SystemExit(2)
