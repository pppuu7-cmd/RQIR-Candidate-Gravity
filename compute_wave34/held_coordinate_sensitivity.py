import numpy as np
from common import L4_0,G4_0,solve_conditional,beta3,jac_fd,write
base,ok,_,_=solve_conditional(); rows=[]; root_shifts=[]; eig_shifts=[]
baseJ=jac_fd(lambda y: beta3(y),base); basevals=np.linalg.eigvals(baseJ)
for fl4 in [0.90,0.95,1.00,1.05,1.10]:
  for fg4 in [0.90,0.95,1.00,1.05,1.10]:
    l4=L4_0*fl4; g4=G4_0*fg4
    r,good,it,res=solve_conditional(l4,g4,start=base)
    J=jac_fd(lambda y,l4=l4,g4=g4: beta3(y,l4,g4),r)
    vals=np.linalg.eigvals(J)
    root_shift=float(np.linalg.norm(r-base)); root_shifts.append(root_shift)
    # compare sorted real parts only; no physical eigenvector matching is claimed
    eig_shift=float(np.linalg.norm(np.sort(vals.real)-np.sort(basevals.real))); eig_shifts.append(eig_shift)
    rows.append({'fl4':fl4,'fg4':fg4,'ok':good,'residual':res,'root':r.tolist(),'root_shift':root_shift,'eig_real_sorted':np.sort(vals.real).tolist(),'eig_real_shift':eig_shift})
signals={'all_25_held_coordinate_variants_converge':all(r['ok'] and r['residual']<1e-8 for r in rows),'conditional_root_depends_nontrivially_on_held_coordinates':max(root_shifts)>5e-2,'projected_spectrum_depends_nontrivially_on_held_coordinates':max(eig_shifts)>5e-2}
out={'test':'held_coordinate_sensitivity','variants':rows,'max_root_shift':max(root_shifts),'max_real_spectrum_shift':max(eig_shifts),'signals':signals}; write('wave34_held_coordinate_sensitivity.json',out); assert all(signals.values())
