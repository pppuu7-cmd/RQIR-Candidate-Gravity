#!/usr/bin/env python3
"""Iter011 / G29: robustness suite for the RQIR-CG two-qubit comparator layer.

Frozen scope inherited from G28 only:
  finite two-qubit Markovian single-axis-per-site measurement-feedback family,
  with Gamma_A Gamma_B = chi^2.

This suite tests robustness/validity of that finite comparator layer. It does NOT
turn a finite-family gap into a theorem about all semiclassical-gravity models.
Scientific negative results are written to JSON and return exit code 0; only
invalid/incomplete numerics are infrastructure failures.
"""
import argparse, json, math
from pathlib import Path
import numpy as np

I2=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.array([[1,0],[0,-1]],dtype=complex)
I4=np.eye(4,dtype=complex)
ZZ=np.kron(Z,Z)
PLUS=np.array([1,1],dtype=complex)/math.sqrt(2)
PSI0=np.kron(PLUS,PLUS)
RHO0=np.outer(PSI0,PSI0.conj())
CASES=[(0.5,0.05),(1.0,0.10),(2.0,0.20),(4.0,0.35)]

def td(a,b):
    return float(.5*np.sum(np.linalg.svd(a-b,compute_uv=False)))

def neg(r):
    p=r.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    e=np.linalg.eigvalsh((p+p.conj().T)/2)
    return float(np.sum(np.abs(e[e<0])))

def target(theta):
    U=math.cos(theta)*I4-1j*math.sin(theta)*ZZ
    return U@RHO0@U.conj().T

def axis(alpha,beta):
    return np.array([math.sin(beta)*math.cos(alpha),math.sin(beta)*math.sin(alpha),math.cos(beta)],dtype=float)

def op(v):
    v=np.asarray(v,dtype=float); v=v/np.linalg.norm(v)
    return v[0]*X+v[1]*Y+v[2]*Z

def Lgen(chi,A,B,a=0.0):
    ga=abs(chi)*math.exp(float(a)); gb=abs(chi)*math.exp(float(-a))
    H=chi*np.kron(A,B)
    L=-1j*(np.kron(I4,H)-np.kron(H.T,I4))
    for rate,Q in ((ga,np.kron(A,I2)),(gb,np.kron(I2,B))):
        Q2=Q.conj().T@Q
        L += rate*(np.kron(Q.conj(),Q)-.5*np.kron(I4,Q2)-.5*np.kron(Q2.T,I4))
    return L,ga,gb

def exp_super(L,t=1.0):
    w,v=np.linalg.eig(L*t)
    return v@np.diag(np.exp(w))@np.linalg.inv(v)

def evolve(L,rho=RHO0,t=1.0):
    E=exp_super(L,t)
    r=(E@rho.reshape(-1,order='F')).reshape(4,4,order='F')
    r=(r+r.conj().T)/2
    tr=np.trace(r)
    if abs(tr)==0: raise FloatingPointError('zero trace')
    return r/tr

def rk4(L,rho,n):
    y=rho.reshape(-1,order='F').astype(complex); h=1.0/n
    for _ in range(n):
        k1=L@y; k2=L@(y+.5*h*k1); k3=L@(y+.5*h*k2); k4=L@(y+h*k3)
        y=y+h*(k1+2*k2+2*k3+k4)/6
    r=y.reshape(4,4,order='F'); r=(r+r.conj().T)/2
    return r/np.trace(r)

def choi(E):
    d=4; J=np.zeros((d*d,d*d),dtype=complex)
    for i in range(d):
        for j in range(d):
            M=np.zeros((d,d),dtype=complex); M[i,j]=1
            out=(E@M.reshape(-1,order='F')).reshape(d,d,order='F')
            J[i*d:(i+1)*d,j*d:(j+1)*d]=out
    return (J+J.conj().T)/2

def local_unitary(v,ang):
    Q=op(v)
    return math.cos(ang/2)*I2-1j*math.sin(ang/2)*Q

def finite_ok(*xs):
    return all(np.all(np.isfinite(np.asarray(x))) for x in xs)

def stream_basis(scale,theta,shard):
    th=scale*theta; tar=target(th)
    A=op(axis(0.3+0.17*shard,0.8)); B=op(axis(-0.5,1.1+0.09*shard))
    L,_,_=Lgen(th,A,B,0.4-0.15*shard); comp=evolve(L)
    UA=local_unitary(axis(.7,1.0),0.41+0.07*shard)
    UB=local_unitary(axis(-.2,.9),-0.33+0.05*shard)
    U=np.kron(UA,UB); tar2=U@tar@U.conj().T; comp2=U@comp@U.conj().T
    d0=td(tar,comp); d1=td(tar2,comp2); n0=neg(tar); n1=neg(tar2)
    err=max(abs(d1-d0),abs(n1-n0))
    return {'metric_error':err,'td_before':d0,'td_after':d1,'neg_before':n0,'neg_after':n1,
            'scientific_support':err<1e-10,'interpretation':'Local-unitary covariance of diagnostics.'}

def stream_admissibility(scale,theta,shard):
    th=scale*theta; A=op(axis(.2+.31*shard,.6+.12*shard)); B=op(axis(-.4+.19*shard,1.2-.08*shard))
    L,ga,gb=Lgen(th,A,B,-.9+.6*shard); E=exp_super(L)
    trace_row=I4.reshape(-1,order='F').conj()
    tp_gen=float(np.linalg.norm(trace_row@L))
    ce=np.linalg.eigvalsh(choi(E)); min_choi=float(np.min(ce))
    mins=[]; trace_err=[]
    for t in (0.0,.125,.25,.5,1.0):
        r=evolve(L,t=t); mins.append(float(np.min(np.linalg.eigvalsh(r)))); trace_err.append(abs(float(np.real(np.trace(r)))-1.0))
    support=tp_gen<1e-10 and min_choi>-1e-8 and min(mins)>-1e-8 and max(trace_err)<1e-10
    return {'tp_generator_residual':tp_gen,'choi_min_eig':min_choi,'state_min_eig':min(mins),
            'max_trace_error':max(trace_err),'ga_gb_minus_chi2':ga*gb-th*th,'scientific_support':support,
            'interpretation':'Numerical TP/CP/PSD admissibility of sampled comparator channels.'}

def stream_null(scale,theta,shard):
    th=scale*theta; aa=-1.2+.8*shard
    va=axis(.4+.2*shard,.7+.1*shard); vb=axis(-.6+.13*shard,1.0-.07*shard)
    A=op(va); B=op(vb); L,_,_=Lgen(th,A,B,aa); null=evolve(L)
    vals=[]
    for da in (0.0,-.2,.2):
        for db in (0.0,-.08,.08):
            A2=op(axis(.4+.2*shard+db,.7+.1*shard)); B2=op(vb)
            L2,_,_=Lgen(th,A2,B2,aa+da); vals.append(td(evolve(L2),null))
    best=float(min(vals)); recovered=best<1e-10
    return {'null_best_gap':best,'n_candidates':len(vals),'scientific_support':recovered,
            'interpretation':'False-positive calibration: an in-family target must be recovered as zero-gap.'}

def stream_convergence(scale,theta,shard):
    th=scale*theta; A=op(axis(.25+.15*shard,.75)); B=op(axis(-.45,1.05-.05*shard))
    L,_,_=Lgen(th,A,B,-.6+.35*shard); exact=evolve(L)
    ns=[50,100,200,400]; errs=[]
    for n in ns: errs.append(td(rk4(L,RHO0,n),exact))
    monotonic=all(errs[i+1] <= max(errs[i]*1.05,1e-13) for i in range(len(errs)-1))
    support=errs[-1]<1e-7 and monotonic
    return {'rk4_steps':ns,'trace_distance_errors':errs,'finest_error':errs[-1],
            'monotonic_convergence':monotonic,'scientific_support':support,
            'interpretation':'Independent RK4 cross-check against eigendecomposition propagator.'}

def state_from_p(p):
    logchi,a,alA,beA,alB,beB=p; chi=math.exp(logchi)
    L,_,_=Lgen(chi,op(axis(alA,beA)),op(axis(alB,beB)),a)
    return evolve(L)

def feature(r):
    return np.concatenate([r.real.ravel(),r.imag.ravel()])

def stream_identifiability(scale,theta,shard):
    th=max(abs(scale*theta),1e-4)
    p=np.array([math.log(th),-.55+.3*shard,.4+.11*shard,.8+.04*shard,-.5+.07*shard,1.1-.05*shard],dtype=float)
    h=1e-5; cols=[]
    for k in range(len(p)):
        dp=np.zeros_like(p); dp[k]=h
        cols.append((feature(state_from_p(p+dp))-feature(state_from_p(p-dp)))/(2*h))
    J=np.stack(cols,axis=1); sv=np.linalg.svd(J,compute_uv=False)
    rel=sv/(sv[0] if sv[0] else 1.0); rank=int(np.sum(rel>1e-7)); cond=float(sv[0]/max(sv[-1],1e-300))
    support=(rank==len(p))
    return {'jacobian_shape':list(J.shape),'singular_values':sv.tolist(),'relative_singular_values':rel.tolist(),
            'effective_rank_1e-7':rank,'parameter_count':len(p),'condition_number':cond,'scientific_support':support,
            'interpretation':'Local identifiability of six-parameter continuous comparator chart; rank loss is a scientific finding, not CI failure.'}

def comparator_gap(x,th,tar):
    alA,beA,alB,beB,a=x
    L,_,_=Lgen(th,op(axis(alA,beA)),op(axis(alB,beB)),a)
    return td(evolve(L),tar)

def stream_adversarial(scale,theta,shard):
    th=scale*theta; tar=target(th); rng=np.random.default_rng(29011+shard)
    best=float('inf'); bestx=None; evals=0; restarts=16
    for _ in range(restarts):
        x=np.array([rng.uniform(-math.pi,math.pi),rng.uniform(0,math.pi),rng.uniform(-math.pi,math.pi),rng.uniform(0,math.pi),rng.uniform(-2,2)])
        f=comparator_gap(x,th,tar); evals+=1
        for step in (0.8,0.4,0.2,0.1,0.05,0.025):
            improved=True; sweeps=0
            while improved and sweeps<2:
                improved=False; sweeps+=1
                for k in range(5):
                    for sgn in (-1,1):
                        y=x.copy(); y[k]+=sgn*step
                        if k==4: y[k]=float(np.clip(y[k],-3,3))
                        g=comparator_gap(y,th,tar); evals+=1
                        if g+1e-14<f: x,f=y,g; improved=True
        if f<best: best=float(f); bestx=x.copy()
    support=best>1e-4
    return {'best_continuous_gap':best,'best_parameters':bestx.tolist(),'n_evaluations':evals,'restarts':restarts,
            'scientific_support':support,
            'interpretation':'Multistart continuous adversarial search inside the frozen single-axis Markovian family; nonzero gap is family-scoped only.'}

STREAMS={'basis_covariance':stream_basis,'admissibility':stream_admissibility,'null_calibration':stream_null,
         'convergence':stream_convergence,'identifiability':stream_identifiability,'adversarial':stream_adversarial}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=STREAMS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); scale,theta=CASES[a.shard]
    res=STREAMS[a.stream](scale,theta,a.shard)
    structural=finite_ok([scale,theta]) and isinstance(res.get('scientific_support'),(bool,np.bool_))
    out={'iteration':'Iter011','gate':'G29','stream':a.stream,'shard':a.shard,'scale':scale,'theta_base':theta,'theta':scale*theta,
         'frozen_thresholds':{'metric_invariance':1e-10,'admissibility_eig_floor':-1e-8,'null_gap':1e-10,'convergence_finest':1e-7,'identifiability_relative_sv':1e-7,'adversarial_nonzero_gap':1e-4},
         'result':res,'structural_valid':bool(structural),
         'scope_lock':'Finite two-qubit Markovian single-axis-per-site measurement-feedback family with Gamma_A*Gamma_B=chi^2; not a general semiclassical-gravity no-go theorem.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)

if __name__=='__main__': main()
