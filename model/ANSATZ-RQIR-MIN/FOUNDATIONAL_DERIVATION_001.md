# Foundational Derivation 001 — weak-field dynamics and Newtonian gate

**Model:** `ANSATZ-RQIR-MIN` v0.1  
**Purpose:** derive the first consequences of the frozen single-dynamics ansatz before any discriminator search.

## 1. Conventions

Use signature `(-,+,+,+)` and

\[
\kappa^2=32\pi G,
\qquad
c=1,
\]

with `hbar` kept conceptually explicit in quantum correlators.

For the local weak-field check take a Minkowski reference background and vanishing background cosmological constant,

\[
g_{\mu\nu}=\eta_{\mu\nu}+\kappa h_{\mu\nu}.
\]

Define the trace-reversed perturbation

\[
\bar h_{\mu\nu}=h_{\mu\nu}-\frac12\eta_{\mu\nu}h.
\]

## 2. Linearized field equation

The Einstein-Hilbert normalization in `MODEL.md` gives

\[
G_{\mu\nu}=8\pi G\,T_{\mu\nu}
=\frac{\kappa^2}{4}T_{\mu\nu}.
\]

Because the physical metric perturbation is `kappa h`, the linearized Einstein tensor in de Donder gauge,

\[
\partial^\mu\bar h_{\mu\nu}=0,
\]

obeys

\[
G^{(1)}_{\mu\nu}[\kappa h]
=-\frac{\kappa}{2}\Box\bar h_{\mu\nu}.
\]

Therefore

\[
-\frac{\kappa}{2}\Box\bar h_{\mu\nu}
=\frac{\kappa^2}{4}T_{\mu\nu},
\]

or

\[
\boxed{
\Box\bar h_{\mu\nu}
=-\frac{\kappa}{2}T_{\mu\nu}
}
\]

at the leading weak-field order.

This normalization is consistent with the leading interaction

\[
S_{\rm int}=-\frac{\kappa}{2}\int d^4x\,h_{\mu\nu}T^{\mu\nu}.
\]

## 3. Conservation / Ward compatibility at linear order

Taking the divergence of the field equation gives

\[
\partial^\mu\Box\bar h_{\mu\nu}
=-\frac{\kappa}{2}\partial^\mu T_{\mu\nu}.
\]

The de Donder condition makes the left-hand side vanish, hence consistency requires

\[
\boxed{\partial^\mu T_{\mu\nu}=0}
\]

for the flat-background leading-order source. The curved-background completion is the corresponding covariant Ward/conservation statement and remains to be checked at the chosen EFT order.

This is an important RQIR constraint: arbitrary detector/source kernels that violate source conservation cannot be inserted into the model.

## 4. Retarded solution

Define the retarded Green object by the convention

\[
\Box G_R(x,y)=-\delta^{(4)}(x-y),
\qquad
G_R(x,y)=0\;\text{when }x\text{ is outside the causal future of }y.
\]

Then

\[
\boxed{
\bar h_{\mu\nu}(x)
=\frac{\kappa}{2}
\int d^4y\,G_R(x,y)T_{\mu\nu}(y)
}
\]

for the sourced part, plus a homogeneous solution.

At the operator level the same structural equation yields the model's leading response map from quantum source operators to the gravitational field operator.

## 5. Newtonian limit

For a static nonrelativistic source,

\[
T_{00}\simeq\rho,
\qquad
T_{0i},T_{ij}\ll T_{00}.
\]

The physical weak-field metric is written

\[
g_{00}\simeq-(1+2\Phi),
\qquad
g_{ij}\simeq(1-2\Phi)\delta_{ij}.
\]

Since `g=eta+kappa h`, this gives

\[
\kappa h_{00}=-2\Phi,
\qquad
\kappa h_{ij}=-2\Phi\delta_{ij}.
\]

The physical trace is

\[
\kappa h=-4\Phi,
\]

and hence

\[
\kappa\bar h_{00}=-4\Phi.
\]

The static `00` field equation is

\[
\nabla^2\bar h_{00}
=-\frac{\kappa}{2}\rho.
\]

Multiplying by `kappa` and using `kappa^2=32 pi G`,

\[
-4\nabla^2\Phi
=-\frac{\kappa^2}{2}\rho
=-16\pi G\rho.
\]

Therefore

\[
\boxed{
\nabla^2\Phi=4\pi G\rho
}
\]

with the correct Newtonian normalization.

**Result:** the Newtonian sub-gate of QG-003 passes at the declared leading weak-field order.

## 6. Gravity-off limit

Because the interaction is proportional to `kappa ~ sqrt(G)`,

\[
G\to0\quad\Rightarrow\quad S_{\rm int}\to0,
\]

so matter and perturbative gravitational excitations decouple at this order. This supplies the structural `G -> 0` limit; the full QG-006 package still requires the semiclassical/coarse-grained and flat-QFT checks.

## 7. CTP closure of response and fluctuations

The same linear coupling implies that integrating the gravitational mediator at Gaussian order produces a CTP influence structure of the schematic form

\[
S_{\rm IF}[T_+,T_-]
\sim
\frac{\kappa^2}{8}T^-\!\cdot G_R\!\cdot T^+
+
\frac{i\kappa^2}{16}T^-\!\cdot G_H\!\cdot T^-
+\cdots,
\]

where `T^- = T_+ - T_-`, `T^+` denotes the declared average/sum convention, `G_R` is the retarded gravitational propagator and `G_H` the symmetrized/Hadamard gravitational correlator. Exact factors depend on the final CTP sum/difference convention and will be frozen before quantitative use.

The structural consequence is already fixed:

> response and fluctuation kernels are projections of one mediator dynamics and cannot be independently tuned.

This is the first nontrivial RQIR-derived closure relation of the candidate.

## 8. What is and is not established

Established within this derivation and declared approximation:

- leading linearized equation and normalization;
- source-conservation compatibility at leading order;
- causal retarded solution structure;
- correct Newtonian Poisson limit;
- gravity-off decoupling structure;
- common-dynamics origin of response/noise at Gaussian CTP order.

Not yet established:

- full nonlinear GR limit at the truncated EFT order;
- complete BRST/constraint proof;
- relational Q1/Q5/Q6 observables;
- renormalized stress-tensor two-point implementation;
- positivity/unitarity certificate for the reduced detector channel;
- any novelty relative to C5 perturbative quantum gravity.

## 9. Decision

`ANSATZ-RQIR-MIN v0.1` survives its first foundational calculation. No new term is justified by this derivation. The next hard check is the exact C5 degeneracy/equivalence audit together with the gauge/relational completion.
