import numpy as np
import matplotlib.pyplot as plt

dt=0.1
m_s = 50
g = 9.81
rho = 1.091
r = 0.5
A = np.pi*r**2
v_e=325
C_D=0.15
m_po=100
m_burn_rate_value=20.
T=100.
t_end_burn=5.

N=int(T/dt)+1

time_grid = np.arange(0,T+dt,dt)
mass_burn_rate=np.zeros_like(time_grid)
mass_grid=np.ones_like(time_grid)*m_po
indices = time_grid < t_end_burn
mass_burn_rate[indices]=m_burn_rate_value
mass_grid[1:]-=np.cumsum(dt*mass_burn_rate[:-1])
# plt.plot(time_grid,mass_burn_rate)
# plt.show()

u=np.empty((N,2))
u[0]=np.array([0,0])
def f(u, i):
    v=u[1]
    mp = mass_grid[i]
    mprime = mass_burn_rate[i]
    return np.array([v, -g+mprime*v_e/(m_s+mp)-0.5*rho*v*np.abs(v)*A*C_D/(m_s+mp)])

def euler_step(u, f, dt, i):
    return u + dt*f(u, i)

for n in range(N-1):
    u[n+1] = euler_step(u[n], f, dt, n)

h = u[:,0]
v = u[:,1]
idx_negative = np.where(h<0.)[0]
idx_ground = idx_negative[0]
t_ground = time_grid[idx_ground]
# h=h[:idx_ground]
# v=v[:idx_ground]
time_grid=time_grid[:idx_ground]
print(t_ground, v[idx_ground])
print(np.max(v), np.argmax(v)*dt, h[np.argmax(v)])
print(np.max(h), np.argmax(h)*dt)
# for i, t in enumerate(time_grid):
#     print (i, t, mass_grid[i])
# plt.subplot(121)
# plt.plot(time_grid, h)
#
# plt.subplot(122)
# plt.plot(time_grid, v)
# plt.show()
