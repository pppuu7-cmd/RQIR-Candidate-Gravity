import numpy as np
from common import write
rng=np.random.default_rng(2803)
J=rng.normal(size=(6,3))
C=rng.normal(scale=0.2,size=(6,3))
def delta(u):
    u=np.asarray(u,float)
    return J@u + (C*(u[None,:]**3)).sum(axis=1)
def estimate(h):
    E=np.eye(3); cols=[]
    for i in range(3):
        cols.append((delta(h*E[i])-delta(-h*E[i]))/(2*h))
    return np.column_stack(cols)
J1=estimate(0.1); J2=estimate(0.05)
e1=float(np.linalg.norm(J1-J)); e2=float(np.linalg.norm(J2-J)); ratio=e1/e2
out={'true_shape':list(J.shape),'estimated_shape':list(J1.shape),'error_h_0_1':e1,'error_h_0_05':e2,'error_ratio':ratio,'synthetic_contract_recovers_6x3_shape':J1.shape==(6,3),'second_order_step_halving_ratio_near_4':bool(3.9<=ratio<=4.1)}
write('synthetic_fd_contract',out)
