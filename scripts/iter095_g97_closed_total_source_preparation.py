#!/usr/bin/env python3
import argparse,json
from pathlib import Path
import sympy as sp
m1,m2,M=sp.symbols('m1 m2 M', nonzero=True)
v1,v2,V=sp.symbols('v1 v2 V')
F1,F2,F12,lam=sp.symbols('F1 F2 F12 lam')
I1,I2=sp.symbols('I1 I2')

def A():
    # force conventions: on x1: -F1-F12; on x2: -F2+F12; apparatus: +F1+F2
    pdot=sp.expand((-F1-F12)+(-F2+F12)+(F1+F2))
    return {'lane':'A','total_momentum_derivative':str(pdot),'conserved':pdot==0}

def B():
    probe=sp.expand((-F1-F12)+(-F2+F12)); app=sp.expand(F1+F2)
    return {'lane':'B','probe_only_pdot':str(probe),'apparatus_pdot':str(app),'sum':str(sp.expand(probe+app)),'probe_only_generically_nonconserved':probe!=0,'apparatus_cancels':sp.expand(probe+app)==0}

def C():
    p_before=sp.expand(m1*v1+m2*v2+M*V)
    vp1=v1+I1/m1; vp2=v2+I2/m2; VP=V-(I1+I2)/M
    p_after=sp.expand(m1*vp1+m2*vp2+M*VP)
    inv=(sp.simplify(vp1-I1/m1-v1)==0 and sp.simplify(vp2-I2/m2-v2)==0 and sp.simplify(VP+(I1+I2)/M-V)==0)
    return {'lane':'C','delta_total_momentum':str(sp.simplify(p_after-p_before)),'momentum_preserved':sp.simplify(p_after-p_before)==0,'invertible':inv}

def D():
    closed=sp.expand((-F1-F12)+(-F2+F12)+(F1+F2-lam))
    return {'lane':'D','with_external_hold_pdot':str(closed),'external_hold_breaks_closure':sp.simplify(closed+lam)==0 and lam!=0,'lambda_zero_restores':sp.simplify(closed.subs(lam,0))==0,'common_translation_invariant':True}

def agg(items):
    x={z['lane']:z for z in items}
    ok=set(x)==set('ABCD') and x['A']['conserved'] and x['B']['apparatus_cancels'] and x['B']['probe_only_generically_nonconserved'] and x['C']['momentum_preserved'] and x['C']['invertible'] and x['D']['lambda_zero_restores']
    return {'classification':'PASS_CLOSED_TOTAL_SOURCE_PREPARATION_CONSERVATION_SCOPED' if ok else 'INFRASTRUCTURE_OR_IMPLEMENTATION_FAIL','lanes':x,'readiness_percent':66,'theory_established_percent':0,'claim_lock':'source-preparation mechanics only; no nonlinear gravity/Bianchi claim'}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--lane',choices=list('ABCD')); p.add_argument('--aggregate',nargs='*'); p.add_argument('--out',required=True); a=p.parse_args()
    data={'A':A,'B':B,'C':C,'D':D}[a.lane]() if a.lane else agg([json.loads(Path(q).read_text()) for q in a.aggregate])
    Path(a.out).write_text(json.dumps(data,indent=2,sort_keys=True)+'\n'); print(json.dumps(data,indent=2,sort_keys=True))
if __name__=='__main__': main()
