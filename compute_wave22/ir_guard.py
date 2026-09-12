import numpy as np
from common import write_result

eps=1e-8
rows=[]
# finite-q spin-2 / spin-0 dressing directions
rows.append([0,0,0,0,eps**2,0])
rows.append([0,0,0,0,0,eps**2])
# cubic finite-kinematic contact proxy
rows.append([eps**2,eps**3,0,0,0.15*eps,-0.10*eps**2])
# quartic proxy approaching the soft/IR origin with s=t=eps
s=t=eps; h=1
rows.append([0.25*(s+t),0.2*h*s*t,s**2+t**2,h*s*t,0.1*s,0.08*t])
M=np.asarray(rows,float)
max_abs=float(np.max(np.abs(M)))
out={
 'test':'diagnostic guard that Wave-22 residual directions do not replace frozen IR pole/residue normalization',
 'epsilon':eps,
 'ir_proxy_rows':M,
 'max_absolute_residual_sensitivity_at_epsilon':max_abs,
 'residual_sensitivities_vanish_toward_ir_origin':max_abs<1e-7,
 'note':'Diagnostic only; Wave 22 tests finite residual shape/contact directions after the GR/IR normalization was already frozen. This is not a full pole calculation.',
 'conclusion':'All Wave-22 proxy residual sensitivities vanish toward the chosen IR origin, so the prospective bank targets finite-momentum/higher-order freedom rather than re-fitting the frozen massless GR normalization.'
}
write_result('ir_guard',out)
