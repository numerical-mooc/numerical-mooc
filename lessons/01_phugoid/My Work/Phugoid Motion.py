# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Phugoid Oscillation Program

# <codecell>

#Import Librarys
import numpy
import matplotlib.pyplot as ply
%matplotlib inline

# <headingcell level=2>

# Time Array Set Up

# <codecell>

T=100.0
dt=0.01
#Barba's linspace code
#N=int(T/dt)+1 #use int and add 1 to get a whole number for number of steps
#t=numpy.linspace(0.0,T,N)
#using arrange eliminates the need for N

#my arange code

t=numpy.arange(0.0,T+dt,dt) #needs to increase size but remain whole number
print t

# <headingcell level=2>

# Initial Conditions Set Up

# <codecell>

z_0=100 #intial height, m
v=10 #upward v from gust, m/s
zt=100
g=9.91 #m/s2

#create array of initial conditions
u=numpy.array([z_0,v])
#create array for changing angles
z=numpy.zeros(N)
z[0]=z_0
print u, len(z)

# <headingcell level=2>

# Euler's Method

# <codecell>

for n in range(1,N):
    u=u+dt*numpy.array([u[1],g*(1-(u[0]/zt))])
    z[n]=u[0]

# <headingcell level=2>

# Plot

# <codecell>

plt.figure(figsize=(10,4))
plt.ylim(40,160)
plt.tick_params(axis="both", labelsize = 16)
plt.xlabel("time, t", fontsize = 16)
plt.ylabel("height, z", fontsize = 16)
plt.plot(t,z);

# <headingcell level=2>

# Questions

# <markdowncell>

# 1) What happens when you have a larger gust?
# 
# 2) What about a smaller gust?
# 
# 3) What happens if there isn't a gust (v = 0)?

# <headingcell level=2>

# Answers

# <markdowncell>

# 1) The amplitude of the oscillations increases relative to the 10 m/s intial gust.
# 
# 2) The amplitude of the oscillations decrease relative to the 10 m/s intial gust.
# 
# 3) The oscillations are eliminated as the is not pertibation from steady state (level flight).

# <headingcell level=2>

# Exact Solution

# <codecell>

z_exact=v*((zt/g)**0.5)*numpy.sin((g/zt)**0.5*t)+(z_0-zt)*numpy.cos((g/zt)**0.5*t)+zt

plt.figure(figsize=(10,4))
plt.ylim(40,160)
plt.tick_params(axis="both", labelsize = 16)
plt.xlabel("time, t", fontsize = 16)
plt.ylabel("height, z", fontsize = 16)
plt.plot(t,z);
plt.plot(t, z_exact)
plt.legend(["Numerical Solution", "Exact Solution"])

# <headingcell level=2>

# Convergence

# <codecell>

#increment array
dt_values=numpy.array([0.1,0.05,0.01,0.005,0.001,0.0001])

z_values=numpy.empty_like(dt_values,dtype=numpy.ndarray) # make array using dt_values parameters and type array


for i, dt in enumerate(dt_values): #enemurate assigns index to each array location
    N=int(T/dt)+1
    t=numpy.linspace(0.0,T,N)
    u=numpy.array([z_0,v])
    z=numpy.empty_like(t)
    z[0]=z_0
    
    for n in range (0,N):
        u=u+dt*numpy.array([u[1],g*(1-u[0]/zt)])
        z[n]=u[0]
        
    z_values[i]=z.copy()

# <headingcell level=2>

# Define Error Function

# <codecell>

def get_error(z,dt):
    """Returns the error relative to analytical solution using L-1 norm.
    
    Parameters
    ----------
    z : array of float
        numerical solution.
    dt : float
        time increment.
        
    Returns
    -------
    err : float
        L_{1} norm of the error with respect to the exact solution.
    """
    N = len(z)
    t = numpy.linspace(0.0, T, N)
    
    z_exact = v*(zt/g)**.5*numpy.sin((g/zt)**.5*t)+(z_0-zt)*numpy.cos((g/zt)**.5*t)+zt
    
    return dt * numpy.sum(numpy.abs(z-z_exact))

# <headingcell level=2>

# Calculate Error

# <codecell>

error_values = numpy.empty_like(dt_values)

for i, dt in enumerate(dt_values):
    ### call the function get_error() ###
    error_values[i] = get_error(z_values[i], dt)
    
plt.figure(figsize=(10, 6))
plt.tick_params(axis='both', labelsize=14) #increase tick font size
plt.grid(True)                         #turn on grid lines
plt.xlabel('$\Delta t$', fontsize=16)  #x label
plt.ylabel('Error', fontsize=16)       #y label
plt.loglog(dt_values, error_values, 'ko-')  #log-log plot
plt.axis('equal')                      #make axes scale equally;

# <codecell>


