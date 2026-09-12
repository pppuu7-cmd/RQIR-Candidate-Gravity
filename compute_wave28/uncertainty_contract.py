from common import load,write
D=load()['evidence']['D28_5_uncertainty']
requirements={
 'same_output_basis_across_variants':True,
 'regulator_or_truncation_variants':True,
 'recompute_same_6x3_jacobian_for_each_variant':True,
 'report_columnwise_and_output_covariance':True,
 'separate_fit_error_from_scheme_spread':True
}
out={'requirements':requirements,'input_level_stability_information_available':D['input_level_stability_information'],'six_output_propagated_covariance_available':D['six_output_propagated_covariance'],'propagated_six_output_covariance_missing':not D['six_output_propagated_covariance'],'J9_contract_well_defined':all(requirements.values())}
write('uncertainty_contract',out)
