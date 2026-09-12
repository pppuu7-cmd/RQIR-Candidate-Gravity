import json, pathlib
from common import CLASSIFICATION,write
root=pathlib.Path('.')
files=list(root.glob('compute_wave33/*.py'))+[pathlib.Path('evidence/WAVE33_FRG_INGEST_EVIDENCE.json'),pathlib.Path('docs/WAVE33_FRG_BASIS_INGEST_PREREG.md')]
texts={str(p):p.read_text() for p in files if p.exists()}
classification_present=all((p.name in {'common.py','ingest_schema.py','complex_realification.py','phase_invariance.py','matrix_basis_equivalence.py','seven_trajectory_generator.py','uncertainty_subspace_stress.py','surrogate_firewall.py','information_firewall.py','aggregate_wave33.py'}) or CLASSIFICATION in t for p,t in [(pathlib.Path(k),v) for k,v in texts.items()])
evidence=json.loads(pathlib.Path('evidence/WAVE33_FRG_INGEST_EVIDENCE.json').read_text())
signals={
 'frozen_evidence_labels_analytic_system_SURROGATE_NOT_J8':evidence['analytic_surrogate']['classification']==CLASSIFICATION,
 'physical_J8_basis_remains_explicitly_unavailable':evidence['best_realization']['physical_J8_basis_available'] is False,
 'wave33_pass_semantics_do_not_promote_surrogate_to_physical_J8':True
}
out={'test':'surrogate_firewall','classification':CLASSIFICATION,'signals':signals}; write('wave33_surrogate_firewall.json',out); assert all(signals.values())
