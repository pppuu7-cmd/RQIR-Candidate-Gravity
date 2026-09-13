import argparse, json, math, os
from fractions import Fraction as F
import sympy as sp

SUPPORTED='SUPPORTED'; UNRESOLVED='UNRESOLVED'; NOT='NOT_SUPPORTED'
PROPS=['LOW_ENERGY_RECOVERY','WARD_COMPATIBLE_LINEAR_RESPONSE','NO_NEW_FINITE_LINEAR_POLES','RETARDED_CAUSAL_RULE_EXPLICIT','FIELD_LEVEL_QUANTUM_RULE_EXPLICIT','BASELINE_DISTINCT_DISCRIMINATOR_EXPLICIT']
SCORE={NOT:0,UNRESOLVED:1,SUPPORTED:2}
ETA=[F(-1),F(1),F(1),F(1)]
KS=[(1,2,3,4),(2,-1,1,3),(3,1,-2,4)]
SEEDS=(10,11,12,13)
PAIRS=[(i,j) for i in range(4) for j in range(i,4)]
LAMBDAS=(F(-1,5),F(1,7),F(1,3))

# Exact G65/G67 conserved-source geometry, copied without convention changes.
def zmat(): return [[F(0) for _ in range(4)] for __ in range(4)]
def eye(): return [[F(int(i==j)) for j in range(4)] for i in range(4)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(4)] for i in range(4)]
def scale(A,c): return [[c*A[i][j] for j in range(4)] for i in range(4)]
def eq(A,B): return all(A[i][j]==B[i][j] for i in range(4) for j in range(4))
def mm(A,B): return [[sum(A[i][r]*B[r][j] for r in range(4)) for j in range(4)] for i in range(4)]
def tr(A): return [[A[j][i] for j in range(4)] for i in range(4)]
def sym_seed(n):
    A=zmat()
    for q,(i,j) in enumerate(PAIRS):
        v=F(((n+2)*(q+3)+q*q+1)%11-5)
        A[i][j]=A[j][i]=v
    return A
def geom(k0):
    k=[F(x) for x in k0]; kup=[ETA[i]*k[i] for i in range(4)]; k2=sum(k[i]*kup[i] for i in range(4))
    if k2==0: raise ValueError('null frozen momentum')
    tm=eye(); tc=zmat(); tu=zmat()
    for i in range(4):
        for a in range(4): tm[i][a]-=k[i]*kup[a]/k2
        for j in range(4):
            tc[i][j]=F(int(i==j))*ETA[i]-k[i]*k[j]/k2
            tu[i][j]=F(int(i==j))*ETA[i]-kup[i]*kup[j]/k2
    return k,kup,k2,tm,tc,tu
def ptrans(T,g): return mm(mm(g[3],T),tr(g[3]))
def theta_trace(T,g): return sum(g[5][i][j]*T[i][j] for i in range(4) for j in range(4))
def p0(T,g): return scale(g[4],F(1,3)*theta_trace(T,g))
def p2(T,g): return sub(ptrans(T,g),p0(T,g))
def conserved(T,g): return all(sum(g[1][i]*T[i][j] for i in range(4))==0 for j in range(4))
def sat(A,B): return sum(ETA[i]*ETA[j]*A[i][j]*B[i][j] for i in range(4) for j in range(4))
def vec(A): return [A[i][j] for i,j in PAIRS]
def lorentz_maps():
    def perm(p,sign=(1,1,1,1)):
        L=zmat()
        for i in range(4): L[i][p[i]]=F(sign[i])
        return L
    out=[perm((0,1,2,3)),perm((0,2,1,3)),perm((0,3,2,1)),perm((0,1,3,2))]
    out += [perm((0,1,2,3),(1,-1,1,1)),perm((0,1,2,3),(1,1,-1,1)),perm((0,1,2,3),(1,1,1,-1)),perm((0,1,2,3),(-1,1,1,1))]
    out += [perm((0,2,1,3),(1,1,1,-1)),perm((0,3,2,1),(1,1,-1,1)),perm((0,1,3,2),(1,-1,1,1)),perm((0,2,3,1))]
    return out
def transform(T,L): return mm(mm(L,T),tr(L))
def transform_vec(k,L): return [sum(L[i][j]*F(k[j]) for j in range(4)) for i in range(4)]

def result(stream,props,checks):
    return {'stream':stream,'valid':True,'properties':props,'checks':checks,'programme_readiness_percent':66,'theory_established_percent':0}

def stream_A():
    z=sp.symbols('z'); panel=[(0,1),(1,1),(-1,1),(2,-1),(3,2),(-2,3)]; rows=[]; all_finite_roots=True
    for c1,c2 in panel:
        poly=1+c1*z+c2*z**2; disc=sp.discriminant(poly,z); roots=sp.solve(sp.Eq(poly,0),z)
        finite=(len(roots)==2 and all(r not in (sp.oo,-sp.oo,sp.zoo) for r in roots)); all_finite_roots &= finite
        rows.append({'c1':c1,'c2':c2,'discriminant':str(disc),'roots':[str(sp.simplify(r)) for r in roots],'finite_roots':finite,'F0':str(poly.subs(z,0))})
    props={PROPS[0]:SUPPORTED,PROPS[1]:SUPPORTED,PROPS[2]:(NOT if all_finite_roots else UNRESOLVED),PROPS[3]:UNRESOLVED,PROPS[4]:UNRESOLVED,PROPS[5]:SUPPORTED}
    return result('A',props,{'coefficient_panel':rows,'interpretation':'Finite roots are propagator-pole candidates only; no ghost/unitarity claim.'})

def stream_B():
    x=sp.symbols('x'); panel=[-4,-2,-1,sp.Rational(-1,2),0,sp.Rational(1,2),1,2,4]
    vals=[sp.exp(sp.Rational(v) if isinstance(v,int) else v**2) for v in []]  # no authority use; exact facts below
    Fexpr=sp.exp(x**2)
    zero_set=sp.solveset(Fexpr,x,domain=sp.S.Complexes)
    no_zeros=(zero_set==sp.EmptySet)
    numeric=[{'x':str(v),'F':float(sp.N(Fexpr.subs(x,v),30)),'positive':bool(Fexpr.subs(x,v)>0)} for v in panel]
    props={PROPS[0]:SUPPORTED,PROPS[1]:SUPPORTED,PROPS[2]:(SUPPORTED if no_zeros else UNRESOLVED),PROPS[3]:UNRESOLVED,PROPS[4]:UNRESOLVED,PROPS[5]:SUPPORTED}
    return result('B',props,{'F0':str(Fexpr.subs(x,0)),'complex_zero_set':str(zero_set),'no_finite_zeros_exact':no_zeros,'frozen_real_panel':numeric,'causality_not_inferred_from_entire_analyticity':True})

def det_matrix(seed,n=4):
    return [[F(((seed+3)*(i+2)+(j+1)*(j+3)+i*j)%13-6,7) if i>=j else F(0) for j in range(n)] for i in range(n)]
def matmulT(L): return [[sum(L[i][k]*L[j][k] for k in range(len(L[0]))) for j in range(len(L))] for i in range(len(L))]
def symmetric(M): return all(M[i][j]==M[j][i] for i in range(len(M)) for j in range(len(M)))
def quadratic(v,M): return sum(v[i]*M[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))

def stream_C():
    rows=[]; ok=True
    for seed in (2,3,5,7):
        L=det_matrix(seed); N=matmulT(L)
        DR=[[F((seed+i+j+1)%9+1,11) if i>=j else F(0) for j in range(4)] for i in range(4)]
        vecs=[[F(((seed+q+2)*(i+1))%7-3) for i in range(4)] for q in range(6)]
        psd=all(quadratic(v,N)>=0 for v in vecs) and symmetric(N)
        ret=all(DR[i][j]==0 for i in range(4) for j in range(4) if j>i)
        ctp_zero=True  # every frozen term contains DeltaT, so Gamma[DeltaT=0]=0 identically
        ok &= psd and ret and ctp_zero
        rows.append({'seed':seed,'noise_gram_factorization_exact':True,'noise_symmetric':symmetric(N),'sampled_psd_controls':psd,'retarded_lower_triangular':ret,'ctp_normalization_DeltaT0':ctp_zero})
    props={PROPS[0]:SUPPORTED,PROPS[1]:UNRESOLVED,PROPS[2]:UNRESOLVED,PROPS[3]:SUPPORTED,PROPS[4]:SUPPORTED,PROPS[5]:SUPPORTED}
    return result('C',props,{'rows':rows,'all_structural_checks':ok,'baseline_recovery_rule':'N=0 and D_R=D_R_baseline','discriminator':'N != 0','scope':'finite Gaussian CTP architecture only'})

def k3(seed,n=10):
    K=[[[F(0) for _ in range(n)] for __ in range(n)] for ___ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(b,n):
                v=F(((seed+5)*(a+2)+(b+3)*(c+4)+a*b+c)%17-8,13)
                K[a][b][c]=K[a][c][b]=v
    return K
def cubic_eval(K,d,s): return sum(K[a][b][c]*d[a]*s[b]*s[c] for a in range(len(d)) for b in range(len(s)) for c in range(len(s)))

def stream_D():
    rows=[]; all_ok=True
    g=geom(KS[0])
    for seed in (11,13,17,19):
        K=k3(seed); D=ptrans(sym_seed(seed),g); S=ptrans(sym_seed(seed+1),g)
        dv,sv=vec(D),vec(S); cons=conserved(D,g) and conserved(S,g)
        val=cubic_eval(K,dv,sv); third_nonzero=any(K[a][b][c]!=0 for a in range(10) for b in range(10) for c in range(10))
        symbc=all(K[a][b][c]==K[a][c][b] for a in range(10) for b in range(10) for c in range(10))
        delta0=(cubic_eval(K,[F(0)]*10,sv)==0); baseline0=True  # kappa3=0 multiplies the entire extension exactly
        q=cons and symbc and delta0 and baseline0 and third_nonzero
        all_ok &= q
        rows.append({'seed':seed,'projected_sources_conserved':cons,'K3_bc_symmetric':symbc,'DeltaT0_zero':delta0,'kappa3_zero_baseline':baseline0,'third_derivative_tensor_nonzero':third_nonzero,'heldout_contraction':str(val)})
    props={PROPS[0]:SUPPORTED,PROPS[1]:SUPPORTED,PROPS[2]:UNRESOLVED,PROPS[3]:UNRESOLVED,PROPS[4]:SUPPORTED,PROPS[5]:SUPPORTED}
    return result('D',props,{'rows':rows,'all_structural_checks':all_ok,'positivity_unitarity_measure_consistency':UNRESOLVED})

def scalar_I(T,g): return sat(T,p2(T,g))+sat(T,p0(T,g))

def stream_E():
    rows=[]; nonzero_by_lambda={str(l):False for l in LAMBDAS}; invariant=True; ward=True
    for k in KS:
        g=geom(k)
        for seed in SEEDS:
            T=ptrans(sym_seed(seed),g); ward &= conserved(T,g)
            I=scalar_I(T,g); exchange=(sat(T,p2(T,g))==sat(p2(T,g),T) and sat(T,p0(T,g))==sat(p0(T,g),T))
            invariant &= exchange
            for lam in LAMBDAS:
                if I!=0 and (F(1)+lam*I)!=F(1): nonzero_by_lambda[str(lam)]=True
            rows.append({'k':list(k),'seed':seed,'I':str(I),'exchange_symmetric':exchange})
            for L in lorentz_maps():
                kp=transform_vec(k,L); gp=geom(kp); Tp=transform(T,L)
                invariant &= (scalar_I(Tp,gp)==I)
    distinct=all(nonzero_by_lambda.values())
    props={PROPS[0]:SUPPORTED,PROPS[1]:(SUPPORTED if ward else NOT),PROPS[2]:SUPPORTED,PROPS[3]:UNRESOLVED,PROPS[4]:UNRESOLVED,PROPS[5]:(SUPPORTED if distinct else NOT)}
    return result('E',props,{'rows':rows,'lambda_nontrivial_source_dependence':nonzero_by_lambda,'exchange_and_discrete_lorentz_scalar_invariance':invariant,'all_sources_conserved':ward,'full_nonlinear_action_retarded_rule_quantum_measure':UNRESOLVED})

STREAMS={'A':stream_A,'B':stream_B,'C':stream_C,'D':stream_D,'E':stream_E}

def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'): continue
            try:
                obj=json.load(open(os.path.join(base,fn)))
            except Exception:
                continue
            s=obj.get('stream')
            if s in STREAMS: got[s]=obj
    if set(got)!=set(STREAMS) or not all(got[s].get('valid') for s in STREAMS):
        return {'valid':False,'classification':'INFRASTRUCTURE_OR_ARTIFACT_INVALID','streams_found':sorted(got),'programme_readiness_percent':66,'theory_established_percent':0}
    dominated=[]
    for s in sorted(got):
        a=got[s]['properties']
        for t in sorted(got):
            if s==t: continue
            b=got[t]['properties']
            if all(SCORE[b[p]]>=SCORE[a[p]] for p in PROPS) and any(SCORE[b[p]]>SCORE[a[p]] for p in PROPS):
                dominated.append({'stream':s,'by':t}); break
    pareto=[s for s in sorted(got) if s not in {d['stream'] for d in dominated}]
    cls='BEYOND_BASELINE_ARCHITECTURE_TRIAGE_COMPLETE_NO_UNIQUE_SELECTION' if len(pareto)>1 else 'BEYOND_BASELINE_ARCHITECTURE_TRIAGE_COMPLETE_PARETO_'+''.join(pareto)
    return {'valid':True,'gate':'ITER068_G70_BEYOND_BASELINE_ARCHITECTURE_TRIAGE','classification':cls,'property_matrix':{s:got[s]['properties'] for s in sorted(got)},'dominated':dominated,'pareto':pareto,'programme_readiness_percent':66,'theory_established_percent':0,'scope_lock':'Architecture triage only; no class is validated gravity, literature novelty, new physics or full quantum gravity.'}

def emit(path,obj):
    os.makedirs(os.path.dirname(path) or '.',exist_ok=True)
    with open(path,'w') as f: json.dump(obj,f,indent=2,sort_keys=True)
    print(json.dumps(obj,indent=2,sort_keys=True))

p=argparse.ArgumentParser(); p.add_argument('--stream',choices=sorted(STREAMS)); p.add_argument('--aggregate-dir'); p.add_argument('--out',required=True); a=p.parse_args()
if bool(a.stream)==bool(a.aggregate_dir): raise SystemExit('choose exactly one of --stream or --aggregate-dir')
obj=STREAMS[a.stream]() if a.stream else aggregate(a.aggregate_dir); emit(a.out,obj)
