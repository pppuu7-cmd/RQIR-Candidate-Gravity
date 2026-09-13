import argparse, json, math, os
import numpy as np
from scipy.integrate import quad

RATIOS = (1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0)
BRANCH_DS = (0.45, 0.62, 0.57, 0.48)
SIGNS = (1.0, -1.0, -1.0, 1.0)


def gaussian_kernel(R, s):
    return math.erf(R/(math.sqrt(2.0)*s))/R


def fourier_kernel(R, s):
    ratio = R/s
    def f(x):
        if abs(x) < 1e-15:
            sinc = 1.0
        else:
            sinc = math.sin(x*ratio)/(x*ratio)
        return math.exp(-0.5*x*x)*sinc
    val, err = quad(f, 0.0, 12.0, epsabs=1e-13, epsrel=1e-13, limit=1000)
    return (2.0/math.pi)*val/s, err


def relerr(a,b):
    return abs(a-b)/max(abs(b),1e-30)


def branch_cross(ds, s):
    vals=[gaussian_kernel(d,s) for d in ds]
    return sum(sign*v for sign,v in zip(SIGNS,vals))


def point_cross(ds):
    return sum(sign/d for sign,d in zip(SIGNS,ds))


def run(case):
    ratio = RATIOS[case]
    s = 1.0
    R = ratio*s
    analytic = gaussian_kernel(R,s)
    numeric, quad_err = fourier_kernel(R,s)
    numerical_relerr = relerr(numeric,analytic)
    point = 1.0/R
    point_ratio = analytic/point
    point_relative_difference = relerr(analytic,point)

    s_branch = min(BRANCH_DS)/ratio
    finite_cross = branch_cross(BRANCH_DS,s_branch)
    p_cross = point_cross(BRANCH_DS)
    branch_point_relerr = relerr(finite_cross,p_cross)

    null_ds=(0.5,0.5,0.5,0.5)
    null_cross=branch_cross(null_ds, min(null_ds)/ratio)

    checks={
        'numerical_vs_analytic': numerical_relerr <= 1e-10,
        'positive_finite': bool(np.isfinite(analytic) and analytic>0 and np.isfinite(numeric) and numeric>0),
        'point_ratio_domain': 0.0 < point_ratio <= 1.0 + 1e-14,
        'high_ratio_point_limit': True if ratio < 8.0 else point_relative_difference <= 1e-12,
        'high_ratio_branch_limit': True if ratio < 8.0 else branch_point_relerr <= 1e-10,
        'equal_geometry_null': abs(null_cross) <= 1e-12,
    }
    structural_valid = ratio>0 and s>0 and R>0
    lane_support = bool(structural_valid and all(checks.values()))
    return {
        'iteration':'Iter049','gate':'G53-W','case':case,'R_over_s':ratio,
        'analytic_kernel':analytic,'numeric_fourier_kernel':numeric,'quad_error_estimate':quad_err,
        'numerical_relative_error':numerical_relerr,
        'point_kernel':point,'point_ratio':point_ratio,'point_relative_difference':point_relative_difference,
        'branch_relative_width_s_m':s_branch,'finite_size_branch_cross_difference':finite_cross,
        'point_branch_cross_difference':p_cross,'branch_point_relative_error':branch_point_relerr,
        'equal_geometry_null_cross_difference':null_cross,
        'checks':checks,'structural_valid':structural_valid,'lane_support':lane_support,
        'frozen_thresholds':{'numeric_rel':1e-10,'high_ratio_point_rel':1e-12,'high_ratio_branch_rel':1e-10,'null_abs':1e-12},
        'scope_lock':'Isotropic Gaussian finite-size weak-field kernel bridge only; not a covariant continuum quantum-gravity dynamics.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--case',type=int,required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); r=run(a.case)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(r,f,indent=2)
    print(json.dumps(r,indent=2))
    if not r['lane_support']: raise SystemExit(1)

if __name__=='__main__': main()
