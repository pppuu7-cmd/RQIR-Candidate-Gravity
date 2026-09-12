# Iter017 / G35 — calibrated K=3/K=4 comparator terminal result

Date: 2026-09-12

Authoritative run: `34697766107`
Authoritative head: `fbc71768da3cec0d6ea5a8cbb755a29036b16726`
Aggregate job: `103578278887`
Aggregate artifact: `10301201162`
Aggregate artifact digest: `sha256:7e07e47311db7a279e2de47502d64a36cf31623c10c0da67f062ee8817bac199`

## Frozen gate

Fixed before result inspection:

- adversarial nonzero trace gap `> 1e-4`;
- Sobol-LSQ/LHS-LSQ agreement on every shard `<= 0.002`;
- nesting sanity: each K may not worsen the calibrated minimum relative to the immediately smaller-K frontier by more than `0.002`;
- physical admissibility: TP residual `<1e-10`, Choi minimum eigenvalue `>-1e-8`, state minimum eigenvalue `>-1e-8`, trace error `<1e-10`;
- trace distance remains the final distance authority;
- historical G30/G31 minima are excluded from authority.

## Raw aggregate classification

All 24 required artifacts were present and structurally valid.

### K=3

All four shards pass nonzero-gap, cross-method-agreement and nesting gates.

- shard 0: Sobol `0.02607083500239983`, LHS `0.02607082455460381`;
- shard 1: Sobol `0.10462705021070003`, LHS `0.1046280224077526`;
- shard 2: Sobol `0.4030775755359582`, LHS `0.4030776193040029`;
- shard 3: Sobol `0.5324536720244457`, LHS `0.5324529974645373`.

K=3 admissibility: 4/4 support.

### K=4

All four shards pass nonzero-gap, cross-method-agreement and nesting gates.

- shard 0: Sobol `0.026070843192707152`, LHS `0.026070840339822314`;
- shard 1: Sobol `0.1046282559394234`, LHS `0.10462763627815973`;
- shard 2: Sobol `0.40307761916005946`, LHS `0.40307752304763794`;
- shard 3: Sobol `0.5324520837003446`, LHS `0.5324521216247678`.

K=4 admissibility: 4/4 support.

## Scientific classification

`DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT`

The result is restricted to the finite additive independent single-axis Markovian measurement-feedback GKSL comparator family tested here. It is not a no-go theorem for general semiclassical gravity, general classical mediators, non-Markovian dynamics, correlated Kossakowski families, or quantum-gravity models.

The near-equality of K=2/K=3/K=4 calibrated minima is evidence that, for these four frozen target shards, adding more independent channels inside this specific family does not close the observed gap. It does not prove saturation in any larger family.

## Next authorized gate

G35 terminal closure authorizes calibration of the broader shared-correlated classical-noise comparator ingredient whose implementation/provenance was independently validated in Iter018A/G36-P. Adversarial RCG-002 use of that broader family is not authorized until its optimizer passes a prospective in-family positive-control calibration gate.
