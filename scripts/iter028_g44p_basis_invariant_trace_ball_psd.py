#!/usr/bin/env python3
"""Iter028 / G44-P: response-blind validation of a basis-invariant bounded
real-PSD family C=A^2 with A=A^T and ||A||_F<=2.

No RCG-002 target/result is used.
"""
import argparse, json, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter025a_g42j_full_psd_kossakowski_identifiability import generator_from_C
from iter027_g43a_heldout_multichart_basis_coverage import panel_objects

RADIUS=2.0
RANK_TOL=1e-10
C_FLOOR=-1e-10
REC_TOL=1e-10
COV_TOL=1e-10
NORM_TOL=1e-12
OLD_BOX_FROB2=6*(0.60**2)+15*(0.30**2)  # 3.51

# New response-blind local basis rotations, disjoint from G42-BC and G43-A.
PANELS=(
    ((2.0,-1.0,1.0),0.58,(1.0,3.0,-2.0),-0.81),
    ((1.0,4.0,2.0),-1.09,(-2.0,3.0,1.0),0.93),
    ((3.0,-2.0,4.0),1.28,(4.0,1.0,-3.0),-1.34),
    ((5.0,2.0,-1.0),-1.47,(2.0,-4.0,3.0),1.16),
)


def hidden_C(rank):
    rng=np.random.default_rng(144000+rank)
    M=rng.normal(size=(6,6))
    Q,_=np.linalg.qr(M)
    if np.linalg.det(Q)<0:
        Q[:,0]*=-1
    amps=np.array([0.42+0.055*j+0.010*rank for j in range(rank)],float)
    C=Q[:,:rank]@np.diag(amps**2)@Q[:,:rank].T
    return (C+C.T)/2


def symmetric_sqrt(C):
    w,V=np.linalg.eigh((C+C.T)/2)
    wp=np.clip(w,0.0,None)
    A=(V*np.sqrt(wp))@V.T
    return (A+A.T)/2,w


def pack_sym(A):
    return np.asarray([A[i,j] for i in range(6) for j in range(i+1)],float)


def representation_diag(C):
    A,eig=symmetric_sqrt(C)
    rec=float(np.linalg.norm(A@A-C)/max(np.linalg.norm(C),1e-15))
    fn=float(np.linalg.norm(A,'fro'))
    q=pack_sym(A)
    return {
        'reconstruction_relative_error':rec,
        'sqrt_frobenius_norm':fn,
        'max_abs_symmetric_coordinate':float(np.max(np.abs(q))),
        'inside_trace_ball':bool(fn<=RADIUS+NORM_TOL),
        'min_C_eigenvalue':float(np.min(eig)),
        'rank':int(np.sum(eig>RANK_TOL)),
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--rank',type=int,choices=range(1,7),required=True)
    ap.add_argument('--panel',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()

    C=hidden_C(a.rank)
    U,O=panel_objects(PANELS[a.panel])
    Cp=O@C@O.T; Cp=(Cp+Cp.T)/2
    d0=representation_diag(C); dp=representation_diag(Cp)

    L0=generator_from_C(C); Lp=generator_from_C(Cp)
    S=np.kron(U.conj(),U)
    Lin=S@L0@S.conj().T
    cov=float(np.linalg.norm(Lp-Lin)/max(np.linalg.norm(Lp),1e-15))

    old_box_nested=bool(OLD_BOX_FROB2 < RADIUS**2)
    vals=[d0['reconstruction_relative_error'],d0['sqrt_frobenius_norm'],d0['max_abs_symmetric_coordinate'],d0['min_C_eigenvalue'],
          dp['reconstruction_relative_error'],dp['sqrt_frobenius_norm'],dp['max_abs_symmetric_coordinate'],dp['min_C_eigenvalue'],cov]
    structural=bool(np.all(np.isfinite(vals)))
    support=bool(
        structural and old_box_nested and
        d0['rank']==a.rank and dp['rank']==a.rank and
        d0['min_C_eigenvalue']>=C_FLOOR and dp['min_C_eigenvalue']>=C_FLOOR and
        d0['reconstruction_relative_error']<REC_TOL and dp['reconstruction_relative_error']<REC_TOL and
        d0['inside_trace_ball'] and dp['inside_trace_ball'] and
        cov<COV_TOL
    )

    out={
        'iteration':'Iter028','gate':'G44-P','rank':a.rank,'panel':a.panel,
        'original':d0,'rotated':dp,
        'basis_covariance':{'relative_generator_error':cov,'support':bool(cov<COV_TOL)},
        'analytic_nesting':{'old_G42_box_max_sqrt_trace':float(np.sqrt(OLD_BOX_FROB2)),'trace_ball_radius':RADIUS,'old_box_fully_nested':old_box_nested},
        'structural_valid':structural,'scientific_support':support,
        'classification':'BASIS_INVARIANT_TRACE_BALL_PSD_REPRESENTATION_LANE_PASS' if support else 'TRACE_BALL_REPRESENTATION_OR_COVARIANCE_LANE_FAIL',
        'frozen':{'radius':RADIUS,'trace_C_max':RADIUS**2,'rank_threshold':RANK_TOL,'kossakowski_floor':C_FLOOR,'reconstruction_tolerance':REC_TOL,'generator_covariance_tolerance':COV_TOL,'RCG002_target_used':False},
        'scope_lock':'Basis-invariant bounded real-PSD trace-ball tr(C)<=4 represented as C=A^2, A symmetric; response-blind representation/covariance pre-gate only.',
        'interpretation':'Implementation/coverage only. PASS cannot establish comparator separation or raise programme readiness.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)

if __name__=='__main__': main()
