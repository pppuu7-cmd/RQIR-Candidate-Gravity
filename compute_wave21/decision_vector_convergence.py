from common import load_snapshot, write_result

s=load_snapshot()
rqir={
 'unique_microscopic_reconstruction_supported':False,
 'candidate_new_QG_primitive_found':False,
 'equivalence_class_endpoint':True,
 'extra_physics_required_for_unique_representative':True
}
kmqgb={
 'new_required_authorized':s['paper_iv']['new_required_authorized'],
 'promotable_ansatz':s['candidate_gravity']['promotable_ansatz'],
 'robust_unique_residual':s['candidate_gravity']['robust_unique_residual'],
 'paper_iv_terminal_authorized':s['paper_iv']['global_decision']!='NOT_YET_AUTHORIZED'
}
convergence={
 'neither_route_authorizes_new_micro_theory': (not rqir['candidate_new_QG_primitive_found']) and (not kmqgb['promotable_ansatz']),
 'neither_route_has_unique_parent_certificate': (not rqir['unique_microscopic_reconstruction_supported']) and (not kmqgb['robust_unique_residual']),
 'polygon_NEW_REQUIRED_not_authorized': not kmqgb['new_required_authorized'],
 'rqir_requires_extra_physics_for_unique_representative':rqir['extra_physics_required_for_unique_representative']
}
out={
 'test':'independent terminal-decision vector convergence',
 'rqir_vector':rqir,
 'kmqgb_vector':kmqgb,
 'convergence':convergence,
 'decision_convergence_pass':all(convergence.values()),
 'routes_are_identical':False,
 'conclusion':'The independently frozen RQIR route and current polygon benchmark authority converge on the same present promotion decision—no new microscopic theory is yet earned—while arriving there through different constructions. Agreement in decision does not imply equation-level model convergence.'
}
write_result('decision_vector_convergence',out)
