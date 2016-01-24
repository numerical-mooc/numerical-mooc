import matplotlib.pyplot as plt
import numpy as np
from math import *

T = 38 	                         # final time
dt = 0.1                           # time increment
N = int(T/dt) + 1                  # number of time-steps
t = np.linspace(0, T, N)      # time discretization

ms=50
g=9.81
rho=1.091
r=0.5
A=pi*r**2
ve=325
CD=0.15

mp=np.zeros(t.shape)
mp[0]=100
mpdot = lambda t: -20 if t<5 else 0
for i in range(0,t.shape[0]-1):
    ti=t[i]
    mpi=mp[i]
    mp[i+1]=mpi+mpdot(ti)*dt

h=np.zeros(t.shape)
v=np.zeros(t.shape)
for i in range(0,t.shape[0]-1):
    ti=t[i]
    hi=h[i]
    vi=v[i]
    mspi=ms+mp[i]
    h[i+1]=hi+vi*dt
    v[i+1]=vi+dt*((1/mspi)*(-mspi*g-mpdot(ti)*ve-0.5*rho*vi*abs(vi)*A*CD))

plt.plot(t, h)
plt.savefig('foo.png')

it = {ti:i for i, ti in enumerate(t)}
iv = {vi:i for i, vi in enumerate(v)}
ih={hi:i for i, hi in enumerate(h)}
print("REMAINING FUEL")
print("remaining fueld mass at t=3.2", mp[it[3.2]])
print("MAXIMUM VELOCITY")
vmax=max(v)
print("max speed", vmax)
tvmax=t[iv[max(v)]]
print("time at max speed", tvmax)
hvmax=h[iv[max(v)]]
print("alt at max speed", hvmax)
print("MAXIMUM HEIGHT")
hmax=max(h)
print("max height", hmax)
print("time at max height", t[ih[hmax]])
print(h)
print("IMPACT")
iimpact=np.where(h<0)[0][0]
timpact=t[iimpact]
print("time at impact", timpact)
vimpact=v[iimpact]
print("velocity at impact", vimpact)
