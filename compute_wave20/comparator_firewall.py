from common import write_result

items=[
 {'structure':'independent higher-curvature Wilson coefficients in one low-energy gravitational EFT action','status':'C5_EFT_STANDARD','novelty_credit':False},
 {'structure':'EOM/field-redefinition quotient of redundant curvature operators','status':'STANDARD_EFT_BASIS_REDUCTION','novelty_credit':False},
 {'structure':'background/nonlinear diffeomorphism Ward identities','status':'STANDARD_GAUGE_CONSISTENCY','novelty_credit':False},
 {'structure':'dispersive/positivity bounds correlating R^3-like and higher-order coefficients','status':'KNOWN_GRAVITATIONAL_AMPLITUDE_EFT_CONSTRAINT','novelty_credit':False},
 {'structure':'higher-spin-gap suppression of anomalous graviton three-point couplings','status':'CEMZ_STYLE_UV_COMPLETION_CONSTRAINT','novelty_credit':False},
 {'structure':'minimum-complexity choice setting optional Wilson coefficients to zero','status':'MODEL_SELECTION_NOT_PHYSICAL_LAW','novelty_credit':False}
]
out={
 'test':'Wave 20 action-level comparator firewall',
 'items':items,
 'firewall_pass':all(not x['novelty_credit'] for x in items),
 'new_QG_requires':'an independently motivated action/generating principle that removes physical higher-order Wilson freedom and yields prospective C5-distinct observables, not merely basis reduction or simplicity selection',
 'conclusion':'Every structural ingredient tested in Wave 20 is standard EFT/gauge/amplitude infrastructure or a model-selection rule. A no-go for uniqueness may be scientifically substantive, but no surviving ingredient is itself a new quantum-gravity primitive.'
}
write_result('comparator_firewall',out)
