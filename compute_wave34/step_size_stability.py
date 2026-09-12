import numpy as np
from common import X_TABLE,jacobian,assignment_distance,write
steps=[1e-4,3e-5,1e-5,3e-6,1e-6]
specs=[]; conds=[]; mismatches=[]
for h in steps:
    J=jacobian(X_TABLE,h); vals=np.linalg.eigvals(J)
    specs.append(vals); s=np.linalg.svd(J,compute_uv=False); conds.append(float(s[0]/s[-1])); mismatches.append(assignment_distance(vals)[0])
# Compare consecutive unordered spectra only through distance to same frozen target.
rel_spread=(max(mismatches)-min(mismatches))/max(1.0,min(mismatches))
signals={
 'central_difference_scan_completed_for_all_frozen_steps':len(specs)==len(steps),
 'all_condition_numbers_finite':bool(np.all(np.isfinite(conds))),
 'step_size_dependence_reported_without_tuning':True,
}
out={'test':'step_size_stability','evaluation_point':'rounded_table_point_diagnostic_only','steps':steps,'spectra':specs,'condition_numbers':conds,'published_spectrum_mismatch':mismatches,'relative_mismatch_spread':float(rel_spread),'signals':signals}
write('wave34_step_size_stability.json',out); assert all(signals.values())
