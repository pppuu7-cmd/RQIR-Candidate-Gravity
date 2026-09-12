import numpy as np
from common import X_and_probes, write_result

X,_=X_and_probes(); rng=np.random.default_rng(2302)
ranks=[]; errors=[]; min_scale=1e99; max_scale=0.0
for _ in range(500):
    scales=10.0**rng.uniform(-2.0,2.0,size=6)
    S=np.diag(scales)
    Xu=X@np.linalg.inv(S)
    theta=rng.normal(size=6)
    theta_u=S@theta
    ranks.append(int(np.linalg.matrix_rank(Xu,tol=1e-10)))
    errors.append(float(np.max(np.abs(X@theta-Xu@theta_u))))
    min_scale=min(min_scale,float(scales.min())); max_scale=max(max_scale,float(scales.max()))
out={
 'test':'500 seeded residual-parameter unit rescalings',
 'seed':2302,
 'trials':500,
 'scale_range_realized':[min_scale,max_scale],
 'full_rank_fraction':sum(r==6 for r in ranks)/len(ranks),
 'max_prediction_error':max(errors),
 'all_rank_6':all(r==6 for r in ranks),
 'predictions_invariant_le_1e_12':max(errors)<=1e-12,
 'conclusion':'Changing parameter units over four decades does not change physical holdout predictions when coefficients transform consistently, and it does not change identifiability rank.'
}
write_result('unit_rescaling',out)
