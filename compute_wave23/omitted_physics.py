import numpy as np
from common import X_and_probes, sector_nuisance, omitted_g7, write_result

X,probes=X_and_probes(); g=omitted_g7(probes)
fit=X@np.linalg.lstsq(X,g,rcond=None)[0]
r=g-fit
frac=float(np.linalg.norm(r)/np.linalg.norm(g))
N=sector_nuisance(probes); A=np.column_stack([X,N])
fitn=A@np.linalg.lstsq(A,g,rcond=None)[0]
rn=g-fitn
fracn=float(np.linalg.norm(rn)/np.linalg.norm(g))
out={
 'test':'preregistered omitted seventh higher-momentum/helicity-shape detection',
 'g7_vector':g,
 'signal_only_residual_fraction':frac,
 'signal_plus_sector_nuisance_residual_fraction':fracn,
 'signal_only_residual_fraction_ge_0_05':frac>=0.05,
 'nuisance_aware_residual_fraction_ge_0_005':fracn>=0.005,
 'signal_fit_residual_norm':float(np.linalg.norm(r)),
 'nuisance_aware_residual_norm':float(np.linalg.norm(rn)),
 'conclusion':'A nonzero orthogonal residual means the frozen six-direction exam can flag at least this explicit omitted-shape challenge as out-of-class rather than exactly absorbing it into existing parameters/nuisances.'
}
write_result('omitted_physics',out)
