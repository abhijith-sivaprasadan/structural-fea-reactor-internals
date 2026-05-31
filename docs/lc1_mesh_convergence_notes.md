# LC1 Mesh Convergence Notes

## Case definition

- Analysis type: Static Structural
- Load case: LC1 lateral load
- Applied load: 2,000 N on the central bore inner face
- Support condition: Fixed support on the mounting-hole cylindrical faces
- Material: Stainless steel, 316, annealed from ANSYS GRANTA Materials Data for Simulation Sample
- Mesh method: Patch Conforming tetrahedral mesh
- Units: mm, N, MPa

## Mesh controls used

The mesh was refined using global element size plus local face sizing. Local sizing was applied to the central bore load face, mounting-hole cylindrical faces, counterbore seat faces, and structural fillet faces, including the underside mounting-hole fillets where the maximum principal stress hotspot was observed.

Inflation layers were not used because this is a structural solid-mechanics model, not a CFD boundary-layer problem.

## Raw convergence table

| Mesh level | Global size [mm] | Nodes | Elements | Max deformation [mm] | Max von Mises [MPa] | Max principal [MPa] | Reaction [N] |
|---|---:|---:|---:|---:|---:|---:|---:|
| Coarse | 8.0 | 104,904 | 60,697 | 0.00036555 | 6.0707 | 6.0963 | 2000 |
| Medium | 5.0 | 217,130 | 127,301 | 0.00036585 | 6.2094 | 6.8885 | 2000 |
| Fine | 3.0 | 416,866 | 245,658 | 0.00036606 | 8.2600 | 7.1615 | 2000 |
| Very fine | 2.0 | 798,700 | 472,372 | 0.00036618 | 8.5602 | 8.1603 | 2000 |

## Convergence observations

### Reaction force

The reaction force remained balanced at 2,000 N for all mesh levels. This confirms that the applied force and fixed support setup are mechanically consistent.

### Deformation

The maximum total deformation changed from 0.00036555 mm in the coarse mesh to 0.00036618 mm in the very fine mesh. The total change from coarse to very fine was approximately 0.172%.

The fine-to-very-fine deformation change was approximately 0.033%, so the global stiffness/deformation response is considered converged.

### Von Mises stress

The maximum von Mises stress increased from 6.0707 MPa in the coarse mesh to 8.5602 MPa in the very fine mesh. The fine-to-very-fine change was approximately 3.63%.

This is acceptable for the current portfolio-level study. The final peak von Mises stress is low compared with typical yield strength levels for annealed 316 stainless steel, but the local peak should still be interpreted with care because it occurs near the idealised mounting-hole support region.

### Maximum principal stress

The maximum principal stress changed from 7.1615 MPa in the fine mesh to 8.1603 MPa in the very fine mesh, corresponding to approximately 13.95% change.

The principal stress hotspot was observed on the back-side/underside mounting-hole fillet region. This is a realistic tensile hotspot location for the current load path, but it is also influenced by the simplified fixed support condition applied to the mounting-hole cylindrical faces.

## Interpretation

The mesh convergence study shows strong convergence in global deformation and acceptable convergence in maximum von Mises stress between the fine and very fine meshes. The maximum principal stress remains more sensitive because the hotspot is located near the underside mounting-hole fillet close to the idealised support region.

For subsequent load cases, the fine mesh is selected as the working mesh because it captures the main stress distribution while keeping the model lighter than the very fine mesh. The very fine mesh is retained as convergence evidence.

## Reporting limitation

The mounting holes were modelled using an idealised fixed support on the cylindrical hole faces. Bolt preload, washer contact, clearance, support compliance, and detailed bolt-joint behaviour were not modelled. Therefore, stress peaks near the fixed mounting-hole support should be treated as local boundary-condition-sensitive values rather than certified bolt-joint design stresses.

This model is an educational/portfolio-level structural FEM demonstration and is not an ASME BPVC-compliant design calculation.
