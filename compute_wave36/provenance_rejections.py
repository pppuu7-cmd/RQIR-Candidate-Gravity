import copy
from common import complete_candidate,validate,write
base=complete_candidate()
cases={}
# Exponents/fixed point only: preserve provenance but remove all orientation data.
e=copy.deepcopy(base); e.pop('stability_matrix'); e.pop('right_relevant_real_basis'); e['critical_exponents']=[-3.0,'-1.9+1.6i','-1.9-1.6i',1.7,3.4]; cases['exponents_only']=e
w=copy.deepcopy(base); w['coordinates']=['lambda3','mu','lambda4','g3','g4']; cases['wrong_coordinate_order']=w
cl=copy.deepcopy(base); cl['closure_id']='different_closure'; cases['wrong_closure']=cl
pp=copy.deepcopy(base); pp.pop('projection_provenance'); cases['missing_projection']=pp
rg=copy.deepcopy(base); rg.pop('regulator_gauge_truncation'); cases['missing_regulator']=rg
np=copy.deepcopy(base); np.pop('numerical_precision'); cases['missing_precision']=np
ch=copy.deepcopy(base); ch.pop('checksum'); cases['missing_checksum']=ch
results={}
for name,c in cases.items():
    ok,reasons,err=validate(c); results[name]={'accepted':ok,'reasons':reasons}
signals={
 'critical_exponents_without_orientation_are_rejected':not results['exponents_only']['accepted'] and 'orientation_object_missing' in results['exponents_only']['reasons'],
 'wrong_coordinate_order_rejected':not results['wrong_coordinate_order']['accepted'],
 'wrong_closure_rejected':not results['wrong_closure']['accepted'],
 'missing_projection_provenance_rejected':not results['missing_projection']['accepted'],
 'missing_regulator_truncation_provenance_rejected':not results['missing_regulator']['accepted'],
 'missing_numerical_precision_rejected':not results['missing_precision']['accepted'],
 'missing_checksum_rejected':not results['missing_checksum']['accepted']
}
out={'test':'provenance_rejections','cases':results,'signals':signals}; write('wave36_provenance_rejections.json',out); assert all(signals.values())
