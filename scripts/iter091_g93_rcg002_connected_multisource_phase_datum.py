import argparse, json, os
import sympy as sp

BITS=[(a,b,c) for a in (0,1) for b in (0,1) for c in (0,1)]
SIG={(a,b,c): (-1)**(3-(a+b+c)) for a,b,c in BITS}

def delta(vals):
    return sp.simplify(sum(SIG[x]*vals[x] for x in BITS))

def lane_a():
    q0,qA,qB,qC=sp.symbols('q0 qA qB qC')
    qAB,qAC,qBC=sp.symbols('qAB qAC qBC')
    vals={(a,b,c):q0+qA*a+qB*b+qC*c+qAB*a*b+qAC*a*c+qBC*b*c for a,b,c in BITS}
    exact=sp.simplify(delta(vals))
    panel=[(sp.Rational(1,3),sp.Rational(-2,5),sp.Rational(7,4),sp.Rational(5,6),sp.Rational(-4,7),sp.Rational(9,8),sp.Rational(11,10)),
           (sp.Rational(-5,9),sp.Rational(3,11),sp.Rational(2,7),sp.Rational(-8,13),sp.Rational(4,9),sp.Rational(-6,5),sp.Rational(7,12))]
    syms=(q0,qA,qB,qC,qAB,qAC,qBC)
    held=[sp.simplify(exact.subs(dict(zip(syms,p)))) for p in panel]
    malformed=dict(SIG); malformed[(1,1,0)]*=-1
    bad=sp.expand(sum(malformed[x]*vals[x] for x in BITS))
    ok=(exact==0 and all(v==0 for v in held) and bad!=0)
    return {'lane':'A','pass':bool(ok),'delta_lower_order':str(exact),'heldout':[str(v) for v in held],'malformed_control':str(bad)}

def lane_b():
    la,lb,lc,xab,xac,xbc=sp.symbols('la lb lc chi_AB chi_AC chi_BC')
    vals={(a,b,c):la*a+lb*b+lc*c+xab*a*b+xac*a*c+xbc*b*c for a,b,c in BITS}
    d=sp.simplify(delta(vals))
    return {'lane':'B','pass':bool(d==0),'delta3_pairwise_rcg002':str(d)}

def lane_c():
    k=sp.symbols('kappa')
    vals={(a,b,c):k*a*b*c for a,b,c in BITS}
    d=sp.simplify(delta(vals))
    panel=[sp.Rational(2,7),sp.Rational(-5,11),sp.Rational(13,9),sp.Rational(1,17)]
    held=[sp.simplify(d.subs(k,v)-v) for v in panel]
    ok=(sp.simplify(d-k)==0 and all(v==0 for v in held))
    return {'lane':'C','pass':bool(ok),'delta3_connected':str(d),'heldout_residuals':[str(v) for v in held]}

def lane_d():
    cols=[]
    cols.append([1 for _ in BITS])
    cols += [[x[i] for x in BITS] for i in range(3)]
    cols += [[x[0]*x[1] for x in BITS],[x[0]*x[2] for x in BITS],[x[1]*x[2] for x in BITS]]
    conn=[x[0]*x[1]*x[2] for x in BITS]
    cols.append(conn)
    M=sp.Matrix.hstack(*[sp.Matrix(c) for c in cols])
    w=sp.Matrix([SIG[x] for x in BITS])
    actions=[sp.simplify((w.T*sp.Matrix(c))[0]) for c in cols]
    dup_cols=cols[:-1]+[cols[4]]
    zero_cols=cols[:-1]+[[0]*8]
    rank_full=M.rank(); rank_dup=sp.Matrix.hstack(*[sp.Matrix(c) for c in dup_cols]).rank(); rank_zero=sp.Matrix.hstack(*[sp.Matrix(c) for c in zero_cols]).rank()
    ok=(actions[:7]==[0]*7 and actions[7]!=0 and rank_full==8 and rank_dup<8 and rank_zero<8)
    return {'lane':'D','pass':bool(ok),'actions':[str(v) for v in actions],'rank_full':rank_full,'rank_dup_control':rank_dup,'rank_zero_control':rank_zero}

def aggregate(root):
    data=[]
    for lane in 'ABCD':
        found=[]
        for dp,_,fs in os.walk(root):
            for f in fs:
                if f==f'g93_{lane}.json': found.append(os.path.join(dp,f))
        if len(found)!=1: raise RuntimeError(f'lane {lane}: expected one artifact json, found {found}')
        with open(found[0]) as fh: data.append(json.load(fh))
    allpass=all(x.get('pass') for x in data)
    classification='BLOCKED_RCG002_CURRENT_PAIRWISE_CHANNEL_HAS_NO_CANDIDATE_OWNED_CONNECTED_THREE_SOURCE_DATUM_SCOPED' if allpass else 'SCIENTIFIC_FAIL_G93_FROZEN_CRITERIA'
    return {'gate':'G93','pass':allpass,'classification':classification,'lanes':data,'theory_established_percent':0,'programme_readiness_percent':66}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--lane',choices=list('ABCD')); p.add_argument('--aggregate'); p.add_argument('--out',required=True); a=p.parse_args()
    if a.aggregate: r=aggregate(a.aggregate)
    else: r={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}[a.lane]()
    with open(a.out,'w') as f: json.dump(r,f,indent=2,sort_keys=True)
    print(json.dumps(r,indent=2,sort_keys=True))
    if not r.get('pass',False): raise SystemExit(2)
if __name__=='__main__': main()
