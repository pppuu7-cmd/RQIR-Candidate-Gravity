import numpy as np
from common import write_result

x=np.linspace(-1.0,1.0,10)
y=np.asarray([0.12,-0.05,0.18,-0.11,0.07,0.20,-0.16,0.09,0.14,-0.08],dtype=float)
coef=np.polynomial.polynomial.polyfit(x,y,9)
yhat=np.polynomial.polynomial.polyval(x,coef)
err=float(np.max(np.abs(y-yhat)))
out={
 'test':'unconstrained single-function finite-holdout interpolation control',
 'probe_coordinates':x,
 'target_vector':y,
 'polynomial_degree':9,
 'coefficient_count':len(coef),
 'coefficients_low_to_high':coef,
 'max_interpolation_error':err,
 'interpolation_error_le_1e_10':err<=1e-10,
 'coefficient_count_10':len(coef)==10,
 'unconstrained_function_interpolates_arbitrary_finite_holdout':err<=1e-10 and len(coef)==10,
 'no_hidden_functional_freedom':False,
 'parent_law_credit':False,
 'conclusion':'One unconstrained function is not automatically low-dimensional physics: a degree-9 function can encode ten arbitrary finite holdout values exactly, so compact notation can hide pointwise freedom.'
}
write_result('functional_freedom',out)
