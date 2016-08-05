# --Schemes for convection
import numpy 
from matplotlib import pyplot

# set the interactive mode to get an animation on screen
pyplot.ion()

# parameters
nx = 201      # number of x-intervals
nt = 80      # number of time intervals
sigma = 0.8  # CFL number
c  = 1.      # wave speed
domain = 4.0
dx = domain/(nx-1)
dt = sigma * dx/c

# initialization
x =  numpy.arange(0,domain+dx,dx)
u =  numpy.zeros(nx)
un = numpy.zeros(nx)
uzero = numpy.sin(8*x*numpy.pi)
unminus1 = numpy.zeros(nx)
unminus1 = uzero.copy()

for i in range(nx):
    if 1 <= x[i] and x[i] <= domain:
        uzero[i] = 0       
u = uzero.copy()
unminus1 = uzero.copy()

# create initial plot lines        
line1,line2 = pyplot.plot(x,u,'k.-',x,u, 'b--')
pyplot.axis([0, domain, -1, 1])
pyplot.xlabel('x')
pyplot.ylabel('u')
pyplot.show()
pyplot.title('nx='+str(nx)+', nt='+str(nt)+', dt='+str(dt), family='serif')

for i in range(1,nx):
    # backward difference for first step in time
    un[i] = unminus1[i]- sigma*( unminus1[i]- unminus1[i-1] )
    
for it in range(1,nt):
    for i in range(1,nx-1):
        # leapfrog
        u[i] = unminus1[i]- sigma*( un[i+1]- un[i-1] )
    unminus1=un.copy()
    un = u.copy()

    line1.set_ydata(u)
    line2.set_xdata(x+c*dt*(it+1))

    pyplot.pause(0.03)
    
