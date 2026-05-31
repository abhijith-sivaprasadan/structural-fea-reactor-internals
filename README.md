# ANSYS Mechanical Pilot Study: Structural Integrity, Mesh Convergence, and Thermal Expansion Behaviour of a Stainless-Steel Support Plate

## Purpose

This project demonstrates a structural integrity screening workflow in ANSYS Mechanical for a simplified reactor-internals-inspired stainless-steel support plate.

## Disclaimer

This is an educational portfolio project. It is not an ASME BPVC-compliant design calculation and does not represent certified nuclear component design.

## Tools

- ANSYS Mechanical Student
- ANSYS SpaceClaim
- Python
- pandas
- matplotlib

## Model

The model is a simplified stainless-steel support plate with:
- central guide opening
- four mounting holes
- mechanical load cases
- thermal expansion sensitivity case

## Planned Workflow

1. Geometry creation
2. Material definition
3. Boundary condition setup
4. Static structural solution
5. Mesh convergence
6. Result export
7. Python post-processing
8. Report generation

## Load Cases

| Load Case | Description |
|---|---|
| LC1 | 2 kN lateral load - complete |
| LC2 | 5 kN lateral load - complete |
| LC3 | 3 kN lateral + 2 kN vertical - complete |
| LC4 | +100 C constrained thermal expansion sensitivity - complete |
| LC4R | +100 C relaxed thermal expansion check - complete |

## Status

LC1 setup, solution evidence, mesh convergence notes and Python post-processing are in place. LC2 fine-mesh results are recorded and verified as a clean linear scaling case from LC1. LC3 fine-mesh results are recorded with vector force-balance checks. LC4 is recorded as a constrained thermal expansion sensitivity case with boundary-condition-sensitive peak stresses. LC4R is recorded as the realistic relaxed thermal expansion check.

Current portfolio artifacts:
- Geometry notes: `geometry/geometry_notes.md`
- Assumptions and limitations: `docs/assumptions_and_limitations.md`
- LC1 mesh convergence notes: `docs/lc1_mesh_convergence_notes.md`
- LC2 linear static notes: `docs/lc2_linear_static_notes.md`
- LC3 combined load notes: `docs/lc3_combined_load_notes.md`
- LC4 constrained thermal notes: `docs/lc4_constrained_thermal_notes.md`
- LC4R relaxed thermal notes: `docs/lc4r_relaxed_thermal_notes.md`
- Final model freeze: `docs/final_model_freeze.md`
- Acceptance criteria and checks: `docs/acceptance_criteria_and_checks.md`
- Design recommendations: `docs/design_recommendations.md`
- Raw exported LC1 convergence data: `ansys/exported_results/mesh_convergence_raw.csv`
- Fine-mesh load case summary: `ansys/exported_results/load_case_summary.csv`
- Final report figures: `ansys/exported_results/final_figures/`
- Python post-processing: `scripts/postprocess_mesh_convergence.py`
- Generated load-case summary outputs: `results/`
- Final reporting values: `results/final_reporting_values.md`
- Safety factor summary: `results/safety_factor_summary.md`
- Draft verification report: `report/final_structural_fem_report.md`

To regenerate the post-processing outputs:

```bash
python scripts/postprocess_mesh_convergence.py
```
