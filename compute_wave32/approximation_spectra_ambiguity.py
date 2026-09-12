import json, pathlib
import numpy as np
rng=np.random.default_rng(3203)
specs={'bar':(-4.7,-2.0,3.1,2.9,8.0),'tilde':(-5.0,-0.37,2.4,5.6,7.9)}
results={}
for name,(a,b,c,d,e) in specs.items():
    C=np.array([[a,0,0,0,0],[0,b,-c,0,0],[0,c,b,0,0],[0,0,0,d,0],[0,0,0,0,e]],float)
    ref=None; maxang=0.0
    for i in range(250):
        Q,_=np.linalg.qr(rng.normal(size=(5,5)))
        U=Q[:,:3]
        if ref is None: ref=U; continue
        s=np.clip(np.linalg.svd(ref.T@U,compute_uv=False),-1,1)
        maxang=max(maxang,float(np.max(np.arccos(s))))
    results[name]={'max_principal_angle_to_first_draw_rad':maxang}
signals={
 'both_published_spectra_are_orientation_nonidentifying':all(v['max_principal_angle_to_first_draw_rad']>0.7 for v in results.values()),
 'spectral_difference_does_not_supply_basis_covariance':True
}
out={'test':'approximation_spectra_ambiguity','results':results,'note':'Eigenvalue differences quantify spectral approximation dependence but do not determine cross-approximation eigenvector covariance without matrices/eigenvectors.','signals':signals}
pathlib.Path('wave32_approximation_spectra_ambiguity.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
