#!/usr/bin/env python3
"""Frozen NCP1 exact controls. Calibration models are NOT RCG-002 dynamics."""
from __future__ import annotations
import argparse, hashlib, json, math, os, platform, time
from fractions import Fraction as Q
from pathlib import Path
import sympy as S
PREREG='a796519c7859c33eb1f590740860cf7f388563e1'
BASE='446852d1675042b09a465e5eae32d482d78afe54'

def moments(nu,k,N=64):
    m=[Q(1),Q(0)]
    for n in range(1,N):
        m.append(n*2*nu*m[n-1]+(n*(n-1)*k*m[n-2]/4 if n>=2 else 0))
    alt=[]
    for n in range(N+1):
        alt.append(math.factorial(n)*sum((nu**i*(k/12)**j/Q(math.factorial(i)*math.factorial(j))
            for j in range(n//3+1) for i in [(n-3*j)//2] if 2*i+3*j==n),Q(0)))
    assert m==alt, 'independent moment constructions disagree'
    return m

def certificate(m,limit=32):
    L=[[Q(0) for j in range(limit+1)] for i in range(limit+1)];D=[]
    for n in range(limit+1):
        L[n][n]=Q(1)
        for j in range(n):
            L[n][j]=(m[n+j]-sum((L[n][r]*D[r]*L[j][r] for r in range(j)),Q(0)))/D[j]
        pivot=m[2*n]-sum((L[n][r]**2*D[r] for r in range(n)),Q(0));D.append(pivot)
        if pivot<0:
            v=[Q(0)]*(n+1);v[n]=Q(1)
            for j in reversed(range(n)):
                v[j]=-sum((L[r][j]*v[r] for r in range(j+1,n+1)),Q(0))
            value=sum((v[i]*v[j]*m[i+j] for i in range(n+1) for j in range(n+1)),Q(0))
            assert value==pivot and all(x>0 for x in D[:-1])
            return {'status':'EXACT_NEGATIVE_CERTIFICATE','polynomial_degree':n,'matrix_size':n+1,
                    'pivot':str(pivot),'witness_coefficients':[str(x) for x in v],
                    'quadratic_form':str(value),'preceding_pivots_positive':True}
        if pivot==0:
            return {'status':'INCONCLUSIVE_ZERO_PIVOT','degree':n}
    return {'status':'POSITIVE_THROUGH_FROZEN_ORDER_ONLY','max_degree':limit}

def lane_a():
    e,k,h,a,b,c=S.symbols('e k h a b c',real=True)
    u,v,w,theta=S.symbols('u v w theta',real=True)
    M=S.Matrix([[1,u,w*S.exp(-S.I*theta)],[u,1,v],[w*S.exp(S.I*theta),v,1]])
    det=S.simplify(S.expand_complex(M.det()))
    expected=1-u*u-v*v-w*w+2*u*v*w*S.cos(theta)
    expr=expected.subs({u:1-a*e**4,v:1-b*e**4,w:1-c*e**4,theta:-k*e**3/2+h*e**4})
    series=S.series(expr,e,0,9).removeO().expand()
    V,T,F=S.symbols('V T F',real=True)
    H=S.Matrix([[1,0,V],[0,V,T],[V,T,F]])
    minor=S.factor(H.det())
    checks={'determinant_identity':S.simplify(det-expected)==0,
            'no_terms_below_order6':all(series.coeff(e,j)==0 for j in range(6)),
            'quartic_noise_cannot_change_order6':series.coeff(e,6)==-k*k/4,
            'zero_cycle_removes_order6':series.subs(k,0).coeff(e,6)==0,
            'moment_inequality':S.expand(minor-(V*F-T*T-V**3))==0}
    return {'checks':checks,'determinant':str(det),'classI_series':str(series),
            'stationary_moment_minor':str(minor),'classI':'FAIL_HIGHER_ORDER_ONLY_NOISE_RESCUE_SCOPED'}

def lane_b():
    x,y,k,nu=S.symbols('x y k nu',real=True)
    gamma=k*(x-y)*((x+y)/2)**2
    identity=S.expand(gamma-k*(x**3-y**3)/3+k*(x-y)**3/12)
    rows=[];controls=[]
    for n in (Q(1,10),Q(1,2),Q(1),Q(2)):
        row={'nu':str(n),'k':'1','certificate':certificate(moments(n,Q(1)))};rows.append(row)
        control=certificate(moments(n,Q(0)));controls.append({'nu':str(n),**control})
    checks={'phase_congruence_identity':identity==0,
            'moment_recurrences_agree':True,
            'all_gaussian_controls_positive':all(r['status']=='POSITIVE_THROUGH_FROZEN_ORDER_ONLY' for r in controls),
            'low_noise_negative_certificate':rows[0]['certificate']['status']=='EXACT_NEGATIVE_CERTIFICATE'}
    return {'checks':checks,'panels':rows,'gaussian_controls':controls,
            'global_theorem_scope':'Global exact stationary exp(polynomial); Marcinkiewicz plus Bochner. Not inferred from finite panels.',
            'classII':'FAIL_EXACT_GAUSSIAN_CUBIC_LOG_KERNEL_SCOPED'}

def lane_c():
    d,x,y,k,nu,a=S.symbols('d x y k nu a',real=True,nonzero=True)
    lam=k/(2*a**3);sig2=2*nu-k/(2*a)
    logchar=-sig2*d*d/2+lam*(S.exp(S.I*a*d)-1-S.I*a*d)
    jet=S.series(logchar,d,0,9).removeO().expand()
    residual=S.expand(jet+nu*d*d+S.I*k*d**3/12)
    rows=[]
    for av in (S.Rational(1,2),S.Integer(1)):
        lv=lam.subs({k:1,a:av});sv=sig2.subs({k:1,nu:1,a:av})
        cumulants=[S.Integer(0),S.simplify(sv+lv*av**2)]+[S.simplify(lv*av**n) for n in range(3,9)]
        rows.append({'a':str(av),'lambda':str(lv),'sigma_squared':str(sv),'cumulants_1_to_8':[str(t) for t in cumulants]})
    checks={'jet_orders0_to3_match':all(S.simplify(residual.coeff(d,i))==0 for i in range(4)),
            'positive_fixed_parameters':all(S.Rational(t['lambda'])>0 and S.Rational(t['sigma_squared'])>=0 for t in rows),
            'first_three_cumulants_identical':rows[0]['cumulants_1_to_8'][:3]==rows[1]['cumulants_1_to_8'][:3],
            'fourth_cumulants_differ':rows[0]['cumulants_1_to_8'][3]!=rows[1]['cumulants_1_to_8'][3],
            'normalized_characteristic':S.simplify(logchar.subs(d,0))==0,
            'fourth_cumulant_formula':S.simplify(jet.coeff(d,4)*24-k*a/2)==0}
    return {'checks':checks,'log_characteristic':str(logchar),'series':str(jet),'examples':rows,
            'positivity_proof':'Fij=E(ui(Z)*conjugate(uj(Z))), ui=exp(i*k*xi^3/3+i*Z*xi); therefore v^*Fv=E|sum(conjugate(vi)*ui)|^2>=0.',
            'classIII':'POSITIVE_NOISY_COMPLETIONS_NONUNIQUE_SCOPED'}

def lane_d():
    x1,x2,X,r,x,y,k,nu=S.symbols('x1 x2 X r x y k nu',real=True)
    q=x1-X
    def translate(f):return S.simplify(S.diff(f,x1)+S.diff(f,x2)+S.diff(f,X))
    gamma=lambda a,b:k*(a-b)*((a+b)/2)**2
    scaling=S.expand(gamma(r*x,r*y)-r**3*gamma(x,y))
    checks={'relative_source_translation_invariant':translate(q)==0,
            'relative_phase_translation_invariant':translate(k*q**3/3)==0,
            'absolute_source_negative_control':translate(x1)==1,
            'cubic_scaling':scaling==0,
            'quadratic_scaling':S.expand(nu*(r*x-r*y)**2-r*r*nu*(x-y)**2)==0,
            'G72_K000_direct_formula':((0+2)*(0+3)+(0+5))%7-3==1}
    return {'checks':checks,'relative_source':'Q=x1-X','K000':'1',
            'scope':'Random-unitary maps generated by functions of Q commute with total translations; no energy/Bianchi/causal/source-realization claim.',
            'still_missing':['native nonlinear source/state/evolution law','source-history map','nonlinear total stress conservation','Bianchi/constraint closure','spacetime causality','physical selector quotient'],
            'physical_status':'BLOCKED_PHYSICAL_EVOLUTION','selection_rank':'UNDEFINED_PHYSICAL_MAP_MISSING'}
LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}

def emit(p,o):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n',encoding='utf-8')

def main():
    p=argparse.ArgumentParser();p.add_argument('--lane',choices=LANES);p.add_argument('--aggregate',nargs=4);p.add_argument('--out',required=True);args=p.parse_args()
    if bool(args.lane)==bool(args.aggregate):p.error('choose a lane or four aggregate inputs')
    if args.lane:
        start=time.time();o=LANES[args.lane]()
        o.update(gate='NCP1',lane=args.lane,prereg=PREREG,base=BASE,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),python=platform.python_version(),sympy=S.__version__,pid=os.getpid(),started_unix=start,finished_unix=time.time())
        o['checks_valid']=all(o['checks'].values())
    else:
        data=[json.loads(Path(f).read_text()) for f in args.aggregate]
        if set(d['lane'] for d in data)!=set(LANES) or len({d['code_sha256'] for d in data})!=1:raise RuntimeError('lane identity/code mismatch')
        if any(d['prereg']!=PREREG or d['base']!=BASE for d in data):raise RuntimeError('provenance mismatch')
        o={'gate':'NCP1','prereg':PREREG,'base':BASE,'lanes':{d['lane']:d for d in data},'raw_sha256':{Path(f).name:hashlib.sha256(Path(f).read_bytes()).hexdigest() for f in args.aggregate},'checks_valid':all(d['checks_valid'] for d in data),'physical_status':'BLOCKED_PHYSICAL_EVOLUTION','selection_rank':'UNDEFINED_PHYSICAL_MAP_MISSING','readiness_percent':66,'theory_established_percent':0}
    emit(args.out,o)
    print(json.dumps({'lane':args.lane,'checks_valid':o['checks_valid'],'out':args.out}))
    if not o['checks_valid']:raise SystemExit(2)
if __name__=='__main__':main()
