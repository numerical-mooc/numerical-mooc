import numpy                       
from matplotlib import pyplot                 
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

# Basic initial conditions
L = 20
nx = 81
dx = L/(nx-1)
dt = 2e-4
gamma = 1.4


def display(x, u, fun='rho', color='#003366', ls='-'):
    '''Display current state'''
    
    f = numpy.zeros_like(u)
    if (fun == 'rho'):
        f = u[:,0]
    elif (fun == 'V'):
        f = u[:,1]/u[:,0]
    elif (fun == 'p'):
        f = (gamma-1)*(u[:,2] - 0.5*u[:,1]**2/u[:,0])
    pyplot.plot(x, f, color=color, ls=ls, lw=2)
#    pyplot.ylim(60, 80)
    
def init_conditions():
    """Computes initial conditions
    
    Parameters
    ----------
    None
        
    Returns
    -------
    u : 2d array of floats
        Array with conserved variables at at every point x
    """
    
    u = numpy.zeros((nx, 3))
    u_l = [1., 0., 100.]    # right
    u_r = [0.125, 0., 10.]  # left
    u[:] = u_r
    u[:nx//2,:] = u_l
    
    return u
    
    
def computeF(u):
    """Computes Eiler's flux

    Parameters
    ----------
    u : array of floats
        Array with conserved variables at one point x
        
    Returns
    -------
    F : array of floats
        Array with flux at one point x
    """
    
    u1 = u[:,0]
    u2 = u[:,1]
    u3 = u[:,2] 
    A = u2**2/u1
    F = numpy.zeros_like(u)
    F[:,0] = u2
    F[:,1] = A + (gamma-1)*(u3 - 0.5*A)
    F[:,2] = (u3 + (gamma-1)*(u3 - 0.5*A))*u2/u1
    
    return F

def richtmyer(u, T):
    """ Computes the solution with the Richtmyer scheme
    
    Parameters
    ----------
    u : array of floats
        Array with conserved variables at every point x
    T : float
        End time
        
    Returns
    -------
    u : array of floats
        Array with conserved variables at the moment T at every point x
    """          
    
    #setup some temporary arrays
    ustar = u.copy()
    u_n = u.copy()
    F = numpy.zeros_like(u)  
    nt = int(T/dt)
    
    for t in range(nt):
        F = computeF(u)
        ustar[:-1] = 0.5*(u[1:] + u[:-1]) - 0.5*dt/dx*(F[1:] - F[:-1])     
        F = computeF(ustar)
        u_n[1:] = u[:-1] - dt/dx*(F[1:] - F[:-1])
        u_n[-1] = u[-1]
        u = u_n.copy()
        
#        rho_plus[:-1] = rho[1:] # Can't do i+1/2 indices, so cell boundary
#        rho_minus = rho.copy()  # arrays at index i are at location i+1/2
#        F = 0.5 * (computeF(V_max, rho_max, rho_minus) + 
#                   computeF(V_max, rho_max, rho_plus) + 
#                   dx / dt * (rho_minus - rho_plus))
#        rho_n[1:-1] = rho[1:-1] + dt/dx*(F[:-2] - F[1:-1])
#        rho_n[0] = rho[0]
#        rho_n[-1] = rho[-1]
#        rho = rho_n.copy()
        
    return u_n

x = numpy.linspace(-L/2,L/2,nx)

u = init_conditions()
display(x, u, 'rho', ls='--')
u_n = richtmyer(u, 0.001)
display(x, u_n, 'rho', ls='-')

i = numpy.where(x==2.5)
print(u_n)


