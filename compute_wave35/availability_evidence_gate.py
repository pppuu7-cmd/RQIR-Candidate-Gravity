import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
E=json.loads((ROOT/'evidence/WAVE35_PUBLIC_ORIENTATION_OBJECT_EVIDENCE.json').read_text())
src={s['id']:s for s in E['sources']}
signals={
 'F1_has_fixed_point_and_exponents_but_no_reusable_orientation_object':src['F1_2018']['best_fixed_point'] and src['F1_2018']['critical_exponents'] and not src['F1_2018']['full_or_approx_numeric_stability_matrix_publicly_reusable_in_audited_record'] and not src['F1_2018']['right_eigenvectors_publicly_reusable_in_audited_record'],
 'later_review_still_points_pure_gravity_stability_analysis_to_F1':src['FLUCTUATION_REVIEW_2023']['states_pure_gravity_stability_analysis_reference_is_F1_2018'],
 'F2_not_credited_with_F1_orientation_object':not src['F2_2024']['five_dimensional_F1_stability_matrix_or_eigenvectors'],
 'public_code_claim_boundary_is_non_exhaustive': 'not proof' in src['PUBLIC_GITHUB_QUERY']['claim_boundary'],
}
out={'test':'availability_evidence_gate','availability_verdict':E['availability_verdict_precompute'],'signals':signals}
Path('wave35_availability_evidence_gate.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
