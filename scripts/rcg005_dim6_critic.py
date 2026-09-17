#!/usr/bin/env python3
"""Independent RCG005 Critic: reverse pairings, selfdual cubic route, normal-coordinate metric-third-jet derivative route."""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from collections import defaultdict
from functools import reduce
from itertools import combinations_with_replacement, permutations, product
from math import gcd
from pathlib import Path
import sympy as sp

SELECTION="355ac8a2d892e311bd1989e7057c3defac2e7e8a";AUTH="d2e38871ee5ac2e1331934647575e4a5b6144e4a";PREREG="1ac1c032dcbbd8e3f0a527a470acc0a44ddffa08";HELDOUT="1fb26a399264747fc2ffa8a564d4d281c0586f9c";PARENT="c39cbbd8a7e8c0caeb14e080344d01119b2ce7db"
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def pairings(rem):
 rem=list(rem)
 if not rem:yield ();return
 x=max(rem);rest=[q for q in rem if q!=x]
 for y in reversed(rest):
  r=[q for q in rest if q!=y]
  for t in pairings(r):yield tuple(sorted(t+((min(x,y),max(x,y)),)))
def local4():
 out=[]
 for ex in (0,1):
  for s1 in (0,1):
   for s2 in (0,1):
    a=[0,1,2,3];sg=1
    if s1:a[0],a[1]=a[1],a[0];sg*=-1
    if s2:a[2],a[3]=a[3],a[2];sg*=-1
    if ex:a=[a[2],a[3],a[0],a[1]]
    inv=[0]*4
    for n,o in enumerate(a):inv[o]=n
    out.append((tuple(inv),sg))
 return out
LS=local4()
def cgroup():
 out=[]
 for fp in permutations((0,1,2)):
  for l0,l1,l2 in product(LS,repeat=3):
   ls=[l0,l1,l2];P=[None]*12;sg=1
   for f in range(3):
    lp,s=ls[f];sg*=s
    for i in range(4):P[4*f+i]=4*fp[f]+lp[i]
   out.append((tuple(P),sg))
 return out
def dgroup():
 out=[]
 for fp in permutations((0,1)):
  for l0,l1 in product(LS,repeat=2):
   ls=[l0,l1];P=[None]*10;sg=1
   for f in range(2):
    lp,s=ls[f];sg*=s;P[5*f]=5*fp[f]
    for i in range(4):P[5*f+1+i]=5*fp[f]+1+lp[i]
   out.append((tuple(P),sg))
 return out
def tr(m,P):return tuple(sorted((min(P[a],P[b]),max(P[a],P[b])) for a,b in m))
def classes(raw,G):
 unseen=set(raw);nz=[];zz=[];mp={}
 while unseen:
  m=max(unseen);d=defaultdict(set)
  for P,s in G:d[tr(m,P)].add(s)
  unseen-=set(d);rep=min(d);bad=any(len(v)>1 for v in d.values());(zz if bad else nz).append(rep)
  if bad:
   for x in d:mp[x]=(None,0)
  else:
   sr=next(iter(d[rep]))
   for x,v in d.items():mp[x]=(rep,next(iter(v))*sr)
 return sorted(nz),sorted(zz),mp
# Independent selfdual/anti-selfdual 20D curvature parameterization.
U=sp.Matrix([[1,0,0,1,0,0],[0,1,0,0,1,0],[0,0,1,0,0,1],[0,0,1,0,0,-1],[0,-1,0,0,1,0],[1,0,0,-1,0,0]])
X=sp.symbols('x0:20');it=iter(X);A=sp.zeros(3,3);B=sp.zeros(3,3);C=sp.zeros(3,3)
for i in range(3):
 for j in range(i,3):z=next(it);A[i,j]=A[j,i]=z
for i in range(3):
 for j in range(3):B[i,j]=next(it)
for i,j in ((0,0),(0,1),(0,2),(1,1),(1,2)):
 z=next(it);C[i,j]=C[j,i]=z
C[2,2]=sp.trace(A)-C[0,0]-C[1,1];S=sp.expand(U*A.row_join(B).col_join(B.T.row_join(C))*U.T);XI={x:i for i,x in enumerate(X)}
SF={}
for i,j in product(range(6),repeat=2):
 p=sp.Poly(S[i,j],*X,domain=sp.QQ);SF[(i,j)]={XI[x]:int(p.coeff_monomial(x)) for x in X if p.coeff_monomial(x)}
PAIRS=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)];PI={p:i for i,p in enumerate(PAIRS)}
def op(a,b):
 if a==b:return None,0
 return (PI[(a,b)],1) if a<b else (PI[(b,a)],-1)
def rf(a,b,c,d):
 p,s=op(a,b);q,t=op(c,d)
 if p is None or q is None:return{}
 return {k:s*t*v for k,v in SF[(p,q)].items()}
def cpoly(m):
 slot=[None]*12
 for e,(a,b) in enumerate(m):slot[a]=slot[b]=e
 o=defaultdict(int)
 for vals in product(range(4),repeat=6):
  ind=[vals[slot[s]] for s in range(12)];fs=[rf(*ind[k:k+4]) for k in (0,4,8)]
  if not all(fs):continue
  for i,x in fs[0].items():
   for j,y in fs[1].items():
    for k,z in fs[2].items():o[tuple(sorted((i,j,k)))]+=x*y*z
 return {k:v for k,v in o.items() if v}
def pmat(ps):
 mons=sorted(set().union(*(p.keys() for p in ps)));M=sp.zeros(len(mons),len(ps));ix={m:i for i,m in enumerate(mons)}
 for j,p in enumerate(ps):
  for m,v in p.items():M[ix[m],j]=v
 return M
# Normal-coordinate metric third jets, 10 symmetric metric pairs x 20 symmetric derivative triples = 200 exact variables.
PAIR=list(combinations_with_replacement(range(4),2));TRI=list(combinations_with_replacement(range(4),3));HID={p+t:i for i,(p,t) in enumerate(product(PAIR,TRI))}
def h(mu,nu,a,b,c):return {HID[tuple(sorted((mu,nu)))+tuple(sorted((a,b,c)))]:1}
def ladd(*terms):
 o=defaultdict(lambda:sp.Rational(0))
 for z,f in terms:
  for k,v in f.items():o[k]+=z*v
 return {k:v for k,v in o.items() if v}
def jt(l,a,b,c,d):
 z=sp.Rational(1,2);return ladd((z,h(a,d,b,c,l)),(z,h(b,c,a,d,l)),(-z,h(a,c,b,d,l)),(-z,h(b,d,a,c,l)))
def dpoly(m):
 slot=[None]*10
 for e,(a,b) in enumerate(m):slot[a]=slot[b]=e
 o=defaultdict(lambda:sp.Rational(0))
 for vals in product(range(4),repeat=5):
  ind=[vals[slot[s]] for s in range(10)];f=jt(*ind[:5]);g=jt(*ind[5:])
  for i,x in f.items():
   for j,y in g.items():o[tuple(sorted((i,j)))]+=x*y
 return {k:v for k,v in o.items() if v}
def canon(mp,idx,m):
 r,s=mp[m];return (None,0) if r is None else (idx[r],s)
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
def comm(raw,dmp,di,cmp,ci,nd,nc):
 u={}
 for m in reversed(raw):
  i,s=canon(dmp,di,ibp(m));j,t=canon(dmp,di,ibp(sw(m)));r=[sp.Rational(0)]*(nd+nc)
  if i is not None:r[i]+=s
  if j is not None:r[j]-=t
  for k in range(4):
   z,v=canon(cmp,ci,ccub(m,k))
   if z is not None:r[nd+z]-=v
  if any(r):u[prim(r)]=1
 return [list(x) for x in sorted(u)]
def rrhash(M):
 R,_=M.rref();return sha([[str(R[i,j]) for j in range(R.cols)] for i in range(R.rows) if any(R[i,j] for j in range(R.cols))])
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
  for q in vals:sg*=ETA[q]
  ind=[vals[slot[s]] for s in range(10)];o+=sg*T(*ind[:5])*T(*ind[5:])
 return sp.expand(o),x

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');args=ap.parse_args()
 cr=list(pairings(range(12)));creps,cz,cmp=classes(cr,cgroup());ci={m:i for i,m in enumerate(creps)};CM=pmat([cpoly(m) for m in creps]);cn=CM.nullspace()
 dr=list(pairings(range(10)));dreps,dz,dmp=classes(dr,dgroup());di={m:i for i,m in enumerate(dreps)};DM=pmat([dpoly(m) for m in dreps]);dn=DM.nullspace();cm=comm(dr,dmp,di,cmp,ci,len(dreps),len(creps));rows=[]
 for v in dn:rows.append(list(v)+[sp.Rational(0)]*len(creps))
 for v in cn:rows.append([sp.Rational(0)]*len(dreps)+list(v))
 rows += [[sp.Rational(x) for x in r] for r in cm];Rel=sp.Matrix(rows);qdim=Rel.cols-Rel.rank()
 p0,x=pinv(dreps[9]);p1,_=pinv(dreps[11]);A6=sp.Matrix([[sp.diff(p0,x[i],x[j]),sp.diff(p1,x[i],x[j])] for i,j in ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))]);parent=json.loads(Path('results/raw/RCG004_CANONICAL_ARTIFACT_MANIFEST.json').read_text());parentok=parent.get('aggregate_valid') is True and parent['exact_results']['constructor_primary_hessian_rank']==6
 ctl={'reverse_raw_cubic_10395':len(cr)==10395,'cubic_classes_13':len(creps)==13,'selfdual_cubic_rank_6':CM.rank()==6,'normal_coordinate_metric_jet_count_200':len(HID)==200,'normal_coordinate_D1_rank_4':DM.rank()==4,'D1_classes_12':len(dreps)==12,'commutator_rank_3':len(cm)==3 and sp.Matrix(cm).rank()==3,'relation_rank_17':Rel.rank()==17,'quotient_dimension_8':qdim==8,'A6_rank_2':A6.rank()==2,'parent_rcg004_rank6_lock':parentok};valid=all(ctl.values());res={'lane':'INDEPENDENT_CRITIC','selection_terminal':SELECTION,'formation_authority':AUTH,'prereg_sha':PREREG,'heldout_prereg_sha':HELDOUT,'parent_terminal':PARENT,'run_head':args.run_head,'method':'REVERSE_PAIRINGS_SELFDUAL_CUBIC_NORMAL_COORDINATE_200_METRIC_THIRD_JETS','constructor_not_imported':True,'raw_counts':{'cubic':len(cr),'D1D1':len(dr)},'class_counts':{'cubic_nonzero':len(creps),'D1D1_nonzero':len(dreps)},'cubic_rank':CM.rank(),'D1D1_pointwise_rank':DM.rank(),'commutator_relation_count':len(cm),'relation_rank':Rel.rank(),'relation_rref_sha256':rrhash(Rel),'quotient_dimension':qdim,'A6_rank':A6.rank(),'K6_dimension':qdim-A6.rank(),'parent_A4_restriction_rank':6 if parentok else -1,'K_SO_dimension':0 if valid else -1,'controls':ctl,'controls_valid':valid,'classification':'PASS_INDEPENDENT_CRITIC_RCG005_QUOTIENT_AND_PRIMARY_NULLITY_ZERO' if valid else 'INVALID_RCG005','source':'VACUUM_ZERO','environment':{'python':sys.version.split()[0],'sympy':sp.__version__,'platform':platform.platform()},'claim_locks':{'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%','new_physics':False}};res['scientific_payload_sha256']=sha(res);Path(args.output).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n');print(json.dumps({k:res[k] for k in ('cubic_rank','D1D1_pointwise_rank','relation_rank','quotient_dimension','A6_rank','K_SO_dimension','classification')},sort_keys=True))
if __name__=='__main__':main()
