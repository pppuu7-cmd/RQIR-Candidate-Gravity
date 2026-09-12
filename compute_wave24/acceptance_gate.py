from common import write_result

criteria=['closure','independent_provenance','comparator_novelty','prospective_predictivity','no_hidden_functional_freedom']
selectors={
 'S1_scalar_relation':{
   'closure':False,'independent_provenance':False,'comparator_novelty':False,'prospective_predictivity':True,'no_hidden_functional_freedom':True},
 'S2_three_relation_proxy':{
   'closure':False,'independent_provenance':False,'comparator_novelty':False,'prospective_predictivity':True,'no_hidden_functional_freedom':True},
 'S3_two_latent_generator':{
   'closure':True,'independent_provenance':False,'comparator_novelty':False,'prospective_predictivity':True,'no_hidden_functional_freedom':True},
 'S4_arbitrary_full_rank_selector':{
   'closure':True,'independent_provenance':False,'comparator_novelty':False,'prospective_predictivity':True,'no_hidden_functional_freedom':True},
 'S5_minimum_complexity':{
   'closure':True,'independent_provenance':False,'comparator_novelty':False,'prospective_predictivity':True,'no_hidden_functional_freedom':True},
 'S6_inequality_region':{
   'closure':False,'independent_provenance':True,'comparator_novelty':False,'prospective_predictivity':True,'no_hidden_functional_freedom':True},
 'S7_unconstrained_function':{
   'closure':False,'independent_provenance':False,'comparator_novelty':False,'prospective_predictivity':False,'no_hidden_functional_freedom':False}
}
for s,v in selectors.items():
    v['parent_law_credit']=all(v[c] for c in criteria)
credit=[s for s,v in selectors.items() if v['parent_law_credit']]
out={
 'test':'Parent-Law Acceptance Gate v1 ledger',
 'criteria':criteria,
 'selectors':selectors,
 'selectors_earning_parent_law_credit':credit,
 'no_tested_selector_earns_parent_law_credit':len(credit)==0,
 'minimum_required_gate_count':len(criteria),
 'conclusion':'Mathematical closure is only one necessary condition. None of the preregistered demonstration selectors simultaneously has independent provenance, comparator novelty, prospective predictions, and controlled functional freedom.'
}
write_result('acceptance_gate',out)
