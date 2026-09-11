#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Generic causal polynomial kernel on the triangle 0<=y<=x<=1.
# K(x,y)=sum_{i,j=0}^2 c_ij x^i y^j. Causality is represented by the triangular domain itself.
pairs=[(i,j) for i in range(3) for j in range(3)]
rows=[]; rhs=[]; labels=[]
# Soft lower endpoint: K(x,0)=0.
for i in range(3):
    rows.append([1.0 if (ii,jj)==(i,0) else 0.0 for ii,jj in pairs]); rhs.append(0.0); labels.append(f'y0_x^{i}')
# Coincidence softness: K(x,x)=0 as a polynomial identity.
for k in range(5):
    rows.append([1.0 if ii+jj==k else 0.0 for ii,jj in pairs]); rhs.append(0.0); labels.append(f'diagonal_degree_{k}')
Ah=np.array(rows,float)
rank_h=int(np.linalg.matrix_rank(Ah,tol=1e-12))
null_h=len(pairs)-rank_h
# Fix overall normalization integral_triangle K = 1.
integ=np.array([1.0/((j+1)*(i+j+2)) for i,j in pairs])
A=np.vstack([Ah,integ]); b=np.r_[rhs,1.0]
rank_full=int(np.linalg.matrix_rank(A,tol=1e-12)); null_full=len(pairs)-rank_full
c=np.linalg.lstsq(A,b,rcond=None)[0]
U,S,Vh=np.linalg.svd(A,full_matrices=True)
nv=Vh[-1]; nv=nv/np.linalg.norm(nv)
# Two untouched kernel functionals.
Ix=np.array([1.0/((j+1)*(i+j+3)) for i,j in pairs])  # integral x*K
Iy=np.array([1.0/((j+2)*(i+j+3)) for i,j in pairs])  # integral y*K
scan=[]
for t in [-1.0,-0.5,0.0,0.5,1.0]:
    cc=c+t*nv
    scan.append({"t":t,"constraint_max_error":float(np.max(np.abs(A@cc-b))),"holdout_int_xK":float(Ix@cc),"holdout_int_yK":float(Iy@cc)})
wx=[r['holdout_int_xK'] for r in scan]; wy=[r['holdout_int_yK'] for r in scan]
out={
 "test":"rank audit of generic structural axioms on a finite causal kernel basis",
 "basis":"K(x,y)=sum c_ij x^i y^j, i,j=0..2 on 0<=y<=x<=1",
 "number_of_coefficients":len(pairs),
 "homogeneous_axioms":["causal triangular support (domain)","K(x,0)=0","K(x,x)=0"],
 "homogeneous_constraint_rank":rank_h,
 "homogeneous_shape_nullity":null_h,
 "normalization":"integral_triangle K = 1",
 "rank_after_normalization":rank_full,
 "shape_nullity_after_normalization":null_full,
 "particular_solution_coefficients":[float(v) for v in c],
 "normalized_remaining_null_vector":[float(v) for v in nv],
 "scan":scan,
 "holdout_int_xK_width":float(max(wx)-min(wx)),
 "holdout_int_yK_width":float(max(wy)-min(wy)),
 "generic_axioms_leave_kernel_shape_freedom":bool(null_full>=1),
 "conclusion":"Causality encoded by triangular support, two soft endpoint/coincidence identities and an overall normalization do not uniquely fix even a 9-coefficient polynomial kernel: one normalized shape direction remains and changes untouched kernel functionals. This is a generic operator-origin proxy, not an RQIR-specific derivation and not a positivity theorem."
}
Path('wave15_results').mkdir(exist_ok=True)
Path('wave15_results/kernel_axiom_rank.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
