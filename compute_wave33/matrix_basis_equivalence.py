import numpy as np
from common import surrogate_matrix,relevant_basis_from_matrix,projector,orth,write
A=surrogate_matrix(); Bm,_=relevant_basis_from_matrix(A)
# Direct basis path deliberately rescales and mixes columns without changing the subspace.
E=np.eye(5)[:,:3]
T=np.array([[2.0,0.3,-0.2],[0.0,-4.0,0.7],[0.0,0.0,1.5]])
Bd=orth(E@T)
err=float(np.linalg.norm(projector(Bm)-projector(Bd)))
signals={'matrix_ingest_and_direct_basis_ingest_agree_on_relevant_projector':err<1e-10}
out={'test':'matrix_basis_equivalence','projector_error':err,'signals':signals}; write('wave33_matrix_basis_equivalence.json',out); assert all(signals.values())
