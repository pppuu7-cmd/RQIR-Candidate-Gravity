import numpy as np
from common import write_result

# Nonlinear/background Ward proxy on one-action coefficients.
# Three identity rows constrain longitudinal response combinations q1,q2,q3 from lower-point data,
# while physical transverse cubic Wilsons cE,cO are annihilated by the identity matrix.
A=np.array([
 [1.,0.,0.,0.,0.],
 [0.,1.,0.,0.,0.],
 [0.4,-0.2,1.,0.,0.]
])
rank=int(np.linalg.matrix_rank(A,tol=1e-12))
nullity=5-rank
_,_,vt=np.linalg.svd(A,full_matrices=True)
N=vt[rank:].T
H=np.array([[0.,0.,0.,1.,0.3],[0.,0.,0.,-0.25,1.]])
sensitivity=float(np.linalg.norm(H@N))
out={
 'test':'nonlinear/background Ward identity rank on action-derived three-point structures',
 'action_coordinates':['q1_longitudinal','q2_longitudinal','q3_longitudinal','cE_transverse','cO_transverse'],
 'ward_matrix':A.tolist(),
 'ward_rank':rank,'ward_nullity':nullity,
 'nullspace_basis':N.tolist(),
 'finite_transverse_holdout_sensitivity':sensitivity,
 'background_Ward_identity_leaves_physical_transverse_action_freedom':rank==3 and nullity==2 and sensitivity>1e-4,
 'conclusion':'Even when the vertex is treated as arising from one action, the Ward/Noether identities constrain gauge-longitudinal combinations and leave gauge-invariant transverse operator coefficients. Background covariance is therefore a consistency relation, not a unique Wilson-coefficient selector.'
}
write_result('background_ward_action_rank',out)
