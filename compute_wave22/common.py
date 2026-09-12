import itertools
import json
from pathlib import Path
import numpy as np

PARAMS=['c3','d3','e4','f4','s2','s0']
SECTORS=['2pt','3pt','4pt']

def build_pool():
    pool=[]
    for q in [0.25,0.65]:
        pool.append({'name':f'P2_q{q}','sector':'2pt','row':[0,0,0,0,q**2,0.0]})
    for q in [0.35,0.75]:
        pool.append({'name':f'P0_q{q}','sector':'2pt','row':[0,0,0,0,0.0,q**2]})
    for x,h in [(0.3,1),(0.5,-1),(0.7,1),(0.9,-1)]:
        pool.append({'name':f'V3_x{x}_h{h}','sector':'3pt','row':[x**2,h*x**3,0,0,0.15*x,-0.10*h*x**2]})
    for s,t,h in [(0.25,0.15,1),(0.4,0.2,-1),(0.55,0.25,1),(0.7,0.3,-1)]:
        pool.append({'name':f'A4_s{s}_t{t}_h{h}','sector':'4pt','row':[0.25*(s+t),0.2*h*s*t,s**2+t**2,h*s*t,0.1*s,0.08*t]})
    return pool

def matrix(pool=None):
    p=pool or build_pool()
    return np.asarray([r['row'] for r in p],dtype=float)

def d_optimal_indices(k=10):
    p=build_pool(); M=matrix(p)
    best=None
    for comb in itertools.combinations(range(len(p)),k):
        X=M[list(comb)]
        sign,ld=np.linalg.slogdet(X.T@X + 1e-12*np.eye(len(PARAMS)))
        if sign<=0:
            continue
        if best is None or ld>best[0]:
            best=(float(ld),comb)
    return best[0],list(best[1])

def selected_bank(k=10):
    ld,idx=d_optimal_indices(k)
    p=build_pool()
    return ld,idx,[p[i] for i in idx],matrix([p[i] for i in idx])

def nuisance_matrix(selected):
    return np.column_stack([[1.0 if r['sector']==sec else 0.0 for r in selected] for sec in SECTORS])

def profile_nuisance(X,selected):
    N=nuisance_matrix(selected)
    P=np.eye(len(selected))-N@np.linalg.pinv(N)
    return P@X,N,P

def write_result(name,obj):
    Path('wave22_results').mkdir(exist_ok=True)
    def default(v):
        if hasattr(v,'item'): return v.item()
        if isinstance(v,np.ndarray): return v.tolist()
        raise TypeError(type(v).__name__)
    text=json.dumps(obj,indent=2,sort_keys=True,default=default)
    Path(f'wave22_results/{name}.json').write_text(text)
    print(text)
