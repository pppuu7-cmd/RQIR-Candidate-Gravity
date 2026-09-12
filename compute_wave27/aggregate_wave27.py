import json,glob
from pathlib import Path
files=glob.glob('wave27_downloads/*/*.json')
data={Path(f).stem:json.loads(Path(f).read_text()) for f in files}
required=['lineage_completeness','anti_splice','jacobian_gate','c3_bridge','vertex_lineage','lorentzian_lineage','integrity_firewall']
missing=[k for k in required if k not in data]
signals={
 'no_single_published_lineage_closes_J0_J9':bool(data.get('lineage_completeness',{}).get('no_single_published_lineage_closes_J0_J9',False)),
 'cross_lineage_union_cannot_substitute_same_realization_chain':bool(data.get('anti_splice',{}).get('cross_lineage_union_cannot_substitute_same_realization_chain',False)),
 'explicit_six_direction_jacobian_missing':bool(data.get('jacobian_gate',{}).get('explicit_six_direction_jacobian_missing',False)),
 'propagated_six_direction_uncertainty_missing':bool(data.get('jacobian_gate',{}).get('propagated_six_direction_uncertainty_missing',False)),
 'C3_partial_UV_to_IR_bridge_exists':bool(data.get('c3_bridge',{}).get('C3_partial_UV_to_IR_bridge_exists',False)),
 'C3_sign_robust_but_magnitude_scheme_sensitive':bool(data.get('c3_bridge',{}).get('C3_sign_robust_but_magnitude_scheme_sensitive',False)),
 'full_momentum_vertices_exist_but_UV_to_RQIR_sensitivity_map_missing':bool(data.get('vertex_lineage',{}).get('full_momentum_vertices_exist_but_UV_to_RQIR_sensitivity_map_missing',False)),
 'lorentzian_quadratic_bridge_exists_but_higher_point_closure_missing':bool(data.get('lorentzian_lineage',{}).get('lorentzian_quadratic_bridge_exists_but_higher_point_closure_missing',False)),
 'integrity_firewall_pass':bool(data.get('integrity_firewall',{}).get('integrity_firewall_pass',False))
}
all_true=(not missing) and all(signals.values())
summary={
 'campaign':'asymptotic-safety-lineage-wave27',
 'all_required_present':not missing,
 'missing':missing,
 'signals':signals,
 'all_predeclared_scientific_signals_true':(not missing) and all(v for k,v in signals.items() if k!='integrity_firewall_pass'),
 'all_signals_including_integrity_true':all_true,
 'max_same_lineage_supported_nodes':data.get('lineage_completeness',{}).get('max_same_lineage_supported_count'),
 'lineage_rows':data.get('lineage_completeness',{}).get('lineages'),
 'cross_lineage_union_missing':data.get('anti_splice',{}).get('cross_lineage_union_missing'),
 'C3_reported_magnitude_ratio':data.get('c3_bridge',{}).get('magnitude_ratio_between_reported_regulator_treatments'),
 'blocking_object':'BLOCKED_MISSING_SAME_REALIZATION_UV_TO_RQIR_SIX_DIRECTION_JACOBIAN_WITH_PROPAGATED_UNCERTAINTY',
 'scientific_verdict':'Wave 27 recognizes substantial asymptotic-safety progress while locating the remaining proof obligation. The strongest fluctuation-vertex lineage supplies UV/IR and physical-limit 2/3/4-point/effective-action ingredients through J7, the Lorentzian lineage supplies a strong two-point/quadratic bridge, and the essential C3 lineage supplies a genuine fixed-point/eigendirection/separatrix-to-one-Wilson-coefficient bridge. Nevertheless no frozen public lineage supplies J8, an explicit same-realization sensitivity/Jacobian from independent UV trajectory coordinates to all six RQIR residual directions, nor J9, propagated six-output uncertainty. Cross-lineage splicing is disallowed. Therefore PL1 remains blocked on a narrowly specified missing object rather than on a generic lack of asymptotic-safety predictions.',
 'next_target':'Freeze the Wave-27 certificate if clean. Then build a derivation contract for the missing Jacobian and test whether the fluctuation-vertex lineage can expose sufficient numerical vertex/trajectory data to construct it without importing another truncation. In parallel compare only the frozen blocker label with KMQGB metadata.'
}
Path('wave27_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True))
print(json.dumps(summary,indent=2,sort_keys=True))
if not all_true: raise SystemExit(1)
