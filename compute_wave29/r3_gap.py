import json, pathlib
e=json.loads(pathlib.Path('evidence/WAVE29_F2_EFFECTIVE_ACTION_BASIS.json').read_text())
r3=e['central_effective_action']['p6_R3_sector']
signal=bool(r3['can_exist_in_general'] and not r3['included_in_F2_reconstruction'])
out={'test':'r3_gap','p6_R3':r3,'signals':{'p6_R3_sector_not_available_in_F2_reconstruction':signal}}
pathlib.Path('wave29_r3_gap.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True)); assert signal
