import argparse, json, math, os
import numpy as np

G=6.67430e-11
HBAR=1.054571817e-34
C=299792458.0
BASIS_BITS=[(0,0),(0,1),(1,0),(1,1)]


def microscopic_chi(scale=1.0):
    m1=2e-14*scale; m2=2.4e-14*scale; t=2.0
    ds=[0.45,0.62,0.57,0.48]
    teff=max(0.0,t-max(ds)/C)
    geom=1/ds[0]+1/ds[3]-1/ds[1]-1/ds[2]
    return G*m1*m2*teff*geom/HBAR


def negativity(rho):
    pt=rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    ev=np.linalg.eigvalsh((pt+pt.conj().T)/2)
    return float(np.maximum(-ev,0).sum())


def dephasing_factor(i,j,cov):
    bi=np.array(BASIS_BITS[i],float); bj=np.array(BASIS_BITS[j],float)
    d=bi-bj
    return float(np.exp(-0.5*d@cov@d))


def apply_channel(rho,chi,cov):
    phase=np.array([1,1,1,np.exp(1j*chi)],complex)
    out=np.empty_like(rho,dtype=complex)
    for i in range(4):
        for j in range(4):
            out[i,j]=phase[i]*phase[j].conjugate()*dephasing_factor(i,j,cov)*rho[i,j]
    return out


def plus_state():
    v=np.ones(4,complex)/2
    return np.outer(v,v.conj())


def gate_boundary(arg):
    scale,corr=[float(x) for x in arg.split(':')]
    chi=microscopic_chi(scale)
    rho=plus_state()
    n0=negativity(apply_channel(rho,chi,np.zeros((2,2))))
    # Dense logarithmic scan followed by bisection for N <= 1e-10.
    def n_of(g):
        cov=g*np.array([[1.0,corr],[corr,1.3]])
        return negativity(apply_channel(rho,chi,cov))
    grid=np.geomspace(1e-8,1.0,321)
    vals=[n_of(float(g)) for g in grid]
    idx=next((i for i,n in enumerate(vals) if n<=1e-10),None)
    if idx is None:
        gc=float('nan'); bracket=None
    elif idx==0:
        gc=float(grid[0]); bracket=[0.0,float(grid[0])]
    else:
        lo=float(grid[idx-1]); hi=float(grid[idx])
        for _ in range(70):
            mid=0.5*(lo+hi)
            if n_of(mid)>1e-10: lo=mid
            else: hi=mid
        gc=hi; bracket=[lo,hi]
    ratio=gc/abs(chi) if np.isfinite(gc) and chi!=0 else float('nan')
    return {'gate':'G22_NOISE_ENTANGLEMENT_BOUNDARY','scale':scale,'corr':corr,'chi':float(chi),'negativity_noiseless':n0,'gamma_critical':gc,'gamma_c_over_abs_chi':ratio,'bracket':bracket,'pass':bool(n0>1e-10 and np.isfinite(gc) and gc>0)}


def local_measure_prepare_channel(rho,eta,theta):
    # Explicit entanglement-breaking LOCC-like comparator: computational-basis
    # local measurement followed by product-state preparation with tunable local
    # Bloch rotations. It may carry correlated classical outcomes but cannot
    # create entanglement from a separable input.
    probs=np.real(np.diag(rho)).clip(min=0)
    probs=probs/probs.sum()
    out=np.zeros((4,4),complex)
    for k,(a,b) in enumerate(BASIS_BITS):
        aa=(a ^ (1 if eta>0.5 else 0))
        bb=(b ^ (1 if eta< -0.5 else 0))
        va=np.array([math.cos(theta/2), ((-1)**aa)*math.sin(theta/2)],complex)
        vb=np.array([math.cos(theta/2), ((-1)**bb)*math.sin(theta/2)],complex)
        psi=np.kron(va,vb)
        out += probs[k]*np.outer(psi,psi.conj())
    return out


def gate_classical(arg):
    eta,theta=[float(x) for x in arg.split(':')]
    rho=plus_state()
    out=local_measure_prepare_channel(rho,eta,theta)
    n=negativity(out)
    mine=float(np.linalg.eigvalsh((out+out.conj().T)/2).min())
    tr=float(np.trace(out).real)
    # Compare against coherent microscopic channel at scale 2.
    chi=microscopic_chi(2.0)
    q=negativity(apply_channel(rho,chi,np.zeros((2,2))))
    return {'gate':'G23_CLASSICAL_MEASURE_PREPARE_COMPARATOR','eta':eta,'theta':theta,'classical_negativity':n,'quantum_reference_negativity':q,'min_state_eig':mine,'trace':tr,'pass':bool(n<1e-11 and q>1e-10 and mine>-1e-11 and abs(tr-1)<1e-12)}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--gate',required=True); ap.add_argument('--arg',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.gate=='boundary': r=gate_boundary(a.arg)
    elif a.gate=='classical': r=gate_classical(a.arg)
    else: raise ValueError(a.gate)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(r,f,indent=2)
    print(json.dumps(r,indent=2))
    if not r['pass']: raise SystemExit(1)

if __name__=='__main__': main()
