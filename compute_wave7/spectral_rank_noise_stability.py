#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

rng=np.random.default_rng(20260912)
x=np.array([0.18,0.47,0.83])
w=np.array([0.22,0.51,0.27])
# Moments m_0...m_8 for a rank-3 atomic measure.
m=np.array([np.sum(w*x**n) for n in range(9)])

def hankel(mv, n=5):
    H=np.empty((n,n),float)
    for i in range(n):
        for j in range(n):
            H[i,j]=mv[i+j]
    return H

H0=hankel(m,5)
s0=np.linalg.svd(H0,compute_uv=False)
records=[]
for sigma in [0.0,1e-12,1e-10,1e-8,1e-6,1e-4]:
    mv=m.copy()
    if sigma>0:
        mv=mv + rng.normal(0,sigma,size=mv.shape)
    s=np.linalg.svd(hankel(mv,5),compute_uv=False)
    est={}
    for tol in [1e-12,1e-10,1e-8,1e-6,1e-4]:
        est[str(tol)]=int(np.sum(s>tol*s[0]))
    records.append({"noise_sigma":sigma,"singular_values":s.tolist(),"estimated_rank_by_relative_tol":est})

out={
 "test":"operational robustness of exact finite spectral rank",
 "exact_singular_values":s0.tolist(),
 "noise_records":records,
 "exact_atomic_rank":3,
 "rank_is_threshold_dependent_under_noise":True,
 "conclusion":"Exact finite Hankel rank is a strong algebraic closure condition, but arbitrarily small measurement/model noise makes numerical rank depend on a threshold. A physical finite-rank principle therefore needs an exact structural derivation, not merely a fit to noisy finite moments.",
 "scope":"finite atomic moment proxy; not an experimental error model for graviton spectroscopy"
}
Path('wave7_results').mkdir(exist_ok=True)
Path('wave7_results/spectral_rank_noise_stability.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
