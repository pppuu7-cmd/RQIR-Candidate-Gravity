import numpy as np
from common import surrogate_matrix,projector,write
A=surrogate_matrix().astype(complex)
vals,vecs=np.linalg.eig(A)
i=max([i for i,z in enumerate(vals) if z.real<0], key=lambda i: vals[i].imag)
v=vecs[:,i]
B0=np.column_stack([v.real,v.imag])
P0=projector(B0)
errs=[]
for phi in np.linspace(0,2*np.pi,73):
    vr=v*np.exp(1j*phi)
    P=projector(np.column_stack([vr.real,vr.imag]))
    errs.append(float(np.linalg.norm(P-P0)))
mx=max(errs)
signals={'complex_phase_leaves_real_plane_projector_invariant':mx<1e-10}
out={'test':'phase_invariance','max_projector_frobenius_error':mx,'samples':len(errs),'signals':signals}; write('wave33_phase_invariance.json',out); assert all(signals.values())
