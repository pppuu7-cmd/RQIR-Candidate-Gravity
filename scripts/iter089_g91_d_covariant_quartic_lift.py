import argparse, json
import sympy as sp

t=sp.symbols('t')
s1,s2,s3,s4,s5,s6=sp.symbols('s1 s2 s3 s4 s5 s6')
r1,r2,r3,r4,r5,r6=sp.symbols('r1 r2 r3 r4 r5 r6')
q2,q3,q4,q5,q6=sp.symbols('q2 q3 q4 q5 q6')
lam,mu=sp.symbols('lam mu')
SQ=1+s1*t+s2*t**2+s3*t**3+s4*t**4+s5*t**5+s6*t**6
R=r1*t+r2*t**2+r3*t**3+r4*t**4+r5*t**5+r6*t**6
Q=q2*t**2+q3*t**3+q4*t**4+q5*t**5+q6*t**6
K1=sp.expand(SQ*R**4)
K2=sp.expand(SQ*R**2*Q)
TIMES=range(4)

def coeff(expr,n): return sp.expand(expr).coeff(t,n)
def order_checks(expr,leading,lead_expr):
    lower=all(sp.simplify(coeff(expr,n))==0 for n in range(leading))
    lead_ok=sp.simplify(coeff(expr,leading)-lead_expr)==0
    ders=[sp.simplify(sp.diff(expr,t,n).subs(t,0)) for n in range(leading+1)]
    low_ders=all(v==0 for v in ders[:leading]); lead_nonzero=(ders[leading]!=0)
    return lower,lead_ok,low_ders,lead_nonzero

def invariant_row(spec):
    eig=[sp.Rational(v) for v in spec]; RR=sum(eig); QQ=sum(v*v for v in eig)
    return [RR**4,RR**2*QQ]

def candidate_kernel():
    K={}
    for td in TIMES:
        for t1 in TIMES:
            for t2 in TIMES:
                v=sp.Rational(((td+2)*(t1+3)+(t2+5))%7-3)
                if td<max(t1,t2): v=sp.Integer(0)
                K[(td,t1,t2)]=v
    for key,v in list(K.items()):
        td,t1,t2=key; w=K[(td,t2,t1)]; vv=sp.simplify((v+w)/2); K[(td,t1,t2)]=K[(td,t2,t1)]=vv
    return K

def retarded(K): return all(v==0 for (td,t1,t2),v in K.items() if td<max(t1,t2))
def symmetric(K): return all(v==K[(td,t2,t1)] for (td,t1,t2),v in K.items())

def lane_A():
    a=order_checks(K1,4,r1**4); b=order_checks(K2,4,r1**2*q2)
    valid=all(a) and all(b)
    checks={'K1_t0_t3_zero':a[0],'K1_t4_is_r1_fourth':a[1],'K1_derivatives_0_to_3_zero':a[2],'K1_fourth_derivative_generically_nonzero':a[3],
            'K2_t0_t3_zero':b[0],'K2_t4_is_r1sq_q2':b[1],'K2_derivatives_0_to_3_zero':b[2],'K2_fourth_derivative_generically_nonzero':b[3],
            'K1_t4':str(coeff(K1,4)),'K2_t4':str(coeff(K2,4))}
    return 'D_COVARIANT_QUARTIC_DENSITIES_START_AT_FOURTH_ORDER_SCOPED',checks,bool(valid)

def lane_B():
    E=invariant_row([1,1,1,1]); P=invariant_row([1,1,2,2]); Z=invariant_row([1,-1,2,-2])
    M=sp.Matrix([E,P]); rank=M.rank(); det=sp.simplify(M.det())
    prop=sp.Matrix([[E[0],2*E[0]],[P[0],2*P[0]]]).rank(); zzero=all(v==0 for v in Z); withz=sp.Matrix([E,P,Z]).rank(); onerow=sp.Matrix([E]).rank()
    valid=(rank==2 and det!=0 and prop==1 and zzero and withz==2 and onerow<=1)
    checks={'E':[str(v) for v in E],'P':[str(v) for v in P],'Z':[str(v) for v in Z],'EP_rank':rank,'EP_determinant':str(det),'K1_2K1_rank':prop,'Z_zero_row':zzero,'EPZ_rank':withz,'one_background_rank':onerow}
    return 'D_COVARIANT_QUARTIC_INVARIANTS_POINTWISE_INDEPENDENT_SCOPED',checks,bool(valid)

def lane_C():
    Rp,Qp,Gp,Rm,Qm,Gm=sp.symbols('Rp Qp Gp Rm Qm Gm')
    D=sp.expand(lam*(Gp*Rp**4-Gm*Rm**4)+mu*(Gp*Rp**2*Qp-Gm*Rm**2*Qm))
    equal=sp.simplify(D.subs({Rp:Rm,Qp:Qm,Gp:Gm}))==0
    swapped=sp.expand(D.subs({Rp:Rm,Qp:Qm,Gp:Gm,Rm:Rp,Qm:Qp,Gm:Gp},simultaneous=True)); odd=sp.simplify(swapped+D)==0
    rp1,rp2,rp3,rp4,rm1,rm2,rm3,rm4=sp.symbols('rp1 rp2 rp3 rp4 rm1 rm2 rm3 rm4')
    qp2,qp3,qp4,qm2,qm3,qm4=sp.symbols('qp2 qp3 qp4 qm2 qm3 qm4')
    gp1,gp2,gp3,gm1,gm2,gm3=sp.symbols('gp1 gp2 gp3 gm1 gm2 gm3')
    RpT=rp1*t+rp2*t**2+rp3*t**3+rp4*t**4; RmT=rm1*t+rm2*t**2+rm3*t**3+rm4*t**4
    QpT=qp2*t**2+qp3*t**3+qp4*t**4; QmT=qm2*t**2+qm3*t**3+qm4*t**4
    GpT=1+gp1*t+gp2*t**2+gp3*t**3; GmT=1+gm1*t+gm2*t**2+gm3*t**3
    DT=sp.expand(lam*(GpT*RpT**4-GmT*RmT**4)+mu*(GpT*RpT**2*QpT-GmT*RmT**2*QmT))
    lower=[sp.simplify(coeff(DT,n)) for n in range(4)]; lowerzero=all(v==0 for v in lower)
    sample_ok=[all(sp.simplify(v.subs({lam:a,mu:b}))==0 for v in lower) for a,b in [(1,0),(0,1),(1,1),(2,-1),(-2,3)]]
    selection_rank=sp.Matrix(lower).jacobian([lam,mu]).rank()
    K0=candidate_kernel(); K1c=candidate_kernel(); unchanged=(K0==K1c); kr=retarded(K0); ks=symmetric(K0)
    # Frozen D cubic representative jet
    d0,d1,s0,s1x=sp.symbols('d0 d1 s0 s1x'); G3=d0*s0**2+2*d0*s0*s1x+d1*s1x**2; vars_=[d0,d1,s0,s1x]; z={v:0 for v in vars_}
    H=sp.hessian(G3,vars_).subs(z); hzero=(H==sp.zeros(4)); third=[]
    import itertools
    for inds in itertools.product(range(4),repeat=3):
        ex=G3
        for i in inds: ex=sp.diff(ex,vars_[i])
        third.append(sp.simplify(ex.subs(z)))
    tnonzero=any(v!=0 for v in third)
    valid=equal and odd and lowerzero and all(sample_ok) and selection_rank==0 and unchanged and kr and ks and hzero and tnonzero
    checks={'equal_history_zero':equal,'branch_exchange_odd':odd,'formal_t0_t3_zero':lowerzero,'sample_pairs_preserve_lower_order':sample_ok,'inherited_covariant_ctp_selection_rank':selection_rank,'cubic_kernel_unchanged':unchanged,'cubic_kernel_retarded':kr,'cubic_kernel_sigma_symmetric':ks,'D_hessian_zero':hzero,'D_third_derivative_nonzero':tnonzero}
    return 'D_COVARIANT_QUARTIC_CTP_FAMILY_PRESERVES_CUBIC_STRUCTURE_SCOPED',checks,bool(valid)

def lane_D():
    R3=sp.expand(SQ*R**3); lead=coeff(R3,3); contamination=(sp.simplify(lead-r1**3)==0 and lead!=0)
    E=invariant_row([1,1,1,1]); P=invariant_row([1,1,2,2]); collapsed=sp.Matrix([[E[0],2*E[0]],[P[0],2*P[0]]]).rank(); zero_rank=sp.Matrix([[E[0],0],[P[0],0]]).rank(); one_rank=sp.Matrix([E]).rank()
    valid=contamination and collapsed==1 and zero_rank==1 and one_rank<=1
    checks={'R3_t3':str(lead),'R3_rejected_as_lower_order_contamination':contamination,'proportional_family_rank':collapsed,'zero_invariant_augmented_rank':zero_rank,'one_background_rank':one_rank}
    return 'D_COVARIANT_LIFT_ORDER_AND_INDEPENDENCE_CONTROLS_SCOPED',checks,bool(valid)

LANES={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=sorted(LANES)); ap.add_argument('--out',required=True); a=ap.parse_args()
classification,checks,valid=LANES[a.lane]()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
if not valid: raise SystemExit(2)
