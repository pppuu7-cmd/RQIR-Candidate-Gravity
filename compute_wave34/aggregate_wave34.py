import json
from pathlib import Path
required=['source_closure_gate','flow_finiteness','rounded_conditioning','nearby_root_reconstruction','step_size_stability','published_spectrum_comparison','rounding_sensitivity','surrogate_firewall','information_firewall']
found={}
for p in Path('wave34_downloads').rglob('*.json'):
    try: d=json.loads(p.read_text())
    except Exception: continue
    if d.get('test') in required: found[d['test']]=d
missing=[x for x in required if x not in found]
signals={}
for t,d in found.items():
    for k,v in d.get('signals',{}).items(): signals[f'{t}:{k}']=bool(v)
all_true=(not missing) and all(signals.values())
root=found.get('nearby_root_reconstruction',{})
nroots=int(root.get('n_accepted_roots',0))
spec=found.get('published_spectrum_comparison',{})
mis=spec.get('max_assignment_error_to_published_bar_spectrum')
cond=found.get('rounded_conditioning',{})
rounding=found.get('rounding_sensitivity',{})
if nroots>0:
    recon='SURROGATE_ROOT_FOUND_BUT_STILL_NOT_J8'
else:
    recon='SURROGATE_PRINTED_SYSTEM_RECONSTRUCTION_INCONCLUSIVE_NO_RAW_RESIDUAL_ROOT_IN_FROZEN_BOX'
summary={
 'campaign':'appendix-f-surrogate-wave34',
 'classification':'SURROGATE_NOT_J8',
 'all_required_present':not missing,
 'all_predeclared_signals_true':all_true,
 'signal_count':len(signals),
 'signals':signals,
 'n_accepted_nearby_roots':nroots,
 'rounded_point_flow_inf_norm':cond.get('flow_inf_norm'),
 'rounded_point_jacobian_condition_number':cond.get('jacobian_condition_number'),
 'rounded_point_published_spectrum_mismatch':mis,
 'rounding_cell_residual_width':rounding.get('residual_inf_width'),
 'reconstruction_status':recon,
 'physical_J8_closed':False,
 'scientific_verdict':'Wave 34 audits the printed Appendix-F Truncation-4 equations under the frozen eta=0 and higher-coupling closure without fitting any coefficient. The result quantifies numerical stiffness, rounding sensitivity, root reconstructibility and spectrum mismatch. Regardless of agreement quality, the system remains a local/analytic SURROGATE_NOT_J8 and cannot replace the missing best-realization F1 orientation object.',
 'blocking_object':'BLOCKED_MISSING_BEST_REALIZATION_5X5_STABILITY_MATRIX_OR_RIGHT_EIGENVECTOR_BASIS',
 'next_target':'If the printed surrogate is stably reconstructible, use it only for end-to-end surrogate trajectory/Jacobian tests. If inconclusive, freeze the discrepancy and prioritize a fresh same-realization FRG stability calculation or acquisition of the unpublished numerical orientation object.'
}
Path('wave34_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)); print(json.dumps(summary,indent=2,sort_keys=True)); assert all_true
