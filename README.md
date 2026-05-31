# ASME-Aware Structural FEM Study of a Simplified Reactor-Internal Support Component

## Purpose

This project demonstrates a junior-level structural FEM workflow in ANSYS Mechanical for a simplified reactor-internals-inspired support component.

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
| LC4 | +100°C thermal expansion sensitivity |

## Status

LC1 setup, solution evidence, mesh convergence notes and Python post-processing are in place. LC2 fine-mesh results are recorded and verified as a clean linear scaling case from LC1. LC3 fine-mesh results are recorded with vector force-balance checks. LC4 remains a planned follow-on case.

Current portfolio artifacts:
- Geometry notes: `geometry/geometry_notes.md`
- Assumptions and limitations: `docs/assumptions_and_limitations.md`
- LC1 mesh convergence notes: `docs/lc1_mesh_convergence_notes.md`
- LC2 linear static notes: `docs/lc2_linear_static_notes.md`
- LC3 combined load notes: `docs/lc3_combined_load_notes.md`
- Raw exported LC1 convergence data: `ansys/exported_results/mesh_convergence_raw.csv`
- Fine-mesh load case summary: `ansys/exported_results/load_case_summary.csv`
- Python post-processing: `scripts/postprocess_mesh_convergence.py`
- Generated LC1 and LC2 summary outputs: `results/`
- Draft verification report: `report/lc1_lc2_lc3_verification_report.md`

To regenerate the post-processing outputs:

```bash
python scripts/postprocess_mesh_convergence.py
```
