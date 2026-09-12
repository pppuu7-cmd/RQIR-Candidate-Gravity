#!/usr/bin/env python3
"""Iter026B / G42-BC: response-blind local-basis covariance and bounded
Cholesky-chart coverage audit for the G42 classical PSD comparator family.
No RCG-002 target/result is used.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I2,X,Y,Z
from iter024a_g41p_high_rank_classical_kossakowski import LOCAL
from iter025a_g42j_full_psd_kossakowski_identifiability import generator_from_C

PAULI=(X,Y,Z)
RANK_TOL=1e-10; C_FLOOR=-1e-10; COV_TOL=1e-10; REC_TOL=1e-10; BOUND_TOL=1e-12
DIAG_HI=0.60; OFF_HI=0.30
PANELS=(
    ((1.0,1.0,0.0),0.37,(0.0,1.0,1.0),-0.51),
    ((1.0,-2.0,1.0),0.83,(2.0,1.0,-1.0),0.61),
    ((1.0,1.0,1.0),1.17,(1.0,-1.0,2.0),-0.94),
    ((2.0,-1.0,3.0),1.43,(-1.0,3.0,2.0),1.21),
)


def hidden_B(rank):
    rng=np.random.default_rng(126000+rank)
    B=np.zeros((6,6),float)
    for j in range(rank):
        B[j,j]=0.40+0.018*j+0.006*rank
        for i in range(j+1,6):
            B[i,j]=float(rng.uniform(-0.24,0.24))
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


def semichol(C,tol=2e-11):
    C=(np.asarray(C,float)+np.asarray(C,float).T)/2
    n=C.shape[0]; L=np.zeros_like(C)
    ok=True
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


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--rank',type=int,choices=range(1,7),required=True); ap.add_argument('--panel',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    B=hidden_B(a.rank); C=B@B.T
    axA,angA,axB,angB=PANELS[a.panel]; UA=su2(axA,angA); UB=su2(axB,angB); U=np.kron(UA,UB)
    RA=rotation_from_u(UA); RB=rotation_from_u(UB); O=np.zeros((6,6),float); O[:3,:3]=RA; O[3:,3:]=RB
    Cp=O@C@O.T; Cp=(Cp+Cp.T)/2
    e0=np.linalg.eigvalsh(C); ep=np.linalg.eigvalsh(Cp); r0=int(np.sum(e0>RANK_TOL)); rp=int(np.sum(ep>RANK_TOL))
    L0=generator_from_C(C); Lp=generator_from_C(Cp); S=np.kron(U.conj(),U); Lin=S@L0@S.conj().T
    cov=float(np.linalg.norm(Lp-Lin)/max(np.linalg.norm(Lp),1e-15))
    Br,chol_ok=semichol(Cp); rec=float(np.linalg.norm(Br@Br.T-Cp)/max(np.linalg.norm(Cp),1e-15)) if chol_ok else float('inf')
    diag=np.diag(Br); off=np.array([Br[i,j] for i in range(6) for j in range(i)],float)
    maxdiag=float(np.max(diag)) if len(diag) else 0.; maxoff=float(np.max(np.abs(off))) if len(off) else 0.
    inside=bool(chol_ok and np.isfinite(rec) and rec<REC_TOL and np.min(diag)>=-BOUND_TOL and maxdiag<=DIAG_HI+BOUND_TOL and maxoff<=OFF_HI+BOUND_TOL)
    vals=[*e0,*ep,cov,rec,maxdiag,maxoff,*RA.reshape(-1),*RB.reshape(-1)]
    structural=bool(np.all(np.isfinite(vals)) and r0==a.rank and rp==a.rank and e0.min()>=C_FLOOR and ep.min()>=C_FLOOR)
    covariance_support=bool(structural and cov<COV_TOL)
    out={'iteration':'Iter026B','gate':'G42-BC','rank':a.rank,'panel':a.panel,
         'kossakowski':{'original_rank':r0,'rotated_rank':rp,'original_min_eigenvalue':float(e0.min()),'rotated_min_eigenvalue':float(ep.min())},
         'basis_covariance':{'relative_generator_error':cov,'support':covariance_support},
         'chart_coverage':{'semidefinite_cholesky_ok':bool(chol_ok),'reconstruction_relative_error':rec,'max_diagonal_coordinate':maxdiag,'max_abs_offdiagonal_coordinate':maxoff,'inside_frozen_chart':inside},
         'structural_valid':structural,
         'frozen':{'diag_bounds':[0.0,DIAG_HI],'offdiag_bounds':[-OFF_HI,OFF_HI],'rank_threshold':RANK_TOL,'kossakowski_floor':C_FLOOR,'generator_covariance_tolerance':COV_TOL,'chart_reconstruction_tolerance':REC_TOL,'RCG002_target_used':False},
         'scope_lock':'Response-blind local SO(3)xSO(3) basis covariance and bounded-chart coverage panel only.',
         'interpretation':'A chart-coverage limit constrains basis-invariant interpretation of G42-A but does not alter its numerical bounded-chart result.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
