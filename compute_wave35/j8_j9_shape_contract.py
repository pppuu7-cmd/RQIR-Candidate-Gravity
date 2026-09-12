import json
from pathlib import Path
import numpy as np
rng=np.random.default_rng(3506)
# Synthetic contract test only: six outputs as a smooth map of five UV coordinates.
A=rng.normal(size=(6,5))
Q,_=np.linalg.qr(rng.normal(size=(5,5))); B=Q[:,:3]
J=A@B
rank=int(np.linalg.matrix_rank(J,tol=1e-10))
# Propagate small orientation/output perturbations into vec(J), producing an 18x18 covariance object.
vec=[]
for _ in range(600):
    dA=1e-3*rng.normal(size=(6,5))
    dB=1e-3*rng.normal(size=(5,3))
    vec.append(((A+dA)@(B+dB)).reshape(-1))
V=np.vstack(vec)
C=np.cov(V,rowvar=False)
evals=np.linalg.eigvalsh((C+C.T)/2)
signals={
 'synthetic_J8_shape_is_6x3':J.shape==(6,3),
 'synthetic_J8_has_expected_max_rank3':rank==3,
 'J9_covariance_shape_is_18x18_for_vectorized_J8':C.shape==(18,18),
 'propagated_covariance_is_positive_semidefinite_numerically':float(evals.min())>-1e-12,
}
out={'test':'j8_j9_shape_contract','J8_shape':list(J.shape),'J8_rank':rank,'covariance_shape':list(C.shape),'covariance_min_eigenvalue':float(evals.min()),'signals':signals,'note':'Synthetic interface contract only; no physical AS-QG derivative values are inferred.'}
Path('wave35_j8_j9_shape_contract.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
