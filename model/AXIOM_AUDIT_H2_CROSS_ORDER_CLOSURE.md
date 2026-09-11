# Axiom Audit H2 — can Ward/positivity/causality close higher orders?

**Candidate:** H2 from `NEXT_AXIOM_SEARCH.md`  
**Question:** do frozen RQIR consistency conditions uniquely determine `W^(n>=3)` from the lower source hierarchy?  
**Result:** NOT RQIR-FORCED in general.

## 1. Effective-action hierarchy

Let the physical effective/influence object generate connected vertices/cumulants

\[
W=W^{(1)}+W^{(2)}+W^{(3)}+\cdots.
\]

Diffeomorphism invariance implies Ward/Bianchi identities. In momentum-space perturbation theory these constrain contractions of higher vertices with gauge momenta; schematically,

\[
k_\mu\Gamma^{\mu\nu;\alpha\beta;\cdots}
=\text{lower-order/contact structures}.
\]

The exact identity depends on fields, background, gauge convention and contact terms.

## 2. Why Ward identities do not uniquely determine the vertex

Ward identities fix consistency/longitudinal pieces but generally leave transverse, gauge-invariant form factors unconstrained.

If `Gamma_part` is one solution of a Ward identity, then

\[
\Gamma=\Gamma_{part}+\Gamma_T,
\]

with

\[
k\cdot\Gamma_T=0,
\]

is another solution whenever `Gamma_T` respects the remaining symmetries and power counting.

Thus gauge consistency restricts higher-order freedom without removing it.

## 3. Positivity does not supply numerical closure

Positivity/unitarity/CP impose inequalities and spectral relations on admissible correlators and channels. They exclude regions of function space but normally do not assign a unique allowed higher cumulant.

At second order this was already explicit: the Gaussian CP inequality defines a feasible set, and even its saturation was not gravity-specific.

At higher orders the same logical problem remains: consistency bounds are not automatically dynamical equations fixing all amplitudes.

## 4. Causality does not supply numerical closure

Retarded support and microcausal/process constraints restrict where response kernels may have support and how interventions may influence one another.

They do not generally fix the magnitude and detailed spectral dependence of every causal higher-order response vertex.

Many distinct causal interacting quantum theories satisfy the same support rules.

## 5. EFT power counting does not uniquely fix Wilson coefficients

Low-energy EFT determines the allowed operator basis and scaling hierarchy. Symmetry can fix some structures and universal nonanalytic pieces, but local higher-order Wilson coefficients encode UV/matching information unless independently measured or derived.

Therefore an RQIR-compatible EFT still contains physically meaningful higher-order freedom consistent with all frozen gates.

## 6. Combined constraints

Intersecting Ward identities, positivity, causality and EFT power counting can dramatically shrink the candidate space,

\[
\mathcal S_{higher}
=\mathcal S_{Ward}\cap\mathcal S_{positive}\cap\mathcal S_{causal}\cap\mathcal S_{EFT},
\]

but frozen RQIR provides no general proof that this intersection is a singleton.

The already known C5 representative demonstrates at least one admissible solution; modified EFT coefficients or different microscopic completions can supply additional solutions while preserving the same low-order operational data in a finite domain.

## 7. Result

\[
\boxed{
(J,N,D,\chi^R)+\text{Ward} +\text{positivity}+\text{causality}+\text{EFT}
\not\Rightarrow
\text{unique }W^{(n\ge3)}
}
\]

in the general reconstruction problem.

H2 is therefore not currently `RQIR-FORCED`. A proposed universal cross-order closure would be an `EXTRA-HYPOTHESIS` unless proved in a more restrictive physical sector.

## 8. Remaining legitimate route

A sector-specific uniqueness theorem could still exist after adding physical assumptions not contained in the generic RQIR methodology (for example a precisely declared field content, derivative order, state and asymptotic conditions). If such assumptions are imposed, any resulting uniqueness must be attributed to the full assumption set, not to RQIR alone.

## 9. Decision

Do not invent `F_3,F_4,...` to complete QLC. The independent funnel has reached genuine microscopic underdetermination. The next model requires an explicitly named physical hypothesis with independent motivation and a falsifiable departure from the C5-like root.
