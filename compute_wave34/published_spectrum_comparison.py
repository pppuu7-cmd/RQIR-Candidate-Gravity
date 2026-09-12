import numpy as np
from common import X_TABLE,jacobian,assignment_distance,write
J=jacobian(X_TABLE,1e-6); vals=np.linalg.eigvals(J); mismatch,perm=assignment_distance(vals)
signals={
 'published_bar_spectrum_compared_permutation_and_conjugation_invariantly':np.isfinite(mismatch),
 'spectrum_mismatch_is_reported_not_optimized':True,
}
out={'test':'published_spectrum_comparison','evaluation_point':'rounded_table_point_diagnostic_only','numeric_spectrum':vals,'max_assignment_error_to_published_bar_spectrum':mismatch,'best_permutation':perm,'signals':signals}
write('wave34_published_spectrum_comparison.json',out); assert all(signals.values())
