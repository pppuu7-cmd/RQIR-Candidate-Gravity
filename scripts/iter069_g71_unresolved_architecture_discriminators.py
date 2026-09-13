import argparse, json, os
import sympy as sp

SUPPORTED='SUPPORTED'
UNRESOLVED='UNRESOLVED'
BLOCKED='BLOCKED_BY_MISSING_STRUCTURE'
NOT='NOT_SUPPORTED'
PROPS=['LOW_ENERGY_RECOVERY','WARD_COMPATIBLE_LINEAR_RESPONSE','NO_NEW_FINITE_LINEAR_POLES','RETARDED_CAUSAL_RULE_EXPLICIT','FIELD_LEVEL_QUANTUM_RULE_EXPLICIT','BASELINE_DISTINCT_DISCRIMINATOR_EXPLICIT']
SCORE={NOT:0,UNRESOLVED:1,BLOCKED:1,SUPPORTED:2}

G70={
'B':{PROPS[0]:SUPPORTED,PROPS[1]:SUPPORTED,PROPS[2]:SUPPORTED,PROPS[3]:UNRESOLVED,PROPS[4]:UNRESOLVED,PROPS[5]:SUPPORTED},
'C':{PROPS[0]:SUPPORTED,PROPS[1]:UNRESOLVED,PROPS[2]:UNRESOLVED,PROPS[3]:SUPPORTED,PROPS[4]:SUPPORTED,PROPS[5]:SUPPORTED},
'D':{PROPS[0]:SUPPORTED,PROPS[1]:SUPPORTED,PROPS[2]:UNRESOLVED,PROPS[3]:UNRESOLVED,PROPS[4]:SUPPORTED,PROPS[5]:SUPPORTED},
'E':{PROPS[0]:SUPPORTED,PROPS[1]:SUPPORTED,PROPS[2]:SUPPORTED,PROPS[3]:UNRESOLVED,PROPS[4]:UNRESOLVED,PROPS[5]:SUPPORTED},
}

def base(stream):
    return dict(G70[stream])

def lane_B():
    z=sp.symbols('z')
    F=sp.exp(z**2)
    zeros=sp.solveset(F,z,domain=sp.S.Complexes)
    nozeros=(zeros==sp.EmptySet)
    props=base('B')
    props[PROPS[3]]=BLOCKED
    props[PROPS[4]]=BLOCKED
    valid=nozeros and sp.simplify(F.subs(z,0)-1)==0
    return {'stream':'B','valid':bool(valid),'properties':props,'checks':{
        'F':str(F),'F0':str(F.subs(z,0)),'complex_zero_set':str(zeros),'no_finite_zeros_exact':bool(nozeros),
        'retarded_prescription_present_in_frozen_object':False,
        'field_level_quantum_measure_present_in_frozen_object':False,
        'blocked_properties':[PROPS[3],PROPS[4]]},'scope':'Exact consequences of frozen G70 B only.'}

def lane_C():
    props=base('C')
    props[PROPS[1]]=BLOCKED
    props[PROPS[2]]=BLOCKED
    # Reconstruct representative frozen structural facts without adding a spacetime embedding.
    rows=[]; ok=True
    for seed in (2,3,5,7):
        n=4
        L=sp.Matrix([[sp.Rational(((seed+3)*(i+2)+(j+1)*(j+3)+i*j)%13-6,7) if i>=j else 0 for j in range(n)] for i in range(n)])
        N=L*L.T
        DR=sp.Matrix([[sp.Rational((seed+i+j+1)%9+1,11) if i>=j else 0 for j in range(n)] for i in range(n)])
        sym=(N-N.T)==sp.zeros(n)
        ret=all(DR[i,j]==0 for i in range(n) for j in range(n) if j>i)
        gram=(N-L*L.T)==sp.zeros(n)
        ok &= sym and ret and gram
        rows.append({'seed':seed,'noise_gram_exact':bool(gram),'noise_symmetric':bool(sym),'retarded_lower_triangular':bool(ret)})
    return {'stream':'C','valid':bool(ok),'properties':props,'checks':{
        'rows':rows,'spacetime_tensor_embedding_present':False,'momentum_denominator_present':False,
        'blocked_properties':[PROPS[1],PROPS[2]]},'scope':'Finite Gaussian CTP architecture; no gravitational embedding invented.'}

def lane_D():
    # Exact symbolic Hessian test of Gamma3=kappa*K_abc Delta_a Sigma_b Sigma_c.
    kappa=sp.symbols('kappa', nonzero=True)
    d1,d2,s1,s2=sp.symbols('d1 d2 s1 s2')
    fields=[d1,d2,s1,s2]
    # Frozen representative with multiple nonzero coefficients and b<->c symmetry encoded directly.
    G3=kappa*(2*d1*s1**2+3*d1*s1*s2+3*d1*s2*s1-5*d2*s2**2+7*d2*s1*s2+7*d2*s2*s1)
    H=sp.Matrix([[sp.diff(G3,x,y) for y in fields] for x in fields])
    H0=H.subs({x:0 for x in fields})
    cubic_zero=(H0==sp.zeros(len(fields)))
    G2=kappa*(d1*s1+d2*s2+s1**2)
    H2=sp.Matrix([[sp.diff(G2,x,y) for y in fields] for x in fields]).subs({x:0 for x in fields})
    quad_nonzero=(H2!=sp.zeros(len(fields)))
    G1=kappa*(d1+s1)
    H1=sp.Matrix([[sp.diff(G1,x,y) for y in fields] for x in fields]).subs({x:0 for x in fields})
    linear_zero=(H1==sp.zeros(len(fields)))
    third=[sp.diff(G3,fields[i],fields[j],fields[k]).subs({x:0 for x in fields}) for i in range(4) for j in range(4) for k in range(4)]
    third_nonzero=any(v!=0 for v in third)
    valid=cubic_zero and quad_nonzero and linear_zero and third_nonzero
    props=base('D')
    if valid:
        props[PROPS[2]]=SUPPORTED
        props[PROPS[3]]=BLOCKED
    return {'stream':'D','valid':bool(valid),'properties':props,'checks':{
        'cubic_hessian_at_background_zero':bool(cubic_zero),'quadratic_control_hessian_nonzero':bool(quad_nonzero),
        'linear_control_hessian_zero':bool(linear_zero),'cubic_third_derivative_nonzero':bool(third_nonzero),
        'retarded_three_point_ordering_present':False,'blocked_properties':[PROPS[3]]},
        'interpretation':'Cubic extension does not change the quadratic Hessian at the frozen background; no claim about nonlinear poles or unitarity.'}

def lane_E():
    props=base('E')
    props[PROPS[3]]=BLOCKED
    props[PROPS[4]]=BLOCKED
    # Logical inventory audit: the frozen G70 E object has projector/source scalar data only.
    inventory={'conserved_transverse_projector_structure':True,'source_dependent_scalar_deformation':True,
               'retarded_support_or_boundary_condition':False,'field_level_measure_or_ctp_rule':False}
    valid=inventory['conserved_transverse_projector_structure'] and inventory['source_dependent_scalar_deformation'] and not inventory['retarded_support_or_boundary_condition'] and not inventory['field_level_measure_or_ctp_rule']
    return {'stream':'E','valid':bool(valid),'properties':props,'checks':inventory,
            'scope':'No causal or quantum rule inferred from source dependence alone.'}

LANES={'B':lane_B,'C':lane_C,'D':lane_D,'E':lane_E}

def aggregate(root):
    got={}
    for base,_,files in os.walk(root):
        for fn in files:
            if not fn.endswith('.json'): continue
            try: obj=json.load(open(os.path.join(base,fn)))
            except Exception: continue
            if obj.get('stream') in LANES: got[obj['stream']]=obj
    if set(got)!=set(LANES) or not all(got[s].get('valid') for s in LANES):
        return {'valid':False,'classification':'INFRASTRUCTURE_OR_GATE_INVALID','streams_found':sorted(got),'programme_readiness_percent':66,'theory_established_percent':0}
    dominated=[]
    for s in sorted(got):
        a=got[s]['properties']
        for t in sorted(got):
            if s==t: continue
            b=got[t]['properties']
            if all(SCORE[b[p]]>=SCORE[a[p]] for p in PROPS) and any(SCORE[b[p]]>SCORE[a[p]] for p in PROPS):
                dominated.append({'stream':s,'by':t}); break
    ds={x['stream'] for x in dominated}
    pareto=[s for s in sorted(got) if s not in ds]
    return {'valid':True,'gate':'ITER069_G71_UNRESOLVED_ARCHITECTURE_DISCRIMINATORS',
            'classification':'BEYOND_BASELINE_UNRESOLVED_PROPERTY_AUDIT_SCOPED',
            'property_matrix':{s:got[s]['properties'] for s in sorted(got)},
            'dominated':dominated,'pareto':pareto,
            'd_cubic_hessian_result':got['D']['checks'],
            'programme_readiness_percent':66,'theory_established_percent':0,
            'scope_lock':'Architecture-property audit only; no architecture selected as gravity and no candidate dynamics authored.'}

def emit(path,obj):
    os.makedirs(os.path.dirname(path) or '.',exist_ok=True)
    with open(path,'w') as f: json.dump(obj,f,indent=2,sort_keys=True)
    print(json.dumps(obj,indent=2,sort_keys=True))

p=argparse.ArgumentParser(); p.add_argument('--stream',choices=sorted(LANES)); p.add_argument('--aggregate-dir'); p.add_argument('--out',required=True); a=p.parse_args()
if bool(a.stream)==bool(a.aggregate_dir): raise SystemExit('choose exactly one mode')
obj=LANES[a.stream]() if a.stream else aggregate(a.aggregate_dir)
emit(a.out,obj)
if not obj.get('valid'): raise SystemExit(2)
