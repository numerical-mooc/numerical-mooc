# Module 1: The phugoid model of glider flight.

## Summary

The phugoid model motivates the learning of numerical time integration methods. The model is described by a set of two nonlinear ordinary differential equations, representing the oscillatory trajectory of an aircraft subject to longitudinal perturbations.

* [Lesson 1](http://nbviewer.ipython.org/github/numerical-mooc/numerical-mooc/blob/master/lessons/01_phugoid/01_01_Phugoid_Theory.ipynb) presents the physics of phugoids in the assumption of zero drag (following Lanchester, 1909). Plotting the flight path gives fascinating curve shapes. 
* [Lesson 2](http://nbviewer.ipython.org/github/numerical-mooc/numerical-mooc/blob/master/lessons/01_phugoid/01_02_Phugoid_Oscillation.ipynb) develops a single-equation model for zero-drag oscillations, leading to simple harmonic motion. The lesson defines initial-value problems, demonstrates Euler's method, and uses the exact solution to study the numerical convergence. 
* [Lesson 3](http://nbviewer.ipython.org/github/numerical-mooc/numerical-mooc/blob/master/lessons/01_phugoid/01_03_PhugoidFullModel.ipynb) develops the full phugoid model and solves it with (vectorized) Euler's method. In the absence of an exact solution, the study of convergence uses a grid-refinement method, obtaining the observed order of convergence. The lesson ends with the paper-airplane challenge.
* [Lesson 4](http://nbviewer.ipython.org/github/numerical-mooc/numerical-mooc/blob/master/lessons/01_phugoid/01_04_Second_Order_Methods.ipynb) starts with the screencast "Euler's method is a first-order method" and develops second-order methods: explicit midpoint (modified Euler) and Runge-Kutta. It ends with a grid-refinement study.

## Badge earning

Completion of this module in the online course platform can earn the learner the Module 1 badge.

### Description: What does this badge represent?

The earner completed Module 1 "The phugoid model of glider flight" of the course "Practical Numerical Methods with Python" (a.k.a., numericalmooc). 

### Criteria: What needs to be done to earn it?

To earn this badge, the learner needs to complete the graded assessment in the course platform including: answering quiz about basic numerical Python commands; answering quiz about basics of initial-value problems; completing the individual coding assignment "Rocket flight" and answering the numeric questions online. Earners should also have completed self-study of the four module lessons, by reading, reflecting on and writing their own version of the codes. This is not directly assessed, but it is assumed. Thus, earners are encouraged to provide evidence of this self-study by giving links to their code repositories or other learning objects they created in the process.

### Evidence: Website (link to original digital content)

Desirable: link to the earner's GitHub repository (or equivalent) containing the solution to the "Rocket flight" coding assignment.
Optional: link to the earner's GitHub repository (or equivalent)  containing other codes, following the lesson.

### Category: 

Higher education, graduate

### Tags: 

engineering, computation, higher education, numericalmooc, python, gwu, george washington university, lorena barba, github

### Relevant Links: Is there more information on the web?

[Course About page](http://openedx.seas.gwu.edu/courses/GW/MAE6286/2014_fall/about)

[Course Wiki](http://openedx.seas.gwu.edu/courses/GW/MAE6286/2014_fall/wiki/GW.MAE6286.2014_fall/)

[Course GitHub repo](https://github.com/numerical-mooc/numerical-mooc)
