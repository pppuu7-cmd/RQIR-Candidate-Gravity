import glob
from pathlib import Path
from common import EXPECTED_BANK_BLOB, PREREG, git_blob_sha, write_result
import json
proto=json.loads(Path('protocol/PARENT_LAW_ACCEPTANCE_PROTOCOL_V1.json').read_text())
actual=git_blob_sha('holdouts/WAVE22_FROZEN_BANK.json')
other_scripts=[Path(p) for p in glob.glob('compute_wave26/*.py') if not p.endswith('information_firewall.py')]
forbidden_hits=[]
for p in other_scripts:
    t=p.read_text().lower()
    if 'kmqgb' in t or 'polygon' in t:
        forbidden_hits.append(str(p))
text=PREREG.read_text()
checks={
 'bank_blob_exact':actual==EXPECTED_BANK_BLOB,
 'protocol_frozen':proto.get('status')=='FROZEN_PROSPECTIVE_FILTER',
 'wave25_certificate_present':Path('certificates/WAVE25_KNOWN_PRINCIPLE_TOURNAMENT_CERTIFICATE.md').exists(),
 'wave26_prereg_present':PREREG.exists(),
 'anti_import_clause_present':'No KMQGB/polygon candidate equations or architecture may be imported.' in text,
 'compute_scripts_contain_no_forbidden_route_import_terms':len(forbidden_hits)==0
}
write_result('information_firewall',{'checks':checks,'forbidden_hits':forbidden_hits,'actual_bank_blob':actual,'future_candidate_information_firewall_pass':all(checks.values())})
