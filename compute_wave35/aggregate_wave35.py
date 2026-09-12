import json, pathlib
required=['wave35_B_only.json','wave35_C_only.json','wave35_D_only.json','wave35_BC.json','wave35_BCD.json','wave35_decomposition_contract.json','wave35_physical_input_contract.json','wave35_information_firewall.json']
found={}
for p in pathlib.Path('wave35_downloads').rglob('*.json'):
    if p.name in required: found[p.name]=json.loads(p.read_text())
all_present=all(k in found for k in required)
signals={}
for obj in found.values(): signals.update(obj.get('signals',{}))
all_true=bool(signals) and all(bool(v) for v in signals.values())
summary_rows={k.replace('wave35_','').replace('.json',''):v.get('rows') for k,v in found.items() if v.get('rows') is not None}
# Determine the highest median angle at each scale descriptively only; this is not physical ranking.
descriptive=[]
for idx,s in enumerate([0.05,0.10,0.20,0.40]):
    vals={name:rows[idx]['median_max_principal_angle_rad'] for name,rows in summary_rows.items()}
    descriptive.append({'scale':s,'median_angles_rad':vals,'largest_under_declared_synthetic_ensemble':max(vals,key=lambda k: vals[k] if vals[k] is not None else -1)})
summary={
 'campaign':'missing-derivative-leverage-wave35',
 'classification':'SYNTHETIC_INFORMATION_LEVERAGE_NOT_J8',
 'all_required_present':all_present,
 'all_predeclared_signals_true':all_true,
 'descriptive_synthetic_leverage_by_scale':descriptive,
 'blocking_object':'BLOCKED_FULL_5D_SAME_REALIZATION_STABILITY_MATRIX_OR_RIGHT_EIGENSYSTEM_STILL_REQUIRED',
 'scientific_verdict':'Wave 35 stress-tests the information content of the 16 derivatives absent from the Wave-34 3x3 conditional block. Synthetic variations of B, C and D produce inequivalent full five-dimensional relevant-subspace orientations while holding the known A block fixed. The experiment is deliberately prior-dependent and is not a physical ranking of FRG derivatives. Its role is to demonstrate that cross/held-sector derivative information is necessary and to freeze a complete external-computation contract for physical J8.',
 'next_target':'Wave 36: design a provenance-complete drop-in validator for an externally produced F1 5x5 stability matrix/right eigensystem and a finite-difference consistency audit; in parallel audit whether any public supplemental/code artifact from the F1 lineage exposes the missing matrix before requiring a new FRG calculation.',
 'signals':signals
}
pathlib.Path('wave35_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)); print(json.dumps(summary,indent=2,sort_keys=True)); assert all_present and all_true
