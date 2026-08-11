# 1. Project Introduction

This project finds a point where two bivariate polynomial functions are both equal to zero.

In other words, I use the Newton-Raphson method to approximate $(x,y)$ satisfying

```math
f_1(x,y)=0
```

and

```math
f_2(x,y)=0.
```

## Why I Used Two Bivariate Polynomial Functions

First, let's think about a more general case with multiple variables.

Suppose there are $n$ variables and $m$ functions.

The variables can be written as

```math
\mathbf{x}
=
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}
```

and the functions can be written as

```math
F(\mathbf{x})
=
\begin{bmatrix}
f_1(\mathbf{x}) \\
f_2(\mathbf{x}) \\
\vdots \\
f_m(\mathbf{x})
\end{bmatrix}.
```

In the Newton-Raphson method, we approximate the functions around the current point $\mathbf{x}_k$. Then we get the linear system

```math
J(\mathbf{x}_k)\boldsymbol{\delta}_k
=
F(\mathbf{x}_k),
```

and update the point by

```math
\mathbf{x}_{k+1}
=
\mathbf{x}_k-\boldsymbol{\delta}_k.
```

The Jacobian matrix is

```math
J(\mathbf{x})
=
\begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix},
```

so its size is $m \times n$.

## 1. When $m>n$

If there are more functions than variables, the linear system has more equations than unknowns.

In this case, there may not be a $\boldsymbol{\delta}_k$ that satisfies every equation exactly. Depending on the equations, an exact solution can still exist.

If an exact solution does not exist, we can use the least-squares method and find a value that minimizes the error.

```math
\min_{\boldsymbol{\delta}}
\left\|
J(\mathbf{x}_k)\boldsymbol{\delta}
-
F(\mathbf{x}_k)
\right\|^2
```

## 2. When $m<n$

If there are fewer functions than variables, there can be multiple solutions.

The Newton-Raphson step

```math
J(\mathbf{x}_k)\boldsymbol{\delta}_k
=
F(\mathbf{x}_k)
```

may also have more than one possible $\boldsymbol{\delta}_k$.

In this case, we may need an additional condition to choose one of them.

## 3. When $m=n$

If the number of functions and variables is the same, the Jacobian becomes a square matrix.

```math
J(\mathbf{x}_k)
\in
\mathbb{R}^{n\times n}
```

If the Jacobian is invertible, then

```math
J(\mathbf{x}_k)\boldsymbol{\delta}_k
=
F(\mathbf{x}_k)
```

has a unique $\boldsymbol{\delta}_k$.

However, this does not mean that the Newton-Raphson method always works. If the Jacobian is singular at the current point,

```math
\det J(\mathbf{x}_k)=0,
```

the Newton step cannot be uniquely determined.

For this project, I chose the basic case where the number of variables and functions is the same. More specifically, I used **two variables and two bivariate polynomial functions**.
