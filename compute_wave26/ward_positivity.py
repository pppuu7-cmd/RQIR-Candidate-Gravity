import numpy as np
from common import W, BOUNDS, X, null_basis, write_result
rng=np.random.default_rng(2601)
N=null_basis(W)
nullity=N.shape[1]
n=20000
z=rng.normal(size=(n,nullity)); z/=np.linalg.norm(z,axis=1,keepdims=True)
dirs=z@N.T
ell=np.sqrt(((dirs/BOUNDS)**2).sum(axis=1))
r=rng.random(n)**(1/nullity)
theta=dirs/ell[:,None]*r[:,None]
ward_residual=float(np.max(np.linalg.norm(theta@W.T,axis=1)))
Y=theta@X().T
widths=Y.max(axis=0)-Y.min(axis=0)
mx=float(widths.max())
signal=bool(nullity==3 and ward_residual<1e-10 and mx>=0.05)
write_result('ward_positivity',{'samples':n,'seed':2601,'ward_nullity':nullity,'max_ward_residual':ward_residual,'max_frozen_bank_prediction_width':mx,'ward_positivity_intersection_nonunique':signal})
