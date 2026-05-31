# Acceptance Criteria And Verification Checks

## Objective

The objective of this study is to evaluate whether a stainless-steel support plate can safely withstand representative lateral, vertical, combined and thermal expansion loading while maintaining low deformation and acceptable stress levels. The study also compares idealized and realistic thermal boundary conditions to show the effect of overconstraint on thermal stress prediction.

This is an ASME-inspired preliminary screening, not a certified ASME BPVC assessment.

## Screening Criteria

| Quantity | Criterion | How checked |
|---|---|---|
| Max von Mises stress | Must be below the preliminary yield-strength screen | Compare max von Mises stress to an assumed 205 MPa yield strength for annealed 316 stainless steel |
| Max deformation | Must remain small relative to component size and support function | Review displacement magnitude and deformation pattern |
| Reaction force | Must balance applied mechanical load | Compare ANSYS reaction resultant with applied load resultant |
| Mesh convergence | Final mesh result should be reasonably stable | LC1 coarse/medium/fine/very-fine convergence study |
| Thermal stress | Must be interpreted based on constraint realism | Compare LC4 fixed-hole thermal case with LC4R relaxed thermal expansion case |

## Preliminary Stress Screening

The safety factor table uses 205 MPa as a preliminary yield-strength screening value for annealed 316 stainless steel. If the ANSYS/GRANTA material card used in the model lists a different yield value, the table should be updated to use that exact value.

The LC4 constrained thermal peak is excluded from design screening because it is a boundary-condition-sensitive over-constraint artifact.

## Hand / Sanity Checks

### LC2 Load Scaling

LC2 increases the LC1 lateral load from 2,000 N to 5,000 N.

```text
Load ratio = 5000 / 2000 = 2.5
Displacement ratio = 0.00091514 / 0.00036606 = 2.500
```

The displacement response scales almost exactly with the applied lateral load, indicating that the model remains in the expected linear elastic range.

### LC3 Reaction Force

LC3 applies a combined load vector of `[3000, 2000, 0]` N.

```text
Expected resultant = sqrt(3000^2 + 2000^2) = 3605.5 N
ANSYS reaction resultant = 3605.6 N
```

The reaction balance is effectively exact for the current model.

## Boundary-Condition Sensitivity

| Case | Boundary condition | Result behavior | Interpretation |
|---|---|---|---|
| LC1-LC3 mechanical | Fixed mounting-hole cylindrical faces | Low deformation, local hole/fillet stress concentration | Conservative support idealization for mechanical loads |
| LC4 thermal | Fully fixed mounting holes under uniform +100 C | Unrealistically high thermal stress | Useful over-constraint comparison only |
| LC4R thermal | 3-2-1 locating/sliding support | Realistic expansion, negligible thermal stress | Final thermal expansion representation |

Thermal stress is not caused by temperature alone. It is caused by restrained thermal expansion. LC4R shows that when thermal growth is allowed, the stress collapses to near zero.
