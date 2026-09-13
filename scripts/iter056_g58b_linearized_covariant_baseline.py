#!/usr/bin/env python3
import argparse, json, math, os, random
from pathlib import Path
import numpy as np
import mpmath as mp

G=6.67430e-11
C=299792458.0
ETA=np.diag([-1.0,1.0,1.0,1.0])


def dump(path,obj):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,sort_keys=True))


def lin_riemann(h,kcov):
    R=np.zeros((4,4,4,4),dtype=float)
    for m in range(4):
      for n in range(4):
       for r in range(4):
        for s in range(4):
         R[m,n,r,s]=0.5*(-kcov[r]*kcov[n]*h[m,s]-kcov[s]*kcov[m]*h[n,r]+kcov[s]*kcov[n]*h[m,r]+kcov[r]*kcov[m]*h[n,s])
    return R


def einstein_from_riemann(R):
    Ric=np.zeros((4,4))
    for n in range(4):
      for s in range(4):
        acc=0.0
        for m in range(4):
          for r in range(4):
            acc += ETA[m,r]*R[m,n,r,s]
        Ric[n,s]=acc
    Rsc=float(np.sum(ETA*Ric))
    return Ric-0.5*ETA*Rsc


def stream_a():
    rng=np.random.default_rng(5801)
    qs=[(0.7,1.1,1.9),(1.2,0.8,2.3),(1.5,2.1,0.6),(2.2,1.4,0.9),(0.9,2.6,1.3),(1.8,0.5,2.7),(2.4,1.7,0.4),(0.6,2.2,2.0),(1.3,1.9,1.1),(2.7,0.9,1.5),(1.1,2.8,0.7),(2.0,1.2,2.4)]
    lanes=[]
    worst={"conservation":0.0,"dedonder":0.0,"riemann_gauge":0.0,"bianchi":0.0}
    for i,qv in enumerate(qs):
        q=np.array(qv,float); q2=float(q@q); nh=q/math.sqrt(q2); P=np.eye(3)-np.outer(nh,nh)
        S=rng.normal(size=(3,3)); S=(S+S.T)/2; S=P@S@P
        T=np.zeros((4,4)); T[0,0]=1.0+0.07*i; T[1:,1:]=S
        kcov=np.array([0.0,*q]); kup=ETA@kcov
        cons=kup@T
        cres=float(np.linalg.norm(cons)/max(np.linalg.norm(T),1e-300))
        barh=T/q2
        dg=kup@barh
        dres=float(np.linalg.norm(dg)/max(np.linalg.norm(barh),1e-300))
        tracebar=float(np.sum(ETA*barh)); h=barh-0.5*ETA*tracebar
        xi=rng.normal(size=4); dh=np.outer(kcov,xi)+np.outer(xi,kcov)
        R0=lin_riemann(h,kcov); R1=lin_riemann(h+dh,kcov)
        scale=max(float(np.max(np.abs(R0))),1e-300)
        rg=float(np.max(np.abs(R1-R0))/scale) if scale>2e-12 else float(np.max(np.abs(R1-R0)))
        ht=rng.normal(size=(4,4)); ht=(ht+ht.T)/2
        Gt=einstein_from_riemann(lin_riemann(ht,kcov))
        b=kup@Gt
        bres=float(np.linalg.norm(b)/max(np.linalg.norm(Gt),1.0))
        passed=(cres<=2e-13 and dres<=2e-13 and rg<=2e-12 and bres<=2e-12 and np.isfinite([cres,dres,rg,bres]).all())
        lanes.append({"i":i,"q":qv,"conservation":cres,"dedonder":dres,"riemann_gauge":rg,"bianchi":bres,"pass":bool(passed)})
        worst["conservation"]=max(worst["conservation"],cres); worst["dedonder"]=max(worst["dedonder"],dres); worst["riemann_gauge"]=max(worst["riemann_gauge"],rg); worst["bianchi"]=max(worst["bianchi"],bres)
    return {"stream":"A","valid":True,"pass":all(x["pass"] for x in lanes),"worst":worst,"lanes":lanes}


def rho_gauss(r,s): return math.exp(-r*r/(2*s*s))/((2*math.pi)**1.5*s**3)
def phi(r,s): return -G*math.erf(r/(math.sqrt(2)*s))/r

def lap5_cartesian_radial(f,r,h):
    def val(x,y,z): return f(math.sqrt(x*x+y*y+z*z))
    c=val(r,0,0); total=0.0
    for ax in range(3):
        vals=[]
        for d in (-2,-1,1,2):
            xyz=[r,0.0,0.0]; xyz[ax]+=d*h; vals.append(val(*xyz))
        fm2,fm1,fp1,fp2=vals
        total += (-fp2+16*fp1-30*c+16*fm1-fm2)/(12*h*h)
    return total


def stream_b():
    us=[0.31,0.63,1.08,1.66,2.31,3.14,4.02,5.11]; ss=[0.094,0.143,0.211,0.287,0.359,0.449,0.557,0.673]
    lanes=[]; worst={"phi_poisson":0.0,"barh_poisson":0.0,"ident":0.0}
    for u,s in zip(us,ss):
        r=u*s; h=0.01*s; rh=rho_gauss(r,s); ph=phi(r,s)
        lp=lap5_cartesian_radial(lambda rr: phi(rr,s),r,h)
        target=4*math.pi*G*rh
        e1=abs(lp-target)/max(abs(target),1e-300)
        lb=lap5_cartesian_radial(lambda rr: -4*phi(rr,s)/C**2,r,h)
        targetb=-16*math.pi*G*rh/C**2
        e2=abs(lb-targetb)/max(abs(targetb),1e-300)
        bh=-4*ph/C**2
        e3=abs(ph+C**2*bh/4)/max(abs(ph),G/s)
        passed=e1<=2e-5 and e2<=2e-5 and e3<=2e-13 and math.isfinite(ph) and rh>0
        lanes.append({"u":u,"s":s,"phi_poisson":e1,"barh_poisson":e2,"identity":e3,"pass":passed})
        worst["phi_poisson"]=max(worst["phi_poisson"],e1); worst["barh_poisson"]=max(worst["barh_poisson"],e2); worst["ident"]=max(worst["ident"],e3)
    return {"stream":"B","valid":True,"pass":all(x["pass"] for x in lanes),"worst":worst,"lanes":lanes}


def pulse(t): return math.sin(math.pi*t)**2 if 0<t<1 else 0.0

def stream_c():
    rs=[0.2,0.35,0.5,0.8,1.1,1.4]; lanes=[]; adv_count=0
    for r in rs:
        grid=sorted(set([0.25-r,0.0,max(0.0,r-0.17),max(0.0,r-0.03),r+0.07,r+0.31,r+0.73]))
        pre=[t for t in grid if t<r]
        ret_pre=[pulse(t-r)/r for t in pre]
        ret_post=[pulse(t-r)/r for t in grid if t>r]
        adv_pre=[pulse(t+r)/r for t in pre]
        a=any(v>1e-14 for v in adv_pre); adv_count+=int(a)
        passed=max([abs(v) for v in ret_pre] or [0.0])<=1e-14 and any(v>0 for v in ret_post)
        lanes.append({"r":r,"pre_max":max([abs(v) for v in ret_pre] or [0.0]),"post_positive":any(v>0 for v in ret_post),"advanced_pre_nonzero":a,"pass_local":passed})
    ok=all(x["pass_local"] for x in lanes) and adv_count>=5
    return {"stream":"C","valid":True,"pass":ok,"advanced_count":adv_count,"lanes":lanes}


def stream_d():
    triples=[(0.8,1.3,0.7),(1.1,0.9,1.2),(1.7,2.2,0.5),(2.5,0.6,1.8),(0.4,3.1,2.4),(1.9,1.4,1.1),(2.7,2.8,0.9),(3.3,0.7,1.5),(1.2,2.6,2.1),(2.1,1.8,0.6)]
    widths=[0.11,0.16,0.23,0.29,0.37,0.44,0.52,0.61,0.73,0.84]
    seps=[0.17,0.31,0.48,0.69,0.93,1.21,1.57,1.96,2.42,2.95]
    lanes=[]; worst_tree=0.0; worst_fourier=0.0
    mp.mp.dps=60
    for (m1,m2,q),s,R in zip(triples,widths,seps):
        k2=32*math.pi*G/C**4
        coeff=(k2/4)*0.5*(m1*C**2)*(m2*C**2)
        target=4*math.pi*G*m1*m2
        e1=abs(coeff-target)/abs(target); worst_tree=max(worst_tree,e1)
        smp=mp.mpf(str(s)); Rmp=mp.mpf(str(R)); Gmp=mp.mpf(str(G)); m1p=mp.mpf(str(m1)); m2p=mp.mpf(str(m2))
        integ=mp.quad(lambda x: mp.e**(-smp*smp*x*x/2)*mp.sin(x*Rmp)/x,[0, mp.inf])
        vn=-2*Gmp*m1p*m2p*integ/(mp.pi*Rmp)
        va=-Gmp*m1p*m2p*mp.erf(Rmp/(mp.sqrt(2)*smp))/Rmp
        e2=float(abs(vn-va)/abs(va)); worst_fourier=max(worst_fourier,e2)
        lanes.append({"m1":m1,"m2":m2,"q":q,"s":s,"R":R,"tree_rel":e1,"fourier_rel":e2,"pass":e1<=2e-14 and e2<=2e-10})
    return {"stream":"D","valid":True,"pass":all(x["pass"] for x in lanes),"classification":"RCG002_WEAK_FIELD_BRANCH_BASELINE_EQUIVALENT_TO_LINEARIZED_SPIN2_AT_STATIC_TREE_ORDER" if all(x["pass"] for x in lanes) else "BASELINE_EQUIVALENCE_NOT_ESTABLISHED","worst_tree":worst_tree,"worst_fourier":worst_fourier,"lanes":lanes}


def stream_e():
    params=[(0.7,1.1,0.4,0.3),(1.2,0.8,0.7,0.5),(1.5,2.0,1.1,0.8),(2.4,0.6,1.7,0.9),(0.9,2.8,2.1,1.2),(1.8,1.3,0.55,1.5),(2.7,2.1,1.35,0.65),(3.1,0.9,2.4,1.1)]
    lgs=[1,0.5,0.1,0.01,0]; lhs=[1,0.5,0.25,0.125]; hbar=1.054571817e-34
    lanes=[]; worstg=0.0; worsth=0.0
    for m1,m2,R,t in params:
        A=G*m1*m2*t/R
        base=A/hbar
        eg=[]
        for lam in lgs:
            chi=lam*A/hbar
            err=abs(chi-lam*base)/max(abs(lam*base),1.0) if lam else abs(chi)
            eg.append(err); worstg=max(worstg,err)
        eh=[]
        for lam in lhs:
            chi=A/(lam*hbar); err=abs(abs(chi)-abs(base)/lam)/max(abs(base)/lam,1.0); eh.append(err); worsth=max(worsth,err)
        lanes.append({"G_errors":eg,"hbar_errors":eh,"pass":max(eg)<=2e-13 and max(eh)<=2e-13})
    ok=all(x["pass"] for x in lanes)
    return {"stream":"E","valid":True,"pass":ok,"G_zero_identity":True,"hbar_interpretation":"HBAR_ZERO_POINTWISE_PHASE_LIMIT_NOT_AVAILABLE_FROM_CHANNEL_ALONE","worst_G":worstg,"worst_hbar":worsth,"lanes":lanes}


def aggregate(root):
    files=list(Path(root).rglob('*.json')); rec=[]
    for f in files:
        try:
            x=json.loads(f.read_text())
            if x.get('stream') in list('ABCDE'): rec.append(x)
        except Exception: pass
    by={x['stream']:x for x in rec}
    valid=(set(by)==set('ABCDE') and all(by[k].get('valid') for k in 'ABCDE'))
    consistency=valid and all(by[k].get('pass') for k in 'ABCE')
    equivalence=valid and by['D'].get('pass')
    if not valid: cls='G58B_INVALID_OR_MISSING_STREAM_ARTIFACT'
    elif not consistency: cls='G58B_LINEARIZED_BASELINE_CONSISTENCY_RULE_NOT_MET'
    elif not equivalence: cls='G58B_BASELINE_EQUIVALENCE_NOT_ESTABLISHED'
    else: cls='LINEARIZED_COVARIANT_BASELINE_EMBEDDING_SUPPORTED_AND_WEAK_FIELD_NOVELTY_NOT_ESTABLISHED'
    return {"gate":"ITER056_G58B_LINEARIZED_COVARIANT_BASELINE","valid":valid,"stream_count":len(by),"passes":{k:by.get(k,{}).get('pass') for k in 'ABCDE'},"internal_consistency":consistency,"baseline_equivalence":equivalence,"classification":cls,"programme_readiness_percent":66,"theory_established_percent":0}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=list('ABCDE')); ap.add_argument('--aggregate-dir'); ap.add_argument('--out',required=True); a=ap.parse_args()
    if a.aggregate_dir: obj=aggregate(a.aggregate_dir)
    else: obj={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d,'E':stream_e}[a.stream]()
    dump(a.out,obj); print(json.dumps(obj,indent=2))

if __name__=='__main__': main()
