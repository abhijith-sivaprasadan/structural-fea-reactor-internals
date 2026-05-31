# LC1-LC2-LC3-LC4-LC4R Verification-Style Report

## Project

ASME-aware structural FEM study of a simplified reactor-internal support component.

This report summarizes the LC1, LC2, LC3, LC4 and LC4R load cases for a non-proprietary educational portfolio model. It is not an ASME BPVC-compliant design calculation and is not a certified nuclear component assessment.

## Model Description

The analyzed component is a simplified stainless-steel support plate with a raised central guide collar, central through-bore, four mounting bosses, counterbored mounting holes, radial stiffening ribs and filleted load-transfer features.

Reference files:
- Geometry notes: `../geometry/geometry_notes.md`
- STEP geometry: `../geometry/simplified_reactor_support_improved.step`
- Assumptions and limitations: `../docs/assumptions_and_limitations.md`

## Load Case Definition

| Item | Value |
|---|---|
| Load cases | LC1, LC2, LC3, LC4 and LC4R |
| Analysis type | Static structural |
| Applied loads | LC1: 2,000 N lateral; LC2: 5,000 N lateral; LC3: 3,000 N lateral + 2,000 N vertical; LC4/LC4R: +100 C uniform body temperature |
| Support condition | Fixed support on mounting-hole cylindrical faces |
| Material | Stainless steel 316, annealed, from ANSYS GRANTA sample data |
| Units | mm, N, MPa |
| Mesh type | Patch conforming tetrahedral mesh |

## Evidence Reviewed

Screenshots:
- `../ansys/screenshots/02_geometry_improved_isometric.png`
- `../ansys/screenshots/03_mesh_course.png`
- `../ansys/screenshots/04_mesh_medium.png`
- `../ansys/screenshots/05_mesh_fine.png`
- `../ansys/screenshots/06_lc1_deformation_fine.png`
- `../ansys/screenshots/07_lc1_principal_stress_fine.png`
- `../ansys/screenshots/08_lc1_von_mises_fine.png`
- `../ansys/screenshots/09_lc1_hotspot_backside_mounting_hole.png`
- `../ansys/screenshots/10_mesh_very_fine.png`
- `../ansys/screenshots/lc2_fine_total_deformation.png`
- `../ansys/screenshots/lc2_fine_von_mises.png`
- `../ansys/screenshots/lc2_fine_max_principal.png`
- `../ansys/screenshots/lc2_fine_reaction_force.png`
- `../ansys/screenshots/lc3_fine_total_deformation.png`
- `../ansys/screenshots/lc3_fine_von_mises.png`
- `../ansys/screenshots/lc3_fine_max_principal.png`
- `../ansys/screenshots/lc3_fine_reaction_force.png`
- `../ansys/screenshots/lc4_fine_total_deformation.png`
- `../ansys/screenshots/lc4_fine_von_mises.png`
- `../ansys/screenshots/lc4_fine_max_principal_stress.png`
- `../ansys/screenshots/lc4_fine_reaction_force.png`
- `../ansys/screenshots/lc4r_fine_total_deformation.png`
- `../ansys/screenshots/lc4r_fine_von_mises.png`
- `../ansys/screenshots/lc4r_fine_principal_stress.png`

Data and generated outputs:
- Raw convergence data: `../ansys/exported_results/mesh_convergence_raw.csv`
- Processed convergence table: `../results/lc1_mesh_convergence_summary.csv`
- Markdown convergence table: `../results/lc1_mesh_convergence_summary.md`
- Deformation convergence plot: `../results/lc1_deformation_convergence.png`
- Von Mises convergence plot: `../results/lc1_von_mises_convergence.png`
- Principal stress convergence plot: `../results/lc1_principal_stress_convergence.png`
- Normalized convergence plot: `../results/lc1_normalized_convergence.png`
- Load case summary: `../results/load_case_summary.md`
- LC2 linear scaling check: `../results/lc2_linear_scaling_check.md`
- Load case force balance: `../results/load_case_force_balance.md`

## Mesh Convergence Summary

| Mesh level | Global size [mm] | Nodes | Elements | Max deformation [mm] | Max von Mises [MPa] | Max principal [MPa] | Reaction [N] |
|---|---:|---:|---:|---:|---:|---:|---:|
| Coarse | 8.0 | 104,904 | 60,697 | 0.00036555 | 6.0707 | 6.0963 | 2000 |
| Medium | 5.0 | 217,130 | 127,301 | 0.00036585 | 6.2094 | 6.8885 | 2000 |
| Fine | 3.0 | 416,866 | 245,658 | 0.00036606 | 8.2600 | 7.1615 | 2000 |
| Very fine | 2.0 | 798,700 | 472,372 | 0.00036618 | 8.5602 | 8.1603 | 2000 |

## Results Interpretation

The reaction force remained balanced at 2,000 N for every mesh level, indicating that the LC1 applied load and fixed-support setup are mechanically consistent.

Maximum total deformation changed from 0.00036555 mm on the coarse mesh to 0.00036618 mm on the very fine mesh. The fine-to-very-fine deformation change was approximately 0.033%, so the global stiffness response is considered converged for this educational study.

Maximum von Mises stress increased from 6.0707 MPa on the coarse mesh to 8.5602 MPa on the very fine mesh. The fine-to-very-fine change was approximately 3.63%, which is acceptable for the current portfolio-level screening objective.

Maximum principal stress remained more mesh-sensitive, with a fine-to-very-fine change of approximately 13.95%. The observed hotspot is on the back-side mounting-hole fillet region and should be treated as boundary-condition-sensitive because the mounting holes were idealized as fixed supports.

## LC2 Linear Scaling Check

LC2 uses the same geometry, material, fine mesh, load face and fixed support definition as LC1, with the lateral load increased from 2,000 N to 5,000 N. The expected linear scale factor is 2.5.

| Quantity | LC1 fine | Expected LC2 = LC1 x 2.5 | LC2 fine |
|---|---:|---:|---:|
| Max deformation [mm] | 0.00036606 | 0.00091515 | 0.00091514 |
| Max von Mises stress [MPa] | 8.2600 | 20.650 | 20.65 |
| Max principal stress [MPa] | 7.1615 | 17.9038 | 17.904 |
| Reaction force [N] | 2000 | 5000 | 5000 |

The LC2 response scales almost exactly from LC1, confirming a clean linear static result with no evidence of changed mesh, material, constraint or force direction.

## LC3 Combined Load Check

LC3 uses the same geometry, material, fine mesh and support definition as LC1-LC2, but applies a combined load vector of `[3000, 2000, 0]` N.

| Quantity | LC3 fine result |
|---|---:|
| Max total deformation [mm] | 0.001009 |
| Max von Mises stress [MPa] | 19.572 |
| Max principal stress [MPa] | 20.067 |
| Reaction X [N] | -3000 |
| Reaction Y [N] | -2000 |
| Reaction Z [N] | 0 |
| Total reaction [N] | 3605.6 |

The expected reaction resultant is:

```text
sqrt(3000^2 + 2000^2) = 3605.5 N
```

The ANSYS total reaction result of 3605.6 N is effectively exact for this portfolio-level model.

LC3 has a lower resultant load than LC2, but slightly higher total deformation. This is physically reasonable because the added vertical component excites a different bending and twisting response rather than the same purely lateral load path used in LC2. The LC3 maximum principal stress is also slightly higher than LC2, which is reasonable for combined loading that creates a stronger local tensile hotspot.

## LC4 Constrained Thermal Expansion Check

LC4 applies a uniform +100 C body temperature change while retaining the idealized fixed support on the mounting-hole cylindrical faces. This case is retained as a conservative thermal over-constraint sensitivity case.

| Quantity | LC4 fine result |
|---|---:|
| Max total deformation [mm] | 0.15288 |
| Max von Mises stress [MPa] | 2705.7 |
| Max principal stress [MPa] | 1527.5 |
| Reaction X [N] | -9.52e-05 |
| Reaction Y [N] | -5.63e-06 |
| Reaction Z [N] | -7.73e-06 |
| Total reaction [N] | 9.5726e-05 |

The deformation confirms that the temperature load is active and that thermal expansion is being calculated. The near-zero total reaction is not by itself an error because a pure thermal expansion case can have internal constraint reactions whose vector sum is near zero.

The very high peak stresses are not accepted as realistic design stresses. They are interpreted as local boundary-condition artifacts caused by suppressing thermal expansion at the fixed mounting-hole faces. LC4 is therefore reported as a constraint-sensitivity case rather than an ASME-style allowable stress result.

## LC4R Relaxed Thermal Expansion Check

LC4R applies the same uniform +100 C body temperature change as LC4, but replaces the fixed mounting-hole supports with a lightly constrained 3-2-1 locating/sliding support scheme. The intent is to prevent rigid-body motion while allowing the plate to expand thermally.

| Quantity | LC4R fine result |
|---|---:|
| Max total deformation [mm] | 0.30092 |
| Max von Mises stress [MPa] | 0.0171 |
| Max principal stress [MPa] | 0.0166 |
| RD1 reaction total [N] | 0.257 |
| RD2 reaction total [N] | 0.234 |
| RD3 reaction total [N] | 0.561 |

LC4R is the realistic thermal-expansion sanity case. The deformation is plausible for +100 C thermal expansion over this plate size, while the stresses and remote reactions are negligible. This confirms that the high LC4 peak stresses are caused by the fixed-hole over-constraint rather than the uniform temperature load itself.

ANSYS reported a warning that not enough constraints may be applied to prevent rigid-body motion. This is acceptable for LC4R if there is no solver pivot warning, no missing result file, and the displayed results remain stable. The remote-boundary-condition element-count warning is interpreted as a solver performance warning rather than a physics failure.

## Screening Statement

The LC1, LC2 and LC3 peak stresses are low compared with typical room-temperature yield strength levels for annealed 316 stainless steel. LC4 peak stress is intentionally not treated as a design stress because it is dominated by the idealized fixed-hole thermal constraint. LC4R indicates that thermal expansion alone is not structurally critical under a sliding/support mounting assumption. This report does not claim formal ASME acceptance because it does not perform ASME stress categorization, use certified design-allowable data, or model bolt preload, contact, support compliance, fatigue, seismic loading, irradiation, welds or nonlinear plasticity.

## Conclusion

For LC1, the model shows stable global deformation convergence and acceptable von Mises stress convergence between the fine and very fine meshes. The fine mesh is a reasonable working mesh for follow-on educational load cases because it captures the main stress distribution at lower computational cost than the very fine mesh.

For LC2, the fine-mesh response scales by approximately 2.5 from LC1, matching the applied load increase from 2 kN to 5 kN. LC2 is accepted as complete for this educational linear static study.

For LC3, the reaction vector balances the combined applied load and the deformation/stress behavior is physically reasonable for a different loading direction. LC3 is accepted as complete for this educational linear static study.

For LC4, the uniform +100 C temperature load is active and the deformation magnitude is plausible. The stress peak is treated as a boundary-condition-sensitive over-constraint indicator, not as a final design stress. LC4 is accepted as complete only in that sensitivity-case role.

For LC4R, the same thermal load produces realistic expansion with negligible stress and tiny remote reactions. LC4R is accepted as the final realistic thermal expansion case for this portfolio model.

The maximum principal stress hotspot near the idealized mounting-hole support should be reported as a local modeling sensitivity, not as a certified bolt-joint design stress.

## Recommended Follow-On Work

1. Add a final screening table that separates mechanical stresses from the LC4 over-constraint sensitivity stress.
2. Optionally add an assembly-level thermal mismatch model with a base plate and simplified bolts/washers.
3. Include a simplified allowable-stress screening table with clearly stated non-code assumptions.
4. If more realism is desired, replace fixed mounting-hole supports with bolt/contact/support-compliance modeling.
