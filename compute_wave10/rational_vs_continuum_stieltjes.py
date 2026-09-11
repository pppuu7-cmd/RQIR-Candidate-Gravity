#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from numpy.polynomial.legendre import leggauss

# Continuum Stieltjes transform for rho(x)=1 on [0,1]: F(Q2)=int_0^1 dx/(Q2+x)=log((Q2+1)/Q2).
Q2=np.logspace(-3,1,240)
F=np.log((Q2+1.0)/Q2)
records=[]
for r in [1,2,3,5,8,12,16]:
    z,wg=leggauss(r)
    x=(z+1.0)/2.0
    w=wg/2.0
    Fr=np.array([np.sum(w/(q+x)) for q in Q2])
    abs_err=np.abs(Fr-F)
    rel_err=abs_err/np.maximum(np.abs(F),1e-30)
    records.append({
      "atomic_rank":r,
      "max_abs_error":float(abs_err.max()),
      "max_rel_error":float(rel_err.max()),
      "abs_error_at_Q2_min":float(abs_err[0]),
      "abs_error_at_Q2_1_index":float(abs_err[np.argmin(np.abs(Q2-1.0))]),
      "pole_locations_minus_x":(-x).tolist()
    })

out={
 "test":"finite atomic/rational quadrature approximations to a genuine continuum Stieltjes transform",
 "continuum_transform":"F(Q^2)=log((Q^2+1)/Q^2)",
 "Q2_range":[float(Q2.min()),float(Q2.max())],
 "records":records,
 "finite_rank_can_approximate_continuum":True,
 "no_finite_rank_is_exact_for_full_continuum_transform":True,
 "analytic_structure_difference":"Each finite approximation is rational with finitely many simple poles; the exact continuum transform has logarithmic branch-point/cut structure after analytic continuation.",
 "conclusion":"Increasing finite atomic rank systematically approximates continuum Euclidean data, but no finite rational realization reproduces the exact continuum analytic structure. Excellent finite-data fits therefore do not establish exact finite spectral rank.",
 "scope":"uniform-density Stieltjes proxy using Gauss-Legendre quadrature; not a fit to a computed graviton spectrum."
}
Path('wave10_results').mkdir(exist_ok=True)
Path('wave10_results/rational_vs_continuum_stieltjes.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
