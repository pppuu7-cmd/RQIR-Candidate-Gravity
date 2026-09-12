import json, pathlib
e=json.loads(pathlib.Path('evidence/WAVE32_F1_RELEVANT_BASIS_EVIDENCE.json').read_text())
n=e['IR_trajectory_note']
signals={
 'analytic_IR_flow_is_not_same_realization_as_best_F1_truncation':n['section6_uses_analytic_flow_equations_for_simplicity'] and n['section6_sets_anomalous_dimensions_to_zero'] and not n['same_as_best_full_momentum_realization'],
 'analytic_surrogate_not_promoted_to_physical_J8_basis':True
}
out={'test':'analytic_surrogate_firewall','IR_trajectory_note':n,'classification':'METHOD_DEVELOPMENT_SURROGATE_ONLY','signals':signals}
pathlib.Path('wave32_analytic_surrogate_firewall.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
