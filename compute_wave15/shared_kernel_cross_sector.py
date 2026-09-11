#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from numpy.polynomial.legendre import leggauss
from scipy.optimize import root
from scipy.special import beta as B

a0,b0=1.7,2.4
N=500
z,w=leggauss(N); x=(z+1.0)/2.0; w=w/2.0
base=x**(a0-1)*(1-x)**(b0-1)/B(a0,b0)

def u(alpha,beta):
    g2=alpha*alpha/4.0+beta
    if g2>1e-12:
        g=np.sqrt(g2)
        return np.exp(alpha*x/2.0)*(np.cosh(g*x)+(alpha/(2*g))*np.sinh(g*x))
    if g2<-1e-12:
        g=np.sqrt(-g2)
        return np.exp(alpha*x/2.0)*(np.cos(g*x)+(alpha/(2*g))*np.sin(g*x))
    return np.exp(alpha*x/2.0)*(1+alpha*x/2.0)

def rho(alpha,beta):
    uu=u(alpha,beta)
    Z=np.sum(w*base*uu)
    return base*uu/Z

def moments(alpha,beta,nmax=8):
    r=rho(alpha,beta)
    return np.array([np.sum(w*r*x**n) for n in range(nmax+1)])

def F(alpha,beta,Q2):
    r=rho(alpha,beta)
    return float(np.sum(w*r/(Q2+x)))

p_true=np.array([-0.65,2.35])
m_true=moments(*p_true,8)
design=m_true[1:3]
sol=root(lambda p:moments(*p,2)[1:3]-design,[-0.4,2.0],tol=1e-12)
p_fit=sol.x
m_fit=moments(*p_fit,8)
Q2=[0.02,0.1,0.5,2.0,10.0]
F_true=np.array([F(*p_true,q) for q in Q2])
F_fit=np.array([F(*p_fit,q) for q in Q2])
# Low-energy Wilson/dispersion moment proxies are higher moments m3..m8, not used in fit.
wilson_true=m_true[3:9]
wilson_fit=m_fit[3:9]
out={
 "test":"one finite kernel realization closes spectral and dispersive/Wilson sectors",
 "kernel_equation":"u=1+alpha int_0^x u(y)dy + beta int_0^x (x-y)u(y)dy; rho proportional rho0*u",
 "true_parameters":[float(v) for v in p_true],
 "design_spectral_m1_m2":[float(v) for v in design],
 "recovered_parameters":[float(v) for v in p_fit],
 "root_success":bool(sol.success),
 "parameter_max_error":float(np.max(np.abs(p_fit-p_true))),
 "spectral_holdout_m3_to_m8_max_error":float(np.max(np.abs(wilson_fit-wilson_true))),
 "Q2":Q2,
 "dispersion_holdout_true":[float(v) for v in F_true],
 "dispersion_holdout_pred":[float(v) for v in F_fit],
 "dispersion_holdout_max_error":float(np.max(np.abs(F_fit-F_true))),
 "same_parameters_used_in_all_sectors":True,
 "shared_kernel_cross_sector_closure_demonstrated":bool(sol.success and np.max(np.abs(p_fit-p_true))<1e-8 and np.max(np.abs(F_fit-F_true))<1e-10),
 "candidate_new_physics":False,
 "conclusion":"Within a frozen synthetic kernel class, two spectral design moments identify the same two kernel parameters that then predict higher spectral/Wilson moments and nonlocal dispersive observables without sector-specific retuning. This validates the architecture of cross-sector closure, not the physical origin of the kernel."
}
Path('wave15_results').mkdir(exist_ok=True)
Path('wave15_results/shared_kernel_cross_sector.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
