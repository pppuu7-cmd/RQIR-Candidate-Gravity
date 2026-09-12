import json, glob
from pathlib import Path

files=glob.glob('wave25_downloads/*/*.json')
data={Path(f).stem:json.loads(Path(f).read_text()) for f in files}
required=['soft_ward','positivity','causality_uv','asymptotic_safety','double_copy','gate_matrix','information_firewall']
missing=[k for k in required if k not in data]
signals={
 'soft_ward_leaves_residual_nullity':bool(data.get('soft_ward',{}).get('soft_ward_leaves_residual_nullity',False)),
 'positivity_region_nonunique':bool(data.get('positivity',{}).get('positivity_region_nonunique',False)),
 'causality_uv_region_nonunique':bool(data.get('causality_uv',{}).get('causality_uv_region_nonunique',False)),
 'asymptotic_fixed_point_with_relevant_directions_nonunique':bool(data.get('asymptotic_safety',{}).get('asymptotic_fixed_point_with_relevant_directions_nonunique',False)),
 'double_copy_is_conditional_on_parent_choice':bool(data.get('double_copy',{}).get('double_copy_is_conditional_on_parent_choice',False)),
 'literature_gate_matrix_has_no_full_pass':bool(data.get('gate_matrix',{}).get('literature_gate_matrix_has_no_full_pass',False)),
 'no_known_principle_tested_here_earns_new_parent_law_credit':bool(data.get('gate_matrix',{}).get('no_known_principle_tested_here_earns_new_parent_law_credit',False)),
 'future_candidate_information_firewall_pass':bool(data.get('information_firewall',{}).get('future_candidate_information_firewall_pass',False))
}
all_true=not missing and all(signals.values())
summary={
 'campaign':'known-principle-tournament-wave25',
 'all_required_present':not missing,
 'missing':missing,
 'signals':signals,
 'all_predeclared_signals_true':all_true,
 'known_principle_parent_law_found':False,
 'soft_ward_residual_nullity':data.get('soft_ward',{}).get('residual_nullity'),
 'positivity_max_prediction_width':data.get('positivity',{}).get('max_prediction_width'),
 'causality_uv_prediction_diameter':data.get('causality_uv',{}).get('prediction_diameter'),
 'double_copy_parent_choice_prediction_distance':data.get('double_copy',{}).get('holdout_prediction_distance'),
 'scientific_verdict':'Wave 25 finds that none of the five preregistered established principle classes, taken alone in its declared role, passes the frozen Parent-Law Acceptance Protocol v1. Soft/Ward identities retain a residual nullspace; positivity and causality define nonunique admissible regions; asymptotic-safety fixed-point scaling remains trajectory-dependent whenever relevant directions are present; and double copy is conditional on upstream gauge-parent choice. This does not falsify any programme and does not prove that combinations or stronger microscopic realizations cannot close the residual space.',
 'next_target':'Freeze the Wave-25 certificate if all preregistered signals are true. Next test preregistered combinations of independently motivated principles for rank synergy without granting novelty twice or allowing retrofit to the frozen Wave-22 bank.'
}
Path('wave25_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True))
print(json.dumps(summary,indent=2,sort_keys=True))
if not all_true: raise SystemExit(1)
