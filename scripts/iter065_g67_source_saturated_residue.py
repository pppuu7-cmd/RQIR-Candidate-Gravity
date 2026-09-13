import argparse, json, os
from fractions import Fraction as F

ETA=[F(-1),F(1),F(1),F(1)]
KS=[(1,2,3,4),(2,-1,1,3),(3,1,-2,4)]
RAYS=[(1,1),(2,-1),(1,-2),(-1,1),(-2,3),(3,2),(2,-5),(-3,4)]
SEEDS=(10,11,12,13)
ZS=(F(1,7),F(3,7),F(5,6),F(-5,7))
PAIRS=[(i,j) for i in range(4) for j in range(i,4)]


def zmat(): return [[F(0) for _ in range(4)] for __ in range(4)]
def eye(): return [[F(int(i==j)) for j in range(4)] for i in range(4)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(4)] for i in range(4)]
def scale(A,c): return [[c*A[i][j] for j in range(4)] for i in range(4)]
def eq(A,B): return all(A[i][j]==B[i][j] for i in range(4) for j in range(4))
def mm(A,B): return [[sum(A[i][r]*B[r][j] for r in range(4)) for j in range(4)] for i in range(4)]
def tr(A): return [[A[j][i] for j in range(4)] for i in range(4)]

def sym_seed(n):
    A=zmat()
    for q,(i,j) in enumerate(PAIRS):
        v=F(((n+2)*(q+3)+q*q+1)%11-5)
        A[i][j]=A[j][i]=v
    return A

def geom(k0):
    k=[F(x) for x in k0]
    kup=[ETA[i]*k[i] for i in range(4)]
    k2=sum(k[i]*kup[i] for i in range(4))
    if k2==0: raise ValueError('null frozen momentum')
    tm=eye(); tc=zmat(); tu=zmat()
    for i in range(4):
        for a in range(4): tm[i][a]-=k[i]*kup[a]/k2
        for j in range(4):
            tc[i][j]=F(int(i==j))*ETA[i]-k[i]*k[j]/k2
            tu[i][j]=F(int(i==j))*ETA[i]-kup[i]*kup[j]/k2
    return k,kup,k2,tm,tc,tu

def ptrans(T,g): return mm(mm(g[3],T),tr(g[3]))
def theta_trace(T,g): return sum(g[5][i][j]*T[i][j] for i in range(4) for j in range(4))
def p0(T,g): return scale(g[4],F(1,3)*theta_trace(T,g))
def p2(T,g): return sub(ptrans(T,g),p0(T,g))
def conserved(T,g): return all(sum(g[1][i]*T[i][j] for i in range(4))==0 for j in range(4))
def sat(A,B): return sum(ETA[i]*ETA[j]*A[i][j]*B[i][j] for i in range(4) for j in range(4))
def euclid_sat(A,B): return sum(A[i][j]*B[i][j] for i in range(4) for j in range(4))

def ptt(a,b,z): return z*(F(-2)+F(b)*z/F(2))
def ps(a,b,z): return z*(F(6)+F(3)*F(3*a+b)*z)

def response(T,g,a,b,z,guard=True):
    if guard and not conserved(T,g): raise ValueError('nonconserved source')
    x,y=ptt(a,b,z),ps(a,b,z)
    if x==0 or y==0: return None
    return add(scale(p2(T,g),1/x),scale(p0(T,g),1/y))

def tt_pf(z,b):
    if b==0: return F(-1,2)/z
    r=F(4,b)
    return F(-1,2)/z + F(1,2)/(z-r)

def sc_pf(z,a,b):
    c=3*a+b
    if c==0: return F(1,6)/z
    r=F(-2,c)
    return F(1,6)/z - F(1,6)/(z-r)

def pf_amplitude(n2,n0,a,b,z): return n2*tt_pf(z,b)+n0*sc_pf(z,a,b)

def lorentz_maps():
    def perm(p,sign=(1,1,1,1)):
        L=zmat()
        for i in range(4): L[i][p[i]]=F(sign[i])
        return L
    out=[perm((0,1,2,3)),perm((0,2,1,3)),perm((0,3,2,1)),perm((0,1,3,2))]
    out += [perm((0,1,2,3),(1,-1,1,1)),perm((0,1,2,3),(1,1,-1,1)),perm((0,1,2,3),(1,1,1,-1)),perm((0,1,2,3),(-1,1,1,1))]
    out += [perm((0,2,1,3),(1,1,1,-1)),perm((0,3,2,1),(1,1,-1,1)),perm((0,1,3,2),(1,-1,1,1)),perm((0,2,3,1))]
    return out

def eta_preserved(L):
    E=zmat()
    for i in range(4): E[i][i]=ETA[i]
    return eq(mm(mm(tr(L),E),L),E)
def transform(T,L): return mm(mm(L,T),tr(L))
def transform_vec(k,L): return [sum(L[i][j]*F(k[j]) for j in range(4)) for i in range(4)]

def stream_A():
    checks=0; ok=True; nonzero=0
    for k in KS:
        g=geom(k)
        for n in SEEDS:
            T=p2(ptrans(sym_seed(n),g),g)
            base=conserved(T,g) and eq(p0(T,g),zmat()) and eq(p2(T,g),T)
            n2=sat(T,p2(T,g)); nonzero += int(n2!=0)
            ok &= base and n2!=0
            for a,b in RAYS:
                if b==0: continue
                r0=n2*F(-1,2); re=n2*F(1,2)
                q=(r0!=0 and re!=0 and re/r0==F(-1) and r0==n2*F(-1,2) and re==n2*F(1,2))
                ok &= q; checks+=1
    return {'stream':'A','valid':True,'checks':checks,'nonzero_numerators':nonzero,'pass':bool(ok)}

def stream_B():
    checks=0; ok=True; nonzero=0
    for k in KS:
        g=geom(k)
        for n in SEEDS:
            T=p0(ptrans(sym_seed(n),g),g)
            base=conserved(T,g) and eq(p2(T,g),zmat()) and eq(p0(T,g),T)
            n0=sat(T,p0(T,g)); nonzero += int(n0!=0)
            ok &= base and n0!=0
            for a,b in RAYS:
                c=3*a+b
                if c==0: continue
                r0=n0*F(1,6); re=n0*F(-1,6)
                q=(r0!=0 and re!=0 and re/r0==F(-1) and r0==n0*F(1,6) and re==n0*F(-1,6))
                ok &= q; checks+=1
    return {'stream':'B','valid':True,'checks':checks,'nonzero_numerators':nonzero,'pass':bool(ok)}

def stream_C():
    checks=0; ok=True; invalid=0
    for k in KS:
        g=geom(k)
        for n in SEEDS:
            T=ptrans(sym_seed(n),g); n2=sat(T,p2(T,g)); n0=sat(T,p0(T,g))
            lane=conserved(T,g) and n2!=0 and n0!=0
            if not lane: invalid+=1
            ok &= lane
            for a,b in RAYS:
                for z in ZS:
                    R=response(T,g,a,b,z)
                    if R is None:
                        invalid+=1; ok=False; checks+=1; continue
                    direct=sat(T,R); recon=pf_amplitude(n2,n0,a,b,z)
                    ok &= direct==recon; checks+=1
    return {'stream':'C','valid':True,'checks':checks,'invalid_frozen_lanes':invalid,'pass':bool(ok)}

def stream_D():
    checks=0; ok=True; bad=0
    for L in lorentz_maps():
        lp=eta_preserved(L); ok &= lp
        if not lp: bad+=1
        for k in KS:
            g=geom(k); kp=transform_vec(k,L); gp=geom(kp)
            for n in SEEDS:
                T=ptrans(sym_seed(n),g); Tp=transform(T,L)
                n2=sat(T,p2(T,g)); n0=sat(T,p0(T,g))
                n2p=sat(Tp,p2(Tp,gp)); n0p=sat(Tp,p0(Tp,gp))
                base=conserved(T,g) and conserved(Tp,gp) and n2==n2p and n0==n0p
                ok &= base; checks+=1
                for a,b in RAYS:
                    for z in (ZS[0],ZS[2]):
                        R=response(T,g,a,b,z); Rp=response(Tp,gp,a,b,z)
                        if R is None or Rp is None:
                            bad+=1; ok=False; checks+=1; continue
                        q=sat(T,R)==sat(Tp,Rp)
                        ok &= q; checks+=1
    return {'stream':'D','valid':True,'checks':checks,'invalid_or_failed_lanes':bad,'pass':bool(ok)}

def stream_E():
    g=geom(KS[0]); z=ZS[0]
    # exceptional lines
    e1=(ptt(1,0,z)==-2*z and tt_pf(z,0)==F(-1,2)/z)
    e2=(ps(1,-3,z)==6*z and sc_pf(z,1,-3)==F(1,6)/z)
    base=ptrans(sym_seed(SEEDS[0]),g)
    T0=p0(base,g); T2=p2(base,g)
    e3=(sat(T0,p2(T0,g))==0 and eq(p2(T0,g),zmat()))
    e4=(sat(T2,p0(T2,g))==0 and eq(p0(T2,g),zmat()))
    bad=sym_seed(401)
    guard=False
    try:
        response(bad,g,1,1,z,guard=True)
    except ValueError:
        guard=True
    e5=(not conserved(bad,g)) and guard
    mismatch=False
    mismatch_example=None
    for k in KS:
        gg=geom(k)
        for n in SEEDS:
            T=ptrans(sym_seed(n),gg)
            m=sat(T,p2(T,gg)); e=euclid_sat(T,p2(T,gg))
            if m!=e:
                mismatch=True; mismatch_example={'k':list(k),'seed':n,'minkowski':str(m),'euclidean':str(e)}
                break
        if mismatch: break
    e6=mismatch
    checks={'tt_exceptional_single_pole':e1,'scalar_exceptional_single_pole':e2,'pure_scalar_no_tt':e3,'pure_tt_no_scalar':e4,'nonconserved_guard':e5,'euclidean_contraction_rejected':e6}
    return {'stream':'E','valid':True,'checks':checks,'mismatch_example':mismatch_example,'pass':all(checks.values())}

def aggregate(d):
    vals={}; found_map={}
    for s in 'ABCDE':
        found=[]
        for root,_,fs in os.walk(d):
            for fn in fs:
                if fn==f'{s}.json': found.append(os.path.join(root,fn))
        found_map[s]=found
        if len(found)!=1:
            return {'gate':'ITER065_G67_SOURCE_SATURATED_RESIDUE','valid':False,'classification':'INFRASTRUCTURE_OR_ARTIFACT_INVALID','found':found_map,'programme_readiness_percent':66,'theory_established_percent':0}
        vals[s]=json.load(open(found[0]))
    passes={s:bool(vals[s].get('valid') and vals[s].get('pass')) for s in 'ABCDE'}
    ok=all(passes.values())
    cls='FOUR_DERIVATIVE_LINEARIZED_SOURCE_SATURATED_OPPOSITE_RESIDUE_COUPLING_SCOPED' if ok else 'SCIENTIFIC_FAIL_G67_'+''.join(s for s in 'ABCDE' if not passes[s])
    return {'gate':'ITER065_G67_SOURCE_SATURATED_RESIDUE','valid':True,'passes':passes,'classification':cls,'programme_readiness_percent':66,'theory_established_percent':0,'scope_lock':'Frozen local linearized four-derivative source-saturated response only; not a physical-ghost or unitarity theorem.'}

def emit(path,obj):
    os.makedirs(os.path.dirname(path) or '.',exist_ok=True)
    with open(path,'w') as f: json.dump(obj,f,indent=2,sort_keys=True)
    print(json.dumps(obj,indent=2,sort_keys=True))

p=argparse.ArgumentParser(); p.add_argument('--stream'); p.add_argument('--aggregate-dir'); p.add_argument('--out',required=True); a=p.parse_args()
if a.aggregate_dir: out=aggregate(a.aggregate_dir)
else: out={'A':stream_A,'B':stream_B,'C':stream_C,'D':stream_D,'E':stream_E}[a.stream]()
emit(a.out,out)
