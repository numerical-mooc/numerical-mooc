# Script to plot the flight path of the phugoid using Lanchester's model.
# It uses the sign convention and formulae provided by Milne-Thomson (1958).

import numpy
from matplotlib import pyplot

numpy.seterr(all='ignore')
'''
see http://docs.scipy.org/doc/numpy/reference/generated/numpy.seterr.html for explanation.  ignore over/underflow errors that pop up in the radius_of_curvature function
'''

def radius_of_curvature(z, zt, C):
    """Returns the radius of curvature of the flight path at any point.
    
    Parameters
    ---------
    z : float
        current depth below the reference horizontal line.
    zt : float
        initial depth below the reference horizontal line.
    C : float
        constant of integration.

    Returns
    -------
    radius : float
        radius of curvature.
    """
    return zt / (1/3 - C/2*(zt/z)**1.5)

def rotate(x, z, xCenter, zCenter, angle):
    """Returns the new position of the point.

    Parameters
    ---------
    x : float
        previous x-position of the point
    z : float
        previous z-position of the point.
    xCenter : float
        x-location of the center of rotation.
    zCenter : float
        z-location of the center of rotation.
    angle : float
        angle of rotation

    Returns
    -------
    xCenter_new : float
        new x-location of the center of rotation.
    zCenter_new : float
        new z-location of the center of rotation.
    """
    dx = x - xCenter
    dz = z - zCenter
    # the following formulae take into account the orientation of the axes
    xNew = dx*numpy.cos(angle) + dz*numpy.sin(angle)
    zNew = -dx*numpy.sin(angle) + dz*numpy.cos(angle)
    return xCenter + xNew, zCenter + zNew

def plot_flight_path(zt, z0, theta0):
    """Plots the flight path.

    Parameters
    ---------
    zt : float
        trim height of the glider.
    z0 : float
        initial height of the glider.
    theta0 : float
        initial orientation of the glider.

    Returns
    -------
    None : None
    """
    # arrays to store the coordinates of the flight path
    N = 1000
    z = numpy.zeros(N)
    x = numpy.zeros(N)

    # set initial conditions
    z[0] = z0
    x[0] = 0.
    theta = theta0

    # calculate the constant C
    C = (numpy.cos(theta) - 1/3*z[0]/zt)*(z[0]/zt)**.5
    # incremental distance along the flight path
    ds = 1 
        
    #obtain the curve coordinates
    for i in range(1,N):
        # minus sign for the second coordinate because the z-axis points downwards
        normal = numpy.array([numpy.cos(theta+numpy.pi/2.), -numpy.sin(theta+numpy.pi/2.)])
        R = radius_of_curvature(z[i-1], zt, C)
        center = numpy.array([x[i-1]+normal[0]*R, z[i-1]+normal[1]*R])
        dtheta = ds/R
        x[i], z[i] = rotate(x[i-1], z[i-1], center[0], center[1], dtheta)
        theta = theta + dtheta

    # generate a plot
    pyplot.figure(figsize=(10,6))
    pyplot.plot(x, -z, color = 'k', ls='-', lw=2.0, label="$z_t=\ %.1f,\\,z_0=\ %.1f,\\,\\theta_0=\ %.2f$" % (zt, z[0], theta0))
    pyplot.axis('equal')
    pyplot.title("Flight path for $C$ = %.3f" % C, fontsize=18)
    pyplot.xlabel("$x$", fontsize=18)
    pyplot.ylabel("$z$", fontsize=18)
    pyplot.legend()
    pyplot.show()

# End of File
