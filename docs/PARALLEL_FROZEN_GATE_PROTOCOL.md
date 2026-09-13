# Parallel frozen-gate protocol

Status: **RESEARCH INFRASTRUCTURE / NO SCIENTIFIC CLAIM**
Updated: 2026-09-13

## Purpose
Run scientifically independent RQIR-CG gates concurrently without creating hidden cross-contamination, post-hoc selection, or false authority from green CI.

## Sibling-gate rule
Parallel gates may run concurrently only when all of the following are true:

1. They branch from the same already-terminal scientific base commit.
2. Each gate has its own prospectively frozen preregistration committed before implementation/results.
3. Each gate has separate implementation, workflow, run, raw lane artifacts and aggregate artifact.
4. No sibling gate may consume another sibling's result, artifact, classification, coefficient choice or desired conclusion before both are terminal.
5. A later synthesis may consume only terminal sibling results and is retrospective unless separately preregistered as a new gate.

## Per-gate authority chain
The canonical chain is:

`scientific base -> preregistration -> implementation -> production workflow head -> run -> raw lane artifacts -> frozen aggregate -> independent raw validation -> terminal result -> merge`

Record, where applicable:
- base SHA;
- preregistration SHA;
- implementation SHA;
- production head SHA;
- Actions run ID;
- job IDs;
- raw artifact IDs and SHA-256 digests;
- aggregate artifact ID and digest;
- frozen terminal classification;
- interpretation ceiling.

## CI is not scientific authority
A green workflow proves only that the workflow executed successfully. Scientific classification requires:

1. raw lane artifacts are present;
2. lane classifications and frozen predicates match preregistration;
3. controls behave as prospectively specified;
4. aggregate consumes the intended lanes and applies the frozen rule;
5. terminal result is written only after those checks.

Unexpected scientific outcomes are retained as FAIL/BLOCKED when required by the frozen rule. Criteria are never weakened to recover a preferred result.

## Infrastructure recovery
Infrastructure-only failures may be repaired without changing frozen science. The recovery must:
- identify the infrastructure-only defect explicitly;
- change only the minimum technical surface required;
- preserve preregistered scientific predicates, panels, controls and aggregate rule;
- record the recovery launch/production authority separately.

## Concurrency policy
Prefer parallelism where scientific dependencies permit it.

- A single gate should normally use independent matrix lanes for prospectively frozen subtests.
- Distinct sibling questions should use separate branches/workflows.
- Do not create extra workflows merely to occupy runners; GitHub runner queueing can make excessive fan-out slower rather than faster.
- When runner availability is constrained, prioritize the highest-information sibling gates and perform artifact validation, synthesis preparation and repository bookkeeping while queued jobs execute.

## Merge discipline
Sibling branches merge to `main` only after their own terminal classifications are established. Merge order must not change their scientific interpretation because sibling gates are required to be result-independent.

If branch divergence creates a code conflict, preserve each sibling's unique prereg/implementation/results history rather than silently rewriting one gate against another sibling's result.

## Readiness discipline
Structural, robustness, identifiability or blocker-resolution gates do not automatically increase programme readiness. A readiness change requires its own documented criterion. `THEORY_ESTABLISHED` never follows from CI status, rank recovery, numerical robustness, or existence of a construction witness.

## Current demonstrated use
This protocol has already been exercised by parallel sibling families including G76–G79, G80/G81, G82/G83, G84/G85, G86/G87, G88/G89 and the active G90/G91 covariant-lift pair.
