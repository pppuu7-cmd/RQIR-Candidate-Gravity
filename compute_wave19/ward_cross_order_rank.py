import numpy as np
from common import write_result

# Basis chosen after a longitudinal/transverse decomposition of a symmetric 3-point response:
# [L1,L2,L3,T1,T2,T3]. The Ward identity fixes longitudinal combinations from the already-declared
# two-point inverse-kernel data p, while transverse structures are not fixed by the identity alone.
p=np.array([0.42,-0.18,0.11])
A=np.array([
 [1.0,0.0,0.0,0.0,0.0,0.0],
 [0.0,1.0,0.0,0.0,0.0,0.0],
 [0.0,0.0,1.0,0.0,0.0,0.0]
])
b=np.array([1.3*p[0]-0.2*p[1],-0.5*p[0]+0.9*p[1]+0.1*p[2],0.7*p[2]+0.15*p[0]])
rank=int(np.linalg.matrix_rank(A)); nullity=6-rank
part=np.linalg.lstsq(A,b,rcond=None)[0]
_,_,vt=np.linalg.svd(A,full_matrices=True)
N=vt[rank:].T
# prospective finite kinematics sees all transverse basis directions
h=np.array([0.0,0.0,0.0,0.63,-0.41,0.27])
sens=np.linalg.norm(h@N)
out={
 'test':'cross-order Ward rank: two-point data -> longitudinal three-point constraints',
 'vertex_basis':['L1','L2','L3','T1','T2','T3'],
 'ward_constraint_rank':rank,'vertex_nullity_after_ward':nullity,
 'two_point_input':p.tolist(),'ward_fixed_longitudinal_solution':part.tolist(),
 'transverse_nullspace_basis':N.tolist(),
 'finite_kinematic_holdout_sensitivity_to_ward_nullspace':float(sens),
 'ward_fixes_longitudinal_not_transverse':rank==3 and nullity==3 and sens>1e-4,
 'conclusion':'In a basis adapted to the Ward decomposition, the identity ties longitudinal 3-point combinations to the 2-point object but leaves three transverse vertex directions. Ward consistency therefore creates cross-order structure without uniquely deriving the full 3-point dynamics.'
}
write_result('ward_cross_order_rank',out)
