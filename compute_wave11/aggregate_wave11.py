#!/usr/bin/env python3
import json
from pathlib import Path

root=Path('wave11_downloads')
items={}
for p in root.rglob('*.json'):
    try:
        items[p.stem]=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        items[p.stem]={"parse_error":str(e)}
required={'beta_continuum_generator','continuum_stieltjes_holdout','low_moment_generator_nonuniqueness','continuum_to_wilson_tower','continuum_generator_comparator_firewall'}
missing=sorted(required-set(items))
sig={}
if 'beta_continuum_generator' in items:
 d=items['beta_continuum_generator']
 sig['finite_differential_law_can_generate_positive_continuum_and_all_order_moments']=bool(d.get('finite_generator_with_continuum_and_infinite_moment_tower',False)) and d.get('holdout_max_error',1)<1e-9
if 'continuum_stieltjes_holdout' in items:
 d=items['continuum_stieltjes_holdout']
 sig['finite_generator_predicts_nonlocal_integral_holdouts']=bool(d.get('integral_holdouts_pass',False))
if 'low_moment_generator_nonuniqueness' in items:
 d=items['low_moment_generator_nonuniqueness']
 sig['finite_low_moments_do_not_derive_continuum_generator']=bool(d.get('finite_low_moments_do_not_derive_generator',False))
if 'continuum_to_wilson_tower' in items:
 d=items['continuum_to_wilson_tower']
 sig['continuum_generator_can_close_Wilson_tower_without_finite_Hankel_rank']=bool(d.get('finite_generator_closes_infinite_Wilson_tower_without_finite_Hankel_rank',False)) and d.get('max_ratio_error',1)<1e-12
if 'continuum_generator_comparator_firewall' in items:
 d=items['continuum_generator_comparator_firewall']
 sig['synthetic_continuum_generator_is_not_novel_physics']=not d.get('candidate_novelty_earned',True)

summary={
 'campaign':'post-freeze-continuum-generator-wave11',
 'missing':missing,
 'signals':sig,
 'all_required_present':not missing,
 'finite_continuum_generator_architecture_validated':bool(sig.get('finite_differential_law_can_generate_positive_continuum_and_all_order_moments',False)) and bool(sig.get('continuum_generator_can_close_Wilson_tower_without_finite_Hankel_rank',False)),
 'generator_equation_physically_derived':False,
 'candidate_new_QG_primitive_found':False,
 'scientific_verdict':'Finite-parent closure does not require finite spectral rank. A finite differential/generative law can produce a positive continuum, an infinite moment/Wilson tower and prospective integral holdouts through n-dependent recurrences. This resolves the architectural conflict exposed by Wave 10. But low moments alone do not determine the generator, and the synthetic generator is not new physics. The remaining problem is now the physical origin of the continuum-generating equation.',
 'next_target':'Derive candidate continuum-generator equations from an RQIR operational composition/semigroup principle, Ward/causality structure, or another finite microscopic axiom; then freeze the equation before fitting and test independent spectral, dispersive and apparatus-level holdouts. Comparator-check against FRG/SD/spectral-bootstrap equations before novelty claims.',
 'scope':'continuum-generator architecture and identifiability proxies; no claim that the Beta generator describes gravitons.'
}
Path('wave11_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
if missing:
    raise SystemExit(2)
