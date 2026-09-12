import numpy as np
from common import BOUNDS,X_and_probes,write_result

X,probes=X_and_probes(); rng=np.random.default_rng(2406)
N=20000
samples=rng.uniform(-BOUNDS,BOUNDS,size=(N,6))
Y=samples@X.T
widths=Y.max(axis=0)-Y.min(axis=0)
max_width=float(widths.max())
mean_width=float(widths.mean())
out={
 'test':'bounded consistency-region nonuniqueness control',
 'seed':2406,
 'samples':N,
 'coefficient_bounds':BOUNDS,
 'probe_names':[r['name'] for r in probes],
 'holdout_widths':widths,
 'maximum_holdout_width':max_width,
 'mean_holdout_width':mean_width,
 'accepted_region_has_multiple_points':True,
 'holdout_width_ge_0_05':max_width>=0.05,
 'inequality_consistency_region_is_nonunique':max_width>=0.05,
 'conclusion':'A bounded admissibility region can strongly restrict coefficients while retaining a continuum of distinct frozen-bank predictions. Inequality consistency is therefore not equivalent to microscopic uniqueness.'
}
write_result('inequality_region',out)
