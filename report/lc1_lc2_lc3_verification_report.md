# LC1-LC2-LC3 Verification-Style Report

## Project

ASME-aware structural FEM study of a simplified reactor-internal support component.

This report summarizes the LC1, LC2 and LC3 load cases for a non-proprietary educational portfolio model. It is not an ASME BPVC-compliant design calculation and is not a certified nuclear component assessment.

## Model Description

The analyzed component is a simplified stainless-steel support plate with a raised central guide collar, central through-bore, four mounting bosses, counterbored mounting holes, radial stiffening ribs and filleted load-transfer features.

Reference files:
- Geometry notes: `../geometry/geometry_notes.md`
- STEP geometry: `../geometry/simplified_reactor_support_improved.step`
- Assumptions and limitations: `../docs/assumptions_and_limitations.md`

## Load Case Definition

| Item | Value |
|---|---|
| Load cases | LC1, LC2 and LC3 |
| Analysis type | Static structural |
| Applied loads | LC1: 2,000 N lateral; LC2: 5,000 N lateral; LC3: 3,000 N lateral + 2,000 N vertical |
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

## Screening Statement

The LC1, LC2 and LC3 peak stresses are low compared with typical room-temperature yield strength levels for annealed 316 stainless steel. However, this report does not claim formal ASME acceptance because it does not perform ASME stress categorization, use certified design-allowable data, or model bolt preload, contact, support compliance, fatigue, seismic loading, irradiation, welds or nonlinear plasticity.

## Conclusion

For LC1, the model shows stable global deformation convergence and acceptable von Mises stress convergence between the fine and very fine meshes. The fine mesh is a reasonable working mesh for follow-on educational load cases because it captures the main stress distribution at lower computational cost than the very fine mesh.

For LC2, the fine-mesh response scales by approximately 2.5 from LC1, matching the applied load increase from 2 kN to 5 kN. LC2 is accepted as complete for this educational linear static study.

For LC3, the reaction vector balances the combined applied load and the deformation/stress behavior is physically reasonable for a different loading direction. LC3 is accepted as complete for this educational linear static study.

The maximum principal stress hotspot near the idealized mounting-hole support should be reported as a local modeling sensitivity, not as a certified bolt-joint design stress.

## Recommended Follow-On Work

1. Export and post-process LC4 result data using the same table format.
2. Expand the comparison table across all load cases after LC4 is solved.
3. Include a simplified allowable-stress screening table with clearly stated non-code assumptions.
4. If more realism is desired, replace fixed mounting-hole supports with bolt/contact/support-compliance modeling.
