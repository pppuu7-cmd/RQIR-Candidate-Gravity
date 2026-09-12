#!/usr/bin/env python3
"""Iter041/G49-C: response-blind direct-PSD calibration, frozen by preregistration."""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
from scipy.stats import qmc,norm

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I4,td,choi
from iter022b_g40c_rtn_optimizer_calibration import PROBES
from iter024a_g41p_high_rank_classical_kossakowski import map_apply
from iter025a_g42j_full_psd_kossakowski_identifiability import TIMES,generator_from_C
from iter034_g46c_extended_trace_ball_calibration import weighted_pack,weighted_unpack

METHODS=('sobol_lsq','lhs_lsq')
BOX=8.0; N_START=32; N_REFINE=6; MAX_NFEV=1200
TARGET_NORMS=(0.5,1.0,2.0,3.0,4.0,5.0)
GAP_TOL=0.002; C_REL_TOL=0.02; RANK_EIG_TOL=1e-5
LO=-BOX*np.ones(21); HI=BOX*np.ones(21)

def cmat(w):
    A=weighted_unpack(np.asarray(w,float)); return A@A

def traj(w):
    G=generator_from_C(cmat(w)); out=[]
    for t in TIMES:
        E=expm(G*float(t)); out.append([map_apply(E,rho) for rho in PROBES])
    return out

def residual(w,target):
    pred=traj(w); arr=[]
    for aa,bb in zip(pred,target):
        for x,y in zip(aa,bb):
            d=x-y; arr.extend(d.real.reshape(-1)); arr.extend(d.imag.reshape(-1))
    return np.asarray(arr,float)

def hidden_A(rank):
    rng=np.random.default_rng(241000+rank)
    M=rng.normal(size=(6,rank)); Q,_=np.linalg.qr(M); Q=Q[:,:rank]
    ev=np.linspace(1.0,1.0+0.2*(rank-1),rank)
    ev=ev/np.linalg.norm(ev)*TARGET_NORMS[rank-1]
    A=Q@np.diag(ev)@Q.T; return (A+A.T)/2

def starts(method,rank):
    seed=242000+10*rank+(0 if method=='sobol_lsq' else 3)
    if method=='sobol_lsq': u=qmc.Sobol(d=21,scramble=True,seed=seed).random_base2(5)
    else: u=qmc.LatinHypercube(d=21,seed=seed).random(N_START)
    # Response-blind broad starts concentrated well inside numerical box.
    g=norm.ppf(np.clip(u,1e-12,1-1e-12));
    scale=1.5/np.maximum(np.linalg.norm(g,axis=1,keepdims=True),1e-15)
    return g*scale

def physicality(C):
    ce=np.linalg.eigvalsh((C+C.T)/2); G=generator_from_C(C)
    trrow=I4.reshape(-1,order='F').conj(); tp=[]; cp=[]; se=[]; te=[]
    for t in TIMES:
        E=expm(G*float(t)); tp.append(float(np.linalg.norm(trrow@E-trrow))); cp.append(float(np.min(np.linalg.eigvalsh(choi(E)))))
        for rho in PROBES:
            out=map_apply(E,rho); se.append(float(np.min(np.linalg.eigvalsh((out+out.conj().T)/2)))); te.append(float(abs(np.trace(out)-1)))
    return {'min_kossakowski_eigenvalue':float(ce.min()),'trace_C':float(np.trace(C).real),'max_tp_residual':max(tp),'min_choi_eigenvalue':min(cp),'min_output_state_eigenvalue':min(se),'max_trace_error':max(te)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--rank',type=int,choices=range(1,7),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    Ah=hidden_A(a.rank); wh=weighted_pack(Ah); Ch=Ah@Ah; target=traj(wh)
    he=np.linalg.eigvalsh((Ch+Ch.T)/2); hidden_rank=int(np.sum(he>RANK_EIG_TOL))
    scored=[]
    for w0 in starts(a.method,a.rank):
        rr=residual(w0,target); scored.append((float(rr@rr),w0))
    scored.sort(key=lambda x:x[0]); cands=[]
    for _,w0 in scored[:N_REFINE]:
        fit=least_squares(lambda w:residual(w,target),w0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        C=cmat(fit.x); pred=traj(fit.x); gaps=[td(x,y) for aa,bb in zip(pred,target) for x,y in zip(aa,bb)]
        eig=np.linalg.eigvalsh((C+C.T)/2); rel=float(np.linalg.norm(C-Ch)/max(np.linalg.norm(Ch),1e-15)); rank=int(np.sum(eig>RANK_EIG_TOL)); phy=physicality(C)
        cands.append({'gap':float(max(gaps)),'residual_norm':float(np.linalg.norm(residual(fit.x,target))),'relative_kossakowski_error':rel,'recovered_effective_rank':rank,'w':fit.x.tolist(),'box_fraction':float(np.max(np.abs(fit.x))/BOX),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success),'physicality':phy})
    best=min(cands,key=lambda c:(c['gap'],c['relative_kossakowski_error'],c['residual_norm']))
    p=best['physicality']; vals=[*he,*wh]+[v for c in cands for v in (c['gap'],c['residual_norm'],c['relative_kossakowski_error'],c['box_fraction'],*c['w'])]
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)) and hidden_rank==a.rank)
    support=bool(structural and best['gap']<GAP_TOL and best['relative_kossakowski_error']<C_REL_TOL and best['recovered_effective_rank']==a.rank and best['box_fraction']<0.80 and p['min_kossakowski_eigenvalue']>=-1e-10 and p['max_tp_residual']<1e-10 and p['min_choi_eigenvalue']>-1e-8 and p['min_output_state_eigenvalue']>-1e-8 and p['max_trace_error']<1e-10)
    out={'iteration':'Iter041','gate':'G49-C','method':a.method,'rank':a.rank,'hidden':{'effective_rank':hidden_rank,'sqrt_trace_C':float(np.sqrt(np.trace(Ch))),'trace_C':float(np.trace(Ch)),'max_abs_weighted_coordinate':float(np.max(np.abs(wh)))},'best_candidate':best,'n_refined_candidates':len(cands),'structural_valid':structural,'scientific_support':support,'classification':'CAPFREE_DIRECT_PSD_CALIBRATION_LANE_PASS' if support else 'CAPFREE_DIRECT_PSD_CALIBRATION_LANE_NOT_ESTABLISHED','frozen':{'family':'C=A^2, A real symmetric, direct weighted physical-scale coordinates, no trace cap','numerical_box':BOX,'box_inactivity_fraction':0.80,'target_norms':list(TARGET_NORMS),'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'gap_tolerance':GAP_TOL,'relative_kossakowski_tolerance':C_REL_TOL,'rank_eigenvalue_threshold':RANK_EIG_TOL,'RCG002_target_used':False},'scope_lock':'Response-blind numerical optimizer calibration only. No unbounded-PSD theorem.','interpretation':'PASS only authorizes later prospectively frozen RCG-002 transport in this direct-PSD parameterization.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
