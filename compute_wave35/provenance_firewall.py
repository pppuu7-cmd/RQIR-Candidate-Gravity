import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=(ROOT/'docs/WAVE35_SAME_REALIZATION_ORIENTATION_PREREGISTRATION.md').read_text()
signals={
 'same_realization_recompute_required_for_output_projection':'reproduced on the same displaced trajectories' in P,
 'author_overlap_not_treated_as_same_realization':'same authors/program lineage' in P,
 'metadata_audit_cannot_promote_J8':'metadata audit alone cannot promote J8' in P,
}
out={'test':'provenance_firewall','signals':signals,'verdict':'SAME_REALIZATION_REQUIRED'}
Path('wave35_provenance_firewall.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
