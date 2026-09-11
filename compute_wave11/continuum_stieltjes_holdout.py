#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from scipy.special import roots_jacobi, beta as beta_fn
from scipy.optimize import least_squares

# Same Beta(a,b) continuum family, now tested on an integral observable (Stieltjes transform)
# after fitting only low moments.
a_true,b_true=1.7,2.4

def moment(n,a,b):
    out=1.0
    for k in range(n): out *= (a+k)/(a+b+k)
    return out
m1,m2=moment(1,a_true,b_true),moment(2,a_true,b_true)

def res(z):
    a,b=np.exp(z)
    return [moment(1,a,b)-m1,moment(2,a,b)-m2]
fit=least_squares(res,np.log([1.2,1.8]),xtol=1e-14,ftol=1e-14,gtol=1e-14)
a_fit,b_fit=np.exp(fit.x)

# Gauss-Jacobi quadrature for integral of x^(a-1)(1-x)^(b-1)/(B(a,b)(Q2+x)).
def stieltjes(Q2,a,b,N=120):
    # t in [-1,1], x=(t+1)/2; weight (1-t)^(b-1)(1+t)^(a-1)
    t,w=roots_jacobi(N,b-1,a-1)
    x=(t+1.0)/2.0
    pref=2.0**(-(a+b-1))/beta_fn(a,b)
    return float(pref*np.sum(w/(Q2+x)))

Q2s=[0.02,0.05,0.2,1.0,4.0,20.0]
records=[]
for q in Q2s:
    tru=stieltjes(q,a_true,b_true)
    pred=stieltjes(q,a_fit,b_fit)
    records.append({"Q2":q,"true":tru,"predicted":pred,"abs_error":abs(pred-tru)})

out={
 "test":"finite continuum generator predicts untouched integral/Stieltjes observables",
 "design_inputs":{"m1":m1,"m2":m2},
 "recovered_parameters":[float(a_fit),float(b_fit)],
 "holdout_records":records,
 "holdout_max_abs_error":max(r['abs_error'] for r in records),
 "integral_holdouts_pass":max(r['abs_error'] for r in records)<1e-10,
 "conclusion":"Within a specified finite continuum generator family, two low-moment design inputs determine the generator parameters and predict nonlocal integral observables over a wide Q^2 range. This is the correct validation architecture for a continuum parent law, but the family itself still needs an independent physical derivation.",
 "scope":"Beta continuum / Gauss-Jacobi quadrature proxy, not a graviton propagator fit."
}
Path('wave11_results').mkdir(exist_ok=True)
Path('wave11_results/continuum_stieltjes_holdout.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
