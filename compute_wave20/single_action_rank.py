import numpy as np
from common import write_result

# One-action parameter vector p=[a2,b2,c3,d3].
# a2,b2 control physical quadratic/two-point transverse form-factor corrections.
# c3,d3 are independent cubic transverse Wilson directions in the same action.
# The precise operator basis is abstracted; the rank question is whether 'one action' alone links orders.
J2=np.array([
 [1.0,0.25,0.0,0.0],
 [0.2,1.0,0.0,0.0],
 [0.75,-0.4,0.0,0.0]
])
J3=np.array([
 [0.35,-0.15,1.0,0.2],
 [-0.25,0.45,0.3,1.0]
])
rank2=int(np.linalg.matrix_rank(J2,tol=1e-12))
rankfull=int(np.linalg.matrix_rank(np.vstack([J2,J3]),tol=1e-12))
null2=4-rank2
nullfull=4-rankfull
_,_,vt=np.linalg.svd(J2,full_matrices=True)
N2=vt[rank2:].T
three_sens=np.linalg.norm(J3@N2)
out={
 'test':'single covariant action does not by itself identify independent higher-order Wilson directions',
 'parameter_vector':['a2_two_point','b2_two_point','c3_cubic','d3_cubic'],
 'two_point_jacobian':J2.tolist(),
 'three_point_jacobian':J3.tolist(),
 'two_point_rank':rank2,
 'two_point_nullity':null2,
 'joint_two_plus_three_point_rank':rankfull,
 'joint_nullity':nullfull,
 'three_point_sensitivity_to_two_point_nullspace':float(three_sens),
 'same_action_still_has_cross_order_Wilson_freedom':rank2==2 and null2==2 and three_sens>1e-4,
 'higher_point_data_can_identify_extra_action_directions':rankfull>rank2,
 'conclusion':'Packaging all sectors into one action enforces a common dynamics but does not relate independent operator coefficients at different orders. Two-point observables leave cubic Wilson directions exactly unconstrained; finite three-point data can see them. The RQIR single-dynamics rule is necessary but is not an action-level closure law.'
}
write_result('single_action_rank',out)
