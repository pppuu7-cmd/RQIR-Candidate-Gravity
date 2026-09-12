import pathlib, json
from common import write
root=pathlib.Path('compute_wave33')
forbidden=['polygon','kmqgb','msqgr','isqgr','mechanism-synthesis-qg','inter-school']
hits=[]
for p in root.glob('*.py'):
    if p.name in {'information_firewall.py'}: continue
    t=p.read_text().lower()
    for token in forbidden:
        if token in t: hits.append({'file':str(p),'token':token})
signals={'information_firewall_pass':len(hits)==0}
out={'test':'information_firewall','scanned_files':[str(p) for p in root.glob('*.py') if p.name!='information_firewall.py'],'hits':hits,'signals':signals}; write('wave33_information_firewall.json',out); assert all(signals.values())
