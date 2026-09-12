import json, pathlib
import numpy as np
rng=np.random.default_rng(3002)
cases=[]
for k in [2,4,5]:
    codims=[]
    ranks=[]
    for _ in range(1000):
        P=rng.normal(size=(6,k))
        r=int(np.linalg.matrix_rank(P))
        ranks.append(r); codims.append(6-r)
    cases.append({'k':k,'min_rank':min(ranks),'max_rank':max(ranks),'min_codimension':min(codims),'max_codimension':max(codims),'analytic_lower_bound':6-k})
signals={
 'constants_only_residual_codimension_ge_4':cases[0]['min_codimension']>=4,
 'first_slope_baseline_quotiented_residual_codimension_ge_2':cases[1]['min_codimension']>=2,
 'one_extra_EH_coefficient_residual_codimension_ge_1':cases[2]['min_codimension']>=1
}
out={'test':'codimension_bounds','trials_per_k':1000,'cases':cases,'signals':signals}
pathlib.Path('wave30_codimension_bounds.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
