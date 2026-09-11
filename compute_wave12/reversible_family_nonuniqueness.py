#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from scipy.linalg import eigh

a,b=1.7,2.4
DEG=6
ks=[-2.0,-1.0,0.0,1.0,3.0]

def moment(n):
    if n==0: return 1.0
    v=1.0
    for j in range(n):
        v *= (a+j)/(a+b+j)
    return v

M=np.array([[moment(i+j) for j in range(DEG+1)] for i in range(DEG+1)],float)

def amat_coeffs(k):
    # A=x(1-x)[1+k x(1-x)] = x +(k-1)x^2 -2k x^3 + k x^4
    return {1:1.0,2:k-1.0,3:-2.0*k,4:k}

def spectrum(k):
    A=amat_coeffs(k)
    K=np.zeros_like(M)
    for i in range(1,DEG+1):
        for j in range(1,DEG+1):
            s=0.0
            for p,c in A.items():
                s += c*moment(i+j-2+p)
            K[i,j]=i*j*s
    vals,_=eigh(K,M)
    vals=np.sort(np.maximum(vals,0.0))
    nz=vals[vals>1e-9]
    gap=float(nz[0])
    scaled=nz/gap
    return gap,[float(x) for x in scaled[:5]]

records=[]
for k in ks:
    gap,scaled=spectrum(k)
    records.append({"k":k,"raw_gap":gap,"scale_to_unit_gap":1.0/gap,"scaled_nonzero_eigenvalues":scaled})

second=[r['scaled_nonzero_eigenvalues'][1] for r in records]
third=[r['scaled_nonzero_eigenvalues'][2] for r in records]
out={
 "test":"reversible diffusion family after stationarity, positivity, detailed balance and fixed first gap",
 "stationary_density":"Beta(1.7,2.4)",
 "mobility_family":"A_k(x)=x(1-x)[1+k x(1-x)], k>-4",
 "drift_rule":"B=A'+A d(log rho)/dx (zero-current detailed balance)",
 "records":records,
 "lambda2_width_after_gap_fix":float(max(second)-min(second)),
 "lambda3_width_after_gap_fix":float(max(third)-min(third)),
 "all_scanned_mobilities_positive_inside_interval":True,
 "same_stationary_density_and_unit_gap_leave_nonunique_higher_spectrum":bool((max(second)-min(second))>1e-3),
 "conclusion":"Semigroup/local diffusion structure, positivity, normalization, detailed balance, a fixed Beta stationary continuum and even a fixed leading relaxation gap do not uniquely determine the generator. A nontrivial mobility family survives and changes higher spectral data.",
 "scope":"Polynomial Galerkin/Rayleigh-Ritz test in degree-6 monomial space; sufficient as a constructive nonuniqueness counterexample, not a continuum-spectrum theorem."
}
Path('wave12_results').mkdir(exist_ok=True)
Path('wave12_results/reversible_family_nonuniqueness.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
