# LC4 Constrained Thermal Expansion Notes

## Case Definition

- Analysis type: Static Structural with thermal strain
- Load case: LC4 constrained thermal expansion sensitivity
- Temperature load: +100 C uniform body temperature change
- Temperature scope: 1 body
- Support condition: Fixed support on the mounting-hole cylindrical faces
- Material: Stainless steel, 316, annealed from ANSYS GRANTA Materials Data for Simulation Sample
- Mesh level: Fine
- Mesh size basis: same fine mesh used for LC1-LC3
- Units: mm, N, MPa, C

## Fine Mesh Results

| Quantity | LC4 result |
|---|---:|
| Thermal delta [C] | 100 |
| Max total deformation [mm] | 0.15288 |
| Max von Mises stress [MPa] | 2705.7 |
| Max principal stress [MPa] | 1527.5 |
| Reaction X [N] | -9.52e-05 |
| Reaction Y [N] | -5.63e-06 |
| Reaction Z [N] | -7.73e-06 |
| Total reaction [N] | 9.5726e-05 |

## Interpretation

The temperature load is active and the deformation magnitude is believable for a +100 C thermal expansion case on a stainless-steel part of this size.

The near-zero net reaction force is also acceptable for a pure thermal case with no external mechanical load. Individual fixed regions may carry internal constraint reactions, while the total vector sum can still be near zero.

The very high local peak stresses are not treated as design stresses. The max von Mises stress of 2705.7 MPa and max principal stress of 1527.5 MPa are interpreted as local artifacts from the idealized fixed mounting-hole supports suppressing uniform thermal expansion.

The average stress behavior is more believable than the local peak. Therefore, LC4 is retained as a conservative thermal over-constraint sensitivity case, not as a realistic final thermal design case.

## Screenshots

- `../ansys/screenshots/lc4_fine_total_deformation.png`
- `../ansys/screenshots/lc4_fine_von_mises.png`
- `../ansys/screenshots/lc4_fine_max_principal_stress.png`
- `../ansys/screenshots/lc4_fine_reaction_force.png`

## Reporting Statement

The high local stress peak in LC4 is caused by idealized fixed mounting-hole constraints under uniform thermal expansion. Therefore, the peak stress is treated as a constraint-sensitivity indicator rather than a design-allowable stress value.

## Recommended Follow-On Case

A relaxed thermal expansion check should be added later as `LC4R_Relaxed_Thermal_Expansion_100C`, using minimal constraints only to prevent rigid-body motion. Expected behavior is near-zero stress with a free thermal expansion deformation pattern.

## Verdict

LC4 is complete as a constrained thermal expansion sensitivity case. It should not be presented as a clean final design-stress result.
