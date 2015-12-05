#Module 5:
## Relax and hold steady: elliptic problems
## Summary
This course module is dedicated to the solution of elliptic PDS, like the Laplace and Poisson equations.
These equations have no time dependence and the solutions can be found by iterative schemes, where an 
initial guess is relaxed to the steady-state solution.

* [Lesson 1] introduces the five-point discrete Laplace operator and the Jacobi method. We solve a 2D Laplace problem
with both Dirichlet and Neumann boundary conditions. Via a spatial grid-convergence analysis, we show that the Neumann
boundary conditions needs a second-order difference approximation to get second-order spatial convergence throughout.

* [Lesson 2] is dedicated to the Poisson equation: we see the effect of having internal souces with an elliptic equation.

* In [lesson 3] we improve on the Jacobi method: we look at Gauss-Seidel and successive over-relaxation (SOR) schemes.
We also learn about Numba, an optimizing compiler that gives us high performance in Python.

* [Lesson 4] focuses on the conjugate gradient (CG) method.
