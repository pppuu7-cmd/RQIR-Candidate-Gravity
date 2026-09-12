import json
from pathlib import Path

required={
 'rank':'rank_and_selection.json',
 'nuisance':'nuisance_robustness.json',
 'noise':'noise_stability.json',
 'cross_order':'cross_order_visibility.json',
 'comparator':'comparator_power.json',
 'firewall':'information_firewall.json',
 'coverage':'coverage_report.json',
 'ir_guard':'ir_guard.json'
}

def find_one(filename):
    hits=list(Path('wave22_downloads').glob(f'**/{filename}'))
    return hits[0] if len(hits)==1 else None

loaded={}; missing=[]
for key,filename in required.items():
    p=find_one(filename)
    if p is None: missing.append(filename)
    else: loaded[key]=json.loads(p.read_text())

signals={
 'full_pool_rank_6':bool(loaded.get('rank',{}).get('full_pool_rank_6',False)),
 'selected_bank_rank_6':bool(loaded.get('rank',{}).get('selected_rank_6',False)),
 'selected_condition_number_le_8':bool(loaded.get('rank',{}).get('condition_number_le_8',False)),
 'nuisance_profiled_rank_6':bool(loaded.get('nuisance',{}).get('profiled_rank_6',False)),
 'nuisance_profiled_min_sv_ge_0_15':bool(loaded.get('nuisance',{}).get('profiled_min_sv_ge_0_15',False)),
 'perturbation_full_rank_fraction_ge_0_99':bool(loaded.get('noise',{}).get('full_rank_fraction_ge_0_99',False)),
 'perturbation_q05_min_sv_ge_0_15':bool(loaded.get('noise',{}).get('min_sv_q05_ge_0_15',False)),
 'two_point_alone_does_not_close_higher_order':bool(loaded.get('cross_order',{}).get('two_point_only_cannot_identify_all_higher_order',False)),
 'cross_order_bank_resolves_four_higher_order_directions':bool(loaded.get('cross_order',{}).get('selected_bank_resolves_all_four_higher_order_directions',False)),
 'synthetic_comparators_are_separated':bool(loaded.get('comparator',{}).get('all_pairwise_nonzero',False)) and bool(loaded.get('comparator',{}).get('reference_and_all_deformation_classes_distinguished',False)),
 'future_candidate_information_firewall_pass':bool(loaded.get('firewall',{}).get('candidate_information_firewall_pass',False))
}
all_present=len(missing)==0
all_primary=all(signals.values()) and all_present

diagnostics={
 'sector_coverage_pass':bool(loaded.get('coverage',{}).get('sector_coverage_pass',False)),
 'ir_residual_sensitivities_vanish':bool(loaded.get('ir_guard',{}).get('residual_sensitivities_vanish_toward_ir_origin',False))
}

out={
 'campaign':'prospective-qgr-holdouts-wave22',
 'all_required_present':all_present,
 'missing':missing,
 'predeclared_signals':signals,
 'all_predeclared_signals_true':all_primary,
 'diagnostics':diagnostics,
 'candidate_blind_holdout_bank_ready':all_primary,
 'future_candidate_may_modify_frozen_bank':False,
 'selected_names':loaded.get('rank',{}).get('selected_names',[]),
 'selected_condition_number':loaded.get('rank',{}).get('condition_number'),
 'profiled_min_singular_value':loaded.get('nuisance',{}).get('profiled_min_singular_value'),
 'perturbation_full_rank_fraction':loaded.get('noise',{}).get('full_rank_fraction'),
 'perturbation_min_sv_q05':loaded.get('noise',{}).get('min_sv_q05'),
 'minimum_synthetic_comparator_distance':loaded.get('comparator',{}).get('minimum_pairwise_distance'),
 'scientific_verdict':('Wave 22 freezes a candidate-blind, full-rank prospective discriminator bank over the six declared RQIR residual proxy directions. The bank remains full-rank after sector-normalization nuisance profiling and seeded 2% sensitivity perturbations, explicitly restores visibility to higher-order directions invisible to 2-point data, and separates preregistered synthetic residual classes. It is therefore suitable as a frozen finite-proxy exam for a future QGR-P or other candidate. This is not an experimental-sensitivity forecast or a proof that the six-dimensional proxy spans all quantum-gravity deformations.' if all_primary else 'Wave 22 failed at least one preregistered holdout-bank gate; the bank is not certified and must not be used as a frozen future-candidate exam without a versioned redesign.'),
 'next_target':'Freeze the selected holdout bank and its coefficients if this run closes. Continue the polygon route independently. When a concrete QGR-P is frozen, evaluate it as a new row against this unchanged bank; do not reselect probes or thresholds after inspecting candidate predictions.'
}
text=json.dumps(out,indent=2,sort_keys=True)
Path('wave22_summary.json').write_text(text)
print(text)
if not all_primary:
    raise SystemExit(2)
