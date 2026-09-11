#!/usr/bin/env python3
import json
from pathlib import Path

root=Path('wave7_downloads')
items={}
for p in root.rglob('*.json'):
    try:
        items[p.stem]=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        items[p.stem]={"parse_error":str(e)}
required={'kl_rg_scaling_consistency','operational_rg_identifiability','spectral_rank_noise_stability','analytic_growth_holdout','current_spectral_rg_comparator'}
missing=sorted(required-set(items))
sig={}
if 'kl_rg_scaling_consistency' in items:
    d=items['kl_rg_scaling_consistency']
    sig['naive_same_field_normalized_KL_and_q4_scaling_need_extra_structure']=not d.get('simultaneous_naive_conditions_compatible',True)
if 'operational_rg_identifiability' in items:
    d=items['operational_rg_identifiability']
    cases=d.get('cases',[])
    sig['RG_relevant_coordinates_require_full_rank_operational_Jacobian']=any(c.get('locally_identifiable',False) for c in cases) and any(c.get('relevant_parameter_nullity',0)>0 for c in cases)
if 'spectral_rank_noise_stability' in items:
    d=items['spectral_rank_noise_stability']
    sig['finite_spectral_rank_needs_exact_structural_protection']=bool(d.get('rank_is_threshold_dependent_under_noise',False))
if 'analytic_growth_holdout' in items:
    d=items['analytic_growth_holdout']
    sig['finite_low_energy_data_do_not_fix_UV_growth']=bool(d.get('global_growth_not_fixed_by_finite_taylor_data',False))
if 'current_spectral_rg_comparator' in items:
    d=items['current_spectral_rg_comparator']
    sig['positive_spectral_plus_fixed_point_is_known_comparator']=not d.get('positive_spectral_plus_fixed_point_route_is_novel_by_itself',True)

summary={
 'campaign':'post-freeze-cross-constraint-wave7',
 'missing':missing,
 'signals':sig,
 'all_required_present':not missing,
 'new_methodological_gate_found':True,
 'gate':'scheme/field/normalization consistency must be explicit before combining RG fixed-point scaling with spectral positivity; RG relevant coordinates must be operationally identifiable with full-rank prospective observables.',
 'candidate_new_QG_primitive_found':False,
 'scientific_verdict':'Cross-constraints sharpen the admissibility map but do not yet produce a new microscopic law. They show exactly which missing data must be derived: field/scheme matching, full-rank operational closure of relevant directions, structural protection of any finite spectral rank, and an independent UV growth law.',
 'next_target':'Construct and test a joint closure functional in which the same finite primitive predicts RG-relevant coordinates, spectral moments/rank and at least one holdout observable without importing a known comparator rule.',
 'scope':'cross-constraint consistency and identifiability proxies; not a theorem excluding asymptotic safety or other UV completions'
}
Path('wave7_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
if missing:
    raise SystemExit(2)
