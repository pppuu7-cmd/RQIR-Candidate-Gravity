#!/usr/bin/env python3
import json,glob,os
from pathlib import Path
files=glob.glob('wave15_downloads/*/*.json')
data={os.path.basename(p):json.load(open(p,encoding='utf-8')) for p in files}
need=['shared_kernel_cross_sector.json','unlinked_vs_shared_kernel_rank.json','kernel_null_perturbation_holdout.json','same_realization_consistency.json','kernel_axiom_rank.json','comparator_firewall.json']
missing=[n for n in need if n not in data]
signals={
 'shared_kernel_predicts_spectral_and_dispersion_holdouts':data.get('shared_kernel_cross_sector.json',{}).get('shared_kernel_cross_sector_closure_demonstrated',False),
 'sharing_removes_unlinked_parameter_nullity':data.get('unlinked_vs_shared_kernel_rank.json',{}).get('shared_model_removes_parameter_nullity',False),
 'unlinked_null_direction_changes_prospective_holdout':data.get('unlinked_vs_shared_kernel_rank.json',{}).get('unlinked_null_direction_changes_holdout',False),
 'cross_sector_holdout_detects_spectral_design_null':data.get('kernel_null_perturbation_holdout.json',{}).get('spectral_design_null_is_seen_cross_sector',False),
 'same_realization_gate_rejects_sector_switching':data.get('same_realization_consistency.json',{}).get('same_realization_gate_detects_inconsistency',False),
 'generic_kernel_axioms_leave_shape_freedom':data.get('kernel_axiom_rank.json',{}).get('generic_axioms_leave_kernel_shape_freedom',False),
 'cross_sector_architecture_is_not_by_itself_novel':data.get('comparator_firewall.json',{}).get('shared_spectral_dispersion_parameters_are_not_by_themselves_novel',False)
}
out={
 'campaign':'post-freeze-cross-sector-kernel-wave15',
 'missing':missing,
 'signals':signals,
 'all_required_present':(not missing) and all(signals.values()),
 'shared_kernel_cross_sector_architecture_validated':bool(signals['shared_kernel_predicts_spectral_and_dispersion_holdouts'] and signals['sharing_removes_unlinked_parameter_nullity'] and signals['cross_sector_holdout_detects_spectral_design_null']),
 'same_realization_gate_required':True,
 'generic_structural_axioms_uniquely_fix_kernel':False,
 'independent_qg_specific_kernel_origin_required':True,
 'candidate_new_QG_primitive_found':False,
 'scientific_verdict':'Wave 15 shows that cross-sector closure is materially stronger than sector-by-sector fitting. A single frozen kernel realization can use spectral design data to predict higher/Wilson moments and nonlocal dispersive holdouts; sharing the kernel removes a parameter null direction that survives in an unlinked description; and cross-sector holdouts detect positive continuum directions invisible to the spectral design alone. The same-realization gate also exposes false closure produced by allowing different sector-specific parameter copies. However, generic causal/soft/normalization axioms still leave kernel-shape freedom even in a small finite basis, and shared spectral-dispersive structure is already present in known comparator frameworks. The unresolved step is therefore the independent gravitational/RQIR derivation of the operator/kernel itself.',
 'next_target':'Wave 16: derive or constrain the kernel from original frozen RQIR composition/operational structure rather than selecting a convenient spectral equation. Build a provenance matrix from explicit RQIR requirements to operator constraints, quantify the kernel-basis rank each requirement adds, reserve cross-sector spectral/dispersion holdouts, and reject any operator condition imported only from the polygon/QGR-P or known comparator solutions. If original RQIR does not uniquely fix the kernel, identify the exact residual nullity and the minimal additional physical principle required.',
 'scope':'synthetic cross-sector closure and generic finite-kernel rank proxies; no claim that the Volterra kernel is a graviton law.'
}
Path('wave15_summary.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
