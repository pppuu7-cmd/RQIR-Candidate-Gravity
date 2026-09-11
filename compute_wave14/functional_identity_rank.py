#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

a,b=1.7,2.4

def moment(n):
    v=1.0
    for j in range(n): v*= (a+j)/(a+b+j)
    return v

def orth_poly(deg):
    G=np.array([[moment(i+j) for j in range(deg)] for i in range(deg)],float)
    rhs=-np.array([moment(deg+i) for i in range(deg)],float)
    low=np.linalg.solve(G,rhs)
    c=np.concatenate([low,[1.0]])
    x=np.linspace(0,1,20001)
    q=sum(c[j]*x**j for j in range(len(c)))
    return c/np.max(np.abs(q))

def dpoly(c,x): return sum(j*c[j]*x**(j-1) for j in range(1,len(c)))

degs=list(range(3,9))
cs=[orth_poly(d) for d in degs]
# sensitivities of low moments to each null direction
S=np.zeros((3,len(cs)))
for k,c in enumerate(cs):
    for n in range(3): S[n,k]=sum(c[j]*moment(n+j) for j in range(len(c)))
# functional identity linearized residual R[q]=x(1-x)q'(x)
x=np.linspace(0.01,0.99,250)
R=np.column_stack([x*(1-x)*dpoly(c,x) for c in cs])
sv=np.linalg.svd(R,compute_uv=False)
rank=int(np.linalg.matrix_rank(R,tol=1e-10*sv[0]))
out={
 "test":"functional identity rank versus finite moment-null directions",
 "null_mode_degrees":degs,
 "max_abs_low_moment_sensitivity":float(np.max(np.abs(S))),
 "functional_collocation_shape":list(R.shape),
 "functional_singular_values":[float(v) for v in sv],
 "functional_rank":rank,
 "number_of_tested_null_modes":len(cs),
 "finite_low_moments_blind_to_modes":bool(np.max(np.abs(S))<1e-10),
 "functional_identity_full_rank_on_tested_nullspace":rank==len(cs),
 "conclusion":"Six independent polynomial continuum deformations that are invisible to m0,m1,m2 are linearly independent under a pointwise functional identity. A functional law can therefore supply infinitely many effective constraints across the continuum, unlike a finite moment checklist. This is an architectural fact, not evidence for this specific identity as QG dynamics."
}
Path('wave14_results').mkdir(exist_ok=True)
Path('wave14_results/functional_identity_rank.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
