#!/usr/bin/env python3
import json
from pathlib import Path

root=Path('wave9_downloads')
items={}
for p in root.rglob('*.json'):
    try:
        items[p.stem]=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        items[p.stem]={"parse_error":str(e)}
required={'minimal_defect_rank','spectral_to_dispersion_recurrence','recurrence_holdout_selection','higher_derivative_onset_scale','minimal_defect_comparator_firewall'}
missing=sorted(required-set(items))
sig={}
if 'minimal_defect_rank' in items:
 d=items['minimal_defect_rank']
 sig['known_proxy_constraints_reduce_to_one_higher_derivative_defect']=d.get('residual_nullity')==1 and bool(d.get('single_residual_defect_is_cy',False))
if 'spectral_to_dispersion_recurrence' in items:
 d=items['spectral_to_dispersion_recurrence']
 sig['finite_spectral_recurrence_can_predict_dispersive_Wilson_tower']=bool(d.get('rank3_law_closes_Wilson_tower',False))
 sig['without_rank_axiom_next_Wilson_remains_ambiguous']=bool(d.get('finite_positive_moments_alone_leave_next_Wilson_ambiguous',False))
if 'recurrence_holdout_selection' in items:
 d=items['recurrence_holdout_selection']
 sig['prospective_holdout_discriminates_closure_order']=bool(d.get('rank3_passes_holdout',False)) and bool(d.get('rank2_fails_holdout',False))
if 'higher_derivative_onset_scale' in items:
 d=items['higher_derivative_onset_scale']
 sig['nonzero_residual_defect_maps_to_finite_onset_scale']=bool(d.get('nonzero_defect_implies_finite_onset_scale',False))
if 'minimal_defect_comparator_firewall' in items:
 d=items['minimal_defect_comparator_firewall']
 sig['known_constraints_localize_but_do_not_derive_defect']=bool(d.get('known_constraints_can_localize_one_higher_derivative_defect',False)) and not d.get('known_constraints_by_themselves_derive_defect_value',True)

summary={
 'campaign':'post-freeze-minimal-defect-wave9',
 'missing':missing,
 'signals':sig,
 'all_required_present':not missing,
 'minimal_defect_localized':bool(sig.get('known_proxy_constraints_reduce_to_one_higher_derivative_defect',False)),
 'spectral_to_amplitude_closure_architecture_demonstrated':bool(sig.get('finite_spectral_recurrence_can_predict_dispersive_Wilson_tower',False)),
 'physical_rank_or_recurrence_derived':False,
 'candidate_new_QG_primitive_found':False,
 'scientific_verdict':'The post-freeze constraints can be organized so that the unresolved finite theory data collapse to one higher-derivative/contact defect in the proxy. A finite spectral recurrence would mathematically predict that defect and an entire dispersive Wilson tower, with higher coefficients serving as prospective holdouts. But the physical origin of the recurrence/rank is still missing; choosing it is not new physics.',
 'next_target':'Search for an exact structural reason for finite spectral/transfer rank or a non-arbitrary recurrence: symmetry algebra closure, finite-state transfer law, meromorphic bootstrap uniqueness, or an RQIR operational composition axiom. Any proposal must predict the recurrence order and coefficients before seeing the holdouts.',
 'scope':'minimal-defect localization and spectral-to-dispersion closure architecture; not evidence that gravity has finite spectral rank or a new R^3 law'
}
Path('wave9_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
if missing:
    raise SystemExit(2)
