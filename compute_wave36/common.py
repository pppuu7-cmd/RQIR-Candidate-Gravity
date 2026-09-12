import json, pathlib, numpy as np
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parent
COORDS=['mu','lambda3','lambda4','g3','g4']
CLASSIFICATION='VALIDATOR_TEST_NOT_PHYSICAL_J8'
REQUIRED_META=['target_realization','closure_id','projection_provenance','regulator_gauge_truncation','derivative_provenance','numerical_precision','checksum']

def canonical_matrix():
    A=np.zeros((5,5),float)
    A[0,0]=-3.0
    A[1:3,1:3]=np.array([[-1.9,-1.6],[1.6,-1.9]])
    A[3,3]=1.7; A[4,4]=3.4
    return A

def orth(B):
    B=np.asarray(B,float); Q,_=np.linalg.qr(B)
    if B.ndim!=2 or np.linalg.matrix_rank(B,tol=1e-10)!=B.shape[1]: raise ValueError('rank deficient basis')
    return Q[:,:B.shape[1]]

def relevant_basis_from_matrix(M):
    M=np.asarray(M,float)
    if M.shape!=(5,5) or not np.all(np.isfinite(M)): raise ValueError('matrix')
    vals,vecs=np.linalg.eig(M.astype(complex)); neg=[i for i,z in enumerate(vals) if z.real<0]
    if len(neg)!=3: raise ValueError('attractive count')
    cols=[]; used=set()
    for i in neg:
        if i in used: continue
        z=vals[i]; v=vecs[:,i]
        if abs(z.imag)<1e-8:
            cols.append(v.real); used.add(i)
        elif z.imag>0:
            js=[j for j in neg if j!=i]
            j=min(js,key=lambda q:abs(vals[q]-np.conj(z)))
            if abs(vals[j]-np.conj(z))>1e-6: raise ValueError('unpaired')
            cols.extend([v.real,v.imag]); used.update([i,j])
    if len(cols)!=3: raise ValueError('real dim')
    return orth(np.column_stack(cols)),vals

def projector(B):
    Q=orth(B); return Q@Q.T

def complete_candidate():
    M=canonical_matrix(); Q,vals=relevant_basis_from_matrix(M)
    return {
      'target_realization':'Denz-Pawlowski-Reichert-1612.07315-F1-same-closure-placeholder',
      'closure_id':'g_n>4_to_g4__lambda_n>4_to_lambda3',
      'fixed_point':[-0.45,0.12,0.028,0.83,0.57],
      'coordinates':COORDS,
      'stability_matrix':M.tolist(),
      'right_relevant_real_basis':Q.tolist(),
      'projection_provenance':'synthetic-validator-only; would require exact F1 nonlocal/bilocal projection metadata for physical use',
      'regulator_gauge_truncation':'synthetic-validator-only; would require exact F1 metadata',
      'derivative_provenance':'synthetic analytic test matrix',
      'numerical_precision':{'dtype':'float64','matrix_tolerance':1e-10,'projector_tolerance':1e-8},
      'checksum':'sha256:synthetic-wave36-validator-object'
    }

def validate(c,expected_closure='g_n>4_to_g4__lambda_n>4_to_lambda3'):
    reasons=[]
    if c.get('coordinates')!=COORDS: reasons.append('coordinate_order')
    if c.get('closure_id')!=expected_closure: reasons.append('closure_id')
    fp=np.asarray(c.get('fixed_point',[]),float)
    if fp.shape!=(5,) or not np.all(np.isfinite(fp)): reasons.append('fixed_point')
    for k in REQUIRED_META:
        if k not in c or c[k] in [None,'',{}]: reasons.append(k)
    hasM='stability_matrix' in c; hasB='right_relevant_real_basis' in c
    if not (hasM or hasB): reasons.append('orientation_object_missing')
    M=None; Bm=None
    if hasM:
        try:
            M=np.asarray(c['stability_matrix'],float)
            Bm,vals=relevant_basis_from_matrix(M)
        except Exception: reasons.append('invalid_matrix_or_attractive_structure')
    if hasB:
        try:
            Bd=orth(np.asarray(c['right_relevant_real_basis'],float))
            if Bd.shape!=(5,3): raise ValueError
        except Exception:
            Bd=None; reasons.append('invalid_right_basis')
    else: Bd=None
    if Bm is not None and Bd is not None:
        err=float(np.linalg.norm(projector(Bm)-projector(Bd)))
        tol=float(c.get('numerical_precision',{}).get('projector_tolerance',1e-8))
        if err>tol: reasons.append('matrix_basis_inconsistent')
    else: err=None
    return len(reasons)==0,reasons,err

def write(name,obj):
    obj=dict(obj); obj.setdefault('classification',CLASSIFICATION)
    def default(x):
        if isinstance(x,np.generic): return x.item()
        if isinstance(x,np.ndarray): return x.tolist()
        raise TypeError
    text=json.dumps(obj,indent=2,sort_keys=True,default=default); pathlib.Path(name).write_text(text); print(text)
