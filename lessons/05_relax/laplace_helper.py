import numpy
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D

def L2_rel_error(p, pn):
    ''' Compute the relative L2 norm of the difference
    Parameters:
    ----------
    p : array of float
        array 1
    pn: array of float
        array 2
    Returns:
    -------
    Relative L2 norm of the difference
    '''
    return numpy.sqrt(numpy.sum((p - pn)**2)/numpy.sum(pn**2))

def plot_3D(x, y, p, elev=30, azi=45):
    '''Creates 3D projection plot with appropriate limits and viewing angle
    
    Parameters:
    ----------
    x: array of float
        nodal coordinates in x
    y: array of float
        nodal coordinates in y
    p: 2D array of float
        calculated potential field
    
    '''
    fig = pyplot.figure(figsize=(11,7), dpi=100)
    ax = fig.gca(projection='3d')
    X,Y = numpy.meshgrid(x,y)
    surf = ax.plot_surface(X,Y,p[:], rstride=1, cstride=1, cmap=cm.viridis,
            linewidth=0, antialiased=False)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    ax.view_init(elev,azi)

def p_analytical(x, y):
    '''Returns the analytical solution for the given Laplace Problem on a grid
    with coordinates x and y
    
    Parameters:
    ----------
    xL array of float
        Nodal coordinates in x
    y: array of float
        Nodal coordinates in y
        
    Returns:
    -------
    pxy: 2D array of float
        Potential distribution analytical solution
    
    '''
    X, Y = numpy.meshgrid(x,y)
    pxy = numpy.sinh(1.5*numpy.pi*Y / x[-1]) /\
    (numpy.sinh(1.5*numpy.pi*y[-1]/x[-1]))*numpy.sin(1.5*numpy.pi*X/x[-1])
    
    return pxy
