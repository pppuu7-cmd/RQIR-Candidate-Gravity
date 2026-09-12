#!/usr/bin/env python3
"""Iter035 / G47-P: response-blind provenance audit for a three-state hidden-classical switching channel."""
import argparse, json
from pathlib import Path
import numpy as np
from scipy.linalg import expm

I2=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.array([[1,0],[0,-1]],complex)
PAULIS=(X,Y,Z)
D=4
DV=16
TIMES=(0.15,0.45,0.9,1.4)
DTS=(0.07,0.19)
SEMIGROUP_T=0.45
SEMIGROUP_S=0.45
TP_TOL=1e-10
CHOI_FLOOR=-1e-8
FACT_TOL=1e-11
NEG_TOL=1e-9
Q_TOL=1e-12
STAT_TOL=1e-10
MEMORY_DEFECT=1e-4


def h2(v):
    return sum(float(v[k])*PAULIS[k] for k in range(3))


def comm_liouvillian(H):
    return -1j*(np.kron(np.eye(D),H)-np.kron(H.T,np.eye(D)))


def qmatrix(shard):
    s=float(shard)
    # rates[to,from]; strictly positive and response-blind deterministic.
    R=np.zeros((3,3),float)
    R[1,0]=0.070+0.008*s
    R[2,0]=0.035+0.004*s
    R[0,1]=0.055+0.006*s
    R[2,1]=0.045+0.003*s
    R[0,2]=0.030+0.005*s
    R[1,2]=0.060+0.004*s
    Q=R.copy()
    for j in range(3):
        Q[j,j]=-float(np.sum(R[:,j]))
    return Q


def fields(shard):
    s=float(shard)
    a=[
        np.array([0.62+0.045*s, 0.08, 0.03]),
        np.array([0.04, 0.79+0.035*s, -0.11]),
        np.array([0.18, -0.05, 0.93+0.025*s]),
    ]
    b=[
        np.array([-0.31, 0.51+0.028*s, 0.07]),
        np.array([0.57+0.022*s, -0.16, 0.12]),
        np.array([-0.09, 0.23, -0.72-0.031*s]),
    ]
    return a,b


def stationary(Q):
    A=np.vstack([Q,np.ones(3)])
    rhs=np.array([0.0,0.0,0.0,1.0])
    pi,*_=np.linalg.lstsq(A,rhs,rcond=None)
    return np.real_if_close(pi).astype(float)


def block_generator(Q,Hs):
    B=np.zeros((3*DV,3*DV),complex)
    eye=np.eye(DV,dtype=complex)
    for j in range(3):
        for k in range(3):
            B[j*DV:(j+1)*DV,k*DV:(k+1)*DV]+=Q[j,k]*eye
        B[j*DV:(j+1)*DV,j*DV:(j+1)*DV]+=comm_liouvillian(Hs[j])
    return B


def visible_superop(B,pi,t):
    inject=np.vstack([float(pi[j])*np.eye(DV,dtype=complex) for j in range(3)])
    collect=np.hstack([np.eye(DV,dtype=complex) for _ in range(3)])
    return collect@expm(B*float(t))@inject


def apply_map(E,rho):
    return (E@np.asarray(rho,complex).reshape(-1,order='F')).reshape((D,D),order='F')


def choi(E):
    J=np.zeros((D*D,D*D),complex)
    for i in range(D):
        for j in range(D):
            eij=np.zeros((D,D),complex); eij[i,j]=1.0
            out=apply_map(E,eij)
            J+=np.kron(eij,out)
    return (J+J.conj().T)/2


def pure(v):
    v=np.asarray(v,complex); v=v/np.linalg.norm(v)
    return np.outer(v,v.conj())


def product_states():
    zero=np.array([1,0],complex); one=np.array([0,1],complex)
    plus=np.array([1,1],complex)/np.sqrt(2)
    plusi=np.array([1,1j],complex)/np.sqrt(2)
    ss=(zero,one,plus,plusi)
    return [np.kron(pure(a),pure(b)) for a in ss for b in ss]


def partial_transpose_B(rho):
    x=np.asarray(rho,complex).reshape(2,2,2,2)
    return x.transpose(0,3,2,1).reshape(4,4)


def negativity(rho):
    ev=np.linalg.eigvalsh((partial_transpose_B(rho)+partial_transpose_B(rho).conj().T)/2)
    return float(np.sum(np.maximum(-ev,0.0)))


def factorization_residuals(a,b):
    vals=[]
    for j in range(3):
        HA=h2(a[j]); HB=h2(b[j])
        H=np.kron(HA,I2)+np.kron(I2,HB)
        for dt in DTS:
            u=expm(-1j*H*dt)
            up=np.kron(expm(-1j*HA*dt),expm(-1j*HB*dt))
            vals.append(float(np.linalg.norm(u-up,'fro')))
    return vals


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--shard',type=int,choices=range(6),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()

    Q=qmatrix(a.shard)
    va,vb=fields(a.shard)
    HA=[h2(x) for x in va]; HB=[h2(x) for x in vb]
    Hs=[np.kron(HA[j],I2)+np.kron(I2,HB[j]) for j in range(3)]
    pi=stationary(Q)
    B=block_generator(Q,Hs)

    offdiag=[Q[i,j] for i in range(3) for j in range(3) if i!=j]
    q_col=float(np.max(np.abs(np.sum(Q,axis=0))))
    stat_res=float(np.linalg.norm(Q@pi))
    pi_norm=float(abs(np.sum(pi)-1.0))
    fact=factorization_residuals(va,vb)

    tvec=np.eye(D,dtype=complex).reshape(-1,order='F').conj()
    max_tp=0.0; min_choi=1e9; max_trace_err=0.0
    Es={}
    probes=product_states()
    max_neg=0.0
    vals=[]
    for t in TIMES:
        E=visible_superop(B,pi,t); Es[float(t)]=E
        max_tp=max(max_tp,float(np.linalg.norm(tvec@E-tvec)))
        min_choi=min(min_choi,float(np.min(np.linalg.eigvalsh(choi(E))).real))
        for rho in probes:
            out=apply_map(E,rho)
            max_trace_err=max(max_trace_err,float(abs(np.trace(out)-1.0)))
            if abs(t-0.9)<1e-12:
                max_neg=max(max_neg,negativity(out))

    Et=visible_superop(B,pi,SEMIGROUP_T)
    Esm=visible_superop(B,pi,SEMIGROUP_S)
    Ets=visible_superop(B,pi,SEMIGROUP_T+SEMIGROUP_S)
    semigroup_defect=float(np.linalg.norm(Ets-Et@Esm,'fro'))

    vals=[*offdiag,q_col,stat_res,pi_norm,*pi,*fact,max_tp,min_choi,max_trace_err,max_neg,semigroup_defect]
    finite=bool(np.all(np.isfinite(vals)))
    provenance=bool(
        finite and min(offdiag)>=-Q_TOL and q_col<=Q_TOL and min(pi)>=-Q_TOL and pi_norm<=Q_TOL and stat_res<=STAT_TOL
        and max(fact)<=FACT_TOL and max_tp<=TP_TOL and min_choi>=CHOI_FLOOR and max_trace_err<=TP_TOL and max_neg<=NEG_TOL
    )
    memory=bool(provenance and semigroup_defect>MEMORY_DEFECT)

    out={
        'iteration':'Iter035','gate':'G47-P','shard':a.shard,
        'hidden_chain':{'Q':Q.tolist(),'stationary_pi':pi.tolist(),'min_offdiag_rate':float(min(offdiag)),'max_column_sum_residual':q_col,'stationary_residual':stat_res,'stationary_normalization_error':pi_norm},
        'provenance':{'max_conditional_product_unitary_factorization_error':max(fact),'max_tp_residual':max_tp,'min_choi_eigenvalue':min_choi,'max_product_output_negativity':max_neg,'max_product_output_trace_error':max_trace_err},
        'memory':{'t':SEMIGROUP_T,'s':SEMIGROUP_S,'reduced_semigroup_defect_fro':semigroup_defect,'witness_threshold':MEMORY_DEFECT,'nonsemigroup_witness':memory},
        'structural_valid':finite,'classical_provenance_support':provenance,'memory_witness_support':memory,
        'classification':'THREE_STATE_CLASSICAL_SWITCHING_PROVENANCE_LANE_PASS' if provenance else 'THREE_STATE_CLASSICAL_SWITCHING_PROVENANCE_LANE_NOT_ESTABLISHED',
        'frozen':{'times':list(TIMES),'factorization_dts':list(DTS),'n_product_inputs':len(probes),'RCG002_target_used':False,'hidden_initialization':'stationary','tp_tolerance':TP_TOL,'choi_floor':CHOI_FLOOR,'factorization_tolerance':FACT_TOL,'negativity_tolerance':NEG_TOL,'memory_defect_threshold':MEMORY_DEFECT},
        'scope_lock':'Explicit three-state classical CTMC switching among local-sum Hamiltonians; provenance/memory implementation only, no target separation.',
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if not finite:
        raise SystemExit(2)

if __name__=='__main__':
    main()
