import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
E=json.loads((ROOT/'evidence/WAVE34_APPENDIX_F_SURROGATE_EVIDENCE.json').read_text())
P=(ROOT/'docs/WAVE34_APPENDIX_F_SURROGATE_PREREGISTRATION.md').read_text()
signals={
 'surrogate_classification_is_permanent':E['classification']=='SURROGATE_NOT_J8' and 'SURROGATE_NOT_J8' in P,
 'good_match_cannot_close_physical_J8':'Physical J8 remains blocked' in P,
 'poor_match_is_retained_not_coefficient_fitted':'No coefficient may be altered' in P,
}
out={'test':'surrogate_firewall','signals':signals,'physical_J8_closed':False}
Path('wave34_surrogate_firewall.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
