#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from scipy.integrate import quad
from scipy.special import beta as B

a,b=1.7,2.4

def moment(n):
    v=1.0
    for j in range(n): v*= (a+j)/(a+b+j)
    return v
G=np.array([[moment(i+j) for j in range(3)] for i in range(3)],float)
rhs=-np.array([moment(3+i) for i in range(3)],float)
c0,c1,c2=np.linalg.solve(G,rhs)
coef=np.array([c0,c1,c2,1.0])
grid=np.linspace(0,1,20001)
q=sum(coef[j]*grid**j for j in range(4)); qmax=float(np.max(np.abs(q))); coefn=coef/qmax

def qn(x): return sum(coefn[j]*x**j for j in range(4))
def rho0(x): return x**(a-1)*(1-x)**(b-1)/B(a,b)
def F(eps,Q2):
    val,_=quad(lambda x: rho0(x)*(1+eps*qn(x))/(Q2+x),0,1,epsabs=2e-12,epsrel=2e-12,limit=300)
    return val

epss=[-0.8,0.0,0.8]
Q2s=[0.02,0.1,1.0,10.0]
records=[]
for eps in epss:
    records.append({"epsilon":eps,"F":[float(F(eps,Q2)) for Q2 in Q2s]})
widths=[]
for j in range(len(Q2s)):
    vv=[r['F'][j] for r in records]; widths.append(float(max(vv)-min(vv)))
out={
 "test":"nonlocal Stieltjes/dispersion holdouts resolve static spectral nullspace",
 "Q2":Q2s,
 "records":records,
 "holdout_widths":widths,
 "max_holdout_width":float(max(widths)),
 "nonlocal_holdouts_discriminate_static_nullspace":bool(max(widths)>1e-5),
 "conclusion":"Continuum deformations invisible to normalization and low moment/sum-rule constraints remain visible to nonlocal dispersive observables. A genuine parent equation must therefore predict such holdouts rather than merely satisfy finite static constraints."
}
Path('wave13_results').mkdir(exist_ok=True)
Path('wave13_results/stieltjes_dispersion_holdout.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
