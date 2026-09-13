#!/usr/bin/env python3
"""CPI1 exact structural controls. Not a physical RCG-002 model.
Frozen contract: 7be8d9f08eefb38caafe6718a367e5f43f3517e3.
Frozen G72 source: fcecaf0108576c0ab17b5dc3a94eeb3a8cc6dd96,
blob 8f67e57e3399b37f5e2ddb79d756932f7ce3200e.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools as it
import json
import os
from pathlib import Path
import platform
import time
from concurrent.futures import ProcessPoolExecutor
import sympy as S

PREREG = '7be8d9f08eefb38caafe6718a367e5f43f3517e3'
SOURCE = 'fcecaf0108576c0ab17b5dc3a94eeb3a8cc6dd96'

def diff3(expr, variables):
    return S.expand(sum((-1)**(3-sum(bits))*expr.subs(dict(zip(variables,bits)), simultaneous=True)
                        for bits in it.product((0,1),repeat=3)))

def lane_a():
    k, x, y, z, d, s, eps = S.symbols('k x y z d s eps', real=True)
    gamma = lambda u,v: k*(u-v)*((u+v)/2)**2
    cycle = S.factor(gamma(x,y)+gamma(y,z)+gamma(z,x))
    cycle012 = S.simplify(cycle.subs({x:0,y:1,z:2}))
    repaired = k*d*s*s+k*d**3/12
    true_difference = S.expand(k*((s+d/2)**3-(s-d/2)**3)/3)
    theta = S.symbols('theta', real=True)
    M = S.Matrix([[1,1,S.exp(-S.I*theta)],[1,1,1],[S.exp(S.I*theta),1,1]])
    determinant = S.simplify(S.expand_complex(M.det()))
    det012 = S.simplify(determinant.subs(theta,cycle012))
    r1,r2,r3 = S.symbols('r1 r2 r3',real=True)
    N=S.Matrix([[1,r1,r3*S.exp(-S.I*theta)],[r1,1,r2],[r3*S.exp(S.I*theta),r2,1]])
    noise_det=S.simplify(S.expand_complex(N.det()))
    eigenvalues=[]
    # Fixed illustrations only. Exact determinant is controlling.
    for kv in (S.Rational(1,10),S.Integer(1)):
        import numpy as np
        numerical=np.array([[complex(S.N(S.exp(S.I*gamma(i,j).subs(k,kv)),17))
                             for j in (0,1,2)] for i in (0,1,2)])
        eigenvalues.append({'k':str(kv),'eigenvalues':np.linalg.eigvalsh(numerical).tolist()})
    checks={
        'normalization':S.simplify(gamma(x,x))==0,
        'exchange_oddness':S.simplify(gamma(x,y)+gamma(y,x))==0,
        'nonzero_cycle':cycle012 == -k/2,
        'phase_difference_repair_identity':S.expand(repaired-true_difference)==0,
        'triangle_determinant_identity':S.simplify(determinant-(2*S.cos(theta)-2))==0,
        'negative_determinant_form':S.trigsimp(det012+4*S.sin(k/4)**2)==0,
        'noisy_necessary_minor_identity':S.simplify(noise_det-(1-r1*r1-r2*r2-r3*r3+2*r1*r2*r3*S.cos(theta)))==0,
    }
    return {'checks':checks, 'cycle_general':str(cycle),'cycle_012':str(cycle012),
            'determinant':str(det012),'determinant_scaled_series':str(S.series(det012.subs(k,k*eps**3),eps,0,13)),
            'repaired_control':str(repaired),'noisy_minor':str(noise_det),'numerical_illustrations':eigenvalues,
            'scope':'Exact unit-modulus Schur kernel on freely variable histories; not a noisy EFT truncation or a realized source protocol.'}

def g72_kernel():
    # Exact transcription of D1 construction, not the D2 reduced surrogate.
    K={}
    for td,t1,t2 in it.product(range(4),repeat=3):
        v=S.Rational(((td+2)*(t1+3)+(t2+5))%7-3)
        if td<max(t1,t2): v=S.Integer(0)
        K[td,t1,t2]=v
    for (td,t1,t2),v in list(K.items()):
        w=K[td,t2,t1]
        vv=(v+w)/2
        K[td,t1,t2]=K[td,t2,t1]=vv
    return K

def lane_b():
    K=g72_kernel()
    ss=S.symbols('s0:4',real=True)
    V=[S.expand(sum(K[i,j,k]*ss[j]*ss[k] for j,k in it.product(range(4),repeat=2))) for i in range(4)]
    curl=[]
    for i,l in it.combinations(range(4),2):
        c=S.expand(S.diff(V[i],ss[l])-S.diff(V[l],ss[i]))
        curl.append({'i':i,'l':l,'value':str(c),'zero':c==0})
    violations=[{'indices':[i,j,k],'K':str(K[i,j,k]),'K_response_swap':str(K[j,i,k])}
                for i,j,k in it.product(range(4),repeat=3) if K[i,j,k]!=K[j,i,k]]
    # A fully symmetric tensor can have a nonzero unordered triple only when
    # all permutations satisfy latest-response-time support.
    symmetric_allowed=[]
    for triple in it.combinations_with_replacement(range(4),3):
        if all(i>=max(j,k) for i,j,k in set(it.permutations(triple))):
            symmetric_allowed.append(list(triple))
    strict_allowed=[]
    for triple in it.combinations_with_replacement(range(4),3):
        if all(i>max(j,k) for i,j,k in set(it.permutations(triple))): strict_allowed.append(triple)
    s0,s1,d0,d1=S.symbols('s0 s1 d0 d1',real=True)
    D2=d0*s0*s0+2*d0*s0*s1+d1*s1*s1
    d2curl=S.diff(S.diff(D2,d0),s1)-S.diff(S.diff(D2,d1),s0)
    a,b,c,e=S.symbols('a b c e',real=True)
    dcubic=a*d0**3+b*d0**2*d1+c*d0*d1**2+e*d1**3
    response_extra=[S.diff(dcubic,dv).subs({d0:0,d1:0}) for dv in (d0,d1)]
    # Fully symmetric nonlocal positive control: its response is integrable,
    # but its time kernel does not have latest-response support.
    p,q=S.symbols('p q',real=True)
    phi=p*p*q
    control_curl=S.diff(S.diff(phi,p),q)-S.diff(S.diff(phi,q),p)
    checks={
        'g72_nonzero_count_26':sum(v!=0 for v in K.values())==26,
        'g72_sigma_symmetry':all(K[i,j,k]==K[i,k,j] for i,j,k in K),
        'g72_retarded_support':all(v==0 or i>=max(j,k) for (i,j,k),v in K.items()),
        'g72_nonintegrable_response':any(not row['zero'] for row in curl),
        'g72_scalar_ray_matches_A':K[0,0,0]==1,
        'D2_nonzero_curl':d2curl==2*s0,
        'contact_only_symmetric_retarded':symmetric_allowed==[[i,i,i] for i in range(4)],
        'strict_retarded_symmetric_zero':len(strict_allowed)==0,
        'delta_cubic_does_not_change_response':response_extra==[0,0],
        'symmetric_potential_control':control_curl==0,
    }
    return {'checks':checks,'response_V':[str(v) for v in V],'curl':curl,'first_response_swap_violations':violations[:6],
            'response_swap_violation_count':len(violations),'symmetric_retarded_allowed':symmetric_allowed,
            'D2_curl':str(d2curl),'K000':str(K[0,0,0]),
            'kernel_entries':{','.join(map(str,key)):str(value) for key,value in K.items()},
            'scope':'Finite-grid unrestricted-history coherent potential test; not a no-go for open noisy dynamics, contact distributions, or a restricted physical protocol.'}

def lane_c():
    a,b,c,q=S.symbols('a b c q',real=True)
    t=(S.Integer(1),a,b,c)
    def homogeneous(n):
        coeff={}; expr=0
        for indices in it.combinations_with_replacement(range(4),n):
            counts=[indices.count(i) for i in range(4)]
            symbol=S.Symbol('W'+str(n)+'_'+''.join(map(str,indices)),real=True)
            coeff[indices]=symbol
            expr+=symbol*S.prod(t[i]**counts[i]/S.factorial(counts[i]) for i in range(4))
        return S.expand(expr),coeff
    W3,c3=homogeneous(3); W4,c4=homogeneous(4)
    chi3=diff3(W3,(a,b,c)); chi4=diff3(W4,(a,b,c))
    expected4=c4[(0,1,2,3)]+(c4[(1,1,2,3)]+c4[(1,2,2,3)]+c4[(1,2,3,3)])/2
    scaled4=diff3(W4.subs({a:q*a,b:q*b,c:q*c},simultaneous=True),(a,b,c))
    lam,p0,pA,pB,pC,pAB,pAC,pBC=S.symbols('lambda p0 pA pB pC pAB pAC pBC',real=True)
    pair=p0+pA*a+pB*b+pC*c+pAB*a*b+pAC*a*c+pBC*b*c
    phases=pair+lam*a*b*c
    pp={bits:S.Symbol('phi'+''.join(map(str,bits)),real=True) for bits in it.product((0,1),repeat=3)}
    delta=lambda bv,cv:pp[(1,bv,cv)]-pp[(0,bv,cv)]
    conditional=delta(1,1)-delta(1,0)-delta(0,1)+delta(0,0)
    direct=sum((-1)**(3-sum(bits))*v for bits,v in pp.items())
    eta=S.symbols('eta',real=True)
    spectator_pair=a*b*(1+eta*c)
    source_shift=S.expand(diff3(spectator_pair,(a,b,c)))
    # Exact cubic average-derivative identity for the quartic polynomial.
    u,v,w=S.symbols('u v w',real=True)
    avg=S.integrate(S.diff(W4,a,b,c).subs({a:u,b:v,c:w}),(u,0,1),(v,0,1),(w,0,1))
    checks={
        'cubic_trilinear_response':chi3==c3[(1,2,3)],
        'quartic_background_and_repeated_source_terms':S.expand(chi4-expected4)==0,
        'finite_difference_integral_identity':S.expand(avg-chi4)==0,
        'conditional_coherence_expression':S.expand(conditional-direct)==0,
        'pairwise_null_independent_sources':diff3(pair,(a,b,c))==0,
        'unitary_extension_free_connected_phase':diff3(phases,(a,b,c))==lam,
        'all_zero_branch_faces_preserved':all(S.expand((phases-pair).subs(x,0))==0 for x in (a,b,c)),
        'spectator_dependent_pairwise_counterexample':source_shift==eta,
    }
    return {'checks':checks,'chi_cubic':str(chi3),'chi_quartic':str(chi4),'quartic_scaled_differences_fixed_background':str(scaled4),
            'conditional_phase_combination':str(conditional),'free_unitary_chi':str(lam),'spectator_pair_chi':str(source_shift),
            'physical_completion_space':'UNDEFINED_NO_NATIVE_DYNAMICS_AND_SOURCE_QUOTIENT',
            'selector_rank':'UNDEFINED_PHYSICAL_MAP_MISSING',
            'scope':'Conditional source-action identities and operational calibration; W3/W4 and lambda are not candidate-owned gravitational dynamics.'}

def lane_d():
    x,eps,rho=S.symbols('x eps rho',real=True)
    f=S.Function('f')(x); lapse=S.exp(eps*f)
    # ds^2=-N(x)^2 dt^2+dx^2+dy^2+dz^2. Held dust only.
    metric=S.diag(-lapse*lapse,1,1,1); inv=metric.inv()
    coords=S.symbols('t x_dummy y z'); coords=(coords[0],x,coords[2],coords[3])
    def Gamma(a,b,c):
        return S.simplify(sum(inv[a,l]*(S.diff(metric[l,c],coords[b])+S.diff(metric[l,b],coords[c])-S.diff(metric[b,c],coords[l]))/2 for l in range(4)))
    stress=S.zeros(4); stress[0,0]=eps*rho/(lapse*lapse)
    flat_div=S.simplify(sum(S.diff(stress[mu,1],coords[mu]) for mu in range(4)))
    cov_div=S.simplify(flat_div+sum(Gamma(mu,mu,al)*stress[al,1]+Gamma(1,mu,al)*stress[mu,al] for mu,al in it.product(range(4),repeat=2)))
    checks={
        'flat_divergence_zero':flat_div==0,
        'nonlinear_covariant_divergence_nonzero':S.simplify(cov_div-eps**2*rho*S.diff(f,x))==0,
        'flat_metric_control':S.simplify(cov_div.subs(f,S.Integer(0)).doit())==0,
    }
    return {'checks':checks,'metric_lapse':str(lapse),'T00':str(stress[0,0]),'partial_divergence_x':str(flat_div),
            'covariant_divergence_x':str(cov_div),
            'scope':'Exact external-metric held-dust consistency counterexample, not a self-consistent gravity solution; support/apparatus is missing.'}

LANES={'A':lane_a,'B':lane_b,'C':lane_c,'D':lane_d}

def execute(name):
    start=time.time(); result=LANES[name]()
    result.update(lane=name,prereg_commit=PREREG,source_commit=SOURCE,pid=os.getpid(),started_unix=start,finished_unix=time.time())
    result['structural_checks_passed']=all(result['checks'].values())
    return result

def emit(output, result):
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')

def main():
    p=argparse.ArgumentParser(); p.add_argument('--outdir',default='raw');p.add_argument('--lane',choices=LANES);args=p.parse_args()
    out=Path(args.outdir)
    if args.lane:
        results=[execute(args.lane)]
    else:
        with ProcessPoolExecutor(max_workers=4) as executor: results=list(executor.map(execute,LANES))
    for result in results: emit(out/('cpi1_'+result['lane']+'.json'),result)
    summary={'gate':'RCG002-CPI1','prereg_commit':PREREG,'source_commit':SOURCE,
             'python_version':platform.python_version(),'sympy_version':S.__version__,
             'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'lanes':{r['lane']:{'all_checks_passed':r['structural_checks_passed'],'checks':r['checks'],'pid':r['pid'],
                               'started_unix':r['started_unix'],'finished_unix':r['finished_unix']} for r in results},
             'raw_file_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(out.glob('cpi1_[ABCD].json'))},
             'physical_map_status':'BLOCKED_REQUIRES_NEW_NONLINEAR_SOURCE_STATE_EVOLUTION_PRINCIPLE',
             'naive_exact_phase_promotion':'FAIL_SCOPED_UNRESTRICTED_HISTORY_NOISELESS_KERNEL',
             'selector_rank':'UNDEFINED_PHYSICAL_MAP_MISSING','readiness_percent':66,'theory_established_percent':0}
    summary['structural_checks_passed']=all(r['structural_checks_passed'] for r in results)
    emit(out/'cpi1_summary.json',summary)
    print(json.dumps(summary,indent=2,sort_keys=True))
    if not summary['structural_checks_passed']: raise SystemExit(2)

if __name__=='__main__': main()
