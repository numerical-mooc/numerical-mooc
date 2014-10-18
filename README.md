#Practical Numerical Methods in Python

A multi-campus, connected course (plus MOOC) on numerical methods for differential equations in science and engineering. Collaboratively developed by:
- Lorena A. Barba, George Washington University, USA
- Ian Hawke, Southampton University, UK
- Carlos Jerez, Pontificia Universidad Catolica de Chile

**Note:** David Ketcheson, from King Abdullah University of Science and Technology (KAUST), Saudi Arabia was going to be our fourth partner, but unfortunately the local course at KAUST got cancelled due to low enrollment.

####Find the list of IPython Notebooks, with links to nbviewer, in the [Wiki](https://github.com/numerical-mooc/numerical-mooc/wiki).

##List of Modules

1. **The phugoid model of glider flight.**
Described by a set of two nonlinear ordinary differential equations, the phugoid model motivates numerical time integration methods, and we build it up starting from one simple equation, so that the unit can include 3 or 4 lessons  on initial value problems. This includes: a) Euler's method, 2nd-order RK, and leapfrog; b) consistency, convergence testing, local vs. global error; c) stability
Computational techniques: array operations with NumPy; symbolic computing with SymPy; ODE integrators and libraries; writing and using functions.
2. **Space and Time—Introduction to finite-difference solutions of PDEs.**
Starting with the simplest model represented by a partial differential equation (PDE)—the linear convection equation in one dimension—, this module builds the foundation of using finite differencing in PDEs. (The module is based on the “CFD Python” collection, steps 1 through 4.)  It also motivates CFL condition, numerical diffusion, accuracy of finite-difference approximations via Taylor series, consistency and stability, and the physical idea of conservation laws.
Computational techniques: more array operations with NumPy and symbolic computing with SymPy; getting high performance with Numba.
3. **Riding the wave: convection problems.**
Starting with the inviscid Burgers’ equation in conservation form and a 1D shock wave, cover a sampling of finite-difference convection schemes of various types: upwind, Lax-Friedrichs, Lax-Wendroff, MacCormack, then MUSCL (discussing limiters). Traffic-flow equation with MUSCL (from HyperPython). Reinforce concepts of numerical diffusion and stability, in the context of solutions with shocks.  It will motivate spectral analysis of schemes, dispersion errors, Gibbs phenomenon, conservative schemes.
4. **Spreading out: Parabolic PDEs.**
Start with heat equation in 2D (first introduction of two-dimensional FD discretization). Introduce implicit methods: backward Euler, trapezoidal rule (Crank-Nicolson), backward-differentiation formula (BDF). Pattern formation models (reaction-diffusion). Theory content: A-stability (unconditional stability), L-stability (?). Fourier spectral methods and splitting.
5. **Relax and hold steady: elliptic problems.**
Laplace and Poisson equations (steps 9 and 10 of “CFD Python”), explained as systems relaxing under the influence of the boundary conditions and the Laplace operator; introducing the idea of pseudo-time and iterative methods. Linear solvers for PDEs : Jacobi’s method, slow convergence of low-frequency modes (matrix analysis of Jacobi), Jacobi as a smoother, Multigrid.
6. **Boundaries take over: the boundary element method (BEM).**
Weak and boundary integral formulation of elliptic partial differential equations; the free space Green's function. Boundary discretization: basis functions; collocation and Galerkin systems. The BEM stiffness matrix: dense versus sparse;  matrix conditioning. Solving the BEM system: singular and near-singular integrals; Gauss quadrature integration.
7. **Tsunami: Shallow-water equation with finite volume method.**
1D first … 2D problem with HPC solution (Python parallel or CUDA Python) -- *optional*.

