# Module 5:
## Relax and hold steady: elliptic problems
## Summary
This course module is dedicated to the solution of elliptic PDS, like the Laplace and Poisson equations.
These equations have no time dependence and the solutions can be found by iterative schemes, where an 
initial guess is relaxed to the steady-state solution.

* [Lesson 1](http://nbviewer.ipython.org/github/numerical-mooc/numerical-mooc/blob/master/lessons/05_relax/05_01_2D.Laplace.Equation.ipynb) 
introduces the five-point discrete Laplace operator and the Jacobi method. We solve a 2D Laplace problem
with both Dirichlet and Neumann boundary conditions. Via a spatial grid-convergence analysis, we find that the Neumann
boundary conditions needs a second-order difference approximation to get second-order spatial convergence throughout.

* [Lesson 2](http://nbviewer.ipython.org/github/numerical-mooc/numerical-mooc/blob/master/lessons/05_relax/05_02_2D.Poisson.Equation.ipynb) 
is dedicated to the Poisson equation: we see the effect of having internal sources with an elliptic equation.
We also learn about algebraic convergence of iterative methods and protest at how slow the Jacobi method is.

* In [lesson 3](http://nbviewer.ipython.org/github/numerical-mooc/numerical-mooc/blob/master/lessons/05_relax/05_03_Iterate.This.ipynb) 
we improve on the Jacobi method: we look at Gauss-Seidel and successive over-relaxation (SOR) schemes.
We also learn about **Numba**, an optimizing compiler that gives us high performance in Python.

* [Lesson 4](http://nbviewer.ipython.org/github/numerical-mooc/numerical-mooc/blob/master/lessons/05_relax/05_04_Conjugate.Gradient.ipynb) 
focuses on the conjugate gradient (CG) method, perhaps the most popular iterative method.

* The [Coding Assignment](http://nbviewer.ipython.org/github/numerical-mooc/numerical-mooc/blob/master/lessons/05_relax/05_05_Stokes.Flow.ipynb)
for Module 5 consists of solving the Stokes equation for flow in a square cavity at very low Reynolds number.
