#!/usr/bin/env python3
import json
from pathlib import Path

OUT=Path("wave4_results"); OUT.mkdir(exist_ok=True)

# Structural flat-space metric quadratic-gravity classifier for
# S ~ EH + alpha R^2 + beta R_{mu nu} R^{mu nu}, modulo the 4D Gauss-Bonnet
# topological combination / basis changes.
# Standard metric quadratic gravity contains:
# - an extra massive spin-2 mode when beta != 0; in the ordinary metric
#   quantization this mode is ghost-like;
# - an extra scalar unless 3 alpha + beta = 0 (normalization-independent
#   structural disappearance condition in this basis, up to conventions).
# To have neither extra spin-2 nor scalar in this simple local metric sector,
# beta=0 and 3alpha+beta=0 -> alpha=0.
# We classify a small integer grid; we do not use exact mass formulas/signs.

vals=[-3,-2,-1,0,1,2,3]
records=[]
for alpha in vals:
    for beta in vals:
        extra_spin2=(beta!=0)
        scalar_combo=3*alpha+beta
        extra_scalar=(scalar_combo!=0)
        if not extra_spin2 and not extra_scalar:
            cls="NO_EXTRA_LOCAL_DOF__EH_ROOT"
        elif extra_spin2 and extra_scalar:
            cls="EXTRA_GHOSTLIKE_SPIN2_PLUS_SCALAR_IN_STANDARD_METRIC_QUADRATIC_GRAVITY"
        elif extra_spin2:
            cls="EXTRA_GHOSTLIKE_SPIN2_ONLY_ON_SCALAR_DECOUPLING_LINE"
        else:
            cls="EXTRA_SCALAR_ONLY__F_R_LIKE_DIRECTION"
        records.append({"alpha":alpha,"beta":beta,"3alpha_plus_beta":scalar_combo,"extra_spin2":extra_spin2,"extra_scalar":extra_scalar,"classification":cls})

healthy_no_extra=[r for r in records if not r["extra_spin2"] and not r["extra_scalar"]]
summary={
 "test":"local metric quadratic-curvature state-content cost",
 "basis":"EH + alpha R^2 + beta Ricci^2 (4D, modulo Gauss-Bonnet/boundary basis freedom)",
 "grid":vals,
 "records":records,
 "no_extra_local_dof_points":healthy_no_extra,
 "unique_no_extra_point_on_grid":len(healthy_no_extra)==1 and healthy_no_extra[0]["alpha"]==0 and healthy_no_extra[0]["beta"]==0,
 "scope":"structural classifier using standard metric quadratic-gravity particle content; exact pole masses/sign conventions are not computed here"
}
(OUT/"quadratic_curvature_state_cost.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
