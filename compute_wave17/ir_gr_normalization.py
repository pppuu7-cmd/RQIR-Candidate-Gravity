import numpy as np
from common import write_result

# Parameterization of the two transverse conserved-source form factors.
# x denotes a dimensionless q^2 scale inside a declared EFT domain.
# GR normalization at x=0 fixes c2=1 and c0=-1/2, but not analytic slopes/curvatures.
# p = [c2,c0,a1,a2,b1,b2]
J=np.array([
 [1,0,0,0,0,0],
 [0,1,0,0,0,0]
],dtype=float)
rank=int(np.linalg.matrix_rank(J))
nullity=6-rank

# Scan controlled small higher-order deformations preserving exact IR residues.
xs=[0.0,0.15,0.45]
scan=[]
for a1,a2,b1,b2 in [(-0.2,0.1,0.15,-0.08),(0,0,0,0),(0.18,-0.12,-0.2,0.1)]:
    vals=[]
    for x in xs:
        f2=1+a1*x+a2*x*x
        f0=-0.5+b1*x+b2*x*x
        vals.append({'x':x,'f2':f2,'f0':f0})
    scan.append({'shape':[a1,a2,b1,b2],'values':vals})
width_f2=max(s['values'][-1]['f2'] for s in scan)-min(s['values'][-1]['f2'] for s in scan)
width_f0=max(s['values'][-1]['f0'] for s in scan)-min(s['values'][-1]['f0'] for s in scan)

out={
 'test':'IR GR/Newtonian normalization rank on transverse tensor form factors',
 'parameterization':'f2(x)=c2+a1 x+a2 x^2; f0(x)=c0+b1 x+b2 x^2',
 'GR_IR_constraints':['c2=1','c0=-1/2'],
 'constraint_rank':rank,
 'parameter_nullity_after_IR_normalization':nullity,
 'finite_q_scan':scan,
 'holdout_width_f2_at_x_0p45':width_f2,
 'holdout_width_f0_at_x_0p45':width_f0,
 'IR_GR_normalization_fixes_residues_not_shape': rank==2 and nullity==4 and width_f2>1e-3 and width_f0>1e-3,
 'conclusion':'The weak-field/GR limit fixes the massless transverse residue combination at q^2->0 but leaves higher-order analytic form-factor shape freedom. Those directions are naturally EFT-like unless an extra microscopic law fixes them.'
}
write_result('ir_gr_normalization',out)
