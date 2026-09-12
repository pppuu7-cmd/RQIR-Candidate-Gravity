import pathlib
from common import write
HERE=pathlib.Path(__file__).resolve().parent
forbidden=['polygon','kmqgb','msqgr','isqgr','mechanism-synthesis-qg','inter-school']
hits=[]
scanned=[]
for p in HERE.glob('*.py'):
    if p.name=='information_firewall.py': continue
    scanned.append(str(p.relative_to(HERE.parent)))
    t=p.read_text().lower()
    for token in forbidden:
        if token in t: hits.append({'file':str(p.relative_to(HERE.parent)),'token':token})
signals={'information_firewall_pass':len(hits)==0}
out={'test':'information_firewall','scanned_files':sorted(scanned),'hits':hits,'signals':signals}; write('wave33_information_firewall.json',out); assert all(signals.values())
