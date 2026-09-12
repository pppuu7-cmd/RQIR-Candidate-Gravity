import json, pathlib
import numpy as np
b=json.loads(pathlib.Path('holdouts/WAVE22_FROZEN_BANK.json').read_text())
H=np.array([p['row'] for p in b['probes']],dtype=float)
r=int(np.linalg.matrix_rank(H))
s=np.linalg.svd(H,compute_uv=False)
out={'test':'wave22_rank','shape':list(H.shape),'rank':r,'singular_values':[float(x) for x in s],'condition_number':float(s[0]/s[-1]),'signals':{'wave22_probe_matrix_rank_is_6':r==6}}
pathlib.Path('wave30_wave22_rank.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert r==6
