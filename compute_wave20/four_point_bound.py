import numpy as np
from common import write_result

# Logical dispersive/positivity proxy motivated by amplitude-EFT bounds that constrain an R^3-like
# cubic coefficient using higher-order/four-graviton data. We do NOT use published numerical constants.
# Admissibility surrogate: c3^2 <= c4, with c4 fixed/positive by an independent four-point sector.
c4_values=[0.16,0.36,0.81]
rows=[]
for c4 in c4_values:
    lim=float(np.sqrt(c4))
    rows.append({'c4':c4,'allowed_c3_interval':[-lim,lim],'allowed_width':2*lim})
# Even if c4 were exactly known at 0.36, c3 is bounded, not selected.
known_c4=0.36
lim=np.sqrt(known_c4)
scan=np.linspace(-lim,lim,121)
hold=scan*0.72**2
out={
 'test':'four-point/dispersive bound versus unique selection of a cubic Wilson coefficient',
 'inequality_proxy':'c3^2 <= c4',
 'motivation':'abstracts the fact that amplitude unitarity/crossing/dispersion can bound an R^3-like coefficient using higher-order Wilson data; no literature numerical coefficient is imported',
 'examples':rows,
 'exact_c4_control':known_c4,
 'allowed_c3_interval_at_exact_c4':[-float(lim),float(lim)],
 'allowed_c3_width_at_exact_c4':float(2*lim),
 'finite_three_point_holdout_width':float(hold.max()-hold.min()),
 'higher_point_bound_reduces_but_does_not_identify_cubic_coefficient':2*lim>1e-6,
 'conclusion':'Adding higher-point positivity/dispersive information can correlate and bound Wilson coefficients, but an inequality generically leaves a continuum (and at least a sign ambiguity). This improves predictivity without producing a unique action from RQIR alone.'
}
write_result('four_point_bound',out)
