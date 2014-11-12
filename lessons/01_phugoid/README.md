#Module 1: The phugoid model of glider flight.

##Summary

The phugoid model motivates the learning of numerical time integration methods. The model is described by a set of two nonlinear ordinary differential equations, representing the oscillatory trajectory of an aircraft subject to longitudinal perturbations.

Lesson 1 presents the physics of phugoids in the assumption of zero drag (following Lanchester, 1909). Plotting the flight path gives fascinating curve shapes. 
Lesson 2 develops a single-equation model for zero-drag oscillations, leading to simple harmonic motion. The lesson defines initial-value problems, demonstrates Euler's method, and uses the exact solution to study the numerical convergence. 
Lesson 3 develops the full phugoid model and solves it with (vectorized) Euler's method. In the absence of an exact solution, the study of convergence uses a grid-refinement method, obtaining the observed order of convergence. The lesson ends with the paper-airplane challenge.
Lesson 4 starts with the screencast "Euler's method is a first-order method" and develops second-order methods: explicity midpoint (modified Euler) and Runge-Kutta. It ends with a grid-refinement study.
