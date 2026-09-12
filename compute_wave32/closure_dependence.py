import json, pathlib
e=json.loads(pathlib.Path('evidence/WAVE32_F1_RELEVANT_BASIS_EVIDENCE.json').read_text())
f=e['full_stability_object']; c=e['closure_dependence']
signals={
 'full_stability_matrix_blocked_by_unknown_higher_coupling_flows':(not f['paper_statement_full_matrix_access']) and f['finite_truncation_still_requires_closure'],
 'closure_choice_changes_relevant_dimension_in_one_approximation':c['across_identification_schemes_tildeB_attractive_dimension'].startswith('1 or 3')
}
out={'test':'closure_dependence','full_stability_object':f,'closure_dependence':c,'signals':signals}
pathlib.Path('wave32_closure_dependence.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
