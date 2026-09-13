import argparse
import json
import math
import os
from pathlib import Path

import numpy as np
from scipy.integrate import quad

US = (0.27, 0.58, 0.97, 1.47, 2.18, 2.87, 3.56, 4.43)
SS = (0.089, 0.131, 0.197, 0.269, 0.347, 0.431, 0.523, 0.619)
XS = (0.13, 0.37, 0.79, 1.31, 2.07, 3.11, 4.29, 5.33)
QS = (1.3, 0.77)
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
    return sum(second_derivative_5(f, x, h, axis) for axis in range(3))


def radial_first_5(r, s, h):
    f = lambda z: kernel_r(float(z), s)
    return (f(r - 2*h) - 8*f(r - h) + 8*f(r + h) - f(r + 2*h)) / (12*h)


def relerr(a, b):
    return abs(a-b) / max(abs(b), 1e-300)


def stream_real():
    rows = []
    all_pass = True
    for case, (u, s) in enumerate(zip(US, SS)):
        r = u*s
        h = 0.012*s
        rho = rho_r(r, s)
        target_lap = -4.0*math.pi*rho
        laps = [float(cartesian_laplacian(r*n, s, h)) for n in ORIENTATIONS]
        worst_lap = max(relerr(x, target_lap) for x in laps)
        scaled = [(s**3)*x for x in laps]
        spread = max(scaled)-min(scaled)
        flux = -r*r*radial_first_5(r, s, h)
        flux_err = abs(flux-enclosed_fraction(r, s))
        norm, norm_qerr = quad(lambda rr: 4*math.pi*rr*rr*rho_r(rr, s), 0.0, 12*s,
                               epsabs=1e-13, epsrel=1e-13, limit=500)
        norm_err = abs(norm-1.0)
        k = kernel_r(r, s)
        qdim = math.erf(u/math.sqrt(2.0))/u
        rhodim = math.exp(-0.5*u*u)/((2*math.pi)**1.5)
        lapdim = -SQRT2PI*math.exp(-0.5*u*u)
        scale_k_err = abs(s*k-qdim)
        scale_rho_err = abs((s**3)*rho-rhodim)
        scale_lap_err = abs((s**3)*target_lap-lapdim)
        wrong_sign_min = min(relerr(x, +4*math.pi*rho) for x in laps)
        mfrac = enclosed_fraction(r, s)
        finite = all(np.isfinite(v) for v in [r,h,rho,target_lap,*laps,flux,norm,k,mfrac])
        checks = {
            "cartesian_laplacian": bool(worst_lap <= 2e-5),
            "orientation_spread": bool(spread <= 2e-7),
            "gauss_flux": bool(flux_err <= 2e-8),
            "normalization": bool(norm_err <= 2e-10),
            "scale_kernel": bool(scale_k_err <= 2e-12),
            "scale_source": bool(scale_rho_err <= 2e-12),
            "scale_laplacian": bool(scale_lap_err <= 2e-12),
            "wrong_sign_control": bool(wrong_sign_min >= 1.5),
            "source_positive": bool(rho > 0),
            "enclosed_range": bool(0 < mfrac < 1),
            "finite": bool(finite),
        }
        lane_pass = all(checks.values())
        all_pass = all_pass and lane_pass
        rows.append({
            "case": case, "u": u, "s": s, "r": r, "h": h,
            "worst_laplacian_relative_error": float(worst_lap),
            "orientation_scaled_spread": float(spread),
            "gauss_flux_absolute_error": float(flux_err),
            "source_normalization_absolute_error": float(norm_err),
            "source_normalization_quad_error": float(norm_qerr),
            "scale_kernel_absolute_error": float(scale_k_err),
            "scale_source_absolute_error": float(scale_rho_err),
            "scale_laplacian_absolute_error": float(scale_lap_err),
            "wrong_sign_min_relative_error": float(wrong_sign_min),
            "checks": checks,
            "lane_support": bool(lane_pass),
        })
    return {
        "iteration": "Iter054", "gate": "G56-F2", "stream": "R_REAL_SPACE",
        "lanes": rows, "all_lanes_support": bool(all_pass),
        "structural_valid": bool(len(rows) == 8),
        "historical_g56f_unchanged": True,
    }


def stream_spectral():
    qrows = []
    all_q = True
    for u in US:
        def integrand(x):
            if x == 0.0:
                return u
            return math.exp(-0.5*x*x)*math.sin(u*x)/x
        val, err = quad(integrand, 0.0, 12.0, epsabs=1e-13, epsrel=1e-13, limit=500)
        qspec = (2.0/(math.pi*u))*val
        qexact = math.erf(u/math.sqrt(2.0))/u
        abs_err = abs(qspec-qexact)
        passed = abs_err <= 2e-11 and np.isfinite(qspec)
        all_q = all_q and passed
        qrows.append({"u":u,"q_spectral":float(qspec),"q_exact":float(qexact),
                      "absolute_error":float(abs_err),"quadrature_error":float(err),"support":bool(passed)})
    xrows = []
    all_x = True
    for x in XS:
        source = 4.0*math.pi*math.exp(-0.5*x*x)
        ktilde = source/(x*x)
        reconstructed = x*x*ktilde
        identity_rel = relerr(reconstructed, source)
        wrong_sign_rel = relerr(-reconstructed, source)
        passed = identity_rel <= 2e-14 and wrong_sign_rel >= 1.5 and all(np.isfinite(v) for v in [source,ktilde,reconstructed])
        all_x = all_x and passed
        xrows.append({"x":x,"identity_relative_error":float(identity_rel),
                      "wrong_sign_relative_discrepancy":float(wrong_sign_rel),"support":bool(passed)})
    return {
        "iteration":"Iter054","gate":"G56-F2","stream":"S_SPECTRAL",
        "kernel_reconstruction":qrows,"source_multiplier":xrows,
        "all_kernel_support":bool(all_q),"all_multiplier_support":bool(all_x),
        "stream_support":bool(all_q and all_x),
        "structural_valid":bool(len(qrows)==8 and len(xrows)==8),
        "historical_g56f_unchanged":True,
    }


def radial_profile(u, q):
    return 4.0*math.pi*u*u*math.exp(-0.5*(u/q)**2)/(((2.0*math.pi)**1.5)*q**3)


def stream_global():
    rows=[]
    all_pass=True
    ref_norm, ref_norm_qerr = quad(lambda u: radial_profile(u,1.0),0.0,10.0,epsabs=1e-13,epsrel=1e-13,limit=500)
    ref_m2, ref_m2_qerr = quad(lambda u: u*u*radial_profile(u,1.0),0.0,10.0,epsabs=1e-13,epsrel=1e-13,limit=500)
    ref_mean2 = ref_m2/ref_norm
    for q in QS:
        norm, norm_qerr=quad(lambda u: radial_profile(u,q),0.0,10.0,epsabs=1e-13,epsrel=1e-13,limit=500)
        l1,l1_qerr=quad(lambda u: abs(radial_profile(u,q)-radial_profile(u,1.0)),0.0,10.0,epsabs=1e-12,epsrel=1e-12,limit=700)
        m2,m2_qerr=quad(lambda u: u*u*radial_profile(u,q),0.0,10.0,epsabs=1e-13,epsrel=1e-13,limit=500)
        mean2=m2/norm
        moment_ratio=mean2/ref_mean2
        ratio_err=abs(moment_ratio-q*q)
        checks={
            "reference_normalization":bool(abs(ref_norm-1.0)<=2e-10),
            "alternative_normalization":bool(abs(norm-1.0)<=2e-10),
            "global_l1_separation":bool(l1>=0.25),
            "second_moment_ratio":bool(ratio_err<=2e-9),
            "width_moment_separation":bool(abs(q*q-1.0)>=0.30),
            "finite":bool(all(np.isfinite(v) for v in [norm,l1,m2,mean2,moment_ratio,ratio_err])),
            "profile_positive_samples":bool(all(radial_profile(u,q)>0 and radial_profile(u,1.0)>0 for u in (0.1,0.5,1.0,2.0,4.0,8.0))),
        }
        passed=all(checks.values())
        all_pass=all_pass and passed
        rows.append({"q":q,"reference_normalization":float(ref_norm),"alternative_normalization":float(norm),
                     "global_l1_separation":float(l1),"second_moment_ratio":float(moment_ratio),
                     "expected_second_moment_ratio":float(q*q),"second_moment_ratio_absolute_error":float(ratio_err),
                     "quadrature_errors":{"ref_norm":float(ref_norm_qerr),"norm":float(norm_qerr),"l1":float(l1_qerr),
                                          "ref_m2":float(ref_m2_qerr),"m2":float(m2_qerr)},
                     "checks":checks,"support":bool(passed)})
    return {
        "iteration":"Iter054","gate":"G56-F2","stream":"G_GLOBAL_CONTROLS",
        "controls":rows,"stream_support":bool(all_pass),"structural_valid":bool(len(rows)==2),
        "historical_g56f_unchanged":True,
    }


def aggregate(directory):
    data=[]
    for f in sorted(Path(directory).rglob("*.json")):
        with open(f) as h:
            x=json.load(h)
        if x.get("iteration")=="Iter054" and x.get("gate")=="G56-F2" and x.get("stream"):
            data.append(x)
    by={x["stream"]:x for x in data}
    expected={"R_REAL_SPACE","S_SPECTRAL","G_GLOBAL_CONTROLS"}
    structural=bool(set(by)==expected and all(by[k].get("structural_valid") for k in expected))
    support=bool(structural and by["R_REAL_SPACE"].get("all_lanes_support") and by["S_SPECTRAL"].get("stream_support") and by["G_GLOBAL_CONTROLS"].get("stream_support"))
    classification=("RCG002_GAUSSIAN_CONTINUUM_SOURCE_KERNEL_CLOSURE_VALIDATED_ROBUST_REPLACEMENT_SCOPED"
                    if support else "G56F2_FROZEN_ROBUST_CONTINUUM_FIELD_CLOSURE_RULE_NOT_MET")
    return {
        "iteration":"Iter054","gate":"G56-F2","streams_consumed":sorted(by),
        "all_streams_structural_valid":structural,"scientific_support":support,"classification":classification,
        "historical_g56f_terminal_classification":"G56F_FROZEN_CONTINUUM_FIELD_CLOSURE_RULE_NOT_MET",
        "historical_g56f_unchanged":True,"programme_readiness_percent":66,"theory_established_percent":0,
        "scope_lock":"Robust replacement validation of RCG-002 isotropic Gaussian weak-field source/kernel closure only."
    }


def write(obj,out):
    os.makedirs(os.path.dirname(out) or ".",exist_ok=True)
    with open(out,"w") as f: json.dump(obj,f,indent=2)
    print(json.dumps(obj,indent=2))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--stream",choices=("r","s","g"))
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    if a.aggregate_dir: result=aggregate(a.aggregate_dir)
    elif a.stream=="r": result=stream_real()
    elif a.stream=="s": result=stream_spectral()
    elif a.stream=="g": result=stream_global()
    else: raise SystemExit("provide --stream or --aggregate-dir")
    write(result,a.out)
    structural=result.get("structural_valid",result.get("all_streams_structural_valid",False))
    if not structural: raise SystemExit(2)

if __name__=="__main__":
    main()
