# ANSATZ-RQIR-QLC — Quantum-Limited Relational Gravity Channel

**Version:** 0.1  
**Status:** DRAFT / TESTING  
**Type:** low-energy operational gravity-interface model (Gaussian quantum channel in a finite relational mode sector)  
**Origin:** frozen RQIR v1.0; no polygon-derived QGR equations or model-specific benchmark repairs used  
**Novelty claim:** not yet established.

## 0. Why this branch exists

The metric-only minimum-complexity root `ANSATZ-RQIR-MIN` naturally falls into the C5 perturbative quantum-GR/EFT class. The present branch asks a different RQIR-native question:

> Can the gravity–quantum interface itself be the primary dynamical object, constrained directly by causal GR response, quantum complete positivity, relational observability and minimum added noise?

The RQIR model template explicitly permits a channel as primary dynamics. This branch therefore treats the operational interface map, rather than a microscopic UV field theory, as fundamental within its declared domain.

## 1. Domain and mode reduction

Work in a controlled weak-field, low-energy sector around a globally hyperbolic background. Choose finite sets of **smeared, conserved, relationally defined** input/source modes and output/geometry modes.

Input operator vector:

\[
\hat{\mathbf X}=(\hat X_1,\ldots,\hat X_n)^T,
\]

where each `X_a` is a calibrated source observable constructed from a renormalized/smeared stress-energy perturbation or a linearized matter quadrature that generates it in the chosen operating point.

Output operator vector:

\[
\hat{\mathbf Y}=(\hat Y_1,\ldots,\hat Y_m)^T,
\]

where each `Y_i` is a relational geometry readout: for example a clock phase, smeared curvature response, differential acceleration, or another gauge-completed weak-field observable.

The Gaussian approximation is claimed only when the selected mode sector is closed to the declared perturbative order and higher cumulants are negligible or separately bounded.

## 2. State and commutator data — QG-001

For the linearized mode sector define first moments and centered covariance matrices

\[
\mathbf d_X=\langle\hat{\mathbf X}\rangle,
\qquad
V_X=\frac12\langle\{\Delta\hat{\mathbf X},\Delta\hat{\mathbf X}^T\}\rangle,
\]

and similarly for `Y`.

Define the commutator matrices in the calibrated operating sector,

\[
[\hat X_a,\hat X_b]=i\hbar(\Omega_X)_{ab},
\qquad
[\hat Y_i,\hat Y_j]=i\hbar(\Omega_Y)_{ij},
\]

where a c-number commutator description is an approximation that must be justified for the chosen finite mode basis.

If the stress-energy modes do not admit this closure, the Gaussian branch is BLOCKED for that sector rather than silently replacing their algebra.

## 3. Primary dynamics as a causal Gaussian channel — QG-002

The fundamental v0.1 map is

\[
\mathcal E_G:\rho_X\mapsto\rho_Y,
\]

with first and second moments

\[
\boxed{\mathbf d_Y=K\,\mathbf d_X+\mathbf d_0}
\]

and

\[
\boxed{V_Y=K V_X K^T+Y_G}.
\]

`K` is the gravity transfer matrix/kernel and `Y_G=Y_G^T\ge0` is the gravity-interface added-noise covariance.

The offset `d_0` is fixed by the declared background and calibration convention; it is not a signal parameter.

## 4. GR fixes the mean transfer

The mean channel is **not** freely fitted. In the weak-field domain `K` is the projection of the retarded Einstein response onto the chosen conserved source and relational detector modes.

Schematically,

\[
K=\mathcal P_Y\,\frac{\kappa}{2}G_R\,\mathcal S_X,
\]

where

- `S_X` embeds the calibrated input mode into the conserved stress-energy source sector;
- `G_R` is the retarded linearized gravitational Green operator with constraints treated consistently;
- `P_Y` projects to the relational output observable.

In the static nonrelativistic sector this transfer must reduce to

\[
\nabla^2\Phi=4\pi G\rho.
\]

Thus the model inherits the controlled GR/Newtonian mean limit rather than replacing it.

## 5. Complete-positivity constraint

For a bosonic Gaussian channel in the declared canonicalized mode coordinates, complete positivity requires

\[
\boxed{
Y_G+rac{i\hbar}{2}\left(\Omega_Y-K\Omega_XK^T\right)\ge0
}
\]

up to the frozen covariance/CCR normalization convention.

This inequality is not an optional fit. It is the quantum consistency condition relating transfer and added noise.

The model is rejected in a mode sector if no `Y_G` exists that simultaneously satisfies complete positivity, gauge/conservation constraints, causal structure and the declared symmetries.

## 6. Quantum-limited closure postulate

The RQIR-native hypothesis is:

> **QLC postulate:** in the absence of an identified additional gravitational environment or unresolved sector, the interface adds no noise beyond the minimum required by complete positivity and the frozen symmetries.

Operationally, after bringing each admissible mode block to a canonical/symplectic normal form, choose the CP-saturating added noise in that block.

This is a **minimum-noise principle**, not a fitted free noise function.

The exact covariant construction of the normal-mode decomposition is a mandatory derivation target. If CP saturation is nonunique in a block, the degeneracy is retained explicitly; a preferred solution may not be selected by detector performance.

## 7. RQIR hierarchy induced by the channel

In the Gaussian sector:

- first moments of source modes map through `K`;
- symmetrized covariance maps through `K V_X K^T + Y_G`;
- ordered/commutator information is constrained jointly by `Omega_X`, `Omega_Y`, `K` and the CP condition;
- retarded response is carried by the causal part of `K`;
- Q4 information transmission is determined by the channel's ability to preserve/transmit quantum correlations;
- Q5 geometry fluctuations are separated into transferred source covariance and irreducible interface noise `Y_G`.

Thus mean, noise, response and channel capacity are not independent phenomenological knobs.

## 8. Classical and decoupling limits

### Classical limit

When the physical commutator scales vanish with `hbar -> 0`, the CP lower bound on quantum added noise vanishes. The model tends toward the deterministic/stochastic classical GR transfer allowed by the remaining classical covariance.

### Gravity-off limit

The physical gravitational transfer satisfies `K -> 0` as `G -> 0`. A valid physical normalization must also make the gravity-interface commutator/noise sector vanish in this limit; otherwise QG-006 fails.

### Newtonian limit

The first-moment transfer must reproduce the Poisson response in the static nonrelativistic sector.

## 9. Gauge and conservation construction rule

The finite mode maps are defined only on the conserved/gauge-admissible quotient:

- source smearing tensors/functions must respect the applicable conservation/Ward identities;
- output modes must be relational or gauge-completed;
- coordinate-only metric components are not detector observables;
- `K` is evaluated on the physical quotient, not on arbitrary gauge directions.

A gauge direction that changes `K` or the CP floor after physical projection is a model inconsistency.

## 10. Causality

`K(t,t')` is retarded:

\[
K(t,t')=0\qquad\text{for }t'<\text{outside the causal past of }t.
\]

Noise correlations may be nonlocal as quantum correlations, but they may not enable operational signalling outside the declared causal structure. This must be certified at channel level.

## 11. First possible discriminator

Unlike `ANSATZ-RQIR-MIN`, this branch has a candidate-specific structural relation:

\[
\boxed{
Y_G=Y_{\rm CP,min}[K,\Omega_X,\Omega_Y]
}
\]

in each uniquely canonicalizable physical mode block.

This links the measurable added-noise floor to the independently calibrated causal gravitational transfer.

The first discriminator is therefore **not** 'nonzero noise'. It is the joint relation among:

1. calibrated mean/retarded transfer `K`;
2. source commutator structure `Omega_X`;
3. output commutator structure `Omega_Y`;
4. irreducible geometry-channel covariance `Y_G`.

A classical/stochastic/hybrid model may match one or several of these objects. The RQIR test is whether it can reproduce the **joint CP-saturating relation in the same operational mode basis**.

## 12. Comparator expectations

No DISTINCT state is assigned yet.

- C0: likely distinct only if a quantum noise/correlation floor is operationally resolved.
- C1: may differ because the channel retains second-order/commutator information.
- C2: stochastic models can reproduce covariance, so response/commutator/channel tests are mandatory.
- C3: measurement-feedback/classical-channel constructions are major competitors; CP alone does not exclude them.
- C4: ordinary quantum mediator/technical channels must be included apparatus-specifically.
- C5: crucial comparator. Standard perturbative quantum gravity may realize exactly the same quantum-limited Gaussian channel in some regimes. If so, the model is an operational reformulation, not a new theory.
- C6: quantum source statistics plus classical transfer may mimic `K V_X K^T`; the irreducible `Y_G` and channel structure must carry the distinction.

## 13. Falsification / rejection conditions

Reject v0.1 in a claimed mode sector if:

- the source/output mode algebra cannot be consistently canonicalized to the working order;
- no CP-compatible `Y_G` exists with the required causal/gauge symmetries;
- the minimum-noise prescription is nonunique in a way that affects predictions and no RQIR-internal principle removes the degeneracy;
- the Newtonian/GR mean transfer fails;
- the `G -> 0` or `hbar -> 0` limits leave an unphysical residual gravity noise floor;
- the channel enables signalling outside the declared causal structure;
- predicted observables depend on gauge directions;
- the candidate-specific relation is exactly reproduced by C5 and no further RQIR observable distinguishes the models.

The last case rejects **novelty**, not necessarily the operational channel representation.

## 14. Immediate derivation targets

1. Construct a one-mode or two-mode canonical toy sector with a conserved source preparation and relational output.
2. Compute `K` from the same weak-field GR normalization already certified in the root model.
3. Solve the Gaussian CP inequality and obtain the quantum-limited `Y_G` analytically.
4. Check `G -> 0`, `hbar -> 0`, positivity and causal support.
5. Derive the entanglement-breaking threshold and compare it with the quantum-limited noise floor.
6. Compare the resulting channel with the C1/C2/C3/C5/C6 classes without using polygon-QGR information.
7. Promote only if QG-001/QG-002 and the relevant cross-gates receive repository evidence.
