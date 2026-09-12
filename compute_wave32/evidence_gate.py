import json, pathlib
e=json.loads(pathlib.Path('evidence/WAVE32_F1_RELEVANT_BASIS_EVIDENCE.json').read_text())
signals={
 'F1_best_truncation_dimension_is_5':len(e['best_truncation_coordinates'])==5 and len(e['best_truncation_fixed_point'])==5,
 'F1_displayed_relevant_real_dimension_is_3':e['approximation_A']['attractive_real_dimension_for_displayed_closure']==3 and e['approximation_B']['attractive_real_dimension_for_displayed_closure']==3,
 'F1_public_record_lacks_reusable_numeric_relevant_eigenbasis':not e['published_reusable_basis']['explicit_numeric_relevant_right_eigenvectors'] and not e['published_reusable_basis']['explicit_numeric_barB_matrix'] and not e['published_reusable_basis']['explicit_numeric_tildeB_matrix']
}
out={'test':'evidence_gate','coordinates':e['best_truncation_coordinates'],'fixed_point':e['best_truncation_fixed_point'],'published_reusable_basis':e['published_reusable_basis'],'signals':signals}
pathlib.Path('wave32_evidence_gate.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
