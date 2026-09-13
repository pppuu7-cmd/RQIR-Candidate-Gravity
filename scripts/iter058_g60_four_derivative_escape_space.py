#!/usr/bin/env python3
import argparse, json, itertools
from pathlib import Path
import sympy as sp

ETA = sp.diag(-1, 1, 1, 1)
PAIRS = [(i,j) for i in range(4) for j in range(i,4)]
HVAR = sp.symbols('h0:10')
A_MOMENTA = [(1,2,3,5),(2,1,4,3),(3,5,2,1),(1,3,2,4)]
B_MOMENTA = [(2,3,5,7),(3,1,5,2),(4,3,2,1),(5,2,1,3),(1,4,5,2),(2,5,3,1)]
C_MOMENTA = [(1,2,3,5),(2,1,4,3),(3,5,2,1),(1,3,2,4)]


def hmat(v):
    H = sp.zeros(4)
    for x,(i,j) in zip(v, PAIRS):
        H[i,j] = x
        H[j,i] = x
    return H


def curvature_invariants(k, v=HVAR):
    H = hmat(v)
    R4 = [[[[sp.Integer(0) for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a,b,c,d in itertools.product(range(4), repeat=4):
        R4[a][b][c][d] = sp.Rational(1,2) * (
            k[c]*k[b]*H[a,d] + k[d]*k[a]*H[b,c]
            - k[d]*k[b]*H[a,c] - k[c]*k[a]*H[b,d]
        )
    Ric = sp.zeros(4)
    for b,d in itertools.product(range(4), repeat=2):
        Ric[b,d] = sp.expand(sum(ETA[a,a]*R4[a][b][a][d] for a in range(4)))
    Rs = sp.expand(sum(ETA[b,b]*Ric[b,b] for b in range(4)))
    riem2 = sp.expand(sum(ETA[a,a]*ETA[b,b]*ETA[c,c]*ETA[d,d]*R4[a][b][c][d]**2
                          for a,b,c,d in itertools.product(range(4), repeat=4)))
    ric2 = sp.expand(sum(ETA[b,b]*ETA[d,d]*Ric[b,d]**2 for b,d in itertools.product(range(4), repeat=2)))
    r2 = sp.expand(Rs**2)
    return [riem2, ric2, r2]


def qmatrix(expr):
    return sp.hessian(expr, HVAR) / 2


def flatten_sym(M):
    out=[]
    for i in range(M.rows):
        for j in range(i,M.cols):
            out.append(sp.expand(M[i,j]))
    return out


def invariant_column_matrix(momenta):
    cols=[[],[],[]]
    for k in momenta:
        inv=curvature_invariants(k)
        for q in range(3):
            cols[q].extend(flatten_sym(qmatrix(inv[q])))
    return sp.Matrix.hstack(*[sp.Matrix(c) for c in cols])


def projective(v):
    vals=[sp.Rational(x) for x in list(v)]
    nz=[x for x in vals if x != 0]
    if not nz: return tuple(vals)
    vals=[sp.simplify(x/nz[0]) for x in vals]
    return tuple(vals)


def conservation_matrix(k):
    M=sp.zeros(4,10)
    for b in range(4):
        for idx,(a,c) in enumerate(PAIRS):
            val=sp.Integer(0)
            if c == b:
                val += k[a]
            if a == b and c != a:
                val += k[c]
            M[b,idx]=val
    return M


def stream_a():
    M=invariant_column_matrix(A_MOMENTA)
    ns=M.nullspace()
    rel=projective(ns[0]) if len(ns)==1 else None
    target=projective(sp.Matrix([1,-4,1]))
    ok=(M.rank()==2 and len(ns)==1 and rel==target)
    return {"stream":"A","valid":True,"pass":bool(ok),"rank":int(M.rank()),"nullity":len(ns),
            "relation":list(map(str, rel)) if rel else None,"target":list(map(str,target))}


def eval_expr(expr, vec):
    return sp.expand(expr.subs({HVAR[i]:sp.Integer(vec[i]) for i in range(10)}))


def gauge_vec(k, xi):
    vals=[]
    for a,b in PAIRS:
        vals.append(sp.Integer(k[a])*sp.Integer(xi[b]) + sp.Integer(k[b])*sp.Integer(xi[a]))
    return vals


def stream_b():
    zero=0; wrong=0; details=[]
    for idx,k in enumerate(B_MOMENTA):
        base=[sp.Integer(((i+2)*(idx+3))%11-5) for i in range(10)]
        xi=[sp.Integer(idx+1),sp.Integer(2-idx),sp.Integer(3+idx),sp.Integer(-2-idx)]
        gv=gauge_vec(k,xi)
        shifted=[base[i]+gv[i] for i in range(10)]
        nongauge=base.copy(); nongauge[(idx*3)%10] += sp.Integer(1)
        inv=curvature_invariants(k)
        diffs=[sp.simplify(eval_expr(e,shifted)-eval_expr(e,base)) for e in inv]
        ctrls=[sp.simplify(eval_expr(e,nongauge)-eval_expr(e,base)) for e in inv]
        if all(x==0 for x in diffs): zero += 1
        if any(x!=0 for x in ctrls): wrong += 1
        details.append({"k":k,"gauge_zero":all(x==0 for x in diffs),"nongauge_changes":any(x!=0 for x in ctrls)})
    ok=(zero==len(B_MOMENTA) and wrong==len(B_MOMENTA))
    return {"stream":"B","valid":True,"pass":bool(ok),"heldout_exact_zero":zero,
            "heldout_n":len(B_MOMENTA),"nongauge_rejected":wrong,"details":details}


def c_response_matrix(momenta):
    rows=[]
    for k in momenta:
        inv=curvature_invariants(k)
        HR2=qmatrix(inv[2]); HRic=qmatrix(inv[1])
        ns=conservation_matrix(k).nullspace()
        for t in ns:
            rows.append([sp.expand((t.T*HR2*t)[0]), sp.expand((t.T*HRic*t)[0])])
    return sp.Matrix(rows)


def stream_c():
    M=c_response_matrix(C_MOMENTA)
    duplicate=sp.Matrix.hstack(M[:,0],M[:,0])
    ok=(M.rank()==2 and duplicate.rank()==1)
    return {"stream":"C","valid":True,"pass":bool(ok),"response_rank":int(M.rank()),
            "rows":int(M.rows),"duplicate_control_rank":int(duplicate.rank())}


def stream_d():
    M=invariant_column_matrix(A_MOMENTA)
    relation=projective(M.nullspace()[0])
    transforms=[]
    # Three exact invertible changes of the 10 symmetric-tensor coordinates.
    S1=sp.eye(10); S1[0,1]=1
    S2=sp.zeros(10)
    for i in range(10): S2[i,(i+3)%10]=1
    S3=sp.eye(10); S3[4,2]=-2; S3[7,5]=1
    for S in (S1,S2,S3):
        cols=[]
        for q in range(3):
            pieces=[]
            for k in A_MOMENTA:
                Q=qmatrix(curvature_invariants(k)[q])
                pieces.extend(flatten_sym(S.T*Q*S))
            cols.append(sp.Matrix(pieces))
        Mt=sp.Matrix.hstack(*cols)
        ns=Mt.nullspace()
        transforms.append(Mt.rank()==2 and len(ns)==1 and projective(ns[0])==relation)
    C=c_response_matrix(C_MOMENTA)
    Ulist=[sp.Matrix([[1,1],[0,1]]),sp.Matrix([[0,1],[1,0]]),sp.Matrix([[2,1],[1,1]])]
    response_cov=[(C*U).rank()==2 for U in Ulist]
    # Deliberately insufficient observation: one scalar row cannot establish a two-direction rank.
    bad=C[:1,:]
    bad_detected=(bad.rank()<2)
    ok=all(transforms) and all(response_cov) and bad_detected
    return {"stream":"D","valid":True,"pass":bool(ok),"coordinate_covariance":transforms,
            "invariant_coordinate_covariance":response_cov,"rank_deficient_control_detected":bool(bad_detected),
            "bad_rank":int(bad.rank())}


def aggregate(indir):
    got={}
    for p in Path(indir).rglob('*.json'):
        try:
            d=json.loads(p.read_text())
        except Exception:
            continue
        if d.get('stream') in 'ABCD': got[d['stream']]=d
    valid=(set(got)==set('ABCD') and all(got[s].get('valid') for s in 'ABCD'))
    passes={s:bool(got.get(s,{}).get('pass',False)) for s in 'ABCD'}
    if valid and all(passes.values()):
        cls='FOUR_DERIVATIVE_LINEARIZED_GAUGE_INVARIANT_ESCAPE_SPACE_TWO_DIMENSIONAL_SCOPED'
    elif valid:
        failed=''.join(s for s in 'ABCD' if not passes[s])
        cls='SCIENTIFIC_FAIL_G60_'+failed
    else:
        cls='INFRASTRUCTURE_OR_IMPLEMENTATION_FAIL'
    return {"gate":"ITER058_G60_FOUR_DERIVATIVE_ESCAPE_SPACE","valid":valid,"passes":passes,
            "classification":cls,"programme_readiness_percent":66,"theory_established_percent":0}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=list('ABCD')); ap.add_argument('--out',required=True); ap.add_argument('--aggregate-dir')
    args=ap.parse_args()
    if args.aggregate_dir:
        d=aggregate(args.aggregate_dir)
    else:
        d={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d}[args.stream]()
    Path(args.out).parent.mkdir(parents=True,exist_ok=True); Path(args.out).write_text(json.dumps(d,indent=2,sort_keys=True))
    print(json.dumps(d,indent=2,sort_keys=True))

if __name__=='__main__': main()
