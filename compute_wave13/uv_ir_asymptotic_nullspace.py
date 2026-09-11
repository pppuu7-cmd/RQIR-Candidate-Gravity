#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
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

def qn_x(x): return sum(coefn[j]*x**j for j in range(4))
def rho_s(s,eps):
    x=s/(1+s)
    rho_x=x**(a-1)*(1-x)**(b-1)/B(a,b)*(1+eps*qn_x(x))
    return rho_x/(1+s)**2

def slope(eps,s1,s2):
    r1,r2=rho_s(s1,eps),rho_s(s2,eps)
    return float(np.log(r2/r1)/np.log(s2/s1))
records=[]
for eps in [-0.8,0.0,0.8]:
    records.append({
      "epsilon":eps,
      "IR_log_slope_1e-8_to_1e-5":slope(eps,1e-8,1e-5),
      "UV_log_slope_1e5_to_1e8":slope(eps,1e5,1e8)
    })
ir=[r['IR_log_slope_1e-8_to_1e-5'] for r in records]
uv=[r['UV_log_slope_1e5_to_1e8'] for r in records]
out={
 "test":"IR/UV power-law asymptotics do not remove interior continuum nullspace",
 "map":"s=x/(1-x), giving beta-prime-type continuum on s in (0,infinity)",
 "expected_IR_exponent":a-1,
 "expected_UV_exponent":-(b+1),
 "records":records,
 "IR_slope_width":float(max(ir)-min(ir)),
 "UV_slope_width":float(max(uv)-min(uv)),
 "same_asymptotic_exponents_across_deformations":bool(max(ir)-min(ir)<5e-4 and max(uv)-min(uv)<5e-4),
 "conclusion":"Fixing threshold/IR and ultraviolet power-law exponents constrains only endpoint behavior. Positive interior spectral deformations can preserve both asymptotic exponents while changing finite-energy spectral and dispersive data."
}
Path('wave13_results').mkdir(exist_ok=True)
Path('wave13_results/uv_ir_asymptotic_nullspace.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
