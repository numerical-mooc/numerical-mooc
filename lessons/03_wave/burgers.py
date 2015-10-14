import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

nx = 81
nt = 70
dx = 4.0/(nx-1)

x = np.linspace(0,4,nx)

def u_initial(nx):
    u = np.ones(nx)
    u[nx/2:]=0
    return u

def computeF(u):
    return u**2/2.

def maccormack(u, nt, dt, dx):
    un = np.zeros((nt, len(u)))
    un[:] = u.copy()
    print(un)
    ustar = u.copy()
    for n in range(1,nt):
        F = computeF(u)
        ustar = un[n]-dt/dx*(np.roll(un[n], 1) - un[n])
        Fstar = computeF(ustar)
        un[n]=0.5*(un[n]+ustar-dt/dx*(Fstar - np.roll(Fstar, -1)))
    return un

u = u_initial(nx)
sigma = .5
dt = sigma*dx

def animate(data):
    x = np.linspace(0,4,nx)
    y = data
    line.set_data(x,y)
    return line,

un = maccormack(u,nt,dt,dx)

fig=plt.figure()
ax = plt.axes(xlim=(0,4), ylim=(-.5, 2))
line, = ax.plot([], [], lw=2)

anim = animation.FuncAnimation(fig, animate, frames=un, interval=50)
plt.show()
