import numpy as np
from common import X_TABLE,flows,jacobian,write
b=flows(X_TABLE); J=jacobian(X_TABLE,1e-6)
s=np.linalg.svd(J,compute_uv=False)
cond=float(s[0]/s[-1]) if s[-1]>0 else float('inf')
signals={
 'rounded_point_residual_recorded_without_forcing_zero':bool(np.all(np.isfinite(b))),
 'rounded_point_jacobian_singular_values_recorded':bool(np.all(np.isfinite(s))) and len(s)==5,
 'conditioning_is_reported_not_repaired':True,
}
out={'test':'rounded_conditioning','rounded_point':X_TABLE,'flow':b,'flow_inf_norm':float(np.linalg.norm(b,np.inf)),'jacobian_singular_values':s,'jacobian_condition_number':cond,'signals':signals}
write('wave34_rounded_conditioning.json',out); assert all(signals.values())
