# RQIRCG automation runtime incident — 2026-09-14

Status: operational diagnosis; not scientific authority.

## Symptom

Several recurring research automations across multiple independent projects ran on schedule, produced no durable scientific GitHub result, then became disabled roughly one minute after `last_run_time`.

For RQIRCG specifically:

| Automation | last_run_time UTC | metadata update/disable UTC | elapsed |
|---|---:|---:|---:|
| Independent Constructor | 2026-09-14 16:01:56.772859 | 16:03:02.338841 | 65.6 s |
| Selector Auditor | 2026-09-14 15:30:51.118793 | 15:31:56.989400 | 65.9 s |
| Selector Auditor | 2026-09-14 16:31:29.115002 | 16:32:32.353665 | 63.2 s |
| Independent Constructor | 2026-09-14 17:00:39.218632 | 17:01:46.012883 | 66.8 s |

The same approximately one-minute failure/disable pattern was independently visible in other long research automations (QGR and MSQGR), which strongly argues against an RQIRCG-specific equation, repository, or workflow defect.

## GitHub-side exclusion

At incident diagnosis time, RQIRCG `main` was already synchronized to terminal RSC1 at `bb9a15cd5953469078334e7ba211ee3b1ebc9844`.

The newest GitHub Actions run in the repository was still CM1 run `34861269613`, completed successfully at the earlier CM1 stage. No post-CM1 GitHub Actions workflow had been launched by the failing scheduled iterations.

The failing scheduled iterations also left no new RQIRCG commit at their run times. Therefore the repeated error occurs before a new GitHub Actions scientific workflow or durable scientific GitHub result is created.

## Best-supported root cause

The automation service does not expose the internal failure code or execution trace through the available task metadata, so an exact platform exception string cannot be recovered here.

However the observed evidence supports, with high confidence, an execution-budget/runtime failure around the one-minute boundary:

1. independent recurring tasks in several projects fail on the same approximately 63–67 second timescale;
2. after the failed run they become disabled automatically;
3. no corresponding GitHub Actions failure exists;
4. the original automation prompts demanded a very large state reconstruction, historical scans, multiple connector calls, artifact/provenance checks, one complete scientific gate, several GitHub writes and a final durable handoff in a single scheduled run;
5. this workload is materially larger than a one-minute bounded automation turn.

Thus the operational failure is best classified as:

`AUTOMATION_EXECUTION_BUDGET_EXCEEDED_OR_EQUIVALENT_PLATFORM_TIMEOUT_HIGH_CONFIDENCE`

and not as a scientific FAIL.

## Control-only repair

No scientific hypothesis, object, PASS/FAIL/BLOCKED criterion, interpretation ceiling, candidate coefficient, source direction, or claim lock was changed.

Both RQIRCG scheduled prompts were shortened and converted to **bounded micro-iterations**:

- read only current recovery, newest terminal/progress result, recent commits/actions and the latest peer handoff;
- do not re-scan historical bootstrap/G92 material once recovery supersedes it;
- perform at most one small independent subproblem or one bounded review per run;
- persist a prereg/progress/handoff early rather than attempting an entire multi-lane gate;
- avoid old artifact downloads and new Actions workflows unless the current exact subproblem requires them;
- never disable the automation or change its schedule;
- preserve all scientific firewalls and claim locks.

Both recurring RQIRCG automations were re-enabled after this repair.

## Confirmation criterion

The repair is operationally confirmed only if subsequent scheduled runs:

1. remain enabled after execution;
2. leave a durable bounded progress/result commit or explicit no-result handoff when warranted;
3. do not reproduce the approximately one-minute disable pattern.

If the approximately one-minute disable pattern persists even with the bounded prompt, the next diagnosis should focus on platform/connector latency or a lower fixed automation runtime cap rather than scientific code.

## Scientific-state firewall

This incident note has no scientific authority. Current scientific authority remains `recovery/CURRENT_FRONT.md` and terminal result notes. The RSC scientific frontier remains `RSC_SOURCE_STRESS_EQUIVALENCE_PREREQUISITE_FRONTIER` until a prospectively valid successor gate changes it.