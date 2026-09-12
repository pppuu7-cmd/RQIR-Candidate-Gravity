import numpy as np
from common import X, write_result

def dc(a,b):
    a=np.asarray(a,float); b=np.asarray(b,float)
    return np.asarray([a[0]*b[0],a[1]*b[1],a[0]*b[1]+a[1]*b[0],a[2]*b[2],a[0]*b[2]+a[2]*b[0],a[1]*b[2]+a[2]*b[1]],float)
A1=[0.8,-0.4,0.3]; B1=[0.7,0.5,-0.2]
A2=[0.45,0.6,-0.5]; B2=[-0.3,0.9,0.4]
g1=dc(A1,B1); g2=dc(A2,B2)
d=float(np.linalg.norm(X()@g1-X()@g2))
out={'principle':'K5_double_copy','gravity_vector_1':g1,'gravity_vector_2':g2,'holdout_prediction_distance':d,'double_copy_is_conditional_on_parent_choice':bool(d>=0.05),'PL1':'FAIL','PL2':'PASS','PL3':'FAIL','PL4':'PASS','PL5':'FAIL'}
write_result('double_copy',out)
