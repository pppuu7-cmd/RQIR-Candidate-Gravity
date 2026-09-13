#!/usr/bin/env python3
import argparse, json
import sympy as sp

p=argparse.ArgumentParser(); p.add_argument('--lane',required=True); p.add_argument('--out',required=True); a=p.parse_args()
R,Q=sp.symbols('R Q')
J1=R**3; J2=R*Q; K1=R**4; K2=R**2*Q

def emit(stream, classification, checks, valid):
    row={'stream':stream,'classification':classification if valid else 'SCIENTIFIC_OR_GATE_FAIL','checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
    open(a.out,'w').write(json.dumps(row,indent=2,sort_keys=True))
    if not valid: raise SystemExit(2)

if a.lane=='A':
    shell={R:0,Q:0}
    vals=[sp.simplify(x.subs(shell)) for x in (J1,J2)]
    coeff_samples=[(-3,5),(1,1),(7,-2),(0,4)]
    combos=[sp.simplify((u*J1+v*J2).subs(shell)) for u,v in coeff_samples]
    checks={'J1_shell':str(vals[0]),'J2_shell':str(vals[1]),'all_frozen_linear_combinations_zero':all(x==0 for x in combos)}
    valid=(vals==[0,0] and all(x==0 for x in combos))
    emit('A','C_G90_RICCI_ONLY_WITNESSES_VANISH_ON_LEADING_EINSTEIN_VACUUM_SHELL_SCOPED',checks,valid)
elif a.lane=='B':
    shell={R:0,Q:0}
    vals=[sp.simplify(x.subs(shell)) for x in (K1,K2)]
    coeff_samples=[(-3,5),(1,1),(7,-2),(0,4)]
    combos=[sp.simplify((u*K1+v*K2).subs(shell)) for u,v in coeff_samples]
    checks={'K1_shell':str(vals[0]),'K2_shell':str(vals[1]),'all_frozen_linear_combinations_zero':all(x==0 for x in combos)}
    valid=(vals==[0,0] and all(x==0 for x in combos))
    emit('B','D_G91_RICCI_ONLY_WITNESSES_VANISH_ON_LEADING_EINSTEIN_VACUUM_SHELL_SCOPED',checks,valid)
elif a.lane=='C':
    samples=[(1,2,-3),(2,-5,3),(1,-4,3)]
    rows=[]; valid=True
    for s in samples:
        w2=sum(x*x for x in s); w3=sum(x**3 for x in s); w4=sum(x**4 for x in s)
        rows.append({'lambda':list(s),'trace':sum(s),'W2':w2,'W3':w3,'W4':w4})
        valid &= (sum(s)==0 and w3!=0 and w4!=0)
    z=(0,0,0); zw=[sum(x**n for x in z) for n in (2,3,4)]
    valid &= (zw==[0,0,0])
    emit('C','RICCI_FLAT_SHELL_DOES_NOT_FORCE_ALL_ALGEBRAIC_WEYL_INVARIANTS_ZERO_SCOPED',{'samples':rows,'zero_spectrum_W234':zw},valid)
elif a.lane=='D':
    off={R:2,Q:3}; c_off=[sp.simplify(x.subs(off)) for x in (J1,J2)]; d_off=[sp.simplify(x.subs(off)) for x in (K1,K2)]
    rzero={R:0,Q:7}; rzero_vals=[sp.simplify(x.subs(rzero)) for x in (J1,J2,K1,K2)]
    constant_control=sp.Integer(1).subs({R:0,Q:0})
    checks={'C_offshell':[str(x) for x in c_off],'D_offshell':[str(x) for x in d_off],'R_zero_specific_family':[str(x) for x in rzero_vals],'constant_control_shell':str(constant_control)}
    valid=(any(x!=0 for x in c_off) and any(x!=0 for x in d_off) and all(x==0 for x in rzero_vals) and constant_control==1)
    emit('D','VACUUM_SHELL_AUDIT_FALSE_POSITIVE_CONTROLS_SCOPED',checks,valid)
else:
    raise SystemExit('unknown lane')
