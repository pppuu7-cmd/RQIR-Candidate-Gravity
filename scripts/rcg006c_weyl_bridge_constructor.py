#!/usr/bin/env python3
"""Exact RCG006C bridge from the unique EFT quotient class to parity-even Weyl-cubed."""
from __future__ import annotations
import argparse, hashlib, json, sys
from collections import defaultdict
from itertools import product
from pathlib import Path
import sympy as sp
sys.path.insert(0,'scripts')
import rcg004_complete_cubic_constructor as p4

PREREG='1122988893e9d5f87771da8a6390f031be8fafca'
PARENT_BASIS=[0,1,2,4,5,8]

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()
def add(o,p,c=1):
    for k,v in p.items():o[k]+=sp.Rational(c)*v
    return o
def ric(b,d):
    o=defaultdict(sp.Rational)
    for a in range(4):add(o,p4.rform(a,b,a,d))
    return {k:v for k,v in o.items() if v}
RIC=[[ric(b,d) for d in range(4)] for b in range(4)]
def scalarR():
    o=defaultdict(sp.Rational)
    for b in range(4):add(o,RIC[b][b])
    return {k:v for k,v in o.items() if v}
RS=scalarR()
def delta(a,b):return 1 if a==b else 0
def C(a,b,c,d):
    o=defaultdict(sp.Rational);add(o,p4.rform(a,b,c,d))
    add(o,RIC[d][b],-sp.Rational(1,2)*delta(a,c));add(o,RIC[c][b],sp.Rational(1,2)*delta(a,d))
    add(o,RIC[d][a],sp.Rational(1,2)*delta(b,c));add(o,RIC[c][a],-sp.Rational(1,2)*delta(b,d))
    add(o,RS,sp.Rational(1,6)*(delta(a,c)*delta(d,b)-delta(a,d)*delta(c,b)))
    return {k:v for k,v in o.items() if v}
def c3poly():
    o=defaultdict(sp.Rational)
    for a,b,c,d,e,f in product(range(4),repeat=6):
      x=C(a,b,c,d);y=C(a,b,e,f);z=C(e,f,c,d)
      if x and y and z:p4.p3(o,x,y,z)
    return {k:v for k,v in o.items() if v}
def express(poly):
    raw=list(p4.matchings(range(12)));reps,_=p4.canonical_classes(raw);U,mons=p4.universal_matrix([p4.universal_poly(m) for m in reps]);_,piv=U.rref();B=U[:,list(piv)]
    allm=sorted(set(mons)|set(poly));ix={m:i for i,m in enumerate(allm)};BB=sp.zeros(len(allm),B.cols);v=sp.zeros(len(allm),1);old={m:i for i,m in enumerate(mons)}
    for m,i in old.items():
      for j in range(B.cols):BB[ix[m],j]=B[i,j]
    for m,c in poly.items():v[ix[m],0]=c
    sol=sp.linsolve((BB,v));coord=sp.Matrix(next(iter(sol)))
    return list(piv),coord
def trace_checks():
    ok=True
    for b,d in product(range(4),repeat=2):
      o=defaultdict(sp.Rational)
      for a in range(4):add(o,C(a,b,a,d))
      if any(o.values()):ok=False
    sym=True
    for a,b,c,d in product(range(4),repeat=4):
      x=C(a,b,c,d)
      def eq(p,q):return all(sp.simplify(p.get(k,0)-q.get(k,0))==0 for k in set(p)|set(q))
      if not eq(x,{k:-v for k,v in C(b,a,c,d).items()}):sym=False;break
      if not eq(x,{k:-v for k,v in C(a,b,d,c).items()}):sym=False;break
      if not eq(x,C(c,d,a,b)):sym=False;break
    return ok,sym
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args();tr,sym=trace_checks();poly=c3poly();piv,coord=express(poly)
    c=json.loads(Path('results/raw/RCG006_MFR_L0_CANONICAL.json').read_text());rows=sp.Matrix([[sp.Rational(x) for x in r] for r in c['image_rref_rows']]);I=rows.T;x=sp.Matrix([0,0]+list(coord));base=I.rank();aug=I.row_join(x).rank()
    ell=I.T.nullspace()[0];d11=sp.zeros(8,1);d11[1]=1;cu8=sp.zeros(8,1);cu8[7]=1
    qx=(ell.T*x)[0];qd=(ell.T*d11)[0];qc=(ell.T*cu8)[0]
    checks={'weyl_trace_zero':tr,'weyl_pair_symmetries':sym,'parent_basis_lock':piv==PARENT_BASIS,'c3_nonzero':any(coord),'image_rank7':base==7,'c3_extends_image_to8':aug==8,'qeft_parent_dim1':c['Q_EFT_dimension']==1}
    res={'phase':'RCG006C_WEYL_CUBED_BRIDGE_CONSTRUCTOR','prereg_commit':PREREG,'run_head':a.run_head,'RCG004_coordinates':[str(v) for v in coord],'RCG005_coordinates':[str(v) for v in x],
      'C3_polynomial_sha256':sha({str(k):str(v) for k,v in poly.items()}),'image_rank':base,'rank_image_plus_C3':aug,'C3_in_image':aug==base,
      'quotient_covector':[str(v) for v in ell],'quotient_value_C3':str(qx),'quotient_value_D1D1_CLASS_11':str(qd),'quotient_value_RCG004_AXIS_8':str(qc),
      'C3_over_D1D1_CLASS_11_mod_image':str(sp.simplify(qx/qd)) if qd else None,'C3_over_RCG004_AXIS_8_mod_image':str(sp.simplify(qx/qc)) if qc else None,
      'checks':checks,'constructor_valid':all(checks.values()),'classification':'PASS_SCOPED_RCG006C_UNIQUE_EFT_CLASS_IS_PARITY_EVEN_WEYL_CUBED' if all(checks.values()) else 'INVALID_RCG006C_WEYL_BRIDGE','chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%'}
    res['scientific_payload_sha256']=sha(res);Path(a.output).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n');print(json.dumps({k:res[k] for k in ('RCG004_coordinates','rank_image_plus_C3','C3_in_image','C3_over_D1D1_CLASS_11_mod_image','classification')},sort_keys=True))
if __name__=='__main__':main()
