import numpy as np
from common import write_result

# RQIR minimum-complexity discipline is a model-selection rule, not a physical law.
# Demonstrate that an L1/L2-type complexity objective uniquely prefers zero higher-order coefficients
# inside an allowed continuum even though the data/consistency gates do not force zero.
grid=np.linspace(-0.6,0.6,121)
allowed=[(c,d) for c in grid for d in grid if c*c+d*d<=0.36+1e-12]
def complexity(c,d): return abs(c)+abs(d)
vals=[(complexity(c,d),c,d) for c,d in allowed]
vals.sort()
best=vals[0]
near=[x for x in vals if x[0] <= best[0]+1e-12]
# pick two nonzero allowed alternatives with finite holdout effects
alts=[(-0.3,0.2),(0.25,-0.25)]
hold=[0.8*c-0.35*d for c,d in alts]
out={
 'test':'minimum-complexity selector versus physical determination',
 'allowed_disk_radius_squared':0.36,
 'number_allowed_grid_points':len(allowed),
 'complexity':'|c3|+|d3|',
 'minimum':{'complexity':float(best[0]),'c3':float(best[1]),'d3':float(best[2])},
 'number_grid_minimizers':len(near),
 'nonzero_allowed_examples':[{'c3':c,'d3':d,'holdout':h} for (c,d),h in zip(alts,hold)],
 'minimality_selects_zero_inside_proxy':abs(best[1])<1e-12 and abs(best[2])<1e-12,
 'minimality_is_not_equivalent_to_physical_constraint':True,
 'conclusion':'A simplicity objective can choose the Einstein-like zero-cubic point uniquely among an allowed family, but that choice is epistemic/model-selection discipline. It cannot be promoted to a microscopic law or evidence that the physical Wilson coefficients vanish.'
}
write_result('minimality_selector',out)
