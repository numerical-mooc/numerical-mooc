#Practical Numerical Methods with Python

This project started in 2014 as a multi-campus, connected course (plus MOOC) on numerical methods for science and engineering. 

In Fall 2015, the second run of the connected courses, we have these instructors participating:
- [Lorena A. Barba](http://lorenabarba.com), George Washington University, USA
- [Ian Hawke](http://www.southampton.ac.uk/maths/about/staff/ih3.page), Southampton University, UK
- [Bernard Knaepen](http://depphys.ulb.ac.be/bknaepen/), Université Libre de Bruxelles, Belgium


[**"Practical Numerical Methods with Python"**](http://openedx.seas.gwu.edu/courses/GW/MAE6286/2014_fall/about) is an open, online course hosted on an independent installation of the [Open edX](http://code.edx.org) software platform for MOOCs.
The MOOC (massive open online course) was run in 2014 for the first time by Prof. Barba at the George Washington University. At the same time, two other participating instructors ran a local course, for credit at their institution. 

###Update for 2015

The synchronous course at the George Washington University will run again, starting September 1st, 2015. In addition, there will be a **new site for numericalmooc!**

- [Bernard Knaepen](http://depphys.ulb.ac.be/bknaepen/), Physics Department, Université Libre de Bruxelles
 
Prof. Knaepen will be teaching his numerical methods class at ULB, adopting the numericalmooc materials and creating new content.

### The MOOC

You can register for the MOOC at any time in the [GW Online Open edX](http://openedx.seas.gwu.edu/) platform to experience the complete course (including quizzes, examples and discussion board). 

All content is open —really open, i.e., you can use, share, mod, remix— and most is available outside the course platform also (on GitHub and YouTube).

####Find the list of IPython Notebooks, with links to nbviewer, in the [Wiki](https://github.com/numerical-mooc/numerical-mooc/wiki).

##Course Modules

1. [**The phugoid model of glider flight.**](https://github.com/numerical-mooc/numerical-mooc/tree/master/lessons/01_phugoid)
Described by a set of two nonlinear ordinary differential equations, the phugoid model motivates numerical time integration methods, and we build it up starting from one simple equation, so that the unit can include 3 or 4 lessons  on initial value problems. This includes: a) Euler's method, 2nd-order RK, and leapfrog; b) consistency, convergence testing; c) stability
Computational techniques: array operations with NumPy; symbolic computing with SymPy; ODE integrators and libraries; writing and using functions.
2. [**Space and Time—Introduction to finite-difference solutions of PDEs.**](https://github.com/numerical-mooc/numerical-mooc/tree/master/lessons/02_spacetime)
Starting with the simplest model represented by a partial differential equation (PDE)—the linear convection equation in one dimension—, this module builds the foundation of using finite differencing in PDEs. (The module is based on the “CFD Python” collection, steps 1 through 4.)  It also motivates CFL condition, numerical diffusion, accuracy of finite-difference approximations via Taylor series, consistency and stability, and the physical idea of conservation laws.
Computational techniques: more array operations with NumPy and symbolic computing with SymPy; getting better performance with NumPy array operations.
3. [**Riding the wave: convection problems.**](https://github.com/numerical-mooc/numerical-mooc/tree/master/lessons/03_wave)
Starting with an overview of the concept of conservation laws, this module uses the traffic-flow model to study different solutions methods for problems with shocks: upwind, Lax-Friedrichs, Lax-Wendroff, MacCormack, then MUSCL (discussing limiters). Reinforces concepts of numerical diffusion and stability, in the context of solutions with shocks.  It will motivate spectral analysis of schemes, dispersion errors, Gibbs phenomenon, conservative schemes.
4. [**Spreading out: diffusion problems.**](https://github.com/numerical-mooc/numerical-mooc/tree/master/lessons/04_spreadout)
This module deals with solutions to parabolic PDEs, exemplified by the diffusion (heat) equation. Starting with the 1D heat equation, we learn the details of implementing boundary conditions and are introduced to implicit schemes for the first time. Another first in this module is the solution of a two-dimensional problem. The 2D heat equation is solved with both explicit and implict schemes, each time taking special care with boundary conditions. The final lesson builds solutions with a Crank-Nicolson scheme. 
5. [**Relax and hold steady: elliptic problems.**](https://github.com/numerical-mooc/numerical-mooc/tree/master/lessons/05_relax)
Laplace and Poisson equations (steps 9 and 10 of “CFD Python”), seen as systems relaxing under the influence of the boundary conditions and the Laplace operator. Iterative methods for algebraic equations resulting from discretizign PDEx: Jacobi method, Gauss-Seidel and successive over-relaxation methods. Conjugate gradient methods.
6. **Perform like a pro: making your codes run faster**
Getting performance out of your numerical Python codes with just-in-time compilation, targeting GPUs with Numba and PyCUDA.

Planned module (not yet started):
- **Boundaries take over: the boundary element method (BEM).**
Weak and boundary integral formulation of elliptic partial differential equations; the free space Green's function. Boundary discretization: basis functions; collocation and Galerkin systems. The BEM stiffness matrix: dense versus sparse;  matrix conditioning. Solving the BEM system: singular and near-singular integrals; Gauss quadrature integration.


