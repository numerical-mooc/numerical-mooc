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


doit = 1
if doit == 1:
    #convection - traffic problem
    nx = 51
    L = 11.
    dx = L/(nx-1.)
    nt = 60    
    dt = .001  
    
    rho_max = 250
    V_max = 80

#    print (dt/dx)
    
    x = np.linspace(0,L,nx)
    rho = np.ones(nx)*10.
    rho[10:20] = 50.
 #   rho = np.ones(nx)
    V =  V_max *(1 - rho/rho_max)
    print 'Vmin at time zero = %f'%np.min(V)

    plotit = 0
    if plotit ==1:
        plt.figure()
        plt.plot(x,rho,'b')
        plt.figure()
        plt.plot(x,V,'b')
        plt.show()
        plt.close()

    for n in range(1,nt):
        rhon = rho.copy()
        rho[1:] = rhon[1:] - (dt/dx)*(V_max-V_max*2*rhon[1:]/rho_max)*(rhon[1:]-rhon[0:-1])
        rho[0] = 10
        V = V_max *(1 - rho/rho_max)
        print 'Time = %f [min], Vmin = %f'%(dt*n*60., np.mean(V))

        plotit = 0
        if plotit == 1:
            plt.figure()
           # plt.plot(x,rho)
            plt.plot(x,V)
            plt.show()
            plt.close()

    V = V_max *(1 - rho/rho_max)
    plotit = 1
    if plotit == 1:
        plt.figure()
        plt.plot(x,rho,'d')
     #   plt.plot(x,V,'d')
     #   plt.ylim(-1000,1000)
        plt.show()
        plt.close()




doit = 0
if doit == 1:
    #convection
    nx = 41  # try changing this number from 41 to 81 and Run All ... what happens?
    dx = 2./(nx-1)
    nt = 25    
    dt = .02  
    c = 1.      #assume wavespeed of c = 1

    u = np.ones(nx)      #numpy function ones()
    u[.5/dx : 1/dx+1]=2  #setting u = 2 between 0.5 and 1 as per our I.C.s
    print(u)



    for n in range(1,nt):  
        un = u.copy() 
        for i in range(1,nx): 
    
            u[i] = un[i]-c*dt/dx*(un[i]-un[i-1])

    plotit = 1
    if plotit == 1:
        plt.figure()
        plt.plot(np.linspace(0,2,nx), u, color='#003366', ls='--', lw=3)
        plt.ylim(0,2.5);
        plt.show()
        plt.close()

doit = 0
if doit == 1:
    nx = 41
    dx = 2./(nx-1)
    nt = 20   
    nu = 0.3   #the value of viscosity
    sigma = .2 
    dt = sigma*dx**2/nu 

    x = np.linspace(0,2,nx)

    u = np.ones(nx)      
    u[.5/dx : 1/dx+1]=2  

    un = np.ones(nx) 

    nt = 50

    u = np.ones(nx)      
    u[.5/dx : 1/dx+1]=2  

    un = np.ones(nx) 



    fig = plt.figure(figsize=(8,5))
    ax = plt.axes(xlim=(0,2), ylim=(1,2.5))
    line = ax.plot([], [], color='#003366', ls='--', lw=3)[0]

    def diffusion(i):
        line.set_data(x,u)

        un = u.copy() 
        u[1:-1] = un[1:-1] + nu*dt/dx**2*(un[2:] -2*un[1:-1] +un[0:-2]) 


    animation.FuncAnimation(fig, diffusion,
                            frames=nt, interval=100)

 #   plt.show()


doit = 0
if doit == 1:
    x, nu, t = sympy.symbols('x nu t')
    phi = sympy.exp(-(x-4*t)**2/(4*nu*(t+1))) + \
        sympy.exp(-(x-4*t-2*np.pi)**2/(4*nu*(t+1)))
    phiprime = phi.diff(x)

    u = -2*nu*(phiprime/phi)+4
    print(u)

    ufunc = lambdify((t, x, nu), u)
    print("The value of u at t=1, x=4, nu=3 is {}.".format(ufunc(1,4,3)))


    ###variable declarations
    nx = 101
    nt = 100
    dx = 2*np.pi/(nx-1)
    nu = .07
    dt = dx*nu

    x = np.linspace(0, 2*np.pi, nx)
    un = np.empty(nx)
    t = 0

    u = np.asarray([ufunc(t, x0, nu) for x0 in x])

    
    plotit = 0
    if plotit == 1:
        plt.figure(figsize=(8,5), dpi=100)
        plt.plot(x,u, color='#003366', ls='--', lw=3)
        plt.xlim([0,2*np.pi])
        plt.ylim([0,10]);
        plt.show()
        plt.close()

    for n in range(nt):
        un = u.copy()

        u[1:-1] = un[1:-1] - un[1:-1] * dt/dx * (un[1:-1] - un[:-2]) + nu*dt/dx**2*\
                        (un[2:] - 2*un[1:-1] + un[:-2])

        u[0] = un[0] - un[0] * dt/dx * (un[0] - un[-1]) + nu*dt/dx**2*\
                    (un[1] - 2*un[0] + un[-1])
        u[-1] = un[-1] - un[-1] * dt/dx * (un[-1] - un[-2]) + nu*dt/dx**2*\
                    (un[0]- 2*un[-1] + un[-2])
        
    u_analytical = np.asarray([ufunc(nt*dt, xi, nu) for xi in x])

    plotit = 1
    if plotit == 1:
        plt.figure(figsize=(8,5), dpi=100)
        plt.plot(x,u, color='#003366', ls='--', lw=3, label='Computational')
        plt.plot(x, u_analytical, label='Analytical')
        plt.xlim([0,2*np.pi])
        plt.ylim([0,10])
        plt.legend();
        plt.show()
        plot.close()

