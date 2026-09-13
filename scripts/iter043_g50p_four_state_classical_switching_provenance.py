#!/usr/bin/env python3
"""Iter043/G50-P: response-blind four-state hidden-classical switching provenance/memory qualification."""
import argparse, json
from pathlib import Path
import numpy as np
from scipy.linalg import expm

I2=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.array([[1,0],[0,-1]],complex)
PAULIS=(X,Y,Z)
D=4; DV=16; NH=4
TIMES=(0.12,0.35,0.75,1.25)
DTS=(0.05,0.17)
SEMIGROUP_T=0.35; SEMIGROUP_S=0.35
TP_TOL=1e-10; CHOI_FLOOR=-1e-8; FACT_TOL=1e-11; NEG_TOL=1e-9
Q_TOL=1e-12; STAT_TOL=1e-10; MEMORY_DEFECT=1e-4


def h2(v): return sum(float(v[k])*PAULIS[k] for k in range(3))

def comm_liouvillian(H):
    return -1j*(np.kron(np.eye(D),H)-np.kron(H.T,np.eye(D)))

def qmatrix(shard):
    s=float(shard)
    R=np.zeros((NH,NH),float)
    # deterministic strictly-positive directed rates; response-blind shard perturbations
    base=np.array([
        [0, .061, .034, .028],
        [.073, 0, .052, .031],
        [.041, .047, 0, .066],
        [.036, .029, .058, 0],
    ],float)
    for i in range(NH):
        for j in range(NH):
            if i!=j:
                R[i,j]=base[i,j]+(0.0015+0.0003*((i+2*j)%3))*s
    Q=R.copy()
    for j in range(NH): Q[j,j]=-float(np.sum(R[:,j]))
    return Q

def fields(shard):
    s=float(shard)
    a=[
        np.array([ .61+.031*s, .07, .02]),
        np.array([ .05, .78+.027*s,-.10]),
        np.array([ .17,-.06, .91+.021*s]),
        np.array([-.42+.018*s, .26, .33]),
    ]
    b=[
        np.array([-.30, .49+.023*s, .08]),
        np.array([ .55+.019*s,-.15, .13]),
        np.array([-.10, .22,-.70-.024*s]),
        np.array([ .29,-.38+.016*s, .44]),
    ]
    return a,b

def stationary(Q):
    A=np.vstack([Q,np.ones(NH)])
    rhs=np.r_[np.zeros(NH),1.0]
    pi,*_=np.linalg.lstsq(A,rhs,rcond=None)
    return np.real_if_close(pi).astype(float)

def block_generator(Q,Hs):
    B=np.zeros((NH*DV,NH*DV),complex); eye=np.eye(DV,dtype=complex)
    for j in range(NH):
        for k in range(NH): B[j*DV:(j+1)*DV,k*DV:(k+1)*DV]+=Q[j,k]*eye
        B[j*DV:(j+1)*DV,j*DV:(j+1)*DV]+=comm_liouvillian(Hs[j])
    return B

def visible_superop(B,pi,t):
    inject=np.vstack([float(pi[j])*np.eye(DV,dtype=complex) for j in range(NH)])
    collect=np.hstack([np.eye(DV,dtype=complex) for _ in range(NH)])
    return collect@expm(B*float(t))@inject

def apply_map(E,rho):
    return (E@np.asarray(rho,complex).reshape(-1,order='F')).reshape((D,D),order='F')

def choi(E):
    J=np.zeros((D*D,D*D),complex)
    for i in range(D):
        for j in range(D):
            eij=np.zeros((D,D),complex); eij[i,j]=1.0
            J+=np.kron(eij,apply_map(E,eij))
    return (J+J.conj().T)/2

def pure(v):
    v=np.asarray(v,complex); v=v/np.linalg.norm(v); return np.outer(v,v.conj())

def product_states():
    z=np.array([1,0],complex); o=np.array([0,1],complex)
    p=np.array([1,1],complex)/np.sqrt(2); pi=np.array([1,1j],complex)/np.sqrt(2)
    ss=(z,o,p,pi); return [np.kron(pure(a),pure(b)) for a in ss for b in ss]

def partial_transpose_B(rho):
    x=np.asarray(rho,complex).reshape(2,2,2,2)
    return x.transpose(0,3,2,1).reshape(4,4)

def negativity(rho):
    pt=partial_transpose_B(rho); ev=np.linalg.eigvalsh((pt+pt.conj().T)/2)
    return float(np.sum(np.maximum(-ev,0.0)))

def factorization_residuals(a,b):
    vals=[]
    for j in range(NH):
        HA=h2(a[j]); HB=h2(b[j]); H=np.kron(HA,I2)+np.kron(I2,HB)
        for dt in DTS:
            u=expm(-1j*H*dt); up=np.kron(expm(-1j*HA*dt),expm(-1j*HB*dt))
            vals.append(float(np.linalg.norm(u-up,'fro')))
    return vals

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--shard',type=int,choices=range(6),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    Q=qmatrix(a.shard); va,vb=fields(a.shard)
    HA=[h2(x) for x in va]; HB=[h2(x) for x in vb]
    Hs=[np.kron(HA[j],I2)+np.kron(I2,HB[j]) for j in range(NH)]
    pi=stationary(Q); B=block_generator(Q,Hs)
    offdiag=[Q[i,j] for i in range(NH) for j in range(NH) if i!=j]
    q_col=float(np.max(np.abs(np.sum(Q,axis=0)))); stat_res=float(np.linalg.norm(Q@pi)); pi_norm=float(abs(np.sum(pi)-1.0)); fact=factorization_residuals(va,vb)
    tvec=np.eye(D,dtype=complex).reshape(-1,order='F').conj(); max_tp=0.; min_choi=1e9; max_trace_err=0.; max_neg=0.; probes=product_states()
    for t in TIMES:
        E=visible_superop(B,pi,t); max_tp=max(max_tp,float(np.linalg.norm(tvec@E-tvec))); min_choi=min(min_choi,float(np.min(np.linalg.eigvalsh(choi(E))).real))
        for rho in probes:
            out=apply_map(E,rho); max_trace_err=max(max_trace_err,float(abs(np.trace(out)-1.0)))
            if abs(t-0.75)<1e-12: max_neg=max(max_neg,negativity(out))
    Et=visible_superop(B,pi,SEMIGROUP_T); Es=visible_superop(B,pi,SEMIGROUP_S); Ets=visible_superop(B,pi,SEMIGROUP_T+SEMIGROUP_S)
    semigroup_defect=float(np.linalg.norm(Ets-Et@Es,'fro'))
    vals=[*offdiag,q_col,stat_res,pi_norm,*pi,*fact,max_tp,min_choi,max_trace_err,max_neg,semigroup_defect]
    finite=bool(np.all(np.isfinite(vals)))
    provenance=bool(finite and min(offdiag)>=-Q_TOL and q_col<=Q_TOL and min(pi)>=-Q_TOL and pi_norm<=Q_TOL and stat_res<=STAT_TOL and max(fact)<=FACT_TOL and max_tp<=TP_TOL and min_choi>=CHOI_FLOOR and max_trace_err<=TP_TOL and max_neg<=NEG_TOL)
    memory=bool(provenance and semigroup_defect>MEMORY_DEFECT)
    out={'iteration':'Iter043','gate':'G50-P','shard':a.shard,'hidden_chain':{'Q':Q.tolist(),'stationary_pi':pi.tolist(),'min_offdiag_rate':float(min(offdiag)),'max_column_sum_residual':q_col,'stationary_residual':stat_res,'stationary_normalization_error':pi_norm},'provenance':{'max_conditional_product_unitary_factorization_error':max(fact),'max_tp_residual':max_tp,'min_choi_eigenvalue':min_choi,'max_product_output_negativity':max_neg,'max_product_output_trace_error':max_trace_err},'memory':{'t':SEMIGROUP_T,'s':SEMIGROUP_S,'reduced_semigroup_defect_fro':semigroup_defect,'witness_threshold':MEMORY_DEFECT,'nonsemigroup_witness':memory},'structural_valid':finite,'classical_provenance_support':provenance,'memory_witness_support':memory,'classification':'FOUR_STATE_CLASSICAL_SWITCHING_PROVENANCE_MEMORY_LANE_PASS' if memory else 'FOUR_STATE_CLASSICAL_SWITCHING_QUALIFICATION_LANE_NOT_ESTABLISHED','frozen':{'hidden_states':4,'times':list(TIMES),'factorization_dts':list(DTS),'n_product_inputs':len(probes),'RCG002_target_used':False,'hidden_initialization':'stationary','tp_tolerance':TP_TOL,'choi_floor':CHOI_FLOOR,'factorization_tolerance':FACT_TOL,'negativity_tolerance':NEG_TOL,'memory_defect_threshold':MEMORY_DEFECT},'scope_lock':'Explicit finite four-state classical CTMC switching among local-sum Hamiltonians; provenance/memory qualification only, no target separation.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not finite: raise SystemExit(2)
if __name__=='__main__': main()
