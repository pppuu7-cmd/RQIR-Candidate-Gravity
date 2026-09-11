import numpy as np
from common import write_result

# Finite coordinate proxy for an action-basis quotient.
# r1,r2: EOM/field-redefinition-redundant Ricci-type cubic directions.
# wE,wO: physical transverse Weyl-cubic-like directions (parity-even/odd labels used only as coordinates).
# This is not claimed as a complete D=4 operator classification.
basis=['r1_EOM_redundant','r2_EOM_redundant','wE_physical','wO_physical']
R=np.array([[1.,0.,0.,0.],[0.,1.,0.,0.]])
redundant_rank=int(np.linalg.matrix_rank(R))
quotient_dim=len(basis)-redundant_rank
# On-shell/finite-kinematic observables are insensitive to redundant coordinates and see physical ones.
H=np.array([[0.,0.,1.0,0.25],[0.,0.,-0.3,1.0]])
physical_rank=int(np.linalg.matrix_rank(H))
_,_,vt=np.linalg.svd(R,full_matrices=True)
Q=vt[redundant_rank:].T
holdout_rank_on_quotient=int(np.linalg.matrix_rank(H@Q,tol=1e-12))
out={
 'test':'field-redefinition/EOM quotient versus physical cubic action freedom',
 'basis':basis,
 'redundancy_matrix':R.tolist(),
 'redundant_rank':redundant_rank,
 'quotient_dimension':quotient_dim,
 'finite_kinematic_observable_matrix':H.tolist(),
 'physical_observable_rank':physical_rank,
 'holdout_rank_on_redefinition_quotient':holdout_rank_on_quotient,
 'field_redefinitions_remove_redundant_but_not_all_cubic_directions':quotient_dim>=1 and holdout_rank_on_quotient>=1,
 'scope_note':'Coordinate/rank proxy inspired by EOM-redundant Ricci operators and physical Weyl-cubic structures; not a claim of a complete operator basis.',
 'conclusion':'Quotienting by field redefinitions can remove unphysical/EOM-proportional operator coordinates, but physical cubic directions remain visible in on-shell/finite-kinematic observables. Redundancy removal therefore cannot convert the action into a unique cross-order completion.'
}
write_result('field_redefinition_quotient',out)
