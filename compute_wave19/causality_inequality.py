import numpy as np
from common import write_result

# Causality/eikonal inequality proxy for an anomalous higher-derivative three-point coefficient c.
# We preregister a positive-delay surrogate tau(b)=1-c^2/(1+b^2), so tau>=0 bounds |c|
# but does not select c=0. This only tests the logical power of an inequality gate.
bs=np.linspace(0.2,4.0,80)
cs=np.linspace(-0.95,0.95,191)
allowed=[]
for c in cs:
    tau=1.0-c*c/(1.0+bs*bs)
    if tau.min()>=0:
        allowed.append(float(c))
width=max(allowed)-min(allowed)
holdouts=[c*(0.7**3) for c in allowed]
out={
 'test':'causality inequality versus uniqueness of a cubic transverse coupling',
 'allowed_c_min':min(allowed),'allowed_c_max':max(allowed),'allowed_width':width,
 'finite_kinematic_holdout_width':max(holdouts)-min(holdouts),
 'causality_gate_reduces_domain_but_not_unique':width>1e-3,
 'scope_note':'Positive-delay surrogate used only to test inequality-vs-uniqueness logic; it is not a quantitative CEMZ shockwave computation.',
 'conclusion':'A causality gate can bound an anomalous higher-point coupling while leaving a continuous allowed interval. Inequality consistency is therefore not the missing unique cross-order law.'
}
write_result('causality_inequality',out)
