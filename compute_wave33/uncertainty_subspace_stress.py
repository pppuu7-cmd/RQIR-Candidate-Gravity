import numpy as np
from common import surrogate_matrix,relevant_basis_from_matrix,principal_angles,write
rng=np.random.default_rng(330033)
A0=surrogate_matrix(); B0,_=relevant_basis_from_matrix(A0)
angles=[]; kept=0; failures=0
for _ in range(500):
    d=rng.normal(size=(5,5))
    A=A0+0.03*d
    try:
        B,vals=relevant_basis_from_matrix(A)
        kept+=1
        angles.append(float(np.max(principal_angles(B0,B))))
    except Exception:
        failures+=1
angles=np.array(angles)
finite=bool(len(angles)>0 and np.all(np.isfinite(angles)))
nonzero=bool(len(angles)>0 and np.max(angles)>1e-4)
signals={
 'small_matrix_perturbations_produce_finite_subspace_uncertainty':finite and nonzero,
 'relevant_real_dimension_remains_three_under_frozen_stress_scale':kept==500 and failures==0,
 'uncertainty_ensemble_is_nontrivial_not_a_single_basis':float(np.std(angles))>1e-5
}
out={'test':'uncertainty_subspace_stress','sigma':0.03,'trials':500,'accepted':kept,'failures':failures,'median_max_principal_angle_rad':float(np.median(angles)),'p95_max_principal_angle_rad':float(np.quantile(angles,0.95)),'max_principal_angle_rad':float(np.max(angles)),'signals':signals}; write('wave33_uncertainty_subspace_stress.json',out); assert all(signals.values())
