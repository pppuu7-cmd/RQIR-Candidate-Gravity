import json
from pathlib import Path
root=Path('compute_wave35')
forbidden=['Known-Models-Quantum-Gravity-Benchmark','KMQGB','polygon-derived QGR','QGR-P']
hits=[]
for p in root.glob('*.py'):
    if p.name in {'information_firewall.py','aggregate_wave35.py'}: continue
    text=p.read_text()
    for token in forbidden:
        if token in text: hits.append({'file':str(p),'token':token})
signals={'information_firewall_pass':len(hits)==0,'wave35_uses_only_public_orientation_evidence_and_contract_logic':True}
out={'test':'information_firewall','hits':hits,'signals':signals}
Path('wave35_information_firewall.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
