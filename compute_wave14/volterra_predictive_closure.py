#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import beta as B

a,b=1.7,2.4

def rho0(x): return x**(a-1)*(1-x)**(b-1)/B(a,b)
def u(x,lam):
    if abs(lam)<1e-14: return 1.0
    if lam>0: return np.cosh(np.sqrt(lam)*x)
    return np.cos(np.sqrt(-lam)*x)
def norm(lam): return quad(lambda x: rho0(x)*u(x,lam),0,1,epsabs=2e-12,epsrel=2e-12,limit=300)[0]
def mom(n,lam):
    z=norm(lam)
    return quad(lambda x: x**n*rho0(x)*u(x,lam)/z,0,1,epsabs=2e-12,epsrel=2e-12,limit=300)[0]
def F(Q2,lam):
    z=norm(lam)
    return quad(lambda x: rho0(x)*u(x,lam)/z/(Q2+x),0,1,epsabs=2e-12,epsrel=2e-12,limit=300)[0]

lam_true=2.2
m1_design=mom(1,lam_true)
lam_fit=brentq(lambda L:mom(1,L)-m1_design,0.0,8.0,xtol=1e-13)
hold_m=[mom(n,lam_true) for n in range(2,8)]
pred_m=[mom(n,lam_fit) for n in range(2,8)]
Q2s=[0.02,0.1,1.0,10.0]
hold_F=[F(q,lam_true) for q in Q2s]
pred_F=[F(q,lam_fit) for q in Q2s]
# Volterra equation u=1+lambda integral_0^x (x-y)u(y)dy, analytic solution cosh(sqrt(lambda)x)
pts=np.linspace(0,1,21)
res=[]
for xx in pts:
    integ=quad(lambda y:(xx-y)*u(y,lam_fit),0,xx,epsabs=1e-13,epsrel=1e-13)[0]
    res.append(abs(u(xx,lam_fit)-(1+lam_fit*integ)))
out={
 "test":"finite causal Volterra law with one design datum and prospective holdouts",
 "equation":"u(x)=1+lambda integral_0^x (x-y)u(y)dy; rho proportional rho0*u",
 "true_lambda":lam_true,
 "design_m1":m1_design,
 "recovered_lambda":lam_fit,
 "lambda_error":abs(lam_fit-lam_true),
 "moment_holdout_max_error":float(max(abs(x-y) for x,y in zip(hold_m,pred_m))),
 "Q2":Q2s,
 "stieltjes_holdout_max_error":float(max(abs(x-y) for x,y in zip(hold_F,pred_F))),
 "volterra_residual_max":float(max(res)),
 "unique_linear_volterra_second_kind_for_declared_kernel":True,
 "finite_equation_predictive_closure_demonstrated":bool(abs(lam_fit-lam_true)<1e-9 and max(res)<1e-10),
 "candidate_new_physics":False,
 "conclusion":"A finite causal Volterra equation can uniquely generate a positive continuum and turn one design observable into many moment and nonlocal holdout predictions. This demonstrates the needed architecture, but the kernel was chosen synthetically and therefore supplies no QG novelty by itself."
}
Path('wave14_results').mkdir(exist_ok=True)
Path('wave14_results/volterra_predictive_closure.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
