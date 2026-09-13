#!/usr/bin/env python3
import argparse, json, random
from pathlib import Path
import sympy as sp

ETA = sp.diag(-1,1,1,1)
QREF = sp.Matrix([1,-2,2,-1])


def sym_matrix(vals):
    H=sp.zeros(4); k=0
    for i in range(4):
        for j in range(i,4):
            H[i,j]=H[j,i]=sp.Rational(vals[k]); k+=1
    return H


def raise2(H): return ETA*H*ETA

def bilinear_terms(p,H,K):
    p=sp.Matrix(p); pu=ETA*p; Hu=raise2(H); Ku=raise2(K)
    p2=(p.T*ETA*p)[0]
    ta=p2*sum(H[i,j]*Ku[i,j] for i in range(4) for j in range(4))
    vH=[sum(p[m]*Hu[m,n] for m in range(4)) for n in range(4)]
    vK=[sum(p[m]*Ku[m,n] for m in range(4)) for n in range(4)]
    wH=[sum(pu[l]*H[l,n] for l in range(4)) for n in range(4)]
    wK=[sum(pu[l]*K[l,n] for l in range(4)) for n in range(4)]
    tb=(sum(vH[n]*wK[n] for n in range(4))+sum(vK[n]*wH[n] for n in range(4)))/2
    trH=sum(ETA[i,j]*H[i,j] for i in range(4) for j in range(4))
    trK=sum(ETA[i,j]*K[i,j] for i in range(4) for j in range(4))
    divH=sum(p[n]*sum(p[m]*Hu[m,n] for m in range(4)) for n in range(4))
    divK=sum(p[n]*sum(p[m]*Ku[m,n] for m in range(4)) for n in range(4))
    tc=(trH*divK+trK*divH)/2
    td=p2*trH*trK
    return sp.Matrix([sp.simplify(x) for x in (ta,tb,tc,td)])


def B(p,H,K,q=QREF): return sp.simplify((q.T*bilinear_terms(p,H,K))[0])

def gauge(p,xi):
    p=sp.Matrix(p); xi=sp.Matrix(xi)
    return p*xi.T+xi*p.T


def rand_nonnull(rng):
    while True:
        p=[rng.randint(-4,4) or 1 for _ in range(4)]
        if (sp.Matrix(p).T*ETA*sp.Matrix(p))[0] != 0: return p


def rand_H(rng): return sym_matrix([rng.randint(-3,3) for _ in range(10)])

def rand_xi(rng): return [rng.randint(-3,3) or 1 for _ in range(4)]


def constraint_matrix(seed,n=28):
    rng=random.Random(seed); rows=[]
    for _ in range(n):
        p=rand_nonnull(rng); H=rand_H(rng); G=gauge(p,rand_xi(rng))
        rows.append(list(bilinear_terms(p,H,G)))
    return sp.Matrix(rows)


def proportional(v,w):
    idx=next(i for i,x in enumerate(w) if x!=0)
    lam=sp.simplify(v[idx]/w[idx])
    return all(sp.simplify(v[i]-lam*w[i])==0 for i in range(len(w)))


def stream_A():
    M=constraint_matrix(5701,32); ns=M.nullspace(); ok=M.rank()==3 and len(ns)==1 and proportional(ns[0],QREF)
    return {"stream":"A","valid":True,"pass":bool(ok),"rank":int(M.rank()),"nullity":len(ns),"null_ray":[str(x) for x in (ns[0] if ns else [])]}


def stream_B():
    rng=random.Random(5711); good=[]; wrong=[]; qwrong=sp.Matrix([1,-2,2,sp.Rational(-4,5)])
    for _ in range(18):
        p=rand_nonnull(rng); H=rand_H(rng); G=gauge(p,rand_xi(rng))
        good.append(B(p,H,G,QREF)==0)
        wrong.append(B(p,H,G,qwrong)!=0)
    ok=all(good) and any(wrong)
    return {"stream":"B","valid":True,"pass":bool(ok),"heldout_exact_zero":sum(good),"heldout_n":len(good),"wrong_ray_nonzero":sum(wrong)}


def transverse_basis(p):
    pu=(ETA*sp.Matrix(p)).T
    ns=pu.nullspace()
    return [sp.Matrix(v) for v in ns]


def coupling(T,X):
    Xu=raise2(X)
    return sp.simplify(sum(T[i,j]*Xu[i,j] for i in range(4) for j in range(4)))


def make_source(p,rng):
    vs=transverse_basis(p); T=sp.zeros(4)
    for i,v in enumerate(vs):
        for j,w in enumerate(vs):
            coeff=sp.Rational(rng.randint(-3,3) or (1 if i==j else 0))
            if j<i: continue
            if i==j: T += coeff*(v*v.T)
            else: T += coeff*(v*w.T+w*v.T)
    return sp.simplify(T)


def trace(T): return sp.simplify(sum(ETA[i,j]*T[i,j] for i in range(4) for j in range(4)))


def response(T,alpha): return sp.simplify(T-alpha*ETA*trace(T))


def source_residual(p,T,alpha):
    H=response(T,alpha)
    rng=random.Random(99)
    tests=[]
    # Compare B(H,X) to lambda coupling(T,X) on 10 basis tensors, eliminating lambda from first nonzero denominator.
    for k in range(10):
        vals=[0]*10; vals[k]=1; X=sym_matrix(vals)
        tests.append((sp.simplify(B(p,H,X,QREF)),sp.simplify(coupling(T,X))))
    lam=None
    for lhs,rhs in tests:
        if rhs!=0:
            lam=sp.simplify(lhs/rhs); break
    if lam is None: return False,None
    return all(sp.simplify(lhs-lam*rhs)==0 for lhs,rhs in tests),lam


def stream_C():
    rng=random.Random(5721); right=[]; wrong=[]; lambdas=[]
    ps=[[0,1,2,3],[1,3,2,2],[2,4,1,3],[1,2,4,3],[3,5,2,1],[2,1,4,5],[1,5,3,4],[3,2,5,4],[2,5,1,4],[1,4,5,2]]
    ps=[p for p in ps if (sp.Matrix(p).T*ETA*sp.Matrix(p))[0]!=0]
    for p in ps:
        T=make_source(p,rng)
        ok,lam=source_residual(p,T,sp.Rational(1,2)); right.append(ok); lambdas.append(str(lam))
        okw,_=source_residual(p,T,sp.Rational(1,3)); wrong.append(not okw)
    ok=all(right) and sum(wrong)>=6 and len(right)>=8
    return {"stream":"C","valid":True,"pass":bool(ok),"right_exact":sum(right),"n":len(right),"wrong_trace_rejected":sum(wrong),"lambdas":lambdas}


def stream_D():
    transforms=[sp.eye(4), sp.Matrix([[1,1,0,0],[0,1,1,0],[0,0,1,1],[0,0,0,1]]), sp.Matrix([[2,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,2]]), sp.Matrix([[1,2,0,1],[0,1,1,0],[1,0,2,0],[0,0,1,1]])]
    batches=[]; ok=True
    for seed in [5731,5732,5733]:
        M=constraint_matrix(seed,26)
        local=[]
        for S in transforms:
            if S.det()==0: ok=False; continue
            Mt=M*S
            ns=Mt.nullspace(); good=(Mt.rank()==3 and len(ns)==1 and proportional(S*ns[0],QREF))
            local.append(good); ok=ok and good
        batches.append(local)
    # Deliberately insufficient batch: one row must have nullity >1 and be detected.
    Mbad=constraint_matrix(5799,1); diagnostic=(4-Mbad.rank())>1
    ok=ok and diagnostic
    return {"stream":"D","valid":True,"pass":bool(ok),"basis_batch_passes":batches,"rank_deficient_control_detected":bool(diagnostic),"bad_nullity":int(4-Mbad.rank())}


def aggregate(dirp):
    data={}
    for s in 'ABCD':
        p=Path(dirp)/f'g59-{s}'/f'{s}.json'
        if not p.exists(): return {"gate":"ITER057_G59","valid":False,"classification":"INFRASTRUCTURE_OR_IMPLEMENTATION_INVALID","missing":str(p),"programme_readiness_percent":66,"theory_established_percent":0}
        data[s]=json.loads(p.read_text())
    valid=all(data[s].get('valid') for s in data); passes={s:bool(data[s].get('pass')) for s in data}
    if valid and all(passes.values()): cls='TWO_DERIVATIVE_LINEARIZED_LOCAL_CONSTITUTION_UNIQUE_UP_TO_NORMALIZATION_SCOPED'
    else: cls='G59_FROZEN_RULE_NOT_MET' if valid else 'INFRASTRUCTURE_OR_IMPLEMENTATION_INVALID'
    return {"gate":"ITER057_G59_TWO_DERIVATIVE_CONSTITUTION_FREEDOM","valid":valid,"passes":passes,"classification":cls,"programme_readiness_percent":66,"theory_established_percent":0}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=list('ABCD')); ap.add_argument('--aggregate-dir'); ap.add_argument('--out',required=True); args=ap.parse_args()
    if args.aggregate_dir: res=aggregate(args.aggregate_dir)
    else: res={'A':stream_A,'B':stream_B,'C':stream_C,'D':stream_D}[args.stream]()
    Path(args.out).parent.mkdir(parents=True,exist_ok=True); Path(args.out).write_text(json.dumps(res,indent=2)); print(json.dumps(res,indent=2))

if __name__=='__main__': main()
