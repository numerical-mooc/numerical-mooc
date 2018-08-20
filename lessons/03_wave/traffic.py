"""
Implementation of functions for the traffic model.
"""

import numpy
import ipywidgets
from matplotlib import pyplot


# Set the type and size of the font to use in Matplotlib figures.
pyplot.rcParams['font.family'] = 'serif'
pyplot.rcParams['font.size'] = 16


def rho_red_light(x, rho_max):
    """
    Computes the "red light" initial condition with shock.

    Parameters
    ----------
    x : numpy.ndarray
        Locations on the road as a 1D array of floats.
    rho_max : float
        The maximum traffic density allowed.

    Returns
    -------
    rho : numpy.ndarray
        The initial car density along the road as a 1D array of floats.
    """
    rho = rho_max * numpy.ones_like(x)
    mask = numpy.where(x < 3.0)
    rho[mask] = 0.5 * rho_max
    return rho


def flux(rho, u_max, rho_max):
    """
    Computes the traffic flux F = V * rho.

    Parameters
    ----------
    rho : numpy.ndarray
       Traffic density along the road as a 1D array of floats.
    u_max : float
        Maximum speed allowed on the road.
    rho_max : float
        Maximum car density allowed on the road.

    Returns
    -------
    F : numpy.ndarray
        The traffic flux along the road as a 1D array of floats.
    """
    F = rho * u_max * (1.0 - rho / rho_max)
    return F


def plot_traffic_density(x, rho_all, n):
    """
    Plots the traffic density along the road at a given time step.

    Parameters
    ----------
    x : numpy.ndarray
        Locations on the road as a 1D array of floats.
    rho_all : list of numpy.ndarray objects
        History of the traffic density over the time steps
        as a list of 1D arrays of floats.
    n : integer
        The time-step index of the traffic to plot.
    """
    fig, ax = pyplot.subplots(figsize=(6.0, 4.0))
    ax.set_xlabel('Distance')
    ax.set_ylabel('Traffic density')
    ax.grid()
    ax.plot(x, rho_all[n], label=f'time step {n}',
            color='C0', linestyle='-', linewidth=2)
    ax.plot(x, rho_all[0], label='initial',
            color='black', linestyle='--', linewidth=1)
    ax.legend(loc='lower right')
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(0.0, 12.0)
    pyplot.show()


def interactive_traffic(x, rho_all):
    """
    Returns an interactive plot of the traffic.

    Parameters
    ----------
    x : numpy.ndarray of floats
        Locations on the road as a 1D array of floats.
    rho_all : list of numpy.ndarray objects
        History of the traffic density over the time steps
        as a list of 1D arrays of floats.

    Returns
    -------
    w : ipywidgets.widgets.interaction.interactive
        An interactive figure of the traffic density.
    """
    nt = len(rho_all) - 1
    nt_slider = ipywidgets.IntSlider(value=0, min=0, max=nt, step=1,
                                     description='time step')
    w = ipywidgets.interactive(plot_traffic_density,
                               x=ipywidgets.fixed(x),
                               rho_all=ipywidgets.fixed(rho_all),
                               n=nt_slider)
    return w
