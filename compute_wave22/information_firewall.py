from pathlib import Path
from common import write_result

root=Path('compute_wave22')
files=sorted(p for p in root.glob('*.py') if p.name!='information_firewall.py')
texts={str(p):p.read_text() for p in files}
banned=['KMQGB_AUTHORITY_SNAPSHOT','cross_route/','candidate_synthesis/','Known-Models-Quantum-Gravity-Benchmark']
violations={token:[name for name,text in texts.items() if token in text] for token in banned}
violations={k:v for k,v in violations.items() if v}
prereg=Path('post_freeze/WAVE22_PROSPECTIVE_HOLDOUT_PREREGISTRATION.md').read_text()
endpoint=Path('model/RQIR_ONLY_ACTION_LEVEL_ENDPOINT_V1.md').read_text()
checks={
 'no_banned_polygon_reads_in_compute':len(violations)==0,
 'prereg_forbids_future_candidate_equations':'Forbidden: KMQGB candidate equations' in prereg,
 'frozen_endpoint_present':'FROZEN RQIR-ONLY ENDPOINT' in endpoint,
 'endpoint_authority_wave20':'34659887695' in endpoint,
 'wave22_declared_candidate_blind':'candidate-blind' in prereg.lower()
}
out={
 'test':'Wave-22 future-candidate information firewall',
 'files_scanned':[str(p) for p in files],
 'banned_tokens':banned,
 'violations':violations,
 'checks':checks,
 'candidate_information_firewall_pass':all(checks.values()),
 'conclusion':'Wave 22 is constructed from the frozen RQIR endpoint and generic proxy physics only. It does not read KMQGB/polygon candidate equations, synthesis files or authority snapshots.'
}
write_result('information_firewall',out)
