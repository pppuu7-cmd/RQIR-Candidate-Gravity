# Compute Wave 6 — All-Order Closure Results

**Source branch:** `post-freeze-all-order-wave6`  
**GitHub Actions run:** `34654330846`  
**Status:** COMPLETE / 5 PRIMARY JOBS + AGGREGATOR SUCCESS

## Aggregate verdict

All required artifacts were present. The aggregator returned:

- `finite_relevant_RG_surface_is_not_unique_trajectory = true`;
- `finite_rank_recurrence_can_close_sequence = true`;
- `spectral_closure_needs_extra_rank_form_assumption = true`;
- `finite_Regge_law_generates_infinite_tower_but_is_known_comparator = true`;
- `same_IR_gap_leaves_positive_microscopic_transfer_family = true`;
- `obvious_all_order_routes_fail_novelty_by_name_only = true`;
- `candidate_all_order_primitive_found = false`.

## RG / fixed-point stream

A linearized 8-coupling fixed-point proxy with three positive critical exponents was used. UV completeness reduced the flow to a 3-dimensional critical surface but did not select a unique trajectory.

- relevant directions: 3;
- irrelevant directions: 5;
- sampled UV-complete trajectories: 125;
- representative IR-observable widths across the critical surface: `1.01, 0.80, 0.77, 0.72`;
- three independent IR conditions were required to solve the three relevant amplitudes.

Interpretation: asymptotic-safety-style finite predictivity is not the same as zero-parameter uniqueness. A deeper rule would still be needed to determine the relevant coordinates prospectively.

## Spectral recurrence stream

A three-atom positive spectral measure was generated. Assuming a rank-3 moment recurrence, the all-order sequence was reconstructed with maximum error `1.18e-16`.

However, without fixing that rank/form, positive measures matching only finite moments remained nonunique. Widths of the next-moment interval after matching through orders 2–5 were approximately:

- `3.4456e-2`;
- `7.6248e-3`;
- `1.5211e-3`;
- `3.1834e-4`.

Interpretation: finite-rank recurrence is a genuine compression mechanism, but the rank/recurrence itself is extra microscopic information unless derived from another principle.

## Regge / tower stream

A finite two-parameter linear Regge law generated an arbitrarily long evenly spaced pole tower. This demonstrates the type of finite generative compression an all-order theory needs.

Comparator firewall verdict: this route is already string/Regge/higher-spin-like and cannot count as Candidate Gravity novelty by itself.

## Nonperturbative transfer stream

A positive symmetric 4-state transfer-matrix family was constructed with the same fixed leading nontrivial eigenvalue `lambda1 = 0.4`, hence the same correlation-length proxy `xi = 1.0913567`.

Yet 24 distinct positive microscopic rules remained admissible. Their finite-step return probabilities varied with widths:

- `return_p2_width = 0.22560794`;
- `return_p4_width = 0.20362656`.

Interpretation: the correct IR gap/spectrum does not determine a unique microscopic path-integral/transfer rule.

## Comparator firewall

The obvious all-order routes audited here map closely onto established programs:

- UV fixed point -> asymptotic safety / functional RG;
- finite spectral recurrence -> spectral reconstruction / Padé / finite-pole ansatz;
- meromorphic infinite tower -> string / Regge / higher-spin completion;
- nonperturbative transfer/path integral -> lattice / CDT / spinfoam-type programs;
- modular/algebraic selection -> algebraic-QFT / modular-bootstrap / holographic families.

Therefore novelty cannot be claimed from relabeling one of these mechanisms. A new result must be a quantitative comparator-orthogonal cross-constraint or finite generating law.

## External literature anchor

The interpretation is consistent with the standard asymptotic-safety notion that a UV fixed point with finitely many relevant directions yields a predictive finite-dimensional critical surface rather than automatically a unique trajectory. Recent work continues to treat the connection from UV fixed point to physical, gauge-invariant observables as a substantive part of the program rather than a solved uniqueness theorem.

Representative anchors:

- D. Benedetti, *On the number of relevant operators in asymptotically safe gravity*, arXiv:1301.4422;
- R. Ferrero, *Asymptotic Safety and Canonical Quantum Gravity*, arXiv:2507.14296.

## New frontier

The next high-value question is not whether finite closure mechanisms exist — they do. It is whether **independent RQIR-compatible constraints can derive the missing closure data**:

1. derive RG relevant coordinates rather than fit them;
2. derive spectral rank/recurrence rather than assume it;
3. derive a tower-generating law rather than import a known string/Regge comparator;
4. derive a unique microscopic measure/state rule from operational data.

This motivates Wave 7: cross-constraint closure and incompatibility tests.
