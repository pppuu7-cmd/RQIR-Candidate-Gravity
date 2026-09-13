import argparse, json, math
import numpy as np
import mpmath as mp

PRIMARY=[1/3,2/3,5/4,7/3]
HELDOUT=[[1/5,3/5,4/3,9/4],[2/7,5/6,7/5,11/3],[1/2,4/5,3/2,13/5]]
ALPHAS=[1.0,1e-1,1e-2,1e-3,1e-4,1e-5,1e-6]
TOL=1e-12

def baseline(zs):
    rows=[[-z,0,z,0] for z in zs]
    rows.append([0,1,0,1])
    return np.array(rows,dtype=float)

def aug(M,*rows):
    return np.vstack([M,*[np.asarray(r,dtype=float).reshape(1,4) for r in rows]])

def metrics(M):
    s=np.linalg.svd(M,compute_uv=False)
    rank=int(np.sum(s>TOL))
    smin=float(s[-1]); smax=float(s[0])
    cond=float(smax/smin) if smin>0 else float('inf')
    return rank,smin,smax,cond

def strict_dec(xs): return all(xs[i+1] < xs[i] for i in range(len(xs)-1))
def strict_inc(xs): return all(xs[i+1] > xs[i] for i in range(len(xs)-1))

def lane_A():
    M=baseline(PRIMARY); rows=[]
    for a in ALPHAS:
        r,smin,smax,c=metrics(aug(M,[0,0,a,0],[0,0,0,a]))
        rows.append({'a':a,'rank':r,'smin':smin,'smax':smax,'cond':c})
    zero_rank=metrics(aug(M,[0,0,0,0],[0,0,0,0]))[0]
    valid=(all(x['rank']==4 and x['smin']>0 for x in rows)
           and strict_dec([x['smin'] for x in rows])
           and strict_inc([x['cond'] for x in rows])
           and zero_rank==2)
    return 'DIRECT_ANCHOR_STRENGTH_CONDITIONING_SCOPED',{'series':rows,'zero_anchor_rank':zero_rank},valid

def lane_B():
    M=baseline(PRIMARY); z=1.5; rows=[]
    for d in ALPHAS:
        Q=[-z+d,0,z,0]; D=[0,1,0,1+d]
        r,smin,smax,c=metrics(aug(M,Q,D))
        rows.append({'delta':d,'rank':r,'smin':smin,'smax':smax,'cond':c})
    r0=metrics(aug(M,[-z,0,z,0],[0,1,0,1]))[0]
    valid=(all(x['rank']==4 and x['smin']>0 for x in rows)
           and strict_dec([x['smin'] for x in rows])
           and strict_inc([x['cond'] for x in rows])
           and r0==2)
    return 'NEAR_SHAPE_APPROACH_TO_ALIAS_CONDITIONING_SCOPED',{'series':rows,'exact_alias_rank':r0},valid

def orthogonals():
    I=np.eye(4)
    Pq=I[:,[2,1,0,3]]
    Pd=I[:,[0,3,2,1]]
    Pboth=Pq@Pd
    Sc=np.diag([-1,1,1,1])
    Sd=np.diag([1,-1,1,1])
    return [('I',I),('swap_C_N1',Pq),('swap_D_N3',Pd),('both_swaps',Pboth),('flip_C',Sc),('flip_D',Sd)]

def lane_C():
    checks=[]; valid=True
    for pi,zs in enumerate(HELDOUT):
        M=baseline(zs)
        for a in [1.0,1e-3,1e-6]:
            F=aug(M,[0,0,a,0],[0,0,0,a])
            base_s=np.linalg.svd(F,compute_uv=False)
            rank=metrics(F)[0]
            item={'panel':pi,'a':a,'rank':rank,'orthogonal_relerrs':{}}
            valid &= (rank==4)
            for name,R in orthogonals():
                s=np.linalg.svd(F@R,compute_uv=False)
                rel=float(np.max(np.abs(s-base_s)/np.maximum(np.abs(base_s),1e-300)))
                item['orthogonal_relerrs'][name]=rel
                valid &= (rel < 1e-12)
            checks.append(item)
    return 'HELDOUT_AND_ORTHOGONAL_COORDINATE_ROBUSTNESS_SCOPED',{'cases':checks},bool(valid)

def mp_svals(M):
    mp.mp.dps=80
    A=mp.matrix([[mp.mpf(str(x)) for x in row] for row in M.tolist()])
    G=A.T*A
    vals,_=mp.eigsy(G)
    vals=[max(mp.mpf('0'),vals[i]) for i in range(len(vals))]
    ss=sorted([mp.sqrt(v) for v in vals],reverse=True)
    return float(ss[0]),float(ss[-1])

def lane_D():
    M=baseline(PRIMARY); cases=[]; valid=True
    for a in [1.0,1e-2,1e-4,1e-6]:
        F=aug(M,[0,0,a,0],[0,0,0,a])
        _,smin,smax,_=metrics(F)
        hmax,hmin=mp_svals(F)
        relmin=abs(smin-hmin)/max(abs(hmin),1e-300)
        relmax=abs(smax-hmax)/max(abs(hmax),1e-300)
        cases.append({'a':a,'rel_smin':relmin,'rel_smax':relmax})
        valid &= (relmin<1e-8 and relmax<1e-8)
    zero_smin=metrics(aug(M,[0,0,0,0],[0,0,0,0]))[1]
    z=1.5
    same_smin=metrics(aug(M,[-z,0,z,0],[0,1,0,1]))[1]
    one_rank=metrics(aug(M,[0,0,1,0]))[0]
    valid &= (zero_smin<TOL and same_smin<TOL and one_rank==3)
    return 'PRECISION_CONVERGENCE_AND_FALSE_POSITIVE_CALIBRATION_SCOPED',{'precision_cases':cases,'zero_smin':zero_smin,'same_shape_smin':same_smin,'one_sided_anchor_rank':one_rank},bool(valid)

ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=list('ABCD')); ap.add_argument('--out',required=True); a=ap.parse_args()
fn={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}[a.lane]
classification,checks,valid=fn()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True,allow_nan=False)
if not valid: raise SystemExit(2)
