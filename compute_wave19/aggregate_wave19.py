import json
from pathlib import Path

files={
 'ward':'ward_cross_order_rank.json',
 'soft':'soft_contact_freedom.json',
 'eft':'cubic_only_eft_control.json',
 'causality':'causality_inequality.json',
 'product':'same_generating_product_law.json',
 'holdout':'cross_order_holdout.json',
 'firewall':'comparator_firewall.json'
}
found={}; missing=[]
for k,fn in files.items():
    m=list(Path('wave19_downloads').glob(f'**/{fn}'))
    if not m: missing.append(k)
    else: found[k]=json.loads(m[0].read_text())
signals={}
if not missing:
    signals={
      'Ward_cross_order_constraints_leave_transverse_vertex_freedom':found['ward']['ward_fixes_longitudinal_not_transverse'],
      'soft_constraints_leave_higher_derivative_contact_freedom':found['soft']['leading_and_first_subleading_soft_data_leave_contact_freedom'],
      'C5_EFT_has_cubic_only_cross_order_direction':found['eft']['cubic_only_direction_exists_in_EFT_proxy'],
      'causality_inequality_not_unique_selector':found['causality']['causality_gate_reduces_domain_but_not_unique'],
      'strong_same_generating_product_law_is_predictive_inside_restricted_class':found['product']['cross_order_predictive_inside_restricted_product_class'],
      'same_two_point_and_soft_data_can_differ_at_three_point_holdout':found['holdout']['cross_order_degeneracy_exists'],
      'comparator_firewall_pass':found['firewall']['firewall_pass']
    }
all_present=not missing
out={
 'campaign':'cross-order-closure-wave19',
 'missing':missing,
 'signals':signals,
 'all_required_present':all_present,
 'all_predeclared_signals_true':bool(signals) and all(signals.values()),
 'frozen_Ward_soft_causality_uniquely_determine_three_point_from_two_point':False if all_present else None,
 'C5_EFT_cross_order_obstruction_present':bool(all_present and signals.get('C5_EFT_has_cubic_only_cross_order_direction')),
 'restricted_product_law_demonstrates_required_selector_strength':bool(all_present and signals.get('strong_same_generating_product_law_is_predictive_inside_restricted_class')),
 'restricted_product_law_is_derived_new_QG_primitive':False,
 'candidate_new_QG_primitive_found':False,
 'scientific_verdict':('Wave 19 moves the underdetermination from a two-point form-factor issue to an explicit cross-order statement. Ward identities constrain longitudinal three-point components but leave transverse vertex directions. Leading/subleading soft information and a causality inequality further restrict admissibility without uniquely fixing higher-derivative transverse contacts. A curvature-cubed EFT control supplies a concrete C5-compatible direction that changes the three-graviton interaction while leaving the leading two-point kernel unchanged. A finite three-point holdout therefore distinguishes candidates that are identical in the selected two-point and soft/Ward data. A deliberately stronger same-generating product law can make cross-order predictions with no new vertex parameters, demonstrating the selector strength required, but that product rule is an extra modeling postulate and not an RQIR-derived or C5-distinct law. Thus the missing ingredient is now localized to an independently motivated cross-order dynamical closure principle.' if all_present else 'Incomplete campaign.'),
 'next_target':'Wave 20: search for genuinely gravity-specific cross-order closure candidates rather than generic factorisation. Test whether nonlinear diffeomorphism/background-field identities plus a concrete action/generating functional can reduce the cubic-only EFT freedom, and compare against explicit R^3/Weyl^3 controls. If no independent law removes the cubic-only direction, freeze the RQIR-derived endpoint as an equivalence class plus a quantified no-go for unique microscopic reconstruction.',
 'scope':'Finite-dimensional cross-order rank/visibility proxies and perturbative degree counting; not a full on-shell amplitude classification or nonperturbative proof.'
}
Path('wave19_summary.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True))
