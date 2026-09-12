import json, pathlib
b=json.loads(pathlib.Path('holdouts/WAVE22_FROZEN_BANK.json').read_text())
order=b['parameter_order']
vis={}
for sec in ['2pt','3pt','4pt']:
    idx=set()
    for p in b['probes']:
        if p['sector']==sec:
            idx.update(i for i,x in enumerate(p['row']) if abs(x)>0)
    vis[sec]=[order[i] for i in sorted(idx)]
expected={'2pt':['s2','s0'],'3pt':['c3','d3','s2','s0'],'4pt':['c3','d3','e4','f4','s2','s0']}
out={'test':'wave22_sector_visibility','visibility':vis,'expected':expected,'signals':{'wave22_sector_visibility_matches_frozen_bank':vis==expected}}
pathlib.Path('wave29_wave22_sector_visibility.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True)); assert all(out['signals'].values())
