import numpy as np
from common import canonical_matrix,relevant_basis_from_matrix,write
M=canonical_matrix(); B,vals=relevant_basis_from_matrix(M)
neg=[z for z in vals if z.real<0]
complex_pair=sum(abs(z.imag)>1e-8 for z in neg)==2
signals={
 'one_real_plus_one_complex_pair_realifies_to_real_rank3_basis':B.shape==(5,3) and np.linalg.matrix_rank(B)==3 and complex_pair,
 'realified_basis_is_orthonormal':float(np.linalg.norm(B.T@B-np.eye(3)))<1e-10
}
out={'test':'complex_pair_realification','eigenvalues':[str(z) for z in vals],'orthonormal_error':float(np.linalg.norm(B.T@B-np.eye(3))),'signals':signals}; write('wave36_complex_pair_realification.json',out); assert all(signals.values())
