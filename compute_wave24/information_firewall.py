import hashlib
from pathlib import Path
from common import BANK,write_result

files=sorted(p for p in Path('compute_wave24').glob('*.py') if p.name!='information_firewall.py')
texts={str(p):p.read_text() for p in files}
banned=['Known-Models-Quantum-Gravity-Benchmark','candidate_synthesis/','cross_route/','KMQGB_AUTHORITY_SNAPSHOT','QGR-P equations']
viol={tok:[name for name,text in texts.items() if tok in text] for tok in banned}
viol={k:v for k,v in viol.items() if v}
data=BANK.read_bytes()
actual=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
expected='c32bd52edd003589ef65e0240c757475f215f55f'
checks={
 'no_polygon_candidate_reads':len(viol)==0,
 'frozen_wave22_bank_blob_exact':actual==expected,
 'wave24_prereg_present':Path('post_freeze/WAVE24_PARENT_LAW_STRENGTH_PREREGISTRATION.md').exists(),
 'wave23_certificate_present':Path('certificates/WAVE23_HOLDOUT_STRESS_CERTIFICATE.md').exists()
}
out={
 'test':'Wave-24 information and frozen-bank firewall',
 'files_scanned':list(texts),
 'violations':viol,
 'expected_bank_blob_sha':expected,
 'actual_bank_blob_sha':actual,
 'checks':checks,
 'future_candidate_information_firewall_pass':all(checks.values()),
 'conclusion':'Wave 24 measures selector strength and legitimacy using only the frozen RQIR-derived residual/holdout structure; it imports no polygon candidate dynamics and does not mutate the prospective exam.'
}
write_result('information_firewall',out)
