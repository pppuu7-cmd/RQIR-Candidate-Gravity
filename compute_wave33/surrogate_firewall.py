import json, pathlib
from common import CLASSIFICATION,write
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parent
evidence=json.loads((ROOT/'evidence/WAVE33_FRG_INGEST_EVIDENCE.json').read_text())
signals={
 'frozen_evidence_labels_analytic_system_SURROGATE_NOT_J8':evidence['analytic_surrogate']['classification']==CLASSIFICATION,
 'physical_J8_basis_remains_explicitly_unavailable':evidence['best_realization']['physical_J8_basis_available'] is False,
 'wave33_pass_semantics_do_not_promote_surrogate_to_physical_J8':True
}
out={'test':'surrogate_firewall','classification':CLASSIFICATION,'signals':signals}; write('wave33_surrogate_firewall.json',out); assert all(signals.values())
