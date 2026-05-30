# Assumptions and Limitations

| ID | Assumption | Why used | Risk | How reported |
|---|---|---|---|---|
| A1 | Generic geometry | Avoid proprietary design | Not a real component | State as portfolio model |
| A2 | Linear elastic material | One-week scope | No plasticity captured | Mention as limitation |
| A3 | Fixed mounting holes | Simple support representation | May over-constrain model | Discuss as conservative stiffness assumption |
| A4 | No bolt preload/contact | Scope control | Local stress may be unrealistic | Future work |
| A5 | No fatigue/seismic | Scope control | Not code-complete | Future work |
| A6 | Simplified allowable stress | ASME-aware only | Not ASME compliant | Explicit disclaimer |

## Disclaimer

This project is an ASME-aware educational portfolio study, not an ASME BPVC-compliant design calculation. It uses simplified geometry, conservative material assumptions, fixed support boundary conditions and linear elastic analysis to demonstrate a structural FEM workflow. It does not include formal ASME stress categorization, certified material data, fatigue, seismic loading, irradiation effects, welds, bolt preload, nonlinear plasticity, manufacturing tolerances or nuclear qualification.