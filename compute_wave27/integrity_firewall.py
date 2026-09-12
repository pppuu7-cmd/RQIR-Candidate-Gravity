from pathlib import Path
from common import load,blob_sha,EXPECTED_BANK_BLOB,write
D=load(); checks={
 'evidence_frozen':D.get('status')=='FROZEN_EVIDENCE_SET_BEFORE_COMPUTE',
 'bank_blob_exact':blob_sha('holdouts/WAVE22_FROZEN_BANK.json')==EXPECTED_BANK_BLOB,
 'protocol_present':Path('protocol/PARENT_LAW_ACCEPTANCE_PROTOCOL_V1.json').exists(),
 'wave26_certificate_present':Path('certificates/WAVE26_PRINCIPLE_SYNERGY_TRANSVERSALITY_CERTIFICATE.md').exists(),
 'prereg_present':Path('post_freeze/WAVE27_ASYMPTOTIC_SAFETY_LINEAGE_PREREGISTRATION.md').exists(),
 'six_residuals_exact':D.get('rqir_residual_order')==['c3','d3','e4','f4','s2','s0']
}
write('integrity_firewall',{'checks':checks,'integrity_firewall_pass':all(checks.values())})
