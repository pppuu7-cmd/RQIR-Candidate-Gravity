import json, pathlib
import numpy as np
b=json.loads(pathlib.Path('holdouts/WAVE22_FROZEN_BANK.json').read_text())
H=np.array([p['row'] for p in b['probes']],dtype=float)
rng=np.random.default_rng(3003)
rows=[]
for k in [2,4,5]:
    for trial in range(500):
        P=rng.normal(size=(6,k))
        rp=int(np.linalg.matrix_rank(P)); rhp=int(np.linalg.matrix_rank(H@P))
        rows.append({'k':k,'rank_P':rp,'rank_HP':rhp,'nonincrease':rhp<=rp})
signals={
 'probe_composition_cannot_raise_latent_rank':all(x['nonincrease'] for x in rows),
 'one_extra_EH_coefficient_cannot_close_six_dimensions':max(x['rank_HP'] for x in rows if x['k']==5)<=5
}
out={'test':'probe_composition','trials':len(rows),'max_observable_rank_by_k':{str(k):max(x['rank_HP'] for x in rows if x['k']==k) for k in [2,4,5]},'signals':signals}
pathlib.Path('wave30_probe_composition.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
