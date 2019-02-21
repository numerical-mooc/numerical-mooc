"""
Implementation of the functions to compute and plot the flight path of the
phugoid using Lanchester's mode.
The implementation uses the sign convention and formula provided by
Milne-Thomson (1958).
"""

import numpy
from matplotlib import pyplot


# Ignore over/underflow errors that pop up in the `radius_of_curvature`
# function.
# (See http://docs.scipy.org/doc/numpy/reference/generated/numpy.seterr.html
# for more explanations.)
numpy.seterr(all='ignore')


def radius_of_curvature(z, zt, C):
    """
    Returns the radius of curvature of the flight path at any point.

    Parameters
    ----------
    z : float
        Current depth below the reference horizontal line.
    zt : float
        Initial depth below the reference horizontal line.
    C : float
        Constant of integration.

    Returns
    -------
    radius : float
        Radius of curvature.
    """
    return zt / (1 / 3 - C / 2 * (zt / z)**1.5)


def rotate(coords, center=(0.0, 0.0), angle=0.0, mode='degrees'):
    """
    Rotates a point or an array of points
    by a given angle around a given center point.

    Parameters
    ----------
    coords :tuple
        Current x and z positions of the point(s)
        as a tuple of two floats or a tuple of two 1D arrays of floats.
    center : tuple, optional
        Center of rotation (x, z) as a tuple of two floats;
        default: (0.0, 0.0).
    angle : float, optional
        Angle of rotation;
        default: 0.0.
    mode : string, optional
        Set if angle given in degrees or radians;
        choices: ['degrees', 'radians'];
        default: 'degrees'.

    Returns
    -------
    x_new : float or numpy.ndarray
        x position of the rotated point(s)
        as a single float or a 1D array of floats.
    z_new : float or numpy.ndarray
        z position of the rotated point(s)
        as a single float or a 1D array of floats.
    """
    x, z = coords
    xc, zc = center
    if mode == 'degrees':
        angle = numpy.radians(angle)
    x_new = xc + (x - xc) * numpy.cos(angle) + (z - zc) * numpy.sin(angle)
    z_new = zc - (x - xc) * numpy.sin(angle) + (z - zc) * numpy.cos(angle)
    return x_new, z_new


def plot_flight_path(zt, z0, theta0, N=1000):
    """
    Plots the flight path of the glider.

    Parameters
    ----------
    zt : float
        Trim height of the glider.
    z0 : float
        Initial height of the glider.
    theta0 : float
        Initial orientation of the glider (in degrees).
    N : integer, optional
        Number of points used to discretize the path;
        default: 1000.
    """
    # Convert initial angle to radians.
    theta0 = numpy.radians(theta0)
    # Create arrays to store the coordinates of the flight path.
    x, z = numpy.zeros(N), numpy.zeros(N)
    # Set initial conditions.
    x[0], z[0], theta = 0.0, z0, theta0
    # Calculate the constant of integration C.
    C = (numpy.cos(theta) - 1 / 3 * z[0] / zt) * (z[0] / zt)**0.5
    # Set incremental distance along the flight path.
    ds = 1.0
    # Calculate coordinates along the path.
    for i in range(1, N):
        # We use a minus sign for the second coordinate of the normal vector
        # because the z-axis points downwards.
        normal = numpy.array([+ numpy.cos(theta + numpy.pi / 2.0),
                              - numpy.sin(theta + numpy.pi / 2.0)])
        # Get curvature radius and compute center of rotation.
        R = radius_of_curvature(z[i - 1], zt, C)
        center = numpy.array([x[i - 1], z[i - 1]]) + R * normal
        # Set angular increment.
        dtheta = ds / R
        # Calculate new position and update angle.
        x[i], z[i] = rotate((x[i - 1], z[i - 1]),
                            center=center, angle=dtheta, mode='radians')
        theta += dtheta
    # Set the font family and size to use for Matplotlib figures.
    pyplot.rcParams['font.family'] = 'serif'
    pyplot.rcParams['font.size'] = 16
    # Create Matplotlib figure.
    fig, ax = pyplot.subplots(figsize=(9.0, 4.0))
    ax.grid()
    ax.set_title(f'Flight path for $C={C:.3f}$\n' +
                 rf'($z_t={zt:.1f}$, $z_0={z0:.1f}$, ' +
                 rf'$\theta_0={numpy.degrees(theta0):.1f}^o$)')
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$z$')
    ax.plot(x, -z, linestyle='-', linewidth=2.0)
    ax.axis('scaled', adjustable='box')
    pyplot.show()
