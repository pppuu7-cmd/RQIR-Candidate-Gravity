import json
from pathlib import Path
import numpy as np

BANK=Path('holdouts/WAVE22_FROZEN_BANK.json')
PARAMS=['c3','d3','e4','f4','s2','s0']
L1=np.asarray([[1,1,1,1,1,1]],dtype=float)
L3=np.asarray([
    [1.0,0.0,0.0,0.0,-0.4,0.1],
    [0.0,1.0,0.0,0.0,0.2,-0.5],
    [0.0,0.0,1.0,-0.6,0.0,0.0]
],dtype=float)
B=np.asarray([
    [1.0,-0.3],
    [0.4,0.7],
    [0.2,-0.2],
    [-0.1,0.6],
    [0.5,0.1],
    [0.2,0.8]
],dtype=float)
TARGET_A=np.asarray([0.10,-0.08,0.06,-0.04,0.03,-0.02],dtype=float)
TARGET_B=np.asarray([-0.07,0.11,-0.05,0.09,-0.025,0.04],dtype=float)
Q6=np.asarray([
    [0,1,0,0,0,0],
    [0,0,1,0,0,0],
    [0,0,0,1,0,0],
    [0,0,0,0,1,0],
    [0,0,0,0,0,1],
    [1,0,0,0,0,0]
],dtype=float)
BOUNDS=np.asarray([0.20,0.20,0.15,0.15,0.10,0.10],dtype=float)
DESIGN_NAMES=['P2_q0.65','P0_q0.75']

def load_bank(): return json.loads(BANK.read_text())
def X_and_probes():
    b=load_bank(); p=b['probes']
    return np.asarray([r['row'] for r in p],float),p

def write_result(name,obj):
    Path('wave24_results').mkdir(exist_ok=True)
    def default(v):
        if isinstance(v,np.ndarray): return v.tolist()
        if hasattr(v,'item'): return v.item()
        raise TypeError(type(v).__name__)
    text=json.dumps(obj,indent=2,sort_keys=True,default=default)
    Path(f'wave24_results/{name}.json').write_text(text)
    print(text)
