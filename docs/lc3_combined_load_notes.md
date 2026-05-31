# LC3 Combined Load Notes

## Case Definition

- Analysis type: Static Structural
- Load case: LC3 combined lateral and vertical load
- Applied load vector: 3,000 N lateral + 2,000 N vertical
- Support condition: Fixed support on the mounting-hole cylindrical faces
- Material: Stainless steel, 316, annealed from ANSYS GRANTA Materials Data for Simulation Sample
- Mesh level: Fine
- Mesh size basis: same fine mesh used for LC1 and LC2
- Units: mm, N, MPa

## Fine Mesh Results

| Quantity | LC3 result |
|---|---:|
| Max total deformation [mm] | 0.001009 |
| Max von Mises stress [MPa] | 19.572 |
| Max principal stress [MPa] | 20.067 |
| Reaction X [N] | -3000 |
| Reaction Y [N] | -2000 |
| Reaction Z [N] | 0 |
| Total reaction [N] | 3605.6 |

## Force Balance Check

The applied load vector is `[3000, 2000, 0]` N and the reaction vector is `[-3000, -2000, 0]` N.

```text
sqrt(3000^2 + 2000^2) = 3605.5 N
ANSYS reaction result = 3605.6 N
```

The force balance is effectively exact for this portfolio-level result.

## Sanity Check Against LC2

LC2 has a higher resultant load of 5,000 N, while LC3 has a resultant load of approximately 3,605.6 N. LC3 still shows slightly higher deformation than LC2 because the vertical component excites a different bending and twisting mode rather than only the lateral load-transfer path.

LC3 stresses are close to LC2 but have a different distribution. The maximum principal stress being slightly higher than LC2 is reasonable because combined loading can create a stronger local tensile hotspot even with a lower resultant force.

## Screenshots

- `../ansys/screenshots/lc3_fine_total_deformation.png`
- `../ansys/screenshots/lc3_fine_von_mises.png`
- `../ansys/screenshots/lc3_fine_max_principal.png`
- `../ansys/screenshots/lc3_fine_reaction_force.png`

## Verdict

LC3 is complete. The fine-mesh solution has a clean vector force balance and physically reasonable deformation/stress behavior for the combined loading direction.
