import json,glob
from pathlib import Path
files=glob.glob('wave28_downloads/*/*.json')
data={Path(f).stem:json.loads(Path(f).read_text()) for f in files}
required=['evidence_gate','trajectory_count','synthetic_fd_contract','projection_contract','uncertainty_contract','anti_splice_firewall']
missing=[k for k in required if k not in data]
signals={
 'central_physical_fits_available':bool(data.get('evidence_gate',{}).get('central_physical_fits_available',False)),
 'critical_exponents_do_not_substitute_eigenvectors':bool(data.get('evidence_gate',{}).get('critical_exponents_do_not_substitute_eigenvectors',False)),
 'minimum_one_sided_trajectory_count_is_4':bool(data.get('trajectory_count',{}).get('minimum_one_sided_trajectory_count_is_4',False)),
 'minimum_symmetric_trajectory_count_is_7':bool(data.get('trajectory_count',{}).get('minimum_symmetric_trajectory_count_is_7',False)),
 'public_same_realization_derivative_ensemble_missing':bool(data.get('evidence_gate',{}).get('public_same_realization_derivative_ensemble_missing',False)),
 'explicit_six_output_projection_missing':bool(data.get('projection_contract',{}).get('explicit_six_output_projection_missing',False)),
 'propagated_six_output_covariance_missing':bool(data.get('uncertainty_contract',{}).get('propagated_six_output_covariance_missing',False)),
 'central_fit_availability_does_not_close_J8':bool(data.get('evidence_gate',{}).get('central_fit_availability_does_not_close_J8',False)),
 'anti_splice_firewall_pass':bool(data.get('anti_splice_firewall',{}).get('anti_splice_firewall_pass',False))
}
supporting={
 'synthetic_contract_recovers_6x3_shape':bool(data.get('synthetic_fd_contract',{}).get('synthetic_contract_recovers_6x3_shape',False)),
 'second_order_step_halving_ratio_near_4':bool(data.get('synthetic_fd_contract',{}).get('second_order_step_halving_ratio_near_4',False)),
 'J9_contract_well_defined':bool(data.get('uncertainty_contract',{}).get('J9_contract_well_defined',False))
}
all_true=(not missing) and all(signals.values()) and all(supporting.values())
summary={
 'campaign':'jacobian-data-contract-wave28',
 'all_required_present':not missing,
 'missing':missing,
 'signals':signals,
 'supporting_contract_checks':supporting,
 'all_predeclared_signals_true':(not missing) and all(signals.values()),
 'all_contract_checks_true':all_true,
 'jacobian_shape':[6,3],
 'minimum_one_sided_trajectories':data.get('trajectory_count',{}).get('minimum_one_sided_trajectory_count'),
 'minimum_symmetric_trajectories':data.get('trajectory_count',{}).get('minimum_symmetric_trajectory_count'),
 'synthetic_step_halving_error_ratio':data.get('synthetic_fd_contract',{}).get('error_ratio'),
 'blocking_object':'BLOCKED_MISSING_F1F2_UV_EIGENVECTOR_BASIS_PLUS_DISPLACED_TRAJECTORY_ENSEMBLE_PLUS_SIX_OUTPUT_PROJECTION_AND_COVARIANCE',
 'scientific_verdict':'Wave 28 finds that F2 central physical-limit momentum dependence is substantially more reusable than a plot-only result because published analytic fits exist. The missing J8/J9 object is narrower: the frozen public F1+F2 record does not expose an explicit numerical relevant-eigenvector basis, a same-realization trajectory ensemble displaced independently along all three UV-relevant directions, an explicit projection from the reconstructed effective-action basis to all six frozen RQIR residual outputs, or propagated six-output covariance. A synthetic contract confirms the planned 6x3 symmetric finite-difference pipeline and its expected step-size convergence, but no synthetic result is counted as physics.',
 'next_target':'Freeze Wave-28 certificate if clean. Next inspect whether F1/F2 TeX/source or author-released numerical packages contain enough hidden tabulated coefficients/eigenvectors to instantiate the contract. If not, construct a minimal author-data request / reproducibility specification and shift computation to any same-lineage quantities that can be reconstructed exactly from the published analytic fits.'
}
Path('wave28_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True))
print(json.dumps(summary,indent=2,sort_keys=True))
if not all_true: raise SystemExit(1)
