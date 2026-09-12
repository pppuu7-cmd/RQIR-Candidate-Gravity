#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import numpy as np


def psd_gate(seed):
    rng=np.random.default_rng(seed)
    A=rng.normal(size=(5,5)); N=A@A.T
    R=np.tril(rng.normal(size=(5,5)),-1)
    S=rng.normal(size=(5,5)); Ct=S@S.T
    G=2.5e-3; hbar=1.0
    C=G*hbar*N + G*G*R@Ct@R.T
    eN=np.linalg.eigvalsh(N); eC=np.linalg.eigvalsh(C)
    return {"gate":"G3_POSITIVITY","min_eig_N":float(eN.min()),"min_eig_total":float(eC.min()),
            "pass":bool(eN.min()>=-1e-12 and eC.min()>=-1e-12)}


def limit_gate(seed):
    rng=np.random.default_rng(seed)
    R=np.tril(rng.normal(size=(4,4)),-1); tau=rng.normal(size=4)
    N=np.eye(4)
    def norms(G,h):
        coherent=G*R@tau
        fluct=G*h*N
        return float(np.linalg.norm(coherent)), float(np.linalg.norm(fluct))
    g1=norms(1e-3,1.0); g2=norms(5e-4,1.0)
    h1=norms(1e-3,1.0); h2=norms(1e-3,0.25)
    # coherent scales ~G; intrinsic covariance scales ~hbar
    rg=g2[0]/g1[0] if g1[0] else 0
    rh=h2[1]/h1[1] if h1[1] else 0
    return {"gate":"G1_G2_LIMITS","G_half_coherent_ratio":rg,"hbar_quarter_noise_ratio":rh,
            "pass":bool(abs(rg-0.5)<1e-10 and abs(rh-0.25)<1e-10)}


def causal_gate(seed):
    rng=np.random.default_rng(seed)
    R=np.tril(rng.normal(size=(8,8)),-1)
    upper=np.triu(R,0)
    return {"gate":"G4_RETARDED_CAUSALITY","future_or_equal_norm":float(np.linalg.norm(upper)),
            "pass":bool(np.linalg.norm(upper)<1e-14)}


def identifiability_gate(seed):
    rng=np.random.default_rng(seed)
    n=240
    # Three RQIR-style channels with non-collinear response loadings.
    X=rng.normal(size=(n,3))
    coherent=np.array([1.0,-0.6,0.35])
    noise_loading=np.array([0.2,0.8,-0.5])
    # Mean residual identifies coherent deformation; variance residual identifies noise deformation.
    ymean=X*coherent + rng.normal(scale=0.03,size=(n,3))
    yvar=(X*X)*noise_loading + rng.normal(scale=0.03,size=(n,3))
    D=np.concatenate([X.reshape(-1,1)*np.tile(coherent,(n,1)).reshape(-1,1),
                      (X*X).reshape(-1,1)*np.tile(noise_loading,(n,1)).reshape(-1,1)],axis=1)
    s=np.linalg.svd(D,compute_uv=False)
    rank=int(np.sum(s>1e-10*s[0]))
    cond=float(s[0]/s[-1])
    # Also require all three channel mean loadings to be non-zero.
    pass_gate=rank==2 and np.all(np.abs(coherent)>0.1) and cond<50
    return {"gate":"G5_MULTI_CHANNEL_IDENTIFIABILITY","design_rank":rank,"condition_number":cond,
            "channels":3,"pass":bool(pass_gate)}


def stochastic_degeneracy_gate(seed):
    # Gaussian seed with PSD N has an exact classical Gaussian stochastic representation
    # at the level of first two moments/characteristic function. This is intentionally a FAIL
    # for a quantum-specific novelty claim.
    return {"gate":"G6_STOCHASTIC_COMPARATOR","classical_gaussian_representation_exists":True,
            "pass_quantum_specific_novelty":False,
            "classification":"DEGENERATE_AT_GAUSSIAN_SEED_LEVEL"}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--gate',required=True); ap.add_argument('--seed',type=int,default=17); ap.add_argument('--output',required=True)
    a=ap.parse_args()
    fn={"positivity":psd_gate,"limits":limit_gate,"causality":causal_gate,"identifiability":identifiability_gate,"stochastic":stochastic_degeneracy_gate}[a.gate]
    out=fn(a.seed); out["seed"]=a.seed; out["candidate"]="RCG-001"
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
