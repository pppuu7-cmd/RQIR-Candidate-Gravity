# Iter020B / G38-C terminal result

Authoritative run `34704210632`, head `86eb78312d1cdcf58c4844e98b4065482b9fc4c8`, aggregate job `103581251810`, summary artifact `10300863359`, digest `sha256:bd16f6d2fb356285d29725b2275fe3f1ca93b4bbb8287c2815e52a755f12cf2f`.

All 12 prospectively frozen three-time OU trajectory positive-control lanes were structurally valid and scientifically supported under the frozen `max_t trace distance < 0.002` rule at observation times `T=[0.25,0.5,1.0]`.

- Sobol-LSQ: 6/6 PASS; worst maximum per-time trace-distance recovery `1.4952140765689448e-13`.
- LHS-LSQ: 6/6 PASS; worst maximum per-time trace-distance recovery `2.3292762004080123e-14`.

The six hidden controls included interior trajectories plus prospectively fixed short- and long-correlation controls. Hidden source coordinates were not optimizer starts.

Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_OU_COLORED_TRAJECTORY`.

This closes optimizer calibration for the finite three-time OU colored-classical-noise trajectory family and authorizes a separate prospective RCG-002 multi-time adversarial gate. It does not itself establish information-backflow non-Markovianity, new physics, or a general classical/semiclassical no-go.