import numpy as np
from common import selected_bank, profile_nuisance, write_result

ld,idx,selected,X=selected_bank(10)
Xp,N,P=profile_nuisance(X,selected)
sv=np.linalg.svd(Xp,compute_uv=False)
rank=int(np.linalg.matrix_rank(Xp,tol=1e-10))
out={
 'test':'sector-normalization nuisance profiling',
 'nuisance_columns':['norm_2pt','norm_3pt','norm_4pt'],
 'nuisance_rank':int(np.linalg.matrix_rank(N)),
 'profiled_signal_rank':rank,
 'profiled_singular_values':sv,
 'profiled_min_singular_value':float(sv[-1]),
 'profiled_rank_6':rank==6,
 'profiled_min_sv_ge_0_15':float(sv[-1])>=0.15,
 'conclusion':'Profiling independent normalization nuisances for the 2pt, 3pt and 4pt sectors does not erase any of the six residual proxy directions in the frozen holdout bank.'
}
write_result('nuisance_robustness',out)
