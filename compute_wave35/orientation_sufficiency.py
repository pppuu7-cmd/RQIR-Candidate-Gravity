import json, itertools
from pathlib import Path
import numpy as np
rng=np.random.default_rng(3504)
Q,_=np.linalg.qr(rng.normal(size=(5,5)))
B=Q[:,:3]
# A matrix carrying one real attractive eigenvalue + one attractive complex pair.
C=np.zeros((5,5)); C[0,0]=-4.7; C[1:3,1:3]=np.array([[-2.0,-3.1],[3.1,-2.0]]); C[3,3]=2.9; C[4,4]=8.0
M=Q@C@Q.T
vals,vecs=np.linalg.eig(M)
cols=[]
for i,z in enumerate(vals):
    if z.real<0 and abs(z.imag)<1e-8: cols.append(np.real(vecs[:,i]))
for i,z in enumerate(vals):
    if z.real<0 and z.imag>1e-8:
        cols.extend([np.real(vecs[:,i]),np.imag(vecs[:,i])]); break
Qm,_=np.linalg.qr(np.column_stack(cols)); Bm=Qm[:,:3]
P=lambda X:X@X.T
matrix_direct_err=float(np.linalg.norm(P(Bm)-P(B)))
# Eigenvalues alone: rotate the same canonical block with a new orthogonal matrix.
Q2,_=np.linalg.qr(rng.normal(size=(5,5))); M2=Q2@C@Q2.T
# true first-three invariant subspaces differ generically.
s=np.linalg.svd(B.T@Q2[:,:3],compute_uv=False); max_angle=float(np.max(np.arccos(np.clip(s,-1,1))))
# Seven trajectories from either matrix-derived or direct basis.
eps=1e-3; x0=np.array([-0.45,0.12,0.028,0.83,0.57])
def traj(X):
    rows=[x0]
    for j in range(3): rows.extend([x0+eps*X[:,j],x0-eps*X[:,j]])
    return np.vstack(rows)
T=traj(Bm)
signals={
 'numeric_matrix_is_sufficient_to_recover_rank3_real_basis':Bm.shape==(5,3) and np.linalg.matrix_rank(Bm)==3,
 'direct_normalized_5x3_basis_is_sufficient_for_seven_trajectories':T.shape==(7,5),
 'matrix_and_direct_basis_agree_on_projector':matrix_direct_err<1e-10,
 'eigenvalues_alone_are_not_orientation_sufficient':max_angle>0.2,
}
out={'test':'orientation_sufficiency','matrix_direct_projector_error':matrix_direct_err,'same_spectrum_alternative_max_subspace_angle_rad':max_angle,'trajectory_shape':list(T.shape),'signals':signals}
Path('wave35_orientation_sufficiency.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
