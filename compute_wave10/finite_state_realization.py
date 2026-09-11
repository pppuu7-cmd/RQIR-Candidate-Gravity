#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

x=np.array([0.1,0.3,0.7])
w=np.array([0.25,0.50,0.25])
m=np.array([np.sum(w*x**n) for n in range(16)])

# Direct finite-dimensional realization m_n = c^T A^n b.
A=np.diag(x)
b=np.ones(3)
c=w.copy()
mr=[]
for n in range(16):
    mr.append(float(c @ np.linalg.matrix_power(A,n) @ b))

# Hankel realization rank.
H=np.array([[m[i+j] for j in range(6)] for i in range(6)])
s=np.linalg.svd(H,compute_uv=False)
rank=int(np.sum(s>1e-12*s[0]))

# Characteristic polynomial roots give recurrence.
poly=np.poly(x) # z^3 + a2 z^2 + a1 z + a0
# x_i^3 = -a2 x_i^2 - a1 x_i - a0
rec=[-poly[3],-poly[2],-poly[1]] # coefficients on m_n,m_n+1,m_n+2
res=[]
for n in range(13):
    pred=rec[0]*m[n]+rec[1]*m[n+1]+rec[2]*m[n+2]
    res.append(float(pred-m[n+3]))

out={
 "test":"finite spectral recurrence as finite-dimensional linear realization",
 "state_dimension":3,
 "A_diagonal":x.tolist(),
 "b":b.tolist(),
 "c":c.tolist(),
 "direct_realization_max_error":float(np.max(np.abs(np.array(mr)-m))),
 "hankel_numeric_rank":rank,
 "hankel_singular_values":s.tolist(),
 "characteristic_polynomial":poly.tolist(),
 "recurrence_coefficients":rec,
 "recurrence_max_error":float(np.max(np.abs(res))),
 "finite_recurrence_equivalent_to_finite_rational_realization_in_proxy":True,
 "conclusion":"The rank-3 moment recurrence has an exact three-dimensional linear/rational realization. Thus adopting exact finite spectral rank implicitly selects a finite-dimensional realization class in this proxy; the state dimension is extra structural information unless derived.",
 "scope":"linear-system/moment realization identity; realization states need not be literal physical particles in a general QFT."
}
Path('wave10_results').mkdir(exist_ok=True)
Path('wave10_results/finite_state_realization.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
