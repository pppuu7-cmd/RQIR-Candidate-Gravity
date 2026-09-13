import argparse, json, math, os
import numpy as np
from scipy.integrate import quad

RATIOS = (0.35, 0.70, 1.20, 2.00, 3.00, 4.00)
SCALES = (0.071, 0.113, 0.173, 0.257, 0.389, 0.541)
SQRT2PI = math.sqrt(2.0 / math.pi)
ORIENTATIONS = (
    np.array([1.0, 0.0, 0.0]),
    np.array([1.0, 1.0, 1.0]),
    np.array([2.0, -1.0, 3.0]),
)
ORIENTATIONS = tuple(v / np.linalg.norm(v) for v in ORIENTATIONS)


def kernel_r(r, s):
    if r == 0.0:
        return SQRT2PI / s
    return math.erf(r / (math.sqrt(2.0) * s)) / r


def rho_r(r, s):
    return math.exp(-0.5 * (r / s) ** 2) / ((2.0 * math.pi) ** 1.5 * s ** 3)


def enclosed_fraction(r, s):
    u = r / s
    return math.erf(u / math.sqrt(2.0)) - SQRT2PI * u * math.exp(-0.5 * u * u)


def second_derivative_5(f, x, h, axis):
    e = np.zeros(3)
    e[axis] = h
    return (-f(x + 2*e) + 16*f(x + e) - 30*f(x) + 16*f(x - e) - f(x - 2*e)) / (12*h*h)


def cartesian_laplacian(x, s, h):
    f = lambda y: kernel_r(float(np.linalg.norm(y)), s)
    return sum(second_derivative_5(f, x, h, a) for a in range(3))


def radial_first_5(r, s, h):
    f = lambda z: kernel_r(float(z), s)
    return (f(r - 2*h) - 8*f(r - h) + 8*f(r + h) - f(r + 2*h)) / (12*h)


def relerr(a, b):
    return abs(a - b) / max(abs(b), 1e-300)


def run(case):
    u = float(RATIOS[case])
    s = float(SCALES[case])
    r = u * s
    h = 0.01 * s

    k = kernel_r(r, s)
    rho = rho_r(r, s)
    source_lap = -4.0 * math.pi * rho
    mfrac = enclosed_fraction(r, s)

    laps = []
    lap_relerrs = []
    for n in ORIENTATIONS:
        x = r * n
        lap = float(cartesian_laplacian(x, s, h))
        laps.append(lap)
        lap_relerrs.append(relerr(lap, source_lap))

    scaled_laps = [float((s**3) * x) for x in laps]
    orient_spread = float(max(scaled_laps) - min(scaled_laps))
    worst_lap_rel = float(max(lap_relerrs))

    dkr = float(radial_first_5(r, s, h))
    flux = float(-r*r*dkr)
    flux_abs_error = float(abs(flux - mfrac))

    norm, norm_err = quad(
        lambda rr: 4.0 * math.pi * rr * rr * rho_r(rr, s),
        0.0, 12.0*s, epsabs=1e-13, epsrel=1e-13, limit=500
    )
    norm_abs_error = float(abs(norm - 1.0))

    q_dimless = math.erf(u / math.sqrt(2.0)) / u
    rho_dimless = math.exp(-0.5*u*u) / ((2.0*math.pi)**1.5)
    lap_dimless = -SQRT2PI * math.exp(-0.5*u*u)
    scale_k_error = float(abs(s*k - q_dimless))
    scale_rho_error = float(abs((s**3)*rho - rho_dimless))
    scale_lap_error = float(abs((s**3)*source_lap - lap_dimless))

    wrong_sign = +4.0 * math.pi * rho
    wrong_sign_min_rel = float(min(relerr(lap, wrong_sign) for lap in laps))
    wrong_rho = rho_r(r, 1.3*s)
    wrong_width_rel = float(relerr(wrong_rho, rho))

    finite = bool(all(np.isfinite(v) for v in [k,rho,source_lap,mfrac,*laps,flux,norm,
        scale_k_error,scale_rho_error,scale_lap_error,wrong_sign_min_rel,wrong_width_rel]))
    checks = {
        'cartesian_laplacian': bool(worst_lap_rel <= 2e-5),
        'orientation_scaled_spread': bool(orient_spread <= 2e-7),
        'gauss_flux': bool(flux_abs_error <= 2e-8),
        'source_normalization': bool(norm_abs_error <= 2e-10),
        'source_positive': bool(rho > 0.0),
        'enclosed_fraction_range': bool(0.0 < mfrac < 1.0),
        'scale_collapse_kernel': bool(scale_k_error <= 2e-12),
        'scale_collapse_source': bool(scale_rho_error <= 2e-12),
        'scale_collapse_laplacian': bool(scale_lap_error <= 2e-12),
        'wrong_sign_negative_control': bool(wrong_sign_min_rel >= 1.5),
        'wrong_width_negative_control': bool(wrong_width_rel >= 0.05),
        'finite': finite,
    }
    structural_valid = bool(case in range(6) and u > 0 and s > 0 and r > 2*h)
    lane_support = bool(structural_valid and all(checks.values()))

    return {
        'iteration':'Iter052','gate':'G56-F','case':case,'u_r_over_s':u,'s':s,'r':r,'h':h,
        'kernel':k,'rho':rho,'analytic_laplacian':source_lap,
        'cartesian_laplacians':laps,'cartesian_laplacian_relative_errors':lap_relerrs,
        'worst_cartesian_laplacian_relative_error':worst_lap_rel,
        'scaled_laplacians':scaled_laps,'orientation_scaled_laplacian_spread':orient_spread,
        'enclosed_fraction':mfrac,'numeric_gauss_flux':flux,'gauss_flux_absolute_error':flux_abs_error,
        'source_normalization_0_12s':float(norm),'source_normalization_quad_error':float(norm_err),
        'source_normalization_absolute_error':norm_abs_error,
        'scale_kernel_absolute_error':scale_k_error,'scale_source_absolute_error':scale_rho_error,
        'scale_laplacian_absolute_error':scale_lap_error,
        'wrong_sign_min_relative_error':wrong_sign_min_rel,'wrong_width_relative_difference':wrong_width_rel,
        'checks':checks,'structural_valid':structural_valid,'lane_support':lane_support,
        'scope_lock':'RCG-002 isotropic Gaussian weak-field continuum source/kernel closure only; not a covariant gravity theory or dynamical field equation.'
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--case',type=int,required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    result=run(a.case)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(result,f,indent=2)
    print(json.dumps(result,indent=2))
    if not result['structural_valid']:
        raise SystemExit(2)

if __name__=='__main__':
    main()
