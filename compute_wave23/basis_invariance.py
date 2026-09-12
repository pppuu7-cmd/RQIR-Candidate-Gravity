import numpy as np
from common import X_and_probes, write_result

X,_=X_and_probes(); base_sv=np.linalg.svd(X,compute_uv=False)
rng=np.random.default_rng(2301)
ranks=[]; sv_err=[]; pred_err=[]
for _ in range(500):
    A=rng.normal(size=(6,6))
    Q,R=np.linalg.qr(A)
    Q=Q@np.diag(np.where(np.diag(R)>=0,1.0,-1.0))
    Xr=X@Q
    theta=rng.normal(size=6)
    theta_r=Q.T@theta
    ranks.append(int(np.linalg.matrix_rank(Xr,tol=1e-10)))
    sv=np.linalg.svd(Xr,compute_uv=False)
    sv_err.append(float(np.max(np.abs(sv-base_sv)/np.maximum(base_sv,1e-15))))
    pred_err.append(float(np.max(np.abs(X@theta-Xr@theta_r))))
out={
 'test':'500 seeded orthogonal residual-basis rotations',
 'seed':2301,
 'trials':500,
 'full_rank_fraction':sum(r==6 for r in ranks)/len(ranks),
 'max_relative_singular_value_error':max(sv_err),
 'max_prediction_error':max(pred_err),
 'all_rank_6':all(r==6 for r in ranks),
 'singular_spectrum_invariant_le_1e_12':max(sv_err)<=1e-12,
 'predictions_invariant_le_1e_12':max(pred_err)<=1e-12,
 'conclusion':'The frozen exam is invariant under harmless orthogonal reparameterizations of the six residual directions.'
}
write_result('basis_invariance',out)
