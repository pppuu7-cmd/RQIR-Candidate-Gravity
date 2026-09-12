import numpy as np
from common import solve_conditional,beta3,jac_fd,write
root,ok,it,res=solve_conditional(); f=lambda y: beta3(y); J=jac_fd(f,root); vals=np.linalg.eigvals(J)
rank=int(np.linalg.matrix_rank(J,tol=1e-10)); cond=float(np.linalg.cond(J)); det=float(np.linalg.det(J))
neg=sum(z.real<0 for z in vals); pos=sum(z.real>0 for z in vals)
signals={'projected_jacobian_is_full_rank_3':rank==3,'projected_jacobian_is_finite_and_well_defined':np.isfinite(cond) and cond<1e4,'projected_flow_has_two_attractive_real_dimensions_and_one_repulsive_dimension':neg==2 and pos==1}
out={'test':'projected_jacobian','root':root.tolist(),'jacobian':J.tolist(),'eigenvalues':[str(z) for z in vals],'rank':rank,'condition_number':cond,'determinant':det,'negative_real_count':neg,'positive_real_count':pos,'signals':signals}; write('wave34_projected_jacobian.json',out); assert all(signals.values())
