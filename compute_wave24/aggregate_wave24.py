import json
from pathlib import Path

required={
 'rank':'rank_budget.json',
 'latent':'two_latent_generator.json',
 'retrofit':'full_rank_retrofit.json',
 'minimality':'minimum_complexity.json',
 'inequality':'inequality_region.json',
 'function':'functional_freedom.json',
 'acceptance':'acceptance_gate.json',
 'firewall':'information_firewall.json'
}

def find_one(filename):
    hits=list(Path('wave24_downloads').glob(f'**/{filename}'))
    return hits[0] if len(hits)==1 else None

loaded={}; missing=[]
for k,f in required.items():
    p=find_one(f)
    if p is None: missing.append(f)
    else: loaded[k]=json.loads(p.read_text())

signals={
 'scalar_relation_leaves_nullity_5':bool(loaded.get('rank',{}).get('scalar_relation_leaves_nullity_5',False)),
 'three_relation_class_leaves_nullity_3':bool(loaded.get('rank',{}).get('three_relation_class_leaves_nullity_3',False)),
 'two_latent_generator_is_predictive_inside_class':bool(loaded.get('latent',{}).get('two_latent_generator_is_predictive_inside_class',False)) and bool(loaded.get('latent',{}).get('design_rank_2',False)),
 'two_latent_generator_is_falsifiable_outside_class':bool(loaded.get('latent',{}).get('two_latent_generator_is_falsifiable_outside_class',False)),
 'arbitrary_full_rank_selectors_can_choose_conflicting_unique_points':bool(loaded.get('retrofit',{}).get('arbitrary_full_rank_selectors_can_choose_conflicting_unique_points',False)),
 'minimality_is_unique_but_not_physical_law':bool(loaded.get('minimality',{}).get('minimality_is_unique_but_not_physical_law',False)) and not bool(loaded.get('minimality',{}).get('parent_law_credit',True)),
 'inequality_consistency_region_is_nonunique':bool(loaded.get('inequality',{}).get('inequality_consistency_region_is_nonunique',False)),
 'unconstrained_function_interpolates_arbitrary_finite_holdout':bool(loaded.get('function',{}).get('unconstrained_function_interpolates_arbitrary_finite_holdout',False)) and not bool(loaded.get('function',{}).get('no_hidden_functional_freedom',True)),
 'no_tested_selector_earns_parent_law_credit':bool(loaded.get('acceptance',{}).get('no_tested_selector_earns_parent_law_credit',False)),
 'future_candidate_information_firewall_pass':bool(loaded.get('firewall',{}).get('future_candidate_information_firewall_pass',False))
}
all_present=len(missing)==0
all_true=all_present and all(signals.values())
out={
 'campaign':'parent-law-strength-wave24',
 'all_required_present':all_present,
 'missing':missing,
 'signals':signals,
 'all_predeclared_signals_true':all_true,
 'tested_parent_law_found':False,
 'minimum_local_closure_rank_required_from_unconstrained_6d_residual':6,
 'remaining_nullity_after_one_relation':loaded.get('rank',{}).get('S1_nullity'),
 'remaining_nullity_after_three_relations':loaded.get('rank',{}).get('S2_nullity'),
 'two_latent_out_of_family_residual':loaded.get('latent',{}).get('out_of_family_normalized_holdout_residual'),
 'conflicting_full_rank_prediction_distance':loaded.get('retrofit',{}).get('holdout_prediction_distance_l2'),
 'inequality_max_holdout_width':loaded.get('inequality',{}).get('maximum_holdout_width'),
 'functional_interpolation_error':loaded.get('function',{}).get('max_interpolation_error'),
 'scientific_verdict':('Wave 24 separates mathematical selector strength from scientific parent-law legitimacy. Partial equalities leave residual nullspaces; a compact two-latent generator can make prospective predictions and be falsified outside its class but lacks independent provenance/novelty; arbitrary full-rank selectors and minimum-complexity choices can each select unique representatives without physically earning them; inequality bounds remain nonunique; and one unconstrained function can hide enough pointwise freedom to interpolate the full finite holdout vector. Therefore the missing ingredient is not merely a rank-six algebraic condition but an independently motivated, comparator-distinct, prospectively predictive closure law with controlled functional freedom. No tested selector earns parent-law credit.' if all_true else 'Wave 24 failed at least one preregistered anti-retrofit gate. Do not weaken thresholds; inspect the failed signal before making a parent-law-strength claim.'),
 'scope':'Finite local six-dimensional residual proxy and frozen ten-probe prospective bank; not a theorem excluding all possible microscopic quantum-gravity principles.',
 'next_target':'If clean, freeze Parent-Law Acceptance Protocol v1 and use it prospectively. Continue independent KMQGB D2/D4/D7 closure. Only candidate principles with external provenance should enter a future principle tournament; they must be tested without changing the frozen Wave-22 bank.'
}
text=json.dumps(out,indent=2,sort_keys=True)
Path('wave24_summary.json').write_text(text)
print(text)
if not all_true:
    raise SystemExit(2)
