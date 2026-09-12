import json, pathlib
e=json.loads(pathlib.Path('evidence/WAVE31_GENERALIZED_EH_EVIDENCE.json').read_text())
excluded=e['excluded_shortcuts']
signals={'p6_R3_not_used_to_rescue_generalized_EH_rank':any('p6/R3' in x for x in excluded)}
out={'test':'p6_exclusion','excluded_shortcuts':excluded,'signals':signals}
pathlib.Path('wave31_p6_exclusion.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
