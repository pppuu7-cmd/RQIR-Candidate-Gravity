import argparse, json, os
from fractions import Fraction as F

ETA=[F(-1),F(1),F(1),F(1)]
KS=[(1,2,3,4),(2,-1,1,3),(3,1,-2,4)]
RAYS=[(1,1),(2,-1),(1,-2),(-1,1),(-2,3),(3,2),(2,-5),(-3,4)]
ZS=[F(1,5),F(2,3),F(5,4)]
PAIRS=[(i,j) for i in range(4) for j in range(i,4)]

def zmat(): return [[F(0) for _ in range(4)] for __ in range(4)]
def eye(): return [[F(int(i==j)) for j in range(4)] for i in range(4)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(4)] for i in range(4)]
def scale(A,c): return [[c*A[i][j] for j in range(4)] for i in range(4)]
def eq(A,B): return all(A[i][j]==B[i][j] for i in range(4) for j in range(4))
def nonzero(A): return any(A[i][j] for i in range(4) for j in range(4))
def mm(A,B): return [[sum(A[i][r]*B[r][j] for r in range(4)) for j in range(4)] for i in range(4)]
def tr(A): return [[A[j][i] for j in range(4)] for i in range(4)]
def vec(A): return [A[i][j] for i,j in PAIRS]
def sym_seed(n):
 A=zmat()
 for q,(i,j) in enumerate(PAIRS):
  v=F(((n+2)*(q+3)+q*q+1)%11-5)
  A[i][j]=A[j][i]=v
 return A

def rank(M):
 A=[list(r) for r in M]; m=len(A); n=len(A[0]) if m else 0; r=0
 for c in range(n):
  p=next((i for i in range(r,m) if A[i][c]),None)
  if p is None: continue
  A[r],A[p]=A[p],A[r]; piv=A[r][c]; A[r]=[x/piv for x in A[r]]
  for i in range(m):
   if i!=r and A[i][c]:
    f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
  r+=1
 return r

def geom(k0):
 k=[F(x) for x in k0]; kup=[ETA[i]*k[i] for i in range(4)]; k2=sum(k[i]*kup[i] for i in range(4))
 assert k2!=0
 tm=eye(); tc=zmat(); tu=zmat()
 for i in range(4):
  for a in range(4): tm[i][a]-=k[i]*kup[a]/k2
  for j in range(4):
   tc[i][j]=F(int(i==j))*ETA[i]-k[i]*k[j]/k2
   tu[i][j]=F(int(i==j))*ETA[i]-kup[i]*kup[j]/k2
 return k,kup,k2,tm,tc,tu

def ptrans(T,g):
 tm=g[3]; return mm(mm(tm,T),tr(tm))
def theta_trace(T,g):
 tu=g[5]; return sum(tu[i][j]*T[i][j] for i in range(4) for j in range(4))
def p0(T,g,c=F(1,3)): return scale(g[4],c*theta_trace(T,g))
def p2(T,g): return sub(ptrans(T,g),p0(T,g))
def conserved(T,g):
 kup=g[1]; return all(sum(kup[i]*T[i][j] for i in range(4))==0 for j in range(4))
def op_matrix(fn,g):
 cols=[]
 for i,j in PAIRS:
  B=zmat(); B[i][j]=F(1); B[j][i]=F(1) if i!=j else F(1)
  cols.append(vec(fn(B,g)))
 return [[cols[c][r] for c in range(10)] for r in range(10)]
def compose_ok(f,h,g):
 for i,j in PAIRS:
  B=zmat(); B[i][j]=F(1); B[j][i]=F(1) if i!=j else F(1)
  if not eq(f(h(B,g),g), (f(B,g) if f is h else zmat())): return False
 return True

def ptt(a,b,z): return z*(F(-2)+F(b)*z/F(2))
def ps(a,b,z): return z*(F(6)+F(3)*F(3*a+b)*z)
def response(T,g,a,b,z):
 x,y=ptt(a,b,z),ps(a,b,z)
 if x==0 or y==0: return None
 return add(scale(p2(T,g),1/x),scale(p0(T,g),1/y))
def apply_O(R,g,a,b,z): return add(scale(p2(R,g),ptt(a,b,z)),scale(p0(R,g),ps(a,b,z)))

def lorentz_maps():
 out=[]
 def perm(p,sign=(1,1,1,1)):
  L=zmat()
  for i in range(4): L[i][p[i]]=F(sign[i])
  return L
 out.append(perm((0,1,2,3)))
 out += [perm((0,2,1,3)),perm((0,3,2,1)),perm((0,1,3,2))]
 out += [perm((0,1,2,3),(1,-1,1,1)),perm((0,1,2,3),(1,1,-1,1)),perm((0,1,2,3),(1,1,1,-1)),perm((0,1,2,3),(-1,1,1,1))]
 out += [perm((0,2,1,3),(1,1,1,-1)),perm((0,3,2,1),(1,1,-1,1)),perm((0,1,3,2),(1,-1,1,1)),perm((0,2,3,1))]
 return out

def eta_preserved(L):
 E=zmat()
 for i in range(4): E[i][i]=ETA[i]
 return eq(mm(mm(tr(L),E),L),E)
def transform(T,L): return mm(mm(L,T),tr(L))
def transform_vec(k,L): return [sum(L[i][j]*F(k[j]) for j in range(4)) for i in range(4)]

def stream(s):
 if s=='A':
  rows=[]; ok=True
  for k in KS:
   g=geom(k); M2=op_matrix(p2,g); M0=op_matrix(p0,g); MT=op_matrix(lambda T,gg:add(p2(T,gg),p0(T,gg)),g)
   id2=all(eq(p2(p2(sym_seed(n),g),g),p2(sym_seed(n),g)) for n in range(10))
   id0=all(eq(p0(p0(sym_seed(n),g),g),p0(sym_seed(n),g)) for n in range(10))
   orth=all(eq(p2(p0(sym_seed(n),g),g),zmat()) and eq(p0(p2(sym_seed(n),g),g),zmat()) for n in range(10))
   trans=all(sum(g[3][i][a]*F(k[a]) for a in range(4))==0 for i in range(4))
   r2,r0,rt=rank(M2),rank(M0),rank(MT); p=(id2 and id0 and orth and trans and (r2,r0,rt)==(5,1,6)); ok &= p
   rows.append({'k':k,'rank2':r2,'rank0':r0,'rankT':rt,'id2':id2,'id0':id0,'orth':orth,'transverse':trans,'pass':p})
  return {'stream':'A','valid':True,'rows':rows,'pass':ok}
 if s=='B':
  checks=0; ok=True
  for k in KS:
   g=geom(k)
   for n in range(8):
    T=ptrans(sym_seed(20+n),g); p=conserved(T,g) and eq(T,add(p2(T,g),p0(T,g))); ok &= p; checks+=1
    for a,b in RAYS:
     for z in ZS:
      R=response(T,g,a,b,z)
      if R is None: continue
      q=eq(apply_O(R,g,a,b,z),T); ok &= q; checks+=1
  return {'stream':'B','valid':True,'checks':checks,'pass':ok}
 if s=='C':
  checks=0; ok=True; T0=sym_seed(41)
  for L in lorentz_maps():
   ok &= eta_preserved(L); checks+=1
   for k in KS:
    g=geom(k); T=ptrans(T0,g); kp=transform_vec(k,L); gp=geom(kp); Tp=transform(T,L)
    q=eq(p2(Tp,gp),transform(p2(T,g),L)) and eq(p0(Tp,gp),transform(p0(T,g),L)); ok &= q; checks+=1
    a,b=RAYS[checks%len(RAYS)]; z=ZS[checks%len(ZS)]; R=response(T,g,a,b,z); Rp=response(Tp,gp,a,b,z)
    if R is not None and Rp is not None: q2=eq(Rp,transform(R,L)); ok &= q2; checks+=1
  return {'stream':'C','valid':True,'checks':checks,'pass':ok}
 if s=='D':
  g=geom(KS[0]); bad=sym_seed(77); c1=(not conserved(bad,g)) and (not eq(bad,add(p2(bad,g),p0(bad,g))))
  th=g[4]; malformed=p0(th,g,F(1,4)); c2=not eq(p0(malformed,g,F(1,4)),malformed)
  c3=not eq(th,p2(th,g))
  tt=p2(sym_seed(88),g); c4=nonzero(tt) and (not eq(tt,p0(tt,g)))
  ok=c1 and c2 and c3 and c4
  return {'stream':'D','valid':True,'nonconserved_rejected':c1,'malformed_p0_rejected':c2,'omit_p0_rejected':c3,'omit_p2_rejected':c4,'pass':ok}
 raise ValueError(s)

def aggregate(d):
 vals={}
 for s in 'ABCD':
  found=[]
  for root,_,fs in os.walk(d):
   for fn in fs:
    if fn==f'{s}.json': found.append(os.path.join(root,fn))
  if len(found)!=1: return {'valid':False,'classification':'INFRASTRUCTURE_OR_ARTIFACT_INVALID','found':{s:found}}
  vals[s]=json.load(open(found[0]))
 ok=all(vals[s].get('valid') and vals[s].get('pass') for s in 'ABCD')
 return {'gate':'ITER063_G65_FULL_CONSERVED_SOURCE_PROJECTOR','valid':True,'passes':{s:vals[s].get('pass') for s in 'ABCD'},'classification':'FOUR_DERIVATIVE_LINEARIZED_FULL_CONSERVED_SOURCE_PROJECTOR_DECOMPOSITION_SCOPED' if ok else 'SCIENTIFIC_FAIL','programme_readiness_percent':66,'theory_established_percent':0}

def emit(path,obj):
 os.makedirs(os.path.dirname(path) or '.',exist_ok=True)
 with open(path,'w') as f: json.dump(obj,f,indent=2,sort_keys=True)

p=argparse.ArgumentParser(); p.add_argument('--stream'); p.add_argument('--aggregate-dir'); p.add_argument('--out',required=True); a=p.parse_args()
emit(a.out,aggregate(a.aggregate_dir) if a.aggregate_dir else stream(a.stream))
