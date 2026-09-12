import json, pathlib
import numpy as np
rng=np.random.default_rng(3202)
# Real canonical representation of bar_B spectrum: one real attractive eigenvalue,
# one attractive complex pair represented as a 2x2 block, and two repulsive modes.
C=np.array([[-4.7,0,0,0,0],[0,-2.0,-3.1,0,0],[0,3.1,-2.0,0,0],[0,0,0,2.9,0],[0,0,0,0,8.0]],float)
def draw():
    Q,_=np.linalg.qr(rng.normal(size=(5,5)))
    B=Q@C@Q.T
    U=Q[:,:3]
    return B,U
angles=[]; spectral_errors=[]
for _ in range(400):
    B1,U1=draw(); B2,U2=draw()
    s=np.linalg.svd(U1.T@U2,compute_uv=False)
    s=np.clip(s,-1,1)
    a=np.arccos(s)
    angles.append([float(x) for x in a])
    eig=np.linalg.eigvals(B1)
    # compare sorted real parts / abs imag as a robust invariant summary
    spectral_errors.append(abs(np.trace(B1)-np.trace(C)))
max_angle=max(max(a) for a in angles)
median_max=float(np.median([max(a) for a in angles]))
signals={
 'same_critical_exponents_allow_inequivalent_relevant_subspaces':max_angle>0.7 and median_max>0.4,
 'critical_exponents_alone_cannot_define_displacement_basis':max(spectral_errors)<1e-10 and max_angle>0.7
}
out={'test':'spectrum_orientation_nonidentifiability','trials':400,'max_principal_angle_rad':max_angle,'median_max_principal_angle_rad':median_max,'max_trace_invariance_error':max(spectral_errors),'signals':signals}
pathlib.Path('wave32_spectrum_orientation_nonidentifiability.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
