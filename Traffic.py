# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:49:40 2010

@author: jdensmor

"""
import sys
import os

import matplotlib.pyplot as plt
import matplotlib as mplib
#from subprocess import Popen
#import Image_PIL as JMD
import numpy as np
from scipy import stats
import scipy.integrate as inte
from scipy.optimize import newton, fsolve
from scipy import linspace, polyval, polyfit, sqrt, stats, randn

import sympy
from sympy.utilities.lambdify import lambdify

#from JSAnimation.IPython_display import display_animation
#from matplotlib import animation

pub = 0
if pub == 1:
    scale = 2.
    fig_width_pt = 246.0  # Get this from LaTeX using \showthe\columnwidth
    inches_per_pt = 1.0/72.27               # Convert pt to inch
    golden_mean = (np.sqrt(5)-1.0)/2.0         # Aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    fig_height = fig_width*golden_mean      # height in inches
    #   print 'Figure width = %f' % fig_width
    fig_size =  [scale *fig_width,scale *fig_height]
    params = {'backend': 'ps',
              'font.family': 'sans-serif',
              'font.sans-serif':'Arial',
              'axes.labelsize': 12,
              'text.fontsize': 12,
              'legend.fontsize': 12,
              'xtick.labelsize': 12,
              'savefig.dpi': 300,
              'ps.usedistiller':True,
              'ps.distiller.res':6000,
              'xtick.fontname':'Arial',
              'ytick.fontname':'Arial',
              'ytick.labelsize': 12,
              'text.usetex': False,
              'lines.linewidth':2,
    #   'text.dvipnghack':True,
              'figure.figsize': fig_size}
    mplib.rcParams.update(params)

np.set_printoptions(edgeitems=10,linewidth=300)



'''
Part A
'''
doit = 0
if doit == 1:
    #convection - traffic problem
    nx = 51
    L = 11.
    dx = L/(nx-1.)
    nt = 60   
    dt = .001  

    rho_max = 250.
    V_max = 80.

#    print (dt/dx)
    x = np.linspace(0,L,nx)
    rho = np.ones(nx)*10.
    rho[10:20] = 50.
 #   rho = np.ones(nx)
    V =  V_max *(1 - rho/rho_max)
    F = V * rho
    print 'Vmin at time zero = %f'%(np.min(V)*1000./3600.)

    plotit = 0
    if plotit ==1:
        plt.figure()
        plt.plot(x,rho,'b')
        plt.figure()
        plt.plot(x,V,'b')
        plt.figure()
        plt.plot(x,F,'b')
        plt.show()
        plt.close()

    for n in range(1,nt):
        rhon = rho.copy()
        rho[1:] = rhon[1:] - (dt/dx)*(V_max-V_max*2*rhon[1:]/rho_max)*(rhon[1:]-rhon[0:-1])
        rho[0] = 10
        V = V_max *(1 - rho/rho_max)
        print 'Time = %f [min], Vmin = %f m/s'%(dt*n*60., (np.min(V)*1000./3600.))

        plotit = 0
        if plotit == 1:
            plt.figure()
           # plt.plot(x,rho)
            plt.plot(x,V)
            plt.show()
            plt.close()

    plotit = 1
    if plotit == 1:
        plt.figure()
        plt.plot(x,rho,'d')
     #   plt.plot(x,V,'d')
        plt.show()
        plt.close()


'''
Part B
'''
doit = 1
if doit == 1:
    #convection - traffic problem
    nx = 51
    L = 11.
    dx = L/(nx-1.)
    nt = 60   
    dt = .001  

    rho_max = 250.
    V_max =136.

    x = np.linspace(0,L,nx)
    rho = np.ones(nx)*20.
    rho[10:20] = 50.
 #   rho = np.ones(nx)
    V =  V_max *(1 - rho/rho_max)
    F = V * rho
    print 'Vmin at time zero = %f'%(np.min(V)*1000./3600.)

    plotit = 0
    if plotit ==1:
        plt.figure()
        plt.plot(x,rho,'b')
        plt.figure()
        plt.plot(x,V,'b')
        plt.figure()
        plt.plot(x,F,'b')
        plt.show()
        plt.close()

    for n in range(1,nt):
        rhon = rho.copy()
        rho[1:] = rhon[1:] - (dt/dx)*(V_max-V_max*2*rhon[1:]/rho_max)*(rhon[1:]-rhon[0:-1])
        rho[0] = 10
        V = V_max *(1 - rho/rho_max)
        print 'Time = %f [min], Vmean = %f m/s, VMin = %f m/s'%(dt*n*60.,\
                                (np.mean(V)*1000./3600.),(np.min(V)*1000./3600.))



        plotit = 0
        if plotit == 1:
            plt.figure()
           # plt.plot(x,rho)
            plt.plot(x,V)
            plt.show()
            plt.close()
