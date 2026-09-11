import json
from pathlib import Path
import numpy as np

# Method correction 18.1.
# The original H0 used the same spin-sector geometry at design and holdout, so changing only x
# leaves the design-null vector exactly invisible. This corrected control reuses the already-frozen
# independent source geometry from Wave 17; it is not chosen from the failed Wave-18 H0 result.
A1,B1=-0.33089440785040997,-1.2145566246797788
A2,B2=-1.9148121969269116,0.05959647629583646
xd,xh=0.25,0.90
J=np.array([[xd*A1,xd*B1]])
rank=int(np.linalg.matrix_rank(J)); nullity=2-rank
_,_,vt=np.linalg.svd(J,full_matrices=True)
n=vt[-1]/np.linalg.norm(vt[-1])
base=np.array([0.08,-0.04]); amp=0.35
pairs=[base-amp*n,base+amp*n]
def obs(p,x,A,B):
    a,b=p
    return (1+a*x)*A+(-0.5+b*x)*B
vals=[{'p':p.tolist(),'design':float(obs(p,xd,A1,B1)),'independent_geometry_holdout':float(obs(p,xh,A2,B2))} for p in pairs]
dw=max(v['design'] for v in vals)-min(v['design'] for v in vals)
hw=max(v['independent_geometry_holdout'] for v in vals)-min(v['independent_geometry_holdout'] for v in vals)
out={
 'correction_id':'W18-METHOD-CORR-001',
 'test':'corrected H0 no-extra-hypothesis control with frozen independent source geometry',
 'original_defect':'Wave-18 H0 reused the same spin-2/spin-0 source geometry at design and holdout; the holdout gradient was therefore collinear with the design gradient and could not detect the design null direction.',
 'correction_provenance':'holdout geometry coefficients are reused from the already-frozen Wave-17 tensor_holdout test, not selected after seeing the Wave-18 failure',
 'design_rank':rank,'design_nullity':nullity,'null_vector':n.tolist(),
 'candidate_pair':vals,'design_width':dw,'independent_geometry_holdout_width':hw,
 'underdetermination_survives_design':nullity>0 and dw<1e-10,
 'independent_frozen_holdout_resolves_null':hw>1e-4,
 'corrected_H0_signal':nullity>0 and dw<1e-10 and hw>1e-4,
 'conclusion':'The failed original H0 signal was a holdout-geometry defect, not physical closure. With the previously frozen independent source geometry, the no-extra-hypothesis control again exhibits a physical transverse null direction invisible to design but visible prospectively.'
}
Path('wave18_correction_results').mkdir(exist_ok=True)
Path('wave18_correction_results/h0_corrected.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True))
