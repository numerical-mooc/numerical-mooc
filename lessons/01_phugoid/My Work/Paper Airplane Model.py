#Christopher Bell
#01-03 Paper Airplane Model
#derivation of equations can be found in class notebook

from math import sin, cos, log, ceil, pi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family']= 'serif'
rcParams['font.size']= 16

# Constants
g = 9.81 # m/s2
v_t = 4.9 #trim velocity m/s
C_D = 1/5.0
C_L = 1.0 #C_L/C_D = L/D --> 5

#####IC's
v_0 = np.linspace(v_t,1.5*v_t,100)
theta_0 = np.linspace(-pi/4,pi/4.0,100)
x_0 = 0.0
y_0 = 1.5 #initial throw height

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
    

def trajectory(v_0,theta_0,x_0,y_0,N):
    u = np.empty((N,4)) #made an empty array N,4 because 4 variables n steps
    u[0]= np.array([v_0, theta_0, x_0, y_0]) # IC's
    for n in range(N-1): #N-1 because already have initial step
        u[n+1] = euler_step(u[n], f, dt)
        if u[n+1,3] <= 0:
            break
    return u,n
                      
#time stepping set-up
T = 100.0   #end time
dt = 0.1    #time step size
N = int(T/dt) + 1 #total time steps
t=np.linspace(0.0,T,N)

dist = np.zeros(100)

for k in range(100):
    for q in range(100):
        [u,n] = trajectory(v_0[k],theta_0[q],x_0,y_0,N)
        x_path= u[0:n,2].copy()
        y_path= u[0:n,3].copy()
        print y_path
        if q == 0:
            bestx = x_path.copy()
            besty = y_path.copy()
        else:
            if len(y_path) > len(besty):
                bestx = x_path.copy()
                besty = y_path.copy()
                v_best = v_0[k]
                theta_best = theta_0[q]*(180.0/pi)
                                
plt.figure()
plt.grid(True)
plt.xlabel(r'x (m)', fontsize=18)
plt.ylabel(r'y (m)', fontsize=18)
plt.title('Airplane Trajectory v_0 = %.2f m/s theta_0 = %.2f degrees' %(v_best,theta_best), fontsize=14)
plt.plot(bestx,besty, 'k-', lw=2);
plt.show()