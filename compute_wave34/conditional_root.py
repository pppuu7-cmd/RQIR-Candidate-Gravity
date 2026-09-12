import numpy as np
from common import solve_conditional,beta3,write
root,ok,it,res=solve_conditional()
signals={'conditional_three_equation_root_converges':ok and res<1e-8,'conditional_root_stays_in_declared_domain':root[0]>-1 and root[2]>0}
out={'test':'conditional_root','root':root.tolist(),'iterations':it,'residual_norm':res,'beta':beta3(root).tolist(),'signals':signals}; write('wave34_conditional_root.json',out); assert all(signals.values())
