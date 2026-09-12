#!/usr/bin/env python3
"""Iter022A / G40-P: strict information-backflow pre-gate for a classical
random-telegraph-noise (RTN) comparator ingredient.

A hidden classical two-state process xi(t)=+/-1 switches symmetrically at rate
gamma.  Conditioned system blocks obey a classical Markov embedding
  d rho_+ = -i[+H,rho_+] - gamma rho_+ + gamma rho_-
  d rho_- = -i[-H,rho_-] + gamma rho_+ - gamma rho_-
with H = nu*(cA Z⊗I + cB I⊗Z).  Every noise trajectory is a product of local
unitaries; tracing out the hidden classical state can nevertheless show BLP
trace-distance revival in the strong-coupling regime.

This is implementation/witness validation only.  It does not compare RCG-002.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I2,I4,Z,choi,neg,td

TP_TOL=1e-10; CHOI_TOL=-1e-8; NEG_TOL=1e-9
BACKFLOW_MIN=2e-2; NO_BACKFLOW_MAX=1e-6; FACT_TOL=1e-12
TIMES=np.linspace(0.0,12.0,241)


def hsuper(H): return -1j*(np.kron(I4,H)-np.kron(H.T,I4))

def block_generator(gamma,nu,cA=1.0,cB=0.55):
    H=nu*(cA*np.kron(Z,I2)+cB*np.kron(I2,Z))
    Lp=hsuper(H); Lm=hsuper(-H); Q=np.eye(16,dtype=complex)
    return np.block([[Lp-gamma*Q,gamma*Q],[gamma*Q,Lm-gamma*Q]]),H

def reduced_map(G,t):
    J=np.vstack([0.5*np.eye(16),0.5*np.eye(16)])
    P=np.hstack([np.eye(16),np.eye(16)])
    return P@expm(G*t)@J

def evolve_map(E,rho):
    r=(E@rho.reshape(-1,order='F')).reshape(4,4,order='F'); return (r+r.conj().T)/2

def pair_states():
    z0=np.array([1,0],complex); p=np.array([1,1],complex)/np.sqrt(2); m=np.array([1,-1],complex)/np.sqrt(2)
    pp=np.kron(p,z0); mm=np.kron(m,z0)
    return np.outer(pp,pp.conj()),np.outer(mm,mm.conj())
def blp_measure(G):
    a,b=pair_states(); ds=[]
    for t in TIMES:
        E=reduced_map(G,float(t)); ds.append(td(evolve_map(E,a),evolve_map(E,b)))
    ds=np.asarray(ds); inc=np.diff(ds); return float(np.sum(np.clip(inc,0,None))),float(np.max(np.clip(inc,0,None))),ds

def diagnostics(G,H,seed):
    tr=I4.reshape(-1,order='F').conj(); tp=[]; cm=[]
    for t in (0.0,0.25,0.5,1.0,2.0,4.0):
        E=reduced_map(G,t); tp.append(float(np.linalg.norm(tr@E-tr))); cm.append(float(np.min(np.linalg.eigvalsh(choi(E)))))
    # Local factorization of each conditioned Hamiltonian trajectory step.
    dt=0.137; cA=1.0; cB=0.55
    # Infer nu from H coefficient using trace projection.
    ZA=np.kron(Z,I2); ZB=np.kron(I2,Z); nu=float(np.real(np.trace(ZA@H))/np.real(np.trace(ZA@ZA))/cA)
    UA=expm(-1j*dt*nu*cA*Z); UB=expm(-1j*dt*nu*cB*Z); fact=float(np.linalg.norm(expm(-1j*dt*H)-np.kron(UA,UB)))
    rng=np.random.default_rng(seed); maxneg=0.0
    for _ in range(10):
        va=rng.normal(size=2)+1j*rng.normal(size=2); vb=rng.normal(size=2)+1j*rng.normal(size=2); va/=np.linalg.norm(va); vb/=np.linalg.norm(vb)
        psi=np.kron(va,vb); rho=np.outer(psi,psi.conj()); out=evolve_map(reduced_map(G,1.0),rho); maxneg=max(maxneg,neg(out))
    return max(tp),min(cm),fact,maxneg

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    strong=[(0.30,1.00),(0.50,1.00),(0.20,0.80),(0.70,1.20)][a.shard]
    weak=[(1.00,0.08),(1.20,0.09),(1.40,0.10),(1.60,0.11)][a.shard]
    Gs,Hs=block_generator(*strong); Gw,Hw=block_generator(*weak)
    bs,ms,Ds=blp_measure(Gs); bw,mw,Dw=blp_measure(Gw)
    tps,cps,facts,negs=diagnostics(Gs,Hs,50000+a.shard); tpw,cpw,factw,negw=diagnostics(Gw,Hw,51000+a.shard)
    support=bool(bs>BACKFLOW_MIN and bw<NO_BACKFLOW_MAX and max(tps,tpw)<TP_TOL and min(cps,cpw)>CHOI_TOL and max(facts,factw)<FACT_TOL and max(negs,negw)<NEG_TOL)
    structural=bool(np.all(np.isfinite([bs,ms,bw,mw,tps,cps,facts,negs,tpw,cpw,factw,negw])))
    out={'iteration':'Iter022A','gate':'G40-P','shard':a.shard,
         'strong_control':{'gamma':strong[0],'nu':strong[1],'blp_total_positive_increment':bs,'max_single_step_revival':ms,'D_min':float(Ds.min()),'D_final':float(Ds[-1])},
         'weak_control':{'gamma':weak[0],'nu':weak[1],'blp_total_positive_increment':bw,'max_single_step_revival':mw,'D_min':float(Dw.min()),'D_final':float(Dw[-1])},
         'admissibility':{'max_tp_error':max(tps,tpw),'min_choi_eig':min(cps,cpw),'max_product_unitary_factorization_error':max(facts,factw),'max_product_input_output_negativity':max(negs,negw)},
         'structural_valid':structural,'scientific_support':bool(structural and support),
         'frozen_thresholds':{'strong_blp_backflow_min':BACKFLOW_MIN,'weak_blp_backflow_max':NO_BACKFLOW_MAX,'tp':TP_TOL,'choi_floor':CHOI_TOL,'factorization':FACT_TOL,'negativity':NEG_TOL,'time_grid_points':len(TIMES)},
         'interpretation':'Implementation and strict BLP information-backflow witness validation for a hidden classical RTN channel only. No RCG-002 adversarial inference.',
         'scope_lock':'Shared symmetric classical random-telegraph Hamiltonian noise with local additive Z couplings; each hidden trajectory is a product unitary.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
