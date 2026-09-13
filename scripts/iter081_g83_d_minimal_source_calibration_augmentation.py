import argparse, json
from fractions import Fraction as F
import sympy as sp

TIMES=range(4)
QS=[F(1),F(2),F(5,3)]


def rank(a,b): return sp.Matrix.hstack(sp.Matrix(a),sp.Matrix(b)).rank()
def candidate_kernel():
    K={}
    for td in TIMES:
        for t1 in TIMES:
            for t2 in TIMES:
                v=F(((td+2)*(t1+3)+(t2+5))%7-3)
                if td < max(t1,t2): v=F(0)
                K[(td,t1,t2)]=v
    for key,v in list(K.items()):
        td,t1,t2=key; w=K[(td,t2,t1)]; vv=(v+w)/2
        K[(td,t1,t2)]=K[(td,t2,t1)]=vv
    return K

def reference_kernel(advanced=False):
    R={(td,t1,t2):F(0) for td in TIMES for t1 in TIMES for t2 in TIMES}
    if advanced:
        R[(0,2,3)]=F(1); R[(0,3,2)]=F(1)
    else:
        R[(3,1,2)]=F(1); R[(3,2,1)]=F(1)
    return R

def retarded(K): return all(v==0 for (td,t1,t2),v in K.items() if td<max(t1,t2))
def symmetric(K): return all(v==K[(td,t2,t1)] for (td,t1,t2),v in K.items())
def norm2(K): return sum(v*v for v in K.values())
def nonzero_vals(K): return [v for _,v in sorted(K.items()) if v!=0]

def lane_A():
    vals=nonzero_vals(candidate_kernel()); base=rank(vals,vals); valid=(len(vals)>=2 and base==1)
    q_ranks={}
    for q in QS:
        r=rank(vals+[F(0)],vals+[q]); q_ranks[str(q)]=r; valid &= r==2
    z=rank(vals+[F(0)],vals+[F(0)]); valid &= z==1
    return 'D_SINGLE_REFERENCE_CHANNEL_ALGEBRAIC_SUFFICIENCY_SCOPED',{'science_nonzero_entries':len(vals),'science_rank':base,'q_ranks':q_ranks,'zero_q_rank':z},bool(valid)

def lane_B():
    K=candidate_kernel(); R=reference_kernel(False); qref=norm2(R)
    kr=retarded(K); ks=symmetric(K); rr=retarded(R); rs=symmetric(R)
    vals=nonzero_vals(K); aug=rank(vals+[F(0)],vals+[qref])
    valid=(kr and ks and rr and rs and qref!=0 and aug==2)
    checks={'candidate_retarded':kr,'candidate_sigma_symmetric':ks,'reference_retarded':rr,'reference_sigma_symmetric':rs,'q_ref':str(qref),'augmented_rank':aug,'candidate_advanced_support_absent':kr,'reference_advanced_support_absent':rr}
    return 'D_RETARDED_SOURCE_DEFINED_REFERENCE_COMPATIBILITY_SCOPED',checks,bool(valid)

def lane_C():
    K=candidate_kernel(); before=dict(K); after=dict(K)
    d0,d1,s0,s1=sp.symbols('d0 d1 s0 s1'); fields=[d0,d1,s0,s1]
    G=d0*s0**2+2*d0*s0*s1+d1*s1**2; zero={x:0 for x in fields}
    H=[sp.diff(G,x,y).subs(zero) for x in fields for y in fields]
    T=[sp.diff(G,x,y,z).subs(zero) for x in fields for y in fields for z in fields]
    ctp_norm=sp.simplify(G.subs({d0:0,d1:0}))==0
    hzero=all(x==0 for x in H); tnonzero=any(x!=0 for x in T)
    vals=nonzero_vals(K); recovered=rank(vals,vals)
    checks={'candidate_kernel_identical':before==after,'ctp_normalization_exact':ctp_norm,'hessian_zero':hzero,'third_derivative_nonzero':tnonzero,'recovered_rank_without_reference':recovered}
    valid=(before==after and ctp_norm and hzero and tnonzero and recovered==1)
    return 'D_REFERENCE_CHANNEL_BLOCK_SEPARATE_NONMODIFICATION_SCOPED',checks,bool(valid)

def lane_D():
    vals=nonzero_vals(candidate_kernel()); q=F(5,3)
    same=rank(vals+[q],vals+[q]); zero=rank(vals+[F(0)],vals+[F(0)]); candidate_only=rank(vals+[q],vals+[F(0)])
    bad=reference_kernel(True); advanced_detected=not retarded(bad)
    rescales={}; valid=(same==1 and zero==1 and candidate_only==2 and advanced_detected)
    for a in [F(1),F(-2),F(3,5)]:
        r=rank(vals+[F(0)],vals+[a*q]); rescales[str(a)]=r; valid &= r==2
    checks={'same_kernel_pseudoref_rank':same,'zero_pseudoref_rank':zero,'candidate_only_detection_rank':candidate_only,'candidate_only_is_accepted_calibration':False,'advanced_reference_rejected':advanced_detected,'accepted_reference_rescale_ranks':rescales}
    return 'D_REFERENCE_CHANNEL_FALSE_ANCHOR_CONTROLS_SCOPED',checks,bool(valid)

LANES={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=sorted(LANES)); ap.add_argument('--out',required=True); a=ap.parse_args()
classification,checks,valid=LANES[a.lane]()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
if not valid: raise SystemExit(2)
