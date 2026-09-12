#!/usr/bin/env python3
"""Iter022B / G40-C: positive-control optimizer calibration for a strict
BLP-backflow-capable hidden-classical RTN comparator family.

No RCG-002 target is used.  Four hidden in-family trajectories are recovered
under two independent start constructions (Sobol and LHS).  The fit uses a
fixed multi-time, multi-probe state trajectory and the scientific recovery
metric is maximum trace distance across all frozen probes/times.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
from scipy.stats import qmc

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I2,I4,X,Y,Z,td
from iter022a_g40p_rtn_information_backflow_validation import pair_states

METHODS=('sobol_lsq','lhs_lsq')
TIMES=np.array([0.35,0.80,1.60,3.00],float)
N_STARTS=16; N_REFINE=4; MAX_NFEV=600; RECOVERY_TOL=0.002; BACKFLOW_MIN=0.02
BLP_TIMES=np.linspace(0.0,12.0,241)

# u -> [r,nu,cA,cB,thetaA,phiA,thetaB,phiB], gamma=r*nu*cA.
LO=np.array([0.20,0.60,0.70,0.40,0.15*np.pi,-np.pi,0.15*np.pi,-np.pi])
HI=np.array([0.60,1.40,1.30,1.20,0.85*np.pi, np.pi,0.85*np.pi, np.pi])

CONTROLS=np.array([
 [0.31,1.08,0.92,0.61,0.44*np.pi, 0.35,0.62*np.pi,-0.70],
 [0.47,0.88,1.16,0.52,0.67*np.pi,-1.05,0.38*np.pi, 0.91],
 [0.24,1.27,0.78,1.03,0.29*np.pi, 1.34,0.73*np.pi,-1.42],
 [0.55,1.16,1.24,0.84,0.58*np.pi,-2.08,0.47*np.pi, 2.21],
],float)


def axis(th,ph): return np.sin(th)*np.cos(ph)*X+np.sin(th)*np.sin(ph)*Y+np.cos(th)*Z

def unpack(p):
    r,nu,cA,cB,ta,pa,tb,pb=np.asarray(p,float); gamma=r*nu*cA
    A=axis(ta,pa); B=axis(tb,pb); H=nu*(cA*np.kron(A,I2)+cB*np.kron(I2,B)); return gamma,H

def hsuper(H): return -1j*(np.kron(I4,H)-np.kron(H.T,I4))
def block(p):
    gamma,H=unpack(p); Q=np.eye(16,dtype=complex); Lp=hsuper(H); Lm=hsuper(-H)
    return np.block([[Lp-gamma*Q,gamma*Q],[gamma*Q,Lm-gamma*Q]])
def reduced_map(G,t):
    J=np.vstack([0.5*np.eye(16),0.5*np.eye(16)]); P=np.hstack([np.eye(16),np.eye(16)]); return P@expm(G*t)@J

def probes():
    z0=np.array([1,0],complex); z1=np.array([0,1],complex); xp=np.array([1,1],complex)/np.sqrt(2); yp=np.array([1,1j],complex)/np.sqrt(2)
    vec=[np.kron(xp,xp),np.kron(yp,xp),np.kron(xp,yp),np.kron(z0,xp),np.kron(xp,z0),np.kron(z0,z1)]
    return [np.outer(v,v.conj()) for v in vec]
PROBES=probes()

def apply(E,rho):
    x=(E@rho.reshape(-1,order='F')).reshape(4,4,order='F'); return (x+x.conj().T)/2

def trajectory(p):
    G=block(p); return [[apply(reduced_map(G,float(t)),rho) for rho in PROBES] for t in TIMES]

def residual_u(u,target_traj):
    p=LO+np.clip(np.asarray(u,float),0,1)*(HI-LO); tr=trajectory(p); out=[]
    for aa,bb in zip(tr,target_traj):
        for a,b in zip(aa,bb):
            d=a-b; out.extend(np.real(d).ravel()); out.extend(np.imag(d).ravel())
    return np.asarray(out,float)
def metric_u(u,target_traj):
    p=LO+np.clip(np.asarray(u,float),0,1)*(HI-LO); tr=trajectory(p); vals=[]
    for aa,bb in zip(tr,target_traj):
        vals.extend(td(a,b) for a,b in zip(aa,bb))
    return float(max(vals)),float(np.linalg.norm(residual_u(u,target_traj)))
def design(method,shard):
    seed=62000+100*shard+(0 if method=='sobol_lsq' else 37)
    if method=='sobol_lsq': return qmc.Sobol(d=8,scramble=True,seed=seed).random_base2(4)
    return qmc.LatinHypercube(d=8,seed=seed).random(N_STARTS)
def blp_u(u):
    p=LO+np.clip(np.asarray(u,float),0,1)*(HI-LO); G=block(p); a,b=pair_states(); ds=[]
    for t in BLP_TIMES:
        E=reduced_map(G,float(t)); ds.append(td(apply(E,a),apply(E,b)))
    ds=np.asarray(ds); return float(np.sum(np.clip(np.diff(ds),0,None)))
def optimize(method,shard,target_traj):
    scored=[]
    for u in design(method,shard):
        rr=residual_u(u,target_traj); scored.append((float(np.dot(rr,rr)),u))
    scored.sort(key=lambda z:z[0]); best=None
    for _,u0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual_u(z,target_traj),u0,bounds=(0,1),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn=metric_u(fit.x,target_traj); cand=(gap,rn,int(fit.nfev),bool(fit.success),fit.x.copy())
        if best is None or (gap,rn)<(best[0],best[1]): best=cand
    return best

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    hidden=CONTROLS[a.shard]; target_traj=trajectory(hidden); gap,rn,nfev,ok,u=optimize(a.method,a.shard,target_traj); backflow=blp_u(u)
    structural=bool(np.all(np.isfinite([gap,rn,backflow])))
    support=bool(structural and gap<RECOVERY_TOL and backflow>BACKFLOW_MIN)
    out={'iteration':'Iter022B','gate':'G40-C','method':a.method,'shard':a.shard,'best_max_trace_gap':gap,'residual_norm':rn,'nfev':nfev,'optimizer_success_flag':ok,'recovered_BLP_total_positive_increment':backflow,'structural_valid':structural,'scientific_support':support,
         'frozen':{'times':TIMES.tolist(),'n_probes':len(PROBES),'recovery_tolerance':RECOVERY_TOL,'BLP_backflow_min':BACKFLOW_MIN,'n_starts':N_STARTS,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'hidden_control_never_used_as_start':True},
         'scope_lock':'Finite symmetric hidden-classical RTN with arbitrary local Pauli axes; gamma=r*nu*cA, r in [0.2,0.6], each trajectory product-local-unitary.',
         'interpretation':'Positive-control optimizer calibration only. PASS may authorize a separate RCG-002 adversarial trajectory gate; no novelty inference here.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
