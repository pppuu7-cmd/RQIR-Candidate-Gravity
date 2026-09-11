#!/usr/bin/env python3
import json
from pathlib import Path

root=Path('wave8_downloads')
items={}
for p in root.rglob('*.json'):
    try:
        items[p.stem]=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        items[p.stem]={"parse_error":str(e)}
required={'dispersion_subtraction_closure','regge_contact_nullspace','joint_latent_holdout','running_dispersion_bookkeeping','dispersion_comparator_firewall'}
missing=sorted(required-set(items))
sig={}
if 'dispersion_subtraction_closure' in items:
    d=items['dispersion_subtraction_closure']
    sig['two_subtractions_leave_two_finite_data']=d.get('subtraction_constant_count_before_low_energy_inputs')==2
    sig['two_independent_inputs_close_subtractions_and_predict_holdout']=d.get('holdout_error_abs',1)>-1 and d.get('holdout_error_abs',1)<1e-10 and d.get('holdout_width_without_subtraction_inputs',0)>0
if 'regge_contact_nullspace' in items:
    d=items['regge_contact_nullspace']
    sig['s2_Regge_growth_truncates_but_does_not_close_contacts']=d.get('regge_allowed_dimension',0)>0 and not d.get('unique_after_regge_plus_soft_plus_one_fix',True)
if 'joint_latent_holdout' in items:
    d=items['joint_latent_holdout']
    sig['shared_latent_architecture_can_close_design_and_predict_holdout']=bool(d.get('linked_model_predicts_holdout',False))
    sig['unlinked_sector_model_retains_holdout_ambiguity']=bool(d.get('unlinked_model_has_holdout_ambiguity',False))
if 'running_dispersion_bookkeeping' in items:
    d=items['running_dispersion_bookkeeping']
    sig['naive_local_sign_not_scale_invariant_but_physical_sum_can_be']=bool(d.get('local_coefficient_changes_sign_over_scan',False)) and d.get('physical_sum_variation',1)<1e-12
if 'dispersion_comparator_firewall' in items:
    d=items['dispersion_comparator_firewall']
    sig['dispersion_Regge_route_is_established_comparator_territory']=not d.get('candidate_novelty_earned',True)

summary={
 'campaign':'post-freeze-joint-closure-wave8',
 'missing':missing,
 'signals':sig,
 'all_required_present':not missing,
 'joint_closure_architecture_demonstrated':bool(sig.get('shared_latent_architecture_can_close_design_and_predict_holdout',False)),
 'physical_cross_sector_law_derived':False,
 'candidate_new_QG_primitive_found':False,
 'scientific_verdict':'Two-subtraction/Regge information converts unlimited EFT ambiguity into a smaller finite-data problem but does not remove all subtraction/contact data. A shared finite primitive can mathematically close several sectors and predict a holdout, whereas an unlinked description remains ambiguous. The missing scientific step is to derive that shared map from an independent physical principle rather than choose it synthetically.',
 'next_target':'Search for a physically motivated cross-sector invariant or Ward/dispersion/RG relation that fixes at least one subtraction/contact datum from spectral or RG data and then test an untouched amplitude or response holdout.',
 'scope':'joint closure architecture, subtraction/contact counting and RG-consistent bookkeeping; not a derivation of a quantum-gravity microscopic law'
}
Path('wave8_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
if missing:
    raise SystemExit(2)
