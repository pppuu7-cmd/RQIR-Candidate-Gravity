# Iter056 / G58-B — initial production control-invalid authority record

Date: 2026-09-13

## Status

`CONTROL_IMPLEMENTATION_INVALID_STREAM_C_ADVANCED_SUPPORT_COVERAGE`

This record preserves initial production run `34750487200` without reclassifying it as a scientific PASS or FAIL.

Frozen preregistration commit: `99d984aadb25f849a15a250b94cdc895eaca798a`.
Implementation commit: `cf8bd95de3a2470209f32008353497c7ba837989`.
Initial workflow/head: `8ed8a2de3656867743eddfed27d53a60ef7b778e`.

Initial artifacts:
- A job `103706050408`; artifact `10316000025`; digest `sha256:71021fa3513d9ca379aec9c12a35eaed95392accb160f78610cf3b22f52396d1` — structural-valid PASS.
- B job `103706050339`; artifact `10315144425`; digest `sha256:38cac4acdb92635af5b6a44c95151bceca2898c11b20f32b3b672765940ce256` — structural-valid PASS.
- C job `103706050365`; artifact `10315965029`; digest `sha256:68f54ce1a1e5940d75af3791cde699eb9c4b26fef5f37bd685b508f9501a0cfe` — structural-valid computation but invalid negative-control coverage for terminal science classification.
- D job `103706050320`; artifact `10315438697`; digest `sha256:aaf281017b635fcbeb7f9b1fe4c7cf7d91930cba8f6592539102c97198870a80` — structural-valid PASS; baseline equivalence supported on the frozen panel.
- E job `103706050210`; artifact `10315538380`; digest `sha256:34503cb13f0d2676a5bedd2e9d55849ae79a81bd47cee1869b3e0361422c6d9d` — structural-valid PASS.
- aggregate job `103706077600`; artifact `10315164272`; digest `sha256:c1286ff1e84ec9f1bf4bbb63046309d680cafa0824cfed8cedb0ef504ef287b8`.

## First causal failure

Stream C preregistered an intentionally advanced control `S(t+r)/r` and required it to be nonzero for at least one pre-arrival sample in at least 5/6 radii. The implementation used only nonnegative pre-arrival sample times. For frozen pulse support `0 < t < 1`, at radii `r=1.1` and `r=1.4` this makes every sampled advanced argument `t+r > 1`, outside the source support. Thus the advanced negative control is structurally incapable of firing in those two lanes even though the advanced kernel itself has pre-arrival support at negative observation times.

Observed Stream C: retarded pre-arrival maximum exactly 0 in all 6 lanes; post-arrival positive in all 6; advanced control nonzero in 4/6 only. The aggregate therefore emitted `G58B_LINEARIZED_BASELINE_CONSISTENCY_RULE_NOT_MET`, but that aggregate label is not accepted as a scientific FAIL because the first causal failure is the control-support implementation.

## Repair authority

Only the Stream-C sample grid may be repaired so that each frozen radius includes a pre-arrival time whose advanced argument lies strictly inside `(0,1)`. The pulse, radii, retarded/advanced formulas, `>=5/6` requirement, `1e-14` threshold, all A/B/D/E science, and all interpretation locks remain unchanged.

A control-only C retry is required. Do not rerun A/B/D/E.