import argparse, json
import numpy as np

PRIMARY=[1/3,2/3,5/4,7/3]
HELDOUT=[[1/5,3/5,4/3,9/4],[2/7,5/6,7/5,11/3],[1/2,4/5,3/2,13/5]]
TOL=1e-12

def base(zs):
    rows=[[-z,0,z,0] for z in zs]
    rows += [[0,1,0,1],[0,0,1,0],[0,0,0,1]]
    return np.array(rows,dtype=float)
def rank(M): return int(np.linalg.matrix_rank(M,tol=TOL))

def lane_A():
    M=base(PRIMARY); rs=[]
    for i in range(M.shape[0]): rs.append(rank(np.delete(M,i,axis=0)))
    valid=(rank(M)==4 and rs[:4]==[4,4,4,4] and rs[4:]==[3,3,3])
    return 'SINGLE_ROW_DELETION_FAILURE_MAP_SCOPED',{'full_rank':rank(M),'delete_ranks':rs},bool(valid)

def lane_B():
    M=base(PRIMARY); extra=np.array([[0,2,0,1]],float); X=np.vstack([M,extra])
    drop_orig=rank(np.delete(X,4,axis=0)); drop_extra=rank(np.delete(X,7,axis=0)); drop_both=rank(np.delete(X,[4,7],axis=0))
    valid=(rank(X)==4 and drop_orig==4 and drop_extra==4 and drop_both==3)
    return 'DISTINCT_CUBIC_ROW_ADDS_SINGLE_FAILURE_REDUNDANCY_SCOPED',{'aug_rank':rank(X),'drop_original_cubic_rank':drop_orig,'drop_extra_cubic_rank':drop_extra,'drop_both_cubic_rank':drop_both},bool(valid)

def lane_C():
    M=base(PRIMARY)
    no_ad=np.delete(M,6,axis=0); no_aq=np.delete(M,5,axis=0); no_cubic=np.delete(M,4,axis=0)
    dup_aq=rank(np.vstack([no_ad,[0,0,1,0]])); dup_ad=rank(np.vstack([no_aq,[0,0,0,1]])); pseudo=rank(np.vstack([no_cubic,[0,0,0,1]]))
    valid=(dup_aq==3 and dup_ad==3 and pseudo==3)
    return 'ROW_REDUNDANCY_FALSE_POSITIVE_CONTROLS_SCOPED',{'duplicated_AQ_without_AD_rank':dup_aq,'duplicated_AD_without_AQ_rank':dup_ad,'same_shape_cubic_pseudorow_rank':pseudo},bool(valid)

def lane_D():
    cases=[]; valid=True
    for pi,zs in enumerate(HELDOUT):
        M=base(zs); rs=[rank(np.delete(M,i,axis=0)) for i in range(M.shape[0])]
        item={'panel':pi,'full_rank':rank(M),'delete_ranks':rs}; cases.append(item)
        valid &= item['full_rank']==4 and rs[:4]==[4,4,4,4] and rs[4:]==[3,3,3]
    return 'HELDOUT_SINGLE_ROW_FAILURE_PATTERN_SCOPED',{'cases':cases},bool(valid)

ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=list('ABCD')); ap.add_argument('--out',required=True); a=ap.parse_args()
fn={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}[a.lane]
classification,checks,valid=fn()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True,allow_nan=False)
if not valid: raise SystemExit(2)
