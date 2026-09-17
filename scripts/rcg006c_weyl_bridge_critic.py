#!/usr/bin/env python3
"""Independent RCG006C Weyl-cubed bridge Critic via bivector trace(C^3)."""
from __future__ import annotations
import argparse, hashlib, json, sys
from collections import defaultdict
from itertools import product
from pathlib import Path
import sympy as sp
sys.path.insert(0,'scripts')
import rcg004_complete_cubic_constructor as p4
PAIRS=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()
def add(o,p,c=1):
    for k,v in p.items():o[k]+=sp.Rational(c)*v
    return o
def ric(b,d):
    o=defaultdict(lambda: sp.Rational(0))
    for a in range(4):add(o,p4.rform(a,b,a,d))
    return {k:v for k,v in o.items() if v}
RIC=[[ric(b,d) for d in range(4)] for b in range(4)]
RS={}
_o=defaultdict(lambda: sp.Rational(0))
for b in range(4):add(_o,RIC[b][b])
RS={k:v for k,v in _o.items() if v}
def C(a,b,c,d):
    o=defaultdict(lambda: sp.Rational(0));add(o,p4.rform(a,b,c,d));D=lambda x,y:1 if x==y else 0
    add(o,RIC[d][b],-sp.Rational(1,2)*D(a,c));add(o,RIC[c][b],sp.Rational(1,2)*D(a,d));add(o,RIC[d][a],sp.Rational(1,2)*D(b,c));add(o,RIC[c][a],-sp.Rational(1,2)*D(b,d));add(o,RS,sp.Rational(1,6)*(D(a,c)*D(d,b)-D(a,d)*D(c,b)))
    return {k:v for k,v in o.items() if v}
def bivector_c3():
    o=defaultdict(lambda: sp.Rational(0))
    for p,q,r in product(range(6),repeat=3):
      a,b=PAIRS[p];c,d=PAIRS[q];e,f=PAIRS[r];x=C(a,b,c,d);y=C(c,d,e,f);z=C(e,f,a,b)
      if x and y and z:p4.p3(o,x,y,z)
    return {k:v for k,v in o.items() if v}
def express(poly):
    raw=list(reversed(list(p4.matchings(range(12)))));reps,_=p4.canonical_classes(raw);U,mons=p4.universal_matrix([p4.universal_poly(m) for m in reps]);_,piv=U.rref();B=U[:,list(piv)]
    allm=sorted(set(mons)|set(poly));ix={m:i for i,m in enumerate(allm)};BB=sp.zeros(len(allm),B.cols);v=sp.zeros(len(allm),1);old={m:i for i,m in enumerate(mons)}
    for m,i in old.items():
      for j in range(B.cols):BB[ix[m],j]=B[i,j]
    for m,c in poly.items():v[ix[m],0]=c
    return list(piv),sp.Matrix(next(iter(sp.linsolve((BB,v)))))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args();poly=bivector_c3();piv,coord=express(poly)
    c=json.loads(Path('results/raw/RCG006_MFR_L0_CANONICAL.json').read_text());I=sp.Matrix([[sp.Rational(x) for x in r] for r in c['image_rref_rows']]).T;x=sp.Matrix([0,0]+list(coord));aug=I.row_join(x).rank();ell=I.T.nullspace()[0];qx=(ell.T*x)[0]
    checks={'parent_basis_lock':piv==[0,1,2,4,5,8],'bivector_C3_nonzero':any(coord),'image_rank7':I.rank()==7,'bivector_C3_extends_image_to8':aug==8,'qeft_dim1':c['Q_EFT_dimension']==1,'quotient_value_nonzero':qx!=0}
    res={'phase':'RCG006C_WEYL_CUBED_BRIDGE_CRITIC','run_head':a.run_head,'bivector_RCG004_coordinates':[str(v) for v in coord],'bivector_RCG005_coordinates':[str(v) for v in x],'bivector_C3_polynomial_sha256':sha({str(k):str(v) for k,v in poly.items()}),'rank_image_plus_C3':aug,'C3_in_image':aug==I.rank(),'quotient_value_C3':str(qx),'checks':checks,'critic_valid':all(checks.values()),'classification':'PASS_SCOPED_RCG006C_UNIQUE_EFT_CLASS_IS_PARITY_EVEN_WEYL_CUBED' if all(checks.values()) else 'INVALID_RCG006C_WEYL_BRIDGE','chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%'}
    res['scientific_payload_sha256']=sha(res);Path(a.output).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n');print(json.dumps({k:res[k] for k in ('bivector_RCG004_coordinates','rank_image_plus_C3','C3_in_image','classification')},sort_keys=True))
if __name__=='__main__':main()
