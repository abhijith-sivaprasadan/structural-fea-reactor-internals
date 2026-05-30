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
| LC1 | 2 kN lateral load |
| LC2 | 5 kN lateral load |
| LC3 | 3 kN lateral + 2 kN vertical |
| LC4 | +100°C thermal expansion sensitivity |

## Status

Project setup started.