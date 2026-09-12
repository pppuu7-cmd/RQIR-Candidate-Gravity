from pathlib import Path
from common import load_snapshot, write_result

s=load_snapshot()
endpoint=Path('model/RQIR_ONLY_ACTION_LEVEL_ENDPOINT_V1.md')
checks={
 'source_repo_exact':s['source_repository']=='pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark',
 'source_file_exact':s['source_file']=='recovery/state.json',
 'source_blob_sha_exact':s['source_blob_sha']=='55b77c8ec0c3541406aa0dd4a4de5fcd4e8da6b3',
 'iteration_exact':s['kmqgb_iteration']==209,
 'candidate_readiness_exact':s['candidate_gravity']['readiness_percent']==24,
 'paper_iv_not_authorized':s['paper_iv']['global_decision']=='NOT_YET_AUTHORIZED',
 'new_required_false':s['paper_iv']['new_required_authorized'] is False,
 'promotable_ansatz_false':s['candidate_gravity']['promotable_ansatz'] is False,
 'robust_unique_residual_false':s['candidate_gravity']['robust_unique_residual'] is False,
 'rqir_endpoint_present':endpoint.exists() and 'FROZEN RQIR-ONLY ENDPOINT' in endpoint.read_text()
}
out={
 'test':'authority freshness and exact-snapshot validation',
 'checks':checks,
 'all_checks_pass':all(checks.values()),
 'snapshot_source_blob_sha':s['source_blob_sha'],
 'kmqgb_iteration':s['kmqgb_iteration'],
 'conclusion':'Wave 21 compares the frozen RQIR endpoint only against the explicitly snapshotted KMQGB Iter209 status/provenance authority. If current KMQGB moves later, this run remains reproducible against the recorded blob rather than silently following main.'
}
write_result('authority_freshness',out)
