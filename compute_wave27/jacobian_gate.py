from common import load,write
D=load(); srcs=D['sources']
j8=[s['id'] for s in srcs if s['support'].get('J8',False)]
j9=[s['id'] for s in srcs if s['support'].get('J9',False)]
write('jacobian_gate',{'J8_supporting_sources':j8,'J9_supporting_sources':j9,'explicit_six_direction_jacobian_missing':len(j8)==0,'propagated_six_direction_uncertainty_missing':len(j9)==0})
