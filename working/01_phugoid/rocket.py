from math import sin, cos, log, ceil
import numpy
from matplotlib import pyplot
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

import math
# model parameters:
g = 9.81        # gravity in m s^{-2}
ms = 50        # weight of the rocket shell
rho = 1.091    # air density
r = 0.5        # max radius of the rocket
A = math.pi*r**2 # max cross sectional area of the rocket
ve = 325       # exhaust speed
Cd = 0.15      # drag coefficient
mp0 = 100      # initial weight of the rocket propellent
mp_rate0 = 20  # popellent burn rate


### set initial conditions ###
t0 = 0  # initial time
h0 = 0.  # initial altitude
v0 = 0.  # initial velocity

def mp(t):
    '''Give the mass of remaining propellent'''
    mp_rem = 0.
    if (t<=5):
        mp_rem = mp0 - mp_rate0*t
    else:
        mp_rem = 0.
    return mp_rem

def mp_rate(t):
    '''Give the propellent burn rate'''
    return mp_rate0 if (t < 4.99) else 0.
    
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
    
    t = u[0]
    h = u[1]
    v = u[2]
    m_inv = 1./(ms+mp(t))

    return numpy.array([1,
                        v,
                        -g + m_inv*mp_rate(t)*ve - 0.5*m_inv*rho*v*abs(v)*A*Cd])
                                                                                        
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
                
T = 40.                             # final time
dt = 0.1                           # time increment
N = int(T/dt) + 1                  # number of time-steps
#t = numpy.linspace(0, T, N)        # time discretization

# initialize the array containing the solution for each time-step
u = numpy.zeros((N, 3))
u[0] = numpy.array([t0, h0, v0]) # fill 1st element with initial values

# time loop - Euler method
for n in range(N-1):   
    u[n+1] = euler_step(u[n], f, dt)

# get the glider's position with respect to the time
t = u[:,0]
h = u[:,1]
v = u[:,2]

#for i, qqq in enumerate(t):
#    print (t[i], h[i], v[i])
    
Vmax = max(v)
print ("Max velocity Vmax = {0} occurs in t = {1}".format(Vmax, 0.))

# visualization of the path
pyplot.figure(figsize=(6,5))
pyplot.grid(True)
pyplot.xlabel(r'time, s', fontsize=18)
pyplot.ylabel(r'h, m', fontsize=18)
pyplot.title('Rocket altitude, flight time = %.2f' % T, fontsize=18)
pyplot.plot(t,v, 'k-', lw=2);