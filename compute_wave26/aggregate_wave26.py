import json, glob
from pathlib import Path
files=glob.glob('wave26_downloads/*/*.json')
data={Path(f).stem:json.loads(Path(f).read_text()) for f in files}
required=['canonical_transverse','random_orientation','aligned_redundancy','ward_positivity','rank_identity','acceptance_ledger','information_firewall']
missing=[k for k in required if k not in data]
signals={
 'canonical_transverse_examples_close_for_r_le_3':bool(data.get('canonical_transverse',{}).get('canonical_transverse_examples_close_for_r_le_3',False)),
 'r4_cannot_close_by_dimension_count':bool(data.get('rank_identity',{}).get('r4_cannot_close_by_dimension_count',False)),
 'random_orientation_closure_fraction_ge_0_99_for_r_le_3':bool(data.get('random_orientation',{}).get('random_orientation_closure_fraction_ge_0_99_for_r_le_3',False)),
 'aligned_redundancy_counterexamples_prevent_universal_closure':bool(data.get('aligned_redundancy',{}).get('aligned_redundancy_counterexamples_prevent_universal_closure',False)),
 'ward_positivity_intersection_nonunique':bool(data.get('ward_positivity',{}).get('ward_positivity_intersection_nonunique',False)),
 'principle_level_PL1_blocked_without_same_realization_transversality_map':bool(data.get('acceptance_ledger',{}).get('principle_level_PL1_blocked_without_same_realization_transversality_map',False)),
 'no_known_principle_combination_tested_here_earns_parent_law_credit':bool(data.get('acceptance_ledger',{}).get('no_known_principle_combination_tested_here_earns_parent_law_credit',False)),
 'future_candidate_information_firewall_pass':bool(data.get('information_firewall',{}).get('future_candidate_information_firewall_pass',False))
}
all_true=(not missing) and all(signals.values())
summary={
 'campaign':'principle-synergy-wave26',
 'all_required_present':not missing,
 'missing':missing,
 'signals':signals,
 'all_predeclared_signals_true':all_true,
 'random_orientation_cases':data.get('random_orientation',{}).get('cases'),
 'canonical_cases':data.get('canonical_transverse',{}).get('cases'),
 'aligned_counterexample_cases':data.get('aligned_redundancy',{}).get('cases'),
 'ward_positivity_max_prediction_width':data.get('ward_positivity',{}).get('max_frozen_bank_prediction_width'),
 'rank_identity_verified':data.get('rank_identity',{}).get('rank_identity_and_transversality_condition_verified'),
 'known_combination_parent_law_found':False,
 'scientific_verdict':'Wave 26 establishes conditional rank synergy but not a unique known-principle parent law. Ward plus fixed-point constraints can close the six-dimensional finite proxy for transverse realizations with at most three relevant directions, and random orientations are generically transverse in that proxy. However explicit full-rank fixed-point constraint spaces with extra Ward overlap leave residual nullities, proving that closure is not guaranteed by the abstract principle labels. Ward plus positivity also remains a finite-width continuum. Therefore PL1 at principle-class level remains BLOCKED until a concrete same-realization microscopic-to-RQIR map proves the required transversality without double counting gauge/Ward consistency.',
 'next_target':'Freeze the Wave-26 transversality certificate if clean. Then search for or derive the missing same-realization microscopic-to-RQIR Jacobian/tangent map for the most promising UV principle rather than adding more abstract constraints.'
}
Path('wave26_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True))
print(json.dumps(summary,indent=2,sort_keys=True))
if not all_true: raise SystemExit(1)
