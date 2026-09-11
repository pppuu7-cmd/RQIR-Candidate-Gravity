#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from numpy.polynomial.legendre import leggauss
from scipy.special import beta as B

a0,b0=1.7,2.4
N=600
z,w=leggauss(N); x=(z+1)/2; w=w/2
base=x**(a0-1)*(1-x)**(b0-1)/B(a0,b0)
p=np.array([-0.65,2.35])

def u(p):
    alpha,beta=p; g2=alpha*alpha/4+beta
    if g2>1e-12:
        g=np.sqrt(g2); return np.exp(alpha*x/2)*(np.cosh(g*x)+(alpha/(2*g))*np.sinh(g*x))
    if g2<-1e-12:
        g=np.sqrt(-g2); return np.exp(alpha*x/2)*(np.cos(g*x)+(alpha/(2*g))*np.sin(g*x))
    return np.exp(alpha*x/2)*(1+alpha*x/2)
rr=base*u(p); rr=rr/np.sum(w*rr)

def m(n): return float(np.sum(w*rr*x**n))
# q3=x^3+c2 x^2+c1 x+c0 orthogonal to 1,x,x^2 under the actual shared-kernel density.
G=np.array([[m(i+j) for j in range(3)] for i in range(3)])
rhs=-np.array([m(3+i) for i in range(3)])
c0,c1,c2=np.linalg.solve(G,rhs); c=np.array([c0,c1,c2,1.0])
q=sum(c[j]*x**j for j in range(4)); c=c/np.max(np.abs(q)); q=sum(c[j]*x**j for j in range(4))

def obs(eps):
    r=rr*(1+eps*q); r=r/np.sum(w*r)
    mm=[float(np.sum(w*r*x**n)) for n in range(7)]
    F=[float(np.sum(w*r/(Q+x))) for Q in [0.02,0.1,1.0,10.0]]
    return mm,F,float(np.min(1+eps*q))
records=[]
for eps in [-0.8,-0.4,0,0.4,0.8]:
    mm,F,mn=obs(eps); records.append({"epsilon":eps,"moments_m0_to_m6":mm,"F":F,"min_multiplier":mn})
base_rec=records[2]
design=max(max(abs(r['moments_m0_to_m6'][n]-base_rec['moments_m0_to_m6'][n]) for n in range(3)) for r in records)
widthF=[]
for j in range(4):
    vals=[r['F'][j] for r in records]; widthF.append(float(max(vals)-min(vals)))
m3=[r['moments_m0_to_m6'][3] for r in records]
out={
 "test":"effective kernel-output deformation invisible to spectral design but exposed by cross-sector holdouts",
 "deformation":"rho_e proportional rho_shared*(1+epsilon*q3), q3 orthogonal to 1,x,x^2 under rho_shared",
 "q3_coefficients_low_to_high":[float(v) for v in c],
 "records":records,
 "max_design_change_m0_m1_m2":float(design),
 "m3_width":float(max(m3)-min(m3)),
 "Q2":[0.02,0.1,1.0,10.0],
 "dispersion_holdout_widths":widthF,
 "max_dispersion_holdout_width":float(max(widthF)),
 "all_positive":all(r['min_multiplier']>0 for r in records),
 "spectral_design_null_is_seen_cross_sector":bool(design<1e-10 and max(widthF)>1e-4),
 "conclusion":"A positive deformation can be exactly invisible to the spectral design moments while changing higher/Wilson moments and nonlocal dispersion observables. Cross-sector holdouts therefore provide genuine information against output/kernel directions left unconstrained by the spectral design alone."
}
Path('wave15_results').mkdir(exist_ok=True)
Path('wave15_results/kernel_null_perturbation_holdout.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
