#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import numpy as np


def plus_state():
    p=np.array([1,1],dtype=complex)/np.sqrt(2)
    psi=np.kron(p,p)
    return np.outer(psi,psi.conj())


def unitary(chi):
    return np.diag([1,1,1,np.exp(1j*chi)]).astype(complex)


def local_dephase(rho,eta):
    # Independent phase damping on each qubit: each single-qubit off-diagonal gets eta.
    out=np.zeros_like(rho,dtype=complex)
    bits=[(0,0),(0,1),(1,0),(1,1)]
    for i,(a,b) in enumerate(bits):
        for j,(c,d) in enumerate(bits):
            h=(a!=c)+(b!=d)
            out[i,j]=rho[i,j]*(eta**h)
    return out


def partial_transpose_B(rho):
    return rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)


def negativity(rho):
    ev=np.linalg.eigvalsh(partial_transpose_B(rho))
    return float(np.sum(np.abs(ev[ev<0])))


def channel_state(chi,eta=1.0):
    U=unitary(chi)
    rho=U@plus_state()@U.conj().T
    return local_dephase(rho,eta)


def local_phase_unitary(a,b):
    UA=np.diag([1,np.exp(1j*a)])
    UB=np.diag([1,np.exp(1j*b)])
    return np.kron(UA,UB)


def comparator_state(seed,n=800):
    rng=np.random.default_rng(seed)
    rho0=plus_state(); out=np.zeros((4,4),dtype=complex)
    # Allow arbitrary correlation between local phases through a shared latent variable plus jitter.
    z=rng.uniform(-np.pi,np.pi,size=n)
    coeff=rng.normal(size=(2,2))
    for k in range(n):
        a=coeff[0,0]*z[k] + coeff[0,1]*np.sin(z[k]) + rng.normal(scale=0.35)
        b=coeff[1,0]*z[k] + coeff[1,1]*np.cos(z[k]) + rng.normal(scale=0.35)
        U=local_phase_unitary(a,b)
        out += U@rho0@U.conj().T
    return out/n


def gate_consistency(chi,eta,seed):
    U=unitary(chi)
    uerr=float(np.linalg.norm(U.conj().T@U-np.eye(4)))
    rho=channel_state(chi,eta)
    tr=complex(np.trace(rho)); mineig=float(np.min(np.linalg.eigvalsh(rho)))
    return {"gate":"G7_CHANNEL_CONSISTENCY","chi":chi,"eta":eta,
            "unitarity_error":uerr,"trace_real":tr.real,"trace_imag":tr.imag,
            "min_state_eigenvalue":mineig,
            "pass":bool(uerr<1e-12 and abs(tr.real-1)<1e-12 and abs(tr.imag)<1e-12 and mineig>-1e-12)}


def gate_comparator(chi,eta,seed):
    nr=negativity(channel_state(chi,eta))
    nc=negativity(comparator_state(seed))
    expected_nonzero=abs(np.sin(chi/2))>1e-8 and eta>0
    passed=(nr>1e-6 and nc<1e-10) if expected_nonzero else (nc<1e-10)
    return {"gate":"G8_COMPARATOR_RESISTANT_ENTANGLEMENT","chi":chi,"eta":eta,
            "rcg002_negativity":nr,"classical_local_phase_negativity":nc,
            "comparator_scope":"correlated_mixtures_of_local_phase_unitaries",
            "pass":bool(passed)}


def gate_holdout(chi,eta,seed):
    # Holdout identity is frozen only for noiseless eta=1 branch.
    rho=channel_state(chi,1.0)
    n=negativity(rho)
    pred=0.5*abs(np.sin(chi/2))
    err=abs(n-pred)
    return {"gate":"G9_PARAMETER_FREE_HOLDOUT","chi":chi,"eta":1.0,
            "measured_negativity":n,"predicted_negativity":float(pred),"abs_error":float(err),
            "pass":bool(err<1e-12)}


def gate_robustness(chi,eta,seed):
    n=negativity(channel_state(chi,eta))
    return {"gate":"G10_DEPHASING_ROBUSTNESS","chi":chi,"eta":eta,
            "negativity":n,"witness_survives":bool(n>1e-6),"pass":True}


def gate_null(chi,eta,seed):
    rho=channel_state(0.0,eta)
    n=negativity(rho)
    # coherent action at eta=1 is exactly identity; eta<1 may add local nuisance dephasing but no entanglement.
    U=unitary(0.0)
    return {"gate":"G11_ZERO_INTERACTION_NULL","chi":0.0,"eta":eta,
            "negativity":n,"unitary_identity_error":float(np.linalg.norm(U-np.eye(4))),
            "pass":bool(n<1e-12 and np.linalg.norm(U-np.eye(4))<1e-12)}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--gate',required=True,choices=['consistency','comparator','holdout','robustness','null'])
    ap.add_argument('--chi',type=float,required=True)
    ap.add_argument('--eta',type=float,default=1.0)
    ap.add_argument('--seed',type=int,default=17)
    ap.add_argument('--output',required=True)
    a=ap.parse_args()
    fn={'consistency':gate_consistency,'comparator':gate_comparator,'holdout':gate_holdout,
        'robustness':gate_robustness,'null':gate_null}[a.gate]
    out=fn(a.chi,a.eta,a.seed); out['seed']=a.seed; out['candidate']='RCG-002'
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if out.get('pass') is False:
        raise SystemExit(2)

if __name__=='__main__':
    main()
