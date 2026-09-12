import numpy as np
from common import XSTAR,surrogate_matrix,relevant_basis_from_matrix,orth,write
A=surrogate_matrix(); B,_=relevant_basis_from_matrix(A)
eps=1e-3
traj=[XSTAR.copy()]
for i in range(3):
    traj += [XSTAR+eps*B[:,i], XSTAR-eps*B[:,i]]
traj=np.array(traj)
pair_errors=[]
for j in range(3):
    pair_errors.append(float(np.linalg.norm(traj[1+2*j]+traj[2+2*j]-2*XSTAR)))
# scale/mix each direction independently; after normalization trajectories must be identical up to signs.
Bs=orth(B@np.diag([3.7,-0.2,11.0]))
Perr=float(np.linalg.norm(B@B.T-Bs@Bs.T))
step_norms=[float(np.linalg.norm(traj[k]-XSTAR)) for k in range(1,7)]
signals={
 'exactly_seven_symmetric_trajectories_generated':len(traj)==7 and max(pair_errors)<1e-12,
 'all_displacement_steps_have_frozen_norm':max(abs(x-eps) for x in step_norms)<1e-12,
 'input_vector_rescaling_does_not_change_normalized_relevant_subspace':Perr<1e-10
}
out={'test':'seven_trajectory_generator','epsilon':eps,'trajectory_count':len(traj),'pair_cancellation_errors':pair_errors,'step_norms':step_norms,'rescaling_projector_error':Perr,'trajectories':traj.tolist(),'signals':signals}; write('wave33_seven_trajectory_generator.json',out); assert all(signals.values())
