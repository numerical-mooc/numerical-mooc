from math import sin, cos, log, ceil
import numpy
from matplotlib import pyplot
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

import math
# model parameters:
g = 9.8      # gravity in m s^{-2}
v_t = 4.9   # trim velocity in m s^{-1}   
C_D = 1/5  # drag coefficient --- or D/L if C_L=1
C_L = 1   # for convenience, use C_L = 1

### set initial conditions ###
v0 = 6.5  # start at the trim velocity (or add a delta)
#alpha0 = 0 # initil angle in degrees
#theta0 = alpha/180*math.pi # initial angle of trajectory (rad)
x0 = 0     # horizotal position is arbitrary
y0 = 2.0   # initial altitude

def f(u):
    """Returns the right-hand side of the phugoid system of equations.
    
    Parameters
    ----------
    u : array of float
        array containing the solution at time n.
        
    Returns
    -------
    dudt : array of float
        array containing the RHS given u.
    """
    
    v = u[0]
    theta = u[1]
    x = u[2]
    y = u[3]
    return numpy.array([-g*sin(theta) - C_D/C_L*g/v_t**2*v**2,
                        -g*cos(theta)/v + g/v_t**2*v,
                        v*cos(theta),
                        v*sin(theta)])
                                                                                        
def euler_step(u, f, dt):
    """Returns the solution at the next time-step using Euler's method.
    
    Parameters
    ----------
    u : array of float
        solution at the previous time-step.
    f : function
        function to compute the right hand-side of the system of equation.
    dt : float
        time-increment.
    
    Returns
    -------
    u_n_plus_1 : array of float
        approximate solution at the next time step.
    """
    
    return u + dt * f(u)

def dist(u):
    '''Returns distance of flight'''
    for d, h in u[:,2:4]:
        if h<0:
            return d
                
T = 5                            # final time
dt = 0.1                           # time increment
N = int(T/dt) + 1                  # number of time-steps
t = numpy.linspace(0, T, N)      # time discretization

alphas = numpy.arange(-30, 30, 1) # initial angle in deg
thetas = alphas/180*math.pi # initial angle in rad
dist_val = numpy.empty_like(alphas, dtype=float)

for i, theta0 in enumerate(thetas):
    # initialize the array containing the solution for each time-step
    u = numpy.zeros((N, 4))
    u[0] = numpy.array([v0, theta0, x0, y0])# fill 1st element with initial values

    # time loop - Euler method
    for n in range(N-1):   
        u[n+1] = euler_step(u[n], f, dt)
    dist_val[i] = dist(u)

# get the glider's position with respect to the time
#x = u[:,2]
#y = u[:,3]
x = alphas
y = dist_val
print (dist_val)

# visualization of the path
pyplot.figure(figsize=(6,5))
pyplot.grid(True)
pyplot.xlabel(r'x', fontsize=18)
pyplot.ylabel(r'y', fontsize=18)
pyplot.title('Glider trajectory, flight time = %.2f' % T, fontsize=18)
pyplot.plot(x,y, 'k-', lw=2);