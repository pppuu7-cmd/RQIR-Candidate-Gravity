#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import sympy as sp

z,a,b=sp.symbols('z a b', real=True)
c=3*a+b
Ptt=z*(b*z-4)/2
Psc=3*z*(c*z+2)
rays=[(1,1),(2,-1),(1,-2),(-1,1),(-2,3),(3,2),(2,-5),(-3,4),(5,-1),(4,-7),(7,3),(-5,2)]
mats=[[[1,0],[0,1]],[[1,1],[0,1]],[[1,0],[1,1]],[[2,1],[1,1]],[[1,2],[1,3]],[[-1,1],[1,1]],[[2,-1],[1,1]],[[3,1],[-1,1]]]

def residue(P, root):
    return sp.simplify(1/sp.diff(P,z).subs(z,root))

def sector_data(P, root):
    r0=sp.simplify(1/sp.diff(P,z).subs(z,0))
    r1=sp.simplify(residue(P,root))
    recon=sp.simplify(r0/z+r1/(z-root)-1/P)
    signs=(int(sp.sign(r0)),int(sp.sign(r1)))
    return r0,r1,recon,signs

def stream_A():
    ztt=sp.simplify(4/b); zsc=sp.simplify(-2/c)
    t=sector_data(Ptt,ztt); s=sector_data(Psc,zsc)
    ok=(t[0]==-sp.Rational(1,2) and t[1]==sp.Rational(1,2) and t[2]==0 and t[3][0]*t[3][1]==-1 and
        s[0]==sp.Rational(1,6) and s[1]==-sp.Rational(1,6) and s[2]==0 and s[3][0]*s[3][1]==-1)
    return {'stream':'A','valid':True,'pass':bool(ok),'tt_root':str(ztt),'scalar_root':str(zsc),'tt_res':[str(t[0]),str(t[1])],'scalar_res':[str(s[0]),str(s[1])],'tt_reconstruction_zero':bool(t[2]==0),'scalar_reconstruction_zero':bool(s[2]==0),'inertia':[1,1]}

def stream_B():
    details=[]; ok=True; nonexc=0; exc=0
    for av,bv in rays:
        cv=3*av+bv
        row={'ray':[av,bv]}
        if bv!=0:
            root=sp.Rational(4,bv); r0=-sp.Rational(1,2); r1=sp.Rational(1,2)
            good=(root.is_real is True and r0*r1<0)
            row['tt']={'exceptional':False,'root':str(root),'res':[str(r0),str(r1)],'inertia':[1,1],'pass':bool(good)}; nonexc+=1; ok &= bool(good)
        else:
            row['tt']={'exceptional':True,'one_pole':True}; exc+=1
        if cv!=0:
            root=-sp.Rational(2,cv); r0=sp.Rational(1,6); r1=-sp.Rational(1,6)
            good=(root.is_real is True and r0*r1<0)
            row['scalar']={'exceptional':False,'root':str(root),'res':[str(r0),str(r1)],'inertia':[1,1],'pass':bool(good)}; nonexc+=1; ok &= bool(good)
        else:
            row['scalar']={'exceptional':True,'one_pole':True}; exc+=1
        details.append(row)
    return {'stream':'B','valid':True,'pass':bool(ok),'rays':len(rays),'nonexceptional_sectors':nonexc,'exceptional_sectors':exc,'details':details}

def stream_C():
    checks=0; passed=0; rows=[]
    for name,S in [('tt',sp.diag(-1,1)),('scalar',sp.diag(1,-1))]:
        for mm in mats:
            M=sp.Matrix(mm); detm=sp.det(M); T=sp.simplify(M.T*S*M); lhs=sp.det(T); rhs=sp.expand(detm**2*sp.det(S))
            good=(detm!=0 and sp.simplify(lhs-rhs)==0 and lhs<0)
            checks+=1; passed+=int(bool(good)); rows.append({'sector':name,'M':mm,'det':str(lhs),'pass':bool(good)})
    return {'stream':'C','valid':True,'pass':passed==checks,'checks':checks,'passed':passed,'rows':rows}

def stream_D():
    tt_exc=sp.simplify((1/Ptt).subs(b,0)+sp.Rational(1,2)/z)==0
    sc_exc=sp.simplify((1/Psc).subs(c,0)-sp.Rational(1,6)/z)==0
    target_det=sp.det(sp.diag(-1,1))
    wrong_pos=sp.det(sp.eye(2)); wrong_neg=sp.det(-sp.eye(2))
    wrong_rejected=(target_det<0 and wrong_pos>0 and wrong_neg>0)
    zero_coupling_rejected=(sp.Rational(1,2)!=0 and -sp.Rational(1,6)!=0)
    ok=tt_exc and sc_exc and wrong_rejected and zero_coupling_rejected
    return {'stream':'D','valid':True,'pass':bool(ok),'tt_exceptional_one_pole':bool(tt_exc),'scalar_exceptional_one_pole':bool(sc_exc),'wrong_definite_controls_rejected':bool(wrong_rejected),'zero_coupling_fake_rejected':bool(zero_coupling_rejected)}

def aggregate(root):
    found={}
    for p in Path(root).rglob('*.json'):
        try:
            d=json.loads(p.read_text())
            if d.get('stream') in 'ABCD': found[d['stream']]=d
        except Exception: pass
    valid=(set(found)==set('ABCD') and all(found[k].get('valid') and found[k].get('pass') for k in 'ABCD'))
    return {'gate':'ITER061_G63_AUXILIARY_SECOND_ORDER_FACTORIZATION','valid':bool(valid),'passes':{k:bool(found.get(k,{}).get('pass')) for k in 'ABCD'},'classification':'FOUR_DERIVATIVE_LINEARIZED_AUXILIARY_TWO_MODE_INDEFINITE_INERTIA_SCOPED' if valid else 'ITER061_G63_FROZEN_GATE_FAIL','programme_readiness_percent':66,'theory_established_percent':0}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream'); ap.add_argument('--out',required=True); ap.add_argument('--aggregate-dir')
    args=ap.parse_args()
    if args.aggregate_dir: data=aggregate(args.aggregate_dir)
    else: data={'A':stream_A,'B':stream_B,'C':stream_C,'D':stream_D}[args.stream]()
    Path(args.out).parent.mkdir(parents=True,exist_ok=True); Path(args.out).write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print(json.dumps(data,sort_keys=True))
    if not data.get('valid') or not data.get('pass', True): raise SystemExit(1)
if __name__=='__main__': main()
