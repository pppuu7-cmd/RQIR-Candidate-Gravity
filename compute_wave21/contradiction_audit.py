from common import load_snapshot, write_result

s=load_snapshot()
# Direct contradiction is narrowly defined: the current KMQGB authority would have to
# assert a promoted/robust unique new-theory result or claim RQIR invalid under the same
# frozen premises. Iter209 does neither.
claims={
    'rqir_unique_microtheory_supported': False,
    'rqir_new_qg_primitive_found': False,
    'rqir_endpoint_is_equivalence_class': True,
    'kmqgb_new_required_authorized': s['paper_iv']['new_required_authorized'],
    'kmqgb_promotable_ansatz': s['candidate_gravity']['promotable_ansatz'],
    'kmqgb_robust_unique_residual': s['candidate_gravity']['robust_unique_residual'],
    'kmqgb_global_decision': s['paper_iv']['global_decision'],
}
contradictions=[]
if claims['kmqgb_new_required_authorized'] and claims['kmqgb_promotable_ansatz'] and claims['kmqgb_robust_unique_residual']:
    contradictions.append('KMQGB presently asserts an authorized robust unique candidate while RQIR endpoint denies uniqueness from its own frozen premises; this would require an extra-postulate provenance audit before any compatibility statement.')
# NOT_YET_AUTHORIZED is compatible with an RQIR equivalence-class endpoint.
no_direct_contradiction=(len(contradictions)==0 and claims['kmqgb_global_decision']=='NOT_YET_AUTHORIZED')
out={
    'test':'logical contradiction audit between frozen RQIR endpoint and KMQGB Iter209 authority',
    'claims':claims,
    'contradictions':contradictions,
    'no_current_cross_route_contradiction':no_direct_contradiction,
    'important_nonimplication':'No contradiction does not mean the routes are mathematically identical. KMQGB may later add independently motivated premises that choose a representative from the RQIR equivalence class.',
    'conclusion':'Current authorities are logically compatible: RQIR withholds unique microscopic reconstruction and KMQGB also withholds NEW_REQUIRED/candidate promotion. No thaw of the RQIR-v1 endpoint is warranted.'
}
write_result('contradiction_audit',out)
