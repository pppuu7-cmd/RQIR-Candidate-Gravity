import argparse, json, os
import sympy as sp

ZS=[sp.Rational(1,3),sp.Rational(2,3),sp.Rational(5,4),sp.Rational(7,3)]
TRANSFORMS=[sp.Matrix([[1,1],[0,1]]),sp.Matrix([[2,0],[1,1]]),sp.Matrix([[1,-1],[1,2]]),sp.Matrix([[-1,2],[1,1]])]

def stream_a():
    C=sp.Matrix([-z for z in ZS]+[0])
    D=sp.Matrix([0,0,0,0,1])
    J=C.row_join(D)
    valid=(list(C)==[-z for z in ZS]+[0] and list(D)==[0,0,0,0,1] and J.rank()==2 and J[:4,:].rank()==1 and J[4:5,:].rank()==1)
    return {'stream':'A','valid':bool(valid),'classification':'JOINT_EXACT_RANK_TWO_SCOPED' if valid else 'SCIENTIFIC_FAIL_FROZEN_IDENTIFIABILITY_PREDICATE','checks':{'C_column':[str(x) for x in C],'D_column':[str(x) for x in D],'joint_rank':J.rank(),'quadratic_only_rank':J[:4,:].rank(),'cubic_only_rank':J[4:5,:].rank()},'readiness':66,'theory_established':0}

def stream_b():
    x,c,d=sp.symbols('x c d')
    GD=d*x**3/sp.Integer(6)
    GC=c*x**2/sp.Integer(2)
    d_hess=sp.diff(GD,x,2)
    d_third=sp.diff(GD,x,3)
    c_hess=sp.diff(GC,x,2)
    c_third=sp.diff(GC,x,3)
    valid=(sp.simplify(d_hess.subs(x,0))==0 and sp.simplify(sp.diff(d_third,d))==1 and sp.simplify(sp.diff(c_hess,c))==1 and c_third==0)
    return {'stream':'B','valid':bool(valid),'classification':'PERTURBATIVE_JET_ORDER_SEPARATION_EXACT_SCOPED' if valid else 'SCIENTIFIC_FAIL_FROZEN_IDENTIFIABILITY_PREDICATE','checks':{'D_hessian_at_background':str(d_hess.subs(x,0)),'D_third':str(d_third),'D_third_parameter_tangent':str(sp.diff(d_third,d)),'C_hessian':str(c_hess),'C_hessian_parameter_tangent':str(sp.diff(c_hess,c)),'C_third':str(c_third)},'readiness':66,'theory_established':0}

def stream_c():
    C=sp.Matrix([-z for z in ZS]+[0]); D=sp.Matrix([0,0,0,0,1]); J=C.row_join(D)
    rows=[]; ok=True
    base_rank=J.rank()
    for M in TRANSFORMS:
        det=sp.det(M); JT=J*M
        same=(det!=0 and JT.rank()==base_rank and JT.columnspace()==J.columnspace())
        # columnspace list equality can be basis-sensitive; verify mutual rank instead.
        same=(det!=0 and JT.rank()==base_rank and J.row_join(JT).rank()==base_rank)
        ok &= bool(same)
        rows.append({'M':[[str(v) for v in M.row(i)] for i in range(2)],'det':str(det),'rank':JT.rank(),'same_column_space':bool(same)})
    return {'stream':'C','valid':bool(ok),'classification':'IDENTIFIABILITY_RANK_REPARAMETERIZATION_COVARIANT_SCOPED' if ok else 'SCIENTIFIC_FAIL_FROZEN_IDENTIFIABILITY_PREDICATE','checks':{'base_rank':base_rank,'rows':rows},'readiness':66,'theory_established':0}

def stream_d():
    C=sp.Matrix([-z for z in ZS]+[0]); D=sp.Matrix([0,0,0,0,1]); J=C.row_join(D)
    Jzero=sp.Matrix([0,0,0,0,0]).row_join(D)
    no_cubic=J[:4,:]
    no_quad=J[4:5,:]
    leak=sp.Matrix([1,1,1,1,1])
    leakage_detected=(any(leak[i]!=0 for i in range(4)) and leak[4]!=0)
    controls={'zero_momentum_rank':Jzero.rank(),'remove_cubic_rank':no_cubic.rank(),'remove_quadratic_rank':no_quad.rank(),'leakage_detected':bool(leakage_detected),'leakage_matrix_rank':C.row_join(leak).rank()}
    valid=(Jzero.rank()==1 and no_cubic.rank()==1 and no_quad.rank()==1 and leakage_detected)
    return {'stream':'D','valid':bool(valid),'classification':'RANK_LOSS_AND_ORDER_LEAKAGE_CONTROLS_DETECTED_SCOPED' if valid else 'SCIENTIFIC_FAIL_FROZEN_IDENTIFIABILITY_PREDICATE','checks':controls,'readiness':66,'theory_established':0}

LANES={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d}

def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'): continue
            try: obj=json.load(open(os.path.join(base,fn)))
            except Exception: continue
            if obj.get('stream') in LANES: got[obj['stream']]=obj
    if set(got)!=set(LANES):
        return {'valid':False,'classification':'INFRASTRUCTURE_OR_GATE_INVALID','found':sorted(got),'readiness':66,'theory_established':0}
    if not all(got[k].get('valid') for k in LANES):
        return {'valid':False,'classification':'SCIENTIFIC_FAIL_FROZEN_IDENTIFIABILITY_PREDICATE','lane_classifications':{k:got[k].get('classification') for k in sorted(got)},'readiness':66,'theory_established':0}
    return {'valid':True,'classification':'CD_ORDER_SEPARATED_DIRECTIONS_JOINTLY_IDENTIFIABLE_ONLY_WITH_MULTIORDER_PANEL_SCOPED','lane_classifications':{k:got[k]['classification'] for k in sorted(got)},'scope_lock':'Local identifiability of frozen G72 construction representatives only; no architecture selection or candidate law.','readiness':66,'theory_established':0}

def emit(path,obj):
    os.makedirs(os.path.dirname(path) or '.',exist_ok=True)
    with open(path,'w') as f: json.dump(obj,f,indent=2,sort_keys=True)
    print(json.dumps(obj,indent=2,sort_keys=True))

p=argparse.ArgumentParser(); p.add_argument('--stream',choices=sorted(LANES)); p.add_argument('--aggregate-dir'); p.add_argument('--out',required=True); a=p.parse_args()
if bool(a.stream)==bool(a.aggregate_dir): raise SystemExit('choose exactly one mode')
o=LANES[a.stream]() if a.stream else aggregate(a.aggregate_dir)
emit(a.out,o)
if not o.get('valid'): raise SystemExit(2)
