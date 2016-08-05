import numpy                       
from matplotlib import pyplot                 
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

L = 11
V_max = 136
rho_max = 250
nx = 51
dx = L/(nx-1)
dt = 0.001

# Set initial conditions
x = numpy.linspace(0,L,nx)
rho_1 = 10
rho_2 = 150
rho = numpy.ones(nx)*rho_1
rho[10:20] = rho_2
rho_n = numpy.ones(nx)

def ave(A):
    '''Calculate average'''
    ave = 0
    for a in A:
        ave += a
    return ave/len(A)
    
def flux(rho):
    '''Calculate traffic flux'''
    return V_max*rho*(1 - rho/rho_max)

def init():
    '''Set initial conditions'''
    x = numpy.linspace(0,L,nx)
    rho0 = numpy.ones(nx)*rho_1
    rho0[10:20] = rho_2

    V0 = numpy.asarray([1000/3600*V_max*(1-rho/rho_max) for rho in rho0])
    
    pyplot.plot(x, rho0, color='#003366', ls='--', lw=2)
#    pyplot.plot(x, rho0, color='b', ls='--', lw=2)
#    pyplot.ylim(60, 80);
    print (min(V0))
    
    return (x, rho0)   
    
def conv(T):
    """Solve the non-linear convection equation for traffic flow
    
    Solves the equation d_t rho + d_x F = 0 where 
    * F - traffic flux: F = V_max*rho*(1 - rho/rho_max)
    
    Produces a plot of the results
    
    Parameters
    ----------
    
    T : float
        end time
        
    Returns
    -------
    
    None : none
    """   
    nt = int(T/dt)
    for n in range(nt):  
        rho_n = rho.copy()
        rho[1:] = rho_n[1:] - dt/dx*(flux(rho_n[1:]) - flux(rho_n[0:-1])) 
        rho[0] = rho_1
    
    V = numpy.asarray([1000/3600*V_max*(1-rho_i/rho_max) for rho_i in rho]) 
    print(ave(V))
    print(min(V))
    
    pyplot.plot(x, rho, color='k', ls='-', lw=2)
#    pyplot.ylim(0,60);

init()
conv(0.05)


#from JSAnimation.IPython_display import display_animation
#from matplotlib import animation

#nt = 100
#fig = pyplot.figure(figsize=(6,4))
#ax = pyplot.axes(xlim=(0,11), ylim=(10,160))
#line = ax.plot([], [], color='#003366', ls='--', lw=3)[0]
##ax.legend(['Computed','Analytical'])
#
#def make_frame(i):
#    '''Make frame for animation'''
#    line.set_data(x, rho)
#    
#    rho_n = rho.copy()
#    rho[0] = rho_1
#    rho[1:] = rho_n[1:] - dt/dx*(flux(rho_n[1:]) - flux(rho_n[0:-1])) 
#    
#animation.FuncAnimation(fig, make_frame, frames=nt, interval=100)
