# Module 3:
## Riding the wave: convection problems

## Summary

This module explores in depth the solution of transport problems and conservation laws using numerical methods.

* [Lesson 1](http://nbviewer.ipython.org/github/numerical-mooc/numerical-mooc/blob/master/lessons/03_wave/03_01_conservationLaw.ipynb) discusses the meaning and mathematical representation of a conservation law. 
The application that will motivate this module is traffic flow, and it is described here.
The first problem to tackle is the impulsive start of traffic upon a red light turning green.
But instability develops wiith the simple forward-time/backward-space scheme: we need upwind methods.

* [Lesson 2](http://nbviewer.ipython.org/github/numerical-mooc/numerical-mooc/blob/master/lessons/03_wave/03_02_convectionSchemes.ipynb) moves on to a red-light problem, creating a back-moving shock wave. The lesson explores different numerical schemes:
Lax-Friedrichs, Lax-Wendroff and MacCormack.

* [Lesson 3](http://nbviewer.ipython.org/github/numerical-mooc/numerical-mooc/blob/master/lessons/03_wave/03_03_aBetterModel.ipynb) focuses on an improved model for traffic flow, requiring symbolic calculations (with SymPy).

* [Lesson 4](http://nbviewer.ipython.org/github/numerical-mooc/numerical-mooc/blob/master/lessons/03_wave/03_04_MUSCL.ipynb) is an introduction to the finite-volume method, including study of the conservative discretization, Godunov's method and the MUSCL method.

## Badge earning
Completion of this module in the online course platform can earn the learner the Module 3 badge.

### Description: What does this badge represent?
The earner completed Module 3 of the course "Practical Numerical Methods with Python" (a.k.a., numericalmooc).

### Criteria: What needs to be done to earn it?
To earn this badge, the learner needs to complete the graded assessment in the course platform including: 
answering quiz questions involving symbolic calculations with the improved traffic model, and additional SymPy practice;
answering quiz questions on convergence and truncation error; 
completing the individual coding assignment using "Sod's shock-tube" problem and answering the numeric questions online.
Earners should also have completed self-study of the four module lessons, by reading, reflecting on and writing their own version of the codes. This is not directly assessed, but it is assumed. Thus, earners are encouraged to provide evidence of this self-study by giving links to their code repositories or other learning objects they created in the process.

### Evidence: Website (link to original digital content)
Desirable: link to the earner's GitHub repository (or equivalent) containing the solution to the "Sod's shock-tube" coding assignment. Optional: link to the earner's GitHub repository (or equivalent) containing other codes, following the lesson.

### Category:
Higher education, graduate

### Tags:
engineering, computation, higher education, numericalmooc, python, gwu, george washington university, lorena barba, github

### Relevant Links: Is there more information on the web?

[Course About page](http://openedx.seas.gwu.edu/courses/GW/MAE6286/2014_fall/about)

[Course wiki](http://openedx.seas.gwu.edu/courses/GW/MAE6286/2014_fall/wiki/GW.MAE6286.2014_fall/)

[Course GitHub repo](https://github.com/numerical-mooc/numerical-mooc)
