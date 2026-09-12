from common import load,write
D=load(); s=next(x for x in D['sources'] if x['id']=='L1'); q=s['support']
signal=all(q[k] for k in ['J0','J1','J3','J4','J7']) and (not q['J5']) and (not q['J6']) and (not q['J8'])
write('lorentzian_lineage',{'source':'L1','support':q,'lorentzian_quadratic_bridge_exists_but_higher_point_closure_missing':signal})
