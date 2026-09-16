#!/usr/bin/env python3
"""RCG003B direct Euler-Lagrange highest-derivative cross-check."""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from pathlib import Path
import sympy as sp

def derive_reduced_density():
    t,x,y,z=sp.symbols("t x y z"); coords=(t,x,y,z)
    a=sp.Function("a")(t); b=sp.Function("b")(t)
    g=sp.diag(-1,sp.exp(2*a),sp.exp(2*b),sp.exp(2*b)); gi=g.inv(); n=4
    G=[[[0]*n for _ in range(n)] for _ in range(n)]
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
    R2=sp.simplify(sum(gi[m,r]*gi[q,s]*Ric[m,q]*Ric[r,s]
       for m in range(n) for q in range(n) for r in range(n) for s in range(n)))
    R3=sp.simplify(sp.trace((gi*Ric)**3))
    va,vb,ua,ub=sp.symbols("va vb ua ub")
    sub={sp.diff(a,t):va,sp.diff(b,t):vb,sp.diff(a,(t,2)):ua,sp.diff(b,(t,2)):ub}
    O=sp.expand((7*R**3-36*R*R2+36*R3).subs(sub))
    return sp.exp(a+2*b)*O,(a,b,va,vb,ua,ub)

def total_derivative(e, q):
    a,b,va,vb,ua,ub,ja,jb,ka,kb=q
    return sp.expand(
      sp.diff(e,a)*va + sp.diff(e,b)*vb +
      sp.diff(e,va)*ua + sp.diff(e,vb)*ub +
      sp.diff(e,ua)*ja + sp.diff(e,ub)*jb +
      sp.diff(e,ja)*ka + sp.diff(e,jb)*kb)

def coeff_matrix(Ea,Eb,vars_high):
    return [[sp.expand(sp.diff(Ea,v)) for v in vars_high],
            [sp.expand(sp.diff(Eb,v)) for v in vars_high]]

def minimal_poly_witness(entries, vars_):
    for label,e in entries:
        p=sp.Poly(sp.expand(e),*vars_,domain=sp.QQ)
        if not p.is_zero:
            terms=sorted([(sum(m),m,c) for m,c in p.terms()],key=lambda x:(x[0],x[1]))
            _,m,c=terms[0]
            mon="*".join(f"{v}^{k}" for v,k in zip(vars_,m) if k) or "1"
            return {"location":label,"monomial":mon,"powers":list(m),"coefficient":str(c),
                    "common_density_factor":"exp(a+2b)"}
    return None

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True); ap.add_argument("--prereg-sha",required=True)
    ap.add_argument("--parent-terminal",required=True); ap.add_argument("--run-head",default="")
    args=ap.parse_args()

    L,(a,b,va,vb,ua,ub)=derive_reduced_density()
    ja,jb,ka,kb=sp.symbols("ja jb ka kb")
    q=(a,b,va,vb,ua,ub,ja,jb,ka,kb)

    Ea=sp.expand(sp.diff(L,a)-total_derivative(sp.diff(L,va),q)+total_derivative(total_derivative(sp.diff(L,ua),q),q))
    Eb=sp.expand(sp.diff(L,b)-total_derivative(sp.diff(L,vb),q)+total_derivative(total_derivative(sp.diff(L,ub),q),q))

    fourth=coeff_matrix(Ea,Eb,(ka,kb))
    third=coeff_matrix(Ea,Eb,(ja,jb))
    ef=sp.exp(a+2*b)
    fourth_n=[[sp.expand(e/ef) for e in row] for row in fourth]
    third_n=[[sp.expand(e/ef) for e in row] for row in third]

    H=[[sp.diff(L,ua,ua),sp.diff(L,ua,ub)],[sp.diff(L,ub,ua),sp.diff(L,ub,ub)]]
    Hn=[[sp.expand(e/ef) for e in row] for row in H]
    corr=all(sp.expand(fourth_n[i][j]-Hn[i][j])==0 for i in range(2) for j in range(2))
    fourth_nonzero=any(e!=0 for row in fourth_n for e in row)
    third_nonzero=any(e!=0 for row in third_n for e in row)

    if not corr:
        classification="INVALID_RCG003B"
        witness=None
    elif fourth_nonzero:
        classification="FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED"
        witness=minimal_poly_witness([
            ("E_a:a4",fourth_n[0][0]),("E_a:b4",fourth_n[0][1]),
            ("E_b:a4",fourth_n[1][0]),("E_b:b4",fourth_n[1][1])],(ua,ub,va,vb))
    elif third_nonzero:
        classification="FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED"
        witness=minimal_poly_witness([
            ("E_a:a3",third_n[0][0]),("E_a:b3",third_n[0][1]),
            ("E_b:a3",third_n[1][0]),("E_b:b3",third_n[1][1])],(ua,ub,va,vb))
    else:
        classification="PASS_SCOPED_RCG003B_AXISYMMETRIC_SECOND_ORDER_DERIVATIVE_CLOSURE"
        witness=None

    exprs=[L]+[e for row in fourth_n for e in row]+[e for row in third_n for e in row]
    symbolic_sha=hashlib.sha256("\n--\n".join(sp.srepr(sp.expand(e)) for e in exprs).encode()).hexdigest()
    result={
      "lane":"DIRECT_EULER_LAGRANGE_ADVERSARIAL_CROSSCHECK",
      "method":"METRIC_DERIVATION_PLUS_EXACT_JET_TOTAL_DERIVATIVE_EL",
      "prereg_sha":args.prereg_sha,"parent_terminal":args.parent_terminal,"run_head":args.run_head,
      "production_ray":[7,-36,36],
      "fourth_derivative_matrix_normalized":{
        "E_a":{"a4":str(sp.factor(fourth_n[0][0])),"b4":str(sp.factor(fourth_n[0][1]))},
        "E_b":{"a4":str(sp.factor(fourth_n[1][0])),"b4":str(sp.factor(fourth_n[1][1]))},
      },
      "third_derivative_coefficients_normalized":{
        "E_a":{"a3":str(sp.factor(third_n[0][0])),"b3":str(sp.factor(third_n[0][1]))},
        "E_b":{"a3":str(sp.factor(third_n[1][0])),"b3":str(sp.factor(third_n[1][1]))},
      },
      "fourth_hessian_correspondence":bool(corr),
      "fourth_derivative_obstruction_present":bool(fourth_nonzero),
      "third_derivative_obstruction_present":bool(third_nonzero),
      "minimal_exact_obstruction":witness,
      "symbolic_sha256":symbolic_sha,
      "classification":classification,
      "environment":{"python":sys.version.split()[0],"sympy":sp.__version__,"platform":platform.platform()},
      "claim_ceiling":"VERIFICATION_ONLY_SAME_FROZEN_RCG003B_CLASSIFIER"
    }
    result["scientific_payload_sha256"]=hashlib.sha256(json.dumps(result,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"classification":classification,"correspondence":corr,"witness":witness},sort_keys=True))

if __name__=="__main__": main()
