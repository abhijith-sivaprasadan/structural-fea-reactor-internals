# LC1 Verification-Style Report

## Project

ASME-aware structural FEM study of a simplified reactor-internal support component.

This report summarizes the LC1 lateral-load case for a non-proprietary educational portfolio model. It is not an ASME BPVC-compliant design calculation and is not a certified nuclear component assessment.

## Model Description

The analyzed component is a simplified stainless-steel support plate with a raised central guide collar, central through-bore, four mounting bosses, counterbored mounting holes, radial stiffening ribs and filleted load-transfer features.

Reference files:
- Geometry notes: `../geometry/geometry_notes.md`
- STEP geometry: `../geometry/simplified_reactor_support_improved.step`
- Assumptions and limitations: `../docs/assumptions_and_limitations.md`

## Load Case Definition

| Item | Value |
|---|---|
| Load case | LC1 |
| Analysis type | Static structural |
| Applied load | 2,000 N lateral load on central bore inner face |
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

Data and generated outputs:
- Raw convergence data: `../ansys/exported_results/mesh_convergence_raw.csv`
- Processed convergence table: `../results/lc1_mesh_convergence_summary.csv`
- Markdown convergence table: `../results/lc1_mesh_convergence_summary.md`
- Deformation convergence plot: `../results/lc1_deformation_convergence.png`
- Von Mises convergence plot: `../results/lc1_von_mises_convergence.png`
- Principal stress convergence plot: `../results/lc1_principal_stress_convergence.png`
- Normalized convergence plot: `../results/lc1_normalized_convergence.png`

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

## Screening Statement

The LC1 peak stresses are low compared with typical room-temperature yield strength levels for annealed 316 stainless steel. However, this report does not claim formal ASME acceptance because it does not perform ASME stress categorization, use certified design-allowable data, or model bolt preload, contact, support compliance, fatigue, seismic loading, irradiation, welds or nonlinear plasticity.

## Conclusion

For LC1, the model shows stable global deformation convergence and acceptable von Mises stress convergence between the fine and very fine meshes. The fine mesh is a reasonable working mesh for follow-on educational load cases because it captures the main stress distribution at lower computational cost than the very fine mesh.

The maximum principal stress hotspot near the idealized mounting-hole support should be reported as a local modeling sensitivity, not as a certified bolt-joint design stress.

## Recommended Follow-On Work

1. Export and post-process LC2, LC3 and LC4 result data using the same table format.
2. Add one comparison table across all load cases after LC2-LC4 are solved.
3. Include a simplified allowable-stress screening table with clearly stated non-code assumptions.
4. If more realism is desired, replace fixed mounting-hole supports with bolt/contact/support-compliance modeling.
