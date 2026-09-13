import argparse, json
import numpy as np

ZS=[1/3,2/3,5/4,7/3]
ALPHAS=[1.0,1e-2,1e-4]
TOL=1e-12

def design(a,aq=True,ad=True):
    rows=[[-z,0,z,0] for z in ZS]+[[0,1,0,1]]
    if aq: rows.append([0,0,a,0])
    if ad: rows.append([0,0,0,a])
    return np.array(rows,dtype=float)
def rank(M): return int(np.linalg.matrix_rank(M,tol=TOL))
def covs():
    n=7
    I=np.eye(n)
    H=np.diag([1,2,4,3,1.5,0.8,1.2])
    C=(1-0.25)*I+0.25*np.ones((n,n))
    Q=np.eye(n); Q[:4,:4]=(1-0.55)*np.eye(4)+0.55*np.ones((4,4))
    return [('identity',I),('heteroscedastic',H),('compound_rho025',C),('quadratic_block_rho055',Q)]
def fisher(M,S): return M.T@np.linalg.solve(S,M)
def finfo(M,S):
    F=fisher(M,S); e=np.linalg.eigvalsh(F); r=int(np.sum(e>TOL)); V=np.linalg.inv(F) if r==4 else None
    return F,e,r,V
def inc(xs): return all(xs[i+1]>xs[i] for i in range(len(xs)-1))

def lane_A():
    cases=[]; valid=True
    for name,S in covs():
        cvars=[]; dvars=[]
        for a in ALPHAS:
            M=design(a); F,e,r,V=finfo(M,S)
            cv=float(V[0,0]); dv=float(V[1,1]); cases.append({'covariance':name,'a':a,'rank':r,'min_fisher_eig':float(e[0]),'c_var':cv,'d_var':dv})
            cvars.append(cv); dvars.append(dv); valid &= r==4 and e[0]>0
        valid &= inc(cvars) and inc(dvars)
    return 'SPD_GLS_FULL_RANK_WITH_WEAK_ANCHOR_VARIANCE_GROWTH_SCOPED',{'cases':cases},bool(valid)

def lane_B():
    cases=[]; valid=True; M=design(1e-2)
    for name,S in covs():
        L=np.linalg.cholesky(S); Wc=np.linalg.solve(L,M); Fc=Wc.T@Wc
        e,U=np.linalg.eigh(S); We=(U*(1/np.sqrt(e)))@U.T; Fe=(We@M).T@(We@M)
        rel=float(np.max(np.abs(Fc-Fe))/max(np.max(np.abs(Fc)),1e-300)); cases.append({'covariance':name,'whitening_fisher_relerr':rel}); valid &= rel<1e-10
    return 'CHOLESKY_AND_EIGEN_WHITENING_AGREE_SCOPED',{'cases':cases},bool(valid)

def orthogonals():
    I=np.eye(4)
    return [('I',I),('swap_C_N1',I[:,[2,1,0,3]]),('swap_D_N3',I[:,[0,3,2,1]]),('flip_C',np.diag([-1,1,1,1]))]
def lane_C():
    cases=[]; valid=True; M=design(1e-2)
    for cname,S in covs():
        F=fisher(M,S); base=np.linalg.eigvalsh(F)
        for rname,R in orthogonals():
            eig=np.linalg.eigvalsh(R.T@F@R); rel=float(np.max(np.abs(eig-base)/np.maximum(np.abs(base),1e-300)))
            cases.append({'covariance':cname,'transform':rname,'fisher_eigen_relerr':rel}); valid &= rel<1e-8
    return 'ORTHOGONAL_GLS_FISHER_SPECTRUM_INVARIANCE_SCOPED',{'cases':cases},bool(valid)

def lane_D():
    S=np.eye(7); S[1,:]=S[0,:]; S[:,1]=S[:,0]
    singular_rejected=False
    try:
        np.linalg.solve(S,design(1.0))
    except np.linalg.LinAlgError:
        singular_rejected=True
    q=rank(design(1.0,aq=True,ad=False)); d=rank(design(1.0,aq=False,ad=True))
    valid=singular_rejected and q==3 and d==3
    return 'SINGULAR_COVARIANCE_AND_ONE_SIDED_GLS_CONTROLS_SCOPED',{'singular_covariance_rejected':singular_rejected,'aq_only_rank':q,'ad_only_rank':d},bool(valid)

ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=list('ABCD')); ap.add_argument('--out',required=True); a=ap.parse_args()
fn={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}[a.lane]
classification,checks,valid=fn()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True,allow_nan=False)
if not valid: raise SystemExit(2)
