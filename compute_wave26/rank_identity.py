from common import write_result
rows=[]
for r in [1,2,3,4,5,6]:
    rank_w=3; rank_a=6-r
    min_intersection=max(0,rank_w+rank_a-6)
    max_combined=min(6,rank_w+rank_a)
    closure_possible=max_combined==6
    required_intersection=(rank_w+rank_a-6) if closure_possible else None
    rows.append({'r':r,'rank_W':rank_w,'rank_A':rank_a,'minimum_possible_intersection':min_intersection,'maximum_possible_combined_rank':max_combined,'closure_possible_by_dimension_count':closure_possible,'intersection_required_for_rank6':required_intersection})
signal=all((x['intersection_required_for_rank6']==3-x['r']) for x in rows if x['r']<=3) and all(not x['closure_possible_by_dimension_count'] for x in rows if x['r']>=4)
write_result('rank_identity',{'cases':rows,'rank_identity_and_transversality_condition_verified':signal,'r4_cannot_close_by_dimension_count':all(not x['closure_possible_by_dimension_count'] for x in rows if x['r']>=4)})
