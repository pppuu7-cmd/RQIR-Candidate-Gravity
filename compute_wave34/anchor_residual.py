import numpy as np
from common import ANCHOR,beta3,write
b=beta3(ANCHOR); n=float(np.linalg.norm(b))
signals={'rounded_published_anchor_is_not_a_fixed_point_of_restricted_F1_F2_F4_system':n>5e-2,'anchor_residual_is_finite':bool(np.all(np.isfinite(b)))}
out={'test':'anchor_residual','anchor':ANCHOR.tolist(),'beta':b.tolist(),'residual_norm':n,'signals':signals}; write('wave34_anchor_residual.json',out); assert all(signals.values())
