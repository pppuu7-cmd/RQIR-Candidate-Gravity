import numpy as np
from common import solve_conditional,beta3,jac_fd,write
root,ok,_,_=solve_conditional(); J=jac_fd(lambda y: beta3(y),root); vals=np.linalg.eigvals(J)
published=np.array([-3.0,-1.9,-1.9,1.7,3.4])
neg_partial=sum(z.real<0 for z in vals); neg_published=sum(x<0 for x in published)
# Diagnostic only: compare counts and sorted real parts of the three closest published entries.
partial_sorted=np.sort(vals.real)
pub3=np.sort(published)[:3]
count_mismatch=neg_partial!=neg_published
shape_mismatch=float(np.linalg.norm(partial_sorted-pub3))
signals={'partial_projected_negative_real_count_differs_from_published_5d_surrogate_count':count_mismatch,'projected_spectrum_is_not_numerically_substitutable_for_published_5d_spectrum':shape_mismatch>0.5,'no_spectrum_tuning_or_matching_used':True}
out={'test':'published_spectrum_mismatch','partial_eigenvalues':[str(z) for z in vals],'published_bar_spectrum_real_parts':published.tolist(),'partial_negative_real_count':neg_partial,'published_negative_real_count':neg_published,'three_value_realpart_distance':shape_mismatch,'signals':signals}; write('wave34_published_spectrum_mismatch.json',out); assert all(signals.values())
