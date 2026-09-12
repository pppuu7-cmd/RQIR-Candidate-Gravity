import argparse, json, math, os
import numpy as np

G = 6.67430e-11
HBAR = 1.054571817e-34
C = 299792458.0

BASIS_BITS = [(0,0),(0,1),(1,0),(1,1)]


def microscopic_chi(scale=1.0):
    m1=2e-14*scale
    m2=2.4e-14*scale
    t=2.0
    ds=[0.45,0.62,0.57,0.48]
    teff=max(0.0,t-max(ds)/C)
    geom=1/ds[0]+1/ds[3]-1/ds[1]-1/ds[2]
    return G*m1*m2*teff*geom/HBAR


def negativity(rho):
    pt=rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    ev=np.linalg.eigvalsh((pt+pt.conj().T)/2)
    return float(np.maximum(-ev,0).sum())


def dephasing_factor(i,j,cov):
    # Random local phases phi_A n_A + phi_B n_B with Gaussian covariance cov.
    bi=np.array(BASIS_BITS[i],float)
    bj=np.array(BASIS_BITS[j],float)
    d=bi-bj
    return float(np.exp(-0.5*d@cov@d))


def apply_channel(rho,chi,cov):
    phase=np.array([1,1,1,np.exp(1j*chi)],complex)
    out=np.empty_like(rho,dtype=complex)
    for i in range(4):
        for j in range(4):
            out[i,j]=phase[i]*phase[j].conjugate()*dephasing_factor(i,j,cov)*rho[i,j]
    return out


def apply_unitary(rho,chi):
    u=np.diag([1,1,1,np.exp(1j*chi)])
    return u@rho@u.conj().T


def apply_noise(rho,cov):
    return apply_channel(rho,0.0,cov)


def choi_matrix(chi,cov):
    J=np.zeros((16,16),complex)
    for i in range(4):
        for j in range(4):
            Eij=np.zeros((4,4),complex); Eij[i,j]=1
            Y=apply_channel(Eij,chi,cov)
            # J=sum_ij |i><j| \otimes E(|i><j|)
            for a in range(4):
                for b in range(4):
                    J[4*i+a,4*j+b]=Y[a,b]
    return (J+J.conj().T)/2


def gate_cptp(arg):
    gamma,rho_c=[float(x) for x in arg.split(':')]
    cov=gamma*np.array([[1.0,rho_c],[rho_c,1.3]])
    chi=microscopic_chi(1.0)
    ev=np.linalg.eigvalsh(choi_matrix(chi,cov))
    # TP checked directly on basis outputs.
    max_tp=0.0
    for i in range(4):
        E=np.zeros((4,4),complex); E[i,i]=1
        max_tp=max(max_tp,abs(np.trace(apply_channel(E,chi,cov))-1.0))
    mine=float(ev.min())
    return {'gate':'G17_UNIFIED_CPTP','gamma':gamma,'corr':rho_c,'min_choi_eig':mine,'max_tp_error':float(max_tp),'pass':bool(mine>-1e-11 and max_tp<1e-12)}


def gate_coherent_limit(scale):
    chi=microscopic_chi(scale)
    plus=np.ones(4,complex)/2
    rho=np.outer(plus,plus.conj())
    z=np.zeros((2,2))
    a=apply_channel(rho,chi,z); b=apply_unitary(rho,chi)
    err=float(np.linalg.norm(a-b))
    n=negativity(a)
    expected=0.5*abs(math.sin(chi/2))
    return {'gate':'G18_COHERENT_LIMIT','scale':float(scale),'chi':float(chi),'fro_error':err,'negativity':n,'expected_negativity':expected,'pass':bool(err<1e-13 and abs(n-expected)<1e-12)}


def gate_noise_limit(arg):
    gamma,rho_c=[float(x) for x in arg.split(':')]
    cov=gamma*np.array([[1.0,rho_c],[rho_c,1.3]])
    plus=np.ones(4,complex)/2; rho=np.outer(plus,plus.conj())
    out=apply_channel(rho,0.0,cov)
    n=negativity(out)
    mine=float(np.linalg.eigvalsh(out).min())
    return {'gate':'G19_NOISE_ONLY_SEPARABLE','gamma':gamma,'corr':rho_c,'negativity':n,'min_state_eig':mine,'pass':bool(n<1e-11 and mine>-1e-11)}


def gate_no_double_count(arg):
    gamma,rho_c=[float(x) for x in arg.split(':')]
    cov=gamma*np.array([[1.0,rho_c],[rho_c,1.3]])
    chi=microscopic_chi(1.0)
    rng=np.random.default_rng(119)
    A=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)); rho=A@A.conj().T; rho/=np.trace(rho)
    direct=apply_channel(rho,chi,cov)
    seq1=apply_noise(apply_unitary(rho,chi),cov)
    seq2=apply_unitary(apply_noise(rho,cov),chi)
    e1=float(np.linalg.norm(direct-seq1)); e2=float(np.linalg.norm(direct-seq2)); eo=float(np.linalg.norm(seq1-seq2))
    return {'gate':'G20_NO_DOUBLE_COUNT_COMPOSITION','gamma':gamma,'corr':rho_c,'direct_vs_U_then_N':e1,'direct_vs_N_then_U':e2,'order_error':eo,'pass':bool(max(e1,e2,eo)<1e-12)}


def gate_robustness(gamma):
    cov=float(gamma)*np.array([[1.0,0.35],[0.35,1.3]])
    chi=microscopic_chi(2.0)
    plus=np.ones(4,complex)/2; rho=np.outer(plus,plus.conj())
    n0=negativity(apply_channel(rho,chi,np.zeros((2,2))))
    n=negativity(apply_channel(rho,chi,cov))
    return {'gate':'G21_ENTANGLEMENT_NOISE_ROBUSTNESS','gamma':float(gamma),'chi':float(chi),'negativity_noiseless':n0,'negativity_noisy':n,'pass':bool(n>1e-10 and n<=n0+1e-12)}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--gate',required=True); ap.add_argument('--arg',required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.gate=='cptp': r=gate_cptp(a.arg)
    elif a.gate=='coherent_limit': r=gate_coherent_limit(float(a.arg))
    elif a.gate=='noise_limit': r=gate_noise_limit(a.arg)
    elif a.gate=='no_double_count': r=gate_no_double_count(a.arg)
    elif a.gate=='robustness': r=gate_robustness(float(a.arg))
    else: raise ValueError(a.gate)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(r,f,indent=2)
    print(json.dumps(r,indent=2))
    if not r['pass']: raise SystemExit(1)

if __name__=='__main__': main()
