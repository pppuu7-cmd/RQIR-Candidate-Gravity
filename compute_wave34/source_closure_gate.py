import json
from pathlib import Path
E=json.loads(Path('evidence/WAVE34_APPENDIX_F_SURROGATE_EVIDENCE.json').read_text())
p=E['published_truncation4']
signals={
 'classification_is_SURROGATE_NOT_J8':E['classification']=='SURROGATE_NOT_J8',
 'coordinate_order_frozen':E['coordinates']==['mu','lambda3','lambda4','g3','g4'],
 'zero_anomalous_dimensions_frozen':p['eta_phi_zero'] is True,
 'higher_coupling_closure_frozen':p['closure']=={'lambda5':'lambda3','lambda6':'lambda3','g5':'g4','g6':'g4'},
 'all_printed_F1_to_F5_registered':E['printed_equations']==['F1','F2','F3','F4','F5'],
 'local_projection_caveat_recorded':E['source_caveats']['local_projection_at_p0_can_introduce_large_error'] is True,
}
out={'test':'source_closure_gate','signals':signals,'classification':E['classification']}
Path('wave34_source_closure_gate.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
