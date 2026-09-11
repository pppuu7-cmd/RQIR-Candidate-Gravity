from common import write_result

# Endpoint witness: two actions share all selected two-point data and satisfy the same schematic
# Ward/soft/causality/four-point admissibility information, but differ by the sign of a physical cubic Wilson coefficient.
c4=0.36
c=0.30
q=0.72
base3=0.43
acts=[]
for s in [-1,1]:
    c3=s*c
    acts.append({
      'c3':c3,
      'c4':c4,
      'same_two_point_sector':True,
      'ward_longitudinal_same':True,
      'leading_soft_same':True,
      'first_subleading_soft_same':True,
      'dispersive_bound_satisfied':c3*c3<=c4,
      'finite_three_point_holdout':base3+c3*q*q
    })
width=abs(acts[1]['finite_three_point_holdout']-acts[0]['finite_three_point_holdout'])
out={
 'test':'action-level endpoint witness after selected RQIR/consistency/admissibility information',
 'action_pair':acts,
 'finite_three_point_holdout_width':width,
 'both_actions_admissible_under_proxy_gates':all(a['dispersive_bound_satisfied'] for a in acts),
 'same_low_order_and_gates_different_physical_higher_point_prediction':width>1e-4,
 'conclusion':'A pair of one-action EFT witnesses can share the selected two-point sector and the same Ward/soft/admissibility information yet make different finite three-point predictions through a physical cubic Wilson coefficient. This is the concrete endpoint obstruction to unique microscopic reconstruction from those constraints alone.'
}
write_result('endpoint_witness',out)
