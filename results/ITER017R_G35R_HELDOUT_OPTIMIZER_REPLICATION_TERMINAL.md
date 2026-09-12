# Iter017R / G35-R terminal result

Authoritative run `34702384573`, head `1b93cbf14b4705ae2699f559523d1c1b1ae28be5`, aggregate job `103580063685`, summary artifact `10300682102`, digest `sha256:5724519f32faf1e10d011e97d10df283fa6225facdfdb9ad8b14e82577557b13`.

All 18 prospectively frozen held-out calibration lanes were structurally valid. For K=2, K=3 and K=4, both independently calibrated Sobol-LSQ and LHS-LSQ methods recovered all three new hidden in-family controls below the frozen trace-distance tolerance `0.002`.

Worst trace-distance recovery gaps:
- K=2 Sobol `5.6435139378164e-13`, LHS `4.520086887540224e-14`;
- K=3 Sobol `2.1159550194748266e-13`, LHS `2.9192245626619504e-13`;
- K=4 Sobol `2.798500520542598e-15`, LHS `6.158500954656669e-15`.

Classification: `HELDOUT_OPTIMIZER_ROBUSTNESS_PASS_K2_K3_K4`.

This is methodology robustness only. It strengthens confidence that the calibrated optimizer construction is not tied to the original four controls, but it cannot by itself promote or veto the G35 adversarial physics result.