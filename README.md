# Multivariable Newton-Raphson Method

A Python implementation of the multivariable Newton-Raphson method for solving two nonlinear polynomial equations with two variables.

This project was created to understand how the single-variable Newton-Raphson method can be extended to a multivariable system using partial derivatives and the Jacobian matrix.

## Features

- Supports two nonlinear polynomial equations in two variables
- Computes function values and partial derivatives directly from polynomial coefficients
- Constructs the Jacobian matrix at each iteration
- Solves the Newton step using `numpy.linalg.solve`
- Handles singular Jacobian matrices
- Stops when both function values are sufficiently close to zero
- Includes successful and failure test cases

## Method

For

```math
F(\mathbf{x})
=
\begin{bmatrix}
f_1(\mathbf{x}) \\
f_2(\mathbf{x})
\end{bmatrix},
```

the Newton step is obtained by solving

```math
J(\mathbf{x}_k)\boldsymbol{\delta}_k
=
F(\mathbf{x}_k),
```

and updating

```math
\mathbf{x}_{k+1}
=
\mathbf{x}_k-\boldsymbol{\delta}_k.
```

Instead of explicitly computing the inverse of the Jacobian matrix, the implementation solves the linear system directly using `numpy.linalg.solve`.

## Explore the Project

- 💻 [Source Code](code.py)  
  Main Python implementation of the multivariable Newton-Raphson method.

- 📘 [Project Overview](docs/project_overview.md)  
  Project motivation, problem setting, and the reason for focusing on two variables and two equations.

- 📐 [Mathematical Derivation](docs/derivation.md)  
  Derivation from the single-variable Newton-Raphson method to the multivariable formulation using tangent planes and the Jacobian matrix.

- 🧪 [Execution Results](docs/result.md)  
  Actual test cases including successful convergence, maximum-iteration termination, and singular Jacobian failure.

## Requirements

- Python
- NumPy

## Limitations

The Newton-Raphson method does not always converge.

Its behavior depends on the initial point, and the iteration may fail if a singular Jacobian matrix is encountered.
