from common import write_result
matrix={
 'K1_soft_ward':{'PL1':'FAIL','PL2':'PASS','PL3':'FAIL','PL4':'PASS','PL5':'PASS'},
 'K2_positivity_dispersion':{'PL1':'FAIL','PL2':'PASS','PL3':'FAIL','PL4':'FAIL','PL5':'PASS'},
 'K3_causality_uv':{'PL1':'FAIL','PL2':'PASS','PL3':'FAIL','PL4':'FAIL','PL5':'PASS'},
 'K4_asymptotic_safety':{'PL1':'FAIL','PL2':'PASS','PL3':'PASS','PL4':'PASS','PL5':'PASS'},
 'K5_double_copy':{'PL1':'FAIL','PL2':'PASS','PL3':'FAIL','PL4':'PASS','PL5':'FAIL'}
}
full={k:all(v[f'PL{i}']=='PASS' for i in range(1,6)) for k,v in matrix.items()}
out={'matrix':matrix,'full_pass':full,'literature_gate_matrix_has_no_full_pass':not any(full.values()),'no_known_principle_tested_here_earns_new_parent_law_credit':not any(full.values())}
write_result('gate_matrix',out)
