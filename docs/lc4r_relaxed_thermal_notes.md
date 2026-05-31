# LC4R Relaxed Thermal Expansion Notes

## Case Definition

- Analysis type: Static Structural with thermal strain
- Load case: LC4R relaxed thermal expansion check
- Temperature load: +100 C uniform body temperature change
- Support approach: 3-2-1 locating/sliding remote-displacement scheme
- Material: Stainless steel, 316, annealed from ANSYS GRANTA Materials Data for Simulation Sample
- Mesh level: Fine
- Mesh size basis: same fine mesh used for LC1-LC4
- Units: mm, N, MPa, C

## Support Interpretation

LC4R replaces the fully fixed mounting-hole support used in LC4 with a lightly constrained support scheme intended to prevent rigid-body motion while allowing in-plane thermal expansion.

The intended support logic is:

| Support | X | Y | Z | Rotations |
|---|---|---|---|---|
| RD1 locating support | Fixed | Fixed | Fixed | Free |
| RD2 sliding support | Free | Fixed | Fixed | Free |
| RD3 plane support | Free | Free | Fixed | Free |

Rotations are left free to avoid artificial bending restraint.

For the final solved ANSYS session, the practical global-coordinate implementation was:

| Remote support | Final implementation |
|---|---|
| RD1 at approximately `(70, -40, 7)` mm | UX = 0, UY = 0, UZ = 0; RX = RY = RZ = Free |
| RD2 at approximately `(70, 40, 7)` mm | UX = 0, UY = Free, UZ = 0; RX = RY = RZ = Free |
| RD3 at approximately `(-70, 40, 7)` mm | UX = Free, UY = Free, UZ = 0; RX = RY = RZ = Free |

This is the same 3-2-1 intent mapped onto the actual hole layout and global axis directions used in the final ANSYS session.

## Fine Mesh Results

| Quantity | LC4R result |
|---|---:|
| Thermal delta [C] | 100 |
| Max total deformation [mm] | 0.30092 |
| Max von Mises stress [MPa] | 0.0171 |
| Max principal stress [MPa] | 0.0166 |
| RD1 reaction total [N] | 0.257 |
| RD2 reaction total [N] | 0.234 |
| RD3 reaction total [N] | 0.561 |

## Warning Interpretation

ANSYS reported a caution that not enough constraints may be applied to prevent rigid-body motion. For this case, that warning is acceptable if there is no solver pivot warning, no missing result file, and results display normally. The model is intentionally lightly constrained so the part can thermally expand without artificial restraint.

ANSYS also reported that one or more remote boundary conditions are scoped to many elements. This is interpreted as a performance warning rather than a physics failure because the model solved and the remote reaction totals remain very small.

Rejected warning states:

- Solver pivot warning
- Result file not found
- Remote attachment missing or disconnected

Those warning states are not carried forward into the accepted LC4R result.

Clean-solve checks used:

1. Clear generated solution data.
2. Confirm each remote point is attached to the intended mounting-hole region.
3. Confirm rotations remain free.
4. Solve.
5. Accept only if the deformed shape and stress field display normally.
6. Confirm remote reaction totals remain below 1 N.

## Interpretation

LC4R behaves as expected for a realistic thermal-expansion sanity check. The deformation is larger than LC4 because thermal growth is allowed, while stresses and reactions are essentially zero.

This confirms that the very high LC4 stresses were caused by fixed-hole thermal over-constraint, not by the uniform temperature load itself.

## Screenshots

- `../ansys/screenshots/lc4r_fine_total_deformation.png`
- `../ansys/screenshots/lc4r_fine_von_mises.png`
- `../ansys/screenshots/lc4r_fine_principal_stress.png`

## Reporting Statement

The realistic thermal-expansion case produced a maximum deformation of 0.30092 mm, while stresses and reactions remained negligible because the support scheme allowed in-plane expansion. This confirms that thermal loading alone is not structurally critical under a sliding/support mounting assumption.

## Verdict

LC4R is accepted as the final realistic thermal expansion case. LC4 is retained only as a conservative over-constraint sensitivity comparison.
