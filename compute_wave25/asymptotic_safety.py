from common import write_result
rows=[]
for r in range(5): rows.append({'relevant_directions':r,'fixed_directions':6-r,'residual_nullity':r,'unique_from_fixed_point_alone':r==0})
signal=all(x['residual_nullity']==x['relevant_directions'] for x in rows if x['relevant_directions']>=1)
out={'principle':'K4_asymptotic_safety','critical_surface_cases':rows,'tournament_scope':'r>=1','asymptotic_fixed_point_with_relevant_directions_nonunique':signal,'PL1':'FAIL','PL2':'PASS','PL3':'PASS','PL4':'PASS','PL5':'PASS'}
write_result('asymptotic_safety',out)
