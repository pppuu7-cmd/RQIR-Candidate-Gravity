import json, pathlib, sys
required=['f2_operator_basis','wave22_sector_visibility','anti_overcounting_rank','low_energy_truncation_rank','r3_gap','projection_identifiability','information_firewall']
files={name:pathlib.Path(f'wave29_downloads/wave29-{name}/wave29_{name}.json') for name in required}
missing=[name for name,p in files.items() if not p.exists()]
if missing:
    print(json.dumps({'missing':missing},indent=2)); sys.exit(2)
data={name:json.loads(p.read_text()) for name,p in files.items()}
signals={}
for d in data.values(): signals.update(d.get('signals',{}))
expected=[
'f2_quadratic_curvature_operator_rank_is_2',
'wave22_sector_visibility_matches_frozen_bank',
'multiple_npoint_rows_do_not_raise_rank_above_latent_rank',
'three_and_four_point_inputs_do_not_imply_four_independent_residual_directions',
'constants_only_quadratic_rank_le_2',
'constants_plus_first_slopes_rank_le_4_before_generalized_EH',
'p6_R3_sector_not_available_in_F2_reconstruction',
'F2_to_wave22_six_coordinate_projection_nonunique_without_extra_map',
'central_f2_information_does_not_close_frozen_six_direction_parent_law',
'information_firewall_pass']
all_true=all(signals.get(k) is True for k in expected)
summary={
'campaign':'f2-central-projection-wave29',
'all_required_present':not missing,
'all_predeclared_signals_true':all_true,
'signals':{k:signals.get(k,False) for k in expected},
'f2_quadratic_operator_rank':data['f2_operator_basis']['rank'],
'constants_only_rank_upper_bound':2,
'constant_plus_first_slope_rank_upper_bound':4,
'full_wave22_dimension':6,
'projection_example_image_ranks':data['projection_identifiability']['probe_image_rank'],
'blocking_object':'BLOCKED_F2_CENTRAL_ACTION_HAS_CORRELATED_LOW_RANK_BASIS_AND_NO_EXPLICIT_SIX_COORDINATE_PROJECTION_PLUS_WAVE28_UV_DERIVATIVE_ENSEMBLE_STILL_MISSING',
'scientific_verdict':'Wave 29 finds that the published F2 central effective action is a strong reusable same-action object but does not license six independent RQIR residual coordinates. TT three- and four-point p^4 information jointly reconstructs two quadratic-curvature form factors; under a first-slope low-energy truncation the quadratic sector carries at most four latent coefficients before any separately justified generalized-EH residual degree of freedom. The frozen F2 scope omits p^6/R^3 reconstruction, and no explicit F2-to-Wave22 six-coordinate projection is supplied. Multiple observable rows therefore cannot be counted as independent theory parameters. This is an identifiability/rank result, not a failure of F2 or asymptotic safety.',
'next_target':'Freeze Wave-29 certificate if clean. Then Wave 30 should derive the maximal same-lineage central projection that can be fixed from F2 low-energy coefficients and frozen 2pt/3pt/4pt incidence, while explicitly quotienting baseline/generalized-EH freedom; separately keep the Wave-28 requirement for displaced UV trajectories.'
}
pathlib.Path('wave29_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True))
print(json.dumps(summary,indent=2,sort_keys=True))
if not all_true: sys.exit(3)
