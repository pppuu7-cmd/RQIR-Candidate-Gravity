import argparse, json, math, os
import numpy as np

G=6.67430e-11
HBAR=1.054571817e-34
C=299792458.0
I2=np.eye(2,dtype=complex)
Z=np.array([[1,0],[0,-1]],complex)


def microscopic_chi(scale=1.0):
    m1=2e-14*scale; m2=2.4e-14*scale; t=2.0
    ds=[0.45,0.62,0.57,0.48]
    teff=max(0.0,t-max(ds)/C)
    geom=1/ds[0]+1/ds[3]-1/ds[1]-1/ds[2]
    return G*m1*m2*teff*geom/HBAR


def plus_state():
    v=np.ones(4,complex)/2
    return np.outer(v,v.conj())


def negativity(rho):
    pt=rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    ev=np.linalg.eigvalsh((pt+pt.conj().T)/2)
    return float(np.maximum(-ev,0).sum())


def coherent_target(scale):
    chi=microscopic_chi(scale)
    phase=np.array([1,1,1,np.exp(1j*chi)],complex)
    rho=plus_state()
    out=(phase[:,None]*rho)*phase.conj()[None,:]
    return chi,out


def rz(phi):
    return np.diag([np.exp(-0.5j*phi),np.exp(0.5j*phi)])


def weak_z_kraus(mu,s):
    # Two-outcome unsharp Z measurement: E_s=(I+s*mu*Z)/2, 0<=mu<1.
    e0=0.5*(1+s*mu)
    e1=0.5*(1-s*mu)
    return np.diag([math.sqrt(max(e0,0.0)),math.sqrt(max(e1,0.0))]).astype(complex)


def measurement_feedback_channel(rho,mu,lam):
    # Explicit continuous-measurement surrogate: local unsharp measurements,
    # classical exchange of outcomes, and reciprocal local Z feedback. Every
    # trajectory is a product of local operations; averaging therefore remains
    # in the LOCC/separable class for product input.
    out=np.zeros((4,4),complex)
    for sa in (-1,1):
        for sb in (-1,1):
            ma=weak_z_kraus(mu,sa); mb=weak_z_kraus(mu,sb)
            m=np.kron(ma,mb)
            # A receives b's classical record and conversely.
            u=np.kron(rz(lam*sb),rz(lam*sa))
            k=u@m
            out += k@rho@k.conj().T
    return out


def trace_distance(a,b):
    d=(a-b + (a-b).conj().T)/2
    ev=np.linalg.eigvalsh(d)
    return float(0.5*np.abs(ev).sum())


def purity(rho):
    return float(np.real(np.trace(rho@rho)))


def gate(arg):
    scale,mu=[float(x) for x in arg.split(':')]
    chi,target=coherent_target(scale)
    nt=negativity(target)
    rho0=plus_state()
    # Optimize reciprocal feedback over a broad deterministic grid. This gives
    # the semiclassical comparator its best chance within the preregistered family.
    grid=np.linspace(-math.pi,math.pi,1201)
    best=None
    for lam in grid:
        out=measurement_feedback_channel(rho0,mu,float(lam))
        td=trace_distance(out,target)
        if best is None or td<best[0]:
            best=(td,float(lam),out)
    td,lam,out=best
    nc=negativity(out)
    ev=np.linalg.eigvalsh((out+out.conj().T)/2)
    tr=float(np.trace(out).real)
    # Ratio is descriptive and scale-normalized. The hard gate only claims
    # exclusion of this explicit LOCC continuous-measurement+feedback family.
    ratio=td/max(nt,1e-30)
    passed=(nt>1e-10 and nc<1e-10 and ev.min()>-1e-11 and abs(tr-1)<1e-12 and ratio>0.25)
    return {
        'gate':'G24_CONTINUOUS_MEASUREMENT_FEEDBACK_COMPARATOR',
        'scale':scale,'mu':mu,'chi':float(chi),
        'target_negativity':nt,'best_classical_negativity':nc,
        'best_feedback_lambda':lam,'best_trace_distance':td,
        'distance_over_target_negativity':ratio,
        'classical_purity':purity(out),'min_state_eig':float(ev.min()),
        'trace':tr,'pass':bool(passed),
        'scope_lock':'Explicit reciprocal local weak-Z measurement plus classical-record local Z feedback only; not the full class of semiclassical gravity models.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--arg',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); r=gate(a.arg)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(r,f,indent=2)
    print(json.dumps(r,indent=2))
    if not r['pass']: raise SystemExit(1)

if __name__=='__main__': main()
