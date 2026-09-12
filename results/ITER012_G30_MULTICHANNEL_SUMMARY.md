# Iter012 / G30 — Multi-channel comparator closure

Date: 2026-09-12

## Frozen scope

Additive `K<=3` finite two-qubit Markovian independent single-axis measurement-feedback GKSL channels. This gate does **not** cover arbitrary semiclassical gravity, non-Markovian channels, correlated Kossakowski structures, hidden nonlocal channels, or unrestricted LOCC/non-LOCC constructions.

## Authoritative provenance

- workflow run: `34694264478`
- head commit: `fa9be36b422b84614b03f96de7c37660059f2d74`
- aggregate artifact: `10298417946`
- aggregate digest: `sha256:7c4095c8ddd329b53973fd1bc5b0b823455b2b543c26fe370aba748806b6f0b0`
- workflow: `.github/workflows/rcg-iter012-multichannel.yml`
- computation: `scripts/iter012_multichannel_comparator.py`

## Frozen gate

Twenty lanes: four shards each of `adversarial_k2`, `adversarial_k3`, `aligned_split`, `admissibility_k3`, and `null_k2`.

Scientific-support threshold for adversarial/aligned gap lanes was prospectively `trace_distance > 1e-4`. Admissibility required generator trace preservation, Choi positivity to numerical tolerance, and output-state PSD. Null control required exact in-family self recovery.

## Raw aggregate result

- `n_results = 20`
- structural validity: `20/20`
- scientific-support flags under the frozen local criteria: `20/20`
- minimum K=2 adversarial gap: `0.025014400602647237`
- minimum K=3 adversarial gap: `0.025028081208365957`
- all five streams: `4/4` structurally valid and `4/4` local-support flags

## Scientific classification

`DERIVED_SCOPED_NEGATIVE_COMPARATOR_RESULT_WITH_MULTICHANNEL_ROBUSTNESS`

Within the frozen additive independent-channel family, allowing two or three channels did not close the coherent-target trace-distance gap. The near-equality of the K=2 and K=3 minima suggests saturation inside this particular parametrized family, but **does not prove global optimality** because G30 used finite-restart coordinate search.

## Interpretation ceiling

Supported: the RCG target remains distinguishable from the tested finite additive K<=3 independent-channel Markovian GKSL comparators under the frozen search and controls.

Not supported: any claim excluding all semiclassical gravity, all classical mediators, arbitrary correlated GKSL generators, non-Markovian feedback, or all measurement-feedback constructions.

## Next authorized gate

G31 must calibrate the nearest-comparator search itself with a stronger global optimizer and positive in-family recovery controls, while simultaneously extending to K=4 and rechecking CPTP/PSD admissibility. No promotion is allowed if the positive-control optimizer cannot recover known in-family targets to the preregistered tolerance.
