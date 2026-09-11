import json
from pathlib import Path

files={
 'single_action':'single_action_rank.json',
 'field_redef':'field_redefinition_quotient.json',
 'ward':'background_ward_action_rank.json',
 'bound':'four_point_bound.json',
 'minimality':'minimality_selector.json',
 'uv':'uv_gap_selector.json',
 'witness':'endpoint_witness.json',
 'firewall':'comparator_firewall.json'
}
found={}; missing=[]
for k,fn in files.items():
    m=list(Path('wave20_downloads').glob(f'**/{fn}'))
    if not m: missing.append(k)
    else: found[k]=json.loads(m[0].read_text())
signals={}
if not missing:
    signals={
      'single_action_still_has_cross_order_Wilson_freedom':found['single_action']['same_action_still_has_cross_order_Wilson_freedom'],
      'field_redefinition_quotient_leaves_physical_cubic_directions':found['field_redef']['field_redefinitions_remove_redundant_but_not_all_cubic_directions'],
      'background_Ward_leaves_transverse_action_freedom':found['ward']['background_Ward_identity_leaves_physical_transverse_action_freedom'],
      'four_point_bounds_reduce_but_do_not_identify_cubic_coefficient':found['bound']['higher_point_bound_reduces_but_does_not_identify_cubic_coefficient'],
      'minimality_selects_a_representative_but_is_not_physical_law':found['minimality']['minimality_selects_zero_inside_proxy'] and found['minimality']['minimality_is_not_equivalent_to_physical_constraint'],
      'UV_gap_information_does_not_uniquely_select_finite_gap_coefficient':found['uv']['finite_gap_bound_not_unique'],
      'explicit_action_level_endpoint_witness_survives':found['witness']['same_low_order_and_gates_different_physical_higher_point_prediction'] and found['witness']['both_actions_admissible_under_proxy_gates'],
      'comparator_firewall_pass':found['firewall']['firewall_pass']
    }
all_present=not missing
all_true=bool(signals) and all(signals.values())
out={
 'campaign':'action-level-no-go-wave20',
 'missing':missing,
 'signals':signals,
 'all_required_present':all_present,
 'all_predeclared_signals_true':all_true,
 'one_action_plus_RQIR_gates_uniquely_determines_all_higher_order_Wilson_coefficients':False if all_present else None,
 'field_redefinition_and_background_Ward_remove_all_physical_cubic_freedom':False if all_present else None,
 'known_amplitude_UV_constraints_make_the_action_unique':False if all_present else None,
 'candidate_new_QG_primitive_found':False,
 'RQIR_only_unique_microscopic_reconstruction_supported':False if all_present else None,
 'freeze_equivalence_class_endpoint_recommended':bool(all_present and all_true),
 'scientific_verdict':('Wave 20 lifts the cross-order underdetermination to the action level. A single covariant action enforces common dynamics but can contain independent physical Wilson coefficients that first enter at cubic and higher order, so two-point data do not determine them. Quotienting EOM/field-redefinition redundancies and enforcing nonlinear/background Ward identities removes unphysical/longitudinal structure but leaves physical transverse action directions. Four-point dispersive/positivity-style information and UV-gap/causality information can correlate or bound these coefficients without selecting a unique value, while minimum-complexity can choose the zero-coefficient representative only as a model-selection convention. An explicit pair of admissible one-action witnesses then shares the selected lower-order/gate information yet differs in a finite three-point prediction. Within the declared finite proxies, this certifies the logical endpoint of frozen RQIR-only reconstruction: a constrained equivalence class, not a unique microscopic theory. No new QG primitive is found.' if all_present else 'Incomplete campaign.'),
 'next_target':'If this wave closes cleanly, freeze an RQIR-ONLY ACTION-LEVEL NO-GO/ENDPOINT certificate. After that, the scientifically clean next move is blind comparison with the independently developed polygon-QGR branch: identify which extra postulate(s) QGR-P uses to choose a representative from the RQIR equivalence class, test whether those postulates have independent provenance, and cross-validate their genuinely new predictions without back-writing them into the RQIR derivation.',
 'scope':'Finite-dimensional action/operator rank and inequality proxies, with explicit fail-closed comparator semantics. This is not a complete classification theorem over all covariant quantum-gravity actions or UV completions.'
}
Path('wave20_summary.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True))
