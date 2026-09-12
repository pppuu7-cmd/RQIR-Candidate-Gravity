import numpy as np
from common import solve_conditional,beta3,jac_fd,write
root,ok,_,_=solve_conditional(); J=jac_fd(lambda y: beta3(y),root)
M2=np.zeros((5,5)); M2[:3,:3]=J; M2[3,3]=2.0; M2[4,4]=3.0
M3=np.zeros((5,5)); M3[:3,:3]=J; M3[3,3]=-4.0; M3[4,4]=3.0
n2=sum(z.real<0 for z in np.linalg.eigvals(M2)); n3=sum(z.real<0 for z in np.linalg.eigvals(M3))
unknown_entries=25-9
signals={'three_by_three_conditional_jacobian_leaves_16_full_matrix_entries_undetermined':unknown_entries==16,'same_projected_block_allows_different_full_5d_relevant_dimensions':n2!=n3,'partial_jacobian_cannot_determine_full_5d_J8_orientation':True}
out={'test':'embedding_no_go','known_entries':9,'unknown_full_matrix_entries':unknown_entries,'completion_A_negative_real_count':n2,'completion_B_negative_real_count':n3,'shared_upper_left_block':J.tolist(),'signals':signals}; write('wave34_embedding_no_go.json',out); assert all(signals.values())
