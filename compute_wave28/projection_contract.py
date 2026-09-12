from common import load,write
D=load()['evidence']['D28_4_six_output_projection']
required=['c3','d3','e4','f4','s2','s0']
out={'required_outputs':required,'required_output_count':len(required),'vertex_to_effective_action_map_available':D['vertex_to_effective_action_map'],'effective_action_to_six_rqir_map_available':D['effective_action_to_six_rqir_map'],'explicit_six_output_projection_missing':not D['effective_action_to_six_rqir_map'],'projection_contract_ready_for_future_data':True}
write('projection_contract',out)
