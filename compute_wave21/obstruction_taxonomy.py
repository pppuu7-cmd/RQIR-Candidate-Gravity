from common import load_snapshot, write_result

s=load_snapshot()
categories=['UPSTREAM_PRIMITIVE_FREEDOM','SAME_REALIZATION_PROVENANCE','FUNCTIONAL_OR_HIGHER_ORDER_RIGIDITY','COMPARATOR_CLOSURE','TERMINAL_PROMOTION_PROOF']
rqir={
 'UPSTREAM_PRIMITIVE_FREEDOM':True,
 'SAME_REALIZATION_PROVENANCE':False,
 'FUNCTIONAL_OR_HIGHER_ORDER_RIGIDITY':True,
 'COMPARATOR_CLOSURE':True,
 'TERMINAL_PROMOTION_PROOF':True
}
kmqgb={
 'UPSTREAM_PRIMITIVE_FREEDOM':not s['candidate_gravity']['robust_unique_residual'],
 'SAME_REALIZATION_PROVENANCE':s['paper_iv']['D2B_complete_same_realization_objects']=='NOT_CLOSED',
 'FUNCTIONAL_OR_HIGHER_ORDER_RIGIDITY':not s['candidate_gravity']['robust_unique_residual'],
 'COMPARATOR_CLOSURE':s['paper_iv']['D4_comparator_subtracted_residual_matrix']!='CLOSED',
 'TERMINAL_PROMOTION_PROOF':s['paper_iv']['D7_global_terminal_proof_obligation']=='NOT_CLOSED'
}
common=[c for c in categories if rqir[c] and kmqgb[c]]
rqir_only=[c for c in categories if rqir[c] and not kmqgb[c]]
kmqgb_only=[c for c in categories if kmqgb[c] and not rqir[c]]
union=[c for c in categories if rqir[c] or kmqgb[c]]
jaccard=len(common)/len(union) if union else 1.0
out={
 'test':'cross-route obstruction taxonomy overlap',
 'categories':categories,
 'rqir_obstructions':rqir,
 'kmqgb_obstructions':kmqgb,
 'common_active_obstructions':common,
 'rqir_only_active_obstructions':rqir_only,
 'kmqgb_only_active_obstructions':kmqgb_only,
 'jaccard_overlap':jaccard,
 'substantial_independent_overlap':len(common)>=3,
 'routes_not_identical':rqir!=kmqgb,
 'conclusion':'The routes substantially overlap on upstream/rigidity/comparator/terminal-selection obstructions, but are not duplicates: KMQGB still has a live same-realization-provenance coverage obstruction, while frozen RQIR localizes residual freedom at higher-order physical action data.'
}
write_result('obstruction_taxonomy',out)
