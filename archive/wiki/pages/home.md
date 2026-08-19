# Welcome to NumericalMOOC!

This repository is the core of the [**"Practical Numerical Methods with Python**](practical-numerical-methods-with-python.md) course. Each course module consists of a set of IPython Notebooks (linked below within this archived repository), practice exercises and a coding assignment. 

## What is this course about?

In this course we aim to help you build a foundation for **scientific computing**.

We use computers every day: to communicate and connect with each other, to entertain ourselves, to check our bank account and for online shopping. But _scientific computing is a special way of using computers_, one that gives you lots of power to be creative and inventive. We love it—it’s challenging but fun.

Scientific computing is essential in any profession of science and technology; it’s a key tool. More than a tool, it is a way of thinking, and the _language of computing_ is as necessary for your success as the language of mathematics.

## What do we mean by "numerical methods"?

Numerical Methods are the ways in which we make problems _computable_ by a machine that operates with numbers (a computer). Much of our scientific knowledge—especially in the physical sciences—is expressed in the language of mathematics. 

Mathematics is really the way into nature’s heart. But mathematics is more about _ideas_ and _symbols_ than it is about numbers. In our minds, we can manipulate ideas and symbols, but in a computer, we just need numbers.

Numerical methods are the translators between the ideal world of mathematics and the numbers world of computers.

## What do we mean by "practical"?

Often, a numerical methods course will cover the various discretization schemes, like a recipe book, and talk about the analysis of methods (consistency, stability, convergence) via "chalk-and-talk" lectures. Sometimes there are homework problems that ask you to apply more analysis, and perhaps a final project where you finally get to program numerical solutions. And guess what, by that time, most of the semester is over and you're thrown in the deep end.

We call this course "Practical Numerical Methods with Python" because we'll get you coding numerical solutions right away, and we aim for you to develop _numerical literacy_. This doesn't mean we ignore the theory, but we discuss the theory when and as you experience the behavior of different solutions, and see the relevance.

In the on-campus courses, we use a "blended learning" model, and emphasize programming practice during class meetings.

When you finish this course, we want you to be confident that you can continue teaching yourself numerical methods, as and when you need to, and apply them to solve problems.

## Module 0: Getting Started.
**How is this course going to work?**

1. [What to expect from the instructors](what-to-expect-from-the-instructors.md)
2. [What is expected of you](what-is-expected-of-you.md)
3. [The idea of connected courses](the-idea-of-connected-courses-2014.md)


## Module 1: The phugoid model.

1. [Phugoid motion](../../../lessons/01_phugoid/01_01_Phugoid_Theory.ipynb)
1. [Phugoid oscillation](../../../lessons/01_phugoid/01_02_Phugoid_Oscillation.ipynb)
1. [Full phugoid model](../../../lessons/01_phugoid/01_03_PhugoidFullModel.ipynb)
1. [Bonus! Second-order and multi-step methods](../../../lessons/01_phugoid/01_04_Second_Order_Methods.ipynb)

## Module 2: Space and Time
**Introduction to finite-difference solutions of PDEs**

1. [1D linear and nonlinear convection](../../../lessons/02_spacetime/02_01_1DConvection.ipynb)
1. [CFL condition](../../../lessons/02_spacetime/02_02_CFLCondition.ipynb)
1. [Diffusion equation in 1D](../../../lessons/02_spacetime/02_03_1DDiffusion.ipynb)
1. [Burgers' equation](../../../lessons/02_spacetime/02_04_1DBurgers.ipynb)

## Module 3: Riding the wave
**Convection problems**

1. [Conservation laws and the traffic-flow problem](../../../lessons/03_wave/03_01_conservationLaw.ipynb)
1. [Numerical schemes for hyperbolic PDEs](../../../lessons/03_wave/03_02_convectionSchemes.ipynb)
1. [A better flux model](../../../lessons/03_wave/03_03_aBetterModel.ipynb)
1. [Finite volume and MUSCL methods.](../../../lessons/03_wave/03_04_MUSCL.ipynb)
1. [Assignment: Sod's test problems](../../../lessons/03_wave/03_05_Sods_Shock_Tube.ipynb)

## Module 4: Spreading out
**Diffusion problems**

1. [Diffusion equation in 1D and boundary conditions](../../../lessons/04_spreadout/04_01_Heat_Equation_1D_Explicit.ipynb)
1. [Implicit schemes in 1D and boundary conditions](../../../lessons/04_spreadout/04_02_Heat_Equation_1D_Implicit.ipynb)
1. [2D heat (diffusion) equation with explicit scheme](../../../lessons/04_spreadout/04_03_Heat_Equation_2D_Explicit.ipynb)
1. [2D heat equation with implicit scheme, and applying boundary conditions](../../../lessons/04_spreadout/04_04_Heat_Equation_2D_Implicit.ipynb)
1. [Crank-Nicolson scheme and spatial & time convergence study](../../../lessons/04_spreadout/04_05_Crank-Nicolson.ipynb)
1. [Assignment: Reaction-diffusion with the Gray-Scott model in 2D](../../../lessons/04_spreadout/04_06_Reaction_Diffusion.ipynb)

## Module 5: Relax and hold steady
**Elliptic problems**

1. [2D Laplace equation with Jacobi iterations](../../../lessons/05_relax/05_01_2D.Laplace.Equation.ipynb)
1. [2D Poisson equation with Jacobi, and algebraic convergence](../../../lessons/05_relax/05_02_2D.Poisson.Equation.ipynb)
1. [Gauss-Seidel, successive over-relaxation (SOR) and tuned SOR, introducing Numba](../../../lessons/05_relax/05_03_Iterate.This.ipynb)
1. [The conjugate gradient method](../../../lessons/05_relax/05_04_Conjugate.Gradient.ipynb)
1. [Assignment: Stokes flow in vorticity-streamfunction formulation](../../../lessons/05_relax/05_05_Stokes.Flow.ipynb)
