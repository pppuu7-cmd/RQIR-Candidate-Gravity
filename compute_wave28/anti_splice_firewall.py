import glob
from pathlib import Path
from common import load,blob_sha,EXPECTED_BANK_BLOB,write
D=load(); prereg=Path('post_freeze/WAVE28_JACOBIAN_DATA_CONTRACT_PREREGISTRATION.md').read_text()
forbidden=[]
for p in glob.glob('compute_wave28/*.py'):
    if p.endswith('anti_splice_firewall.py'): continue
    t=Path(p).read_text().lower()
    if 'known-models-quantum-gravity-benchmark' in t or 'polygon-qgr' in t:
        forbidden.append(p)
checks={
 'evidence_frozen':D.get('status')=='FROZEN_BEFORE_COMPUTE',
 'bank_blob_exact':blob_sha('holdouts/WAVE22_FROZEN_BANK.json')==EXPECTED_BANK_BLOB,
 'wave27_certificate_present':Path('certificates/WAVE27_ASYMPTOTIC_SAFETY_LINEAGE_CERTIFICATE.md').exists(),
 'anti_splice_clause_present':'may not fill missing F1+F2 data' in prereg,
 'no_forbidden_imports_in_compute':len(forbidden)==0,
 'evidence_anti_splice_pass':D['evidence']['D28_7_anti_splice']['status']=='PASS'
}
write('anti_splice_firewall',{'checks':checks,'forbidden_hits':forbidden,'anti_splice_firewall_pass':all(checks.values())})
