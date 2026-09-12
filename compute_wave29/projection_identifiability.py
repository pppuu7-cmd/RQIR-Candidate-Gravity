import json, pathlib
import numpy as np
b=json.loads(pathlib.Path('holdouts/WAVE22_FROZEN_BANK.json').read_text())
H=np.array([p['row'] for p in b['probes']],dtype=float)
# Two inequivalent rank-2 embeddings of the same two-dimensional latent form-factor space into six frozen proxy coordinates.
P1=np.array([[1.,0.],[0.,1.],[0.,0.],[0.,0.],[0.3,0.],[0.,0.2]])
P2=np.array([[0.5,0.2],[0.1,0.7],[0.4,0.],[0.,0.3],[0.2,0.1],[0.1,-0.2]])
O1=H@P1; O2=H@P2
r1=int(np.linalg.matrix_rank(P1)); r2=int(np.linalg.matrix_rank(P2))
ro1=int(np.linalg.matrix_rank(O1)); ro2=int(np.linalg.matrix_rank(O2))
d=float(np.linalg.norm(P1-P2))
signals={
 'F2_to_wave22_six_coordinate_projection_nonunique_without_extra_map':r1==r2==2 and d>1e-6,
 'central_f2_information_does_not_close_frozen_six_direction_parent_law':max(ro1,ro2)<6
}
out={'test':'projection_identifiability','embedding_rank':[r1,r2],'probe_image_rank':[ro1,ro2],'embedding_distance':d,'signals':signals}
pathlib.Path('wave29_projection_identifiability.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
