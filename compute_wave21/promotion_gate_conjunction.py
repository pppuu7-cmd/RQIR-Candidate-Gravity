from common import load_snapshot, write_result

s=load_snapshot()
rqir_gates={
 'endpoint_frozen':True,
 'unique_microtheory_earned':False,
 'new_QG_primitive_found':False
}
kmqgb_gates={
 'D2A_closed':s['paper_iv']['D2A_framework_set_coverage']=='CLOSED',
 'D2B_closed':s['paper_iv']['D2B_complete_same_realization_objects']=='CLOSED',
 'D4_closed':s['paper_iv']['D4_comparator_subtracted_residual_matrix']=='CLOSED',
 'D7_closed':s['paper_iv']['D7_global_terminal_proof_obligation']=='CLOSED',
 'NEW_REQUIRED':s['paper_iv']['new_required_authorized'],
 'promotable_ansatz':s['candidate_gravity']['promotable_ansatz']
}
kmqgb_promotion=all(kmqgb_gates.values())
rqir_promotion=rqir_gates['unique_microtheory_earned'] and rqir_gates['new_QG_primitive_found']
out={
 'test':'independent promotion-gate conjunction',
 'rqir_gates':rqir_gates,
 'kmqgb_gates':kmqgb_gates,
 'rqir_promote_new_microtheory':rqir_promotion,
 'kmqgb_promote_polygon_candidate':kmqgb_promotion,
 'joint_blind_comparison_model_to_model_authorized':rqir_gates['endpoint_frozen'] and kmqgb_promotion,
 'both_routes_fail_closed_against_premature_promotion':(not rqir_promotion) and (not kmqgb_promotion),
 'conclusion':'Each route is evaluated by its own frozen logic. RQIR has a frozen endpoint but no unique primitive; KMQGB has not closed D2/D4/D7 and has no promotable ansatz. Therefore model-to-model blind comparison remains blocked, while obstruction-level comparison is admissible.'
}
write_result('promotion_gate_conjunction',out)
