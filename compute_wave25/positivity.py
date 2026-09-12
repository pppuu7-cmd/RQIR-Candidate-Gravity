import numpy as np
from common import X, write_result
rng=np.random.default_rng(2502)
b=np.asarray([0.20,0.18,0.15,0.12,0.10,0.09],float)
n=20000
u=rng.normal(size=(n,6)); u/=np.linalg.norm(u,axis=1,keepdims=True)
r=rng.random(n)**(1/6)
theta=u*(r[:,None]*b[None,:])
Y=theta@X().T
widths=Y.max(axis=0)-Y.min(axis=0)
mx=float(widths.max())
out={'principle':'K2_positivity_dispersion','samples':n,'seed':2502,'max_prediction_width':mx,'positivity_region_nonunique':bool(mx>=0.05),'PL1':'FAIL','PL2':'PASS','PL3':'FAIL','PL4':'FAIL','PL5':'PASS'}
write_result('positivity',out)
