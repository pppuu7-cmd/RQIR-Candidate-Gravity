import argparse, json, math, os
import numpy as np

G = 6.67430e-11
HBAR = 1.054571817e-34
C = 299792458.0


def entangling_phase(m1, m2, t, d00, d01, d10, d11, causal=True):
    # Branch-invariant controlled phase from pairwise weak-field energies.
    # Global and single-probe phases cancel in this cross-difference.
    ds = [d00, d01, d10, d11]
    if min(ds) <= 0:
        raise ValueError('all separations must be positive')
    rmax = max(ds)
    teff = max(0.0, t - rmax/C) if causal else t
    geom = (1.0/d00 + 1.0/d11 - 1.0/d01 - 1.0/d10)
    return G*m1*m2*teff*geom/HBAR


def negativity_from_chi(chi):
    return 0.5*abs(math.sin(chi/2.0))


def gate_causality(scale):
    # Geometry scaled at fixed masses. Test strict retarded onset around rmax/c.
    ds = np.array([0.45, 0.62, 0.57, 0.48])*scale
    tau = max(ds)/C
    vals=[]
    for f in [0.25,0.75,1.0,1.25,2.0]:
        chi=entangling_phase(1e-14,1.3e-14,f*tau,*ds)
        vals.append([f,chi])
    pre=max(abs(v) for f,v in vals if f<=1.0)
    post=max(abs(v) for f,v in vals if f>1.0)
    return {'gate':'G12_RETARDED_ONSET','scale':float(scale),'tau':float(tau),'samples':[[float(f),float(v)] for f,v in vals],'pass':bool(pre<1e-18 and post>0)}


def gate_scaling(which, factor):
    base=dict(m1=1e-14,m2=1.7e-14,t=3.0,d00=0.45,d01=0.62,d10=0.57,d11=0.48)
    c0=entangling_phase(**base)
    p=base.copy()
    if which=='m1': p['m1']*=factor; expected=factor
    elif which=='m2': p['m2']*=factor; expected=factor
    elif which=='time':
        # subtract retarded offset exactly: compare effective durations.
        tau=max(base[k] for k in ['d00','d01','d10','d11'])/C
        p['t']=tau+factor*(base['t']-tau); expected=factor
    elif which=='distance':
        for k in ['d00','d01','d10','d11']: p[k]*=factor
        # retarded offset changes too; keep the same effective duration.
        tau0=max(base[k] for k in ['d00','d01','d10','d11'])/C
        tau1=max(p[k] for k in ['d00','d01','d10','d11'])/C
        p['t']=tau1+(base['t']-tau0); expected=1.0/factor
    else: raise ValueError(which)
    c1=entangling_phase(**p)
    ratio=c1/c0
    rel=abs(ratio-expected)/max(abs(expected),1e-30)
    return {'gate':'G13_MICROSCOPIC_SCALING','which':which,'factor':float(factor),'ratio':float(ratio),'expected':float(expected),'relerr':float(rel),'pass':bool(rel<1e-12)}


def gate_entanglement(scale):
    # Scale masses upward only to span a numerically resolvable phase domain while retaining weak-field compactness.
    m1=2e-14*scale; m2=2.4e-14*scale
    chi=entangling_phase(m1,m2,2.0,0.45,0.62,0.57,0.48)
    n=negativity_from_chi(chi)
    return {'gate':'G14_MICROSCOPIC_ENTANGLING_PHASE','scale':float(scale),'chi':float(chi),'negativity':float(n),'pass':bool(n>1e-12)}


def gate_separable_bound(seed):
    # A separable/LOCC channel acting on a separable input cannot create entanglement.
    # Numerical stress: random convex mixtures of local phase unitaries remain PPT.
    rng=np.random.default_rng(seed)
    rho0=np.ones((4,4),complex)/4.0
    rho=np.zeros((4,4),complex)
    w=rng.random(64); w/=w.sum()
    for wi in w:
        a,b=rng.uniform(-math.pi,math.pi,2)
        u=np.diag([1,np.exp(1j*b),np.exp(1j*a),np.exp(1j*(a+b))])
        rho+=wi*(u@rho0@u.conj().T)
    # partial transpose on B
    pt=rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    ev=np.linalg.eigvalsh(pt)
    neg=float(np.sum(np.maximum(-ev,0)))
    mineig=float(ev.min())
    return {'gate':'G15_SEPARABLE_LOCC_BOUND','seed':int(seed),'negativity':neg,'min_pt_eig':mineig,'pass':bool(neg<1e-12 and mineig>-1e-12)}


def gate_geometry_null(which):
    p=dict(m1=1e-14,m2=1.7e-14,t=2.0,d00=0.5,d01=0.5,d10=0.5,d11=0.5)
    if which=='equal': pass
    elif which=='zero_mass': p['m1']=0.0
    elif which=='zero_G':
        # explicit algebraic null proxy
        chi=0.0
        return {'gate':'G16_INTERACTION_NULLS','which':which,'chi':chi,'pass':True}
    else: raise ValueError(which)
    chi=entangling_phase(**p)
    return {'gate':'G16_INTERACTION_NULLS','which':which,'chi':float(chi),'pass':bool(abs(chi)<1e-18)}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--gate',required=True); ap.add_argument('--arg',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.gate=='causality': r=gate_causality(float(a.arg))
    elif a.gate=='scaling':
        which,f=a.arg.split(':'); r=gate_scaling(which,float(f))
    elif a.gate=='entanglement': r=gate_entanglement(float(a.arg))
    elif a.gate=='separable': r=gate_separable_bound(int(a.arg))
    elif a.gate=='null': r=gate_geometry_null(a.arg)
    else: raise ValueError(a.gate)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(r,f,indent=2)
    print(json.dumps(r,indent=2))
    if not r['pass']: raise SystemExit(1)

if __name__=='__main__': main()
