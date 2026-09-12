from common import load,write
D=load(); srcs=[s for s in D['sources'] if s['lineage']=='fluctuation_vertex']
union={f'J{i}':any(s['support'].get(f'J{i}',False) for s in srcs) for i in range(10)}
signal=all(union[f'J{i}'] for i in range(8)) and not union['J8']
write('vertex_lineage',{'sources':[s['id'] for s in srcs],'support':union,'full_momentum_vertices_exist_but_UV_to_RQIR_sensitivity_map_missing':signal})
