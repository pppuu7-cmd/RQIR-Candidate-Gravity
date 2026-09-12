import json, pathlib
root=pathlib.Path('compute_wave30')
forbidden=['cross_route/','Known-Models-Quantum-Gravity-Benchmark','Mechanism-Synthesis-QG-Reconstruction','Inter-School Quantum Gravity Reconstruction']
hits=[]; scanned=[]
if root.exists():
    for p in root.glob('*.py'):
        if p.name=='information_firewall.py': continue
        scanned.append(str(p)); txt=p.read_text(errors='ignore')
        for tok in forbidden:
            if tok in txt: hits.append({'file':str(p),'token':tok})
out={'test':'information_firewall','scanned_files':sorted(scanned),'forbidden_dependency_hits':hits,'signals':{'information_firewall_pass':len(hits)==0}}
pathlib.Path('wave30_information_firewall.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert not hits
