import argparse, json
import sympy as sp

zs=[sp.Rational(1,3),sp.Rational(2,3),sp.Rational(5,4),sp.Rational(7,3)]
C=sp.Matrix([-z for z in zs]+[0])
D=sp.Matrix([0,0,0,0,1])
N0=sp.Matrix([1,1,1,1,0])
N1=sp.Matrix(zs+[0])
N2=sp.Matrix([z*z for z in zs]+[0])
N3=D.copy()

def rank(*cols): return sp.Matrix.hstack(*cols).rank()

def lane_A():
    checks={"rank_CD":rank(C,D),"rank_CDN0":rank(C,D,N0),"rank_DN0":rank(D,N0)}
    valid=checks=={"rank_CD":2,"rank_CDN0":3,"rank_DN0":2}
    return "BASELINE_AND_CONSTANT_NUISANCE_INDEPENDENCE_SCOPED",checks,valid

def lane_B():
    checks={"rank_CN1":rank(C,N1),"C_plus_N1_zero":bool(C+N1==sp.zeros(5,1)),"rank_CN2":rank(C,N2)}
    valid=checks=={"rank_CN1":1,"C_plus_N1_zero":True,"rank_CN2":2}
    return "C_SAME_SHAPE_SLOPE_CONFOUNDED_DISTINCT_CURVATURE_SEPARABLE_SCOPED",checks,valid

def lane_C():
    checks={"rank_DN3":rank(D,N3),"rank_DN0":rank(D,N0),"rank_DN2":rank(D,N2)}
    valid=checks=={"rank_DN3":1,"rank_DN0":2,"rank_DN2":2}
    return "D_SAME_SHAPE_CUBIC_CALIBRATION_CONFOUNDED_SCOPED",checks,valid

def lane_D():
    full=rank(C,D,N0,N2)
    with_alias=rank(C,D,N0,N2,N1,N3)
    # auxiliary second cubic observable: extend vectors to 6 rows
    D6=sp.Matrix([0,0,0,0,1,0]); M6=sp.Matrix([0,0,0,0,1,1])
    aux_rank=rank(D6,M6)
    checks={"rank_CDN0N2":full,"rank_with_aliases":with_alias,"auxiliary_cubic_control_rank":aux_rank}
    valid=(full==4 and with_alias==4 and aux_rank==2)
    return "COMBINED_ALIAS_AND_ADDITIONAL_OBSERVABLE_CONTROL_SCOPED",checks,valid

ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=list('ABCD')); ap.add_argument('--out',required=True); a=ap.parse_args()
fn={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}[a.lane]
classification,checks,valid=fn()
out={"stream":a.lane,"classification":classification,"checks":checks,"valid":bool(valid),"readiness":66,"theory_established":0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
if not valid: raise SystemExit(2)
