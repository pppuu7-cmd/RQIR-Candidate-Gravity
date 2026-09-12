import numpy as np
from common import write_result
cs=np.linspace(-0.95,0.95,39); ms=np.linspace(1.0,4.0,31)
Y=np.asarray([[0.4*c/m**2,0.25*c*c/m**4] for c in cs for m in ms],float)
diam=0.0
for i in range(len(Y)):
    diam=max(diam,float(np.linalg.norm(Y[i+1:]-Y[i],axis=1).max()) if i+1<len(Y) else diam)
unique=len(np.unique(np.round(Y,12),axis=0))
out={'principle':'K3_causality_uv','grid_points':len(Y),'distinct_predictions':unique,'prediction_diameter':diam,'causality_uv_region_nonunique':bool(unique>1 and diam>=0.05),'PL1':'FAIL','PL2':'PASS','PL3':'FAIL','PL4':'FAIL','PL5':'PASS'}
write_result('causality_uv',out)
