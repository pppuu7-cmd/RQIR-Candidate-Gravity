#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from numpy.polynomial.legendre import legval

# Base continuum rho0(x)=1 on [0,1]. Add shifted Legendre P3(2x-1), orthogonal to polynomials degree <=2.
# This keeps m0,m1,m2 exactly fixed while changing m3 and above.
N=20001
x=np.linspace(0.0,1.0,N)
t=2*x-1
# P3(t)=(5t^3-3t)/2
P3=0.5*(5*t**3-3*t)
records=[]
for eps in [-0.8,-0.5,-0.2,0.0,0.2,0.5,0.8]:
    rho=1.0+eps*P3
    moments=[]
    for n in range(7):
        moments.append(float(np.trapz(rho*x**n,x)))
    records.append({"epsilon":eps,"rho_min":float(rho.min()),"moments_m0_to_m6":moments})
base=records[3]['moments_m0_to_m6']
max_design_delta=max(max(abs(r['moments_m0_to_m6'][n]-base[n]) for n in range(3)) for r in records)
m3_width=max(r['moments_m0_to_m6'][3] for r in records)-min(r['moments_m0_to_m6'][3] for r in records)

out={
 "test":"same finite low moments, different positive continuum generators/densities",
 "deformation":"rho_e(x)=1+epsilon P3(2x-1)",
 "records":records,
 "max_abs_change_in_m0_m1_m2":max_design_delta,
 "m3_width_across_positive_family":m3_width,
 "positive_for_all_scanned_epsilon":all(r['rho_min']>=-1e-12 for r in records),
 "finite_low_moments_do_not_derive_generator":m3_width>1e-4 and max_design_delta<1e-7,
 "conclusion":"Even exact agreement of normalization and the first two nontrivial moments does not determine a continuum generator. Positive deformations orthogonal to the fitted moment subspace can leave m0-m2 unchanged while shifting m3 and all higher data. The generator equation must therefore come from an independent physical principle, not from low-moment fitting alone.",
 "scope":"shifted-Legendre positive-density counterexample; numerical quadrature proxy with analytically motivated orthogonality."
}
Path('wave11_results').mkdir(exist_ok=True)
Path('wave11_results/low_moment_generator_nonuniqueness.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
