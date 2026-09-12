import numpy as np
from common import X_and_probes, sector_nuisance, projector_out, write_result

X,probes=X_and_probes(); N=sector_nuisance(probes)
drift=np.linspace(-1.0,1.0,len(probes)).reshape(-1,1)
A=np.column_stack([N,drift])
P=projector_out(A); Xp=P@X
sv=np.linalg.svd(Xp,compute_uv=False); rank=int(np.linalg.matrix_rank(Xp,tol=1e-10))
out={
 'test':'extended nuisance stress: sector normalizations plus centered linear probe-order drift',
 'nuisance_rank':int(np.linalg.matrix_rank(A,tol=1e-10)),
 'profiled_signal_rank':rank,
 'profiled_singular_values':sv,
 'profiled_min_singular_value':float(sv[-1]),
 'profiled_rank_6':rank==6,
 'profiled_min_sv_ge_0_03':float(sv[-1])>=0.03,
 'conclusion':'This stress test asks whether one additional coherent calibration/drift direction destroys the six-dimensional residual identifiability of the frozen exam.'
}
write_result('extended_nuisance',out)
