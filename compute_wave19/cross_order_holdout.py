import numpy as np
from common import write_result

# Two candidates share the exact same two-point E and Ward-fixed longitudinal vertex data.
# They differ only by a transverse cubic contact c*q^2, invisible to leading/subleading soft data.
lam=0.4214420626313051
def E(x): return float(np.exp(-lam*x))
ward_long=np.array([0.51,-0.22,0.14])
qsoft=0.0; qhold=0.72
cands=[]
for c in [-0.38,0.38]:
    soft_contact=c*qsoft*qsoft
    soft_derivative=2*c*qsoft
    hold_contact=c*qhold*qhold
    cands.append({
      'cubic_contact_c':c,
      'two_point_design':E(0.25),
      'two_point_holdout':E(0.90),
      'ward_longitudinal':ward_long.tolist(),
      'soft_contact':soft_contact,
      'soft_first_derivative':soft_derivative,
      'three_point_finite_holdout':float(ward_long.sum()+hold_contact)
    })
width=max(x['three_point_finite_holdout'] for x in cands)-min(x['three_point_finite_holdout'] for x in cands)
out={
 'test':'prospective cross-order holdout: same two-point + Ward/soft data, different cubic transverse contact',
 'candidate_pair':cands,
 'two_point_difference':abs(cands[0]['two_point_holdout']-cands[1]['two_point_holdout']),
 'soft_value_difference':abs(cands[0]['soft_contact']-cands[1]['soft_contact']),
 'soft_derivative_difference':abs(cands[0]['soft_first_derivative']-cands[1]['soft_first_derivative']),
 'finite_three_point_holdout_width':width,
 'cross_order_degeneracy_exists':width>1e-4 and abs(cands[0]['two_point_holdout']-cands[1]['two_point_holdout'])<1e-14,
 'conclusion':'Two candidates can be exactly identical in the selected two-point sector and in the Ward-fixed/leading-soft information yet differ at finite three-point kinematics through a transverse higher-derivative contact term. A genuine parent law must therefore predict such cross-order data, not only the propagator.'
}
write_result('cross_order_holdout',out)
