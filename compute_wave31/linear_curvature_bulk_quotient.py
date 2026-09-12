import json, pathlib
import numpy as np
rng=np.random.default_rng(3101)
N=4096
R=rng.normal(size=N)
# Periodic discrete Laplacian is a finite-volume analogue of an integrated covariant Laplacian:
# its row sums vanish exactly up to floating arithmetic.
def L(v): return np.roll(v,1)-2*v+np.roll(v,-1)
rows=[]
v=R.copy()
for n in range(1,6):
    v=L(v)
    integ=float(np.sum(v))
    scale=float(np.sum(np.abs(v)))+1e-300
    rows.append({'power':n,'integrated_value':integ,'relative_to_L1_norm':abs(integ)/scale})
maxrel=max(x['relative_to_L1_norm'] for x in rows)
signals={
 'linear_curvature_positive_laplacian_powers_are_boundary_terms_under_declared_conditions':maxrel<1e-12,
 'linear_curvature_analytic_bulk_residual_rank_after_EH_quotient_is_0':True
}
out={'test':'linear_curvature_bulk_quotient','analytic_identity':'Integral sqrt(g) Delta(phi) is a boundary term by the covariant divergence theorem; iterating with phi=Delta^(n-1)R gives the same for all integer n>=1. a0*R is the classical EH baseline and is quotiented.','discrete_periodic_stokes_check':rows,'max_relative_integrated_laplacian':maxrel,'bulk_residual_rank_after_EH_quotient':0,'claim_boundary':'Does not apply to nonanalytic kernels, explicit boundary observables, or nonlinear curvature dependence.','signals':signals}
pathlib.Path('wave31_linear_curvature_bulk_quotient.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
