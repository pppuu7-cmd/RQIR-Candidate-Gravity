import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
E=json.loads((ROOT/'evidence/WAVE35_PUBLIC_ORIENTATION_OBJECT_EVIDENCE.json').read_text())
R=E['fresh_recompute_minimum']
required=[
 'fixed_point_coordinates','stability_matrix_shape','relevant_real_dimension_expected_for_F1_best_displayed_closure',
 'symmetric_trajectory_count_per_orientation_object','J8_output_dimension','J8_jacobian_shape',
 'J9_requires_approximation_regulator_truncation_variants','right_eigenvectors_must_be_saved','raw_beta_derivative_or_matrix_provenance_must_be_saved'
]
signals={
 'fresh_recompute_contract_complete':all(k in R for k in required),
 'matrix_shape_is_5x5':R['stability_matrix_shape']==[5,5],
 'relevant_real_dimension_is_3':R['relevant_real_dimension_expected_for_F1_best_displayed_closure']==3,
 'symmetric_trajectory_authority_is_7':R['symmetric_trajectory_count_per_orientation_object']==7,
 'J8_shape_is_6x3':R['J8_jacobian_shape']==[6,3],
 'provenance_and_uncertainty_metadata_are_mandatory':R['J9_requires_approximation_regulator_truncation_variants'] and R['raw_beta_derivative_or_matrix_provenance_must_be_saved'],
}
out={'test':'fresh_recompute_contract','required_fields':required,'signals':signals}
Path('wave35_fresh_recompute_contract.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
