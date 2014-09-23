#Christopher Bell
#01-03 Full Phugoid Motion Model
#derivation of equations can be found in class notebook
#section 01-03 Full Phugoid Model aka w/ drag (01-02 = no drag)

from math import sin, cos, log, ceil
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family']= 'serif'
rcParams['font.size']= 16

# Constants
g = 9.81 # m/s2
v_t = 30.0 #trim velocity m/s
C_D = 1/40.0
C_L = 1.0

#IC's
v_0 = v_t
theta_0 = 0.0
x_0 = 0
y_0 = 1000.0

#need to solve right hand side of ode's aka f(u) matrix

def f(u):
    """Returns RHS of the phugoid system of equations.
    
    Params
    ------
    u: array of float
       array containing the solution at time n
       
    Returns
    ------
    dudt: array of float
        array containing RHS from given u
    """
    
    #define locations of inputs in u matrix
    v = u[0]
    theta = u[1]
    x = u[2]
    y = u[3]
    
    return np.array([-g*sin(theta) - (C_D/C_L)*(g/(v_t**2))*v**2,\
    (-g*cos(theta))/v + (g/(v_t**2))*v, v*cos(theta), v*sin(theta)])
    
#implement a eulerian time stepping function

def euler_step(u, f, dt):
    """Returns solution of input function for the next time-step using Euler's method
    
    Params
    ------
    u : array of float
        solution at the previous time-step
    f : function
        fucntion to copute the RHS of the system of equations
    dt : float
        time-increment.
        
    Returns
    ------
    u_n_plus_1: array of float
        approxiamte solution at the next time step.
    """
    
    return u + dt * f(u)
    
#time stepping set-up

T = 100.0   #end time
dt = 0.1    #time step size
N = int(T/dt) + 1 #total time steps

#solution array
u = np.empty((N,4)) #made an empty array N,4 because 4 variables n steps
u[0] = np.array([v_0, theta_0, x_0, y_0]) #IC's

#time step using euler
for n in range(N-1): #N-1 because already have initial step
    
    u[n+1] = euler_step(u[n], f, dt)
    
#plot
#grab all x and y values
x = u[:,2]
y = u[:,3]

plt.figure
plt.grid(True)
plt.xlabel(r'x', fontsize=18)
plt.ylabel(r'y', fontsize=18)
plt.title('Glider Trajectory, flight time = %.2f' % T, fontsize=18)
plt.plot(x,y, 'k-', lw=2);
plt.show()

##Check convergence using different grid sizes
dt_values = np.array([0.1, 0.05, 0.01, 0.005, 0.001])

u_values = np.empty_like(dt_values, dtype=np.ndarray)

for i, dt in enumerate(dt_values):
    
    N = int(T/dt) + 1
    t = np.linspace(0.0, T, N)
    
    u = np.empty((N, 4))
    u[0] = np.array([v_0, theta_0, x_0, y_0])
    
    for n in range(N-1):
        
        u[n+1] = euler_step(u[n], f, dt)
    
    u_values[i] = u
    
## find differences between different grids

def get_diffgrid(u_current, u_fine, dt):
    """Returns the difference between one grid and the fine grid using L-1 norm
    
    Params:
    ------
    u_current : array of float
        solution on the current grid.
    u_finest : array of float
        solution on the fine grid.
    dt : float
        time-increment on the current grid.
        
    Returns
    -------
    diffgrid : float
        difference computed in the L-1 norm
    """
    
    N_current = len(u_current[:,0])
    N_fine = len(u_fine[:,0])
    
    grid_size_ratio = ceil(N_fine/float(N_current))
    
    diffgrid = dt * np.sum(np.abs(u_current[:,2] - u_fine[::grid_size_ratio,2]))
    
    return diffgrid

# Compute actual grid differences

diffgrid = np.empty_like(dt_values)

for i, dt in enumerate(dt_values):
    print('dt = {}'.format(dt))
    
    diffgrid[i] = get_diffgrid(u_values[i], u_values[-1], dt)

#log log plot of the grid differences
plt.figure(figsize=(6,6))
plt.grid(True)
plt.xlabel('$\Delta t$', fontsize=18)
plt.ylabel('$L_1$-norm of the grid differences', fontsize=18)
plt.axis('equal')
plt.loglog(dt_values[:-1], diffgrid[:-1], color='k', ls='-', lw=2, marker='o');
plt.show()

#order of convergence

r = 2
h = 0.001

dt_values2 = np.array([h, r*h, r**2*h])

u_values2 = np.empty_like(dt_values2, dtype=np.ndarray)

diffgrid2 = np.empty(2)

for i, dt in enumerate(dt_values2):
    N=int(T/dt)
    t=np.linspace(0.0, T, N)
    u = np.empty((N,4))
    u[0] = np.array([v_0, theta_0, x_0, y_0])
    for n in range(N-1):
        u[n+1] = euler_step(u[n], f, dt)
        
    u_values2[i] = u
    
#calc f2-f1
diffgrid2[0] = get_diffgrid(u_values2[1], u_values2[0], dt_values2[1])
#calc f3-f2
diffgrid2[1] = get_diffgrid(u_values2[2], u_values2[1], dt_values2[2])
#calc the order of convergence
p = (log(diffgrid2[1]) - log(diffgrid2[0])) / log(r)

print diffgrid
print('The order of convergence is p = {:.3f}'.format(p));