#!/usr/bin/env python3
"""Iter024A / G41-P: implementation/admissibility validation for a finite
rank-4/5/6 classical Gaussian random-Hamiltonian Kossakowski family.

No RCG-002 target is used.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I2,I4,X,Y,Z,choi,neg

RANK_TOL=1e-10; KOSS_FLOOR=-1e-10; TP_TOL=1e-10; CHOI_FLOOR=-1e-8; FACT_TOL=1e-12; NEG_TOL=1e-9
TIMES=(0.1,0.5,1.0)
LOCAL=[np.kron(X,I2),np.kron(Y,I2),np.kron(Z,I2),np.kron(I2,X),np.kron(I2,Y),np.kron(I2,Z)]


def dsuper(F):
    F2=F@F
    return np.kron(F.T,F)-0.5*(np.kron(I4,F2)+np.kron(F2.T,I4))


def construction(rank,shard):
    rng=np.random.default_rng(74000+100*rank+shard)
    M=rng.normal(size=(6,rank)); Q,_=np.linalg.qr(M)
    V=Q[:,:rank].T
    kappas=np.array([0.055+0.018*j+0.004*rank for j in range(rank)],float)
    Fs=[]
    for v in V:
        F=sum(float(v[i])*LOCAL[i] for i in range(6)); Fs.append(F)
    C=V.T@np.diag(kappas)@V
    L=sum(float(k)*dsuper(F) for k,F in zip(kappas,Fs))
    return V,kappas,Fs,C,L


def map_apply(E,rho):
    x=(E@rho.reshape(-1,order='F')).reshape(4,4,order='F'); return (x+x.conj().T)/2


def split_local(v):
    HA=float(v[0])*X+float(v[1])*Y+float(v[2])*Z
    HB=float(v[3])*X+float(v[4])*Y+float(v[5])*Z
    return HA,HB


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--rank',type=int,choices=(4,5,6),required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    V,kappas,Fs,C,L=construction(a.rank,a.shard)
    ce=np.linalg.eigvalsh((C+C.T)/2); numerical_rank=int(np.sum(ce>RANK_TOL)); min_c=float(ce.min())
    tr=I4.reshape(-1,order='F').conj(); tp=[]; cp=[]
    for t in TIMES:
        E=expm(L*float(t)); tp.append(float(np.linalg.norm(tr@E-tr))); cp.append(float(np.min(np.linalg.eigvalsh(choi(E)))))
    # Deterministic simultaneous Gaussian-mode realization: any real linear
    # combination of the F_k is still a local-sum Hamiltonian and must factor.
    xi=np.array([np.sin((j+1)*(a.shard+1)*0.73)+0.37*np.cos((j+2)*(a.rank+1)) for j in range(a.rank)],float)
    coeff=np.sqrt(kappas)*xi
    Htot=sum(float(c)*F for c,F in zip(coeff,Fs)); va=coeff@V
    HA,HB=split_local(va); dt=0.137
    fact=float(np.linalg.norm(expm(-1j*dt*Htot)-np.kron(expm(-1j*dt*HA),expm(-1j*dt*HB))))
    rng=np.random.default_rng(75000+100*a.rank+a.shard); E07=expm(L*0.7); maxneg=0.0
    for _ in range(16):
        x=rng.normal(size=2)+1j*rng.normal(size=2); y=rng.normal(size=2)+1j*rng.normal(size=2); x/=np.linalg.norm(x); y/=np.linalg.norm(y)
        psi=np.kron(x,y); rho=np.outer(psi,psi.conj()); maxneg=max(maxneg,float(neg(map_apply(E07,rho))))
    vals=[*ce,*tp,*cp,fact,maxneg]; structural=bool(np.all(np.isfinite(vals)))
    support=bool(structural and numerical_rank==a.rank and min_c>KOSS_FLOOR and max(tp)<TP_TOL and min(cp)>CHOI_FLOOR and fact<FACT_TOL and maxneg<NEG_TOL)
    out={'iteration':'Iter024A','gate':'G41-P','rank':a.rank,'shard':a.shard,
         'kossakowski':{'intended_rank':a.rank,'numerical_rank':numerical_rank,'min_eigenvalue':min_c,'positive_rates':kappas.tolist()},
         'admissibility':{'max_tp_residual':max(tp),'min_choi_eigenvalue':min(cp),'product_unitary_factorization_error':fact,'max_product_input_output_negativity':maxneg},
         'structural_valid':structural,'scientific_support':support,
         'frozen_thresholds':{'rank_eigenvalue':RANK_TOL,'kossakowski_floor':KOSS_FLOOR,'tp':TP_TOL,'choi_floor':CHOI_FLOOR,'factorization':FACT_TOL,'negativity':NEG_TOL,'times':list(TIMES),'product_inputs':16},
         'scope_lock':'Finite rank-4/5/6 positive Kossakowski random-Hamiltonian family on the six local Pauli generators; explicit classical shared Gaussian noise only.',
         'interpretation':'Implementation/provenance pre-gate only. No RCG-002 target and no comparator-separation inference.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
