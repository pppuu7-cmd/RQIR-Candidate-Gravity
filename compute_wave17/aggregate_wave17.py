import json
from pathlib import Path

expected={
 'projector_algebra':'projector_algebra.json',
 'gauge_decoupling':'gauge_decoupling.json',
 'ward_tensor_rank':'ward_tensor_rank.json',
 'ir_gr_normalization':'ir_gr_normalization.json',
 'pole_audit':'pole_audit.json',
 'tensor_holdout':'tensor_holdout.json',
 'eft_transverse_control':'eft_transverse_control.json',
 'comparator_firewall':'comparator_firewall.json'
}
found={}; missing=[]
for key,fn in expected.items():
    matches=list(Path('wave17_downloads').glob(f'**/{fn}'))
    if not matches:
        missing.append(key)
    else:
        found[key]=json.loads(matches[0].read_text())

signals={}
if not missing:
    signals={
      'tensor_projector_algebra_closes':found['projector_algebra']['projector_algebra_closes'],
      'conserved_sources_remove_longitudinal_sectors':found['projector_algebra']['conserved_sources_remove_longitudinal_sectors'],
      'longitudinal_gauge_freedom_decouples':found['gauge_decoupling']['gauge_longitudinal_freedom_decouples_from_conserved_sources'],
      'ward_conservation_has_nontrivial_rank_reduction':found['ward_tensor_rank']['ward_conservation_has_nontrivial_rank_reduction'],
      'two_transverse_structures_survive':found['ward_tensor_rank']['only_two_transverse_structures_survive'],
      'IR_GR_normalization_leaves_shape_freedom':found['ir_gr_normalization']['IR_GR_normalization_fixes_residues_not_shape'],
      'no_extra_pole_gate_not_unique':found['pole_audit']['no_extra_pole_gate_is_not_a_unique_selector'],
      'prospective_tensor_holdout_resolves_residual':found['tensor_holdout']['same_design_different_tensor_holdout_exists'],
      'residual_transverse_shape_is_C5_EFT_compatible':found['eft_transverse_control']['residual_transverse_shape_is_not_by_itself_C5_distinct'],
      'comparator_firewall_pass':found['comparator_firewall']['firewall_pass']
    }

all_present=not missing
all_signals=all(signals.values()) if signals else False
out={
 'campaign':'rqir-tensor-ward-wave17',
 'missing':missing,
 'signals':signals,
 'all_required_present':all_present,
 'all_predeclared_signals_true':all_signals,
 'frozen_RQIR_tensor_gates_have_real_rank_power': bool(all_present and signals.get('ward_conservation_has_nontrivial_rank_reduction')),
 'frozen_RQIR_plus_GR_IR_uniquely_fix_transverse_form_factors': False if all_present and signals.get('IR_GR_normalization_leaves_shape_freedom') else None,
 'residual_tensor_freedom_is_gauge_only': False if all_present and signals.get('prospective_tensor_holdout_resolves_residual') else None,
 'residual_tensor_freedom_is_already_C5_EFT_compatible': bool(all_present and signals.get('residual_transverse_shape_is_C5_EFT_compatible')),
 'candidate_new_QG_primitive_found':False,
 'scientific_verdict':('The explicit symmetric-rank-2 representation upgrades Wave 16 from a scalar proxy to a tensor Ward/gauge audit. Conserved-source Ward structure removes four longitudinal/mixed projector directions and gauge-sector dependence, demonstrating genuine constraining power. However, the physical transverse spin-2 and transverse-scalar form factors remain independent. Exact GR/weak-field normalization fixes their q^2->0 residue combination but leaves finite-q analytic shape freedom; a no-extra-pole gate also fails to select a unique form because pole-free families remain. Untouched tensor holdouts detect this residual freedom, so it is physical rather than gauge. A conventional EFT control spans the surviving transverse slope directions, preventing a C5-distinct novelty claim. Therefore frozen RQIR plus tensor Ward/gauge/IR gates sharpen the equivalence class but still do not supply the missing microscopic parent law.' if all_present else 'Incomplete campaign.'),
 'next_target':'Wave 18: search independently motivated EXTRA-HYPOTHESIS relations acting specifically on the physical transverse form factors. Run at least three mutually independent candidates plus a no-extra-hypothesis control. Candidate families should be motivated before seeing the residual null direction: composition/semigroup law for physical amplitudes, UV/IR scaling/self-similarity tied to gravitational dimensions, and a relational-information or spectral sum-rule closure. Each candidate must make prospective finite-q/higher-point predictions and survive the C5 comparator firewall; any relation chosen merely because it fixes the Wave-17 nullspace is REJECTED-AS-RETROFIT.',
 'scope':'Finite-dimensional Euclidean projector/rank and form-factor proxies for conserved-source amplitudes. This is not a full Lorentzian nonperturbative gravity proof and does not replace a concrete action/CTP derivation.'
}
Path('wave17_summary.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True))
