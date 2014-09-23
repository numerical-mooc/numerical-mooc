#Christopher Bell
#Module 1 Assessment
#Rocket Code

import numpy as np
import matplotlib.pyplot as plt
import math

#Constants & Givens
m_s = 50 #kg
g = 9.81 #m/s2
rho = 1.091 #kg/m3
r = .5 #m
A = math.pi * (r**2) ##m2
v_e = 325 #m/s
C_D = 0.15
m_p0 = 100 #kg
m_pdot = 20 #kg/s

#Time
T = 50 #s
dt = 0.1 #s
N = int(T/dt) + 1 
t = np.linspace(0.0,T,N)

#initialize height & velociy matrix
z = np.zeros(N)
v = np.zeros(N)

#ICs
z[0] = 0.0
v[0] = 0.0

#max variables
v_max = 0.0 #m/s
z_atmaxv = 0.0 #m
z_max = 0.0 #m
v_atmaxz = 0.0 #m/s
t_vmax = 0.0 #s
t_zmax = 0.0 #s

for n in range (0,N):
    z[n+1] = z[n] + dt*v[n]
    time = n*dt
    if z[n+1] <0:
        v_impact = v[n]
        t_impact = time
        break   
    m_p = m_p0 - (m_pdot*time)
    
    if time>=5:
        m_p = 0.0
        m_pdot = 0.0
        
    v[n+1]=v[n]+dt*(((-(m_s+m_p))*g)+(m_pdot*v_e)-(0.5*rho*v[n]*abs(v[n])*A*C_D))/(m_s+m_p)

    if v[n+1] > v_max:
        v_max = v[n+1]
        z_atmaxv = z[n+1]
        t_vmax = time
    
    if z[n+1] > z_max:
        z_max = z[n+1]
        v_atmaxz = v[n+1]
        t_zmax = time

print "Max Velocity is %.2f m/s^2 at %.2f meters and %.2f seconds" %(v_max, z_atmaxv, t_vmax)
print "Max Height is %.2f meters at %.2f m/s^2 and %.2f seconds" %(z_max, v_atmaxz, t_zmax)
print "Velocity at impact is %.2f m/s^2 at %.2f seconds" %(v_impact, t_impact)
print "Fuel at 3.2 seconds is %.2f" %(m_p_32)