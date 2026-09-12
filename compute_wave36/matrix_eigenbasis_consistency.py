import copy, numpy as np
from common import complete_candidate,validate,write
base=complete_candidate(); ok0,r0,e0=validate(base)
bad=copy.deepcopy(base)
B=np.asarray(bad['right_relevant_real_basis'],float)
# Rotate one basis vector into the fourth coordinate while preserving rank/normalization.
B[:,0]=0.0; B[3,0]=1.0
bad['right_relevant_real_basis']=B.tolist()
ok1,r1,e1=validate(bad)
signals={
 'consistent_matrix_and_eigenbasis_candidate_is_accepted':ok0 and e0 is not None and e0<1e-8,
 'deliberately_inconsistent_basis_is_rejected':(not ok1) and 'matrix_basis_inconsistent' in r1,
 'consistency_rejection_is_projector_based_not_vector_phase_based':e1 is not None and e1>1e-3
}
out={'test':'matrix_eigenbasis_consistency','good_projector_error':e0,'bad_projector_error':e1,'bad_reasons':r1,'signals':signals}; write('wave36_matrix_eigenbasis_consistency.json',out); assert all(signals.values())
