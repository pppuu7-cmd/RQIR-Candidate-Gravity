#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I2,I4,Z,td
from iter013_global_search_calibration import CASES
from iter022a_g40p_rtn_information_backflow_validation import pair_states
from iter022b_g40c_rtn_optimizer_calibration import METHODS,TIMES,PROBES,BLP_TIMES,LO,HI,N_REFINE,MAX_NFEV,block,reduced_map,apply,design,residual_u,metric_u

H=np.array([[1,1],[1,-1]],complex)/np.sqrt(2)
S=np.array([[1,0],[0,1j]],complex)
WITNESSES={'I':I2,'H':H,'SH':S@H,'HS':H@S}


def target_traj(theta):
    ZZ=np.kron(Z,Z); out=[]
    for t in TIMES:
        a=float(theta*t); U=np.cos(a)*I4-1j*np.sin(a)*ZZ
        out.append([U@rho@U.conj().T for rho in PROBES])
    return out


def blp_for_pair(u,rhoa,rhob):
    p=LO+np.clip(np.asarray(u,float),0,1)*(HI-LO); G=block(p); ds=[]
    for t in BLP_TIMES:
        E=reduced_map(G,float(t)); ds.append(td(apply(E,rhoa),apply(E,rhob)))
    ds=np.asarray(ds,float)
    return float(np.sum(np.clip(np.diff(ds),0,None)))


def panel_blp(u):
    a,b=pair_states(); vals={}
    for name,U in WITNESSES.items():
        K=np.kron(U,U); aa=K@a@K.conj().T; bb=K@b@K.conj().T
        vals[name]=blp_for_pair(u,aa,bb)
    best=max(vals,key=vals.get)
    return vals,best,float(vals[best])


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    scale,t0=CASES[a.shard]; theta=float(scale*t0); tar=target_traj(theta)
    scored=[]
    for u in design(a.method,a.shard):
        rr=residual_u(u,tar); scored.append((float(np.dot(rr,rr)),np.asarray(u,float)))
    scored.sort(key=lambda z:z[0]); rows=[]
    for _,u0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual_u(z,tar),u0,bounds=(0,1),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn=metric_u(fit.x,tar); vals,best,bmax=panel_blp(fit.x); orig=float(vals['I'])
        rows.append({'gap':float(gap),'residual_norm':float(rn),'original_BLP':orig,'panel_BLP':vals,'panel_max_BLP':bmax,'panel_argmax':best,'original_admissible':bool(orig>0.02),'panel_admissible':bool(bmax>0.02),'escape':bool(orig<=0.02 and bmax>0.02),'nfev':int(fit.nfev)})
    finite=all(np.all(np.isfinite([r['gap'],r['residual_norm'],r['original_BLP'],r['panel_max_BLP']])) for r in rows)
    admiss=[r for r in rows if r['panel_admissible']]; best=min(admiss,key=lambda r:(r['gap'],r['residual_norm'])) if admiss else None
    out={'iteration':'Iter023A','gate':'G40-D','method':a.method,'shard':a.shard,'theta':theta,'structural_valid':bool(finite),'classification':'FIXED_WITNESS_FRAGILE_ON_PANEL' if any(r['escape'] for r in rows) else 'NO_PANEL_ESCAPE_FOUND','n_refined':len(rows),'n_escape':sum(int(r['escape']) for r in rows),'best_panel_admissible':best,'candidates':rows,'frozen':{'panel':['I','H','SH','HS'],'BLP_threshold':0.02,'same_family_bounds_target_optimizer_as_G40A':True},'interpretation':'Diagnostic only; cannot retroactively promote G40-A or support all-BLP/all-classical claims.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not finite: raise SystemExit(2)
if __name__=='__main__': main()
