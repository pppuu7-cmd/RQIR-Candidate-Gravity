import argparse, json
import sympy as sp

t=sp.symbols('t')
s1,s2,s3,s4,s5=sp.symbols('s1 s2 s3 s4 s5')
r1,r2,r3,r4,r5=sp.symbols('r1 r2 r3 r4 r5')
q2,q3,q4,q5=sp.symbols('q2 q3 q4 q5')
lam,mu=sp.symbols('lam mu')
SQ=1+s1*t+s2*t**2+s3*t**3+s4*t**4+s5*t**5
R=r1*t+r2*t**2+r3*t**3+r4*t**4+r5*t**5
Q=q2*t**2+q3*t**3+q4*t**4+q5*t**5
J1=sp.expand(SQ*R**3)
J2=sp.expand(SQ*R*Q)

def coeff(expr,n): return sp.expand(expr).coeff(t,n)
def order_checks(expr,leading,lead_expr):
    lower=all(sp.simplify(coeff(expr,n))==0 for n in range(leading))
    lead_ok=sp.simplify(coeff(expr,leading)-lead_expr)==0
    ders=[sp.simplify(sp.diff(expr,t,n).subs(t,0)) for n in range(leading+1)]
    low_ders=all(v==0 for v in ders[:leading])
    lead_nonzero=(ders[leading]!=0)
    return lower,lead_ok,low_ders,lead_nonzero,ders

def invariant_row(spec,power):
    eig=[sp.Rational(v) for v in spec]
    RR=sum(eig); QQ=sum(v*v for v in eig)
    if power==3: return [RR**3,RR*QQ]
    return [RR**4,RR**2*QQ]

def lane_A():
    a=order_checks(J1,3,r1**3); b=order_checks(J2,3,r1*q2)
    valid=all(a[:4]) and all(b[:4])
    checks={
        'J1_t0_t2_zero':a[0],'J1_t3_is_r1_cubed':a[1],'J1_derivatives_0_to_2_zero':a[2],'J1_third_derivative_generically_nonzero':a[3],
        'J2_t0_t2_zero':b[0],'J2_t3_is_r1_q2':b[1],'J2_derivatives_0_to_2_zero':b[2],'J2_third_derivative_generically_nonzero':b[3],
        'J1_t3':str(coeff(J1,3)),'J2_t3':str(coeff(J2,3))}
    return 'C_COVARIANT_CUBIC_DENSITIES_START_AT_THIRD_ORDER_SCOPED',checks,bool(valid)

def lane_B():
    E=invariant_row([1,1,1,1],3); P=invariant_row([1,1,2,2],3); Z=invariant_row([1,-1,2,-2],3)
    M=sp.Matrix([E,P]); det=sp.simplify(M.det()); rank=M.rank()
    prop=sp.Matrix([[E[0],2*E[0]],[P[0],2*P[0]]]).rank()
    zzero=all(v==0 for v in Z); withz=sp.Matrix([E,P,Z]).rank(); onerow=sp.Matrix([E]).rank()
    valid=(rank==2 and det!=0 and prop==1 and zzero and withz==2 and onerow<=1)
    checks={'E':[str(v) for v in E],'P':[str(v) for v in P],'Z':[str(v) for v in Z],'EP_rank':rank,'EP_determinant':str(det),'J1_2J1_rank':prop,'Z_zero_row':zzero,'EPZ_rank':withz,'one_background_rank':onerow}
    return 'C_COVARIANT_CUBIC_INVARIANTS_POINTWISE_INDEPENDENT_SCOPED',checks,bool(valid)

def lane_C():
    Rp,Qp,Gp,Rm,Qm,Gm=sp.symbols('Rp Qp Gp Rm Qm Gm')
    D=sp.expand(lam*(Gp*Rp**3-Gm*Rm**3)+mu*(Gp*Rp*Qp-Gm*Rm*Qm))
    equal=sp.simplify(D.subs({Rp:Rm,Qp:Qm,Gp:Gm}))==0
    swapped=sp.expand(D.subs({Rp:Rm,Qp:Qm,Gp:Gm,Rm:Rp,Qm:Qp,Gm:Gp},simultaneous=True)); odd=sp.simplify(swapped+D)==0
    # independent formal branch expansions through the lower frozen order
    rp1,rp2,rp3,rm1,rm2,rm3=sp.symbols('rp1 rp2 rp3 rm1 rm2 rm3')
    qp2,qp3,qm2,qm3=sp.symbols('qp2 qp3 qm2 qm3')
    gp1,gp2,gm1,gm2=sp.symbols('gp1 gp2 gm1 gm2')
    RpT=rp1*t+rp2*t**2+rp3*t**3; RmT=rm1*t+rm2*t**2+rm3*t**3
    QpT=qp2*t**2+qp3*t**3; QmT=qm2*t**2+qm3*t**3
    GpT=1+gp1*t+gp2*t**2; GmT=1+gm1*t+gm2*t**2
    DT=sp.expand(lam*(GpT*RpT**3-GmT*RmT**3)+mu*(GpT*RpT*QpT-GmT*RmT*QmT))
    lower=[sp.simplify(coeff(DT,n)) for n in range(3)]
    lowerzero=all(v==0 for v in lower)
    sample_ok=[]
    for a,b in [(1,0),(0,1),(1,1),(2,-1),(-2,3)]:
        sample_ok.append(all(sp.simplify(v.subs({lam:a,mu:b}))==0 for v in lower))
    selection_rank=sp.Matrix(lower).jacobian([lam,mu]).rank()
    valid=equal and odd and lowerzero and all(sample_ok) and selection_rank==0
    checks={'equal_history_zero':equal,'branch_exchange_odd':odd,'formal_t0_t2_zero':lowerzero,'sample_pairs_preserve_lower_order':sample_ok,'inherited_covariant_ctp_selection_rank':selection_rank}
    return 'C_COVARIANT_CUBIC_CTP_FAMILY_PRESERVES_LOWER_DATA_SCOPED',checks,bool(valid)

def lane_D():
    R2=sp.expand(SQ*R**2)
    r2_lead=coeff(R2,2); lower_contamination=(sp.simplify(r2_lead-r1**2)==0 and r2_lead!=0)
    E=invariant_row([1,1,1,1],3); P=invariant_row([1,1,2,2],3)
    collapsed=sp.Matrix([[E[0],2*E[0]],[P[0],2*P[0]]]).rank()
    zero_rank=sp.Matrix([[E[0],0],[P[0],0]]).rank()
    one_rank=sp.Matrix([E]).rank()
    valid=lower_contamination and collapsed==1 and zero_rank==1 and one_rank<=1
    checks={'R2_t2':str(r2_lead),'R2_rejected_as_lower_order_contamination':lower_contamination,'proportional_family_rank':collapsed,'zero_invariant_augmented_rank':zero_rank,'one_background_rank':one_rank}
    return 'C_COVARIANT_LIFT_ORDER_AND_INDEPENDENCE_CONTROLS_SCOPED',checks,bool(valid)

LANES={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=sorted(LANES)); ap.add_argument('--out',required=True); a=ap.parse_args()
classification,checks,valid=LANES[a.lane]()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
if not valid: raise SystemExit(2)
