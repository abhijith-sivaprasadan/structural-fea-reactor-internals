# LC2 Linear Static Notes

## Case Definition

- Analysis type: Static Structural
- Load case: LC2 lateral load
- Applied load: 5,000 N on the central bore inner face
- Support condition: Fixed support on the mounting-hole cylindrical faces
- Material: Stainless steel, 316, annealed from ANSYS GRANTA Materials Data for Simulation Sample
- Mesh level: Fine
- Mesh size basis: same fine mesh used for LC1
- Units: mm, N, MPa

## Linearity Check

LC2 uses the same geometry, material, mesh and boundary conditions as LC1, with the lateral force increased from 2,000 N to 5,000 N.

The expected linear scale factor is:

```text
5000 / 2000 = 2.5
```

| Quantity | LC1 fine | Expected LC2 = LC1 x 2.5 | LC2 fine |
|---|---:|---:|---:|
| Max deformation [mm] | 0.00036606 | 0.00091515 | 0.00091514 |
| Max von Mises stress [MPa] | 8.2600 | 20.650 | 20.65 |
| Max principal stress [MPa] | 7.1615 | 17.9038 | 17.904 |
| Reaction force [N] | 2000 | 5000 | 5000 |

The LC2 response scales almost exactly from LC1, which confirms a clean linear static setup for this load increase.

## Sanity Checks

- Applied lateral force: 5,000 N
- Total reaction force: 5,000 N
- Deformation pattern: same as LC1, scaled up by the load ratio
- Mesh, material, constraints and force direction: unchanged from LC1

## Screenshots

- `../ansys/screenshots/lc2_fine_total_deformation.png`
- `../ansys/screenshots/lc2_fine_von_mises.png`
- `../ansys/screenshots/lc2_fine_max_principal.png`
- `../ansys/screenshots/lc2_fine_reaction_force.png`

## Verdict

LC2 is complete. The fine-mesh LC2 solution is accepted as a valid linear scaling case from LC1 for this educational portfolio study.
