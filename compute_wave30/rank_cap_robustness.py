import json, pathlib
import numpy as np
rng=np.random.default_rng(3005)
rows=[]
for k in [4,5]:
    for _ in range(500):
        P=rng.normal(size=(6,k))
        # force full column rank, then perturb by 2%
        if np.linalg.matrix_rank(P)<k: continue
        P2=P+0.02*np.linalg.norm(P)/np.sqrt(P.size)*rng.normal(size=P.shape)
        r0=int(np.linalg.matrix_rank(P)); r1=int(np.linalg.matrix_rank(P2))
        rows.append({'k':k,'rank_before':r0,'rank_after':r1,'cap_respected':r1<=k})
signals={'generic_transversality_can_saturate_rank_cap_but_not_exceed_it':all(x['cap_respected'] and x['rank_after']==x['k'] for x in rows)}
out={'test':'rank_cap_robustness','perturbation_fraction':0.02,'cases':len(rows),'signals':signals}
pathlib.Path('wave30_rank_cap_robustness.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
