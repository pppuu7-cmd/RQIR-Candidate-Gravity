#!/usr/bin/env python3
import json
from pathlib import Path
out={
 "test":"Wave 14 functional-equation novelty firewall",
 "known_comparator_classes":[
   "Lorentzian spectral functional renormalisation-group flow equations",
   "Ward/symmetry-improved spectral flows",
   "self-consistent spectral RG with full continuum feedback",
   "Schwinger-Dyson-type self-consistency equations",
   "bootstrap/dispersion integral equations",
   "generic Volterra/Fredholm continuum equations"
 ],
 "mere_existence_of_finite_functional_equation_is_not_novel":True,
 "mere_self_consistency_is_not_novel":True,
 "new_QG_candidate_requires_distinct_physical_derivation_and_kernel":True,
 "must_pass_unique_solution_or_branch_selection_gate":True,
 "must_predict_frozen_nonlocal_holdouts":True,
 "candidate_new_QG_primitive_from_wave14_architectures_alone":False,
 "conclusion":"Wave 14 may validate architectural necessities—functional completeness, uniqueness and holdout prediction—but none of the tested differential/Volterra/Fredholm forms are new QG physics by themselves. A C5-distinct candidate requires an independently derived gravitational principle that fixes the operator/kernel and is not a reparameterisation of spectral FRG, Schwinger-Dyson or bootstrap/dispersion machinery."
}
Path('wave14_results').mkdir(exist_ok=True)
Path('wave14_results/comparator_firewall.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
