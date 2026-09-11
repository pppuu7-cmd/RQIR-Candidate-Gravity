# Foundational Derivation 001 — one-mode complete-positivity floor

**Model:** `ANSATZ-RQIR-QLC` v0.1  
**Purpose:** solve the model's quantum-limited closure exactly in the simplest canonical physical mode block before any comparator claim.

## 1. Canonicalized one-mode block

After physical projection, calibration and symplectic normalization, take one input mode and one output mode with quadrature vectors

\[
\hat{\mathbf X}=(\hat q_X,\hat p_X)^T,
\qquad
\hat{\mathbf Y}=(\hat q_Y,\hat p_Y)^T,
\]

and normalized commutator matrix

\[
\Omega=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
[\hat q,\hat p]=i\hbar.
\]

This canonicalized block is a mathematical normal form. Physical gravity scaling is restored by the source/output mode normalization and the GR transfer map; `eta` below is not identified directly with `G`.

## 2. Phase-insensitive transfer block

Take the simplest symplectic singular block

\[
K=\sqrt{\eta}\,I_2,
\qquad \eta\ge0,
\]

and an isotropic added-noise matrix

\[
Y_G=y I_2,
\qquad y\ge0.
\]

The moment map is

\[
\mathbf d_Y=\sqrt{\eta}\,\mathbf d_X,
\]

\[
V_Y=\eta V_X+y I_2.
\]

## 3. Complete-positivity inequality

For the covariance convention

\[
V_{ij}=\frac12\langle\{\Delta R_i,\Delta R_j\}\rangle,
\]

complete positivity requires

\[
Y_G+rac{i\hbar}{2}\left(\Omega-K\Omega K^T\right)\ge0.
\]

Since

\[
K\Omega K^T=\eta\Omega,
\]

we obtain

\[
M_{CP}
=
yI_2+rac{i\hbar}{2}(1-\eta)\Omega.
\]

The two eigenvalues are

\[
\lambda_\pm
=
y\pm\frac{\hbar}{2}(1-\eta).
\]

Positivity of both eigenvalues is therefore equivalent to

\[
\boxed{
y\ge\frac{\hbar}{2}|1-\eta|
}.
\]

## 4. QLC prediction in the normalized block

The quantum-limited postulate chooses the saturation value

\[
\boxed{
y_*\equiv\frac{\hbar}{2}|1-\eta|
}.
\]

Thus transfer and irreducible added noise are not independent parameters.

For an attenuating block `0 <= eta <= 1`,

\[
y_* = \frac{\hbar}{2}(1-\eta).
\]

For an amplifying block `eta >= 1`,

\[
y_* = \frac{\hbar}{2}(\eta-1).
\]

At `eta=1`, the block is symplectic/noiseless in this normal form and the CP floor vanishes.

## 5. General unequal commutator scales

Physical source and geometry modes need not have the same commutator normalization. Let

\[
\Omega_X=\omega_X\Omega,
\qquad
\Omega_Y=\omega_Y\Omega,
\]

and take `K=k I_2` in that physical block. Then

\[
K\Omega_XK^T=k^2\omega_X\Omega,
\]

so an isotropic physical added-noise matrix `Y=yI` must satisfy

\[
\boxed{
y\ge\frac{\hbar}{2}|\omega_Y-k^2\omega_X|
}.
\]

The QLC saturation prediction is

\[
\boxed{
y_*^{\rm phys}=\frac{\hbar}{2}|\omega_Y-k^2\omega_X|}.
\]

This form is more useful for gravity because `omega_Y`, `omega_X` and `k` carry the physical mode normalization and can scale with `G`, geometry and detector coupling.

## 6. Gravity-off consistency condition

RQIR does not permit an unexplained gravity-induced residual when `G -> 0`.

The physical mode construction must therefore satisfy

\[
\Delta y_*^{\rm phys}(G)\to0
\qquad\text{as}\qquad G\to0,
\]

where `Delta y` is the gravity-attributed residual after the explicitly declared output/detector baseline is removed.

This can occur, for example, when the physical geometry commutator scale and gravitational transfer both vanish with the appropriate powers of `G`. The actual scaling must be derived from the relational output chosen for the first apparatus-independent toy realization.

Failure of this limit rejects that realization of QLC.

## 7. Classical limit

Because the CP floor is proportional to `hbar`,

\[
\boxed{y_*\to0\quad\text{as}\quad\hbar\to0}
\]

in physical coordinates with fixed classical transfer data. This is exactly the behavior required of a purely quantum minimum-noise contribution.

## 8. Information consequence

The one-mode relation already shows why 'nonzero noise' is not the discriminator. The candidate prediction is the **closure relation**

\[
y-y_* = 0
\]

within the ideal QLC model, after calibrated baseline subtraction and transformation to the declared physical mode basis.

An experiment or comparator must therefore reproduce simultaneously:

- the transfer/gain block;
- the input commutator normalization;
- the output commutator normalization;
- the residual added covariance;
- the same causal/gauge constraints.

A stochastic model matching only `y` does not automatically match the closure relation.

## 9. What has passed

Within this canonical toy block:

- the CP inequality is solved analytically;
- a unique isotropic CP-saturating noise floor exists;
- the floor vanishes in the formal classical `hbar -> 0` limit;
- the model produces a quantitative transfer/noise relation rather than independent knobs.

## 10. What remains blocked

- derive a conserved source mode and relational geometry output from the actual weak-field GR transfer;
- demonstrate the physical `G -> 0` residual scaling;
- extend beyond isotropic one-mode blocks;
- treat non-Gaussian higher cumulants;
- prove causal channel composition;
- compare the closure relation to C2/C3/C5/C6;
- determine whether C5 already saturates exactly the same bound.

## 11. Decision

The simplest QLC block is mathematically viable at the complete-positivity level. The branch survives to the next derivation stage. No claim of new quantum gravity is made until the physical GR mode map and C5 comparator audit are completed.
