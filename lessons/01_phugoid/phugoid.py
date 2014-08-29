# Script to plot the flight path of the phugoid using Lanchester's model.
# It uses the sign convention and formulae provided by Lanchester (1909).

import numpy
import matplotlib.pyplot as plt

def radius_of_curvature(y, yt, C):
    """Returns the radius of curvature of the flight path at any point.
    
    Parameters
    ---------
    y : float
        current depth below the reference horizontal line.
    yt : float
        initial depth below the reference horizontal line.
    C : float
        constant of integration.

    Returns
    -------
    radius : float
        radius of curvature.
    """
    #return 2./(C*(1./y)**1.5 - 2./3./yt)
    return -1*yt / (1./3 - C/2.*(yt/y)**1.5)

def rotate(x, y, xCenter, yCenter, angle):
    """Returns the new position of the point.

    Parameters
    ---------
    x : float
        previous x-position of the point
    y : float
        previous y-position of the point.
    xCenter : float
        x-location of the center of rotation.
    yCenter : float
        y-location of the center of rotation.
    angle : float
        angle of rotation

    Returns
    -------
    xCenter_new : float
        new x-location of the center of rotation.
    yCenter_new : float
        new y-location of the center of rotation.
    """
    dx = x - xCenter
    dy = y - yCenter
    xNew = dx*numpy.cos(angle) - dy*numpy.sin(angle)
    yNew = dx*numpy.sin(angle) + dy*numpy.cos(angle)
    return xCenter + xNew, yCenter + yNew

def plot_flight_path(yt, y0, theta0):
    """Plots the flight path.

    Parameters
    ---------
    yt : float
        trim height of the glider.
    y0 : float
        initial height of the glider.
    theta0 : float
        initial orientation of the glider.

    Returns
    -------
    None : None
    """
    # arrays to store the coordinates of the flight path
    N = 1000
    y = numpy.zeros(N)
    x = numpy.zeros(N)

    # set initial conditions
    y[0] = y0
    x[0] = 0.
    theta = theta0

    # calculate the constant C
    #C = numpy.sqrt(y[0])*(numpy.cos(theta) - y[0]/yt/3.)
    C = (numpy.cos(theta) - 1./3*y[0]/yt)*(y[0]/yt)**.5

    # incremental distance along the flight path
    ds = 1 
        
    #obtain the curve coordinates
    for i in range(1,N):
        normal = numpy.array([numpy.cos(theta+numpy.pi/2.), numpy.sin(theta+numpy.pi/2.)])
        R = radius_of_curvature(y[i-1], yt, C)
        center = numpy.array([x[i-1]+normal[0]*R, y[i-1]+normal[1]*R])
        dtheta = ds/R
        x[i], y[i] = rotate(x[i-1], y[i-1], center[0], center[1], dtheta)
        theta = theta + dtheta

    # generate a plot
    plt.figure(figsize=(10,6))
    plt.plot(x, -y, color = 'k', ls='-', lw=2.0, label="$z_t=\ %.1f,\\,z_1=\ %.1f,\\,\\theta_1=\ %.2f$" % (yt, y[0], theta0))
    plt.axis('equal')
    plt.title("Flight path for $C$ = %.3f" % C, fontsize=18)
    plt.xlabel("$x$", fontsize=18)
    plt.ylabel("$z$", fontsize=18)
    plt.legend()
    plt.show()

# End of File
