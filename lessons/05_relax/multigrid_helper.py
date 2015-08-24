import numpy
from numba import autojit

@autojit(nopython=True)
def poisson1d_GS_SingleItr(nx, dx, p, b):
    '''
    Gauss-Seidel method for 1D Poisson eq. with Dirichlet BCs at both 
    ends. Only a single iteration is executed. **blitz** is used.
    
    Parameters:
    ----------
    nx: int, number of grid points in x direction
    dx: float, grid spacing in x
    p: 1D array of float, approximated soln. in last iteration
    b: 1D array of float, 0th-order derivative term in Poisson eq.
    
    Returns:
    -------
    p: 1D array of float, approximated soln. in current iteration
    '''
    
    for i in range(1,len(p)-1):
        p[i] = 0.5 * (p[i+1] + p[i-1] - dx**2 * b[i])
    
    return p



def RMS(p):
    '''
    Return the root mean square of p.
    
    Parameters:
    ----------
    p:   array
        
    Returns:
    -------
    Root mean square of p
    '''
    return numpy.sqrt(numpy.sum(p**2) / p.size)



def residual(dx, pn, b, r):
    '''
    Calculate the residual for the 1D Poisson equation.
    
    Parameters:
    ----------
    pn: 1D array, approximated solution at a certain iteration n
    b:  1D array, the b(x) in the Poisson eq.
    
    Return:
    ----------
    The residual r
    '''
    
    # r[0] = 0
    r[1:-1] = b[1:-1] - (pn[:-2] - 2 * pn[1:-1] + pn[2:]) / dx**2
    # r[-1] = 0
    
    return r



def full_weighting_1d(vF, vC):
    '''
    Transfer a vector on a fine grid to a coarse grid with full weighting 
    .  The number of elements (not points) of the coarse grid is 
    half of that of the fine grid.
    
    Parameters:
    ----------
    vF: 1D numpy array, the vector on the fine grid
    vC: 1D numpy array, the vector on the coarse grid,
        size(vC) = (size(vF) + 1) / 2
    
    Output: vC
    '''
    
    vC[0] = vF[0]
    vC[1:-1] = 0.25 * (vF[1:-3:2] + 2. * vF[2:-2:2] + vF[3:-1:2])
    vC[-1] = vF[-1]
    
    return vC



def interpolation_1d(vC, vF):
    '''
    Transfer a vector on a coarse grid to a fine grid by linear 
    interpolation. The number of elements (not points) of the coarse 
    grid is a half of that of the fine grid.
    
    Parameters:
    ----------
    vC: 1D numpy array, the vector on the coarse grid,
    vF: 1D numpy array, the vector on the fine grid
        size(vF) = size(vC) * 2 - 1
    
    Output: vF
    '''
    
    vF[::2] = vC[:];
    vF[1:-1:2] = 0.5 * (vC[:-1] + vC[1:])
    
    return vF
