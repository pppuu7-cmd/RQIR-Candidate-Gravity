from common import load,write
D=load()['evidence']
out={
 'central_physical_fits_available':D['D28_1_central_physical_representation']['status']=='PASS_ANALYTIC_FITS_AVAILABLE',
 'critical_exponents_do_not_substitute_eigenvectors':bool(D['D28_2_uv_coordinate_basis']['critical_exponents_available'] and not D['D28_2_uv_coordinate_basis']['explicit_numeric_eigenvector_basis_frozen']),
 'public_same_realization_derivative_ensemble_missing':not D['D28_3_trajectory_ensemble']['direction_resolved_displaced_trajectory_ensemble_frozen'],
 'explicit_six_output_projection_missing':not D['D28_4_six_output_projection']['effective_action_to_six_rqir_map'],
 'propagated_six_output_covariance_missing':not D['D28_5_uncertainty']['six_output_propagated_covariance'],
 'central_fit_availability_does_not_close_J8':bool(D['D28_6_reproducible_machine_object']['central_fits_reusable'] and not D['D28_3_trajectory_ensemble']['direction_resolved_displaced_trajectory_ensemble_frozen'])
}
write('evidence_gate',out)
