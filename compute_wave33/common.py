import json, math, pathlib
import numpy as np

COORDS=['mu','lambda3','lambda4','g3','g4']
XSTAR=np.array([-0.23,-0.060,-0.11,0.64,0.55],float)
CLASSIFICATION='SURROGATE_NOT_J8'

def surrogate_matrix():
    # Canonical real matrix carrying the published Truncation-4 first-approximation spectrum.
    # Orientation is deliberately synthetic: this object tests machinery only.
    A=np.zeros((5,5),float)
    A[0,0]=-3.0
    A[1:3,1:3]=np.array([[-1.9,-1.6],[1.6,-1.9]])
    A[3,3]=1.7; A[4,4]=3.4
    return A

def orth(B):
    B=np.asarray(B,float)
    Q,R=np.linalg.qr(B)
    rank=int(np.linalg.matrix_rank(B,tol=1e-10))
    if rank != B.shape[1]:
        raise ValueError('basis is rank deficient')
    return Q[:,:B.shape[1]]

def relevant_basis_from_matrix(A):
    A=np.asarray(A,float)
    if A.shape!=(5,5) or not np.all(np.isfinite(A)):
        raise ValueError('matrix must be finite 5x5')
    vals,vecs=np.linalg.eig(A.astype(complex))
    neg=[i for i,z in enumerate(vals) if z.real < 0]
    if len(neg)!=3:
        raise ValueError(f'expected 3 attractive eigenvalues counting conjugates, got {len(neg)}')
    cols=[]; used=set()
    for i in neg:
        if i in used: continue
        z=vals[i]; v=vecs[:,i]
        if abs(z.imag)<1e-8:
            cols.append(np.real(v)); used.add(i)
        elif z.imag>0:
            j=min((j for j in neg if j!=i), key=lambda j: abs(vals[j]-np.conj(z)))
            if abs(vals[j]-np.conj(z))>1e-6:
                raise ValueError('unpaired complex attractive eigenvalue')
            cols.extend([np.real(v),np.imag(v)]); used.update([i,j])
        else:
            continue
    B=np.column_stack(cols)
    if B.shape[1]!=3:
        raise ValueError(f'real relevant dimension {B.shape[1]} != 3')
    return orth(B), vals

def projector(B):
    Q=orth(B); return Q@Q.T

def principal_angles(B1,B2):
    Q1=orth(B1); Q2=orth(B2)
    s=np.linalg.svd(Q1.T@Q2,compute_uv=False)
    s=np.clip(s,-1,1)
    return np.arccos(s)

def write(name,obj):
    obj=dict(obj); obj.setdefault('classification',CLASSIFICATION)
    pathlib.Path(name).write_text(json.dumps(obj,indent=2,sort_keys=True))
    print(json.dumps(obj,indent=2,sort_keys=True))
