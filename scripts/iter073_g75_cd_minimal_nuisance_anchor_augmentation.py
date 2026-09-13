import argparse, json
import sympy as sp

PRIMARY=[sp.Rational(1,3),sp.Rational(2,3),sp.Rational(5,4),sp.Rational(7,3)]
HELDOUT=[
    [sp.Rational(1,5),sp.Rational(3,5),sp.Rational(4,3),sp.Rational(9,4)],
    [sp.Rational(2,7),sp.Rational(5,6),sp.Rational(7,5),sp.Rational(11,3)],
    [sp.Rational(1,2),sp.Rational(4,5),sp.Rational(3,2),sp.Rational(13,5)],
]
AQ=sp.Matrix([[0,0,1,0]])
AD=sp.Matrix([[0,0,0,1]])
ZERO=sp.Matrix([[0,0,0,0]])
ZSTAR=sp.Rational(3,2)
QAUX=sp.Matrix([[-ZSTAR**2,0,ZSTAR,0]])
DAUX=sp.Matrix([[0,1,0,2]])
QSAME=sp.Matrix([[-ZSTAR,0,ZSTAR,0]])
DSAME=sp.Matrix([[0,1,0,1]])

R1=sp.Matrix([[1,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
R2=sp.Matrix([[1,0,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]])
R3=sp.Matrix([[2,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,2]])
RS=[R1,R2,R3]

def baseline(zs):
    rows=[[-z,0,z,0] for z in zs]
    rows.append([0,1,0,1])
    return sp.Matrix(rows)

def aug(M,*rows):
    out=M
    for r in rows:
        out=out.col_join(r)
    return out

def lane_A():
    M=baseline(PRIMARY)
    checks={
        'baseline_rank':M.rank(),
        'AQ_only_rank':aug(M,AQ).rank(),
        'AD_only_rank':aug(M,AD).rank(),
        'AQ_AD_rank':aug(M,AQ,AD).rank(),
    }
    valid=checks=={'baseline_rank':2,'AQ_only_rank':3,'AD_only_rank':3,'AQ_AD_rank':4}
    return 'DIRECT_TWO_ANCHOR_MINIMALITY_SCOPED',checks,valid

def lane_B():
    M=baseline(PRIMARY)
    checks={
        'qaux_only_rank':aug(M,QAUX).rank(),
        'daux_only_rank':aug(M,DAUX).rank(),
        'both_aux_rank':aug(M,QAUX,DAUX).rank(),
        'qsame_only_rank':aug(M,QSAME).rank(),
        'dsame_only_rank':aug(M,DSAME).rank(),
        'both_same_rank':aug(M,QSAME,DSAME).rank(),
    }
    valid=checks=={
        'qaux_only_rank':3,'daux_only_rank':3,'both_aux_rank':4,
        'qsame_only_rank':2,'dsame_only_rank':2,'both_same_rank':2}
    return 'DISTINCT_RESPONSE_TWO_AUGMENTATION_RESTORES_RANK_SCOPED',checks,valid

def lane_C():
    panel_checks=[]
    valid=True
    for zs in HELDOUT:
        M=baseline(zs)
        row={
            'panel':[str(z) for z in zs],
            'baseline_rank':M.rank(),
            'AQ_only_rank':aug(M,AQ).rank(),
            'AD_only_rank':aug(M,AD).rank(),
            'both_rank':aug(M,AQ,AD).rank(),
        }
        panel_checks.append(row)
        valid &= (row['baseline_rank']==2 and row['AQ_only_rank']==3 and row['AD_only_rank']==3 and row['both_rank']==4)
    F=aug(baseline(PRIMARY),AQ,AD)
    reparam=[]
    for i,R in enumerate(RS,1):
        rr={'name':f'R{i}','det':int(R.det()),'rank':(F*R).rank()}
        reparam.append(rr)
        valid &= (rr['det']!=0 and rr['rank']==4)
    checks={'panels':panel_checks,'reparameterizations':reparam}
    return 'HELDOUT_PANEL_AND_REPARAMETERIZATION_ROBUSTNESS_SCOPED',checks,bool(valid)

def lane_D():
    M=baseline(PRIMARY)
    checks={
        'duplicate_AQ_without_AD_rank':aug(M,AQ,AQ).rank(),
        'duplicate_AD_without_AQ_rank':aug(M,AD,AD).rank(),
        'same_shape_pair_rank':aug(M,QSAME,DSAME).rank(),
        'zero_anchor_pair_rank':aug(M,ZERO,ZERO).rank(),
        'only_quadratic_alias_broken_rank':aug(M,QAUX).rank(),
        'only_cubic_alias_broken_rank':aug(M,DAUX).rank(),
    }
    valid=checks=={
        'duplicate_AQ_without_AD_rank':3,
        'duplicate_AD_without_AQ_rank':3,
        'same_shape_pair_rank':2,
        'zero_anchor_pair_rank':2,
        'only_quadratic_alias_broken_rank':3,
        'only_cubic_alias_broken_rank':3,
    }
    return 'ADVERSARIAL_MINIMALITY_AND_FALSE_POSITIVE_CONTROLS_SCOPED',checks,valid

ap=argparse.ArgumentParser()
ap.add_argument('--lane',required=True,choices=list('ABCD'))
ap.add_argument('--out',required=True)
a=ap.parse_args()
fn={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}[a.lane]
classification,checks,valid=fn()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f:
    json.dump(out,f,indent=2,sort_keys=True)
if not valid:
    raise SystemExit(2)
