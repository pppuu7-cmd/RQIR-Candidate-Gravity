#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Five sector-level quantities x = (3 RG-relevant coordinates, 2 spectral/amplitude features).
# Compare an unlinked 5-parameter description with a 3-parameter shared latent primitive p,
# x = L p. The linkage is deliberately synthetic: this tests architecture, not a proposed law.
L=np.array([
 [1.0,0.2,-0.1],
 [0.1,1.0,0.3],
 [-0.2,0.35,1.0],
 [0.6,-0.25,0.4],
 [-0.15,0.55,0.7],
],float)
p_true=np.array([0.18,-0.11,0.23])
x_true=L@p_true

# Four design observables mix sectors; one holdout is never used in the fit.
J=np.array([
 [1.0,0.0,0.0,0.5,0.0],
 [0.0,1.0,0.0,0.0,0.4],
 [0.0,0.0,1.0,0.3,-0.2],
 [0.3,-0.1,0.0,0.6,0.5],
],float)
h=np.array([0.2,0.1,-0.3,0.4,0.7],float)
y=J@x_true
holdout_true=float(h@x_true)

# Linked latent fit: solve p from y = J L p.
JL=J@L
p_fit=np.linalg.lstsq(JL,y,rcond=None)[0]
x_link=L@p_fit
holdout_link=float(h@x_link)
rank_link=int(np.linalg.matrix_rank(JL))
nullity_link=3-rank_link

# Unlinked fit: y=Jx has one null direction (4 constraints on 5 quantities).
x_min=np.linalg.lstsq(J,y,rcond=None)[0]
U,S,Vt=np.linalg.svd(J)
rank_unlinked=int(np.linalg.matrix_rank(J))
null_basis=Vt[rank_unlinked:,:]
nullity_unlinked=5-rank_unlinked
if null_basis.size:
    n=null_basis[0]/np.linalg.norm(null_basis[0])
    holdout_slope=float(h@n)
    # A bounded +-1 scan along the undetermined unit-norm direction only to quantify sensitivity.
    scan=[float(h@(x_min+a*n)) for a in np.linspace(-1,1,201)]
    holdout_width=float(max(scan)-min(scan))
else:
    holdout_slope=0.0; holdout_width=0.0

out={
 "test":"shared finite latent primitive versus unlinked sector parameters with untouched holdout",
 "latent_parameter_count":3,
 "sector_quantity_count_unlinked":5,
 "design_observable_count":4,
 "linked_design_rank":rank_link,
 "linked_latent_nullity":nullity_link,
 "unlinked_design_rank":rank_unlinked,
 "unlinked_parameter_nullity":nullity_unlinked,
 "true_latent":p_true.tolist(),
 "recovered_latent":p_fit.tolist(),
 "latent_recovery_error_max_abs":float(np.max(np.abs(p_fit-p_true))),
 "holdout_true":holdout_true,
 "holdout_linked_prediction":holdout_link,
 "holdout_linked_error_abs":float(abs(holdout_link-holdout_true)),
 "unlinked_holdout_sensitivity_per_unit_null_displacement":holdout_slope,
 "unlinked_holdout_width_for_unit_null_scan":holdout_width,
 "linked_model_predicts_holdout":nullity_link==0 and abs(holdout_link-holdout_true)<1e-10,
 "unlinked_model_has_holdout_ambiguity":nullity_unlinked>0 and abs(holdout_slope)>1e-10,
 "conclusion":"A shared finite primitive can, in principle, convert cross-sector design data into a prospective holdout prediction while an unlinked sector-by-sector description remains underdetermined. This is only an architecture test: the physical map L must itself be derived independently before it can count as new physics.",
 "scope":"synthetic linear latent-variable identifiability/holdout proxy, not a derived quantum-gravity relation"
}
Path('wave8_results').mkdir(exist_ok=True)
Path('wave8_results/joint_latent_holdout.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
