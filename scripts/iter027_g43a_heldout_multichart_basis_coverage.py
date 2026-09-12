#!/usr/bin/env python3
"""Iter027 / G43-A: response-blind held-out multi-chart basis coverage audit.
No RCG-002 target/result is used.
"""
import argparse, json, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I2, X, Y, Z
from iter025a_g42j_full_psd_kossakowski_identifiability import generator_from_C

PAULI=(X,Y,Z)
RANK_TOL=1e-10; C_FLOOR=-1e-10; COV_TOL=1e-10; REC_TOL=1e-10; BOUND_TOL=1e-12
DIAG_HI=0.60; OFF_HI=0.30

# Frozen G42-BC atlas charts: identity + the four preregistered G42-BC rotations.
ATLAS_PANELS=(
    None,
    ((1.0,1.0,0.0),0.37,(0.0,1.0,1.0),-0.51),
    ((1.0,-2.0,1.0),0.83,(2.0,1.0,-1.0),0.61),
    ((1.0,1.0,1.0),1.17,(1.0,-1.0,2.0),-0.94),
    ((2.0,-1.0,3.0),1.43,(-1.0,3.0,2.0),1.21),
)

# Prospectively frozen held-out rotations, disjoint from G42-BC panel.
HELDOUT_PANELS=(
    ((1.0,2.0,-1.0),0.49,(-2.0,1.0,1.0),0.72),
    ((3.0,1.0,2.0),-0.67,(1.0,2.0,3.0),1.03),
    ((2.0,3.0,-2.0),1.31,(-1.0,2.0,2.0),-1.12),
    ((1.0,-3.0,2.0),0.96,(3.0,-2.0,1.0),1.37),
    ((2.0,1.0,4.0),-1.24,(-3.0,1.0,2.0),0.88),
    ((4.0,-1.0,1.0),1.52,(1.0,4.0,-2.0),-0.76),
)

def hidden_B(rank):
    rng=np.random.default_rng(127000+rank)
    B=np.zeros((6,6),float)
    for j in range(rank):
        B[j,j]=0.39+0.019*j+0.005*rank
        for i in range(j+1,6):
            B[i,j]=float(rng.uniform(-0.235,0.235))
    return B

def su2(axis,angle):
    n=np.asarray(axis,float); n/=np.linalg.norm(n)
    H=n[0]*X+n[1]*Y+n[2]*Z
    return np.cos(angle/2)*I2-1j*np.sin(angle/2)*H

def rotation_from_u(U):
    R=np.empty((3,3),float)
    for i,P in enumerate(PAULI):
        Q=U@P@U.conj().T
        for j,S in enumerate(PAULI):
            R[j,i]=float(np.real(np.trace(S@Q))/2.0)
    return R

def panel_objects(panel):
    if panel is None:
        UA=I2.copy(); UB=I2.copy(); RA=np.eye(3); RB=np.eye(3)
    else:
        axA,angA,axB,angB=panel
        UA=su2(axA,angA); UB=su2(axB,angB)
        RA=rotation_from_u(UA); RB=rotation_from_u(UB)
    U=np.kron(UA,UB)
    O=np.zeros((6,6),float); O[:3,:3]=RA; O[3:,3:]=RB
    return U,O

def semichol(C,tol=2e-11):
    C=(np.asarray(C,float)+np.asarray(C,float).T)/2
    n=C.shape[0]; L=np.zeros_like(C); ok=True
    for j in range(n):
        d=float(C[j,j]-np.dot(L[j,:j],L[j,:j]))
        if d < -tol:
            ok=False; break
        if d <= tol:
            L[j,j]=0.0
            for i in range(j+1,n):
                num=float(C[i,j]-np.dot(L[i,:j],L[j,:j]))
                if abs(num)>tol:
                    ok=False; break
                L[i,j]=0.0
            if not ok: break
        else:
            L[j,j]=np.sqrt(max(d,0.0))
            for i in range(j+1,n):
                num=float(C[i,j]-np.dot(L[i,:j],L[j,:j]))
                L[i,j]=num/L[j,j]
    return L,ok

def chart_metric(Cp,Ochart,index):
    Cc=Ochart.T@Cp@Ochart; Cc=(Cc+Cc.T)/2
    B,ok=semichol(Cc)
    rec=float(np.linalg.norm(B@B.T-Cc)/max(np.linalg.norm(Cc),1e-15)) if ok else float('inf')
    diag=np.diag(B); off=np.array([B[i,j] for i in range(6) for j in range(i)],float)
    maxdiag=float(np.max(diag)) if len(diag) else 0.0
    maxoff=float(np.max(np.abs(off))) if len(off) else 0.0
    inside=bool(ok and np.isfinite(rec) and rec<REC_TOL and np.min(diag)>=-BOUND_TOL and maxdiag<=DIAG_HI+BOUND_TOL and maxoff<=OFF_HI+BOUND_TOL)
    diag_ex=max(0.0,maxdiag-DIAG_HI)
    off_ex=max(0.0,maxoff-OFF_HI)
    score=float(max(diag_ex,off_ex,0.0 if rec<REC_TOL else rec))
    return {'chart':index,'semidefinite_cholesky_ok':bool(ok),'reconstruction_relative_error':rec,'max_diagonal_coordinate':maxdiag,'max_abs_offdiagonal_coordinate':maxoff,'inside_frozen_chart':inside,'coverage_violation_score':score}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--rank',type=int,choices=range(1,7),required=True); ap.add_argument('--panel',type=int,choices=range(6),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    B=hidden_B(a.rank); C=B@B.T
    Ut,Ot=panel_objects(HELDOUT_PANELS[a.panel])
    Cp=Ot@C@Ot.T; Cp=(Cp+Cp.T)/2
    e0=np.linalg.eigvalsh(C); ep=np.linalg.eigvalsh(Cp); r0=int(np.sum(e0>RANK_TOL)); rp=int(np.sum(ep>RANK_TOL))
    L0=generator_from_C(C); Lp=generator_from_C(Cp); S=np.kron(Ut.conj(),Ut); Lin=S@L0@S.conj().T
    cov=float(np.linalg.norm(Lp-Lin)/max(np.linalg.norm(Lp),1e-15))
    atlas=[]
    for idx,p in enumerate(ATLAS_PANELS):
        _,Oc=panel_objects(p); atlas.append(chart_metric(Cp,Oc,idx))
    covered=[m for m in atlas if m['inside_frozen_chart']]
    best=min(atlas,key=lambda m:m['coverage_violation_score'])
    finite_vals=[*e0,*ep,cov]+[x for m in atlas for x in (m['reconstruction_relative_error'],m['max_diagonal_coordinate'],m['max_abs_offdiagonal_coordinate'])]
    structural=bool(np.all(np.isfinite(finite_vals)) and r0==a.rank and rp==a.rank and e0.min()>=C_FLOOR and ep.min()>=C_FLOOR)
    covariance_support=bool(structural and cov<COV_TOL)
    atlas_covered=bool(covariance_support and len(covered)>0)
    out={'iteration':'Iter027','gate':'G43-A','rank':a.rank,'panel':a.panel,
         'kossakowski':{'original_rank':r0,'rotated_rank':rp,'original_min_eigenvalue':float(e0.min()),'rotated_min_eigenvalue':float(ep.min())},
         'basis_covariance':{'relative_generator_error':cov,'support':covariance_support},
         'atlas':{'n_charts':len(atlas),'covered':atlas_covered,'covering_charts':[m['chart'] for m in covered],'best_chart':best['chart'],'best_violation_score':best['coverage_violation_score'],'charts':atlas},
         'structural_valid':structural,
         'frozen':{'diag_bounds':[0.0,DIAG_HI],'offdiag_bounds':[-OFF_HI,OFF_HI],'rank_threshold':RANK_TOL,'kossakowski_floor':C_FLOOR,'generator_covariance_tolerance':COV_TOL,'chart_reconstruction_tolerance':REC_TOL,'atlas_size':5,'heldout_panels':6,'RCG002_target_used':False},
         'scope_lock':'Response-blind five-chart coverage on six new hidden PSD controls and six held-out local-basis rotations only.',
         'interpretation':'Coverage calibration only; cannot alter G42-A or establish basis-invariant full-PSD support.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural or not covariance_support: raise SystemExit(2)
if __name__=='__main__': main()
