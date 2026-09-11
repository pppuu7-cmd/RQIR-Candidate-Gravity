import json
from pathlib import Path
import numpy as np

X_DESIGN = 0.25
X_HOLD = 0.90
TARGET = 0.90

def write_result(name, obj):
    Path('wave18_results').mkdir(exist_ok=True)
    Path(f'wave18_results/{name}.json').write_text(json.dumps(obj, indent=2, sort_keys=True))
    print(json.dumps(obj, indent=2, sort_keys=True))

def svd_nullspace(A, tol=1e-12):
    A=np.asarray(A,dtype=float)
    u,s,vt=np.linalg.svd(A,full_matrices=True)
    rank=int(np.sum(s>tol))
    return rank, vt[rank:].T if rank < vt.shape[0] else np.zeros((A.shape[1],0)), s
