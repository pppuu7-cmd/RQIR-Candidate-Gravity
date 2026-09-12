import json
from pathlib import Path

required={
 'authority_freshness':'authority_freshness.json',
 'decision_vector_convergence':'decision_vector_convergence.json',
 'obstruction_taxonomy':'obstruction_taxonomy.json',
 'promotion_gate_conjunction':'promotion_gate_conjunction.json',
 'contradiction_audit':'contradiction_audit.json',
 'information_independence':'information_independence.json',
 'anti_backwrite_firewall':'anti_backwrite_firewall.json'
}

def find_json(filename):
    hits=list(Path('wave21_downloads').glob(f'**/{filename}'))
    return hits[0] if len(hits)==1 else None

loaded={}
missing=[]
for key,filename in required.items():
    p=find_json(filename)
    if p is None:
        missing.append(filename)
    else:
        loaded[key]=json.loads(p.read_text())

signals={
 'exact_authority_snapshot_valid': bool(loaded.get('authority_freshness',{}).get('all_checks_pass',False)),
 'present_promotion_decision_converges': bool(loaded.get('decision_vector_convergence',{}).get('decision_convergence_pass',False)),
 'substantial_but_nonidentical_obstruction_overlap': bool(loaded.get('obstruction_taxonomy',{}).get('substantial_independent_overlap',False)) and bool(loaded.get('obstruction_taxonomy',{}).get('routes_not_identical',False)),
 'premature_promotion_fail_closed_on_both_routes': bool(loaded.get('promotion_gate_conjunction',{}).get('both_routes_fail_closed_against_premature_promotion',False)),
 'no_current_cross_route_contradiction': bool(loaded.get('contradiction_audit',{}).get('no_current_cross_route_contradiction',False)),
 'comparison_information_barrier_respected': bool(loaded.get('information_independence',{}).get('comparison_information_barrier_respected',False)),
 'no_backwrite_into_frozen_rqir': bool(loaded.get('anti_backwrite_firewall',{}).get('no_backwrite_into_frozen_rqir',False))
}
all_required_present=(len(missing)==0)
all_signals_true=all(signals.values()) and all_required_present
model_to_model_authorized=bool(loaded.get('promotion_gate_conjunction',{}).get('joint_blind_comparison_model_to_model_authorized',False))

out={
 'campaign':'blind-cross-route-wave21',
 'all_required_present':all_required_present,
 'missing':missing,
 'signals':signals,
 'all_predeclared_signals_true':all_signals_true,
 'obstruction_level_independent_convergence_supported':all_signals_true,
 'model_to_model_blind_comparison_authorized':model_to_model_authorized,
 'equation_level_convergence_claim_authorized':False,
 'candidate_new_QG_primitive_found':False,
 'scientific_verdict':('Wave 21 finds clean independent convergence at the obstruction/promotion-decision level: the frozen RQIR route and KMQGB Iter209 both withhold promotion of a unique new microscopic gravity theory, substantially overlap on upstream/rigidity/comparator/terminal-selection obstructions, and do so without being identical routes. There is no present cross-route contradiction and the information/backwrite firewall passes. This does not establish equation-level convergence. A true QGR-RQIR versus QGR-P comparison remains blocked until KMQGB freezes/promotes a concrete polygon-derived candidate.' if all_signals_true else 'Wave 21 did not close cleanly under the preregistered fail-closed criteria; inspect missing/false signals before drawing a cross-route conclusion.'),
 'scope':'Metadata/provenance/gate-level blind comparison against frozen KMQGB Iter209 snapshot; no polygon candidate equations or architecture imported.',
 'next_target':'Preserve the RQIR-v1 endpoint. Continue KMQGB independently toward D2/D4/D7 closure. Reopen model-to-model blind comparison only after a concrete polygon-derived QGR authority is frozen/promoted; then compare extra postulates, physical degrees of freedom, action/generating law, comparator status and prospective holdouts without tuning either route.'
}
text=json.dumps(out,indent=2,sort_keys=True)
Path('wave21_summary.json').write_text(text)
print(text)
if not all_signals_true:
    raise SystemExit(2)
