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
    return chi,(phase[:,None]*rho)*phase.conj()[None,:]


def rz(phi):
    return np.diag([np.exp(-0.5j*phi),np.exp(0.5j*phi)])


def weak_z_kraus(mu,s):
    e0=0.5*(1+s*mu); e1=0.5*(1-s*mu)
    return np.diag([math.sqrt(max(e0,0.0)),math.sqrt(max(e1,0.0))]).astype(complex)


def one_step(rho,mu,lam):
    out=np.zeros((4,4),complex)
    for sa in (-1,1):
        for sb in (-1,1):
            ma=weak_z_kraus(mu,sa); mb=weak_z_kraus(mu,sb)
            m=np.kron(ma,mb)
            u=np.kron(rz(lam*sb),rz(lam*sa))
            k=u@m
            out += k@rho@k.conj().T
    return out


def evolved(rho0,rate,gain,n):
    # Diffusive scaling: measurement contrast and record-conditioned feedback
    # are O(sqrt(dt)); repeating N=1/dt local-LOCC steps defines the operational
    # continuous-time limit tested here. No nonlocal quantum operation is used.
    dt=1.0/n
    mu=min(math.sqrt(2.0*rate*dt),0.999999)
    lam=gain*math.sqrt(dt)
    rho=rho0.copy()
    for _ in range(n): rho=one_step(rho,mu,lam)
    return rho


def trace_distance(a,b):
    d=(a-b+(a-b).conj().T)/2
    ev=np.linalg.eigvalsh(d)
    return float(0.5*np.abs(ev).sum())


def optimize(target,rho0,rate,n):
    # Broad signed feedback-gain grid. Keep deterministic/preregistered.
    gains=np.linspace(-4.0,4.0,401)
    best=None
    for g in gains:
        out=evolved(rho0,rate,float(g),n)
        td=trace_distance(out,target)
        if best is None or td<best[0]: best=(td,float(g),out)
    return best


def gate(arg):
    scale,rate=[float(x) for x in arg.split(':')]
    chi,target=coherent_target(scale); nt=negativity(target); rho0=plus_state()
    ns=[8,16,32,64]
    rows=[]
    for n in ns:
        td,g,out=optimize(target,rho0,rate,n)
        ev=np.linalg.eigvalsh((out+out.conj().T)/2)
        rows.append({'n':n,'best_trace_distance':td,'best_gain':g,
                     'negativity':negativity(out),'trace':float(np.trace(out).real),
                     'min_eig':float(ev.min())})
    # Continuum diagnostic: optimized outputs/distances should stop changing as N doubles.
    d32=rows[-2]['best_trace_distance']; d64=rows[-1]['best_trace_distance']
    rel_drift=abs(d64-d32)/max(d64,nt,1e-15)
    # LOCC preservation is a hard exact-structure consequence numerically checked at every N.
    states_ok=all(r['negativity']<1e-10 and r['min_eig']>-1e-10 and abs(r['trace']-1)<2e-11 for r in rows)
    ratio=d64/max(nt,1e-30)
    # Pre-registered gates: target genuinely entangled, LOCC family stays separable,
    # N=32->64 optimized distance is numerically stable at 20% relative scale,
    # and the continuous-limit comparator cannot close the coherent-target gap.
    passed=(nt>1e-10 and states_ok and rel_drift<0.20 and ratio>0.25)
    return {
      'gate':'G25_CONTINUOUS_TIME_LOCC_LIMIT', 'scale':scale,'rate':rate,'chi':float(chi),
      'target_negativity':nt,'n_sequence':ns,'rows':rows,
      'continuum_relative_distance_drift_32_64':rel_drift,
      'distance_over_target_negativity_N64':ratio,
      'all_states_physical_and_separable':bool(states_ok),'pass':bool(passed),
      'scope_lock':'Operational diffusive-scaling limit of reciprocal local weak-Z measurement plus classical-record local Z feedback only. PASS does not exclude arbitrary semiclassical gravity, non-Markovian classical channels, or models outside this LOCC family.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--arg',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); r=gate(a.arg)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(r,f,indent=2)
    print(json.dumps(r,indent=2))
    if not r['pass']: raise SystemExit(1)

if __name__=='__main__': main()
