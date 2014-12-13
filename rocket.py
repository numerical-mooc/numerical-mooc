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


def f(u,mp,mpdot):

    g = 9.8 
    rho = 1.091
    A = np.pi * 0.5**2.
    ve = 325.
    Cd = 0.15
    ms = 50.

    h = u[0]
    v = u[1]
    return np.array([v, -g + mpdot/(mp+ms) * ve - (0.5*rho*v*np.abs(v)*A*Cd)/(mp+ms)])

def euler_step(u,f,dt,mp,mpdot):

    return u + dt*f(u,mp,mpdot)
   

g = 9.8 
rho = 1.091
A = np.pi * 0.5**2.
ve = 325
Cd = 0.15
mp0 = 100.

Tmax = 50.
dt = 0.1
N = int(Tmax/dt) + 1
t = np.linspace(0.,Tmax,N)


mpdot = np.zeros(N)
mp = np.zeros(N)
#mp[0] = mp0

inn = np.where(t == 5.0)[0][0]
print t[inn]

for i in range(0,inn):
    mpdot[i] = 20.

plotit = 0
if plotit == 1:
    plt.figure()
    plt.plot(t,mpdot)
    plt.show()
    plt.close()

for i in range(0,N-1):

#    print i,i*dt,inte.trapz(mpdot[0:i+1],x=t[0:i+1])
    mp[i] = mp0 - inte.trapz(mpdot[0:i+1],x=t[0:i+1])

innb = np.where(t >= 5.0)[0][0]

for i in range(innb,N):
    mp[i] = 0

t32 = np.where(t == 3.2)[0][0]
print ' t = %f, mp = %f' %(t[t32],mp[t32])

plotit = 0
if plotit == 1:
    plt.figure()
    plt.plot(t,mp)
    plt.ylim(0,110)
    plt.xlim(0,10)
    plt.show()
    plt.close()


u = np.empty((N,2))
u[0] = np.array([0,0])



# Solve

for n in range(0,N-1):
    u[n+1] = euler_step(u[n],f,dt,mp[n],mpdot[n])

v = u[:,1]
h = u[:,0]

vmax = np.max(v)
vmax_in = np.where(v == vmax)[0][0]
tmax = t[vmax_in]
print ' Max velocity = %f m/s, at %f sec'%(vmax,tmax)
print 'h= %f [m]'%h[vmax_in]

hmax = np.max(h)
hmax_in = np.where(h == hmax)[0][0]
print 'max h = %f [m] at %f [sec]'%(hmax,t[hmax_in])

h0_in = np.where(h < 0) [0][0]
h0 = h[h0_in]
t0 = t[h0_in]
vimpact = v[h0_in]

print 'impact at %f [sec], with height = %f [m], velocity = %f'%(t0,h0,vimpact) 

plotit = 1
if plotit == 1:
    plt.figure()
    plt.plot(t,u[:,0])
    plt.xlim(0,Tmax)

    plt.figure()
    plt.plot(t,u[:,1])
   # plt.ylim(0,200)
    plt.xlim(0,Tmax)

    plt.show()
    plt.close()
