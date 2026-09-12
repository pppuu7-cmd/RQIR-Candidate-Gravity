from pathlib import Path
from common import EXPECTED_BLOB_SHA, git_blob_sha, write_result

files=sorted(p for p in Path('compute_wave23').glob('*.py') if p.name!='information_firewall.py')
texts={str(p):p.read_text() for p in files}
banned=['Known-Models-Quantum-Gravity-Benchmark','candidate_synthesis/','cross_route/','KMQGB_AUTHORITY_SNAPSHOT','QGR-P equations']
viol={tok:[name for name,text in texts.items() if tok in text] for tok in banned}
viol={k:v for k,v in viol.items() if v}
checks={
 'no_polygon_candidate_reads':len(viol)==0,
 'frozen_bank_blob_unchanged':git_blob_sha()==EXPECTED_BLOB_SHA,
 'wave23_prereg_exists':Path('post_freeze/WAVE23_HOLDOUT_STRESS_PREREGISTRATION.md').exists(),
 'wave22_certificate_exists':Path('certificates/WAVE22_PROSPECTIVE_HOLDOUT_BANK_CERTIFICATE.md').exists()
}
out={
 'test':'Wave-23 information and frozen-bank firewall',
 'files_scanned':list(texts),
 'violations':viol,
 'checks':checks,
 'firewall_pass':all(checks.values()),
 'conclusion':'Wave 23 stress-tests the already frozen candidate-blind bank and does not import polygon candidate dynamics.'
}
write_result('information_firewall',out)
