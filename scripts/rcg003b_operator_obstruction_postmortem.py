#!/usr/bin/env python3
"""Descriptive exact postmortem of the already-terminal RCG003B obstruction.

This script does not define RCG004, search coefficients, or alter any classifier.
It decomposes the frozen RCG003-v0 ray (7,-36,36) into its three already-
authorized Ricci-cubic operator contributions on the already-authorized
axisymmetric RCG003B metric and transforms the acceleration Hessian to
(volume, shear) variables a=sigma+2 beta, b=sigma-beta.
"""
from __future__ import annotations
import hashlib, json, platform, sys
from pathlib import Path
import sympy as sp
from rcg003b_axisymmetric_constructor import tensor_curvature_axisymmetric, jet


def f(e):
    return str(sp.factor(sp.expand(e)))


def hessian(expr, ua, ub):
    return sp.Matrix([[sp.diff(expr, ua, ua), sp.diff(expr, ua, ub)],
                      [sp.diff(expr, ub, ua), sp.diff(expr, ub, ub)]])


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('RCG003B_OPERATOR_OBSTRUCTION_POSTMORTEM.json')
    t,a,b,g,gi,R,Ric2,Ric3,sqrtg = tensor_curvature_axisymmetric()
    RJ,(va,vb,ua,ub) = jet(R,t,a,b)
    R2J,_ = jet(Ric2,t,a,b)
    R3J,_ = jet(Ric3,t,a,b)
    ops=[('R^3',RJ**3,7),('R Ricci^2',RJ*R2J,-36),('Tr(Ricci^3)',R3J,36)]

    weighted=[]
    entries=[]
    v,u=sp.symbols('v u')
    for name,O,c in ops:
        H=c*hessian(O,ua,ub)
        weighted.append(H)
        iso=sp.expand((H[0,0]+2*H[0,1]+H[1,1]).subs({va:v,vb:v,ua:u,ub:u}))
        entries.append({'operator':name,'coefficient':c,
                        'H_aa':f(H[0,0]),'H_ab':f(H[0,1]),'H_bb':f(H[1,1]),
                        'isotropic_pullback':f(iso)})

    H=sum(weighted,sp.zeros(2,2))
    u_sigma,u_beta,v_sigma,v_beta=sp.symbols('u_sigma u_beta v_sigma v_beta')
    sub_sb={ua:u_sigma+2*u_beta,ub:u_sigma-u_beta,
            va:v_sigma+2*v_beta,vb:v_sigma-v_beta}
    J=sp.Matrix([[1,2],[1,-1]])
    Hz=sp.Matrix([[sp.expand(e.subs(sub_sb)) for e in (J.T*H*J).row(i)] for i in range(2)])

    per_op=[]
    for (name,O,c),M in zip(ops,weighted):
        Z=J.T*M*J
        per_op.append({'operator':name,'coefficient':c,
                       'H_sigma_sigma':f(Z[0,0].subs(sub_sb)),
                       'H_sigma_beta':f(Z[0,1].subs(sub_sb)),
                       'H_beta_beta':f(Z[1,1].subs(sub_sb))})

    result={
      'status':'RETROSPECTIVE_DESCRIPTIVE_POSTMORTEM_NO_CLASSIFIER_CHANGE',
      'parent_gate':'RCG003B_AXISYMMETRIC_BIANCHI_I_DERIVATIVE_CLOSURE',
      'parent_terminal_commit':'72f9ab2ab5ad85259a18fc1f368777c431a56324',
      'parent_classification':'FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED',
      'frozen_ray':[7,-36,36], 'source':'VACUUM_ZERO',
      'operators':entries,
      'total_hessian_ab':{'H_aa':f(H[0,0]),'H_ab':f(H[0,1]),'H_bb':f(H[1,1])},
      'volume_shear_change':'a=sigma+2 beta; b=sigma-beta',
      'operator_contributions_volume_shear':per_op,
      'total_hessian_volume_shear':{
          'H_sigma_sigma':f(Hz[0,0]),
          'H_sigma_beta':f(Hz[0,1]),
          'H_beta_beta':f(Hz[1,1]),
      },
      'isotropic_background_volume_shear':{
          'conditions':'v_beta=0, u_beta=0',
          'H_sigma_sigma':f(Hz[0,0].subs({v_beta:0,u_beta:0})),
          'H_sigma_beta':f(Hz[0,1].subs({v_beta:0,u_beta:0})),
          'H_beta_beta':f(Hz[1,1].subs({v_beta:0,u_beta:0})),
      },
      'mechanism_summary':[
        'The conformal/volume acceleration direction has H_sigma_sigma=0 identically for the frozen ray.',
        'The mixed volume-shear obstruction is -1296*(u_beta+3*v_beta*v_sigma).',
        'Even on an isotropic background, the shear-shear acceleration Hessian is -1296*(u_sigma+v_sigma^2), so the conformal restriction discards an obstructed direction rather than proving the full two-field Hessian vanishes.'
      ],
      'no_new_model_content':True,
      'RCG004_formed':False,
      'coefficient_search_performed':False,
      'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED',
      'theory_established':'0%',
      'environment':{'python':sys.version.split()[0],'sympy':sp.__version__,'platform':platform.platform()},
    }
    payload=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
    result['payload_sha256']=hashlib.sha256(payload).hexdigest()
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'payload_sha256':result['payload_sha256'],
                      'total_hessian_volume_shear':result['total_hessian_volume_shear'],
                      'isotropic_background':result['isotropic_background_volume_shear']},sort_keys=True))


if __name__=='__main__':
    main()
