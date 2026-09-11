#!/usr/bin/env python3
import json
from pathlib import Path

root=Path('wave6_downloads')
items={}
for p in root.rglob('*.json'):
    try:
        items[p.stem]=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        items[p.stem]={"parse_error":str(e)}
required={
 'rg_fixed_point_predictivity','spectral_recurrence_closure','regge_tower_completion',
 'transfer_matrix_uv_degeneracy','comparator_identity_matrix'
}
missing=sorted(required-set(items))
sig={}
if 'rg_fixed_point_predictivity' in items:
 d=items['rg_fixed_point_predictivity']
 sig['finite_relevant_RG_surface_is_not_unique_trajectory']=d.get('uv_complete_trajectory_parameter_count',0)>0 and not d.get('unique_without_ir_boundary_data',True)
if 'spectral_recurrence_closure' in items:
 d=items['spectral_recurrence_closure']
 sig['finite_rank_recurrence_can_close_sequence']=d.get('rank3_recurrence_max_error',1)>-1 and d.get('rank3_recurrence_max_error',1)<1e-9
 sig['spectral_closure_needs_extra_rank_form_assumption']=bool(d.get('closure_requires_rank_assumption',False)) and any((r.get('width',0)>1e-10) for r in d.get('finite_moment_positive_measure_ranges',[]))
if 'regge_tower_completion' in items:
 d=items['regge_tower_completion']
 sig['finite_Regge_law_generates_infinite_tower_but_is_known_comparator']=bool(d.get('infinite_tower_generated',False)) and not d.get('candidate_novel_by_itself',True)
if 'transfer_matrix_uv_degeneracy' in items:
 d=items['transfer_matrix_uv_degeneracy']
 sig['same_IR_gap_leaves_positive_microscopic_transfer_family']=d.get('admissible_family_size',0)>1 and not d.get('unique_uv_rule_from_ir_gap',True)
if 'comparator_identity_matrix' in items:
 d=items['comparator_identity_matrix']
 sig['obvious_all_order_routes_fail_novelty_by_name_only']=d.get('routes_novel_by_name_only',1)==0

summary={
 'campaign':'post-freeze-all-order-wave6',
 'missing':missing,
 'signals':sig,
 'all_required_present':not missing,
 'candidate_all_order_primitive_found':False,
 'scientific_verdict':'Finite closure mechanisms exist, but the tested ones either leave relevant/boundary data, require an extra recurrence/rank axiom, or coincide with known comparators. No new comparator-orthogonal all-order primitive is earned by this wave.',
 'next_target':'Search for a cross-constraint that derives (rather than assumes) the RG relevant coordinates, spectral recurrence/rank, or tower-generating law from RQIR-compatible operational data.',
 'scope':'finite computational closure proxies plus comparator firewall; not a theorem excluding all quantum-gravity completions'
}
Path('wave6_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
if missing:
    raise SystemExit(2)
