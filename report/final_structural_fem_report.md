# ANSYS Mechanical Pilot Study: Structural Integrity, Mesh Convergence, and Thermal Expansion Behaviour of a Stainless-Steel Support Plate

## Objective

The objective of this study is to evaluate whether a stainless-steel support plate can safely withstand representative lateral, vertical, combined and thermal expansion loading while maintaining low deformation and acceptable stress levels. The study also compares idealized and realistic thermal boundary conditions to show the effect of overconstraint on thermal stress prediction.

The work is ASME-aware, but it is not an ASME BPVC-compliant design calculation and does not represent certified nuclear component design.

## Acceptance Criteria

| Quantity | Criterion | Check |
|---|---|---|
| Max von Mises stress | Below preliminary yield-strength screen | Compare against 205 MPa assumed yield strength for annealed 316 stainless steel |
| Max deformation | Small relative to component size/support function | Review displacement magnitude and deformation pattern |
| Reaction force | Balance applied mechanical load | Compare reaction resultant with applied resultant |
| Mesh convergence | Stable final mesh response | LC1 mesh convergence study |
| Thermal stress | Interpreted based on support realism | Compare LC4 fixed thermal case with LC4R relaxed thermal case |

The 205 MPa yield value is used as a preliminary screening value. It should be replaced by the exact ANSYS/GRANTA material-card yield strength if that value differs.

## Geometry Description

The model is a non-proprietary stainless-steel support plate with:

- Central guide opening and raised guide collar
- Four mounting holes with raised bosses/counterbore features
- Four radial stiffening ribs
- Filleted ribs, bosses, collar and plate edges

The geometry is documented in `../geometry/geometry_notes.md`.

## Material

The modeled material is stainless steel 316, annealed, selected from ANSYS GRANTA Materials Data for Simulation Sample.

The analysis uses linear elastic material behavior. Temperature-dependent material behavior, plasticity, fatigue, seismic loading, irradiation effects, welds and certified ASME material allowables are outside the project scope.

## Boundary Conditions And Load Cases

The final frozen load cases are:

| Load case | Description | Reporting role |
|---|---|---|
| LC1 | 2 kN lateral load | Baseline mechanical load |
| LC2 | 5 kN lateral load | Higher lateral robustness case |
| LC3 | 3 kN lateral + 2 kN vertical | Combined mechanical case |
| LC4 | +100 C constrained thermal expansion | Over-constraint comparison only |
| LC4R | +100 C relaxed thermal expansion | Final realistic thermal expansion case |

LC1-LC3 use fixed support on the mounting-hole cylindrical faces. LC4 intentionally keeps that fixed-hole support for a conservative over-constraint sensitivity comparison. LC4R replaces fixed-hole support with a 3-2-1 locating/sliding remote-displacement approach to allow thermal expansion while preventing rigid-body motion.

## Mesh Strategy

The mesh uses patch-conforming tetrahedral elements. Mesh controls were refined around the central bore, mounting-hole regions, counterbores, ribs and fillets. The fine mesh selected for final load-case reporting contains:

| Mesh level | Elements | Nodes |
|---|---:|---:|
| Fine | 245,658 | 416,866 |

Final mesh figure: `../ansys/exported_results/final_figures/final_fine_mesh.png`

## Mesh Convergence

LC1 was used for mesh convergence. The global deformation response converged very strongly, and the fine-to-very-fine von Mises stress change was acceptable for this educational portfolio model.

| Mesh level | Global size [mm] | Nodes | Elements | Max deformation [mm] | Max von Mises [MPa] | Max principal [MPa] |
|---|---:|---:|---:|---:|---:|---:|
| Coarse | 8.0 | 104,904 | 60,697 | 0.00036555 | 6.0707 | 6.0963 |
| Medium | 5.0 | 217,130 | 127,301 | 0.00036585 | 6.2094 | 6.8885 |
| Fine | 3.0 | 416,866 | 245,658 | 0.00036606 | 8.2600 | 7.1615 |
| Very fine | 2.0 | 798,700 | 472,372 | 0.00036618 | 8.5602 | 8.1603 |

The principal stress remained more sensitive because the hotspot occurs near an idealized fixed mounting-hole support. This is reported as a local boundary-condition-sensitive peak.

## Mechanical Load Case Results

| Case | Max deformation [mm] | Max principal stress [MPa] | Max von Mises stress [MPa] | Reaction |
|---|---:|---:|---:|---|
| LC1 | 0.00036606 | 7.1615 | 8.26 | 2000 N |
| LC2 | 0.00091514 | 17.904 | 20.65 | 5000 N |
| LC3 | 0.001009 | 20.067 | 19.572 | 3605.6 N resultant |

LC2 scales almost exactly from LC1 by the load ratio of 2.5, confirming clean linear static behavior. LC3 has a lower resultant load than LC2, but slightly higher deformation because the vertical component excites a different bending/twisting response.

## Verification Checks

The mechanical cases passed basic equilibrium and linearity checks.

| Check | Expected | ANSYS result | Interpretation |
|---|---:|---:|---|
| LC2 / LC1 load ratio | 2.5 | 2.5 displacement ratio | Linear response confirmed |
| LC1 reaction | 2000 N | 2000 N | Balanced |
| LC2 reaction | 5000 N | 5000 N | Balanced |
| LC3 resultant reaction | 3605.5 N | 3605.6 N | Balanced |

For LC3:

```text
sqrt(3000^2 + 2000^2) = 3605.5 N
```

The reaction-force checks show that the load application and supports are mechanically consistent.

## Safety Factor Screening

| Case | Max von Mises [MPa] | Screening yield [MPa] | Preliminary factor of safety | Status |
|---|---:|---:|---:|---|
| LC1 | 8.26 | 205 | 24.82 | Pass |
| LC2 | 20.65 | 205 | 9.93 | Pass |
| LC3 | 19.572 | 205 | 10.47 | Pass |
| LC4 constrained thermal | 2705.7 | 205 | N/A | Not design-screened |
| LC4R relaxed thermal | 0.0171 | 205 | Very large | Pass, thermal sanity check |

LC4 is excluded from design screening because its peak stress is an over-constrained thermal artifact. LC4R is the accepted thermal expansion case.

## Thermal Expansion Comparison

| Case | Max deformation [mm] | Max principal stress [MPa] | Max von Mises stress [MPa] | Interpretation |
|---|---:|---:|---:|---|
| LC4 constrained thermal | 0.15288 | 1527.5 | 2705.7 | Over-constraint comparison only |
| LC4R relaxed thermal | 0.30092 | 0.0166 | 0.0171 | Final realistic thermal expansion case |

LC4 showed very high local stresses because the whole body was trying to thermally expand while the mounting-hole cylindrical faces were fixed. That peak stress is treated as a boundary-condition artifact, not a design stress.

LC4R used a 3-2-1 support approach to allow in-plane thermal expansion. The resulting deformation is plausible for +100 C thermal expansion, while stress and support reactions are negligible. This confirms that thermal loading alone is not structurally critical under the relaxed support assumption.

The thermal-expansion case was intentionally modelled with minimal kinematic constraints to allow free expansion. Solver warnings related to low constraint stiffness were reviewed, and reactions were confirmed to be negligible.

## Boundary-Condition Sensitivity

| Case | Boundary condition | Result behavior | Interpretation |
|---|---|---|---|
| LC1-LC3 mechanical | Fixed mounting-hole cylindrical faces | Low deformation, local stress concentration near holes/fillets | Conservative mechanical support idealization |
| LC4 thermal | Fully fixed mounting holes under uniform +100 C | Unrealistically high local thermal stress | Over-constraint comparison only |
| LC4R thermal | 3-2-1 locating/sliding support | Realistic expansion, negligible thermal stress | Final thermal representation |

The thermal comparison demonstrates a key FEA principle: thermal stress is generated by restrained thermal expansion, not by temperature alone.

## Discussion

The support plate is extremely stiff under the applied mechanical loads. Even under LC3 combined loading, maximum deformation is approximately 0.001 mm and stresses remain far below typical yield strength levels for annealed stainless steel 316.

The highest mechanical stresses occur around hole/fillet regions, which is expected because these regions create local stress concentration and are close to idealized support conditions.

The thermal study is the most important modeling judgment in the project. The fixed-hole LC4 result demonstrates why blindly accepting maximum FEA stress can be misleading. LC4R shows the physically realistic free-expansion behavior for a sliding/support mounting assumption.

## Design Recommendation

The current component is not governed by global bending or gross deformation. The main design attention should be local stress concentration near mounting-hole, counterbore, rib and fillet transitions.

Recommended future geometry improvements:

- Increase fillet radius at rib-to-boss transitions.
- Increase underside mounting-hole fillet radius where practical.
- Smooth abrupt counterbore-to-plate transitions.
- Consider local washer-seat reinforcement if bolt-joint realism is added later.

These changes are expected to reduce local peak stress while leaving the global stiffness response largely unchanged.

## Limitations

This project does not include:

- ASME BPVC stress categorization
- Certified material allowable checks
- Bolt preload, washer contact or realistic joint compliance
- Frictional contact, clearance or support/base-plate assembly modeling
- Nonlinear plasticity
- Fatigue, seismic or irradiation effects
- Manufacturing tolerances or weld details

## Conclusion

The final mechanical load cases show low deformation and low elastic stress for the simplified support component. LC1 provides the mesh-converged baseline, LC2 confirms linear scaling under increased lateral load, and LC3 confirms reasonable behavior under combined lateral and vertical loading.

For thermal loading, LC4 is retained only as an over-constraint comparison. LC4R is the final thermal result because it permits realistic expansion and produces negligible stress. The final engineering conclusion is that the simplified component is mechanically stiff under the studied loads, and that thermal stress is not critical when expansion is not artificially restrained.

## Appendix

Key files:

- Raw mesh convergence data: `../ansys/exported_results/mesh_convergence_raw.csv`
- Final load-case summary: `../ansys/exported_results/load_case_summary.csv`
- Final reporting values: `../results/final_reporting_values.md`
- Safety factor summary: `../results/safety_factor_summary.md`
- Acceptance criteria and checks: `../docs/acceptance_criteria_and_checks.md`
- Design recommendations: `../docs/design_recommendations.md`
- Final figures: `../ansys/exported_results/final_figures/`
- Detailed verification note: `../report/lc1_lc2_lc3_lc4_lc4r_verification_report.md`
