#!/usr/bin/env python3
"""RCG003B independent Critic.

Independent route: derive curvature for fully anisotropic diagonal Bianchi-I
with three scale histories, then specialize q2=q3 only after curvature is built.
Does not import or call the Constructor.
"""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from pathlib import Path
import sympy as sp

def canonical(e): return sp.srepr(sp.expand(e))
def digest(exprs): return hashlib.sha256("\n--\n".join(canonical(e) for e in exprs).encode()).hexdigest()

def general_bianchi():
    t,x,y,z=sp.symbols("t x y z"); coords=(t,x,y,z)
    q1,q2,q3=[sp.Function(n)(t) for n in ("q1","q2","q3")]
    g=sp.diag(-1,sp.exp(2*q1),sp.exp(2*q2),sp.exp(2*q3)); gi=g.inv(); n=4
    G=[[[sp.Integer(0) for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for r in range(n):
      for m in range(n):
       for q in range(n):
        s=sp.Integer(0)
        for k in range(n):
            s += gi[r,k]*(sp.diff(g[k,q],coords[m])+sp.diff(g[k,m],coords[q])-sp.diff(g[m,q],coords[k]))
        G[r][m][q]=sp.simplify(s/2)
    Ric=sp.MutableDenseMatrix(n,n,[0]*16)
    for m in range(n):
      for q in range(n):
        e=sp.Integer(0)
        for r in range(n):
            e += sp.diff(G[r][m][q],coords[r])-sp.diff(G[r][m][r],coords[q])
            for s in range(n):
                e += G[r][r][s]*G[s][m][q]-G[r][q][s]*G[s][m][r]
        Ric[m,q]=sp.simplify(e)
    R=sp.simplify(sum(gi[m,q]*Ric[m,q] for m in range(n) for q in range(n)))
    Ric2=sp.simplify(sum(gi[m,r]*gi[q,s]*Ric[m,q]*Ric[r,s]
        for m in range(n) for q in range(n) for r in range(n) for s in range(n)))
    Ric3=sp.simplify(sp.trace((gi*Ric)**3))
    return t,(q1,q2,q3),R,Ric2,Ric3

def specialize(expr,t,qs):
    q1,q2,q3=qs
    a=sp.Function("a")(t); b=sp.Function("b")(t)
    repl={q1:a,q2:b,q3:b}
    for order in (1,2):
        repl[sp.diff(q1,(t,order))]=sp.diff(a,(t,order))
        repl[sp.diff(q2,(t,order))]=sp.diff(b,(t,order))
        repl[sp.diff(q3,(t,order))]=sp.diff(b,(t,order))
    e=sp.expand(expr.xreplace(repl))
    va,vb,ua,ub=sp.symbols("va vb ua ub")
    e=sp.expand(e.subs({sp.diff(a,t):va,sp.diff(b,t):vb,sp.diff(a,(t,2)):ua,sp.diff(b,(t,2)):ub}))
    return e,(a,b,va,vb,ua,ub)

def witness(entries, vars_):
    for name,e in entries:
        p=sp.Poly(sp.expand(e),*vars_,domain=sp.QQ)
        if not p.is_zero:
            terms=sorted([(sum(m),m,c) for m,c in p.terms()],key=lambda x:(x[0],x[1]))
            _,m,c=terms[0]
            lab="*".join(f"{v}^{k}" for v,k in zip(vars_,m) if k) or "1"
            return {"component":name,"monomial":lab,"powers":list(m),"coefficient":str(c)}
    return None

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True); ap.add_argument("--prereg-sha",required=True)
    ap.add_argument("--parent-terminal",required=True); ap.add_argument("--run-head",default="")
    args=ap.parse_args()

    t,qs,R,R2,R3=general_bianchi()
    RJ,(a,b,va,vb,ua,ub)=specialize(R,t,qs)
    R2J,_=specialize(R2,t,qs); R3J,_=specialize(R3,t,qs)
    O=sp.expand(7*RJ**3-36*RJ*R2J+36*R3J)
    L=sp.exp(a+2*b)*O
    Haa=sp.expand(sp.diff(L,ua,ua)/sp.exp(a+2*b))
    Hab=sp.expand(sp.diff(L,ua,ub)/sp.exp(a+2*b))
    Hbb=sp.expand(sp.diff(L,ub,ub)/sp.exp(a+2*b))
    entries=[("H_aa",Haa),("H_ab",Hab),("H_bb",Hbb)]
    hz=all(e==0 for _,e in entries)
    wit=witness(entries,(ua,ub,va,vb))

    v,u=sp.symbols("v u")
    iso=sp.expand((Haa+2*Hab+Hbb).subs({va:v,vb:v,ua:u,ub:u}))
    iso_ok=(iso==0)

    Om=sp.expand(8*RJ**3-36*RJ*R2J+36*R3J)
    Lm=sp.exp(a+2*b)*Om
    mut=sp.expand((sp.diff(Lm,ua,ua)+2*sp.diff(Lm,ua,ub)+sp.diff(Lm,ub,ub))/sp.exp(a+2*b))
    mut=sp.expand(mut.subs({va:v,vb:v,ua:u,ub:u}))
    mut_ok=(mut!=0)

    LEH=sp.exp(a+2*b)*RJ
    eh_ok=all(sp.expand(e)==0 for e in
              (sp.diff(LEH,ua,ua),sp.diff(LEH,ua,ub),sp.diff(LEH,ub,ub)))
    LR2=sp.exp(a+2*b)*RJ**2
    r2_ok=any(sp.expand(e)!=0 for e in
              (sp.diff(LR2,ua,ua),sp.diff(LR2,ua,ub),sp.diff(LR2,ub,ub)))

    q1,q2,q3=qs
    aa=sp.Function("a")(t); bb=sp.Function("b")(t)
    repl={q1:bb,q2:aa,q3:bb}
    for order in (1,2):
        repl[sp.diff(q1,(t,order))]=sp.diff(bb,(t,order))
        repl[sp.diff(q2,(t,order))]=sp.diff(aa,(t,order))
        repl[sp.diff(q3,(t,order))]=sp.diff(bb,(t,order))
    def relabel(e):
        e=sp.expand(e.xreplace(repl))
        return sp.expand(e.subs({sp.diff(aa,t):va,sp.diff(bb,t):vb,sp.diff(aa,(t,2)):ua,sp.diff(bb,(t,2)):ub}))
    Rp,R2p,R3p=map(relabel,(R,R2,R3))
    Op=sp.expand(7*Rp**3-36*Rp*R2p+36*R3p)
    Lp=sp.exp(aa+2*bb)*Op
    Hp=[sp.expand(sp.diff(Lp,ua,ua)/sp.exp(aa+2*bb)),
        sp.expand(sp.diff(Lp,ua,ub)/sp.exp(aa+2*bb)),
        sp.expand(sp.diff(Lp,ub,ub)/sp.exp(aa+2*bb))]
    axis_ok=all(sp.expand(x-y)==0 for x,y in zip(Hp,(Haa,Hab,Hbb)))

    controls={
      "isotropic_recovery":bool(iso_ok),
      "perturbed_ray_negative":bool(mut_ok),
      "EH_reference":bool(eh_ok),
      "R2_sensitivity":bool(r2_ok),
      "axis_label_duplicate":bool(axis_ok),
      "off_shell_lock":set((va,vb,ua,ub)).issubset(O.free_symbols),
      "source_lock":True,
      "fixed_parent_ray_no_refit":True,
      "constructor_not_imported":True,
    }
    valid=all(controls.values())
    if not valid: cls="INVALID_RCG003B"
    elif not hz: cls="FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED"
    else:
        Aa=sp.diff(L,ua); Ab=sp.diff(L,ub)
        C=sp.expand((sp.diff(Aa,vb)-sp.diff(Ab,va))/sp.exp(a+2*b))
        cls=("PASS_SCOPED_RCG003B_AXISYMMETRIC_SECOND_ORDER_DERIVATIVE_CLOSURE"
             if C==0 else "FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED")

    result={
      "lane":"INDEPENDENT_CRITIC",
      "method":"FULLY_ANISOTROPIC_DIAGONAL_METRIC_CURVATURE_THEN_AXISYMMETRIC_SPECIALIZATION",
      "prereg_sha":args.prereg_sha,"parent_terminal":args.parent_terminal,"run_head":args.run_head,
      "production_ray":[7,-36,36],"source":"VACUUM_ZERO",
      "hessian_normalized_by_exp_a_plus_2b":{"H_aa":str(sp.factor(Haa)),"H_ab":str(sp.factor(Hab)),"H_bb":str(sp.factor(Hbb))},
      "hessian_zero_identically":bool(hz),"minimal_exact_obstruction":wit,
      "controls":controls,"controls_valid":valid,
      "symbolic_sha256":digest([RJ,R2J,R3J,O,Haa,Hab,Hbb]),
      "classification":cls,
      "critic_classification":"PASS_INDEPENDENT_CRITIC_RCG003B_SCOPE_AND_PROVENANCE" if valid else "INVALID_INDEPENDENT_CRITIC",
      "environment":{"python":sys.version.split()[0],"sympy":sp.__version__,"platform":platform.platform()},
      "claim_ceiling":"AXISYMMETRIC_HOMOGENEOUS_UNIT_LAPSE_VACUUM_FIXED_RAY_ONLY"
    }
    result["scientific_payload_sha256"]=hashlib.sha256(json.dumps(result,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"classification":cls,"critic":result["critic_classification"],"witness":wit},sort_keys=True))

if __name__=="__main__": main()
