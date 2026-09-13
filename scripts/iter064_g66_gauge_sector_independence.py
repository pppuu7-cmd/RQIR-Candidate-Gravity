import argparse,json,os
from fractions import Fraction as F
ETA=[F(-1),F(1),F(1),F(1)]
KS=[(1,2,3,4),(2,-1,1,3),(3,1,-2,4)]
RAYS=[(1,1),(2,-1),(1,-2),(-1,1),(-2,3),(3,2),(2,-5),(-3,4)]
ZS=[F(1,5),F(2,3),F(5,4)]
GPS=[(F(0),F(0),F(0)),(F(1),F(2),F(-1)),(F(-3),F(1),F(4)),(F(5),F(-2),F(3)),(F(1,2),F(-3,2),F(5,3)),(F(-7,3),F(2,5),F(11,4))]

def Z(): return [[F(0) for _ in range(4)] for __ in range(4)]
def I(): return [[F(int(i==j)) for j in range(4)] for i in range(4)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(4)] for i in range(4)]
def sc(A,c): return [[c*A[i][j] for j in range(4)] for i in range(4)]
def eq(A,B): return all(A[i][j]==B[i][j] for i in range(4) for j in range(4))
def nz(A): return any(A[i][j] for i in range(4) for j in range(4))
def mm(A,B): return [[sum(A[i][r]*B[r][j] for r in range(4)) for j in range(4)] for i in range(4)]
def tr(A): return [[A[j][i] for j in range(4)] for i in range(4)]
def seed(n):
 A=Z(); q=0
 for i in range(4):
  for j in range(i,4):
   v=F(((n+3)*(q+2)+q*q+2)%13-6); A[i][j]=A[j][i]=v; q+=1
 return A

def geom(k0):
 k=[F(x) for x in k0]; ku=[ETA[i]*k[i] for i in range(4)]; k2=sum(k[i]*ku[i] for i in range(4)); tm=I(); tc=Z(); tu=Z()
 for i in range(4):
  for a in range(4): tm[i][a]-=k[i]*ku[a]/k2
  for j in range(4):
   tc[i][j]=F(int(i==j))*ETA[i]-k[i]*k[j]/k2; tu[i][j]=F(int(i==j))*ETA[i]-ku[i]*ku[j]/k2
 return k,ku,k2,tm,tc,tu

def pt(T,g): return mm(mm(g[3],T),tr(g[3]))
def thtr(T,g): return sum(g[5][i][j]*T[i][j] for i in range(4) for j in range(4))
def p0(T,g): return sc(g[4],thtr(T,g)/3)
def p2(T,g): return sub(pt(T,g),p0(T,g))
def cons(T,g): return all(sum(g[1][i]*T[i][j] for i in range(4))==0 for j in range(4))
def qop(T,g,p):
 a,b,c=p; k,ku,k2=g[0],g[1],g[2]; V=[sum(ku[i]*T[i][j] for i in range(4)) for j in range(4)]; S=sum(ku[j]*V[j] for j in range(4)); Q=Z()
 for m in range(4):
  for n in range(4): Q[m][n]=a*(k[m]*V[n]+k[n]*V[m])+b*k[m]*k[n]*S/k2+c*F(int(m==n))*ETA[m]*S
 return Q

def ptt(a,b,z): return z*(F(-2)+F(b)*z/2)
def ps(a,b,z): return z*(F(6)+F(3)*F(3*a+b)*z)
def resp(T,g,a,b,z):
 x,y=ptt(a,b,z),ps(a,b,z)
 if x==0 or y==0:return None
 return add(sc(p2(T,g),1/x),sc(p0(T,g),1/y))
def Ls():
 def mk(p,s=(1,1,1,1)):
  L=Z()
  for i in range(4):L[i][p[i]]=F(s[i])
  return L
 return [mk((0,1,2,3)),mk((0,2,1,3)),mk((0,3,2,1)),mk((0,1,3,2)),mk((0,1,2,3),(1,-1,1,1)),mk((0,1,2,3),(1,1,-1,1)),mk((0,1,2,3),(1,1,1,-1)),mk((0,1,2,3),(-1,1,1,1)),mk((0,2,1,3),(1,1,1,-1)),mk((0,3,2,1),(1,1,-1,1)),mk((0,1,3,2),(1,-1,1,1)),mk((0,2,3,1))]
def tx(T,L): return mm(mm(L,T),tr(L))
def tv(k,L): return [sum(L[i][j]*F(k[j]) for j in range(4)) for i in range(4)]

def stream(s):
 if s=='A':
  n=0;ok=True
  for k in KS:
   g=geom(k)
   for r in range(10):
    T=pt(seed(100+r),g); ok &= cons(T,g)
    for p in GPS: ok &= eq(qop(T,g,p),Z()); n+=1
  return {'stream':'A','valid':True,'checks':n,'pass':ok}
 if s=='B':
  n=0;ok=True
  for k in KS:
   g=geom(k)
   for r in range(6):
    T=pt(seed(200+r),g)
    for a,b in RAYS:
     for z in ZS:
      R=resp(T,g,a,b,z)
      if R is None: continue
      for p in GPS: ok &= eq(R,add(R,qop(T,g,p))); n+=1
  return {'stream':'B','valid':True,'checks':n,'pass':ok}
 if s=='C':
  n=0;ok=True
  for L in Ls():
   for k in KS:
    g=geom(k); T=pt(seed(301),g); kp=tv(k,L); gp=geom(kp); Tp=tx(T,L)
    for p in GPS[1:]: ok &= eq(qop(Tp,gp,p),tx(qop(T,g,p),L)); n+=1
  return {'stream':'C','valid':True,'checks':n,'pass':ok}
 if s=='D':
  g=geom(KS[0]); bad=seed(401); c1=(not cons(bad,g)) and any(nz(qop(bad,g,p)) for p in GPS[1:]); T=pt(seed(402),g); qwrong=sc([[F(int(i==j))*ETA[i] for j in range(4)] for i in range(4)],thtr(T,g)); c2=nz(qwrong)
  wrong_cons=all(sum(g[0][i]*T[i][j] for i in range(4))==0 for j in range(4)); c3=(wrong_cons != cons(T,g)) or any((sum(g[0][i]*pt(seed(450+r),g)[i][j] for i in range(4))==0)!=(sum(g[1][i]*pt(seed(450+r),g)[i][j] for i in range(4))==0) for r in range(6) for j in range(4))
  return {'stream':'D','valid':True,'nonconserved_detected':c1,'wrong_nonlongitudinal_detected':c2,'index_position_control_detected':c3,'pass':c1 and c2 and c3}
 raise ValueError

def agg(d):
 vals={}
 for s in 'ABCD':
  fs=[]
  for root,_,names in os.walk(d):
   for f in names:
    if f==s+'.json':fs.append(os.path.join(root,f))
  if len(fs)!=1:return {'valid':False,'classification':'INFRASTRUCTURE_OR_ARTIFACT_INVALID'}
  vals[s]=json.load(open(fs[0]))
 ok=all(vals[s].get('valid') and vals[s].get('pass') for s in 'ABCD')
 return {'gate':'ITER064_G66_GAUGE_SECTOR_INDEPENDENCE','valid':True,'passes':{s:vals[s].get('pass') for s in 'ABCD'},'classification':'FOUR_DERIVATIVE_LINEARIZED_CONSERVED_SOURCE_GAUGE_SECTOR_INDEPENDENCE_SCOPED' if ok else 'SCIENTIFIC_FAIL','programme_readiness_percent':66,'theory_established_percent':0}
def emit(p,o):
 os.makedirs(os.path.dirname(p) or '.',exist_ok=True);json.dump(o,open(p,'w'),indent=2,sort_keys=True)
p=argparse.ArgumentParser();p.add_argument('--stream');p.add_argument('--aggregate-dir');p.add_argument('--out',required=True);a=p.parse_args();emit(a.out,agg(a.aggregate_dir) if a.aggregate_dir else stream(a.stream))
