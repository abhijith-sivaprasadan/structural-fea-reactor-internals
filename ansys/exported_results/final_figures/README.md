# Final Figures

This folder contains copied final-report figures exported from the ANSYS screenshot evidence folder.

## Included

| Figure | Source |
|---|---|
| `LC1_total_deformation.png` | `../../screenshots/06_lc1_deformation_fine.png` |
| `LC1_equivalent_stress.png` | `../../screenshots/08_lc1_von_mises_fine.png` |
| `LC1_max_principal_stress.png` | `../../screenshots/07_lc1_principal_stress_fine.png` |
| `LC2_total_deformation.png` | `../../screenshots/lc2_fine_total_deformation.png` |
| `LC2_equivalent_stress.png` | `../../screenshots/lc2_fine_von_mises.png` |
| `LC2_max_principal_stress.png` | `../../screenshots/lc2_fine_max_principal.png` |
| `LC2_reaction_force.png` | `../../screenshots/lc2_fine_reaction_force.png` |
| `LC3_total_deformation.png` | `../../screenshots/lc3_fine_total_deformation.png` |
| `LC3_equivalent_stress.png` | `../../screenshots/lc3_fine_von_mises.png` |
| `LC3_max_principal_stress.png` | `../../screenshots/lc3_fine_max_principal.png` |
| `LC3_reaction_force.png` | `../../screenshots/lc3_fine_reaction_force.png` |
| `LC4_overconstrained_equivalent_stress.png` | `../../screenshots/lc4_fine_von_mises.png` |
| `LC4R_total_deformation.png` | `../../screenshots/lc4r_fine_total_deformation.png` |
| `LC4R_equivalent_stress.png` | `../../screenshots/lc4r_fine_von_mises.png` |
| `final_fine_mesh.png` | `../../screenshots/05_mesh_fine.png` |

## Suggested Captions

| Figure | Caption |
|---|---|
| `final_fine_mesh.png` | Fine working mesh used for LC2-LC4R. Local refinement was applied at the bore, mounting holes, counterbores and filleted transitions. |
| `LC1_total_deformation.png` | LC1 baseline 2 kN lateral-load deformation result. |
| `LC1_equivalent_stress.png` | LC1 equivalent stress distribution for the baseline lateral-load case. |
| `LC2_equivalent_stress.png` | LC2 5 kN lateral-load stress result, used as the linear robustness case. |
| `LC3_reaction_force.png` | LC3 combined-load reaction check; the reaction resultant balances the applied `[3000, 2000, 0]` N load. |
| `LC4_overconstrained_equivalent_stress.png` | LC4 fixed-hole thermal case showing artificial local stress from over-constrained thermal expansion. |
| `LC4R_total_deformation.png` | LC4R relaxed thermal-expansion deformation result using the 3-2-1 support approach. |
| `LC4R_equivalent_stress.png` | LC4R relaxed thermal-expansion stress result showing negligible thermal stress when expansion is allowed. |

## Not Available As Screenshots

The requested `LC1_reaction_force.png` and `LC4R_reaction_forces.png` screenshots were not present in the source screenshot folder. Their values are still reported in `../load_case_summary.csv` and `../../../results/load_case_summary.md`.
