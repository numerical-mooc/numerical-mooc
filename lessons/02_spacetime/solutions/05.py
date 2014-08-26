import numpy
import sympy
import matplotlib.pyplot as plt

from sympy import init_printing
from sympy.utilities.lambdify import lambdify
init_printing(use_latex=True)

x, nu, t = sympy.symbols('x nu t')
phi = sympy.exp(-(x-4*t)**2/(4*nu*(t+1))) + sympy.exp(-(x-4*t-2*numpy.pi)**2/(4*nu*(t+1)))
print phi

phiprime = phi.diff(x)
print phiprime

u = -2*nu*(phiprime/phi)+4
print u

ufunc = lambdify((t, x, nu), u)
print ufunc(1,4,3)


###variable declarations
nx = 101
nt = 100
dx = 2*numpy.pi/(nx-1)
nu = .07
dt = dx*nu

x = numpy.linspace(0, 2*numpy.pi, nx)
#u = numpy.empty(nx)
un = numpy.empty(nx)
t = 0

u = numpy.asarray([ufunc(t, x0, nu) for x0 in x])

plt.figure(figsize=(11,7), dpi=100)
plt.plot(x,u, marker='o', lw=2)
plt.xlim([0,2*numpy.pi])
plt.ylim([0,10]);

for n in range(nt):
    un = u.copy()
    for i in range(nx-1):
        u[i] = un[i] - un[i] * dt/dx *(un[i] - un[i-1]) + nu*dt/dx**2*\
                (un[i+1]-2*un[i]+un[i-1])
    u[-1] = un[-1] - un[-1] * dt/dx * (un[-1] - un[-2]) + nu*dt/dx**2*\
                (un[0]-2*un[-1]+un[-2])
        
u_analytical = numpy.asarray([ufunc(nt*dt, xi, nu) for xi in x])

plt.figure(figsize=(11,7), dpi=100)
plt.plot(x,u, marker='o', lw=2, label='Computational')
plt.plot(x, u_analytical, label='Analytical')
plt.xlim([0,2*numpy.pi])
plt.ylim([0,10])
plt.legend()
plt.show()
