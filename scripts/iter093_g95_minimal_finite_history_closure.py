#!/usr/bin/env python3
import argparse, json, itertools, random
from pathlib import Path
import sympy as sp

TIMES=(0,1,2)
PAIRS={i:[(j,k) for j in range(i+1) for k in range(j,i+1)] for i in TIMES}
VARS=[]
for i in TIMES:
    for j,k in PAIRS[i]: VARS.append((i,j,k))
SYMS=sp.symbols('c0:'+str(len(VARS)))
VMAP=dict(zip(VARS,SYMS))
d=sp.symbols('d0:3'); s=sp.symbols('s0:3')
G=sum(VMAP[i,j,k]*d[i]*s[j]*s[k] for i,j,k in VARS)


def coeff_equations(poly, gens):
    p=sp.Poly(sp.expand(poly), *gens)
    return [sp.expand(c) for c in p.coeffs() if c!=0]

def structural_equations():
    eq=[]
    # affine common shifts
    for q in ((1,1,1),(0,1,2)):
        shifted=G.subs({s[a]:s[a]+q[a] for a in TIMES}, simultaneous=True)
        eq += coeff_equations(shifted-G, d+s)
    # pairwise weak-field preservation: one-cell histories => c_{m;mm}=0
    for m in TIMES:
        if (m,m,m) in VMAP: eq.append(VMAP[m,m,m])
    return [sp.expand(e) for e in eq]

def nullspace():
    eq=structural_equations()
    A,b=sp.linear_eq_to_matrix(eq,SYMS)
    assert all(v==0 for v in b)
    return A, A.nullspace()

def vec_to_expr(v):
    return sp.expand(sum(v[n]*d[i]*s[j]*s[k] for n,(i,j,k) in enumerate(VARS)))

def gamma_eval(expr,x,y):
    subs={d[i]:sp.Rational(x[i]-y[i]) for i in TIMES}
    subs.update({s[i]:sp.Rational(x[i]+y[i],2) for i in TIMES})
    return sp.simplify(expr.subs(subs))

H=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]

def cocycle_failures(expr,limit=8):
    bad=[]
    for x,y,z in itertools.product(H,repeat=3):
        val=sp.simplify(gamma_eval(expr,x,y)+gamma_eval(expr,y,z)-gamma_eval(expr,x,z))
        if val!=0:
            bad.append({'x':x,'y':y,'z':z,'value':str(val)})
            if len(bad)>=limit: break
    return bad

def phase_reconstruct(expr):
    base=H[0]
    phi={h:gamma_eval(expr,h,base) for h in H}
    bad=[]
    for x,y in itertools.product(H,repeat=2):
        if sp.simplify(gamma_eval(expr,x,y)-(phi[x]-phi[y]))!=0:
            bad.append((x,y));
            if len(bad)>=8: break
    return phi,bad

def connected(expr):
    # mixed derivative on embedding d2=A, s0=B, s1=C, others zero
    A,B,C=sp.symbols('A B C')
    emb=sp.expand(expr.subs({d[0]:0,d[1]:0,d[2]:A,s[0]:B,s[1]:C,s[2]:0}))
    mixed=sp.diff(emb,A,B,C)
    distinct=any(v!=0 and j!=k for v,(i,j,k) in zip([sp.expand(expr).coeff(VMAP.get((i,j,k),0)) if False else 0 for i,j,k in VARS],VARS))
    # use coefficient dictionary directly from expression polynomial
    P=sp.Poly(expr,*(d+s))
    cross=False
    for i,j,k in VARS:
        mon=d[i]*s[j]*s[k]
        if j!=k and sp.expand(expr).coeff(mon)!=0: cross=True
    return cross or mixed!=0, str(sp.simplify(mixed))

def lane_A():
    M,ns=nullspace(); basis=[str(vec_to_expr(v)) for v in ns]
    con=[]
    for v in ns:
        con.append(connected(vec_to_expr(v))[0])
    return {'lane':'A','n_variables':len(SYMS),'constraint_rank':int(M.rank()),'nullity':len(ns),'basis':basis,'connected_basis_flags':con,'structural_connected_exists':any(con)}

def lane_B():
    _,ns=nullspace(); survivors=[]; rejected=[]
    for idx,v in enumerate(ns):
        expr=vec_to_expr(v); bad=cocycle_failures(expr)
        if bad: rejected.append({'basis':idx,'counterexamples':bad})
        else: survivors.append(idx)
    return {'lane':'B','structural_nullity':len(ns),'cocycle_survivor_basis_indices':survivors,'rejected':rejected,'survivor_dimension_upper_bound':len(survivors)}

def lane_C():
    _,ns=nullspace(); checks=[]
    for idx,v in enumerate(ns):
        expr=vec_to_expr(v); phi,bad=phase_reconstruct(expr)
        # exact phase reconstruction is the decisive rank-one test
        checks.append({'basis':idx,'rank_one_phase_reconstruction':not bad,'bad_pairs':bad,'phi':[str(phi[h]) for h in H]})
    rng=random.Random(9503); combos=[]
    if ns:
        for _ in range(5):
            coeff=[sp.Rational(rng.randint(-3,3),rng.randint(1,4)) for _ in ns]
            if all(c==0 for c in coeff): coeff[0]=1
            expr=sp.expand(sum(c*vec_to_expr(v) for c,v in zip(coeff,ns)))
            _,bad=phase_reconstruct(expr)
            combos.append({'coeff':[str(c) for c in coeff],'rank_one':not bad,'bad_pairs':bad})
    return {'lane':'C','structural_nullity':len(ns),'basis_phase_checks':checks,'deterministic_combo_checks':combos}

def lane_D():
    x0,x1,x2,y0,y1,y2,k=sp.symbols('x0 x1 x2 y0 y1 y2 k')
    # local cubic potential difference on last cell
    Vdiff=k*(x2**3-y2**3)/3
    dd=x2-y2; ss=(x2+y2)/2
    one_delta=k*dd*ss**2
    completed=sp.expand(one_delta+k*dd**3/12)
    coherent_identity=sp.simplify(Vdiff-completed)==0
    # explicit cocycle fail for one-delta control at histories 0,1,2 in scalar last-cell values
    def od(a,b): return sp.expand(k*(a-b)*((a+b)/2)**2)
    fail=sp.simplify(od(0,1)+od(1,2)-od(0,2))
    zero_pass=(len(cocycle_failures(sp.Integer(0)))==0)
    M,ns=nullspace()
    # without affine shifts, only three diagonal constraints
    eq=[VMAP[m,m,m] for m in TIMES if (m,m,m) in VMAP]
    M0,_=sp.linear_eq_to_matrix(eq,SYMS)
    return {'lane':'D','coherent_local_potential_identity':coherent_identity,'one_delta_control_cocycle_residual_0_1_2':str(fail),'one_delta_control_fails_for_nonzero_k':fail!=0,'zero_passes_cocycle':zero_pass,'zero_is_connected_witness':False,'nullity_with_conservation':len(ns),'nullity_without_affine_conservation':len(SYMS)-int(M0.rank()),'conservation_constraint_has_effect':(len(SYMS)-int(M0.rank()))>len(ns)}

def aggregate(inputs):
    by={x['lane']:x for x in inputs}
    req=set('ABCD')
    if set(by)!=req: return {'classification':'INFRASTRUCTURE_OR_IMPLEMENTATION_FAIL','reason':'missing lanes','lanes':sorted(by)}
    A,B,C,D=by['A'],by['B'],by['C'],by['D']
    controls=bool(D['coherent_local_potential_identity'] and D['one_delta_control_fails_for_nonzero_k'] and D['zero_passes_cocycle'] and D['conservation_constraint_has_effect'])
    if not controls: cls='INFRASTRUCTURE_OR_IMPLEMENTATION_FAIL'
    elif not A['structural_connected_exists']: cls='BLOCKED_MINIMAL_FINITE_HISTORY_STRUCTURAL_SPACE_EMPTY_SCOPED'
    elif B['survivor_dimension_upper_bound']==0: cls='NEGATIVE_MINIMAL_FINITE_HISTORY_NOISELESS_CLOSURE_OBSTRUCTED_SCOPED'
    else:
        surviving=B['cocycle_survivor_basis_indices']
        cgood={q['basis'] for q in C['basis_phase_checks'] if q['rank_one_phase_reconstruction']}
        cls='PASS_EXISTENCE_MINIMAL_FINITE_HISTORY_COHERENT_CLOSURE_SCOPED' if set(surviving)&cgood else 'INFRASTRUCTURE_OR_IMPLEMENTATION_FAIL'
    return {'classification':cls,'controls_valid':controls,'lane_summaries':by,'scope_lock':'finite 3-cell cubic one-Delta noiseless model only','readiness_percent':66,'theory_established_percent':0}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=list('ABCD')); ap.add_argument('--aggregate',nargs='*'); ap.add_argument('--out',required=True); args=ap.parse_args()
    if args.lane:
        data={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}[args.lane]()
    else:
        ins=[]
        for p in args.aggregate or []:
            ins.append(json.loads(Path(p).read_text()))
        data=aggregate(ins)
    Path(args.out).write_text(json.dumps(data,indent=2,sort_keys=True,default=str)+'\n')
    print(json.dumps(data,indent=2,sort_keys=True,default=str))
if __name__=='__main__': main()
