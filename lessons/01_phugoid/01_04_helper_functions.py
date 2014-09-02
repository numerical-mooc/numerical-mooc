import numpy
from math import sin, cos 

def f(u):
    """Returns the right hand-side of the phugoid system of equations.
    
    Parameters
    ----------
    u : array of float
        array containing the solution at time n.
        
    Returns
    -------
    dudt : array of float
        array containing the RHS given u.
    """
    ### to be implemented ###
    
    g = 1.0 # gravity in m s^{-2}, but normalized to 1.0.
    v_t = 1.0 # trim velocity in m s^{-1} : what value should be used? 
    C_D = 0.2 # to match drag coefficient
    C_L = 1.0 # which only works if C_L = 1
    
    v = u[0]
    theta = u[1]
    x = u[2]
    y = u[3]
    return numpy.array([-g*sin(theta) - C_D/C_L*g/v_t**2*v**2,
                      -g*cos(theta)/v + g/v_t**2*v,
                      v*cos(theta),
                      v*sin(theta)])


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
    ### to be implemented ###
    return u + dt * f(u)


def get_error(u_current, u_fine, dt):
    """Returns the difference between one grid and the fine one using L-1 norm.
    
    Parameters
    ----------
    u_current : array of float
        solution on the current grid.
    u_finest : array of float
        solution on the fine grid.
    dt : float
        time-increment on the current grid.
    
    Returns
    -------
    l1_error : float
        error computed in the L-1 norm.
    """
    ### to be implemented ###
    N_current = len(u_current[:,0])
    N_fine = len(u_fine[:,0])
    return dt * numpy.sum(numpy.abs(u_current[:,2]-u_fine[::N_fine/N_current,2]))
