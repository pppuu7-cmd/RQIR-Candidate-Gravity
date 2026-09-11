# Compute Wave 2 — Gravity-Specific Results

**Branch:** `post-freeze-gravity-specific-wave2`  
**GitHub Actions run:** `34652727310`  
**Status:** COMPLETE / 4 OF 4 PRIMARY JOBS + AGGREGATOR SUCCESS  
**Relation to frozen v0:** post-freeze only; no back-edit of the independent RQIR reconstruction.

## Aggregate signals

All planned checks completed with no missing artifacts:

- `positive_TT_spectrum_finite_data_nonunique = true`;
- `finite_Q_TT_shape_nonunique_after_low_energy_fix = true`;
- `Ward_projectors_numerically_transverse = true`;
- `Ward_leaves_regular_form_factor_freedom = true`;
- `causal_low_frequency_data_leave_finite_frequency_shape_freedom = true`;
- `simple_local_q4_TT_has_no_healthy_nonzero_coefficient_in_scan = true`.

## E — fixed GR massless pole + positive massive TT spectrum

Proxy:

`D_TT(Q^2) = 1/Q^2 + sum_i w_i/(Q^2+M_i^2)`, with `w_i >= 0`.

The unit massless pole residue is frozen to the GR value. The positive massive sector therefore represents an explicitly ghost-free discrete spectral correction in this finite proxy.

After fixing successive low-energy inverse moments, the next coefficient remains nonunique:

| fixed coefficients | spectral affine nullity | next-coefficient width |
|---:|---:|---:|
| 1 | 4 | 0.18603515625 |
| 2 | 3 | 0.0270538330078 |
| 3 | 2 | 0.00199556350708 |
| 4 | 1 | 0.0000650882720964 |

After only the first two low-energy coefficients are fixed, the finite-Euclidean-momentum correction also varies:

| Q^2 | response width |
|---:|---:|
| 0.25 | 0.00114482721 |
| 1 | 0.00749684343 |
| 4 | 0.01558159722 |
| 10 | 0.01211895743 |

**Result:** a correct GR massless pole + positive extra TT spectral weight + finitely many low-energy coefficients still does not select a unique spectrum or finite-momentum response.

## F — Ward-transverse spin-2/scalar form factors

In Euclidean D=4 the standard transverse projectors were constructed numerically.

Maximum Ward-transversality error:

`1.04e-16`.

A random projected conserved source had conservation error:

`2.22e-16`.

The general transverse response

`K = A(k^2) P^(2) + B(k^2) P^(0)`

therefore obeys the Ward constraint for arbitrary scalar form factors `A,B`.

The GR massless-pole ratio in this projector convention is

`B/A = -1/2`.

But regular analytic corrections remain free. For maximum regular power `N=8` there are 18 regular coefficients before low-order fixing. Even after the first three regular orders in both sectors are fixed, **12 coefficients remain free**.

**Result:** Ward/gauge transversality constrains tensor support but does not select the momentum-dependent dynamics.

## G — causal/passive retarded-response shape

Finite stable-pole response proxy:

`chi_corr(omega) = sum_i w_i / (M_i^2 - omega^2 - i Gamma_i omega)`

with positive residues and positive damping.

We fixed four pieces of low-frequency data:

1. total positive weight;
2. zero-frequency response;
3. linear dissipative coefficient;
4. quadratic dispersive coefficient.

The six-mode proxy still has affine nullity 2.

Selected finite-frequency ranges:

| omega | Re width | Im width |
|---:|---:|---:|
| 0.2 | 5.52e-6 | 4.15e-6 |
| 0.5 | 3.316e-4 | 1.810e-4 |
| 0.8 | 0.005516 | 0.005129 |
| 1.2 | 0.088263 | 0.026356 |
| 2.0 | 0.288175 | 0.193695 |
| 4.0 | 0.104128 | 0.025758 |

**Result:** causality/passivity plus several low-frequency coefficients can make the response nearly rigid deep in the IR, yet still leave large finite-frequency freedom near and above internal scales.

## H — simplest local q^4 TT modification

Tested

`D_2(k^2) = 1 / [k^2 (1 - a k^2)]`.

For real nonzero `a`:

- `a > 0`: the extra pole has positive mass-squared `1/a`, but its partial-fraction residue is `-1` — a spin-2 ghost in the standard pole interpretation;
- `a < 0`: the extra pole has negative mass-squared — tachyonic in the declared convention;
- `a = 0`: only the GR TT pole remains.

The scan found no healthy nonzero `a` in this restricted one-factor local ansatz.

This agrees with the standard curvature-squared/Stelle propagator issue: a massive spin-2 pole appears with negative residue in the usual quantization.

**Scope warning:** this does not exclude fakeon/Lee-Wick prescriptions, nonlocal entire form factors, extra constrained fields, bimetric UV completions, or other nonstandard mechanisms. Those are precisely separate physical hypotheses and must be tested as such.

## Scientific synthesis

Wave 2 creates a sharper fork than wave 1:

1. **standard healthy spectral/covariant/causal constraints:** still leave families;
2. **the cheapest local higher-derivative TT deformation:** is not healthy in the standard pole interpretation;
3. therefore a new two-point law cannot be obtained merely by 'adding the first higher derivative' while retaining all standard assumptions.

The next wave should test the principal escape routes explicitly:

- positive additional spectral states/continuum;
- entire/nonlocal UV-softened propagators and their relation to positive spectral representation;
- modified pole prescriptions and causal support;
- higher-point-only deformations that leave the GR propagator unchanged.
