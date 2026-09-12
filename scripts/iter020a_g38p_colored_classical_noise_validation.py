#!/usr/bin/env python3
"""Iter020A / G38-P: implementation/provenance validation for a finite-correlation
classical Gaussian colored-noise comparator ingredient.

Take stationary Ornstein-Uhlenbeck covariance C(t,s)=sigma2 exp(-|t-s|/tau)
and H_noise(t)=xi(t) F with F=cA A⊗I+cB I⊗B. Because F is fixed and local terms
commute, the integrated phase Phi_T is Gaussian and every realization gives a
product unitary. The exact fixed-time channel is exp(v(T) D[F]) where
v(T)=Var(Phi_T)=2 sigma2 tau [T-tau(1-exp(-T/tau))].

This validates a colored finite-correlation, non-semigroup classical channel.
It does NOT assert information-backflow non-Markovianity and does not test RCG-002.
"""
import argparse,json,math,sys
from pathlib import Path
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I2,I4,RHO0,axis,op,td,neg,exp_super,choi
from iter018a_correlated_classical_noise_validation import d_super,evolve_super,gaussian_mixture

TH={'tp':1e-10,'choi_floor':-1e-8,'state_floor':-1e-8,'trace':1e-10,'quadrature_td':1e-10,'factorization':1e-12,'negativity':1e-10,'covariance_floor':-1e-10,'semigroup_defect_fraction':0.02}

def variance(T,sigma2,tau):
    return 2.0*sigma2*tau*(T-tau*(1.0-math.exp(-T/tau)))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--shard',type=int,choices=range(12),required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); s=a.shard; rng=np.random.default_rng(38000+s)
    A=op(axis(rng.uniform(-math.pi,math.pi),rng.uniform(0.15,math.pi-0.15))); B=op(axis(rng.uniform(-math.pi,math.pi),rng.uniform(0.15,math.pi-0.15)))
    cA=float(rng.uniform(-1.8,1.8)); cB=float(rng.uniform(-1.8,1.8)); sigma2=float(10**rng.uniform(-2.0,0.2)); T=float(rng.uniform(0.5,1.5)); tau=float(rng.uniform(0.25,1.5))
    v=variance(T,sigma2,tau); v2=variance(2*T,sigma2,tau); defect=float(abs(v2-2*v)/v2)
    F=cA*np.kron(A,I2)+cB*np.kron(I2,B); L_eff=v*d_super(F); E=exp_super(L_eff); rho=evolve_super(E)
    trrow=I4.reshape(-1,order='F').conj(); tp=float(np.linalg.norm(trrow@L_eff)); ce=float(np.min(np.linalg.eigvalsh(choi(E)))); sm=float(np.min(np.linalg.eigvalsh(rho))); te=float(abs(np.trace(rho)-1.0))
    mix,ferr=gaussian_mixture(A,B,cA,cB,v,80); qgap=float(td(rho,mix)); negativity=float(neg(rho))
    ts=np.linspace(0,T,9); C=sigma2*np.exp(-np.abs(ts[:,None]-ts[None,:])/tau); cmin=float(np.min(np.linalg.eigvalsh(C)))
    support=bool(tp<TH['tp'] and ce>TH['choi_floor'] and sm>TH['state_floor'] and te<TH['trace'] and qgap<TH['quadrature_td'] and ferr<TH['factorization'] and negativity<TH['negativity'] and cmin>TH['covariance_floor'] and defect>TH['semigroup_defect_fraction'])
    vals=[tp,ce,sm,te,qgap,ferr,negativity,cmin,defect,v,v2]; valid=bool(np.all(np.isfinite(vals)))
    out={'iteration':'Iter020A','gate':'G38-P','shard':s,'parameters':{'cA':cA,'cB':cB,'sigma2':sigma2,'tau':tau,'T':T,'phase_variance':v},'result':{'tp_residual':tp,'choi_min_eig':ce,'state_min_eig':sm,'trace_error':te,'random_unitary_quadrature_td':qgap,'product_unitary_factorization_error':ferr,'output_negativity':negativity,'ou_covariance_min_eig':cmin,'semigroup_defect_fraction':defect,'scientific_support':support},'structural_valid':valid,'frozen_thresholds':TH,'interpretation':'Implementation validation for finite-correlation classical Gaussian colored noise only; not an RCG-002 test and not an information-backflow non-Markovian claim.','scope_lock':'Stationary OU scalar classical noise coupled through one fixed sum of local Pauli-axis observables; exact fixed-time convex mixture of product unitaries.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)
if __name__=='__main__': main()
