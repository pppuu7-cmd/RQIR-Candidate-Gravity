import json, pathlib
e=json.loads(pathlib.Path('evidence/WAVE31_GENERALIZED_EH_EVIDENCE.json').read_text())
q=e['quadratic_sector_separation']
signals={'quadratic_form_factor_directions_not_recounted_as_generalized_EH':bool(q['R2_and_Ricci2_form_factors_already_counted_in_wave29'] and q['must_not_be_recounted_as_generalized_EH_extra_directions'])}
out={'test':'anti_double_counting','quadratic_sector_separation':q,'signals':signals}
pathlib.Path('wave31_anti_double_counting.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
