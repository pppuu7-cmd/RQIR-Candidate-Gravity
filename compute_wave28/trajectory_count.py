from common import load,write
r=int(load()['relevant_direction_count'])
one_sided=1+r
symmetric=1+2*r
second_step=1+4*r
write('trajectory_count',{
 'relevant_direction_count':r,
 'minimum_one_sided_trajectory_count':one_sided,
 'minimum_symmetric_trajectory_count':symmetric,
 'symmetric_two_step_size_trajectory_count_if_no_reuse_beyond_center':second_step,
 'minimum_one_sided_trajectory_count_is_4':one_sided==4,
 'minimum_symmetric_trajectory_count_is_7':symmetric==7
})
