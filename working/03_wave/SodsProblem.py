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


def display(x, u, index=0, fun='rho', color='#003366', ls='-'):
    '''Display current state'''
    
    f = numpy.zeros_like(u)
    if (fun == 'rho'):
        f = u[:,0]
    elif (fun == 'v'):
        f = u[:,1]/u[:,0]
    elif (fun == 'p'):
        f = (gamma-1)*(u[:,2] - 0.5*u[:,1]**2/u[:,0])
    
    pyplot.plot(x, f, color=color, ls=ls, lw=2)
#    pyplot.ylim(60, 80)
    print(f[index])
    
def conserv_var(rho, u, p):
    """Computes conservative variables"""
    
    U = []
    U.append(rho)   # density
    U.append(rho*u) # momentum
    eT = p/(gamma-1)/rho + 0.5*u**2
    U.append(rho*eT)
    
    return U
    
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
    u_l = conserv_var(1.0, 0., 1e5)    # right
    u_r = conserv_var(0.125, 0., 1e4)   # left
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
    u_n = u.copy()
    F = numpy.zeros_like(u) 
    ustar = numpy.zeros((nx-1, 3))
    Fstar = numpy.zeros((nx-1, 3))
    nt = int(T/dt)
    
    for t in range(nt):
        F = computeF(u)
        ustar[:] = 0.5*(u[1:] + u[:-1]) - 0.5*dt/dx*(F[1:] - F[:-1])     
        Fstar = computeF(ustar)
        u_n[1:-1] = u[1:-1] - dt/dx*(Fstar[1:] - Fstar[:-1])
#        u_n[0] = u[0]
#        u_n[-1] = u[-1]
        u = u_n.copy()
        
    return u_n

x = numpy.linspace(-L/2,L/2,nx)
i = numpy.where(x==2.5)

u = init_conditions()
#display(x, u, i, 'v', ls='--')
u_n = richtmyer(u, 0.01)
display(x, u_n, i, 'rho', ls='-')

#print(u_n[i])


