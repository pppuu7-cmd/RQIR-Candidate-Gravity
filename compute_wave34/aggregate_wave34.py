import json, pathlib
required=['wave34_anchor_residual.json','wave34_conditional_root.json','wave34_projected_jacobian.json','wave34_held_coordinate_sensitivity.json','wave34_embedding_no_go.json','wave34_published_spectrum_mismatch.json','wave34_information_firewall.json']
found={}
for p in pathlib.Path('wave34_downloads').rglob('*.json'):
    if p.name in required: found[p.name]=json.loads(p.read_text())
all_present=all(k in found for k in required)
signals={}
for obj in found.values(): signals.update(obj.get('signals',{}))
all_true=bool(signals) and all(bool(v) for v in signals.values())
root=found.get('wave34_conditional_root.json',{}).get('root')
jac=found.get('wave34_projected_jacobian.json',{})
sens=found.get('wave34_held_coordinate_sensitivity.json',{})
summary={
 'campaign':'appendix-f-projected-jacobian-wave34',
 'classification':'PARTIAL_SURROGATE_NOT_J8',
 'all_required_present':all_present,
 'all_predeclared_signals_true':all_true,
 'conditional_root':root,
 'projected_eigenvalues':jac.get('eigenvalues'),
 'projected_condition_number':jac.get('condition_number'),
 'max_held_coordinate_root_shift':sens.get('max_root_shift'),
 'blocking_object':'BLOCKED_PARTIAL_F1_F2_F4_JACOBIAN_DOES_NOT_DETERMINE_FULL_5D_BEST_REALIZATION_ORIENTATION',
 'scientific_verdict':'Wave 34 reconstructs the maximal declared three-equation Appendix-F subsystem without importing F3/F5 as if the full five-dimensional stability matrix were known. The rounded published Truncation-4 anchor is not a fixed point of this restricted subsystem; a nearby conditional root exists when lambda4 and g4 are held fixed, and its 3x3 Jacobian is reproducible. The conditional root and spectrum move under modest held-coordinate perturbations, and the same 3x3 block admits inequivalent 5x5 completions with different relevant dimensions. Therefore the partial Jacobian supplies local surrogate directional information but cannot be promoted to physical J8.',
 'next_target':'Wave 35: turn the missing full-orientation object into a minimal external-computation specification: enumerate the exact five beta derivatives or right eigenvectors required from the same F1 closure, define numerical tolerances and provenance checks, and test synthetic completions to rank which missing cross-derivatives most strongly control the relevant-subspace orientation.' ,
 'signals':signals
}
pathlib.Path('wave34_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)); print(json.dumps(summary,indent=2,sort_keys=True)); assert all_present and all_true
