#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

OUT=Path("wave2_results")
OUT.mkdir(exist_ok=True)

# Finite causal/passive proxy for additional gravitational memory modes:
# chi_corr(omega) = sum_i w_i / (M_i^2 - omega^2 - i Gamma_i omega),
# with M_i^2>0, Gamma_i>0, w_i>=0. Each term has stable lower-half-plane poles.
# Low-frequency coefficients are linear in w. We fix normalization and two
# low-frequency real expansion moments, then optimize Re/Im response at finite omega.

M=np.array([1.0,1.5,2.2,3.3,5.0,8.0])
M2=M*M
Gamma=0.15*M
n=len(M)
wref=np.ones(n)/n

# chi(0)=sum w/M^2.
# Expand denominator inverse: 1/M^2 + i Gamma omega/M^4 + omega^2*(1/M^4-Gamma^2/M^6)+...
c0=1/M2
c1_im=Gamma/(M2*M2)
c2_re=1/(M2*M2)-(Gamma*Gamma)/(M2*M2*M2)

Aeq=np.vstack([np.ones(n),c0,c1_im,c2_re])
beq=np.array([1.0,float(c0@wref),float(c1_im@wref),float(c2_re@wref)])
rank=int(np.linalg.matrix_rank(Aeq,tol=1e-11))

records=[]
for omega in [0.2,0.5,0.8,1.2,2.0,4.0]:
    denom=M2-omega**2-1j*Gamma*omega
    basis=1/denom
    rec={"omega":omega}
    for part,name in [(basis.real,"Re"),(basis.imag,"Im")]:
        lo=linprog(part,A_eq=Aeq,b_eq=beq,bounds=[(0.0,None)]*n,method="highs")
        hi=linprog(-part,A_eq=Aeq,b_eq=beq,bounds=[(0.0,None)]*n,method="highs")
        if not (lo.success and hi.success):
            raise RuntimeError(f"retarded response LP failed omega={omega} {name}")
        rec[f"{name}_min"]=float(lo.fun)
        rec[f"{name}_max"]=float(-hi.fun)
        rec[f"{name}_width"]=float(-hi.fun-lo.fun)
    records.append(rec)

summary={
 "test":"causal passive massive-mode retarded response under fixed low-frequency data",
 "masses":[float(x) for x in M],
 "dampings":[float(x) for x in Gamma],
 "positive_residues":True,
 "fixed_constraints":["sum weights=1","chi_corr(0)","linear dissipative coefficient","quadratic dispersive coefficient"],
 "constraint_rank":rank,
 "affine_nullity":n-rank,
 "finite_frequency_ranges":records,
 "all_finite_frequency_parts_unique":all(r["Re_width"]<1e-10 and r["Im_width"]<1e-10 for r in records),
 "scope":"finite stable-pole causal/passive proxy; not a theorem for the full graviton retarded function"
}
(OUT/"causal_retarded_shape.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
