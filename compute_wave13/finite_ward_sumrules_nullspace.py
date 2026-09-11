#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

a,b=1.7,2.4

def moment(n):
    v=1.0
    for j in range(n): v*= (a+j)/(a+b+j)
    return v

# q5=x^5+sum_{j=0}^4 c_j x^j, orthogonal to degree <=4
G=np.array([[moment(i+j) for j in range(5)] for i in range(5)],float)
rhs=-np.array([moment(5+i) for i in range(5)],float)
cs=np.linalg.solve(G,rhs)
coef=np.concatenate([cs,[1.0]])
grid=np.linspace(0,1,30001)
q=sum(coef[j]*grid**j for j in range(6))
qmax=float(np.max(np.abs(q)))
coefn=coef/qmax
epss=[-0.75,-0.4,0.0,0.4,0.75]
records=[]
for eps in epss:
    fac=1+eps*sum(coefn[j]*grid**j for j in range(6))
    mm=[]
    for n in range(9):
        delta=sum(coefn[j]*moment(n+j) for j in range(6))
        mm.append(float(moment(n)+eps*delta))
    records.append({"epsilon":eps,"min_multiplier":float(fac.min()),"moments_m0_to_m8":mm})
base=records[2]['moments_m0_to_m8']
max_pres=max(max(abs(r['moments_m0_to_m8'][n]-base[n]) for n in range(5)) for r in records)
m5=[r['moments_m0_to_m8'][5] for r in records]
out={
 "test":"finite Ward/sum-rule constraints leave continuum nullspace",
 "constraint_proxy":"five independent linear spectral sum rules m0...m4",
 "normalized_q5_coefficients_low_to_high":[float(v) for v in coefn],
 "records":records,
 "max_change_constrained_m0_to_m4":float(max_pres),
 "m5_width":float(max(m5)-min(m5)),
 "all_positive":all(r['min_multiplier']>0 for r in records),
 "finite_number_of_sum_rules_not_functionally_complete":bool(max_pres<1e-9 and max(m5)-min(m5)>1e-6),
 "conclusion":"Even five exact independent linear sum rules plus positivity do not fix an infinite-dimensional continuum. An orthogonal positive deformation preserves all five constraints while changing the next and higher moments."
}
Path('wave13_results').mkdir(exist_ok=True)
Path('wave13_results/finite_ward_sumrules_nullspace.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
