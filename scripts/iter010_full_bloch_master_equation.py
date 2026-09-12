#!/usr/bin/env python3
"""Iter010 / G28: full-Bloch-sphere local-axis measurement-feedback audit.

G27 showed that restricting the Markovian classical-channel comparator to ZZ is
basis-sensitive: X-Z rotations improved the trace-distance fit in every lane.
G28 removes the remaining planar restriction while preserving the same physical
trade-off Gamma_A Gamma_B = chi^2.

The axis set contains the entire 11-point G27 X-Z grid plus Y poles and the 12
icosahedral directions, so the previous family is exactly nested in this one.
Scope lock: finite two-qubit, Markovian, single-axis-per-site comparator family;
this is not a theorem about all semiclassical-gravity channels.
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

def neg(r):
    p=r.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    e=np.linalg.eigvalsh((p+p.conj().T)/2)
    return float(np.sum(np.abs(e[e<0])))

def td(a,b):
    return float(.5*np.sum(np.linalg.svd(a-b,compute_uv=False)))

def target(th):
    U=math.cos(th)*I4-1j*math.sin(th)*ZZ
    return U@RHO0@U.conj().T

def op(v):
    v=np.asarray(v,dtype=float); v=v/np.linalg.norm(v)
    return v[0]*X+v[1]*Y+v[2]*Z

def axes():
    out=[]
    # Exact G27 11-point X-Z family.
    for k,b in enumerate(np.linspace(-math.pi/2,math.pi/2,11)):
        out.append((f'xz{k:02d}',np.array([math.sin(float(b)),0.0,math.cos(float(b))]),True))
    out += [('y+',np.array([0.,1.,0.]),False),('y-',np.array([0.,-1.,0.]),False)]
    phi=(1+math.sqrt(5))/2
    raw=[]
    for a in (-1.,1.):
        for b in (-phi,phi): raw.append((0.,a,b))
    for a in (-1.,1.):
        for b in (-phi,phi): raw.append((a,b,0.))
    for a in (-phi,phi):
        for b in (-1.,1.): raw.append((a,0.,b))
    for i,v in enumerate(raw): out.append((f'ico{i:02d}',np.array(v,dtype=float),False))
    return out

def Lgen(chi,A,B,ga,gb):
    H=chi*np.kron(A,B)
    L=-1j*(np.kron(I4,H)-np.kron(H.T,I4))
    for rate,Q in ((ga,np.kron(A,I2)),(gb,np.kron(I2,B))):
        Q2=Q.conj().T@Q
        L += rate*(np.kron(Q.conj(),Q)-.5*np.kron(I4,Q2)-.5*np.kron(Q2.T,I4))
    return L

def evolve(L):
    w,v=np.linalg.eig(L)
    E=v@np.diag(np.exp(w))@np.linalg.inv(v)
    r=(E@RHO0.reshape(-1,order='F')).reshape(4,4,order='F')
    r=(r+r.conj().T)/2
    return r/np.trace(r)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--scale',type=float,required=True)
    ap.add_argument('--theta',type=float,required=True)
    ap.add_argument('--tag',required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    th=a.scale*a.theta; chi=th; tar=target(th); tneg=neg(tar)
    avec=axes(); asym=np.linspace(-2,2,17)
    best=None; best_xz=None; baseline=None; n=0; min_eig=1.0
    for la,va,xa in avec:
        A=op(va)
        for lb,vb,xb in avec:
            B=op(vb)
            for aa in asym:
                ga=abs(chi)*math.exp(float(aa)); gb=abs(chi)*math.exp(float(-aa))
                r=evolve(Lgen(chi,A,B,ga,gb)); d=td(r,tar)
                ev=float(np.min(np.linalg.eigvalsh(r))); min_eig=min(min_eig,ev); n+=1
                rec={'axisA':la,'axisB':lb,'a':float(aa),'ga':ga,'gb':gb,'td':d,'neg':neg(r),'eigmin':ev,
                     'vecA':(va/np.linalg.norm(va)).tolist(),'vecB':(vb/np.linalg.norm(vb)).tolist()}
                if best is None or d<best['td']: best=rec
                if xa and xb and (best_xz is None or d<best_xz['td']): best_xz=rec
                if la=='xz05' and lb=='xz05' and abs(aa)<1e-12: baseline=rec
    structural={
        'target_entangles':tneg>1e-6,
        'g27_family_nested':best_xz is not None,
        'zz_baseline_contained':baseline is not None,
        'states_physical':min_eig>-1e-8,
        'tradeoff_exact':abs(best['ga']*best['gb']-chi*chi)<1e-9,
        'finite_search':n==len(avec)*len(avec)*len(asym),
        'full_axis_count':len(avec)==25,
    }
    improve_xz=(best_xz['td']-best['td'])/best_xz['td']
    improve_zz=(baseline['td']-best['td'])/baseline['td']
    sci={
        'nonzero_full_sphere_gap':best['td']>1e-4,
        'off_plane_improves_xz_by_1pct':best['td']<0.99*best_xz['td'],
        'full_sphere_beats_zz_by_1pct':best['td']<0.99*baseline['td'],
    }
    out={'iteration':'Iter010','gate':'G28','tag':a.tag,'scale':a.scale,'theta_base':a.theta,'theta':th,
         'target_negativity':tneg,'n_axes':len(avec),'n_candidates':n,'baseline_ZZ':baseline,'best_XZ_nested':best_xz,
         'best_full_sphere':best,'improvement_vs_XZ':improve_xz,'improvement_vs_ZZ':improve_zz,
         'structural_gates':structural,'scientific_support':sci,'pass':all(structural.values()),
         'scope_lock':'Finite two-qubit Markovian single-axis-per-site measurement-feedback family with GA*GB=chi^2.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not out['pass']: raise SystemExit(2)

if __name__=='__main__': main()
