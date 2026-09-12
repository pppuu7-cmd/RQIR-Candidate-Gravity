import json, pathlib, sys
required=['linear_curvature_bulk_quotient','generalized_eh_evidence_gate','anti_double_counting','endpoint_identifiability','counterfactual_rank6','p6_exclusion','information_firewall']
files={n:pathlib.Path(f'wave31_downloads/wave31-{n}/wave31_{n}.json') for n in required}
missing=[n for n,p in files.items() if not p.exists()]
if missing:
    print(json.dumps({'missing':missing},indent=2)); sys.exit(2)
data={n:json.loads(p.read_text()) for n,p in files.items()}
signals={}
for d in data.values(): signals.update(d.get('signals',{}))
expected=[
'linear_curvature_positive_laplacian_powers_are_boundary_terms_under_declared_conditions',
'linear_curvature_analytic_bulk_residual_rank_after_EH_quotient_is_0',
'F2_generalized_EH_not_frozen_as_two_independent_residual_coefficients',
'IR_UV_consistency_does_not_define_unique_two_direction_projection',
'quadratic_form_factor_directions_not_recounted_as_generalized_EH',
'endpoint_constraints_allow_inequivalent_residual_embeddings',
'functional_freedom_without_projection_does_not_establish_finite_rank_closure',
'two_transverse_extra_columns_can_close_rank6_mathematically',
'counterfactual_closure_does_not_count_as_F2_physical_evidence',
'p6_R3_not_used_to_rescue_generalized_EH_rank',
'information_firewall_pass']
all_true=all(signals.get(k) is True for k in expected)
summary={
 'campaign':'generalized-eh-wave31',
 'all_required_present':not missing,
 'all_predeclared_signals_true':all_true,
 'signals':{k:signals.get(k,False) for k in expected},
 'linear_curvature_bulk_residual_rank_after_EH_quotient':data['linear_curvature_bulk_quotient']['bulk_residual_rank_after_EH_quotient'],
 'endpoint_diagnostic_rank':data['endpoint_identifiability']['moment_matrix_rank'],
 'counterfactual_two_extra_full_rank_fraction':data['counterfactual_rank6']['full_rank_fraction'],
 'blocking_object':'BLOCKED_NO_TWO_INDEPENDENT_PUBLISHED_GENERALIZED_EH_BULK_RESIDUAL_DIRECTIONS_AFTER_GR_BASELINE_QUOTIENT',
 'scientific_verdict':'Wave 31 finds no frozen basis for crediting the published F2 generalized-EH sector with the two additional independent bulk residual directions required by Wave 30. For an analytic momentum-dependent coefficient multiplying a single curvature scalar, positive Laplacian powers integrate to boundary terms under the declared conditions; after quotienting the classical EH normalization, this linear-curvature bulk local sector contributes zero new finite residual directions. Genuinely nonlinear Rcal(Delta,R) can be nontrivial, but the frozen F2 record constrains it by IR/UV consistency rather than providing a unique two-direction low-energy residual projection. Endpoint constraints admit inequivalent interior embeddings. Arbitrarily adding two transverse columns can close rank six mathematically, but that is counterfactual and receives no physical F2 credit. Quadratic form-factor directions and p6/R3 are not double-counted or imported.',
 'route_decision':'PARK_F2_CENTRAL_PROJECTION_CLOSURE_AND_RETURN_TO_WAVE28_UV_DISPLACED_TRAJECTORY_OBJECT',
 'next_target':'Freeze Wave-31 certificate if clean. Then Wave 32 should return to the Wave-28 J8 front and audit reconstructibility of the F1 relevant-direction basis from published beta-function/stability data, including whether a partial same-lineage eigenbasis can be recovered without inventing missing higher-coupling flow derivatives.'
}
pathlib.Path('wave31_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)); print(json.dumps(summary,indent=2,sort_keys=True))
if not all_true: sys.exit(3)
