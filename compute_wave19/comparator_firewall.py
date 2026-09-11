from common import write_result

comparators=[
 {'structure':'diffeomorphism/Ward identities relating longitudinal vertex components to lower-point functions','status':'STANDARD_GAUGE_STRUCTURE','novelty_credit':False},
 {'structure':'leading/subleading soft-graviton constraints','status':'KNOWN_SOFT_THEOREM_STRUCTURE','novelty_credit':False},
 {'structure':'curvature-cubed / higher-derivative corrections to graviton three-point interactions','status':'C5_EFT_COMPARATOR','novelty_credit':False},
 {'structure':'eikonal/Shapiro-delay causality constraints on anomalous three-point couplings','status':'CEMZ_AND_SUCCESSORS','novelty_credit':False},
 {'structure':'product/factorized use of one form factor across external legs','status':'MODELING_POSTULATE_WITH_NONLOCAL_FORM_FACTOR_ANALOGUES','novelty_credit':False}
]
out={
 'test':'Wave 19 cross-order comparator firewall',
 'comparators':comparators,
 'firewall_pass':all(not c['novelty_credit'] for c in comparators),
 'required_for_new_QG_primitive':[
   'gravity-specific cross-order law derived independently of the tested null directions',
   'same dynamics generating two-point and higher-point structures',
   'finite-kinematic prospective higher-point prediction',
   'prediction outside generic C5/EFT higher-curvature freedom under the same validity domain',
   'frozen RQIR consistency/comparator/identifiability/resource closure'
 ],
 'conclusion':'Ward identities, soft theorems, higher-curvature cubic vertices and causality bounds are comparator infrastructure. A restrictive product closure can generate predictions but has no novelty status unless independently derived and shown to beat C5/EFT cross-order freedom.'
}
write_result('comparator_firewall',out)
