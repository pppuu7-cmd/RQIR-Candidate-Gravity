#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from scipy.optimize import brentq
from scipy.integrate import quad

def L(h):
    if abs(h)<1e-7:
        return h/3.0-h**3/45.0+2*h**5/945.0
    return 1.0/np.tanh(h)-1.0/h

lam=5.0
def eq(m): return m-L(lam*m)
mp=brentq(eq,1e-8,0.999999,xtol=1e-14)
roots=[-mp,0.0,mp]

def Z(m):
    h=lam*m
    if abs(h)<1e-12: return 1.0
    # x in [0,1], y=2x-1. integral_0^1 exp(h y) dx = sinh(h)/h
    return np.sinh(h)/h

def rho(x,m):
    y=2*x-1; h=lam*m
    return np.exp(h*y)/Z(m)
def obs(m):
    mean=quad(lambda x:(2*x-1)*rho(x,m),0,1,epsabs=1e-13,epsrel=1e-13)[0]
    second=quad(lambda x:(2*x-1)**2*rho(x,m),0,1,epsabs=1e-13,epsrel=1e-13)[0]
    F=quad(lambda x:rho(x,m)/(0.1+x),0,1,epsabs=1e-12,epsrel=1e-12)[0]
    return mean,second,F
records=[]
for m in roots:
    mean,second,F=obs(m)
    records.append({"m_root":m,"self_consistency_error":abs(mean-m),"second_moment":second,"stieltjes_Q2_0p1":F,"min_density_on_grid":float(min(rho(x,m) for x in np.linspace(0,1,1001)))})
out={
 "test":"nonlinear Fredholm/mean-field self-consistency can have multiple positive normalized solutions",
 "equation":"rho(x) proportional exp[lambda*m*(2x-1)], m=integral (2x-1)rho(x)dx",
 "lambda":lam,
 "roots":roots,
 "records":records,
 "number_of_positive_normalized_self_consistent_solutions":len(roots),
 "all_self_consistency_errors_small":all(r['self_consistency_error']<1e-10 for r in records),
 "multiple_solution_branches_exist":len(roots)>=3,
 "branch_holdout_spread":float(max(r['stieltjes_Q2_0p1'] for r in records)-min(r['stieltjes_Q2_0p1'] for r in records)),
 "conclusion":"A finite nonlinear self-consistency equation is not sufficient for predictive closure: above a bifurcation it can admit several positive normalized solutions with different nonlocal observables. A viable QG parent law therefore also needs a physical branch/solution-selection principle or a uniqueness theorem in the relevant domain."
}
Path('wave14_results').mkdir(exist_ok=True)
Path('wave14_results/fredholm_bifurcation_audit.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
