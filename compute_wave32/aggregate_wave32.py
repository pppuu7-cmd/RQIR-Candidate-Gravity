import json, pathlib, sys
required=['evidence_gate','spectrum_orientation_nonidentifiability','approximation_spectra_ambiguity','closure_dependence','analytic_surrogate_firewall','minimum_orientation_object','information_firewall']
files={n:pathlib.Path(f'wave32_downloads/wave32-{n}/wave32_{n}.json') for n in required}
missing=[n for n,p in files.items() if not p.exists()]
if missing:
    print(json.dumps({'missing':missing},indent=2)); sys.exit(2)
data={n:json.loads(p.read_text()) for n,p in files.items()}
signals={}
for d in data.values(): signals.update(d.get('signals',{}))
expected=['F1_best_truncation_dimension_is_5','F1_displayed_relevant_real_dimension_is_3','F1_public_record_lacks_reusable_numeric_relevant_eigenbasis','same_critical_exponents_allow_inequivalent_relevant_subspaces','critical_exponents_alone_cannot_define_displacement_basis','both_published_spectra_are_orientation_nonidentifying','spectral_difference_does_not_supply_basis_covariance','full_stability_matrix_blocked_by_unknown_higher_coupling_flows','closure_choice_changes_relevant_dimension_in_one_approximation','analytic_IR_flow_is_not_same_realization_as_best_F1_truncation','analytic_surrogate_not_promoted_to_physical_J8_basis','explicit_matrix_or_right_eigenvectors_are_minimum_orientation_object','J8_displacement_coordinates_remain_blocked_without_orientation_object','information_firewall_pass']
all_true=all(signals.get(k) is True for k in expected)
summary={
 'campaign':'f1-relevant-basis-wave32',
 'all_required_present':not missing,
 'all_predeclared_signals_true':all_true,
 'signals':{k:signals.get(k,False) for k in expected},
 'best_truncation_dimension':5,
 'displayed_relevant_real_dimension':3,
 'bar_spectrum_max_subspace_angle_rad':data['spectrum_orientation_nonidentifiability']['max_principal_angle_rad'],
 'bar_spectrum_median_max_subspace_angle_rad':data['spectrum_orientation_nonidentifiability']['median_max_principal_angle_rad'],
 'blocking_object':'BLOCKED_MISSING_REUSABLE_F1_RELEVANT_EIGENVECTOR_BASIS_OR_NUMERIC_APPROXIMATE_STABILITY_MATRIX_IN_SAME_CLOSURE',
 'scientific_verdict':'Wave 32 separates UV critical-surface dimension evidence from the orientation object required for physical displaced trajectories. F1 publishes a five-coordinate best truncation, fixed-point values and critical-exponent spectra that support three attractive real directions for the displayed closure, but the full stability matrix is explicitly unavailable because higher-coupling flows are unknown and the frozen public record does not provide numeric approximate matrices or right eigenvectors. Identical spectra admit widely different three-dimensional attractive invariant subspaces in five dimensions, so critical exponents cannot define the Wave-28 displacement basis. The Appendix-F/section-6 analytic flow is a useful surrogate but is not the same full momentum-dependent realization and is not promoted to physical J8 evidence.',
 'next_target':'Freeze Wave-32 certificate if clean. Wave 33: create and test an executable FRG basis/trajectory ingest contract; separately audit the maximum surrogate eigensystem reproducible from published analytic flow equations without treating it as the best-realization J8 basis.'
}
pathlib.Path('wave32_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)); print(json.dumps(summary,indent=2,sort_keys=True))
if not all_true: sys.exit(3)
