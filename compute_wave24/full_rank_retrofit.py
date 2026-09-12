import numpy as np
from common import TARGET_A,TARGET_B,Q6,X_and_probes,write_result

X,_=X_and_probes()
A=np.eye(6)
bA=A@TARGET_A
Bsel=Q6
bB=Bsel@TARGET_B
solA=np.linalg.solve(A,bA)
solB=np.linalg.solve(Bsel,bB)
yA=X@solA
yB=X@solB
dist=float(np.linalg.norm(yA-yB))
out={
 'test':'arbitrary full-rank selector conflict control',
 'selector_A_rank':int(np.linalg.matrix_rank(A)),
 'selector_B_rank':int(np.linalg.matrix_rank(Bsel)),
 'selected_theta_A':solA,
 'selected_theta_B':solB,
 'holdout_prediction_distance_l2':dist,
 'both_selectors_full_rank':int(np.linalg.matrix_rank(A))==6 and int(np.linalg.matrix_rank(Bsel))==6,
 'prediction_distance_ge_0_05':dist>=0.05,
 'arbitrary_full_rank_selectors_can_choose_conflicting_unique_points':int(np.linalg.matrix_rank(A))==6 and int(np.linalg.matrix_rank(Bsel))==6 and dist>=0.05,
 'independent_physics_credit':False,
 'conclusion':'Algebraic rank-six closure is insufficient as evidence: two equally finite full-rank postulates can uniquely select different theories and make materially different frozen-bank predictions.'
}
write_result('full_rank_retrofit',out)
