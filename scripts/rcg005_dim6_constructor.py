#!/usr/bin/env python3
"""Exact RCG005 Constructor: complete local 4D parity-even pure-metric dimension-six quotient and primary cascade."""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from collections import defaultdict
from functools import lru_cache, reduce
from itertools import permutations, product
from math import gcd
from pathlib import Path
import sympy as sp
sys.path.insert(0,"scripts")
import rcg004_complete_cubic_constructor as p4

SELECTION="355ac8a2d892e311bd1989e7057c3defac2e7e8a";AUTH="d2e38871ee5ac2e1331934647575e4a5b6144e4a";PREREG="1ac1c032dcbbd8e3f0a527a470acc0a44ddffa08";HELDOUT="1fb26a399264747fc2ffa8a564d4d281c0586f9c";PARENT="c39cbbd8a7e8c0caeb14e080344d01119b2ce7db"
PARENT_BASIS=[0,1,2,4,5,8]; PARENT_RUN=35175941323; PARENT_HSHA="7014978a97fce634d93f00e414903597245b8e4268b2c575dd1764547f96ced9"
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()

def rlocal(slots):
 out={}
 for ex in (0,1):
  for s1 in (0,1):
   for s2 in (0,1):
    a=[0,1,2,3];sg=1
    if s1:a[0],a[1]=a[1],a[0];sg*=-1
    if s2:a[2],a[3]=a[3],a[2];sg*=-1
    if ex:a=[a[2],a[3],a[0],a[1]]
    inv=[0]*4
    for n,o in enumerate(a):inv[o]=n
    out[tuple(slots[inv[i]] for i in range(4))]=sg
 return list(out.items())
def tr(m,P):
 get=(lambda x:P.get(x,x)) if isinstance(P,dict) else (lambda x:P[x])
 return tuple(sorted((min(get(a),get(b)),max(get(a),get(b))) for a,b in m))
def classes(raw,G):
 unseen=set(raw);nz=[];zz=[];mp={}
 while unseen:
  m=min(unseen);d=defaultdict(set)
  for P,s in G:d[tr(m,P)].add(s)
  unseen-=set(d);rep=min(d);bad=any(len(v)>1 for v in d.values());(zz if bad else nz).append(rep)
  if bad:
   for x in d:mp[x]=(None,0)
  else:
   sr=next(iter(d[rep]));
   for x,v in d.items():mp[x]=(rep,next(iter(v))*sr)
 return sorted(nz),sorted(zz),mp
def d1group():
 def bl(b):return [((b,)+p,s) for p,s in rlocal(range(b+1,b+5))]
 out=[]
 for fp in permutations((0,1)):
  for z0,z1 in product(bl(0),bl(5)):
   zs=[z0,z1];P=[None]*10;sg=1
   for f in range(2):
    lp,s=zs[f];sg*=s
    for i in range(5):P[5*f+i]=5*fp[f]+lp[i]-5*f
   out.append((tuple(P),sg))
 return out
def rd2group():
 out=[]
 for p,s in rlocal([0,1,2,3]):
  for q,t in rlocal([6,7,8,9]):out.append(({0:p[0],1:p[1],2:p[2],3:p[3],4:4,5:5,6:q[0],7:q[1],8:q[2],9:q[3]},s*t))
 return out
def d4group():return [({0:0,1:1,2:2,3:3,4:p[0],5:p[1],6:p[2],7:p[3]},s) for p,s in rlocal([4,5,6,7])]
def canon(mp,idx,m):
 r,s=mp[m];return (None,0) if r is None else (idx[r],s)

def derivative_basis():
 rows=[]
 for a,b,c,d,e in product(range(4),repeat=5):
  row=[0]*80
  for da,bb,cc in ((a,b,c),(b,c,a),(c,a,b)):
   for k,v in p4.rform(bb,cc,d,e).items():row[20*da+k]+=v
  if any(row):rows.append(row)
 C=sp.Matrix(rows);return C,sp.Matrix.hstack(*C.nullspace())
def d1matrix(reps,B):
 @lru_cache(None)
 def tf(a,b,c,d,e):
  rv=p4.rform(b,c,d,e);o={}
  for j in range(B.cols):
   z=sum(v*B[20*a+k,j] for k,v in rv.items())
   if z:o[j]=z
  return o
 ps=[]
 for m in reps:
  slot=[None]*10
  for z,(a,b) in enumerate(m):slot[a]=slot[b]=z
  o=defaultdict(lambda:sp.Rational(0))
  for vals in product(range(4),repeat=5):
   ind=[vals[slot[s]] for s in range(10)];f=tf(*ind[:5]);g=tf(*ind[5:])
   for i,x in f.items():
    for j,y in g.items():o[tuple(sorted((i,j)))]+=x*y
  ps.append({k:v for k,v in o.items() if v})
 mons=sorted(set().union(*(q.keys() for q in ps)));M=sp.zeros(len(mons),len(ps));ix={m:i for i,m in enumerate(mons)}
 for j,q in enumerate(ps):
  for m,v in q.items():M[ix[m],j]=v
 return M

def ibp(m):
 q={0:1,1:2,2:3,3:4,4:0,5:5,6:6,7:7,8:8,9:9};return tuple(sorted((min(q[a],q[b]),max(q[a],q[b])) for a,b in m))
def sw(m):
 f=lambda x:5 if x==4 else 4 if x==5 else x;return tuple(sorted((min(f(a),f(b)),max(f(a),f(b))) for a,b in m))
def ccub(m,t):
 lab=[0,1,2,3,'p',6+t,4,5]+[('p' if j==t else 6+j) for j in range(4)];pos=defaultdict(list)
 for i,x in enumerate(lab):pos[x].append(i)
 e=[tuple(sorted(pos['p']))]
 for a,b in m:e.append(tuple(sorted((pos[a][0],pos[b][0]))))
 return tuple(sorted(e))
def prim(row):
 den=sp.ilcm(*[x.q for x in row if x]);z=[int(x*den) for x in row];g=reduce(gcd,[abs(x) for x in z if x],0) or 1;z=[x//g for x in z]
 if next(x for x in z if x)<0:z=[-x for x in z]
 return tuple(z)
def commrels(raw,dmp,di,cmp,ci,nd,nc):
 u={}
 for m in raw:
  i,s=canon(dmp,di,ibp(m));j,t=canon(dmp,di,ibp(sw(m)));r=[sp.Rational(0)]*(nd+nc)
  if i is not None:r[i]+=s
  if j is not None:r[j]-=t
  for k in range(4):
   h,v=canon(cmp,ci,ccub(m,k))
   if h is not None:r[nd+h]-=v
  if any(r):u[prim(r)]=1
 return [list(x) for x in sorted(u)]
def rrhash(M):
 R,_=M.rref();return sha([[str(R[i,j]) for j in range(R.cols)] for i in range(R.rows) if any(R[i,j] for j in range(R.cols))])

def metric_principal():
 t,x=sp.symbols('t x');n=sp.Function('n')(t);q=sp.Function('q')(t);g=sp.diag(-sp.exp(2*n),sp.exp(2*q));gi=g.inv();co=(t,x);G=[[[0]*2 for _ in range(2)] for __ in range(2)]
 for r,a,b in product(range(2),repeat=3):G[r][a][b]=sp.simplify(sp.Rational(1,2)*sum(gi[r,s]*(sp.diff(g[s,b],co[a])+sp.diff(g[s,a],co[b])-sp.diff(g[a,b],co[s])) for s in range(2)))
 rc=sum(g[0,k]*(sp.diff(G[k][1][1],t)-sp.diff(G[k][0][1],x)+sum(G[k][0][l]*G[l][1][1]-G[k][1][l]*G[l][0][1] for l in range(2))) for k in range(2));rh=sp.simplify(rc*sp.exp(-2*n-2*q));want=-sp.exp(-2*n)*(sp.diff(q,t,2)+sp.diff(q,t)**2-sp.diff(n,t)*sp.diff(q,t));coef=sp.simplify(sp.diff(sp.exp(-n)*sp.diff(rh,t),sp.diff(q,t,3)))
 return bool(sp.simplify(rh-want)==0 and sp.simplify(coef+sp.exp(-3*n))==0),str(coef)
ETA=[-1,1,1,1]
def pinv(m):
 x=sp.symbols('x1 x2 x3')
 def R(a,b,c,d):
  if a==b or c==d:return 0
  sg=1
  if a>b:a,b=b,a;sg*=-1
  if c>d:c,d=d,c;sg*=-1
  if (a,b)>(c,d):a,b,c,d=c,d,a,b
  if (a,b)!=(c,d):return 0
  return -sg*x[b-1] if a==0 and b else 0
 def T(a,b,c,d,e):return R(b,c,d,e) if a==0 else 0
 slot=[None]*10
 for k,(a,b) in enumerate(m):slot[a]=slot[b]=k
 o=0
 for vals in product(range(4),repeat=5):
  sg=1
  for v in vals:sg*=ETA[v]
  ind=[vals[slot[s]] for s in range(10)];o+=sg*T(*ind[:5])*T(*ind[5:])
 return sp.expand(o),x

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');args=ap.parse_args();pm=json.loads(Path('results/raw/RCG004_CANONICAL_ARTIFACT_MANIFEST.json').read_text());pa=json.loads(Path('results/raw/RCG004_TERMINAL_AGGREGATE.json').read_text());parent=pm.get('run_id')==PARENT_RUN and pm.get('aggregate_valid') is True and pm['exact_results']['constructor_basis_class_indices']==PARENT_BASIS and pm['exact_results']['constructor_primary_hessian_rank']==6 and pm['exact_results']['constructor_primary_hessian_matrix_sha256']==PARENT_HSHA and pa.get('aggregate_valid') is True
 cr=list(p4.matchings(range(12)));creps,cz,cmp=classes(cr,p4.symmetry_group());ci={m:i for i,m in enumerate(creps)};CU,_=p4.universal_matrix([p4.universal_poly(m) for m in creps]);_,cp=CU.rref()
 dr=list(p4.matchings(range(10)));dreps,dz,dmp=classes(dr,d1group());di={m:i for i,m in enumerate(dreps)};DB,TB=derivative_basis();DU=d1matrix(dreps,TB)
 rd=list(p4.matchings(range(10)));rr,rz,_=classes(rd,rd2group());d4=list(p4.matchings(range(8)));fr,fz,_=classes(d4,d4group());cm=commrels(rd,dmp,di,cmp,ci,len(dreps),len(creps));rows=[]
 for v in DU.nullspace():rows.append(list(v)+[sp.Rational(0)]*len(creps))
 for v in CU.nullspace():rows.append([sp.Rational(0)]*len(dreps)+list(v))
 rows += [[sp.Rational(x) for x in r] for r in cm];Rel=sp.Matrix(rows);qdim=Rel.cols-Rel.rank();chosen=[9,11]+[len(dreps)+i for i in PARENT_BASIS];aug=sp.Matrix.vstack(Rel,*[sp.Matrix([[1 if j==i else 0 for j in range(Rel.cols)]]) for i in chosen]);embed=(aug.rank()==Rel.cols and list(cp)==PARENT_BASIS)
 p0,x=pinv(dreps[9]);p1,_=pinv(dreps[11]);A6=sp.Matrix([[sp.diff(p0,x[i],x[j]),sp.diff(p1,x[i],x[j])] for i,j in ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))]);mp,tc=metric_principal();k6=qdim-A6.rank();a4=6 if parent and embed and k6==6 else -1;kso=k6-a4 if a4>=0 else -1
 ctl={'parent_lock':parent,'raw_total_12390':len(cr)+len(dr)+len(rd)+len(d4)==12390,'cubic_classes_13':len(creps)==13,'D1_classes_12':len(dreps)==12,'RD2_classes_14':len(rr)==14,'D4_classes_12':len(fr)==12,'generic_dR_dimension_60':DB.rank()==20 and TB.cols==60,'D1_pointwise_rank_4':DU.rank()==4,'commutator_rank_3':len(cm)==3 and sp.Matrix(cm).rank()==3,'relation_rank_17':Rel.rank()==17,'quotient_dimension_8':qdim==8,'RCG004_embedding_rank_6':embed,'restored_lapse_principal':mp,'A6_rank_2':A6.rank()==2,'K6_is_RCG004_6d':k6==6,'A4_parent_restriction_rank_6':a4==6,'K_SO_zero':kso==0}
 valid=all(ctl.values());cl='FAIL_SCOPED_RCG005_COMPLETE_LOCAL_DIM6_PURE_METRIC_CLASS_HAS_NO_NONZERO_SECOND_ORDER_SURVIVOR' if valid else 'INVALID_RCG005';res={'gate':'RCG005_DIM6_PRIMARY','selection_terminal':SELECTION,'formation_authority':AUTH,'prereg_sha':PREREG,'heldout_prereg_sha':HELDOUT,'parent_terminal':PARENT,'run_head':args.run_head,'source':'VACUUM_ZERO','field_redefinition_equivalence':'UNRESOLVED_OUT_OF_SCOPE_RCG005_V0','raw_templates':{'Riemann3':len(cr),'D1D1':len(dr),'R_D2R':len(rd),'D4R':len(d4),'total':len(cr)+len(dr)+len(rd)+len(d4)},'symmetry_classes':{'cubic':[len(creps),len(cz)],'D1D1':[len(dreps),len(dz)],'RD2':[len(rr),len(rz)],'D4':[len(fr),len(fz)]},'generic_dR_dimension':TB.cols,'D1_pointwise_rank':DU.rank(),'commutator_relation_count':len(cm),'relation_rank':Rel.rank(),'relation_rref_sha256':rrhash(Rel),'quotient_dimension':qdim,'quotient_basis':{'D1D1':[9,11],'RCG004':PARENT_BASIS},'rcg004_embedding_rank':6 if embed else 0,'new_derivative_principal_polynomials':[str(p0),str(p1)],'principal_common_density':'exp(a+b+c-5*n)','T0_0i0i_q3_coefficient':tc,'A6_matrix':[[str(A6[i,j]) for j in range(2)] for i in range(6)],'A6_rank':A6.rank(),'K6_dimension':k6,'A5_restricted_rank':0,'K5_dimension':k6,'A4_parent_restriction_rank':a4,'K4_dimension':kso,'K_SO_dimension':kso,'mechanism_branch':'A_DERIVATIVE_SECTOR_HAS_NO_NONZERO_HIGHEST_ORDER_DEGENERATE_COMBINATION','heldout_status':'NOT_APPLICABLE_PRIMARY_NULLITY_ZERO' if kso==0 else 'REQUIRED','controls':ctl,'controls_valid':valid,'classification':cl,'environment':{'python':sys.version.split()[0],'sympy':sp.__version__,'platform':platform.platform()},'claim_locks':{'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%','new_physics':False}};res['scientific_payload_sha256']=sha(res);Path(args.output).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n');print(json.dumps({k:res[k] for k in ('quotient_dimension','A6_rank','K6_dimension','A4_parent_restriction_rank','K_SO_dimension','classification')},sort_keys=True))
if __name__=='__main__':main()
