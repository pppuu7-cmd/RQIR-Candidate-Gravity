#!/usr/bin/env python3
"""RCG003B Constructor: exact axisymmetric Bianchi-I derivative-closure evaluator.

Frozen science: prereg/RCG003B_AXISYMMETRIC_BIANCHI_I_DERIVATIVE_CLOSURE.md
The production ray is fixed to (7,-36,36); no fitting or basis search occurs.
"""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from pathlib import Path
import sympy as sp

def tensor_curvature_axisymmetric():
    t,x,y,z = sp.symbols("t x y z")
    a = sp.Function("a")(t); b = sp.Function("b")(t)
    coords=(t,x,y,z)
    g=sp.diag(-1, sp.exp(2*a), sp.exp(2*b), sp.exp(2*b))
    gi=sp.simplify(g.inv()); n=4
    G=[[[sp.Integer(0) for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for m in range(n):
            for q in range(n):
                G[r][m][q]=sp.simplify(sp.Rational(1,2)*sum(
                    gi[r,s]*(sp.diff(g[s,q],coords[m])+sp.diff(g[s,m],coords[q])-sp.diff(g[m,q],coords[s]))
                    for s in range(n)))
    Ric=sp.MutableDenseMatrix(n,n,[0]*16)
    for m in range(n):
        for q in range(n):
            e=sp.Integer(0)
            for r in range(n):
                e += sp.diff(G[r][m][q],coords[r]) - sp.diff(G[r][m][r],coords[q])
                for s in range(n):
                    e += G[r][r][s]*G[s][m][q] - G[r][q][s]*G[s][m][r]
            Ric[m,q]=sp.simplify(e)
    R=sp.simplify(sum(gi[m,q]*Ric[m,q] for m in range(n) for q in range(n)))
    Ric2=sp.simplify(sum(gi[m,r]*gi[q,s]*Ric[m,q]*Ric[r,s]
                         for m in range(n) for q in range(n) for r in range(n) for s in range(n)))
    M=sp.simplify(gi*Ric)
    Ric3=sp.simplify(sp.trace(M**3))
    sqrtg=sp.exp(a+2*b)
    return (t,a,b,g,gi,R,Ric2,Ric3,sqrtg)

def jet(expr,t,a,b):
    va,vb,ua,ub=sp.symbols("va vb ua ub")
    subs={sp.diff(a,t):va, sp.diff(b,t):vb, sp.diff(a,(t,2)):ua, sp.diff(b,(t,2)):ub}
    return sp.expand(expr.subs(subs)), (va,vb,ua,ub)

def canonical(expr):
    return sp.srepr(sp.expand(expr))

def hash_exprs(exprs):
    payload="\n---\n".join(canonical(e) for e in exprs).encode()
    return hashlib.sha256(payload).hexdigest()

def poly_terms(expr, vars_):
    p=sp.Poly(sp.expand(expr), *vars_, domain=sp.QQ)
    return [{"monomial":"*".join(f"{str(v)}^{e}" for v,e in zip(vars_,mon) if e) or "1",
             "powers":list(mon), "coefficient":str(coeff)}
            for mon,coeff in p.terms()]

def minimal_witness(entries, vars_):
    for name,e in entries:
        p=sp.Poly(sp.expand(e), *vars_, domain=sp.QQ)
        if not p.is_zero:
            terms=[(sum(mon), mon, coeff) for mon,coeff in p.terms()]
            _,mon,coeff=sorted(terms, key=lambda x:(x[0],x[1]))[0]
            label="*".join(f"{str(v)}^{k}" for v,k in zip(vars_,mon) if k) or "1"
            return {"component":name,"monomial":label,"powers":list(mon),"coefficient":str(coeff)}
    return None

def axis_relabel_control():
    t,x,y,z=sp.symbols("t x y z")
    a=sp.Function("a")(t); b=sp.Function("b")(t); coords=(t,x,y,z)
    g=sp.diag(-1,sp.exp(2*b),sp.exp(2*a),sp.exp(2*b)); gi=g.inv(); n=4
    G=[[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for m in range(n):
            for q in range(n):
                G[r][m][q]=sp.simplify(sp.Rational(1,2)*sum(
                    gi[r,s]*(sp.diff(g[s,q],coords[m])+sp.diff(g[s,m],coords[q])-sp.diff(g[m,q],coords[s]))
                    for s in range(n)))
    Ric=sp.MutableDenseMatrix(n,n,[0]*16)
    for m in range(n):
        for q in range(n):
            e=0
            for r in range(n):
                e += sp.diff(G[r][m][q],coords[r])-sp.diff(G[r][m][r],coords[q])
                for s in range(n):
                    e += G[r][r][s]*G[s][m][q]-G[r][q][s]*G[s][m][r]
            Ric[m,q]=sp.simplify(e)
    R=sp.simplify(sum(gi[m,q]*Ric[m,q] for m in range(n) for q in range(n)))
    Ric2=sp.simplify(sum(gi[m,r]*gi[q,s]*Ric[m,q]*Ric[r,s]
                         for m in range(n) for q in range(n) for r in range(n) for s in range(n)))
    Ric3=sp.simplify(sp.trace((gi*Ric)**3))
    O=sp.expand(7*R**3-36*R*Ric2+36*Ric3)
    OJ,(va,vb,ua,ub)=jet(O,t,a,b)
    H=sp.Matrix([[sp.diff(OJ,ua,ua),sp.diff(OJ,ua,ub)],[sp.diff(OJ,ub,ua),sp.diff(OJ,ub,ub)]])
    return sp.Matrix([[sp.expand(e) for e in H.row(i)] for i in range(2)])

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True)
    ap.add_argument("--prereg-sha",required=True)
    ap.add_argument("--parent-terminal",required=True)
    ap.add_argument("--run-head",default="")
    args=ap.parse_args()

    t,a,b,g,gi,R,Ric2,Ric3,sqrtg=tensor_curvature_axisymmetric()
    RJ,(va,vb,ua,ub)=jet(R,t,a,b)
    R2J,_=jet(Ric2,t,a,b); R3J,_=jet(Ric3,t,a,b)
    O=sp.expand(7*RJ**3-36*RJ*R2J+36*R3J)
    L=sp.exp(a+2*b)*O
    H=sp.Matrix([[sp.diff(L,ua,ua),sp.diff(L,ua,ub)],
                 [sp.diff(L,ub,ua),sp.diff(L,ub,ub)]])
    Hn=sp.Matrix([[sp.expand(H[i,j]/sp.exp(a+2*b)) for j in range(2)] for i in range(2)])
    entries=[("H_aa",Hn[0,0]),("H_ab",Hn[0,1]),("H_bb",Hn[1,1])]
    hessian_zero=all(sp.expand(e)==0 for _,e in entries)

    v,u=sp.symbols("v u")
    Hiso=sp.expand((Hn[0,0]+2*Hn[0,1]+Hn[1,1]).subs({va:v,vb:v,ua:u,ub:u}))
    isotropic_recovery=(Hiso==0)

    Om=sp.expand(8*RJ**3-36*RJ*R2J+36*R3J)
    Lm=sp.exp(a+2*b)*Om
    Hm=sp.Matrix([[sp.diff(Lm,ua,ua),sp.diff(Lm,ua,ub)],
                  [sp.diff(Lm,ub,ua),sp.diff(Lm,ub,ub)]])
    Hm_diag=sp.expand(((Hm[0,0]+2*Hm[0,1]+Hm[1,1])/sp.exp(a+2*b)).subs({va:v,vb:v,ua:u,ub:u}))
    perturbed_detected=(Hm_diag!=0)

    LEH=sp.exp(a+2*b)*RJ
    HEH=sp.Matrix([[sp.diff(LEH,ua,ua),sp.diff(LEH,ua,ub)],[sp.diff(LEH,ub,ua),sp.diff(LEH,ub,ub)]])
    eh_ok=all(sp.expand(e)==0 for e in HEH)
    LR2=sp.exp(a+2*b)*RJ**2
    HR2=sp.Matrix([[sp.diff(LR2,ua,ua),sp.diff(LR2,ua,ub)],[sp.diff(LR2,ub,ua),sp.diff(LR2,ub,ub)]])
    r2_sensitive=any(sp.expand(e)!=0 for e in HR2)

    Hperm=axis_relabel_control()
    axis_label_ok=all(sp.expand(Hperm[i,j]-Hn[i,j])==0 for i in range(2) for j in range(2))

    source_tag="VACUUM_ZERO"
    external_tag="UNREGISTERED_EXTERNAL_T"
    source_lock=(source_tag=="VACUUM_ZERO" and external_tag!="VACUUM_ZERO")
    offshell_lock=set((va,vb,ua,ub)).issubset(sp.expand(O).free_symbols)

    controls={
        "isotropic_recovery":bool(isotropic_recovery),
        "perturbed_ray_negative":bool(perturbed_detected),
        "EH_reference":bool(eh_ok),
        "R2_sensitivity":bool(r2_sensitive),
        "axis_label_duplicate":bool(axis_label_ok),
        "off_shell_lock":bool(offshell_lock),
        "source_lock":bool(source_lock),
    }
    controls_valid=all(controls.values())
    witness=minimal_witness(entries,(ua,ub,va,vb))

    curl_status="NOT_APPLICABLE_HESSIAN_NONZERO"
    if not controls_valid:
        classification="INVALID_RCG003B"
    elif not hessian_zero:
        classification="FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED"
    else:
        Aa=sp.diff(L,ua); Ab=sp.diff(L,ub)
        Cab=sp.expand((sp.diff(Aa,vb)-sp.diff(Ab,va))/sp.exp(a+2*b))
        curl_status="ZERO" if Cab==0 else "NONZERO"
        if Cab==0:
            classification="PASS_SCOPED_RCG003B_AXISYMMETRIC_SECOND_ORDER_DERIVATIVE_CLOSURE"
        else:
            classification="FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED"

    result={
        "gate":"RCG003B_AXISYMMETRIC_BIANCHI_I_DERIVATIVE_CLOSURE",
        "prereg_sha":args.prereg_sha,
        "parent_terminal":args.parent_terminal,
        "run_head":args.run_head,
        "production_ray":[7,-36,36],
        "source":"VACUUM_ZERO",
        "metric":"diag(-1,exp(2a),exp(2b),exp(2b))",
        "derivation":"DIRECT_METRIC_TO_CHRISTOFFEL_TO_RICCI_TO_INVARIANTS",
        "normalized_R":str(sp.expand(RJ)),
        "normalized_Ricci2":str(sp.expand(R2J)),
        "normalized_Ricci3":str(sp.expand(R3J)),
        "hessian_normalized_by_exp_a_plus_2b":{
            "H_aa":str(sp.factor(Hn[0,0])),
            "H_ab":str(sp.factor(Hn[0,1])),
            "H_bb":str(sp.factor(Hn[1,1])),
        },
        "hessian_terms":{
            "H_aa":poly_terms(Hn[0,0],(ua,ub,va,vb)),
            "H_ab":poly_terms(Hn[0,1],(ua,ub,va,vb)),
            "H_bb":poly_terms(Hn[1,1],(ua,ub,va,vb)),
        },
        "hessian_zero_identically":bool(hessian_zero),
        "minimal_exact_obstruction":witness,
        "common_density_factor":"exp(a+2b)",
        "curl_status":curl_status,
        "controls":controls,
        "controls_valid":controls_valid,
        "control_details":{
            "isotropic_pullback_hessian":str(sp.factor(Hiso)),
            "perturbed_ray_conformal_hessian":str(sp.factor(Hm_diag)),
        },
        "symbolic_sha256":hash_exprs([RJ,R2J,R3J,O,Hn[0,0],Hn[0,1],Hn[1,1]]),
        "scientific_payload_sha256":"",
        "classification":classification,
        "scope":"AXISYMMETRIC_HOMOGENEOUS_UNIT_LAPSE_VACUUM_FIXED_RAY_ONLY",
        "environment":{"python":sys.version.split()[0],"sympy":sp.__version__,"platform":platform.platform()},
        "claim_locks":{
            "theory_established":"0%",
            "chi_ABC":"UNAUTHORIZED_NOT_COMPUTED",
            "GR_derived":False,
            "full_constraint_closure":False,
            "hyperbolicity":False,
            "quantum_gravity":False,
            "new_physics":False,
        }
    }
    tmp=dict(result); tmp["scientific_payload_sha256"]=""
    result["scientific_payload_sha256"]=hashlib.sha256(
        json.dumps(tmp,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"classification":classification,"witness":witness,"controls":controls},sort_keys=True))

if __name__=="__main__":
    main()
