import numpy                       
from matplotlib import pyplot                 
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

from traffic import *

# Basic initial conditions
L = 12
V_max = 100
Rho_max = 200
nx = 101
dx = L/(nx-2)

sigma = 1.0
dt = sigma*dx/V_max


def display(rho, rho_max, fun='rho', color='#003366', ls='-'):
    '''Display current state'''
    
    x = numpy.linspace(0,L,nx)
    f = numpy.zeros_like(x)
    if (fun=='rho'):
        f = rho
    elif (fun=='V'):
        f = V_max*(1-rho/rho_max)
    pyplot.plot(x, f, color=color, ls=ls, lw=2)
#    pyplot.ylim(60, 80);
    
def ftbs(T):
    """Computes the solution with the forward-time-backward-space scheme
    
    Solves the equation d_t rho + d_x F = 0 where 
    * F - traffic flux: F = V_max*rho*(1 - rho/rho_max)
    
    Produces a plot of the results
    
    Parameters
    ----------  
    T : float
        end time
        
    Returns
    -------  
    None : none
    """
    
    #setup some temporary arrays
    rho_n = rho.copy()
    F = numpy.zeros_like(rho)    
    nt = int(T/dt)
    
    for t in range(nt):  
        rho_n = rho.copy()
        
        F = flux(rho, rho_max)
        rho[1:] = rho_n[1:] - dt/dx*(F[1:] - F[:-1]) 
        rho[0] = rho_n[0]
    
    return rho

def godunov(rho, rho_max, V_max, T):
    """ Computes the solution with the Godunov scheme using the Lax-Friedrichs flux
    
    Parameters
    ----------
    rho    : array of floats
            Density at current time-step
    rho_max: float
            Maximum allowed car density
    V_max  : float
            Speed limit
    T : float
        End time
        
    Returns
    -------
    rho_n : array of floats
            Density after nt time steps at every point x
    """          
    
    #setup some temporary arrays
    rho_n = rho.copy()
    rho_plus = numpy.zeros_like(rho)
    rho_minus = numpy.zeros_like(rho)
    F = numpy.zeros_like(rho)  
    nt = int(T/dt)
    
    for t in range(1,nt):
        
        rho_plus[:-1] = rho[1:] # Can't do i+1/2 indices, so cell boundary
        rho_minus = rho.copy()  # arrays at index i are at location i+1/2
        F = 0.5 * (computeF(V_max, rho_max, rho_minus) + 
                   computeF(V_max, rho_max, rho_plus) + 
                   dx / dt * (rho_minus - rho_plus))
        rho_n[1:-1] = rho[1:-1] + dt/dx*(F[:-2] - F[1:-1])
        rho_n[0] = rho[0]
        rho_n[-1] = rho[-1]
        rho = rho_n.copy()
        
    return rho_n

# Set initial conditions
Rho_in = 35
Rho_out = 2*Rho_in
#rho = rho_red_light(nx, Rho_in, Rho_out)
rho = Rho_in*numpy.ones(nx)
#rho = rho_road_narrowing(nx, Rho_in, Rho_out)
rho_n = numpy.zeros_like(rho)

Rho_max_in = 200
Rho_max_out = 0.5*Rho_max_in
#rho_max = Rho_max_in*numpy.ones_like(rho)
rho_max = rho_road_narrowing(nx, Rho_max_in, Rho_max_out)

display(rho, rho_max, fun='V', ls='--')
#display(rho_max, color='r', ls='--')
#ftbs(0.02)
#display(color='r')
rho_n = godunov(rho, rho_max, V_max, 0.05)
display(rho_n, rho_max, fun='V', ls='-')

