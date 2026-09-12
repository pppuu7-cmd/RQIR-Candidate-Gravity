import json, hashlib
from pathlib import Path
import numpy as np

BANK=Path('holdouts/WAVE22_FROZEN_BANK.json')
PROTOCOL=Path('protocol/PARENT_LAW_ACCEPTANCE_PROTOCOL_V1.json')
PREREG=Path('post_freeze/WAVE26_PRINCIPLE_SYNERGY_PREREGISTRATION.md')
EXPECTED_BANK_BLOB='c32bd52edd003589ef65e0240c757475f215f55f'
W=np.asarray([
 [1.0,0.0,0.0,0.0,-0.4,0.1],
 [0.0,1.0,0.0,0.0,0.2,-0.5],
 [0.0,0.0,1.0,-0.6,0.0,0.0]
],float)
BOUNDS=np.asarray([0.20,0.18,0.15,0.12,0.10,0.09],float)

def load_bank(): return json.loads(BANK.read_text())
def X(): return np.asarray([p['row'] for p in load_bank()['probes']],float)
def git_blob_sha(path):
    data=Path(path).read_bytes()
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
def null_basis(A,tol=1e-12):
    u,s,vh=np.linalg.svd(A,full_matrices=True)
    rank=int((s>tol).sum())
    return vh[rank:].T
def write_result(name,obj):
    Path('wave26_results').mkdir(exist_ok=True)
    def default(v):
        if isinstance(v,np.ndarray): return v.tolist()
        if hasattr(v,'item'): return v.item()
        raise TypeError(type(v).__name__)
    text=json.dumps(obj,indent=2,sort_keys=True,default=default)
    Path(f'wave26_results/{name}.json').write_text(text)
    print(text)
