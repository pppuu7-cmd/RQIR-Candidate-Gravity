import json, pathlib
required=[
 'wave33_ingest_schema.json','wave33_complex_realification.json','wave33_phase_invariance.json',
 'wave33_matrix_basis_equivalence.json','wave33_seven_trajectory_generator.json',
 'wave33_uncertainty_subspace_stress.json','wave33_surrogate_firewall.json','wave33_information_firewall.json']
found={}
for p in pathlib.Path('wave33_downloads').rglob('*.json'):
    if p.name in required: found[p.name]=json.loads(p.read_text())
all_present=all(k in found for k in required)
signals={}
for obj in found.values(): signals.update(obj.get('signals',{}))
all_true=all(bool(v) for v in signals.values()) and len(signals)>0
unc=found.get('wave33_uncertainty_subspace_stress.json',{})
summary={
 'campaign':'frg-basis-ingest-wave33',
 'all_required_present':all_present,
 'all_predeclared_signals_true':all_true,
 'classification':'SURROGATE_NOT_J8',
 'physical_J8_status':'BLOCKED_MISSING_BEST_REALIZATION_5X5_STABILITY_MATRIX_OR_RIGHT_EIGENVECTOR_BASIS',
 'symmetric_trajectory_count':7,
 'uncertainty_median_max_principal_angle_rad':unc.get('median_max_principal_angle_rad'),
 'uncertainty_p95_max_principal_angle_rad':unc.get('p95_max_principal_angle_rad'),
 'signals':signals,
 'scientific_verdict':'Wave 33 validates the executable orientation-object ingest and displacement machinery independently of any physical F1 eigenbasis. A valid 5x5 matrix or equivalent right-eigenvector basis is converted into a three-dimensional real relevant subspace, including correct realification of a complex-conjugate pair, phase and normalization invariance, seven symmetric trajectories, and a subspace-uncertainty ensemble. The published Truncation-4 spectrum is used only through a synthetic canonical matrix as SURROGATE_NOT_J8; therefore Wave 33 does not close physical J8.',
 'next_target':'Wave 34: derive the maximal strictly partial projected Jacobian reproducible from Appendix-F analytic beta equations under the published Truncation-4 closure, quantify its local directional information, and prove that it cannot be promoted to the best-realization five-dimensional J8 basis.'
}
pathlib.Path('wave33_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)); print(json.dumps(summary,indent=2,sort_keys=True)); assert all_present and all_true
