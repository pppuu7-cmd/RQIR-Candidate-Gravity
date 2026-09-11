#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Positive symmetric circulant 4-state transfer matrix.
# First row [a,b,c,b], eigenvalues: 1, lambda1 (double), lambda2.
# Fix the leading nontrivial eigenvalue lambda1 -> same long-distance correlation length,
# while lambda2 remains microscopic freedom consistent with positivity.
lambda1=0.4
lambda2_values=np.linspace(-0.19,0.95,24)
records=[]
for lam2 in lambda2_values:
    a=(1+lam2+2*lambda1)/4
    c=(1+lam2-2*lambda1)/4
    b=(1-lam2)/4
    T=np.array([[a,b,c,b],[b,a,b,c],[c,b,a,b],[b,c,b,a]],float)
    eig=np.sort(np.linalg.eigvalsh(T))[::-1]
    positive_entries=bool(np.min(T)>=-1e-12)
    row_error=float(np.max(np.abs(T.sum(axis=1)-1)))
    # Same asymptotic correlation length from lambda1, but finite-step return probabilities differ.
    p2=float(np.linalg.matrix_power(T,2)[0,0])
    p4=float(np.linalg.matrix_power(T,4)[0,0])
    records.append({"lambda2":float(lam2),"a":float(a),"b":float(b),"c":float(c),"positive_entries":positive_entries,"row_error":row_error,"eigenvalues":eig.tolist(),"return_p2":p2,"return_p4":p4})

p2s=[r['return_p2'] for r in records if r['positive_entries']]
p4s=[r['return_p4'] for r in records if r['positive_entries']]
xi=-1.0/np.log(lambda1)
out={
 "test":"same infrared transfer eigenvalue, different microscopic positive transfer rules",
 "fixed_leading_nontrivial_eigenvalue":lambda1,
 "correlation_length_proxy":float(xi),
 "admissible_family_size":sum(1 for r in records if r['positive_entries']),
 "return_p2_width":float(max(p2s)-min(p2s)),
 "return_p4_width":float(max(p4s)-min(p4s)),
 "microscopic_lambda2_range":[float(min(lambda2_values)),float(max(lambda2_values))],
 "records":records,
 "unique_uv_rule_from_ir_gap":False,
 "conclusion":"Fixing the dominant transfer eigenvalue/correlation length does not select a unique positive microscopic transfer matrix. A nonperturbative state/path-integral proposal therefore needs an independent measure/state-selection rule, not only the correct IR spectrum.",
 "scope":"finite-state transfer-matrix universality proxy, not a gravitational lattice path integral"
}
Path('wave6_results').mkdir(exist_ok=True)
Path('wave6_results/transfer_matrix_uv_degeneracy.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
