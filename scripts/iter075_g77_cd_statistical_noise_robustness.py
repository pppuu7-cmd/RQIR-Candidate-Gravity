import argparse, json
import numpy as np

PRIMARY=[1/3,2/3,5/4,7/3]
HELDOUT=[[1/5,3/5,4/3,9/4],[2/7,5/6,7/5,11/3]]
ALPHAS=[1.0,1e-1,1e-2,1e-3]
TOL=1e-12

def design(zs,a,aq=True,ad=True):
    rows=[[-z,0,z,0] for z in zs]
    rows.append([0,1,0,1])
    if aq: rows.append([0,0,a,0])
    if ad: rows.append([0,0,0,a])
    return np.array(rows,dtype=float)

def rank(M): return int(np.linalg.matrix_rank(M,tol=TOL))
def cov(M,sigma): return (sigma*sigma)*np.linalg.inv(M.T@M)
def inc(xs): return all(xs[i+1] > xs[i] for i in range(len(xs)-1))

def lane_A():
    cases=[]; valid=True
    for pi,zs in enumerate([PRIMARY]+HELDOUT):
        cvars=[]; dvars=[]; maxvars=[]
        for a in ALPHAS:
            M=design(zs,a); C=cov(M,1.0)
            item={'panel':pi,'a':a,'rank':rank(M),'c_var':float(C[0,0]),'d_var':float(C[1,1]),'max_var':float(np.max(np.diag(C)))}
            cases.append(item); cvars.append(item['c_var']); dvars.append(item['d_var']); maxvars.append(item['max_var'])
            valid &= item['rank']==4
        valid &= inc(cvars) and inc(dvars) and inc(maxvars)
        valid &= rank(design(zs,0.0))==2
    return 'ANALYTIC_ESTIMATOR_VARIANCE_WEAK_ANCHOR_AMPLIFICATION_SCOPED',{'cases':cases},bool(valid)

def lane_B():
    sigmas=[1e-3,1e-2,1e-1]; cases=[]; valid=True
    for a in [1.0,1e-2,1e-4]:
        M=design(PRIMARY,a); base=np.linalg.inv(M.T@M)
        for s in sigmas:
            C=cov(M,s); rel=float(np.max(np.abs(C/(s*s)-base))/max(np.max(np.abs(base)),1e-300))
            cases.append({'a':a,'sigma':s,'sigma2_scaling_relerr':rel})
            valid &= rel<1e-11
    return 'GAUSSIAN_COVARIANCE_SIGMA2_SCALING_SCOPED',{'cases':cases},bool(valid)

def lane_C():
    rng=np.random.default_rng(76077); sigma=0.02; n=12000; cases=[]; valid=True
    for a in [1.0,1e-1,1e-2]:
        M=design(PRIMARY,a); pinv=np.linalg.inv(M.T@M)@M.T
        noise=rng.normal(0.0,sigma,size=(n,M.shape[0]))
        bhat=noise@pinv.T
        emp=np.cov(bhat,rowvar=False,ddof=1); ana=cov(M,sigma)
        diag_rel=np.abs(np.diag(emp)-np.diag(ana))/np.maximum(np.abs(np.diag(ana)),1e-300)
        mx=float(np.max(diag_rel))
        cases.append({'a':a,'draws':n,'max_diag_relerr':mx})
        valid &= mx<0.08
    return 'FIXED_SEED_MONTE_CARLO_COVARIANCE_REPLICATION_SCOPED',{'seed':76077,'cases':cases},bool(valid)

def orthogonals():
    I=np.eye(4)
    return [('I',I),('swap_C_N1',I[:,[2,1,0,3]]),('swap_D_N3',I[:,[0,3,2,1]]),('flip_C',np.diag([-1,1,1,1])),('flip_D',np.diag([1,-1,1,1]))]

def lane_D():
    M=design(PRIMARY,1e-3); base=np.linalg.eigvalsh(cov(M,1.0)); errs={}; valid=True
    for name,R in orthogonals():
        Mr=M@R
        Cr=cov(Mr,1.0)
        eig=np.linalg.eigvalsh(Cr)
        rel=float(np.max(np.abs(eig-base)/np.maximum(np.abs(base),1e-300)))
        errs[name]=rel; valid &= rel<1e-8
    qrank=rank(design(PRIMARY,1.0,aq=True,ad=False)); drank=rank(design(PRIMARY,1.0,aq=False,ad=True))
    valid &= qrank==3 and drank==3
    return 'ORTHOGONAL_PARAMETER_COVARIANCE_AND_ONE_SIDED_CONTROL_SCOPED',{'eigenvalue_relerrs':errs,'aq_only_rank':qrank,'ad_only_rank':drank},bool(valid)

ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=list('ABCD')); ap.add_argument('--out',required=True); a=ap.parse_args()
fn={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}[a.lane]
classification,checks,valid=fn()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True,allow_nan=False)
if not valid: raise SystemExit(2)
