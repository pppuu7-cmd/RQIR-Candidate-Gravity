#!/usr/bin/env python3
"""Iter014B / G32-J: local identifiability diagnostics on hidden positive controls.

Frozen before G32 results are consumed. This workflow never evaluates RCG-002.
It estimates the local Jacobian of the final density matrix with respect to the
11 K=2 comparator coordinates at the exact hidden in-family source, checks
finite-difference convergence, and reports SVD rank/conditioning. Rank is a
diagnostic, not a physics PASS/FAIL criterion.
"""
import argparse, json, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES, bounds, decode, multi_L
from iter014_optimizer_calibration_diagnostic import source_params
from iter011_robustness_suite import evolve

REL_H1=1e-5
REL_H2=5e-6
JAC_CONVERGENCE_TOL=2e-3
RANK_REL_TOL=1e-8


def obsvec(rho):
    # Redundant real embedding is intentional: rank is unchanged while avoiding
    # a convention-dependent choice of Hermitian coordinates.
    z=np.asarray(rho,dtype=complex).reshape(-1)
    return np.concatenate([z.real,z.imag])


def jacobian(theta,x,relh):
    b=bounds(2)
    cols=[]
    for j,(lo,hi) in enumerate(b):
        h=relh*(hi-lo)
        xp=x.copy(); xm=x.copy()
        xp[j]=min(hi-1e-10,x[j]+h)
        xm[j]=max(lo+1e-10,x[j]-h)
        denom=xp[j]-xm[j]
        yp=obsvec(evolve(multi_L(theta,decode(xp,2))))
        ym=obsvec(evolve(multi_L(theta,decode(xm,2))))
        cols.append((yp-ym)/denom)
    return np.stack(cols,axis=1)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--shard',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    scale,theta0=CASES[a.shard]
    theta=scale*theta0
    x=source_params(a.shard)
    J1=jacobian(theta,x,REL_H1)
    J2=jacobian(theta,x,REL_H2)
    rel=float(np.linalg.norm(J1-J2)/max(np.linalg.norm(J2),1e-30))
    s=np.linalg.svd(J2,compute_uv=False)
    cutoff=float(RANK_REL_TOL*s[0]) if s.size else 0.0
    rank=int(np.sum(s>cutoff))
    nonzero=s[s>cutoff]
    cond=float(nonzero[0]/nonzero[-1]) if nonzero.size else float('inf')
    support=bool(np.all(np.isfinite(J1)) and np.all(np.isfinite(J2)) and rel<JAC_CONVERGENCE_TOL)
    out={
      'iteration':'Iter014B','gate':'G32-J','shard':a.shard,'theta':theta,
      'result':{
        'jacobian_shape':list(J2.shape),
        'relative_two_step_jacobian_difference':rel,
        'singular_values':s.tolist(),
        'rank_relative_cutoff':cutoff,
        'effective_rank':rank,
        'parameter_dimension':int(J2.shape[1]),
        'condition_number_on_retained_subspace':cond,
        'scientific_support':support,
        'interpretation':'Derivative convergence is the validity gate. Effective rank/conditioning are diagnostics of local identifiability, not physics evidence.'
      },
      'structural_valid':bool(support),
      'frozen_thresholds':{
        'relative_fd_steps':[REL_H1,REL_H2],
        'jacobian_convergence':JAC_CONVERGENCE_TOL,
        'svd_rank_relative_cutoff':RANK_REL_TOL
      },
      'scope_lock':'Hidden K=2 positive controls only; no RCG-002 target.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if not support: raise SystemExit(2)

if __name__=='__main__': main()
