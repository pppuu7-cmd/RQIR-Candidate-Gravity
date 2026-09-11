#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

a,b=1.7,2.4

def moment(n):
    v=1.0
    for j in range(n): v*= (a+j)/(a+b+j)
    return v

# q3=x^3+c2 x^2+c1 x+c0 orthogonal to 1,x,x^2 under Beta weight
G=np.array([[moment(i+j) for j in range(3)] for i in range(3)],float)
rhs=-np.array([moment(3+i) for i in range(3)],float)
c0,c1,c2=np.linalg.solve(G,rhs)
coef=np.array([c0,c1,c2,1.0])
grid=np.linspace(0,1,20001)
q=sum(coef[j]*grid**j for j in range(4))
qmax=float(np.max(np.abs(q)))
coefn=coef/qmax
epss=[-0.8,-0.5,0.0,0.5,0.8]
records=[]
for eps in epss:
    fac=1+eps*sum(coefn[j]*grid**j for j in range(4))
    mm=[]
    for n in range(7):
        delta=sum(coefn[j]*moment(n+j) for j in range(4))
        mm.append(float(moment(n)+eps*delta))
    records.append({"epsilon":eps,"min_multiplier":float(fac.min()),"moments_m0_to_m6":mm})
base=records[2]['moments_m0_to_m6']
design=max(max(abs(r['moments_m0_to_m6'][n]-base[n]) for n in range(3)) for r in records)
m3=[r['moments_m0_to_m6'][3] for r in records]
out={
 "test":"positive continuum nullspace preserving unit weight, low moments, and endpoint exponents",
 "base_density":"Beta(1.7,2.4)",
 "deformation":"rho_e=rho_0[1+epsilon q3(x)] with q3 orthogonal to 1,x,x^2",
 "normalized_q3_coefficients_low_to_high":[float(v) for v in coefn],
 "records":records,
 "max_change_m0_m1_m2":float(design),
 "m3_width":float(max(m3)-min(m3)),
 "all_positive":all(r['min_multiplier']>0 for r in records),
 "endpoint_power_exponents_unchanged":True,
 "finite_static_constraints_leave_functional_null_direction":bool(design<1e-10 and max(m3)-min(m3)>1e-5),
 "conclusion":"Positivity, unit spectral weight, fixed endpoint power laws and two low spectral moments do not determine the continuum. A positive interior deformation can satisfy all of them exactly while changing higher data."
}
Path('wave13_results').mkdir(exist_ok=True)
Path('wave13_results/endpoint_sumrule_nullspace.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
