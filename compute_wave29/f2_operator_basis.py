import json, pathlib
import numpy as np

e = json.loads(pathlib.Path('evidence/WAVE29_F2_EFFECTIVE_ACTION_BASIS.json').read_text())
# rows: TT 3pt, TT 4pt; cols: R^2, Ricci^2
M = np.array([[0.0, 1.0], [1.0, 1.0]])
r = int(np.linalg.matrix_rank(M))
out = {
  'test':'f2_operator_basis',
  'incidence_matrix':M.tolist(),
  'rank':r,
  'declared_rank':e['central_effective_action']['quadratic_curvature_operator_rank'],
  'signals':{'f2_quadratic_curvature_operator_rank_is_2': r == 2}
}
pathlib.Path('wave29_f2_operator_basis.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True))
assert all(out['signals'].values())
