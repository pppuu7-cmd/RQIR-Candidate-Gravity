#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Atomic positive measure: three support points -> moment Hankel rank saturates at 3.
x=np.array([0.1,0.3,0.7])
w=np.array([0.25,0.50,0.25])
m_atomic=np.array([np.sum(w*x**n) for n in range(24)])

# Genuine continuum proxy: uniform positive density on [0,1], moments m_n=1/(n+1).
# For any finite N, H_ij=int_0^1 x^(i+j) dx is the Hilbert Gram matrix and is strictly positive definite.
m_cont=np.array([1.0/(n+1) for n in range(24)])

def hankel(m,N):
    return np.array([[m[i+j] for j in range(N)] for i in range(N)],float)

def rec(m):
    out=[]
    for N in range(2,11):
        H=hankel(m,N)
        s=np.linalg.svd(H,compute_uv=False)
        ranks={str(t):int(np.sum(s>t*s[0])) for t in [1e-8,1e-10,1e-12,1e-14]}
        out.append({"N":N,"singular_values":s.tolist(),"numeric_rank_by_relative_tol":ranks,"determinant":float(np.linalg.det(H))})
    return out

out={
 "test":"finite atomic moment rank versus genuine continuum Hankel non-saturation",
 "atomic_support":x.tolist(),"atomic_weights":w.tolist(),
 "atomic_records":rec(m_atomic),
 "continuum_density":"rho(x)=1 on [0,1]",
 "continuum_records":rec(m_cont),
 "atomic_exact_rank":3,
 "continuum_exact_finite_N_rank_statement":"full rank for every finite N because H is the Gram matrix of monomials in L2([0,1],dx) with strictly positive density",
 "finite_atomic_rank_saturates":True,
 "positive_continuum_has_no_fixed_finite_Hankel_rank":True,
 "conclusion":"Exact finite Hankel-rank closure naturally describes finite discrete support in this moment proxy. A positive continuum instead gives strictly positive-definite Hankel matrices of every finite size, so its exact rank does not saturate at any fixed finite value.",
 "scope":"moment/Hankel structural test. Numerical Hilbert matrices become ill-conditioned at large N, so the continuum full-rank claim is analytic, not inferred solely from floating-point ranks."
}
Path('wave10_results').mkdir(exist_ok=True)
Path('wave10_results/atomic_vs_continuum_hankel.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
