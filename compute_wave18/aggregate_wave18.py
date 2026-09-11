import json
from pathlib import Path

expected={
 'h0':'h0_control.json',
 'h1':'h1_common_entire.json',
 'h2':'h2_semigroup.json',
 'h3':'h3_spectral.json',
 'h4':'h4_rg_fixed_point.json',
 'class_id':'class_identifiability.json',
 'firewall':'comparator_firewall.json'
}
found={}; missing=[]
for key,fn in expected.items():
    m=list(Path('wave18_downloads').glob(f'**/{fn}'))
    if not m: missing.append(key)
    else: found[key]=json.loads(m[0].read_text())

signals={}
if not missing:
    signals={
      'H0_underdetermination_survives':found['h0']['undertermination_survives'],
      'H1_common_entire_reduces_but_does_not_close_shape':found['h1']['common_entire_factor_reduces_but_does_not_close_shape'],
      'H2_semigroup_plus_one_design_closes_tested_finite_class':found['h2']['composition_plus_one_design_closes_this_finite_class'],
      'H3_positive_spectral_representation_remains_nonunique':found['h3']['spectral_positivity_and_one_design_do_not_close_shape'],
      'H4_UV_fixed_point_does_not_select_trajectory':found['h4']['UV_fixed_point_alone_does_not_select_trajectory'],
      'equation_class_not_identified_by_low_q_fit':found['class_id']['equation_class_is_not_identified_by_low_q_fit'],
      'comparator_firewall_pass':found['firewall']['firewall_pass']
    }
all_present=not missing
all_true=all(signals.values()) if signals else False
h2_predictive=bool(all_present and signals.get('H2_semigroup_plus_one_design_closes_tested_finite_class'))
out={
 'campaign':'extra-hypothesis-wave18',
 'missing':missing,
 'signals':signals,
 'all_required_present':all_present,
 'all_predeclared_signals_true':all_true,
 'mathematically_strongest_selector_in_tested_finite_classes':'H2_semigroup' if h2_predictive else None,
 'mathematical_finite_class_closure_equals_physical_uniqueness':False,
 'candidate_new_QG_primitive_found':False,
 'promote_any_wave18_class_to_new_QG':False,
 'scientific_verdict':('The no-extra control retains the physical transverse ambiguity. A shared zero-free entire dressing, a positive spectral/Stieltjes representation, and a UV-fixed-point critical-surface proxy all reduce structure but leave prospective finite-q freedom. A multiplicative scale-composition law is much stronger: on the preregistered cubic log-form-factor class it collapses the shape to an exponential one-parameter family, so one low-q design value predicts the holdout. However, this is closure inside a chosen functional class, not a gravity-specific derivation, and the comparator firewall assigns it no novelty credit. Moreover, independently motivated equation classes can all match the same low-q design point while predicting different untouched holdouts. Therefore Wave 18 identifies a useful selector property—functional composition can create predictivity—but no uniquely justified C5-distinct parent law.' if all_present else 'Incomplete campaign.'),
 'next_target':'Wave 19: move beyond two-point shape selection. Test gravity-specific cross-order identities that link the physical two-point transverse dressing to independently computed three-point/response structure. Candidate sources must be motivated without reference to Wave-17/18 null vectors: nonlinear diffeomorphism/Ward identities, soft-graviton consistency/eikonal-causality relations, and a same-CTP generating-law closure. Require one law to predict both two-point finite-q and a higher-point holdout with the same parameters; compare directly against C5/EFT freedom.',
 'scope':'Finite functional-class discrimination on a dimensionless transverse dressing proxy. It establishes identifiability/non-identifiability properties of candidate principles, not a microscopic quantum-gravity theory.'
}
Path('wave18_summary.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True))
