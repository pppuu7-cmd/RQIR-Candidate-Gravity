from common import write_result

comparators=[
 {'structure':'Barnes-Rivers / spin-projector decomposition of symmetric rank-2 kernels','status':'KNOWN_TECHNIQUE','novelty_credit':False},
 {'structure':'conserved-source decoupling of longitudinal gauge sectors','status':'STANDARD_WARD_GAUGE_CONSEQUENCE','novelty_credit':False},
 {'structure':'Einstein/GR massless spin-2 residue with conserved-source trace structure','status':'C5_ROOT_CONTROL','novelty_credit':False},
 {'structure':'analytic finite-q transverse form factors / higher-curvature EFT corrections','status':'C5_EFT_COMPATIBLE','novelty_credit':False},
 {'structure':'extra poles from simple higher-derivative rational propagators','status':'KNOWN_HIGHER_DERIVATIVE_COMPARATOR','novelty_credit':False},
 {'structure':'pole-free nonlocal/entire form-factor families','status':'KNOWN_NONLOCAL_COMPARATOR_CLASS','novelty_credit':False},
 {'structure':'positive graviton spectral-function / functional-RG constructions','status':'ACTIVE_KNOWN_QG_COMPARATOR_CLASS','novelty_credit':False}
]
out={
 'test':'Wave 17 tensor comparator firewall',
 'comparators':comparators,
 'projector_or_form_factor_structure_alone_is_novel':False,
 'required_for_C5_distinct_claim':['independently motivated physical law fixing/linking transverse form factors','same-dynamics derivation','prospective observable not generically reproducible by C5 EFT controls','frozen RQIR gate closure'],
 'firewall_pass': all(not x['novelty_credit'] for x in comparators),
 'conclusion':'Tensor projectors, Ward decoupling, GR residue matching, generic form factors, pole audits and spectral-flow technology are comparator infrastructure. Wave 17 may reduce the candidate space, but none of these ingredients alone counts as a new quantum-gravity primitive.'
}
write_result('comparator_firewall',out)
