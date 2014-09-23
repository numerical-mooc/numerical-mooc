#Christopher Bell
#01 Bonus Notebook 2nd Order Paper Airplane Model
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
v0 = 6.5
theta0 = -0.1
x0 = 0.0
y0 = 2.0 #initial throw height

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
    
def rk2_step(u, f, dt):
    """Returns the solution at the next time step using 2nd order Runge-Kutta
    
    Parameter:
    ----------
    u : array of float
        solution at the previous time-step.
    f : function
        function to compute the RHS of the system of equations.
    dt : float
        time-increment.
    
    Returns:
    --------
    u_n_plus_1 : array of float
        solution at the next time step.
    """
    u_star = u + 0.5*dt*f(u)
    return u + dt*f(u_star)

    
def trajectory(v_0,theta_0,x_0,y_0,N):
    u = np.empty((N,4)) #made an empty array N,4 because 4 variables n steps
    u[0]= np.array([v_0, theta_0, x_0, y_0]) # IC's
    for n in range(N-1): #N-1 because already have initial step
        u[n+1] = euler_step(u[n], f, dt)
        if u[n+1,3] <= 0:
            break
    return u,n
                      
#time stepping set-up
T = 15.0   #end time
dt = 0.01    #time step size
N = int(T/dt) + 1 #total time steps

#t=np.linspace(0.0,T,N)

u_euler = np.empty((N,4))
u_rk2 = np.empty((N,4))

u_euler[0] = np.array([v0, theta0,x0,y0])
u_rk2[0] = np.array([v0,theta0,x0,y0])

for n in range(N-1):
    u_euler[n+1] = euler_step(u_euler[n], f, dt)
    u_rk2[n+1] = rk2_step(u_rk2[n], f, dt)
    
x_euler = u_euler[:,2]
y_euler = u_euler[:,3]
x_rk2 = u_rk2[:,2]
y_rk2 = u_rk2[:,3]

idx_negative_euler = np.where(y_euler<0.0)[0]
if len(idx_negative_euler)==0:
    idx_ground_euler = N-1
    print ('Euler integration has not touched ground yet!')
else:
    idx_ground_euler = idx_negative_euler[0]
    
idx_negative_rk2 = np.where(y_rk2<0.0)[0]
if len(idx_negative_rk2)==0:
    idx_ground_rk2 = N-1
    print ('Runge-Kutta integration has not touched ground yet!')
else:
    idx_ground_rk2 = idx_negative_rk2[0]

# check to see if the paths match
print('Are the x-values close? {}'.format(np.allclose(x_euler, x_rk2)))
print('Are the y-values close? {}'.format(np.allclose(y_euler, y_rk2)))

# plot the glider path
plt.figure(figsize=(10,6))
plt.subplot(121)
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(x_euler[:idx_ground_euler], y_euler[:idx_ground_euler], 'k-', label='Euler')
plt.plot(x_rk2[:idx_ground_rk2], y_rk2[:idx_ground_rk2], 'r--', label='RK2')
plt.title('distance traveled: {:.3f}'.format(x_rk2[idx_ground_rk2-1]))
plt.legend()
plt.show()

# Let's take a closer look!
plt.subplot(122)
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(x_euler, y_euler, 'k-', label='Euler')
plt.plot(x_rk2, y_rk2, 'r--', label='RK2')
plt.xlim(0,5)
plt.ylim(1.8,2.5)
plt.show()


#dist = np.zeros(100)
#
#for k in range(100):
#    for q in range(100):
#        [u,n] = trajectory(v_0[k],theta_0[q],x_0,y_0,N)
#        x_path= u[0:n,2].copy()
#        y_path= u[0:n,3].copy()
#        print y_path
#        if q == 0:
#            bestx = x_path.copy()
#            besty = y_path.copy()
#        else:
#            if len(y_path) > len(besty):
#                bestx = x_path.copy()
#                besty = y_path.copy()
#                v_best = v_0[k]
#                theta_best = theta_0[q]*(180.0/pi)
#                                