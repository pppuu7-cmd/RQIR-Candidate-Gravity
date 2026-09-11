#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from numpy.polynomial.legendre import leggauss
from scipy.optimize import least_squares
from scipy.special import beta as B

a0,b0=1.7,2.4
N=450
z,w=leggauss(N); x=(z+1)/2; w=w/2
base=x**(a0-1)*(1-x)**(b0-1)/B(a0,b0)

def u(p):
    alpha,beta=p; g2=alpha*alpha/4+beta
    if g2>1e-12:
        g=np.sqrt(g2); return np.exp(alpha*x/2)*(np.cosh(g*x)+(alpha/(2*g))*np.sinh(g*x))
    if g2<-1e-12:
        g=np.sqrt(-g2); return np.exp(alpha*x/2)*(np.cos(g*x)+(alpha/(2*g))*np.sin(g*x))
    return np.exp(alpha*x/2)*(1+alpha*x/2)
def rho(p):
    uu=u(p); return base*uu/np.sum(w*base*uu)
def spec(p):
    r=rho(p); return np.array([np.sum(w*r*x),np.sum(w*r*x*x)])
def disp(p):
    r=rho(p); return np.array([np.sum(w*r/(0.1+x)),np.sum(w*r/(1.0+x))])

p_spec=np.array([-0.65,2.35])
p_disp=np.array([-1.15,3.10])
y_spec=spec(p_spec); y_disp=disp(p_disp)
# Unlinked sector fits are exact by construction.
unlinked_residual=0.0
# Force a same-realization parameter pair across all four design data.
y=np.r_[y_spec,y_disp]
def res(p): return np.r_[spec(p),disp(p)]-y
sol=least_squares(res,[-0.8,2.6],xtol=1e-14,ftol=1e-14,gtol=1e-14,max_nfev=4000)
r=res(sol.x)
out={
 "test":"same-realization gate rejects sector-wise scheme/parameter switching",
 "spectral_source_parameters":[float(v) for v in p_spec],
 "dispersion_source_parameters":[float(v) for v in p_disp],
 "spectral_design":[float(v) for v in y_spec],
 "dispersion_design":[float(v) for v in y_disp],
 "unlinked_sector_fit_max_residual":unlinked_residual,
 "best_shared_parameters":[float(v) for v in sol.x],
 "shared_fit_residuals":[float(v) for v in r],
 "shared_fit_max_abs_residual":float(np.max(np.abs(r))),
 "shared_fit_l2_residual":float(np.linalg.norm(r)),
 "optimizer_success":bool(sol.success),
 "sector_switching_can_fake_individual_closure":True,
 "same_realization_gate_detects_inconsistency":bool(np.max(np.abs(r))>1e-4),
 "conclusion":"If spectral and dispersive sectors are allowed different parameter realizations, each can close independently even when no single kernel realization explains both. Enforcing the same parameters across sectors exposes this hidden inconsistency and blocks scheme/realization switching as a false closure mechanism."
}
Path('wave15_results').mkdir(exist_ok=True)
Path('wave15_results/same_realization_consistency.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
