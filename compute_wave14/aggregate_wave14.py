#!/usr/bin/env python3
import json,glob,os
from pathlib import Path
files=glob.glob('wave14_downloads/*/*.json')
data={os.path.basename(p):json.load(open(p,encoding='utf-8')) for p in files}
need=['local_ode_nullspace_killer.json','volterra_predictive_closure.json','fredholm_bifurcation_audit.json','functional_identity_rank.json','equation_class_identifiability.json','comparator_firewall.json']
missing=[n for n in need if n not in data]
signals={
 'functional_law_kills_static_q3_q5_null_modes':data.get('local_ode_nullspace_killer.json',{}).get('all_positive_deformations_violate_functional_law',False),
 'finite_volterra_law_can_be_unique_and_predict_holdouts':data.get('volterra_predictive_closure.json',{}).get('finite_equation_predictive_closure_demonstrated',False),
 'finite_nonlinear_self_consistency_can_have_multiple_branches':data.get('fredholm_bifurcation_audit.json',{}).get('multiple_solution_branches_exist',False),
 'functional_identity_has_full_rank_on_tested_static_nullspace':data.get('functional_identity_rank.json',{}).get('functional_identity_full_rank_on_tested_nullspace',False),
 'same_design_observables_do_not_identify_equation_class':data.get('equation_class_identifiability.json',{}).get('two_design_observables_do_not_identify_equation_class',False),
 'architectural_equations_are_known_comparator_classes':data.get('comparator_firewall.json',{}).get('mere_existence_of_finite_functional_equation_is_not_novel',False)
}
allok=(not missing) and all(signals.values())
out={
 'campaign':'post-freeze-functional-equation-wave14',
 'missing':missing,
 'signals':signals,
 'all_required_present':allok,
 'functional_equation_architecture_can_remove_finite_static_nullspaces':bool(signals['functional_law_kills_static_q3_q5_null_modes'] and signals['functional_identity_has_full_rank_on_tested_static_nullspace']),
 'finite_equation_alone_guarantees_predictive_closure':False,
 'equation_class_selected_by_current_design_data':False,
 'unique_solution_or_physical_branch_selection_required':True,
 'qg_specific_operator_or_kernel_derivation_required':True,
 'candidate_new_QG_primitive_found':False,
 'scientific_verdict':'Wave 14 separates three logically distinct requirements. First, a pointwise/functional law can eliminate continuum directions invisible to finitely many static sum rules. Second, a finite causal Volterra equation can be unique and predictive, demonstrating the desired closure architecture. Third, finite nonlinear self-consistency can still bifurcate, and even two unique finite equation classes can fit the same design observables while disagreeing on untouched dispersive holdouts. Therefore the remaining problem is no longer whether a finite continuum-generating law is mathematically possible. It is the physical derivation and identification of the QG-specific operator/kernel together with uniqueness or branch selection. Existing spectral-FRG/SD/bootstrap equation classes remain comparators.',
 'next_target':'Wave 15: impose cross-sector functional closure. Search for a single finite operator/kernel whose same parameters simultaneously generate the spectral continuum and constrain dispersive/Wilson data. Compare local-flow, causal-kernel and self-consistent candidates under frozen cross-sector holdouts; audit reparameterisation equivalence to spectral FRG/SD/bootstrap. The strongest target is a kernel fixed by an independently motivated RQIR composition/measurement principle rather than fitted to the spectral density.',
 'scope':'architectural proxy tests of functional completeness, uniqueness and equation-class identifiability; no claim that the synthetic equations represent gravitons.'
}
Path('wave14_summary.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
