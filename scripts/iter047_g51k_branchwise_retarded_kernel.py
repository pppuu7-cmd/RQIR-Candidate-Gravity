import argparse, json, os

C = 299792458.0
SIGNS = (1.0, -1.0, -1.0, 1.0)
CASES = [
    (0.45, 0.62, 0.57, 0.48),
    (0.37, 0.54, 0.49, 0.41),
    (0.28, 0.51, 0.44, 0.35),
    (0.73, 0.91, 0.82, 0.77),
    (0.19, 0.32, 0.27, 0.22),
    (1.10, 1.40, 1.25, 1.17),
    (0.52, 0.89, 0.71, 0.58),
    (0.33, 0.77, 0.61, 0.39),
]


def geom(ds):
    return sum(s / d for s, d in zip(SIGNS, ds))


def branchwise_kernel(t, ds):
    return sum(s * max(0.0, t - d / C) / d for s, d in zip(SIGNS, ds))


def common_rmax_kernel(t, ds):
    return max(0.0, t - max(ds) / C) * geom(ds)


def relerr(a, b):
    return abs(a - b) / max(abs(b), 1e-30)


def run(case):
    ds = CASES[case]
    g = geom(ds)
    tau_min = min(ds) / C
    tau_max = max(ds) / C

    pre_t = 0.5 * tau_min
    pre = branchwise_kernel(pre_t, ds)
    pre_ok = abs(pre) <= 1e-18

    post = []
    for factor in (1.25, 2.0, 10.0):
        t = factor * tau_max
        br = branchwise_kernel(t, ds)
        expected = t * g
        er = relerr(br, expected)
        post.append({"factor": factor, "branchwise": br, "expected": expected, "relative_error": er})
    post_ok = all(row["relative_error"] <= 1e-12 for row in post)

    t_probe = 2.0 * tau_max
    br_probe = branchwise_kernel(t_probe, ds)
    common_probe = common_rmax_kernel(t_probe, ds)
    proxy_rel_difference = abs(common_probe - br_probe) / max(abs(br_probe), 1e-30)
    proxy_discrimination_ok = proxy_rel_difference >= 0.1

    null_ds = (0.5, 0.5, 0.5, 0.5)
    null_tau = 0.5 / C
    null_times = (0.5 * null_tau, 1.0 * null_tau, 2.0 * null_tau, 10.0 * null_tau)
    null_values = []
    for t in null_times:
        null_values.append({
            "t": t,
            "branchwise": branchwise_kernel(t, null_ds),
            "common": common_rmax_kernel(t, null_ds),
        })
    null_ok = all(abs(r["branchwise"]) <= 1e-18 and abs(r["common"]) <= 1e-18 for r in null_values)

    structural_valid = all(d > 0 for d in ds) and abs(g) > 1e-12
    lane_support = bool(structural_valid and pre_ok and post_ok and proxy_discrimination_ok and null_ok)

    result = {
        "iteration": "Iter047",
        "gate": "G51-K",
        "case": case,
        "distances_m": list(ds),
        "geometric_cross_difference_per_m": g,
        "tau_min_s": tau_min,
        "tau_max_s": tau_max,
        "pre_lightcone": {"t": pre_t, "value": pre, "pass": pre_ok},
        "post_all_identity": post,
        "post_all_identity_pass": post_ok,
        "shared_rmax_proxy_probe": {
            "t": t_probe,
            "branchwise": br_probe,
            "common_rmax": common_probe,
            "relative_difference": proxy_rel_difference,
            "pass": proxy_discrimination_ok,
        },
        "equal_geometry_null": {"samples": null_values, "pass": null_ok},
        "structural_valid": structural_valid,
        "lane_support": lane_support,
        "frozen_thresholds": {
            "pre_abs": 1e-18,
            "post_relative": 1e-12,
            "proxy_relative_difference_min": 0.1,
            "null_abs": 1e-18,
        },
        "scope_lock": "Finite branchwise-retarded weak-field toy-kernel audit only; not a covariant GR retarded Green-function derivation.",
    }
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", type=int, required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    r = run(a.case)
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    with open(a.out, "w") as f:
        json.dump(r, f, indent=2)
    print(json.dumps(r, indent=2))
    if not r["lane_support"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
