from common import load,write
D=load(); e=next(s for s in D['sources'] if s['id']=='E1'); p=e['partial_bridge']; vals=p['reported_dimensionless_coefficient_magnitudes']; ratio=max(vals)/min(vals)
out={'source':'E1','partial_bridge':p,'magnitude_ratio_between_reported_regulator_treatments':ratio,'C3_partial_UV_to_IR_bridge_exists':bool(p['single_relevant_direction_after_unit_fixing'] and p['unique_separatrix_in_declared_two-coupling_truncation']),'C3_sign_robust_but_magnitude_scheme_sensitive':bool(p['positive_sign_in_both_reported_regulator_treatments'] and not p['quantitative_magnitude_scheme_closed'])}
write('c3_bridge',out)
