# ITER050 / G54-Q launch

Authorized only by the prior preregistration `protocol/ITER050_G54Q_FINITE_SIZE_CONTROLLED_PHASE_CHANNEL_PREREG.md`.

No frozen criterion is changed. Production is the eight-lane finite-size weak-field controlled-phase channel integration defined there.

Retry authority note: the initial production run failed before artifact publication because NumPy boolean scalars were not JSON-serializable. The repair converts only result scalars to builtin Python `bool`/`float` for serialization; target, parameters, thresholds, controls, interpretation rule, and numerical computation are unchanged.