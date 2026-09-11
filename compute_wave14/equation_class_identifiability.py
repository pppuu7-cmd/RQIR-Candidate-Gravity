#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from numpy.polynomial.legendre import leggauss
from scipy.optimize import root
from scipy.special import beta as B

a,b=1.7,2.4
N=400
z,w=leggauss(N); x=(z+1)/2; w=w/2
base=x**(a-1)*(1-x)**(b-1)/B(a,b)

def evaluate(mult):
    Z=np.sum(w*base*mult)
    m=[np.sum(w*base*mult*x**n)/Z for n in [1,2,3]]
    Q=[0.02,0.1,1.0,10.0]
    F=[np.sum(w*base*mult/(q+x))/Z for q in Q]
    return np.array(m),np.array(F),float(Z)

# Class A: local first-order log-density equation with affine derivative.
theta1,theta2=-1.0,1.5
multA=np.exp(theta1*x+theta2*x*x)
mA,FA,ZA=evaluate(multA)

# Class B: causal two-parameter Volterra equation
# u=1+alpha int_0^x u(y)dy+beta int_0^x (x-y)u(y)dy
# => u''=alpha u'+beta u, u(0)=1, u'(0)=alpha.
def uB(alpha,beta):
    g2=alpha*alpha/4+beta
    if g2>1e-12:
        g=np.sqrt(g2)
        return np.exp(alpha*x/2)*(np.cosh(g*x)+(alpha/(2*g))*np.sinh(g*x))
    if g2<-1e-12:
        g=np.sqrt(-g2)
        return np.exp(alpha*x/2)*(np.cos(g*x)+(alpha/(2*g))*np.sin(g*x))
    return np.exp(alpha*x/2)*(1+alpha*x/2)

def residual(p):
    m,_,_=evaluate(uB(p[0],p[1]))
    return m[:2]-mA[:2]
sol=root(residual,[-1.4,4.0],tol=1e-11)
alpha,beta=sol.x
multB=uB(alpha,beta)
mB,FB,ZB=evaluate(multB)
Q=[0.02,0.1,1.0,10.0]
out={
 "test":"different finite equation classes fit same two design observables but disagree on holdouts",
 "class_A":{"law":"d log(rho/rho0)/dx=theta1+2 theta2 x","theta1":theta1,"theta2":theta2},
 "class_B":{"law":"u=1+alpha int u + beta int (x-y)u; rho proportional rho0*u","alpha":float(alpha),"beta":float(beta),"root_success":bool(sol.success)},
 "design_m1_m2_class_A":[float(v) for v in mA[:2]],
 "design_m1_m2_class_B":[float(v) for v in mB[:2]],
 "design_max_mismatch":float(np.max(np.abs(mA[:2]-mB[:2]))),
 "m3_class_A":float(mA[2]),
 "m3_class_B":float(mB[2]),
 "m3_difference":float(abs(mA[2]-mB[2])),
 "Q2":Q,
 "stieltjes_class_A":[float(v) for v in FA],
 "stieltjes_class_B":[float(v) for v in FB],
 "stieltjes_max_difference":float(np.max(np.abs(FA-FB))),
 "minimum_multiplier_class_B":float(np.min(multB)),
 "two_design_observables_do_not_identify_equation_class":bool(sol.success and np.max(np.abs(mA[:2]-mB[:2]))<1e-9 and np.max(np.abs(FA-FB))>1e-4),
 "conclusion":"Two structurally different finite continuum-generating equation classes can be tuned to the same two low moments while making distinct higher-moment and nonlocal dispersive predictions. Therefore equation-class selection itself must come from independent physics and/or stronger prospective holdouts, not from successful closure on the design observables."
}
Path('wave14_results').mkdir(exist_ok=True)
Path('wave14_results/equation_class_identifiability.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
