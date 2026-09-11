#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from numpy.polynomial.legendre import leggauss
from scipy.special import beta as B

a0,b0=1.7,2.4
N=450
z,w=leggauss(N); x=(z+1)/2; w=w/2
base=x**(a0-1)*(1-x)**(b0-1)/B(a0,b0)

def u(p):
    alpha,beta=p
    g2=alpha*alpha/4+beta
    if g2>1e-12:
        g=np.sqrt(g2); return np.exp(alpha*x/2)*(np.cosh(g*x)+(alpha/(2*g))*np.sinh(g*x))
    if g2<-1e-12:
        g=np.sqrt(-g2); return np.exp(alpha*x/2)*(np.cos(g*x)+(alpha/(2*g))*np.sin(g*x))
    return np.exp(alpha*x/2)*(1+alpha*x/2)

def rho(p):
    uu=u(p); return base*uu/np.sum(w*base*uu)
def obs_spec(p):
    r=rho(p); return np.array([np.sum(w*r*x),np.sum(w*r*x*x)])
def F(p,Q2): return float(np.sum(w*rho(p)/(Q2+x)))

def jac(fun,p,h=1e-5):
    p=np.array(p,float); y0=np.atleast_1d(fun(p)); J=np.zeros((len(y0),len(p)))
    for j in range(len(p)):
        d=np.zeros_like(p); d[j]=h
        J[:,j]=(np.atleast_1d(fun(p+d))-np.atleast_1d(fun(p-d)))/(2*h)
    return J

p=np.array([-0.65,2.35])
# Shared: all three design observables depend on the same two parameters.
Jshared=jac(lambda pp:np.r_[obs_spec(pp),F(pp,0.3)],p)
svs=np.linalg.svd(Jshared,compute_uv=False)
rank_shared=int(np.linalg.matrix_rank(Jshared,tol=1e-10*svs[0]))
null_shared=2-rank_shared
# Unlinked: spectral has its own p_s, dispersion its own p_d.
def unlinked(v):
    ps=v[:2]; pd=v[2:]
    return np.r_[obs_spec(ps),F(pd,0.3)]
v=np.r_[p,p]
Jun=jac(unlinked,v)
U,S,Vh=np.linalg.svd(Jun,full_matrices=True)
rank_un=int(np.linalg.matrix_rank(Jun,tol=1e-10*S[0]))
null_un=4-rank_un
nv=Vh[-1]; nv=nv/np.linalg.norm(nv)
# Sign is irrelevant. Scan a modest distance along the design-null direction.
tvals=np.linspace(-0.35,0.35,15)
hold=[]; design_drift=[]
base_design=unlinked(v)
for t in tvals:
    vv=v+t*nv
    hold.append(F(vv[2:],0.02))
    design_drift.append(float(np.max(np.abs(unlinked(vv)-base_design))))
out={
 "test":"cross-sector parameter sharing removes an unlinked design null direction",
 "shared_design_jacobian":Jshared.tolist(),
 "shared_singular_values":[float(q) for q in svs],
 "shared_parameter_rank":rank_shared,
 "shared_parameter_nullity":null_shared,
 "unlinked_design_jacobian":Jun.tolist(),
 "unlinked_singular_values":[float(q) for q in S],
 "unlinked_parameter_rank":rank_un,
 "unlinked_parameter_nullity":null_un,
 "unlinked_null_vector":[float(q) for q in nv],
 "linear_null_scan_max_design_drift":float(max(design_drift)),
 "unlinked_holdout_F_Q2_0p02_width":float(max(hold)-min(hold)),
 "shared_model_removes_parameter_nullity":bool(null_shared==0 and null_un>=1),
 "unlinked_null_direction_changes_holdout":bool(max(hold)-min(hold)>1e-4),
 "conclusion":"Reusing one kernel realization across spectral and dispersive sectors removes a parameter direction that survives when the two sectors are allowed independent kernel copies. The remaining unlinked direction is nearly invisible to the design observables but changes a prospective low-Q^2 dispersive holdout."
}
Path('wave15_results').mkdir(exist_ok=True)
Path('wave15_results/unlinked_vs_shared_kernel_rank.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
