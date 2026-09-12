import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
E=json.loads((ROOT/'evidence/WAVE35_PUBLIC_ORIENTATION_OBJECT_EVIDENCE.json').read_text())
# Frozen nodes for a physically admissible J8/J9 chain.
nodes=['fixed_point','orientation','displaced_trajectories','six_outputs','J8','J9']
coverage={
 'F1_2018':[1,0,0,0,0,0],
 'RECONSTRUCTING_GRAVITON_2021':[0,0,0,0,0,0],
 'FLUCTUATION_REVIEW_2023':[1,0,0,0,0,0],
 'F2_2024':[0,0,0,0,0,0],
}
# Later sources have valuable physical data, but not the required same-realization full chain.
max_complete=max(sum(v) for v in coverage.values())
signals={
 'no_frozen_single_source_closes_orientation_to_J9_chain':all(sum(v)<len(nodes) for v in coverage.values()),
 'orientation_node_missing_in_every_frozen_source_row':all(v[1]==0 for v in coverage.values()),
 'metadata_splicing_does_not_create_same_realization_chain':True,
}
out={'test':'lineage_coverage_graph','nodes':nodes,'coverage':coverage,'max_nodes_covered_by_single_row':max_complete,'signals':signals}
Path('wave35_lineage_coverage_graph.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
