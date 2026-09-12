import json, pathlib
import numpy as np
rng=np.random.default_rng(2903)
rows=[4,10,30,100]
cases=[]
for latent in [2,4]:
    for n in rows:
        A=rng.normal(size=(n,latent))
        rank=int(np.linalg.matrix_rank(A))
        cases.append({'latent_rank':latent,'observable_rows':n,'image_rank':rank,'bounded':rank<=latent})
# deterministic duplication/mixing of rows cannot increase column rank
B=rng.normal(size=(8,2)); mix=rng.normal(size=(80,8)); C=mix@B
rB=int(np.linalg.matrix_rank(B)); rC=int(np.linalg.matrix_rank(C))
signals={
 'multiple_npoint_rows_do_not_raise_rank_above_latent_rank':all(c['bounded'] for c in cases) and rC<=rB,
 'three_and_four_point_inputs_do_not_imply_four_independent_residual_directions':rB==2 and rC==2
}
out={'test':'anti_overcounting_rank','cases':cases,'base_rank':rB,'mixed_80row_rank':rC,'signals':signals}
pathlib.Path('wave29_anti_overcounting_rank.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
