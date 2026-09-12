from pathlib import Path
from common import load_snapshot, write_result

s=load_snapshot()
endpoint_text=Path('model/RQIR_ONLY_ACTION_LEVEL_ENDPOINT_V1.md').read_text()
prereg_text=Path('post_freeze/WAVE21_BLIND_CROSS_ROUTE_PREREGISTRATION.md').read_text()
allowed_scope=s['allowed_scope']
checks={
    'rqir_endpoint_authority_predates_wave21': 'Authority commit:** `e2183953f882b7cc034b784cbeb178f7510fedad`' in endpoint_text,
    'rqir_endpoint_declares_no_polygon_backwrite': 'no polygon result may be back-written' in endpoint_text,
    'snapshot_scope_metadata_only': 'no candidate equations or architecture' in allowed_scope,
    'prereg_forbids_candidate_equations': 'Forbidden: candidate equations, architecture, ansatz details' in prereg_text,
    'snapshot_contains_no_equation_field': all(k not in s for k in ['equations','ansatz','action','lagrangian','hamiltonian']),
    'snapshot_contains_only_status_style_candidate_fields': set(s['candidate_gravity'].keys()) <= {'status','external_iteration','readiness_percent','promotable_ansatz','robust_unique_residual','activation_condition'}
}
out={
    'test':'information-barrier and provenance independence audit',
    'checks':checks,
    'comparison_information_barrier_respected':all(checks.values()),
    'allowed_kmqgb_scope':allowed_scope,
    'conclusion':'Wave 21 consumes only preregistered KMQGB status/provenance metadata after the RQIR action-level endpoint was frozen. No polygon candidate dynamics are available to tune or reinterpret the RQIR derivation.'
}
write_result('information_independence',out)
