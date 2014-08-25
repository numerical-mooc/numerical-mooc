#######################
# Solution code -- this shouldn't be distributed to students
#######################
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

D = 0.2    # Drag coefficient

def Euler_step(U,dt,f):
    "The explicit Euler method"
    return U + dt*f(U)

def phugoid(U):
    "Evaluate the right-hand side of the Phugoid model"
    v     = U[0]
    theta = U[1]
    x     = U[2]
    y     = U[3]
    
    dU = np.zeros(4)
    dU[0] = - np.sin(theta) - D * v**2
    dU[1] = v - np.cos(theta)/v
    dU[2] = v*np.cos(theta)
    dU[3] = v*np.sin(theta)
    
    return dU


T  = 10    # Final time
dt = 0.1   # Step size
t = np.arange(0,T,dt)  # Grid
U = np.zeros( (len(t),4) )  # Storage for the solution

v0 = 3.1       # Initial velocity
theta0 = 0.1   # Initial angle
x0 = 0.
y0 = 0.1
U[0] = np.array([v0, theta0, x0, y0])

for n in range(len(t)-1):
    U[n+1]=Euler_step(U[n],dt,phugoid)
    
v = U[:,0]
theta = U[:,1]
x = U[:,2]
y = U[:,3]
