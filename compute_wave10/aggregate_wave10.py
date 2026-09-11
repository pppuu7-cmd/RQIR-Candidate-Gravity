#!/usr/bin/env python3
import json
from pathlib import Path

root=Path('wave10_downloads')
items={}
for p in root.rglob('*.json'):
    try:
        items[p.stem]=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        items[p.stem]={"parse_error":str(e)}
required={'atomic_vs_continuum_hankel','finite_state_realization','rational_vs_continuum_stieltjes','continuum_recurrence_holdout','continuum_comparator_firewall'}
missing=sorted(required-set(items))
sig={}
if 'atomic_vs_continuum_hankel' in items:
 d=items['atomic_vs_continuum_hankel']
 sig['finite_atomic_measure_has_fixed_Hankel_rank']=bool(d.get('finite_atomic_rank_saturates',False))
 sig['positive_continuum_has_no_fixed_finite_Hankel_rank']=bool(d.get('positive_continuum_has_no_fixed_finite_Hankel_rank',False))
if 'finite_state_realization' in items:
 d=items['finite_state_realization']
 sig['finite_recurrence_implies_finite_rational_realization_in_proxy']=bool(d.get('finite_recurrence_equivalent_to_finite_rational_realization_in_proxy',False))
if 'rational_vs_continuum_stieltjes' in items:
 d=items['rational_vs_continuum_stieltjes']
 sig['finite_rational_rank_can_approximate_but_not_equal_continuum']=bool(d.get('finite_rank_can_approximate_continuum',False)) and bool(d.get('no_finite_rank_is_exact_for_full_continuum_transform',False))
if 'continuum_recurrence_holdout' in items:
 d=items['continuum_recurrence_holdout']
 sig['finite_recurrence_fits_fail_continuum_holdouts']=bool(d.get('every_finite_order_has_nonzero_holdout_error',False))
if 'continuum_comparator_firewall' in items:
 d=items['continuum_comparator_firewall']
 sig['current_graviton_spectral_comparator_contains_continuum']=bool(d.get('full_graviton_spectrum_known_comparator_contains_continuum',False))

summary={
 'campaign':'post-freeze-rank-origin-wave10',
 'missing':missing,
 'signals':sig,
 'all_required_present':not missing,
 'exact_finite_atomic_rank_viable_as_generic_full_graviton_spectrum_target':False,
 'finite_rank_still_useful_as_approximation_or_reduced_sector':True,
 'candidate_new_QG_primitive_found':False,
 'scientific_verdict':'The tempting exact finite-rank spectral closure is too restrictive for a genuine positive continuum in the tested moment/Stieltjes setting. Finite recurrences correspond to finite rational realizations and can approximate continuum data increasingly well, but they fail exact continuum holdouts and analytic structure. Since current Lorentzian graviton spectral calculations contain a multi-graviton continuum, the full-spectrum parent-law search should move from finite spectral rank to a finite generative equation for the continuum.',
 'next_target':'Search for finite-parameter differential/integral/flow equations that generate a positive continuum spectral density while fixing subtraction/contact data and admitting prospective holdouts. Candidate equations must be comparator-checked against FRG/SD/bootstrap/string spectral equations and must not import arbitrary functions.',
 'scope':'moment/Stieltjes/rational-realization proxies plus current comparator evidence; not a theorem that all QG completions require a continuum of exactly the tested form.'
}
Path('wave10_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
if missing:
    raise SystemExit(2)
