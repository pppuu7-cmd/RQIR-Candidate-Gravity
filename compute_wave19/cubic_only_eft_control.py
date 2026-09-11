from common import write_result

# Degree-counting control for a cubic-curvature EFT direction around a flat/weak-field background.
# If Riemann = R1[h] + R2[h,h] + ..., then a local invariant schematically Riemann^3 starts at O(h^3).
# Hence its second variation at h=0 vanishes, while its third variation is generically nonzero.
orders={
 'Einstein-Hilbert_quadratic':'O(h^2)',
 'Einstein-Hilbert_cubic':'O(h^3)',
 'Riemann_cubed_leading':'O(h^3)',
 'Riemann_cubed_second_variation_at_h0':'0',
 'Riemann_cubed_third_variation_at_h0':'generically nonzero'
}
out={
 'test':'C5/EFT cubic-only comparator direction by perturbative degree counting',
 'orders':orders,
 'two_point_propagator_changed_at_leading_flat_background_order':False,
 'three_graviton_vertex_changed':True,
 'cubic_only_direction_exists_in_EFT_proxy':True,
 'conclusion':'A curvature-cubed EFT operator supplies a concrete cross-order degeneracy: around a flat background it can modify the three-graviton interaction while leaving the quadratic/two-point kernel unchanged at leading order. Therefore no two-point-only selector can uniquely determine the full higher-point dynamics without extra assumptions.'
}
write_result('cubic_only_eft_control',out)
