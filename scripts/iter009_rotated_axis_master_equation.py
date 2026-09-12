#!/usr/bin/env python3
"""Iter009 / G27: rotated-axis measurement-feedback master-equation audit.

Extends Iter008 by allowing the two local measured/feedback observables to rotate
independently in the X-Z plane:
 A(betaA)=cos(betaA) Z + sin(betaA) X,
 B(betaB)=cos(betaB) Z + sin(betaB) X.
The coherent comparator Hamiltonian is chi A⊗B and the local dephasing rates obey
GA*GB=chi^2.  The old ZZ family is exactly contained at betaA=betaB=0.

Scope lock: this is a finite-dimensional X-Z-plane Markovian classical-channel
surrogate audit, not a no-go theorem for arbitrary semiclassical gravity.
"""
import argparse,json,math
from pathlib import Path
import numpy as np
I2=np.eye(2,dtype=complex); X=np.array([[0,1],[1,0]],complex); Z=np.array([[1,0],[0,-1]],complex)
ZZ=np.kron(Z,Z); PLUS=np.array([1,1],complex)/math.sqrt(2); PSI0=np.kron(PLUS,PLUS); RHO0=np.outer(PSI0,PSI0.conj())

def neg(r):
 p=r.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4); e=np.linalg.eigvalsh((p+p.conj().T)/2); return float(np.sum(np.abs(e[e<0])))
def td(a,b): return float(.5*np.sum(np.linalg.svd(a-b,compute_uv=False)))
def target(th):
 U=math.cos(th)*np.eye(4,dtype=complex)-1j*math.sin(th)*ZZ; return U@RHO0@U.conj().T
def axis(b): return math.cos(b)*Z+math.sin(b)*X
def Lgen(chi,A,B,ga,gb):
 H=chi*np.kron(A,B); I4=np.eye(4,dtype=complex); L=-1j*(np.kron(I4,H)-np.kron(H.T,I4))
 for rate,Q in ((ga,np.kron(A,I2)),(gb,np.kron(I2,B))):
  Q2=Q.conj().T@Q; L+=rate*(np.kron(Q.conj(),Q)-.5*np.kron(I4,Q2)-.5*np.kron(Q2.T,I4))
 return L
def evolve(L):
 w,v=np.linalg.eig(L); E=v@np.diag(np.exp(w))@np.linalg.inv(v); r=(E@RHO0.reshape(-1,order='F')).reshape(4,4,order='F'); r=(r+r.conj().T)/2; return r/np.trace(r)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--scale',type=float,required=True); ap.add_argument('--theta',type=float,required=True); ap.add_argument('--tag',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
 th=a.scale*a.theta; chi=th; tar=target(th); tneg=neg(tar)
 betas=np.linspace(-math.pi/2,math.pi/2,11); asym=np.linspace(-2,2,17); best=None; baseline=None; n=0; min_eig=1
 for ba in betas:
  A=axis(float(ba))
  for bb in betas:
   B=axis(float(bb))
   for aa in asym:
    ga=abs(chi)*math.exp(float(aa)); gb=abs(chi)*math.exp(float(-aa)); r=evolve(Lgen(chi,A,B,ga,gb)); d=td(r,tar); ev=float(np.min(np.linalg.eigvalsh(r))); n+=1; min_eig=min(min_eig,ev)
    rec={'betaA':float(ba),'betaB':float(bb),'a':float(aa),'ga':ga,'gb':gb,'td':d,'neg':neg(r),'eigmin':ev}
    if best is None or d<best['td']: best=rec
    if abs(ba)<1e-12 and abs(bb)<1e-12 and abs(aa)<1e-12: baseline=rec
 structural={'target_entangles':tneg>1e-6,'baseline_contained':baseline is not None,'states_physical':min_eig>-1e-8,'tradeoff_exact':abs(best['ga']*best['gb']-chi*chi)<1e-9,'finite_search':n==11*11*17}
 sci={'nonzero_global_gap':best['td']>1e-4,'rotations_do_not_beat_ZZ_by_1pct':best['td']>=0.99*baseline['td'],'best_near_Z_axes':abs(best['betaA'])<=math.pi/10+1e-12 and abs(best['betaB'])<=math.pi/10+1e-12}
 out={'iteration':'Iter009','gate':'G27','tag':a.tag,'scale':a.scale,'theta_base':a.theta,'theta':th,'target_negativity':tneg,'n_candidates':n,'baseline_ZZ':baseline,'best_rotated':best,'improvement_fraction':(baseline['td']-best['td'])/baseline['td'],'structural_gates':structural,'scientific_support':sci,'pass':all(structural.values()),'scope_lock':'X-Z-plane local-axis Markovian measurement-feedback surrogate with GA*GB=chi^2; not all semiclassical gravity.'}
 Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2));
 if not out['pass']: raise SystemExit(2)
if __name__=='__main__': main()
