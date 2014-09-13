from math import sin, cos, log, ceil
import numpy 
import matplotlib.pyplot as plt
%matplotlib inline 
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

# Next part of code
# Model Parameters
g = 9.8 #gravity m/s^2
v_t = 4.9 #trim velocity m/s 
C_D = 1/5.0 #drag coefficient 1/(L/D)
C_L = 1.0 #lift coefficient

### Set intitial conditions ###
v0 = v_t # Start at the trim velocity
theta0 = 0.0 #initial angle of trajectory
x0 = 0.0 #horizontal position at start
y0 = 2.5 # initial altitude

#Next part of code
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
    return numpy.array([-g*sin(theta)-C_D/C_L*g/v_t**2*v**2,
                        -g*cos(theta)/v+g/v_t**2*v,
                        v*cos(theta),
                        v*sin(theta)])

#Next part of code
def euler_step(u,f,dt):
    """Returns the solution at the next time step using Euler's method.
    
    Parameters
    ----------
    u: array of float
    solution at the previous time-step
    f: function
    function to compute the right hand-side of the system of equation.
    dt: float
    time-increment.
    
    Returns
    -------
    u_n_plus_s : array of float
        approximate solution at the next time-step.
    """
    
    return u + dt * f(u)
    
#Next part of code
T = 100.0                       #final time
dt = 0.1                        #time increment
N = int(T/dt) + 1               #number of time steps
t = numpy.linspace(0.0,T,N)     #time discretization

#initialize the array containing the solution for each time-step
u = numpy.empty((N,4))
u[0] = numpy.array([v0,theta0,x0,y0])  #fill 1st element with initial values

# time loop - Euler method
for n in range(N-1):
    
    u[n+1] = euler_step(u[n], f, dt)
    
#6
#get the glider's position with respect to the time
x = u[:,2]
y = u[:,3]

#7
#visualization of the path
plt.figure(figsize = (8,6))
plt.grid(True)
plt.xlabel(r'x',fontsize = 18)
plt.ylabel(r'y',fontsize = 18)
plt.title('Glider trajectory, flight time = %.2f'%T, fontsize = 18)
plt.plot(x,y,'k-',lw = 2);














