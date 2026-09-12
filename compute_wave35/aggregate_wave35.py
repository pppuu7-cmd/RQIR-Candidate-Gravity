import json
from pathlib import Path
required=['availability_evidence_gate','lineage_coverage_graph','anti_splice_gate','orientation_sufficiency','fresh_recompute_contract','compute_budget','j8_j9_shape_contract','provenance_firewall','information_firewall']
found={}
for p in Path('wave35_downloads').rglob('*.json'):
    try: d=json.loads(p.read_text())
    except Exception: continue
    if d.get('test') in required: found[d['test']]=d
missing=[x for x in required if x not in found]
signals={}
for t,d in found.items():
    for k,v in d.get('signals',{}).items(): signals[f'{t}:{k}']=bool(v)
all_true=(not missing) and all(signals.values())
summary={
 'campaign':'same-realization-orientation-wave35',
 'all_required_present':not missing,
 'all_predeclared_signals_true':all_true,
 'signal_count':len(signals),
 'signals':signals,
 'availability_verdict':'PUBLIC_ORIENTATION_OBJECT_NOT_IDENTIFIED_FRESH_RECOMPUTE_CONTRACT_READY',
 'physical_J8_closed':False,
 'blocking_object':'BLOCKED_MISSING_BEST_REALIZATION_5X5_STABILITY_MATRIX_OR_RIGHT_EIGENVECTOR_BASIS',
 'scientific_verdict':'The frozen public same-lineage audit does not identify a reusable best-realization 5x5 stability matrix/right-eigenvector basis. Later fluctuation-program sources provide valuable trajectory, propagator, vertex and effective-action data but do not supply the missing UV orientation object in the required same realization. Wave 35 therefore freezes an executable fresh-recompute contract rather than splicing truncations. A physical J8 promotion requires an actual orientation object plus seven same-realization displaced trajectories and six outputs per trajectory.',
 'next_target':'Wave 36: fresh-FRG recomputation feasibility and implementation specification. Enumerate exactly which beta-flow/Jacobian derivatives are available vs missing in the best F1 closure, identify the smallest new diagrammatic/flow computation required, and freeze an output schema directly consumable by Wave 33/35.'
}
if 'orientation_sufficiency' in found:
    summary['same_spectrum_alternative_max_subspace_angle_rad']=found['orientation_sufficiency'].get('same_spectrum_alternative_max_subspace_angle_rad')
if 'j8_j9_shape_contract' in found:
    summary['J8_rank_synthetic']=found['j8_j9_shape_contract'].get('J8_rank')
Path('wave35_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)); print(json.dumps(summary,indent=2,sort_keys=True)); assert all_true
