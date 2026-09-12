import numpy as np
from common import relevant_basis_from_matrix,surrogate_matrix,write
A=surrogate_matrix(); B,vals=relevant_basis_from_matrix(A)
rank=int(np.linalg.matrix_rank(B,tol=1e-10))
orth_err=float(np.linalg.norm(B.T@B-np.eye(3)))
neg=sum(z.real<0 for z in vals)
complex_pairs=sum(z.real<0 and z.imag>1e-8 for z in vals)
signals={
 'one_real_plus_one_complex_pair_realifies_to_rank3':rank==3 and neg==3 and complex_pairs==1,
 'realified_basis_is_orthonormal':orth_err<1e-10
}
out={'test':'complex_realification','eigenvalues':[str(z) for z in vals],'rank':rank,'orthonormal_error':orth_err,'signals':signals}; write('wave33_complex_realification.json',out); assert all(signals.values())
