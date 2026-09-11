#!/usr/bin/env python3
import json,glob,os
from pathlib import Path
files=glob.glob('wave12_downloads/*/*.json')
data={os.path.basename(p):json.load(open(p,encoding='utf-8')) for p in files}
need=[
 'reversible_family_nonuniqueness.json',
 'polynomial_closure_uniqueness.json',
 'semigroup_ctmc_counterexample.json',
 'dynamical_holdout_discriminator.json',
 'comparator_firewall.json'
]
missing=[n for n in need if n not in data]
signals={
 'reversible_diffusion_family_survives_stationarity_detailed_balance_and_unit_gap': data.get('reversible_family_nonuniqueness.json',{}).get('same_stationary_density_and_unit_gap_leave_nonunique_higher_spectrum',False),
 'independent_markov_semigroup_counterexample_confirms_nonuniqueness': data.get('semigroup_ctmc_counterexample.json',{}).get('semigroup_positivity_stationarity_and_gap_do_not_fix_generator',False),
 'extra_polynomial_closure_selects_unique_generator_within_class': data.get('polynomial_closure_uniqueness.json',{}).get('unique_within_declared_polynomial_class_up_to_timescale',False),
 'selected_polynomial_generator_is_known_jacobi_wright_fisher_comparator': data.get('comparator_firewall.json',{}).get('polynomial_beta_generator_maps_to_known_jacobi_wright_fisher',False),
 'prospective_dynamical_holdouts_discriminate_surviving_generators': data.get('dynamical_holdout_discriminator.json',{}).get('dynamical_holdouts_discriminate_surviving_family',False)
}
all_required=(not missing) and all(signals.values())
out={
 'campaign':'post-freeze-generator-origin-wave12',
 'missing':missing,
 'signals':signals,
 'all_required_present':not missing,
 'semigroup_positivity_detailed_balance_gap_sufficient_to_derive_unique_generator':False,
 'polynomial_closure_can_force_uniqueness_but_is_known_comparator':bool(signals['extra_polynomial_closure_selects_unique_generator_within_class'] and signals['selected_polynomial_generator_is_known_jacobi_wright_fisher_comparator']),
 'candidate_new_QG_primitive_found':False,
 'scientific_verdict':'RQIR-like composition/semigroup, positivity, normalization, reversibility, a fixed stationary continuum and even a fixed leading relaxation gap do not uniquely determine the generator. Independent diffusion and finite-state Markov constructions retain different higher modes. An additional polynomial-closure axiom collapses the Beta case to the Jacobi/Wright-Fisher generator and the gap fixes its scale, but that is a known comparator rather than new quantum-gravity physics. Prospective time-domain holdouts can distinguish the surviving family. The missing ingredient must therefore be a QG-specific principle that fixes the mobility/kernel itself, not merely its semigroup structure or equilibrium measure.',
 'next_target':'Wave 13: test candidate QG-specific selectors of the mobility/kernel—scale/self-similarity, endpoint/soft behavior, Ward-like universality, entropy/contractivity, and cross-sector spectral-dispersive closure—while keeping at least one prospective dynamical holdout frozen. Reject any selector that is imposed solely because it reproduces Jacobi/Wright-Fisher or another known comparator.',
 'scope':'constructive nonuniqueness and closure tests in reversible diffusion/CTMC proxies; not a theorem for all QG generators.'
}
Path('wave12_summary.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
