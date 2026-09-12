import hashlib
import json
import re
from pathlib import Path
import numpy as np

BANK_PATH=Path('holdouts/WAVE22_FROZEN_BANK.json')
EXPECTED_BLOB_SHA='c32bd52edd003589ef65e0240c757475f215f55f'
PARAMS=['c3','d3','e4','f4','s2','s0']
SECTORS=['2pt','3pt','4pt']

def load_bank():
    return json.loads(BANK_PATH.read_text())

def X_and_probes():
    b=load_bank(); p=b['probes']
    return np.asarray([r['row'] for r in p],dtype=float),p

def git_blob_sha(path=BANK_PATH):
    data=path.read_bytes()
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()

def sector_nuisance(probes):
    return np.column_stack([[1.0 if r['sector']==s else 0.0 for r in probes] for s in SECTORS])

def projector_out(A):
    return np.eye(A.shape[0])-A@np.linalg.pinv(A)

def omitted_g7(probes):
    out=[]
    for r in probes:
        n=r['name']
        if n.startswith('P2_q'):
            q=float(n.split('q',1)[1]); out.append(q**4)
        elif n.startswith('P0_q'):
            q=float(n.split('q',1)[1]); out.append(-0.7*q**4)
        elif n.startswith('V3_x'):
            m=re.match(r'V3_x([0-9.]+)_h(-?1)$',n)
            x=float(m.group(1)); h=int(m.group(2)); out.append(h*x**4)
        elif n.startswith('A4_s'):
            m=re.match(r'A4_s([0-9.]+)_t([0-9.]+)_h(-?1)$',n)
            s=float(m.group(1)); t=float(m.group(2)); h=int(m.group(3)); out.append(h*(s+t)**3)
        else:
            raise ValueError(n)
    return np.asarray(out,float)

def write_result(name,obj):
    Path('wave23_results').mkdir(exist_ok=True)
    def default(v):
        if isinstance(v,np.ndarray): return v.tolist()
        if hasattr(v,'item'): return v.item()
        raise TypeError(type(v).__name__)
    text=json.dumps(obj,indent=2,sort_keys=True,default=default)
    Path(f'wave23_results/{name}.json').write_text(text)
    print(text)
