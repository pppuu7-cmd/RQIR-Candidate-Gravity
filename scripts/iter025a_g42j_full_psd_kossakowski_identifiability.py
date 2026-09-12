#!/usr/bin/env python3
"""Iter025A / G42-J: local identifiability/Jacobian pre-gate for the full
21-parameter real-PSD classical Kossakowski family. No RCG-002 target.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I4,choi
from iter022b_g40c_rtn_optimizer_calibration import PROBES
from iter024a_g41p_high_rank_classical_kossakowski import LOCAL,map_apply

TIMES=np.array([0.15,0.45,0.9,1.4],float)
H1=1e-6; H2=5e-7; REL_RANK=1e-7; COND_MAX=1e7; JDIFF_MAX=5e-5
TP_TOL=1e-10; CHOI_FLOOR=-1e-8
LOWER=[(i,j) for i in range(6) for j in range(i+1)]


def hidden_z(shard):
    rng=np.random.default_rng(92000+shard)
    z=[]
    for i,j in LOWER:
        if i==j:
            # Cholesky diagonals around 0.22--0.38, safely positive.
            val=0.22+0.025*i+0.015*shard
            z.append(float(np.log(val)))
        else:
            z.append(float(rng.uniform(-0.055,0.055)))
    return np.asarray(z,float)


def unpack(z):
    z=np.asarray(z,float); Lc=np.zeros((6,6),float)
    for q,(i,j) in enumerate(LOWER):
        Lc[i,j]=np.exp(z[q]) if i==j else z[q]
    return Lc


def koss(z):
    Lc=unpack(z); return Lc@Lc.T


def generator_from_C(C):
    L=np.zeros((16,16),complex)
    for i,Gi in enumerate(LOCAL):
        for j,Gj in enumerate(LOCAL):
            cij=float(C[i,j])
            if abs(cij)<1e-18: continue
            P=Gj@Gi
            L += cij*(np.kron(Gj.T,Gi)-0.5*(np.kron(I4,P)+np.kron(P.T,I4)))
    return L


def output_vector(z):
    G=generator_from_C(koss(z)); vals=[]
    for t in TIMES:
        E=expm(G*float(t))
        for rho in PROBES:
            out=map_apply(E,rho)
            vals.extend(out.real.reshape(-1)); vals.extend(out.imag.reshape(-1))
    return np.asarray(vals,float)


def jacobian(z,h):
    n=len(z); y0=output_vector(z); J=np.empty((len(y0),n),float)
    for q in range(n):
        zp=z.copy(); zm=z.copy(); zp[q]+=h; zm[q]-=h
        J[:,q]=(output_vector(zp)-output_vector(zm))/(2*h)
    return J


def rank_diag(J):
    s=np.linalg.svd(J,compute_uv=False); cut=REL_RANK*s[0]; r=int(np.sum(s>cut))
    cond=float(s[0]/s[r-1]) if r else float('inf')
    return s,r,cond


def admissibility(z):
    G=generator_from_C(koss(z)); tr=I4.reshape(-1,order='F').conj(); tp=[]; cp=[]
    for t in TIMES:
        E=expm(G*float(t)); tp.append(float(np.linalg.norm(tr@E-tr))); cp.append(float(np.min(np.linalg.eigvalsh(choi(E)))))
    return max(tp),min(cp)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    z=hidden_z(a.shard); C=koss(z); ce=np.linalg.eigvalsh(C)
    J1=jacobian(z,H1); J2=jacobian(z,H2); s1,r1,c1=rank_diag(J1); s2,r2,c2=rank_diag(J2)
    rel=float(np.linalg.norm(J1-J2)/max(np.linalg.norm(J2),1e-15)); tp,cp=admissibility(z)
    vals=[*ce,*s1,*s2,rel,c1,c2,tp,cp]
    structural=bool(np.all(np.isfinite(vals)))
    support=bool(structural and r1==21 and r2==21 and max(c1,c2)<COND_MAX and rel<JDIFF_MAX and tp<TP_TOL and cp>CHOI_FLOOR)
    classification='FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE' if support else ('LOCAL_RANK_DEFICIENT_OR_ILL_CONDITIONED_PRE_GATE' if structural else 'STRUCTURAL_NUMERICAL_FAIL')
    out={'iteration':'Iter025A','gate':'G42-J','shard':a.shard,
         'kossakowski':{'min_eigenvalue':float(ce.min()),'max_eigenvalue':float(ce.max()),'numerical_rank_1e-10':int(np.sum(ce>1e-10))},
         'jacobian':{'shape':list(J1.shape),'rank_h':r1,'rank_h2':r2,'condition_h':c1,'condition_h2':c2,'relative_two_step_difference':rel,'min_singular_h':float(s1[-1]),'min_singular_h2':float(s2[-1]),'max_singular_h':float(s1[0])},
         'admissibility':{'max_tp_residual':tp,'min_choi_eigenvalue':cp},
         'structural_valid':structural,'scientific_support':support,'classification':classification,
         'frozen':{'times':TIMES.tolist(),'n_probes':len(PROBES),'n_parameters':21,'h':H1,'h2':H2,'relative_rank_cutoff':REL_RANK,'condition_max':COND_MAX,'jacobian_two_step_max':JDIFF_MAX,'tp_tolerance':TP_TOL,'choi_floor':CHOI_FLOOR,'RCG002_target_used':False},
         'scope_lock':'Local identifiability of the full real-PSD 6x6 classical random-Hamiltonian Kossakowski family in 21 Cholesky coordinates; no comparator claim.',
         'interpretation':'Identifiability pre-gate only. PASS may authorize separately preregistered positive-control optimizer calibration.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
