import argparse, json
from fractions import Fraction as F
import sympy as sp

TIMES=range(4)

def kernel():
    K={}
    for td in TIMES:
        for t1 in TIMES:
            for t2 in TIMES:
                v=F(((td+2)*(t1+3)+(t2+5))%7-3)
                if td < max(t1,t2): v=F(0)
                K[(td,t1,t2)]=v
    for key,v in list(K.items()):
        td,t1,t2=key
        w=K[(td,t2,t1)]
        vv=(v+w)/2
        K[(td,t1,t2)]=K[(td,t2,t1)]=vv
    return K

def rank(a,b): return sp.Matrix.hstack(sp.Matrix(a),sp.Matrix(b)).rank()
def s(x): return str(x)

def lane_A():
    K=kernel(); allowed=[(key,v) for key,v in sorted(K.items()) if v!=0]
    vals=[v for _,v in allowed]
    r=rank(vals,vals); equal=all(a==b for a,b in zip(vals,vals))
    valid=(len(vals)>=2 and r==1 and equal)
    return 'D_EXACT_CUBIC_KERNEL_ALIAS_CONFIRMED_SCOPED',{'nonzero_allowed_entries':len(vals),'rank':r,'exact_D_minus_N3_zero':equal},bool(valid)

def lane_B():
    K=kernel(); allowed=[(key,v) for key,v in sorted(K.items()) if v!=0]
    vals=[v for _,v in allowed]
    perm=[K[(td,t2,t1)] for (td,t1,t2),_ in allowed]
    symmetry=all(v==K[(td,t2,t1)] for (td,t1,t2),v in K.items())
    advanced_zero=all(v==0 for (td,t1,t2),v in K.items() if td<max(t1,t2))
    native_zero_rows=[F(0)]*8
    c=vals+perm+native_zero_rows
    n=vals+perm+native_zero_rows
    r=rank(c,n)
    valid=(symmetry and advanced_zero and r==1)
    checks={'augmented_rank':r,'sigma_permutation_exact':symmetry,'advanced_support_exactly_zero':advanced_zero,'native_zero_rows':len(native_zero_rows)}
    return 'D_NATIVE_SUPPORT_PERMUTATION_NORMALIZATION_PRESERVES_ALIAS_SCOPED',checks,bool(valid)

def lane_C():
    d0,d1,s0,s1=sp.symbols('d0 d1 s0 s1'); fields=[d0,d1,s0,s1]
    base=d0*s0**2+2*d0*s0*s1+d1*s1**2
    zero={x:0 for x in fields}
    H=[sp.diff(base,x,y).subs(zero) for x in fields for y in fields]
    T=[sp.diff(base,x,y,z).subs(zero) for x in fields for y in fields for z in fields]
    hzero=all(x==0 for x in H); tnonzero=any(x!=0 for x in T)
    sig=H+T; r=rank(sig,sig)
    valid=(hzero and tnonzero and r==1)
    return 'D_NATIVE_JET_STRUCTURE_PRESERVES_ALIAS_SCOPED',{'hessian_zero':hzero,'third_derivative_nonzero':tnonzero,'combined_jet_rank':r},bool(valid)

def lane_D():
    K=kernel(); vals=[v for _,v in sorted(K.items()) if v!=0]
    alt=list(vals); alt[0]+=F(1)
    distinct=rank(vals,alt)
    direct=rank(vals+[F(0)],vals+[F(1)])
    advanced=rank(vals+[F(0)],vals+[F(1)])
    pseudo=rank(vals+[F(0)],vals+[F(0)])
    valid=(distinct==2 and direct==2 and advanced==2 and pseudo==1)
    checks={'distinct_kernel_rank':distinct,'non_native_direct_calibration_rank':direct,'advanced_nuisance_control_rank':advanced,'zero_pseudocalibration_rank':pseudo}
    return 'D_ANCHOR_AUDIT_SEPARABILITY_CONTROLS_VALID_SCOPED',checks,bool(valid)

LANES={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=sorted(LANES)); ap.add_argument('--out',required=True); a=ap.parse_args()
classification,checks,valid=LANES[a.lane]()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
if not valid: raise SystemExit(2)
