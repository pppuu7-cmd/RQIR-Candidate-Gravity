import argparse, json
from sympy import symbols, diff, simplify, Matrix, Rational

z,a,b=symbols('z a b')
c=3*a+b
PTT=z*(b*z-4)/2
PS=3*z*(c*z+2)
RAYS=[(1,1),(2,-1),(1,-2),(-1,1),(-2,3),(3,2),(2,-5),(-3,4),(5,-1),(4,-7),(7,3),(-5,2)]
US=[Matrix([[1,1],[0,1]]),Matrix([[0,1],[1,0]]),Matrix([[2,1],[1,1]])]

def residues(poly, roots):
    dp=diff(poly,z)
    return [simplify(1/dp.subs(z,r)) for r in roots]

def sector_values(av,bv):
    out={}
    if bv!=0:
        roots=[0,Rational(4,bv)]
        rr=residues(PTT.subs({a:av,b:bv}),roots)
        out['tt']={'extra':True,'roots':[str(x) for x in roots],'res':[str(x) for x in rr],'ratio':str(simplify(rr[1]/rr[0]))}
    else:
        out['tt']={'extra':False}
    cv=3*av+bv
    if cv!=0:
        roots=[0,Rational(-2,cv)]
        rr=residues(PS.subs({a:av,b:bv}),roots)
        out['scalar']={'extra':True,'roots':[str(x) for x in roots],'res':[str(x) for x in rr],'ratio':str(simplify(rr[1]/rr[0]))}
    else:
        out['scalar']={'extra':False}
    return out

def stream_A():
    tt0=simplify(1/diff(PTT,z).subs(z,0))
    tte=simplify(1/diff(PTT,z).subs(z,4/b))
    s0=simplify(1/diff(PS,z).subs(z,0))
    se=simplify(1/diff(PS,z).subs(z,-2/c))
    ok=(tt0==Rational(-1,2) and tte==Rational(1,2) and simplify(tte/tt0)==-1 and s0==Rational(1,6) and se==Rational(-1,6) and simplify(se/s0)==-1)
    return {'stream':'A','valid':True,'pass':bool(ok),'tt':[str(tt0),str(tte)],'scalar':[str(s0),str(se)]}

def stream_B():
    details=[]; ok=True
    for av,bv in RAYS:
        d=sector_values(av,bv); details.append({'ray':[av,bv],**d})
        for key in ('tt','scalar'):
            if d[key].get('extra') and d[key]['ratio']!='-1': ok=False
    return {'stream':'B','valid':True,'pass':ok,'count':len(details),'details':details}

def stream_C():
    checks=0; passed=0
    row_b=Matrix([[0,1]]); row_c=Matrix([[3,1]])
    for U in US:
        Ui=U.inv()
        rb=row_b*Ui; rc=row_c*Ui
        for av,bv in RAYS:
            x=Matrix([av,bv]); xp=U*x
            bv2=simplify((rb*xp)[0]); cv2=simplify((rc*xp)[0])
            checks+=2
            if bv2==bv: passed+=1
            if cv2==3*av+bv: passed+=1
            d=sector_values(av,bv)
            for key in ('tt','scalar'):
                if d[key].get('extra'):
                    checks+=1
                    if d[key]['ratio']=='-1': passed+=1
    return {'stream':'C','valid':True,'pass':checks==passed,'checks':checks,'passed':passed}

def stream_D():
    tt_exc=sector_values(1,0)['tt']['extra'] is False
    sc_exc=sector_values(1,-3)['scalar']['extra'] is False
    wrong_rejected=0; total_nonexc=0; scale_checks=0; scale_pass=0
    for av,bv in RAYS:
        d=sector_values(av,bv)
        for key,poly in [('tt',PTT.subs({a:av,b:bv})),('scalar',PS.subs({a:av,b:bv}))]:
            if d[key].get('extra'):
                total_nonexc+=1
                if d[key]['ratio']!='1': wrong_rejected+=1
                roots=[Rational(0), Rational(4,bv)] if key=='tt' else [Rational(0),Rational(-2,3*av+bv)]
                for k in (-3,-1,2,5):
                    rr=residues(k*poly,roots); scale_checks+=1
                    if simplify(rr[1]/rr[0])==-1: scale_pass+=1
    ok=tt_exc and sc_exc and wrong_rejected==total_nonexc and scale_pass==scale_checks
    return {'stream':'D','valid':True,'pass':ok,'tt_exceptional':tt_exc,'scalar_exceptional':sc_exc,'wrong_same_sign_rejected':wrong_rejected,'nonexceptional_total':total_nonexc,'scale_checks':scale_checks,'scale_pass':scale_pass}

def aggregate(path):
    import os
    passes={}
    for s in 'ABCD':
        found=None
        for root,_,files in os.walk(path):
            if f'{s}.json' in files:
                found=os.path.join(root,f'{s}.json'); break
        if not found: passes[s]=False; continue
        with open(found) as f: d=json.load(f)
        passes[s]=bool(d.get('valid') and d.get('pass'))
    valid=all(passes.values())
    return {'gate':'ITER060_G62_RELATIVE_RESIDUE_ALGEBRAIC_AUDIT','valid':valid,'passes':passes,'classification':'FOUR_DERIVATIVE_LINEARIZED_SECTOR_RELATIVE_RESIDUE_OPPOSITION_SCOPED' if valid else 'SCIENTIFIC_FAIL_G62','programme_readiness_percent':66,'theory_established_percent':0}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--stream'); p.add_argument('--out',required=True); p.add_argument('--aggregate-dir'); args=p.parse_args()
    if args.aggregate_dir: d=aggregate(args.aggregate_dir)
    else: d={'A':stream_A,'B':stream_B,'C':stream_C,'D':stream_D}[args.stream]()
    import os; os.makedirs(os.path.dirname(args.out),exist_ok=True)
    with open(args.out,'w') as f: json.dump(d,f,indent=2,sort_keys=True)
    if not d.get('valid',False) or ('pass' in d and not d['pass']): raise SystemExit(2)
if __name__=='__main__': main()
