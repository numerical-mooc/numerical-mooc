import numpy as numpy
import matplotlib.pyplot as plt

def linearconv(nx):
    dx = 2./(nx-1)
    nt = 20    #nt is the number of timesteps we want to calculate
    c = 1
    sigma = .5
    
    dt = sigma*dx

    u = numpy.ones(nx) 
    u[.5/dx : 1/dx+1]=2

    un = numpy.ones(nx)

    for n in range(nt):  #iterate through time
        un = u.copy() ##copy the existing values of u into un
        for i in range(1,nx):
            u[i] = un[i]-c*dt/dx*(un[i]-un[i-1])
        
    plt.plot(numpy.linspace(0,2,nx),u)
    plt.show()

linearconv(41)
linearconv(61)
linearconv(81)
linearconv(101)
linearconv(121)
