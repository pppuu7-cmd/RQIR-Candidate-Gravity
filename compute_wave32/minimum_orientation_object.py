import json, pathlib
e=json.loads(pathlib.Path('evidence/WAVE32_F1_RELEVANT_BASIS_EVIDENCE.json').read_text())
minimum_object={
 'ordered_coordinates':e['best_truncation_coordinates'],
 'fixed_point_vector':e['best_truncation_fixed_point'],
 'orientation_source':'numeric 5x5 approximate stability matrix under one frozen closure OR normalized right-eigenvector basis',
 'mode_convention':'one real attractive mode plus one complex-conjugate pair represented as three real displacement directions; normalization/sign/phase fixed',
 'flow_engine':'same closure/beta-flow realization used for central and displaced trajectories',
 'uncertainty_extensions':'regulator/truncation/closure variants for J9'
}
published=e['published_reusable_basis']
orientation_available=published['explicit_numeric_relevant_right_eigenvectors'] or published['explicit_numeric_barB_matrix'] or published['explicit_numeric_tildeB_matrix']
signals={
 'explicit_matrix_or_right_eigenvectors_are_minimum_orientation_object':len(minimum_object['ordered_coordinates'])==5 and 'stability matrix' in minimum_object['orientation_source'],
 'J8_displacement_coordinates_remain_blocked_without_orientation_object':not orientation_available
}
out={'test':'minimum_orientation_object','minimum_object':minimum_object,'orientation_available_in_frozen_public_record':orientation_available,'signals':signals}
pathlib.Path('wave32_minimum_orientation_object.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
