import importlib.util, json, pathlib, sys
import numpy as np

HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parent
CLASSIFICATION='SYNTHETIC_INFORMATION_LEVERAGE_NOT_J8'
SEED=350035
SCALES=[0.05,0.10,0.20,0.40]
TRIALS=400

spec=importlib.util.spec_from_file_location('wave34_common',ROOT/'compute_wave34/common.py')
w34=importlib.util.module_from_spec(spec); spec.loader.exec_module(w34)
ROOT3,OK,_,RES=w34.solve_conditional()
A=w34.jac_fd(lambda y:w34.beta3(y),ROOT3)
BASE_SCALE=float(np.linalg.norm(A,'fro')/3.0)
D0=np.diag([-2.0,2.0])

def unit_random(rng,shape):
    X=rng.normal(size=shape); n=np.linalg.norm(X,'fro')
    return X/n

def full_matrix(B=None,C=None,D=None):
    B=np.zeros((3,2)) if B is None else np.asarray(B,float)
    C=np.zeros((2,3)) if C is None else np.asarray(C,float)
    D=D0.copy() if D is None else np.asarray(D,float)
    return np.block([[A,B],[C,D]])

def orth(B):
    B=np.asarray(B,float); Q,_=np.linalg.qr(B)
    if np.linalg.matrix_rank(B,tol=1e-9)!=B.shape[1]: raise ValueError('rank deficient')
    return Q[:,:B.shape[1]]

def relevant_basis(M):
    vals,vecs=np.linalg.eig(np.asarray(M,float).astype(complex))
    neg=[i for i,z in enumerate(vals) if z.real<0]
    if len(neg)!=3: return None,vals
    cols=[]; used=set()
    for i in neg:
        if i in used: continue
        z=vals[i]; v=vecs[:,i]
        if abs(z.imag)<1e-7:
            cols.append(v.real); used.add(i)
        elif z.imag>0:
            cand=[j for j in neg if j!=i]
            if not cand: return None,vals
            j=min(cand,key=lambda q:abs(vals[q]-np.conj(z)))
            if abs(vals[j]-np.conj(z))>1e-5: return None,vals
            cols.extend([v.real,v.imag]); used.update([i,j])
    if len(cols)!=3: return None,vals
    try: return orth(np.column_stack(cols)),vals
    except Exception: return None,vals

def max_angle(B0,B):
    s=np.linalg.svd(B0.T@B,compute_uv=False); s=np.clip(s,-1,1)
    return float(np.max(np.arccos(s)))

BASE_M=full_matrix(); BASE_B,BASE_VALS=relevant_basis(BASE_M)
assert BASE_B is not None

def run_scenario(name):
    offset={'B_only':101,'C_only':202,'D_only':303,'BC':404,'BCD':505}[name]
    rng=np.random.default_rng(SEED+offset)
    rows=[]
    for s in SCALES:
        angles=[]; shifts=[]; topology_changes=0; invalid=0
        for _ in range(TRIALS):
            amp=s*BASE_SCALE
            B=np.zeros((3,2)); C=np.zeros((2,3)); D=D0.copy()
            if name in {'B_only','BC','BCD'}: B=amp*unit_random(rng,(3,2))
            if name in {'C_only','BC','BCD'}: C=amp*unit_random(rng,(2,3))
            if name in {'D_only','BCD'}: D=D0+amp*unit_random(rng,(2,2))
            M=full_matrix(B,C,D); Q,vals=relevant_basis(M)
            if Q is None:
                topology_changes+=1; continue
            angles.append(max_angle(BASE_B,Q))
            shifts.append(float(np.linalg.norm(np.sort(vals.real)-np.sort(BASE_VALS.real))))
        arr=np.array(angles,float); sh=np.array(shifts,float)
        rows.append({'scale':s,'accepted_angle_trials':len(arr),'topology_changes':topology_changes,'topology_change_fraction':topology_changes/TRIALS,'median_max_principal_angle_rad':float(np.median(arr)) if len(arr) else None,'p95_max_principal_angle_rad':float(np.quantile(arr,0.95)) if len(arr) else None,'max_principal_angle_rad':float(np.max(arr)) if len(arr) else None,'median_real_spectrum_shift':float(np.median(sh)) if len(sh) else None})
    return rows

def write(name,obj):
    obj=dict(obj); obj.setdefault('classification',CLASSIFICATION)
    def default(x):
        if isinstance(x,np.generic): return x.item()
        if isinstance(x,np.ndarray): return x.tolist()
        raise TypeError
    text=json.dumps(obj,indent=2,sort_keys=True,default=default); pathlib.Path(name).write_text(text); print(text)
