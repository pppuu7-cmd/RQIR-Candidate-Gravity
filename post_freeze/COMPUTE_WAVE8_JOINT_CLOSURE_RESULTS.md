# Compute Wave 8 — Joint Closure Results

**Source branch:** `post-freeze-joint-closure-wave8`  
**GitHub Actions run:** `34654893093`  
**Status:** COMPLETE / 5 PRIMARY JOBS + AGGREGATOR SUCCESS

## Aggregate signals

All required artifacts were present and every predeclared signal was true:

- `two_subtractions_leave_two_finite_data = true`;
- `two_independent_inputs_close_subtractions_and_predict_holdout = true`;
- `s2_Regge_growth_truncates_but_does_not_close_contacts = true`;
- `shared_latent_architecture_can_close_design_and_predict_holdout = true`;
- `unlinked_sector_model_retains_holdout_ambiguity = true`;
- `naive_local_sign_not_scale_invariant_but_physical_sum_can_be = true`;
- `dispersion_Regge_route_is_established_comparator_territory = true`.

The aggregator set:

- `joint_closure_architecture_demonstrated = true`;
- `physical_cross_sector_law_derived = false`;
- `candidate_new_QG_primitive_found = false`.

## A — two-subtraction closure

A finite pole proxy for a twice-subtracted dispersion relation was used,

`A(s)=a0+a1*s+s^2 Sum_i r_i/[M_i^2(M_i^2-s)]`.

With the absorptive/spectral part fixed, exactly two subtraction constants remained.

Synthetic truth:

- `a0 = 0.17`;
- `a1 = -0.08`.

Two design points, `s=-0.5` and `s=-1.25`, recovered both constants exactly. An untouched holdout at `s=-2` was then predicted:

- true holdout: `0.4853131313131313`;
- predicted holdout: `0.4853131313131313`;
- absolute error: `0`.

Without the two subtraction inputs, the scanned holdout family had width `2.2`.

Scientific point: a two-subtraction dispersive structure turns an unlimited functional ambiguity into a finite-data problem but does not itself provide those finite data.

## B — Regge-bounded contact nullspace

A crossing-symmetric massless `2->2` polynomial proxy used invariants

- `x=s^2+t^2+u^2`;
- `y=s*t*u`;
- `s+t+u=0`.

At fixed `t` and large `s`, both `x` and `y` scale as `s^2`. Imposing a schematic gravitational Regge growth bound `<= s^2` reduced a 25-element scanned polynomial basis to

`{1, x, y}`.

Then:

- removing the constant by a soft/no-constant condition left `{x,y}`;
- fixing one leading low-energy `x` coefficient still left `{y}`;
- residual contact dimension: `1`.

Thus Regge growth is highly restrictive but does not by itself close the contact sector in this proxy.

## C — shared latent primitive versus unlinked sectors

Five sector-level quantities were considered: three RG-relevant coordinates plus two spectral/amplitude features.

Two architectures were compared using the **same four design observables** and an untouched holdout.

### Unlinked architecture

- independent sector parameters: `5`;
- design rank: `4`;
- nullity: `1`;
- holdout sensitivity along the unit null direction: `0.07295601857`;
- holdout width for a unit null scan: `0.14591203713`.

Therefore the design data did not determine the holdout.

### Shared finite latent architecture

A synthetic three-parameter latent primitive `p` generated all five sector quantities through one cross-sector map.

- latent dimension: `3`;
- design rank in latent coordinates: `3`;
- latent nullity: `0`;
- true latent: `[0.18,-0.11,0.23]`;
- maximum latent recovery error: `1.25e-16`;
- true holdout: `0.1205`;
- predicted holdout: `0.1205`;
- holdout error: `4.16e-17`.

This is the first explicit demonstration in the post-freeze programme that the **right kind of shared finite law** can turn otherwise underdetermined cross-sector data into a prospective holdout prediction.

However the map was deliberately synthetic. Its success is an architecture result, not evidence for a new physical law.

## D — RG-consistent dispersive bookkeeping

A toy running local coefficient `C(mu)` and compensating dispersive contribution `I(mu)` were defined so that their physical combination is scale independent.

Across the scale scan, the local renormalized coefficient changes sign while the combined physical quantity remains invariant and positive.

Therefore a positivity gate should not be formulated as a naive sign requirement on a single scheme-dependent Wilson/subtraction coefficient once graviton loops and RG running matter.

This is consistent with recent gravitational dispersion literature emphasizing loop and RG corrections to naive positivity arguments.

## E — comparator firewall

The strong ingredients used here are established research tools:

- gravitational Regge/dispersion bounds;
- amplitude positivity/bootstrap;
- loop-corrected gravitational EFT dispersion;
- string/Regge/higher-spin completion mechanisms.

Accordingly the synthetic existence of a low-dimensional shared map is not Candidate-Gravity novelty.

Novelty can only be earned if RQIR or another independent physical principle **derives** a comparator-orthogonal quantitative cross-relation among RG-relevant coordinates, spectral data and amplitude/subtraction data and then survives holdout testing.

## External anchors

- Häring & Zhiboedov, *Gravitational Regge bounds*, arXiv:2202.08280 — under stated assumptions, two-subtraction dispersion relations and schematic local growth not faster than `s^2`;
- Chang & Parra-Martinez, *Graviton loops and negativity*, arXiv:2501.17949 — loop corrections and care with gravitational positivity/forward singularities;
- Fernandez, Ruhdorfer & Serra, *Negative running of gravitational positivity*, arXiv:2603.15755 — RG-running effects in gravitational positivity bookkeeping.

## New frontier

The design problem has now contracted from an arbitrary theory space to a finite missing relation:

> Find a physically derived cross-sector rule that fixes at least one residual subtraction/contact datum from independently defined RG or spectral data, and then use it to predict an untouched amplitude/response holdout.

Wave 9 therefore targets the **minimal unresolved defect** after imposing Newton-coupling universality/Ward-like relations, soft/Regge structure and spectral-to-dispersion moment relations.
