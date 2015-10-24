import numpy

def rho_red_light(nx, Rho_in, Rho_out):
    """Computes "red light" initial condition with shock

    Parameters
    ----------
    nx        : int
        Number of grid points in x
    rho_max   : float
        Maximum allowed car density
    rho_in    : float
        Density of incoming cars 

    Returns
    -------
    rho: array of floats
        Array with initial values of density
    """
    rho = Rho_in*numpy.ones(nx)
    rho[(nx-1)*3./4:] = Rho_out
    return rho
    
def rho_road_narrowing(nx, Rho_in, Rho_out):
    """Computes "road narrowing" initial condition

    Parameters
    ----------
    nx        : int
        Number of grid points in x
    rho_max   : float
        Maximum allowed car density
    rho_in    : float
        Density of incoming cars 

    Returns
    -------
    rho: array of floats
        Array with initial values of density
    """
    rho = Rho_in*numpy.ones(nx)
    rho[(nx-1)*3./4:] = Rho_out
    
    return rho

def computeF(V_max, rho_max, rho):
    """Computes flux F=V*rho

    Parameters
    ----------
    V_max  : float
        Maximum allowed velocity
    rho    : array of floats
        Array with density of cars at every point x
    rho_max: float
        Maximum allowed car density
        
    Returns
    -------
    F : array
        Array with flux at every point x
    """
    return V_max*rho*(1-rho/rho_max)
