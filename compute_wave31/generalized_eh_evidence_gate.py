import json, pathlib
e=json.loads(pathlib.Path('evidence/WAVE31_GENERALIZED_EH_EVIDENCE.json').read_text())
f=e['published_generalized_EH_facts']
signals={
 'F2_generalized_EH_not_frozen_as_two_independent_residual_coefficients':not f['explicit_two_independent_generalized_EH_residual_coefficients_after_GR_baseline_subtraction'],
 'IR_UV_consistency_does_not_define_unique_two_direction_projection':(set(f['Rcal_constraints_in_paper'])=={'IR consistency','UV consistency'} and not f['unique_published_generalized_EH_low_energy_coefficient_map'])
}
out={'test':'generalized_eh_evidence_gate','published_generalized_EH_facts':f,'signals':signals}
pathlib.Path('wave31_generalized_eh_evidence_gate.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
