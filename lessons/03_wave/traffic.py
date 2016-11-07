import numpy

def rho_red_light(nx, rho_max, rho_in):
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
    rho = rho_max*numpy.ones(nx)
    rho[:int(nx*3/4)] = rho_in
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
